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
API_DELAY = 2.5

# Auto-populated from graph.json: all person entities without photos
REMAINING = []  # populated at runtime from graph data

# Known bad Wikimedia matches (wrong person, wrong image, etc.)
# These will fall through to the Wikipedia page image fallback
WIKIMEDIA_SKIP = {
    "Alois Zwinggi",        # Returns Trump at Davos
    "Claude Haddad",        # Returns Lise Haddad (wrong person)
    "Eleanor Lambert",      # Returns a house photo
    "Harry Hoxsey",         # Returns a bottle, not portrait
    "Helena Blavatsky",     # Returns emblem logo
    "Henri Deterding",      # Returns Shell telegram
    "John Anthony West",    # Returns wrong John West (MP)
    "John Perkins",         # Returns signature only
    "Mark Lombardi",        # Returns a chart/ficha
    "Neil Armstrong",       # Returns "Buzz Aldrin by Neil Armstrong"
    "Peter Hayman",         # Returns a map
    "Peter Scully",         # Returns a church
    "Stanley Meyer",        # Returns circuit diagram
    "Marquis de Cuevas",    # Returns ballet poster
    "Ken Kesey",            # Returns book title page
    "Enrico Mattei",        # Returns blurry group photo
    "George de Mohrenschildt",  # Returns wife's photo
    "Zecharia Sitchin",     # Returns book page illustration
}

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
    "Peter Ball": "Peter Ball bishop Anglican",
    "Peter Hayman": "Peter Hayman diplomat",
    "Peter Brabeck-Letmathe": "Peter Brabeck Nestle",
    "Maude Barlow": "Maude Barlow water activist",
    "Ralph Baric": "Ralph Baric virologist",
    "Robert Mercer": "Robert Mercer hedge fund Renaissance",
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
    # New batch
    "Abraham Flexner": "Abraham Flexner educator",
    "Alan Robock": "Alan Robock climatologist",
    "Aldous Huxley": "Aldous Huxley author",
    "Alice Bailey": "Alice Bailey theosophist",
    "Ancel Keys": "Ancel Keys physiologist",
    "Bernard J. Eastlund": "Bernard Eastlund physicist HAARP",
    "Bo Gritz": "Bo Gritz Green Beret",
    "Bob Lazar": "Bob Lazar Area 51",
    "Brien Foerster": "Brien Foerster elongated skulls",
    "Buzz Aldrin": "Buzz Aldrin astronaut",
    "Carroll Quigley": "Carroll Quigley historian Georgetown",
    "Cecil Rhodes": "Cecil Rhodes colonial",
    "Christopher Dunn": "Christopher Dunn Giza Power Plant author",
    "Christopher Mellon": "Christopher Mellon Pentagon UFO",
    "Colm Kelleher": "Colm Kelleher NIDS Skinwalker",
    "Count Étienne de Beaumont": "Etienne de Beaumont patron arts",
    "Cristin Kearns": "Cristin Kearns sugar industry researcher",
    "Dario Amodei": "Dario Amodei Anthropic CEO",
    "David Keith": "David Keith geoengineering Harvard",
    "David Petraeus": "David Petraeus general CIA",
    "Dean Radin": "Dean Radin parapsychologist",
    "Ed Dames": "Ed Dames remote viewing military",
    "Edwin May": "Edwin May parapsychologist SRI",
    "Eleanor Lambert": "Eleanor Lambert fashion publicist",
    "Enrico Mattei": "Enrico Mattei ENI Italy",
    "Eugene Mallove": "Eugene Mallove cold fusion",
    "Frank Keutsch": "Frank Keutsch Harvard geoengineering",
    "Frank Zappa": "Frank Zappa musician",
    "Fritz ter Meer": "Fritz ter Meer IG Farben",
    "Hugo Chávez": "Hugo Chavez Venezuela president",
    "Hélène Rochas": "Helene Rochas fashion",
    "Ida Tarbell": "Ida Tarbell journalist Standard Oil",
    "Ingo Swann": "Ingo Swann remote viewing",
    "James Clapper": "James Clapper DNI intelligence",
    "James Lacatski": "James Lacatski DIA AAWSAP",
    "James Woolsey": "R. James Woolsey CIA director",
    "Jessica Utts": "Jessica Utts statistician",
    "Jim Channon": "Jim Channon First Earth Battalion",
    "Jim Morrison": "Jim Morrison Doors musician",
    "Joel Osteen": "Joel Osteen pastor",
    "John Anthony West": "John Anthony West Egyptologist",
    "John Brennan": "John Brennan CIA director",
    "John Casablancas": "John Casablancas Elite Model",
    "John DeCamp": "John DeCamp Nebraska senator",
    "John Foster Dulles": "John Foster Dulles secretary state",
    "John Kerry": "John Kerry secretary state senator",
    "John Perkins": "John Perkins economic hit man",
    "John Yudkin": "John Yudkin Pure White Deadly",
    "Joseph McMoneagle": "Joseph McMoneagle remote viewer Stargate",
    "Karen Silkwood": "Karen Silkwood nuclear whistleblower",
    "Karl Wolfe": "Karl Wolfe Air Force disclosure",
    "Ken Caldeira": "Ken Caldeira climate scientist",
    "Ken Kesey": "Ken Kesey author",
    "Kenneth Copeland": "Kenneth Copeland televangelist",
    "Kermit Roosevelt Jr.": "Kermit Roosevelt CIA Iran Ajax",
    "Kit Green": "Kit Green CIA physician",
    "Leon Panetta": "Leon Panetta CIA secretary defense",
    "Luke Iseman": "Luke Iseman geoengineering Make Sunsets",
    "Lyn Buchanan": "Lyn Buchanan remote viewing military",
    "Marie-Laure de Noailles": "Marie-Laure de Noailles patron",
    "Marilyn Ferguson": "Marilyn Ferguson Aquarian Conspiracy",
    "Mark Lombardi": "Mark Lombardi artist conspiracy",
    "Mark Zuckerberg": "Mark Zuckerberg Facebook Meta",
    "Marquis de Cuevas": "Marquis de Cuevas ballet",
    "Max Gerson": "Max Gerson therapy cancer",
    "Michael Hayden": "Michael Hayden NSA CIA director",
    "Michael Levine": "Michael Levine DEA agent author",
    "Morris Fishbein": "Morris Fishbein AMA editor",
    "Muammar Gaddafi": "Muammar Gaddafi Libya",
    "Neil Armstrong": "Neil Armstrong astronaut",
    "Nicolas Sarkozy": "Nicolas Sarkozy president France",
    "Norwin Meneses": "Norwin Meneses Contra drug",
    "P.D. Houston": "P.D. Houston psychic spy",
    "Paul Bennewitz": "Paul Bennewitz UFO Dulce",
    "Paul Bonacci": "Paul Bonacci Franklin scandal",
    "Paul Hellyer": "Paul Hellyer Canada defense minister UFO",
    "Paul Smith": "Paul Smith remote viewing Army major",
    "Peggy Siegal": "Peggy Siegal publicist",
    "Peter Scully": "Peter Scully criminal",
    "Philip Corso": "Philip Corso The Day After Roswell",
    "Philippa Sigl-Glöckner": "Philippa Sigl-Glockner economist",
    "Prince Bernhard": "Prince Bernhard Netherlands Bilderberg",
    "R. Gordon Wasson": "R. Gordon Wasson mushroom ethnomycologist",
    "Richard Doty": "Richard Doty AFOSI disinformation",
    "Richard Sackler": "Richard Sackler Purdue Pharma OxyContin",
    "Robert Monroe": "Robert Monroe Institute out of body",
    "Robert Muller": "Robert Muller United Nations education",
    "Rosemary Vrablic": "Rosemary Vrablic Deutsche Bank Trump",
    "Sam Altman": "Sam Altman OpenAI CEO",
    "Sean Parker": "Sean Parker Napster Facebook",
    "Stanley Meyer": "Stanley Meyer water fuel cell",
    "Stanley Pons": "Stanley Pons cold fusion",
    "Thomas Bowers": "Thomas Bowers Deutsche Bank Epstein",
    "Thomas Valone": "Thomas Valone free energy",
    "Timothy Leary": "Timothy Leary LSD psychedelic",
    "Val Broeksmit": "Val Broeksmit Deutsche Bank whistleblower",
    "Walter Cruttenden": "Walter Cruttenden binary star",
    "Walter Lippmann": "Walter Lippmann journalist public opinion",
    "Wilhelm Reich": "Wilhelm Reich orgone psychoanalyst",
    "William Broeksmit": "William Broeksmit Deutsche Bank",
    "William Colby": "William Colby CIA director",
    "Willis Harman": "Willis Harman SRI futurist",
    "Zecharia Sitchin": "Zecharia Sitchin Sumerian",
    "Gérald Marie": "Gerald Marie Elite Model",
    "Harry Hoxsey": "Harry Hoxsey cancer treatment",
    "Henri Deterding": "Henri Deterding Royal Dutch Shell",
    "Helena Blavatsky": "Helena Blavatsky theosophy",
    "Kenneth Shapiro": "Kenneth Shapiro parapsychology",
    "Charles de Beistegui": "Carlos de Beistegui ball masque",
    "Oscar Danilo Blandon": "Oscar Danilo Blandon Contra drug CIA",
    "Stuart Roffey": "Stuart Roffey",
    "Tammy McFadden": "Tammy McFadden",
    "Angela Dellafiora Ford": "Angela Dellafiora Ford CIA psychic",
    "Cele Castillo": "Celerino Castillo DEA Iran-Contra",
    "Claude Haddad": "Claude Haddad",
    "Bev Harris": "Bev Harris Black Box Voting",
    "Dale Graff": "Dale Graff Stargate Project",
    "Alois Zwinggi": "Alois Zwinggi World Economic Forum",
    "Robert Fraley": "Robb Fraley Monsanto CTO",
    "William Patrick III": "William C. Patrick III bioweapons",
}


