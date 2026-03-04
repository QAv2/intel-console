"""Search Wikimedia Commons for entity photos by name.

Uses the Wikimedia search API to find portrait/headshot photos,
then downloads and links them.

Usage:
    python3 -m seed.search_wiki_photos [--dry-run]
"""

import json
import os
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
API_DELAY = 1.5

# People still needing photos after batch downloads
REMAINING = [
    "Alexander Nix",
    "Andrija Puharich",
    "Bo Gritz",
    "Cardinal Bernard Law",
    "Christopher Wylie",
    "Cyril Smith",
    "David Atlee Phillips",
    "David Fravor",
    "Dean Radin",
    "Edgar Cayce",
    "Enrique Camarena",
    "Frank Olson",
    "Freeway Rick Ross",
    "George de Mohrenschildt",
    "Harlan Crow",
    "Ingo Swann",
    "John Casablancas",
    "John DeCamp",
    "Joseph McMoneagle",
    "Keith Raniere",
    "Licio Gelli",
    "Manly P. Hall",
    "Marc Dutroux",
    "Ralph Baric",
    "Robert Mercer",
    "Robert Monroe",
    "Shirō Ishii",
    "T. Boone Pickens",
    "Thomas Drake",
    "Thomas Townsend Brown",
    "Vandana Shiva",
    "William Donovan",
    "Zecharia Sitchin",
    "Albert Mackey",
    "Bev Harris",
    "Cele Castillo",
    "Clint Curtis",
    "Colm Kelleher",
    "Dale Graff",
    "Ed Dames",
    "Edwin May",
    "Eugene Mallove",
    "Jim Channon",
    "Jim Marrs",
    "John Anthony West",
    "John Hutchison",
    "Ken Alibek",
    "Leon Brittan",
    "Lyn Buchanan",
    "Maude Barlow",
    "Michael Levine",
    "Michael Tellinger",
    "Norwin Meneses",
    "Percy Schmeiser",
    "Peter Ball",
    "Peter Brabeck-Letmathe",
    "Peter Hayman",
    "Robert Fraley",
    "Stanley Pons",
    "Tyrone Hayes",
    "Walter Cruttenden",
    "William Patrick III",
    # Also the ones we skipped entirely:
    "Alois Zwinggi",
    "Angela Dellafiora Ford",
    "Brien Foerster",
    "Christopher Dunn",
    "Claude Haddad",
    "James Lacatski",
    "Jessica Utts",
    "Kenneth Shapiro",
    "Kit Green",
    "Oscar Danilo Blandon",
    "P.D. Houston",
    "Peter Scully",
    "Philippa Sigl-Glöckner",
    "Rosemary Vrablic",
    "Stanley Meyer",
    "Stuart Roffey",
    "Tammy McFadden",
    "Thomas Bowers",
    "Thomas Valone",
    "Val Broeksmit",
    "William Broeksmit",
    "Gérald Marie",
    # non-person entities we haven't checked yet (skip for now)
]

# Search term overrides (some names need different search terms)
SEARCH_OVERRIDES = {
    "Cardinal Bernard Law": "Bernard Francis Law cardinal",
    "T. Boone Pickens": "T. Boone Pickens businessman",
    "Freeway Rick Ross": "Rick Ross drug dealer",
    "Shirō Ishii": "Shiro Ishii Unit 731",
    "George de Mohrenschildt": "George de Mohrenschildt",
    "Thomas Drake": "Thomas Drake NSA",
    "Vandana Shiva": "Vandana Shiva activist",
    "William Donovan": "William J. Donovan OSS",
    "Leon Brittan": "Leon Brittan politician",
    "Peter Ball": "Peter Ball bishop",
    "Peter Hayman": "Peter Hayman diplomat",
    "Peter Brabeck-Letmathe": "Peter Brabeck Nestle",
    "Maude Barlow": "Maude Barlow water activist",
    "Ralph Baric": "Ralph Baric virologist",
    "Robert Mercer": "Robert Mercer hedge fund",
    "Marc Dutroux": "Marc Dutroux",
    "Keith Raniere": "Keith Raniere NXIVM",
    "Licio Gelli": "Licio Gelli P2",
    "Cyril Smith": "Cyril Smith politician Rochdale",
    "Christopher Wylie": "Christopher Wylie Cambridge Analytica whistleblower",
    "Alexander Nix": "Alexander Nix Cambridge Analytica",
    "David Fravor": "David Fravor commander USS Nimitz",
    "Harlan Crow": "Harlan Crow billionaire",
    "Michael Levine": "Michael Levine DEA",
    "Robert Monroe": "Robert Monroe out of body",
    "Percy Schmeiser": "Percy Schmeiser farmer Monsanto",
    "Ken Alibek": "Ken Alibek Kanatjan Alibekov",
    "Robert Fraley": "Robb Fraley Monsanto",
    "Tyrone Hayes": "Tyrone Hayes biologist atrazine",
}


