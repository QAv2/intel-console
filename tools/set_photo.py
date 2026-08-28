#!/usr/bin/env python3
"""Manually set an entity's photo from a specific Wikimedia Commons file (or any URL).

Usage:
  python3 tools/set_photo.py "Entity Name" "File:Some file.jpg"       # Commons title
  python3 tools/set_photo.py "Entity Name" https://.../image.png       # direct URL
  python3 tools/set_photo.py "Entity Name" --unlink                    # remove photo
  python3 tools/set_photo.py --search "query terms"                    # list Commons hits
Logos (non-person entities) are composited on a white square; persons are plain-resized.
"""
import io
import json
import os
import sqlite3
import sys
import time
import urllib.parse
import urllib.request

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import fetch_candidate_photos as FC  # noqa: E402
import fix_logo_photos as FL  # noqa: E402

DB = os.path.join(ROOT, "data", "intel.db")
PHOTOS = os.path.join(ROOT, "static", "photos")


def main():
    if sys.argv[1] == "--search":
        api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(
            {"action": "query", "list": "search", "srnamespace": 6, "srsearch": sys.argv[2], "srlimit": 12, "format": "json"})
        data, _ = FC.fetch(api)
        for h in json.loads(data)["query"]["search"]:
            print(" ", h["title"])
        return
    name, ref = sys.argv[1], sys.argv[2]
    db = sqlite3.connect(DB)
    row = db.execute("SELECT id, entity_type, metadata FROM entities WHERE name = ?", (name,)).fetchone()
    if not row:
        sys.exit(f"entity not found: {name}")
    eid, etype, meta_raw = row
    meta = json.loads(meta_raw or "{}")
    if ref == "--unlink":
        old = meta.pop("photo_url", None)
        db.execute("UPDATE entities SET metadata = ? WHERE id = ?", (json.dumps(meta), eid))
        db.commit()
        if old:
            p = os.path.join(ROOT, "static", old.replace("/static/", ""))
            if os.path.exists(p):
                os.remove(p)
        print(f"unlinked {name} ({old})")
        return
    if ref.startswith("File:"):
        url, mime = FL.commons_url(ref)
        time.sleep(2.0)
    else:
        url, mime = ref, None
    data, ctype = FC.fetch(url)
    mime = mime or ctype
    if "svg" in (mime or "") or url.lower().split("?")[0].endswith(".svg"):
        im = FC.rasterize_svg(data)
    else:
        im = Image.open(io.BytesIO(data))
    out = FL.to_white_square(im) if etype != "person" else FC.to_jpeg(im, False)
    fname = FC.slug(name) + ".jpg"
    out.save(os.path.join(PHOTOS, fname), "JPEG", quality=90)
    meta["photo_url"] = f"/static/photos/{fname}"
    db.execute("UPDATE entities SET metadata = ?, updated_at = datetime('now') WHERE id = ?", (json.dumps(meta), eid))
    db.commit()
    print(f"set {name} → {fname} ({ref})")


if __name__ == "__main__":
    main()
