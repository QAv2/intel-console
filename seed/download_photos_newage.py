"""Download photos for new age psyop entities.

Phase 1: Wikimedia Commons (verified free-license portraits)
Phase 2: Direct URLs from official/public sites (press photos, about pages)

Usage:
    python3 -m seed.download_photos_newage
"""

import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

from PIL import Image

PHOTOS_DIR = Path(__file__).parent.parent / "static" / "photos"
STATIC_DATA = Path(__file__).parent.parent / "static" / "data"
MAX_SIZE = 400
DOWNLOAD_DELAY = 3
API_DELAY = 1

# Verified Wikimedia filenames for new age psyop entities
CURATED = {
    # People with verified Wikimedia Commons photos
    "David Icke": ("David_Icke,_7_June_2013_(2).jpg", "david_icke.jpg"),
    "Sadhguru": ("Sadhguru-Jaggi-Vasudev.jpg", "sadhguru.jpg"),
    "Teal Swan": ("Teal_Swan.jpg", "teal_swan.jpg"),
    "David Wilcock": ("David_Wilcock_(cropped).jpg", "david_wilcock.jpg"),
    "Gregg Braden": ("Gregg_Braden.jpg", "gregg_braden.jpg"),
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

    tmpfile = f"/tmp/photo_{filename}"
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


def update_json(downloaded):
    """Update entities.json and graph.json with photo URLs."""
    with open(STATIC_DATA / "entities.json") as f:
        entities = json.load(f)
    with open(STATIC_DATA / "graph.json") as f:
        graph = json.load(f)

    photo_map = {name: fname for name, fname in downloaded}

    updated_e = 0
    for eid, e in entities.items():
        if e["name"] in photo_map:
            meta = e.get("metadata", {})
            if isinstance(meta, str):
                meta = json.loads(meta)
            meta["photo_url"] = f"photos/{photo_map[e['name']]}"
            e["metadata"] = meta
            updated_e += 1

    updated_n = 0
    for node in graph["nodes"]:
        if node["name"] in photo_map:
            node["photo_url"] = f"photos/{photo_map[node['name']]}"
            updated_n += 1

    with open(STATIC_DATA / "entities.json", "w") as f:
        json.dump(entities, f, indent=2)
    with open(STATIC_DATA / "graph.json", "w") as f:
        json.dump(graph, f, indent=2)

    return updated_e, updated_n


def main():
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

    todo = {}
    already = {}
    for name, (wiki_file, out_file) in CURATED.items():
        if (PHOTOS_DIR / out_file).exists():
            already[name] = out_file
        else:
            todo[name] = (wiki_file, out_file)

    print(f"Curated list: {len(CURATED)} entities")
    print(f"Already on disk: {len(already)}")
    print(f"Need to download: {len(todo)}")

    if not todo and not already:
        return

    # Phase 1: Resolve URLs
    print(f"\n--- Resolving Wikimedia URLs ---")
    urls = {}
    not_found = []
    for name, (wiki_file, out_file) in todo.items():
        url = get_wiki_url(wiki_file)
        if url:
            urls[name] = (url, out_file)
            print(f"  {name}: OK")
        else:
            not_found.append(name)
            print(f"  {name}: [!] not found ({wiki_file})")
        time.sleep(API_DELAY)

    # Phase 2: Download
    print(f"\n--- Downloading {len(urls)} photos ---")
    downloaded = []
    failed = []
    for i, (name, (url, out_file)) in enumerate(urls.items()):
        ok = download_and_resize(url, out_file)
        if ok:
            downloaded.append((name, out_file))
        else:
            failed.append(name)
        if i < len(urls) - 1:
            time.sleep(DOWNLOAD_DELAY)

    # Add pre-existing files
    for name, out_file in already.items():
        downloaded.append((name, out_file))

    # Phase 3: Update JSON
    if downloaded:
        ue, un = update_json(downloaded)
        print(f"\n  Updated {ue} entities, {un} graph nodes")

    print(f"\n{'='*60}")
    print(f"  Downloaded: {len(urls) - len(failed)}")
    print(f"  Already existed: {len(already)}")
    print(f"  Failed: {len(failed)}")
    print(f"  Not on Wikimedia: {len(not_found)}")
    if failed:
        print(f"  Failed: {', '.join(failed)}")
    if not_found:
        print(f"  Not found: {', '.join(not_found)}")

    print(f"{'='*60}")

    # ── Phase 2: Direct URL downloads (non-Wikimedia) ──
    print(f"\n\n{'='*60}")
    print("Phase 2: Direct URL downloads")
    print(f"{'='*60}\n")

    DIRECT = {
        "Robert Edward Grant": (
            "https://robertedwardgrant.com/wp-content/uploads/2025/09/SirRobertEdwardGrant-a-scaled.jpeg",
            "robert_edward_grant.jpg",
        ),
        "Corey Goode": (
            "https://s3.spherebeingalliance.com/e107_media/6670dceeb0/images/cache/corey_goode_a5ac010c3a20b1b7e70487eaf8ced1ff_320x0.jpg",
            "corey_goode.jpg",
        ),
        "Billy Carson": (
            "https://brooklyn.gaia.com/v1/assets-render/c4f6dcf8-ee7b-4b3e-8d0a-709f44b4f828?hash=c5309a93e9a10f0e6fac0e3003892d672eca39d63d823a5121f2d39cbdb665f4",
            "billy_carson.jpg",
        ),
        "Nassim Haramein": (
            "https://nassimharamein.com/wp-content/uploads/2024/11/Nassim-1.webp",
            "nassim_haramein.jpg",
        ),
        "Matias De Stefano": (
            "https://vultology.com/wp-content/uploads/2024/04/000079595_1_MATIAS_DE_STEFANO_202202102057.jpg",
            "matias_de_stefano.jpg",
        ),
        "Emery Smith": (
            "https://brooklyn.gaia.com/v1/assets-render/f32cd057-b72b-4c15-995c-960f723fc288?hash=c5309a93e9a10f0e6fac0e3003892d672eca39d63d823a5121f2d39cbdb665f4",
            "emery_smith.jpg",
        ),
        "Bentinho Massaro": (
            "https://www.spiritualteachers.org/wp-content/uploads/2016/08/bentinho-massaro.jpg",
            "bentinho_massaro.jpg",
        ),
        "Jordan Duchnycz": (
            "https://tssmedia.thespiritscience.net/2022/03/patchjordan.jpg",
            "jordan_duchnycz.jpg",
        ),
        "Santos Bonacci": (
            "https://pingkanisabella.wordpress.com/wp-content/uploads/2014/01/santosbonacci.jpg",
            "santos_bonacci.jpg",
        ),
        "Jordan Maxwell": (
            "https://www.jordanmaxwell.com/images/home/jordanHomePhoto.jpg",
            "jordan_maxwell.jpg",
        ),
        "Alex Collier": (
            "https://alexcollierorg.b-cdn.net/wp-content/uploads/2012/01/alexcollier2.jpg",
            "alex_collier.jpg",
        ),
        "Simon Parkes": (
            "https://static.wixstatic.com/media/bcb736_7b84032bc51a470ba74b013102f182d6~mv2.jpg/v1/fill/w_500,h_500,al_c,q_80,usm_0.66_1.00_0.01,enc_auto,quality_auto/Simon%20Profile%20Pic2_edited_edited.jpg",
            "simon_parkes.jpg",
        ),
        "Michael Salla": (
            "https://secure.gravatar.com/avatar/f424eee6592938ef8b0a06cd701adfb38aad089a3ec1c9a8a4d04a377e85ec61?s=500&r=g",
            "michael_salla.jpg",
        ),
        "Kerry Cassidy": (
            "https://i0.wp.com/projectcamelotportal.com/wp-content/uploads/kerry1_jan27-copy1.png",
            "kerry_cassidy.jpg",
        ),
        "Laura Eisenhower": (
            "https://substack-post-media.s3.amazonaws.com/public/images/f8477e20-7e31-48de-ab89-40e3ae5d9093_720x720.jpeg",
            "laura_eisenhower.jpg",
        ),
        "James Gilliland": (
            "https://www.eceti.org/uploads/1/2/1/7/121701415/editor/james-gilliland_1.jpg",
            "james_gilliland.jpg",
        ),
    }

    direct_downloaded = []
    direct_failed = []
    direct_skipped = []

    for name, (url, out_file) in DIRECT.items():
        if (PHOTOS_DIR / out_file).exists():
            print(f"  [skip] {out_file} already exists")
            direct_skipped.append(name)
            direct_downloaded.append((name, out_file))
            continue
        ok = download_and_resize(url, out_file)
        if ok:
            direct_downloaded.append((name, out_file))
        else:
            direct_failed.append(name)
        time.sleep(DOWNLOAD_DELAY)

    # Update JSON with direct downloads
    if direct_downloaded:
        ue2, un2 = update_json(direct_downloaded)
        print(f"\n  Updated {ue2} entities, {un2} graph nodes")

    print(f"\n{'='*60}")
    print(f"  Phase 2 downloaded: {len(direct_downloaded) - len(direct_skipped)}")
    print(f"  Phase 2 skipped: {len(direct_skipped)}")
    print(f"  Phase 2 failed: {len(direct_failed)}")
    if direct_failed:
        print(f"  Failed: {', '.join(direct_failed)}")

    # Final count
    with open(STATIC_DATA / "entities.json") as f:
        entities = json.load(f)
    with_photo = sum(1 for e in entities.values()
                    if (e.get("metadata", {}) if isinstance(e.get("metadata", {}), dict)
                        else json.loads(e.get("metadata", "{}"))).get("photo_url"))
    print(f"\n  Total entities with photos: {with_photo}/{len(entities)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
