#!/usr/bin/env python3
"""Regenerate broken logo photos (black-on-black / sliver wordmarks) from Wikimedia
Commons originals, composited onto a white square so they read inside circular nodes.

Also swaps a handful of wrong-subject images and removes photos that showed the
wrong person (those entities fall back to the type icon).

Usage:  cd ~/intel-console && python3 tools/fix_logo_photos.py [--only name.jpg,...]
Idempotent; polite to the Commons API (2.5 s between calls; custom User-Agent).
"""

import io
import json
import os
import sqlite3
import subprocess
import sys
import time
import urllib.parse
import urllib.request

from PIL import Image, ImageChops

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTOS = os.path.join(ROOT, "static", "photos")
DB = os.path.join(ROOT, "data", "intel.db")
UA = "IntelConsolePhotoFix/1.0 (https://qav2.github.io/intel-console/; contact: contact@qualia-algebra.com)"
CANVAS = 400
PAD = 34

# target file → Commons title. "logo" = composite on white; "photo" = plain resize.
LOGOS = {
    "blackrock.jpg":          "File:BlackRock wordmark.svg",
    "palantir.jpg":           "File:Palantir Technologies logo.svg",
    "osf.jpg":                "File:Open Society Foundations Logo.svg",
    "ford_foundation.jpg":    "File:Logo of the Ford Foundation.svg",
    "scl_group.jpg":          "File:SCL Group logo.png",
    "halliburton.jpg":        "File:Halliburton logo.svg",
    "general_dynamics.jpg":   "File:General Dynamics logo.svg",
    "sri_international.jpg":  "File:SRI International logo.svg",
    "bnd.jpg":                "File:Logo of the Bundesnachrichtendienst (2024).svg",
    "booz_allen_hamilton.jpg":"File:Booz Allen Hamilton logo.svg",
    "brookings.jpg":          "File:Brookings logo small.svg",
    "club_of_rome.jpg":       "File:Club of Rome Logo.svg",
    "glencore.jpg":           "File:Glencore logo.svg",
    "heritage_foundation.jpg":"File:The Heritage Foundation.svg",
    "jpmorgan_chase.jpg":     "File:Logo of JPMorganChase 2024.svg",
    "lockheed_martin.jpg":    "File:Lockheed Martin logo (2).svg",
    "news_corp.jpg":          "File:News Corp logo 2013.svg",
    "northrop_grumman.jpg":   "File:Northrop Grumman logo blue-on-clear 2020.svg",
    "paramount.jpg":          "File:Paramount Pictures 2022 (Blue).svg",
    "purdue_pharma.jpg":      "File:Purdue Pharma logo.svg",
    "disney.jpg":             "File:The Walt Disney Company Logo.svg",
    "thule_society.jpg":      "File:Thule-Gesellschaft.jpg",
    "trilateral.jpg":         "File:Trilateral.svg",
    "syngenta.jpg":           "File:Syngenta Logo.svg",
    "usamriid.jpg":           "File:Logo of the United States Army Medical Research Institute of Infectious Diseases.svg",
    "world_bank.jpg":         "File:The World Bank logo.svg",
    "cargill.jpg":            "File:Cargill logo.svg",          # was Cargills (Ceylon) — wrong company
}
PHOTOS_SWAP = {
    "hugh_grant.jpg":         "File:Hugh Grant Monsanto.jpg",   # was the actor; entity is Monsanto's CEO
}
# Wrong-subject images: delete file + unlink from entity (falls back to type icon)
REMOVE = {
    "eric_davis.jpg":            "Eric Davis",            # baseball player, not the AAWSAP physicist
    "david_atlee_phillips.jpg":  "David Atlee Phillips",  # CIA seal standing in for a person
    "david_fravor.jpg":          "David Fravor",          # FLIR video still, not the pilot
    "ryan_graves.jpg":           "Ryan Graves",           # NHL player, not the Navy pilot
    "kissinger_associates.jpg":  "Kissinger Associates",  # second copy of Kissinger's face
    "gates_foundation.jpg":      None,                    # 1 KB orphan, unused
}


def api(params):
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def commons_url(title):
    d = api({"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url|mime", "format": "json"})
    pages = d["query"]["pages"]
    for p in pages.values():
        ii = p.get("imageinfo")
        if ii:
            return ii[0]["url"], ii[0]["mime"]
    raise RuntimeError(f"no imageinfo for {title}")


