"""Download photos for Bohemian Grove expansion — v2.

Uses Wikimedia Commons API to resolve correct URLs,
then downloads with generous delays to avoid rate limits.
"""

import asyncio
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from io import BytesIO
from urllib.parse import quote

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent.parent))
from server.db import get_db, init_db, close_db

PHOTOS_DIR = Path(__file__).parent.parent / "static" / "photos"
MAX_SIZE = 400
DOWNLOAD_DELAY = 12  # seconds between CDN downloads
API_DELAY = 2  # seconds between API calls


# person name -> Wikimedia Commons filename
WIKI_FILES = {
    "Dick Cheney": "Richard_Cheney_2003_official_portrait.jpg",
    "Donald Rumsfeld": "Donald_Rumsfeld_portrait_(brighter_flag,_neutral_background).jpg",
    "Colin Powell": "Colin_Powell_official_Secretary_of_State_photo.jpg",
    "Caspar Weinberger": "Caspar_Willard_Weinberger_Secretary_of_Defense_ME755-6.jpg",
    "George Shultz": "George_P._Shultz_official_photo.jpg",
    "Edwin Meese": "Edwin_Meese_III_Attorney_General_portrait_(cropped1).jpg",
    "Alan Greenspan": "Alan_Greenspan_color_photo_portrait.jpg",
    "Clarence Thomas": "Clarence_Thomas_official_SCOTUS_portrait_(cropped).jpg",
    "Michael Bloomberg": "Michael_R_Bloomberg.jpg",
    "Charles Koch": "Charles_Koch.jpg",
    "David McCormick": "Sen._David_McCormick_official_portrait,_119th_Congress.jpg",
    "Edwin Fuelner": "Edwin_Feulner_by_Gage_Skidmore.jpg",
    "Harlan Crow": "Harlan_Crow_(cropped).jpg",
    "Steven Bechtel Sr": "Stephen_Bechtel_Sr.jpg",
    "Joseph Coors Sr": "Joseph_Coors,_President_&_CEO,_Adolph_Coors_Company_-_ME408_(cropped).jpg",
    "Brendan Bechtel": "Brendan_Bechtel_(cropped).jpg",
}

# person name -> output filename
OUTPUT_FILES = {
    "Dick Cheney": "dick_cheney.jpg",
    "Donald Rumsfeld": "donald_rumsfeld.jpg",
    "Colin Powell": "colin_powell.jpg",
    "Caspar Weinberger": "caspar_weinberger.jpg",
    "George Shultz": "george_shultz.jpg",
    "Edwin Meese": "edwin_meese.jpg",
    "Alan Greenspan": "alan_greenspan.jpg",
    "Clarence Thomas": "clarence_thomas.jpg",
    "Michael Bloomberg": "michael_bloomberg.jpg",
    "Charles Koch": "charles_koch.jpg",
    "David McCormick": "david_mccormick.jpg",
    "Edwin Fuelner": "edwin_fuelner.jpg",
    "Harlan Crow": "harlan_crow.jpg",
    "Steven Bechtel Sr": "steven_bechtel_sr.jpg",
    "Joseph Coors Sr": "joseph_coors_sr.jpg",
    "Brendan Bechtel": "brendan_bechtel.jpg",
}


def get_wiki_url(wiki_filename):
    """Use Wikimedia API to get the actual image URL."""
    title = f"File:{wiki_filename}"
    api_url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&titles={quote(title)}&prop=imageinfo"
        f"&iiprop=url&iiurlwidth={MAX_SIZE}&format=json"
    )

    result = subprocess.run(
        ["curl", "-s", "-A", "IntelConsole/1.0 (OSINT research)", api_url],
        capture_output=True, text=True,
    )

    try:
        data = json.loads(result.stdout)
        pages = data["query"]["pages"]
        for pid, page in pages.items():
            if "imageinfo" in page:
                info = page["imageinfo"][0]
                # Prefer the pre-resized thumb URL
                return info.get("thumburl") or info.get("url")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"  [API error] {wiki_filename}: {e}")

    return None


def download_and_resize(url, filename):
    """Download and resize to 400px max."""
    filepath = PHOTOS_DIR / filename
    if filepath.exists():
        print(f"  [skip] {filename} already exists")
        return True

    tmpfile = f"/tmp/grove_{filename}"
    ua = "Mozilla/5.0 (X11; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0"

    result = subprocess.run(
        ["curl", "-s", "-o", tmpfile, "-w", "%{http_code}",
         "-A", ua, "-L", "--max-time", "30", url],
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
        print(f"  [FAIL] {filename}: {e}")
        return False


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
            continue
        meta = json.loads(row[0]["metadata"]) if row[0]["metadata"] else {}
        meta["photo_url"] = f"/static/photos/{filename}"
        await db.execute(
            "UPDATE entities SET metadata = ? WHERE id = ?",
            (json.dumps(meta), row[0]["id"]),
        )
        updated += 1
    await db.commit()
    await close_db()
    return updated


def main():
    # Filter to only those not yet downloaded
    todo = {}
    for name, outfile in OUTPUT_FILES.items():
        if not (PHOTOS_DIR / outfile).exists():
            todo[name] = outfile

    if not todo:
        print("All photos already downloaded!")
        return

    print(f"\n=== Phase 1: Resolving {len(todo)} URLs via Wikimedia API ===\n")

    urls = {}
    for name in todo:
        wiki_file = WIKI_FILES[name]
        url = get_wiki_url(wiki_file)
        if url:
            urls[name] = url
            print(f"  {name}: {url[:80]}...")
        else:
            print(f"  {name}: [!] URL not found")
        time.sleep(API_DELAY)

    print(f"\n=== Phase 2: Downloading {len(urls)} photos ({DOWNLOAD_DELAY}s delays) ===\n")

    downloaded = []
    failed = []

    for i, (name, url) in enumerate(urls.items()):
        outfile = todo[name]
        ok = download_and_resize(url, outfile)
        if ok:
            downloaded.append((name, outfile))
        else:
            failed.append(name)

        if i < len(urls) - 1:
            time.sleep(DOWNLOAD_DELAY)

    print(f"\n=== Results: {len(downloaded)} OK, {len(failed)} failed ===")
    if failed:
        print(f"Failed: {', '.join(failed)}")

    if downloaded:
        print(f"\nUpdating DB for {len(downloaded)} entities...")
        updated = asyncio.run(update_db_photos(downloaded))
        print(f"Updated {updated} entities in DB.")

    total = len(list(PHOTOS_DIR.glob("*.jpg")))
    print(f"\nTotal photos: {total}")


if __name__ == "__main__":
    main()