def name_to_filename(name):
    """Convert entity name to a safe filename."""
    import re
    s = name.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', '_', s.strip())
    return f"{s}.jpg"


def search_wikimedia(search_term):
    """Search Wikimedia Commons for an image of this person."""
    # Try the main search API
    api_url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&list=search&srsearch={quote(search_term)}"
        f"&srnamespace=6&srlimit=5&format=json"
    )
    result = subprocess.run(
        ["curl", "-s", "-A", "IntelConsole/1.0 (OSINT research)", api_url],
        capture_output=True, text=True,
    )
    try:
        data = json.loads(result.stdout)
        results = data.get("query", {}).get("search", [])
        # Filter for likely portrait photos
        for r in results:
            title = r["title"]  # e.g. "File:Something.jpg"
            lower = title.lower()
            # Skip SVGs, PDFs, audio
            if any(ext in lower for ext in ['.svg', '.pdf', '.ogg', '.wav', '.webm']):
                continue
            # Prefer cropped/portrait/official
            return title.replace("File:", "")
        return None
    except (json.JSONDecodeError, KeyError) as e:
        print(f"  [search error] {search_term}: {e}")
        return None


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
        print(f"  [URL error] {wiki_filename}: {e}")
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
    dry_run = "--dry-run" in sys.argv
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

    # Filter to only those without photos on disk already
    todo = []
    for name in REMAINING:
        fname = name_to_filename(name)
        if not (PHOTOS_DIR / fname).exists():
            todo.append(name)

    print(f"Searching Wikimedia for {len(todo)} people...")
    print(f"{'='*60}")

    # Phase 1: Search for Wikimedia filenames
    found = {}
    not_found = []
    for i, name in enumerate(todo):
        search_term = SEARCH_OVERRIDES.get(name, name)
        wiki_file = search_wikimedia(search_term)
        if wiki_file:
            found[name] = wiki_file
            print(f"  [{i+1}/{len(todo)}] {name}: {wiki_file}")
        else:
            not_found.append(name)
            print(f"  [{i+1}/{len(todo)}] {name}: [not found]")
        time.sleep(API_DELAY)

    print(f"\n  Found: {len(found)}, Not found: {len(not_found)}")

    if dry_run:
        print("\n[DRY RUN] Would download:")
        for name, wiki_file in found.items():
            print(f"  {name}: {wiki_file}")
        if not_found:
            print(f"\nNot found ({len(not_found)}):")
            for name in not_found:
                print(f"  {name}")
        return

    # Phase 2: Resolve URLs and download
    print(f"\n--- Downloading {len(found)} photos ---")
    downloaded = []
    failed = []
    for i, (name, wiki_file) in enumerate(found.items()):
        out_file = name_to_filename(name)
        if (PHOTOS_DIR / out_file).exists():
            print(f"  [skip] {out_file} already exists")
            downloaded.append((name, out_file))
            continue

        url = get_wiki_url(wiki_file)
        if not url:
            print(f"  [FAIL] {name}: couldn't resolve URL")
            failed.append(name)
            continue

        time.sleep(API_DELAY)
        ok = download_and_resize(url, out_file)
        if ok:
            downloaded.append((name, out_file))
        else:
            failed.append(name)

        if i < len(found) - 1:
            time.sleep(DOWNLOAD_DELAY)

    # Phase 3: Update JSON
    if downloaded:
        ue, un = update_json(downloaded)
        print(f"\n  Updated {ue} entities, {un} graph nodes")

    print(f"\n{'='*60}")
    print(f"  Downloaded: {len(downloaded)}")
    print(f"  Failed: {len(failed)}")
    print(f"  Not found on Wikimedia: {len(not_found)}")

    if failed:
        print(f"\n  Failed downloads: {', '.join(failed)}")
    if not_found:
        print(f"\n  Not on Wikimedia: {', '.join(not_found)}")

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