def name_to_filename(name):
    """Convert entity name to a safe filename."""
    import re
    s = name.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', '_', s.strip())
    return f"{s}.jpg"


BAD_EXTENSIONS = {'.svg', '.pdf', '.ogg', '.wav', '.webm', '.djvu', '.tif', '.tiff', '.xcf'}

def search_wikimedia(search_term):
    """Search Wikimedia Commons for an image of this person."""
    api_url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&list=search&srsearch={quote(search_term)}"
        f"&srnamespace=6&srlimit=10&format=json"
    )
    result = subprocess.run(
        ["curl", "-s", "-A", "IntelConsole/1.0 (OSINT research)", api_url],
        capture_output=True, text=True,
    )
    try:
        data = json.loads(result.stdout)
        results = data.get("query", {}).get("search", [])
        for r in results:
            title = r["title"]  # e.g. "File:Something.jpg"
            lower = title.lower()
            # Skip non-image formats
            if any(lower.endswith(ext) for ext in BAD_EXTENSIONS):
                continue
            # Skip obvious non-portrait content
            if any(bad in lower for bad in [
                'house', 'building', 'telegram', 'logo', 'emblem',
                'signature', 'circuit', 'map', 'chart', 'diagram',
                'flag', 'seal', 'coat of arms', 'bottle', 'book',
                'filialkirche', 'strassburg', 'bodleian', 'playbill',
                'fayettevillian', 'sugarsin', 'byregions',
            ]):
                continue
            return title.replace("File:", "")
        return None
    except (json.JSONDecodeError, KeyError) as e:
        print(f"  [search error] {search_term}: {e}")
        return None