def rasterize_svg(svg_bytes, width=1200):
    tmp_svg = "/tmp/_logo_in.svg"
    tmp_png = "/tmp/_logo_out.png"
    with open(tmp_svg, "wb") as f:
        f.write(svg_bytes)
    for cmd in (
        [os.path.expanduser("~/.local/bin/cairosvg"), tmp_svg, "-o", tmp_png, "--output-width", str(width)],
        ["convert", "-background", "none", "-density", "300", tmp_svg, "-resize", f"{width}x{width}", tmp_png],
    ):
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=120)
            return Image.open(tmp_png).convert("RGBA")
        except Exception as e:  # noqa
            last = e
    raise RuntimeError(f"svg rasterization failed: {last}")


def to_white_square(im):
    im = im.convert("RGBA")
    # crop to the CONTENT bbox: pixels that are visible AND not (near-)white —
    # many Commons SVGs carry an opaque white or oversized transparent stage.
    r, g, b, a = im.split()
    lum = Image.merge("RGB", (r, g, b)).convert("L")
    dark = lum.point(lambda v: 255 if v < 240 else 0)
    vis = a.point(lambda v: 255 if v > 20 else 0)
    content = ImageChops.multiply(dark, vis)
    bbox = content.getbbox() or im.getbbox()
    if bbox:
        im = im.crop(bbox)
    # if the logo is essentially white-on-transparent, it would vanish on white → flip to dark
    px = im.convert("RGBA").resize((64, 64)).getdata()
    opaque = [p for p in px if p[3] > 40]
    if opaque:
        lum = sum(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2] for p in opaque) / len(opaque)
        if lum > 235:
            r, g, b, a = im.split()
            inv = Image.merge("RGB", (r.point(lambda v: 255 - v), g.point(lambda v: 255 - v), b.point(lambda v: 255 - v)))
            im = Image.merge("RGBA", (*inv.split(), a))
    inner = CANVAS - 2 * PAD
    im.thumbnail((inner, inner), Image.LANCZOS)
    canvas = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    canvas.paste(im, ((CANVAS - im.width) // 2, (CANVAS - im.height) // 2), im)
    return canvas


def load_any(data, mime):
    if mime == "image/svg+xml":
        return rasterize_svg(data)
    return Image.open(io.BytesIO(data)).convert("RGBA")


def main():
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    done, failed = [], []

    for target, title in list(LOGOS.items()) + list(PHOTOS_SWAP.items()):
        if only and target not in only:
            continue
        try:
            url, mime = commons_url(title)
            time.sleep(2.5)
            data = fetch(url)
            im = load_any(data, mime)
            if target in LOGOS:
                out = to_white_square(im)
            else:
                out = im.convert("RGB")
                out.thumbnail((400, 400), Image.LANCZOS)
            out.save(os.path.join(PHOTOS, target), "JPEG", quality=92)
            done.append(target)
            print(f"  ok  {target:28s} ← {title}")
        except Exception as e:  # noqa
            failed.append((target, title, str(e)[:120]))
            print(f"  FAIL {target:27s} ← {title}: {e}")
        time.sleep(1.5)

    # ---- removals ----
    db = sqlite3.connect(DB)
    for fname, ent_name in REMOVE.items():
        if only and fname not in only:
            continue
        p = os.path.join(PHOTOS, fname)
        if os.path.exists(p):
            os.remove(p)
            print(f"  rm  {fname}")
        if ent_name:
            row = db.execute("SELECT id, metadata FROM entities WHERE name = ?", (ent_name,)).fetchone()
            if row:
                try:
                    meta = json.loads(row[1] or "{}")
                except Exception:  # noqa
                    meta = {}
                if meta.pop("photo_url", None) is not None:
                    db.execute("UPDATE entities SET metadata = ?, updated_at = datetime('now') WHERE id = ?",
                               (json.dumps(meta), row[0]))
                    print(f"  unlinked photo from '{ent_name}' (id {row[0]})")
    db.commit()
    db.close()

    print(f"\n{len(done)} regenerated, {len(failed)} failed")
    for f in failed:
        print("  ", f)


if __name__ == "__main__":
    main()
