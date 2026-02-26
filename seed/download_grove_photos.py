"""Download photos for Bohemian Grove expansion entities.

Uses full-size Wikimedia Commons URLs (not thumbs) to avoid rate limits,
then resizes locally to 400px max. Updates entity metadata in DB.
"""

import asyncio
import json
import subprocess
import sys
import time
from pathlib import Path
from io import BytesIO

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent.parent))
from server.db import get_db, init_db, close_db

PHOTOS_DIR = Path(__file__).parent.parent / "static" / "photos"
MAX_SIZE = 400
DELAY = 3  # seconds between downloads — be polite to Wikimedia


def download_and_resize(url, filename):
    """Download image via curl, resize to 400px max, save as JPEG."""
    filepath = PHOTOS_DIR / filename
    if filepath.exists():
        print(f"  [skip] {filename} already exists")
        return True

    tmpfile = f"/tmp/grove_photo_{filename}"

    result = subprocess.run(
        [
            "curl", "-s", "-o", tmpfile, "-w", "%{http_code}",
            "-A", "Mozilla/5.0 (X11; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0",
            "-L",  # follow redirects
            "--max-time", "30",
            url,
        ],
        capture_output=True, text=True,
    )

    status = result.stdout.strip()
    if status != "200":
        print(f"  [FAIL] {filename}: HTTP {status}")
        return False

    try:
        img = Image.open(tmpfile)
        img = img.convert("RGB")

        w, h = img.size
        if max(w, h) > MAX_SIZE:
            ratio = MAX_SIZE / max(w, h)
            img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)

        img.save(str(filepath), "JPEG", quality=85)
        print(f"  [OK] {filename} ({img.size[0]}x{img.size[1]})")
        return True
    except Exception as e:
        print(f"  [FAIL] {filename}: image error: {e}")
        return False


# Full-size Wikimedia Commons URLs — all public domain US government portraits or CC-licensed
PHOTOS = [
    # US Presidents — official White House portraits (public domain)
    {
        "name": "Ronald Reagan",
        "filename": "ronald_reagan.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/16/Official_Portrait_of_President_Reagan_1981.jpg",
    },
    {
        "name": "George H.W. Bush",
        "filename": "george_hw_bush.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/George_H._W._Bush%2C_President_of_the_United_States%2C_1989_official_portrait.jpg",
    },
    {
        "name": "George W. Bush",
        "filename": "george_w_bush.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/George-W-Bush.jpeg",
    },
    # VP / Cabinet — official DoD/State Dept portraits (public domain)
    {
        "name": "Dick Cheney",
        "filename": "dick_cheney.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/46_Dick_Cheney_3x4.jpg",
    },
    {
        "name": "Donald Rumsfeld",
        "filename": "donald_rumsfeld.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Rumsfeld1.jpg",
    },
    {
        "name": "Colin Powell",
        "filename": "colin_powell.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Colin_Powell_official_Secretary_of_State_photo.jpg",
    },
    {
        "name": "Caspar Weinberger",
        "filename": "caspar_weinberger.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Caspar_Weinberger_official_photo.JPEG",
    },
    {
        "name": "George Shultz",
        "filename": "george_shultz.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/George_P._Shultz_official_photo.jpg",
    },
    {
        "name": "Edwin Meese",
        "filename": "edwin_meese.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Ed_Meese_official_portrait.jpg",
    },
    # Federal Reserve — official portrait (public domain)
    {
        "name": "Alan Greenspan",
        "filename": "alan_greenspan.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Alan_Greenspan_color_photo_portrait.jpg",
    },
    # Supreme Court — official SCOTUS portrait (public domain)
    {
        "name": "Clarence Thomas",
        "filename": "clarence_thomas.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/21/Clarence_Thomas_official_SCOTUS_portrait_%28crop%29.jpg",
    },
    # NYC Mayor — official portrait (public domain)
    {
        "name": "Michael Bloomberg",
        "filename": "michael_bloomberg.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Michael_R_Bloomberg.jpg",
    },
    # Charles Koch — CC-BY-SA Gage Skidmore
    {
        "name": "Charles Koch",
        "filename": "charles_koch.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/24/Charles_Koch.jpg",
    },
    # David McCormick — US Senate official portrait (public domain)
    {
        "name": "David McCormick",
        "filename": "david_mccormick.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Sen._David_McCormick_official_portrait%2C_119th_Congress.jpg",
    },
    # Edwin Fuelner — CC-BY-SA Gage Skidmore
    {
        "name": "Edwin Fuelner",
        "filename": "edwin_fuelner.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Edwin_Feulner_by_Gage_Skidmore.jpg",
    },
    # Harlan Crow — CC-BY-SA
    {
        "name": "Harlan Crow",
        "filename": "harlan_crow.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Harlan_Crow_%28cropped%29.jpg",
    },
    # Steven Bechtel Sr — public domain
    {
        "name": "Steven Bechtel Sr",
        "filename": "steven_bechtel_sr.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Stephen_Bechtel_Sr.jpg",
    },
    # Joseph Coors Sr — fair use / wikipedia
    {
        "name": "Joseph Coors Sr",
        "filename": "joseph_coors_sr.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/en/1/1b/Joseph_Coors_Sr.jpg",
    },
    # Brendan Bechtel — CC-BY-SA
    {
        "name": "Brendan Bechtel",
        "filename": "brendan_bechtel.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Brendan_Bechtel_%28cropped%29.jpg",
    },
]


async def update_db_photos(downloaded):
    """Update entity metadata with photo URLs."""
    await init_db()
    db = await get_db()

    updated = 0
    for name, filename in downloaded:
        row = await db.execute_fetchall(
            "SELECT id, metadata FROM entities WHERE name = ?", (name,)
        )
        if not row:
            print(f"  [!] Entity not found in DB: {name}")
            continue

        eid = row[0]["id"]
        meta = json.loads(row[0]["metadata"]) if row[0]["metadata"] else {}
        meta["photo_url"] = f"/static/photos/{filename}"

        await db.execute(
            "UPDATE entities SET metadata = ? WHERE id = ?",
            (json.dumps(meta), eid),
        )
        updated += 1

    await db.commit()
    await close_db()
    return updated


def main():
    print(f"\n=== Downloading {len(PHOTOS)} photos (full-size, {DELAY}s delay) ===\n")

    downloaded = []
    failed = []

    for i, p in enumerate(PHOTOS):
        ok = download_and_resize(p["url"], p["filename"])
        if ok:
            downloaded.append((p["name"], p["filename"]))
        else:
            failed.append(p["name"])

        # Delay between downloads (skip if already existed)
        if i < len(PHOTOS) - 1:
            time.sleep(DELAY)

    print(f"\n=== Download complete: {len(downloaded)} OK, {len(failed)} failed ===")
    if failed:
        print(f"Failed: {', '.join(failed)}")

    # Update DB
    if downloaded:
        print(f"\nUpdating DB metadata for {len(downloaded)} entities...")
        updated = asyncio.run(update_db_photos(downloaded))
        print(f"Updated {updated} entities in DB.")

    total_photos = len(list(PHOTOS_DIR.glob("*.jpg")))
    print(f"\nTotal photos in static/photos/: {total_photos}")


if __name__ == "__main__":
    main()