def search_wikipedia_image(search_term):
    """Fallback: get the main image from a Wikipedia article."""
    # Use Wikipedia API to get the page image (thumbnail)
    api_url = (
        f"https://en.wikipedia.org/w/api.php?"
        f"action=query&titles={quote(search_term)}&prop=pageimages"
        f"&pithumbsize={MAX_SIZE}&format=json&redirects=1"
    )
    result = subprocess.run(
        ["curl", "-s", "-A", "IntelConsole/1.0 (OSINT research)", api_url],
        capture_output=True, text=True,
    )
    try:
        data = json.loads(result.stdout)
        pages = data.get("query", {}).get("pages", {})
        for pid, page in pages.items():
            if pid == "-1":
                continue
            thumb = page.get("thumbnail", {}).get("source")
            if thumb:
                return thumb
    except (json.JSONDecodeError, KeyError) as e:
        print(f"  [wiki fallback error] {search_term}: {e}")
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


def get_missing_people():
    """Get person entities without photos from graph.json."""
    with open(STATIC_DATA / "graph.json") as f:
        graph = json.load(f)
    missing = []
    for n in graph["nodes"]:
        if n.get("entity_type") == "person" and not n.get("photo_url"):
            missing.append(n["name"])
    return sorted(missing)


def update_db(downloaded):
    """Write photo_url into DB metadata so exports preserve them."""
    import sqlite3
    db_path = Path(__file__).parent.parent / "data" / "intel.db"
    if not db_path.exists():
        return 0
    photo_map = {name: fname for name, fname in downloaded}
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, name, metadata FROM entities")
    updated = 0
    for eid, name, meta_str in cur.fetchall():
        if name not in photo_map:
            continue
        meta = {}
        if meta_str:
            try:
                meta = json.loads(meta_str)
            except (json.JSONDecodeError, TypeError):
                meta = {}
        if not isinstance(meta, dict):
            meta = {}
        meta["photo_url"] = f"/static/photos/{photo_map[name]}"
        cur.execute("UPDATE entities SET metadata = ? WHERE id = ?",
                    (json.dumps(meta), eid))
        updated += 1
    conn.commit()
    conn.close()
    return updated


