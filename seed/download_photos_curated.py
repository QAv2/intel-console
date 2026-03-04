"""Download curated photos from Wikimedia — verified correct matches only.

Usage:
    python3 -m seed.download_photos_curated
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

# Verified correct Wikimedia filenames for remaining entities
CURATED = {
    # ── People: verified portraits ──
    "Alexander Nix": ("Web_Summit_2017_-_Centre_Stage_Day_3_SAM_7378_(38286774551)_(cropped).jpg", "alexander_nix.jpg"),
    "Andrija Puharich": ("Andrija_Puharich_parapsychologist.jpg", "andrija_puharich.jpg"),
    "Cardinal Bernard Law": ("Bernard_Francis_Law.jpg", "bernard_law.jpg"),
    "Edgar Cayce": ("Cayce_1910.jpg", "edgar_cayce.jpg"),
    "Enrique Camarena": ("Enrique-camarena1.jpg", "enrique_camarena.jpg"),
    "Frank Olson": ("Frank_Olsen_(1910-1953).jpg", "frank_olson.jpg"),
    "Licio Gelli": ("Licio_Gelli_in_paramenti.jpg", "licio_gelli.jpg"),
    "Manly P. Hall": ("Manly_P._Hall.jpg", "manly_p_hall.jpg"),
    "Shirō Ishii": ("Shiro_Ishii_at_a_reunion_party_of_Unit_731_members_after_the_war.png", "shiro_ishii.jpg"),
    "Vandana Shiva": ("Dr._Vandana_Shiva_DS.jpg", "vandana_shiva.jpg"),
    "William Donovan": ("William_Joseph_(Wild_Bill)_Donovan,_Head_of_the_OSS.jpg", "william_donovan.jpg"),
    "Albert Mackey": ("Albert_mackey.jpg", "albert_mackey.jpg"),
    "Clint Curtis": ("Clint_Curtis_2007.jpg", "clint_curtis.jpg"),
    "Jim Marrs": ("Jim_PR_2010.jpg", "jim_marrs.jpg"),
    "John Hutchison": ("John_Hutchison.png", "john_hutchison.jpg"),
    "Leon Brittan": ("Leon_Brittan_(1996).jpg", "leon_brittan.jpg"),
    "Michael Tellinger": ("Michael_Tellinger_Photo.jpeg", "michael_tellinger.jpg"),
    "Peter Brabeck-Letmathe": ("Peter_Brabeck-Letmathe.jpg", "peter_brabeck.jpg"),

    # ── Additional searches with corrected filenames ──
    "Christopher Wylie": ("Christopher_Wylie_speaks_at_the_Frontline_Club.jpg", "christopher_wylie.jpg"),
    "Cyril Smith": ("Cyril_Smith_(1972).jpg", "cyril_smith.jpg"),
    "David Fravor": ("Commander_David_Fravor.jpg", "david_fravor.jpg"),
    "George de Mohrenschildt": ("George_de_Mohrenschildt.jpg", "george_de_mohrenschildt.jpg"),
    "Keith Raniere": ("Keith_Raniere_mugshot.jpg", "keith_raniere.jpg"),
    "Marc Dutroux": ("Marc_Dutroux_mugshot.jpg", "marc_dutroux.jpg"),
    "Thomas Drake": ("Thomas_Andrews_Drake.jpg", "thomas_drake.jpg"),
    "Zecharia Sitchin": ("Zecharia_sitchin.jpg", "zecharia_sitchin.jpg"),
    "T. Boone Pickens": ("T._Boone_Pickens_2008.jpg", "t_boone_pickens.jpg"),
    "Robert Mercer": ("Robert_Mercer_(cropped).jpg", "robert_mercer.jpg"),
    "Robert Monroe": ("Robert_Monroe_portrait.jpg", "robert_monroe.jpg"),
    "Harlan Crow": ("Harlan_Crow_2012.jpg", "harlan_crow.jpg"),
    "Bo Gritz": ("James_Gordon_Gritz.jpg", "bo_gritz.jpg"),
    "David Atlee Phillips": ("David_Atlee_Phillips_CIA.jpg", "david_atlee_phillips.jpg"),
    "John Casablancas": ("John_Casablancas_1983.jpg", "john_casablancas.jpg"),
    "Ralph Baric": ("Ralph_S._Baric.jpg", "ralph_baric.jpg"),
    "Ingo Swann": ("Ingo_Swann_photo.jpg", "ingo_swann.jpg"),
    "Dean Radin": ("Dean_Radin.jpg", "dean_radin.jpg"),
    "Joseph McMoneagle": ("Joe_McMoneagle.jpg", "joseph_mcmoneagle.jpg"),
    "Maude Barlow": ("Maude_Barlow_2015.jpg", "maude_barlow.jpg"),
    "Percy Schmeiser": ("Percy_Schmeiser.jpg", "percy_schmeiser.jpg"),
    "Ken Alibek": ("Kanatjan_Alibekov.jpg", "ken_alibek.jpg"),
    "Tyrone Hayes": ("Tyrone_B._Hayes.jpg", "tyrone_hayes.jpg"),
    "Gérald Marie": ("Gérald_Marie.jpg", "gerald_marie.jpg"),
    "Freeway Rick Ross": ("Ricky_Donnell_Ross.jpg", "freeway_rick_ross.jpg"),
    "John DeCamp": ("John_DeCamp_Nebraska.jpg", "john_decamp.jpg"),
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

    # Filter to those not already on disk
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
