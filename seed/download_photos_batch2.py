"""Download photos for remaining 96 people from Wikimedia Commons.

Usage:
    python3 -m seed.download_photos_batch2

Downloads photos, resizes to 400px max, saves to static/photos/,
then updates entities.json and graph.json with photo_url metadata.
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
DOWNLOAD_DELAY = 4
API_DELAY = 1


# ── Batch definitions ────────────────────────────────────────────
# { "Entity Name": ("wikimedia_filename", "output_file.jpg") }

BATCH_6 = {
    "Albert Pike": ("Albert_Pike_-_Brady-Handy.jpg", "albert_pike.jpg"),
    "Alexander Nix": ("Alexander_Nix_CEO_of_Cambridge_Analytica.jpg", "alexander_nix.jpg"),
    "Andrija Puharich": ("Andrija_Puharich.jpg", "andrija_puharich.jpg"),
    "Bo Gritz": ("Bo_Gritz.jpg", "bo_gritz.jpg"),
    "Bruce Ivins": ("Bruce_E._Ivins.jpg", "bruce_ivins.jpg"),
    "Cardinal Bernard Law": ("BernardLaw.jpg", "bernard_law.jpg"),
    "Christopher Wylie": ("Christopher_Wylie_at_Chatham_House_-_2018_(42906940691)_(cropped).jpg", "christopher_wylie.jpg"),
    "Cyril Smith": ("Official_portrait_of_Cyril_Smith.jpg", "cyril_smith.jpg"),
    "David Atlee Phillips": ("David_Atlee_Phillips.jpg", "david_atlee_phillips.jpg"),
    "David Fravor": ("David_Fravor_in_2023_(cropped).jpg", "david_fravor.jpg"),
    "Dean Radin": ("Dean_Radin_March_2008.jpg", "dean_radin.jpg"),
    "Edgar Cayce": ("Edgar_Cayce.jpg", "edgar_cayce.jpg"),
    "Edgar Mitchell": ("Edgar_Mitchell_cropped.jpg", "edgar_mitchell.jpg"),
    "Enrique Camarena": ("Enrique_Camarena_Salazar.jpg", "enrique_camarena.jpg"),
    "Flinders Petrie": ("Flinders_Petrie.jpg", "flinders_petrie.jpg"),
    "Frank Olson": ("Frank_Olson.png", "frank_olson.jpg"),
    "Freeway Rick Ross": ("Freeway_Rick_Ross.jpg", "freeway_rick_ross.jpg"),
    "George de Mohrenschildt": ("De_Mohrenschildt_in_1964.png", "george_de_mohrenschildt.jpg"),
    "Harlan Crow": ("Harlan_Crow_(cropped).jpg", "harlan_crow.jpg"),
    "Ingo Swann": ("Ingo_Swann.jpg", "ingo_swann.jpg"),
    "John Bolton": ("John_R._Bolton_official_photo.jpg", "john_bolton.jpg"),
    "John Casablancas": ("John_Casablancas.jpg", "john_casablancas.jpg"),
    "John DeCamp": ("John_DeCamp_at_the_Pentagon.jpg", "john_decamp.jpg"),
    "Joseph McMoneagle": ("Joseph_McMoneagle.jpg", "joseph_mcmoneagle.jpg"),
    "Keith Raniere": ("Keith_Raniere_2_(cropped).jpg", "keith_raniere.jpg"),
    "Licio Gelli": ("Licio_Gelli_crop.jpg", "licio_gelli.jpg"),
    "Manly P. Hall": ("Manly_Palmer_Hall.jpg", "manly_p_hall.jpg"),
    "Marc Dutroux": ("Marc_Dutroux.jpg", "marc_dutroux.jpg"),
    "Nikola Tesla": ("N.Tesla.JPG", "nikola_tesla.jpg"),
    "Ralph Baric": ("Ralph_Baric.jpg", "ralph_baric.jpg"),
    "Robert Mercer": ("Robert_Mercer.jpg", "robert_mercer.jpg"),
    "Robert Monroe": ("Robert_A._Monroe.jpg", "robert_monroe.jpg"),
    "Roberto Calvi": ("Roberto_Calvi.jpg", "roberto_calvi.jpg"),
    "Shirō Ishii": ("Gruesome_War_Criminals_(Shiro_Ishii).jpg", "shiro_ishii.jpg"),
    "T. Boone Pickens": ("T._Boone_Pickens,_Jr._(cropped).jpg", "t_boone_pickens.jpg"),
    "Thomas Drake": ("Thomas_drake_nsa.jpg", "thomas_drake.jpg"),
    "Thomas Townsend Brown": ("Thomas_Townsend_Brown.jpg", "thomas_townsend_brown.jpg"),
    "Vandana Shiva": ("Vandana_Shiva,_2023_(cropped).jpg", "vandana_shiva.jpg"),
    "William Donovan": ("William_Donovan_circa_1945_(cropped).jpg", "william_donovan.jpg"),
    "Zecharia Sitchin": ("Zecharia_Sitchin_(2009).jpg", "zecharia_sitchin.jpg"),
}

BATCH_7 = {
    "Albert Mackey": ("Albert_Mackey.jpg", "albert_mackey.jpg"),
    "Bev Harris": ("Bev_Harris.jpg", "bev_harris.jpg"),
    "Cele Castillo": ("Celerino_Castillo_III.jpg", "cele_castillo.jpg"),
    "Clint Curtis": ("Clinton_Eugene_Curtis.jpg", "clint_curtis.jpg"),
    "Colm Kelleher": ("Colm_Kelleher.jpg", "colm_kelleher.jpg"),
    "Dale Graff": ("Dale_Graff.jpg", "dale_graff.jpg"),
    "David Morehouse": ("David_Morehouse.jpg", "david_morehouse.jpg"),
    "Ed Dames": ("Ed_Dames.jpg", "ed_dames.jpg"),
    "Edwin May": ("Edwin_C._May.jpg", "edwin_may.jpg"),
    "Eugene Mallove": ("Eugene_Mallove.jpg", "eugene_mallove.jpg"),
    "Hugh Grant": ("Hugh_Grant_2014.jpg", "hugh_grant.jpg"),
    "Jim Channon": ("Jim_Channon.jpg", "jim_channon.jpg"),
    "Jim Marrs": ("Jim_Marrs_2014.jpg", "jim_marrs.jpg"),
    "John Anthony West": ("John_Anthony_West.jpg", "john_anthony_west.jpg"),
    "John Hutchison": ("John_Hutchison.jpg", "john_hutchison.jpg"),
    "Ken Alibek": ("Ken_Alibek.jpg", "ken_alibek.jpg"),
    "Khun Sa": ("Khun_Sa.jpg", "khun_sa.jpg"),
    "Leon Brittan": ("Leon_Brittan_1986_(cropped).jpg", "leon_brittan.jpg"),
    "Lyn Buchanan": ("Lyn_Buchanan.jpg", "lyn_buchanan.jpg"),
    "Martin Fleischmann": ("Martin_Fleischmann.jpg", "martin_fleischmann.jpg"),
    "Maude Barlow": ("Maude_Barlow_-_Jan_2015.jpg", "maude_barlow.jpg"),
    "Michael Levine": ("Michael_Levine_(author).jpg", "michael_levine.jpg"),
    "Michael Tellinger": ("Michael_Tellinger.jpg", "michael_tellinger.jpg"),
    "Norwin Meneses": ("Norwin_Meneses.jpg", "norwin_meneses.jpg"),
    "Paul Bonacci": ("Paul_Bonacci.jpg", "paul_bonacci.jpg"),
    "Paul Smith": ("Paul_H._Smith.jpg", "paul_smith_rv.jpg"),
    "Percy Schmeiser": ("Percy_Schmeiser_at_the_Right_Livelihood_Award_2007.jpg", "percy_schmeiser.jpg"),
    "Peter Ball": ("Peter_Ball_(bishop).jpg", "peter_ball.jpg"),
    "Peter Brabeck-Letmathe": ("Peter_Brabeck-Letmathe_-_World_Economic_Forum_Annual_Meeting_2011.jpg", "peter_brabeck.jpg"),
    "Peter Hayman": ("Peter_Hayman_(diplomat).jpg", "peter_hayman.jpg"),
    "Robert Fraley": ("Robert_T._Fraley.jpg", "robert_fraley.jpg"),
    "Stanley Pons": ("Stanley_Pons.jpg", "stanley_pons.jpg"),
    "Tyrone Hayes": ("Tyrone_Hayes.jpg", "tyrone_hayes.jpg"),
    "Walter Cruttenden": ("Walter_Cruttenden.jpg", "walter_cruttenden.jpg"),
    "William Patrick III": ("William_C._Patrick_III.jpg", "william_patrick_iii.jpg"),
}

# These people likely don't have Wikimedia photos or are too obscure:
# Alois Zwinggi, Angela Dellafiora Ford, Brien Foerster, Christopher Dunn,
# Claude Haddad, James Lacatski, Jessica Utts, Kenneth Shapiro, Kit Green,
# Oscar Danilo Blandon, P.D. Houston, Peter Scully, Philippa Sigl-Glöckner,
# Rosemary Vrablic, Stanley Meyer, Stuart Roffey, Tammy McFadden,
# Thomas Bowers, Thomas Valone, Val Broeksmit, William Broeksmit

ALL_BATCHES = [
    ("Batch 6", BATCH_6),
    ("Batch 7", BATCH_7),
]


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


def run_batch(batch_name, batch_data):
    """Download and link one batch."""
    todo = {}
    for name, (wiki_file, out_file) in batch_data.items():
        if not (PHOTOS_DIR / out_file).exists():
            todo[name] = (wiki_file, out_file)

    if not todo:
        print(f"\n=== {batch_name}: All {len(batch_data)} photos already exist ===")
        # Still update JSON for any that exist but aren't linked
        downloaded = [(name, out_file) for name, (_, out_file) in batch_data.items()
                      if (PHOTOS_DIR / out_file).exists()]
        if downloaded:
            ue, un = update_json(downloaded)
            print(f"  Linked {ue} entities, {un} graph nodes")
        return 0

    print(f"\n{'='*60}")
    print(f"  {batch_name}: {len(todo)} to download ({len(batch_data) - len(todo)} already exist)")
    print(f"{'='*60}")

    # Phase 1: Resolve URLs
    print(f"\n--- Resolving Wikimedia URLs ---")
    urls = {}
    for name, (wiki_file, out_file) in todo.items():
        url = get_wiki_url(wiki_file)
        if url:
            urls[name] = (url, out_file)
            print(f"  {name}: OK")
        else:
            print(f"  {name}: [!] not found on Wikimedia")
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

    # Also count pre-existing files for JSON update
    for name, (wiki_file, out_file) in batch_data.items():
        if name not in dict(downloaded) and (PHOTOS_DIR / out_file).exists():
            downloaded.append((name, out_file))

    # Phase 3: Update JSON
    if downloaded:
        ue, un = update_json(downloaded)
        print(f"\n  Updated {ue} entities, {un} graph nodes")

    print(f"\n  Results: {len(downloaded)} OK, {len(failed)} failed")
    if failed:
        print(f"  Failed: {', '.join(failed)}")

    return len(downloaded)


def main():
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

    if len(sys.argv) > 1:
        batch_num = int(sys.argv[1])
        if 1 <= batch_num <= len(ALL_BATCHES):
            name, data = ALL_BATCHES[batch_num - 1]
            run_batch(name, data)
        else:
            print(f"Invalid batch number. Use 1-{len(ALL_BATCHES)}")
            sys.exit(1)
    else:
        total = 0
        for name, data in ALL_BATCHES:
            total += run_batch(name, data)
        print(f"\n{'='*60}")
        print(f"  TOTAL: {total} photos processed")

        with open(STATIC_DATA / "entities.json") as f:
            entities = json.load(f)
        with_photo = sum(1 for e in entities.values()
                        if (e.get("metadata", {}) if isinstance(e.get("metadata", {}), dict)
                            else json.loads(e.get("metadata", "{}"))).get("photo_url"))
        print(f"  Entities with photos: {with_photo}/{len(entities)}")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