def main():
    dry_run = "--dry-run" in sys.argv
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

    # Auto-populate from graph data
    todo = get_missing_people()
    # Filter to only those without photos on disk already
    todo = [name for name in todo if not (PHOTOS_DIR / name_to_filename(name)).exists()]

    print(f"Searching for photos of {len(todo)} people...")
    print(f"{'='*60}")

    # Phase 1: Search Wikimedia Commons (skip known bad matches)
    found = {}       # name -> wiki_filename
    wiki_direct = {} # name -> direct URL (from Wikipedia fallback)
    not_found = []
    for i, name in enumerate(todo):
        search_term = SEARCH_OVERRIDES.get(name, name)
        wiki_file = None
        if name not in WIKIMEDIA_SKIP:
            wiki_file = search_wikimedia(search_term)
        if wiki_file:
            found[name] = wiki_file
            print(f"  [{i+1}/{len(todo)}] {name}: {wiki_file}")
        else:
            # Fallback: try Wikipedia page image (use actual name, not search override)
            wp_url = search_wikipedia_image(name)
            if wp_url:
                wiki_direct[name] = wp_url
                print(f"  [{i+1}/{len(todo)}] {name}: [Wikipedia] {wp_url[:80]}...")
            else:
                not_found.append(name)
                print(f"  [{i+1}/{len(todo)}] {name}: [not found]")
        time.sleep(API_DELAY)

    print(f"\n  Wikimedia: {len(found)}, Wikipedia: {len(wiki_direct)}, Not found: {len(not_found)}")

    if dry_run:
        print("\n[DRY RUN] Would download:")
        for name in sorted(list(found.keys()) + list(wiki_direct.keys())):
            src = found.get(name) or wiki_direct.get(name, "")[:80]
            print(f"  {name}: {src}")
        if not_found:
            print(f"\nNot found ({len(not_found)}):")
            for name in not_found:
                print(f"  {name}")
        return

    # Phase 2: Download from Wikimedia Commons
    print(f"\n--- Downloading {len(found) + len(wiki_direct)} photos ---")
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

    # Phase 2b: Download from Wikipedia direct URLs
    for i, (name, url) in enumerate(wiki_direct.items()):
        out_file = name_to_filename(name)
        if (PHOTOS_DIR / out_file).exists():
            print(f"  [skip] {out_file} already exists")
            downloaded.append((name, out_file))
            continue

        ok = download_and_resize(url, out_file)
        if ok:
            downloaded.append((name, out_file))
        else:
            failed.append(name)

        if i < len(wiki_direct) - 1:
            time.sleep(DOWNLOAD_DELAY)

    # Phase 3: Update JSON + DB
    if downloaded:
        ue, un = update_json(downloaded)
        ud = update_db(downloaded)
        print(f"\n  Updated {ue} entities, {un} graph nodes, {ud} DB rows")

    print(f"\n{'='*60}")
    print(f"  Downloaded: {len(downloaded)}")
    print(f"  Failed: {len(failed)}")
    print(f"  Not found: {len(not_found)}")

    if failed:
        print(f"\n  Failed downloads: {', '.join(failed)}")
    if not_found:
        print(f"\n  Not found anywhere: {', '.join(not_found)}")

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
