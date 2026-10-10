#!/usr/bin/env python3
"""Fetch PHOTO_CANDIDATES declared by expansion modules, serially and politely,
resize to ≤400 px, save to static/photos/<slug>.jpg and write photo_url into the
entity's DB metadata (so export_static.py carries it into the JSON).

Usage:  cd ~/intel-console && python3 tools/fetch_candidate_photos.py seed.expansion_a seed.expansion_b ...
Skips entities that already have a photo. 2.5 s between requests.
"""

import importlib
import io
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
PHOTOS = os.path.join(ROOT, "static", "photos")
DB = os.path.join(ROOT, "data", "intel.db")
UA = "IntelConsolePhotoFetch/1.0 (https://qav2.github.io/intel-console/; contact: contact@qualia-algebra.com)"


def slug(name):
    s = unicodedata.normalize("NFD", name)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^a-z0-9\s]", "", s)
    return re.sub(r"\s+", "_", s.strip())


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), r.headers.get("Content-Type", "")


def commons_direct(url):
    """Turn a Commons 'File:' page URL into the direct upload URL via the API."""
    m = re.search(r"commons\.wikimedia\.org/wiki/(File:[^?#]+)", url)
    if not m:
        return url, None
    title = urllib.parse.unquote(m.group(1))
    api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url|mime", "format": "json"})
    data, _ = fetch(api)
    for p in json.loads(data)["query"]["pages"].values():
        ii = p.get("imageinfo")
        if ii:
            return ii[0]["url"], ii[0]["mime"]
    return url, None


IMG_EXT = (".jpg", ".jpeg", ".png", ".svg")


def wikipedia_pageimage(name):
    """Most reliable fallback for people/orgs: the lead image of the English
    Wikipedia article (follows redirects)."""
    api = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "query", "titles": name, "prop": "pageimages", "piprop": "original",
         "redirects": 1, "format": "json"})
    data, _ = fetch(api)
    for p in json.loads(data)["query"]["pages"].values():
        orig = p.get("original")
        if orig and orig.get("source"):
            return orig["source"], None, "wikipedia:" + p.get("title", name)
    return None, None, None


def unthumb(url):
    """Turn a Commons /thumb/ URL into the original-file URL."""
    m = re.match(r"(https://upload\.wikimedia\.org/wikipedia/commons)/thumb/([0-9a-f]/[0-9a-f]{2}/[^/]+)/.*", url)
    return f"{m.group(1)}/{m.group(2)}" if m else url


def search_fallback(name, etype):
    """Last resort: a Commons search for the entity name; the FULL name must appear
    in the file title (surname-only matching picked a Civil War captain for a CEO)."""
    key = name.lower()
    q = f'"{name}"' + (" portrait" if etype == "person" else " logo")
    api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "query", "list": "search", "srnamespace": 6, "srsearch": q, "srlimit": 10, "format": "json"})
    data, _ = fetch(api)
    hits = [h["title"] for h in json.loads(data)["query"]["search"]]
    time.sleep(2.5)
    for t in hits:
        tl = t.lower()
        if not tl.endswith(IMG_EXT):
            continue
        if key in tl:
            api2 = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(
                {"action": "query", "titles": t, "prop": "imageinfo", "iiprop": "url|mime", "format": "json"})
            d2, _ = fetch(api2)
            for p in json.loads(d2)["query"]["pages"].values():
                ii = p.get("imageinfo")
                if ii:
                    return ii[0]["url"], ii[0]["mime"], t
    return None, None, None


def rasterize_svg(data):
    tmp_svg, tmp_png = "/tmp/_cand.svg", "/tmp/_cand.png"
    with open(tmp_svg, "wb") as f:
        f.write(data)
    subprocess.run([os.path.expanduser("~/.local/bin/cairosvg"), tmp_svg, "-o", tmp_png, "--output-width", "1000"],
                   check=True, capture_output=True, timeout=120)
    return Image.open(tmp_png).convert("RGBA")


def to_jpeg(im, is_logo):
    if is_logo or im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bbox = im.getbbox()
        if bbox:
            im = im.crop(bbox)
        canvas_side = 400
        inner = canvas_side - 60
        im.thumbnail((inner, inner), Image.LANCZOS)
        bg = Image.new("RGB", (canvas_side, canvas_side), (255, 255, 255))
        bg.paste(im, ((canvas_side - im.width) // 2, (canvas_side - im.height) // 2), im)
        return bg
    im = im.convert("RGB")
    im.thumbnail((400, 400), Image.LANCZOS)
    return im


def main():
    mods = [a for a in sys.argv[1:] if not a.startswith("--")]
    db = sqlite3.connect(DB)
    ok, skipped, failed = [], [], []
    for modname in mods:
        mod = importlib.import_module(modname)
        cands = getattr(mod, "PHOTO_CANDIDATES", {})
        types = {e["name"]: e["entity_type"] for e in getattr(mod, "ENTITIES", [])}
        for name, url in cands.items():
            row = db.execute("SELECT id, entity_type, metadata FROM entities WHERE name = ?", (name,)).fetchone()
            if not row:
                failed.append((name, "entity not in DB"))
                continue
            eid, etype, meta_raw = row
            try:
                meta = json.loads(meta_raw or "{}")
            except Exception:  # noqa
                meta = {}
            if meta.get("photo_url"):
                skipped.append(name)
                continue
            fname = slug(name) + ".jpg"
            try:
                direct, mime = commons_direct(unthumb(url))
                time.sleep(2.5)
                try:
                    data, ctype = fetch(direct)
                except urllib.error.HTTPError as he:
                    if he.code not in (400, 403, 404):
                        raise
                    # 1) Wikipedia lead image  2) Commons full-name search
                    direct, mime, title = wikipedia_pageimage(name)
                    time.sleep(2.5)
                    if not direct:
                        direct, mime, title = search_fallback(name, etype)
                    if not direct:
                        raise RuntimeError(f"{he.code} and no Wikipedia/Commons fallback")
                    print(f"       (fallback → {title})")
                    time.sleep(2.5)
                    data, ctype = fetch(direct)
                mime = mime or ctype
                if "svg" in (mime or "") or direct.lower().endswith(".svg"):
                    im = rasterize_svg(data)
                else:
                    im = Image.open(io.BytesIO(data))
                is_logo = etype != "person"
                out = to_jpeg(im, is_logo)
                if out.width < 60 or out.height < 60:
                    raise RuntimeError("image too small")
                out.save(os.path.join(PHOTOS, fname), "JPEG", quality=90)
                meta["photo_url"] = f"/static/photos/{fname}"
                db.execute("UPDATE entities SET metadata = ?, updated_at = datetime('now') WHERE id = ?",
                           (json.dumps(meta), eid))
                db.commit()
                ok.append((name, fname))
                print(f"  ok   {name:40s} → {fname}")
            except Exception as e:  # noqa
                failed.append((name, str(e)[:100]))
                print(f"  FAIL {name:40s} {e}")
            time.sleep(2.5)
    db.close()
    print(f"\n{len(ok)} fetched, {len(skipped)} already had photos, {len(failed)} failed")
    for f in failed:
        print("  ", f)


if __name__ == "__main__":
    main()
