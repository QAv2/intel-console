"""Download entity photos from Wikimedia Commons in batches.

Usage:
    python3 -m seed.download_photos_batch

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
DOWNLOAD_DELAY = 4  # seconds between CDN downloads
API_DELAY = 1  # seconds between API calls


# ── Batch definitions ────────────────────────────────────────────
# Each batch: { "Entity Name": ("wikimedia_filename", "output_file.jpg") }

BATCH_1 = {
    "Allen Dulles": ("Allen_W._Dulles_(cropped).jpg", "allen_dulles.jpg"),
    "Anderson Cooper": ("Anderson_Cooper_crop.jpg", "anderson_cooper.jpg"),
    "Andrew Carnegie": ("Andrew_Carnegie,_three-quarter_length_portrait,_seated,_facing_slightly_left,_1913.jpg", "andrew_carnegie.jpg"),
    "Anthony Fauci": ("Anthony_Fauci_in_2023_02_(cropped).jpg", "anthony_fauci.jpg"),
    "Aleister Crowley": ("Aleister_Crowley,_thinker.jpg", "aleister_crowley.jpg"),
    "Ali Khamenei": ("Ali_Khamenei_crop.jpg", "ali_khamenei.jpg"),
    "Albert Stubblebine": ("Albert_Stubblebine_(US_Army_major_general).jpg", "albert_stubblebine.jpg"),
    "Anton LaVey": ("Anton_LaVey,_1959.jpg", "anton_lavey.jpg"),
    "Averell Harriman": ("Averell_Harriman_(1)_Edit.jpg", "averell_harriman.jpg"),
    "Ben Bernanke": ("Ben_Bernanke_official_portrait.jpg", "ben_bernanke.jpg"),
    "Bill Gates": ("Bill_Gates_2017_(cropped).jpg", "bill_gates.jpg"),
    "Bob Graham": ("Bob_Graham,_official_Senate_photo_portrait,_color.jpg", "bob_graham.jpg"),
    "Carl Bernstein": ("Carl_bernstein_2007.jpg", "carl_bernstein.jpg"),
    "Carlos Marcello": ("YoungCarlosMarcello2.jpg", "carlos_marcello.jpg"),
    "Chelsea Manning": ("Chelsea_Manning_on_18_May_2017.jpg", "chelsea_manning.jpg"),
    "Chuck Schumer": ("Chuck_Schumer_official_photo.jpg", "chuck_schumer.jpg"),
    "Condoleezza Rice": ("Condoleezza_Rice_cropped.jpg", "condoleezza_rice.jpg"),
    "David Rockefeller": ("David_Rockefeller,_1984_(cropped).jpg", "david_rockefeller.jpg"),
    "Dwight D. Eisenhower": ("Dwight_D._Eisenhower,_official_photo_portrait,_May_29,_1959.jpg", "dwight_eisenhower.jpg"),
    "Edward Bernays": ("Edward_Bernays_and_Doris_E._Fleischman_-_gros_plan.png", "edward_bernays.jpg"),
    "Edward Snowden": ("Edward_Snowden-2.jpg", "edward_snowden.jpg"),
    "Erik Prince": ("Erik_Prince.jpg", "erik_prince.jpg"),
    "Fred Hampton": ("Fred_Hampton_speaks_at_a_rally_in_Grant_Park,_Chicago,_1969_crop.jpg", "fred_hampton.jpg"),
    "George Soros": ("George_Soros_-_Festival_Economia_2012_01.JPG", "george_soros.jpg"),
    "George Tenet": ("George_Tenet_portrait_headshot.jpg", "george_tenet.jpg"),
    "Hank Paulson": ("Henry_Paulson_official_Treasury_photo,_2006.jpg", "hank_paulson.jpg"),
    "Harlan Crow": ("Harlan_Crow_(cropped).jpg", "harlan_crow.jpg"),
    "Henry Kissinger": ("Henry_A._Kissinger,_U.S._Secretary_of_State,_1973-1977.jpg", "henry_kissinger_official.jpg"),
    "Jack Ruby": ("Jack_Ruby-1.jpg", "jack_ruby.jpg"),
    "Jeff Bezos": ("Jeff_Bezos_at_Amazon_Spheres_Grand_Opening_in_Seattle_-_2018_(39074799225)_(cropped3).jpg", "jeff_bezos.jpg"),
}

BATCH_2 = {
    "Julian Assange": ("Julian_Assange_full.jpg", "julian_assange.jpg"),
    "Keith Alexander": ("Keith_B._Alexander_official_portrait.jpg", "keith_alexander.jpg"),
    "Klaus Schwab": ("Klaus_Schwab_WEF_2008_(cropped).jpg", "klaus_schwab.jpg"),
    "L. Ron Hubbard": ("L._Ron_Hubbard_in_1950_(cropped).jpg", "l_ron_hubbard.jpg"),
    "Larry Fink": ("Laurence_Douglas_Fink_(cropped).jpg", "larry_fink.jpg"),
    "Larry King": ("Larry_King_by_Gage_Skidmore_2.jpg", "larry_king.jpg"),
    "Lee Harvey Oswald": ("Lee_Harvey_Oswald_1963.jpg", "lee_harvey_oswald.jpg"),
    "Martin Luther King Jr.": ("Martin_Luther_King,_Jr..jpg", "martin_luther_king.jpg"),
    "Nelson Rockefeller": ("Nelson_Rockefeller.jpg", "nelson_rockefeller.jpg"),
    "Osama bin Laden": ("Osama_bin_Laden_portrait.jpg", "osama_bin_laden.jpg"),
    "Prescott Bush": ("PrescottBush.jpg", "prescott_bush.jpg"),
    "Richard Clarke": ("Richard_Clarke.jpg", "richard_clarke.jpg"),
    "Robert F. Kennedy": ("Robert_F._Kennedy_1964.jpeg", "robert_f_kennedy.jpg"),
    "Robert Rubin": ("Robert_Rubin_headshot.jpg", "robert_rubin.jpg"),
    "Rupert Murdoch": ("Rupert_Murdoch_2011_Shankbone_3.JPG", "rupert_murdoch.jpg"),
    "Sam Giancana": ("Sam_Giancana.jpg", "sam_giancana.jpg"),
    "Santos Trafficante": ("Santo_Trafficante,_Jr.jpg", "santos_trafficante.jpg"),
    "Sirhan Sirhan": ("Sirhan_Sirhan_in_2021.jpg", "sirhan_sirhan.jpg"),
    "Smedley Butler": ("SmedleyButler.jpeg", "smedley_butler.jpg"),
    "Timothy Geithner": ("Timothy_Geithner_official_portrait.jpg", "timothy_geithner.jpg"),
    "Wernher von Braun": ("Wernher_von_Braun_1960.jpg", "wernher_von_braun.jpg"),
    "Zbigniew Brzezinski": ("Zbigniew_Brzezinski,_1977.jpg", "zbigniew_brzezinski.jpg"),
    "Lyman Lemnitzer": ("Lyman_L._Lemnitzer.jpg", "lyman_lemnitzer.jpg"),
    "John D. Rockefeller": ("John_D._Rockefeller_1885.jpg", "john_d_rockefeller.jpg"),
    "J.P. Morgan": ("J.P._Morgan.jpg", "jp_morgan.jpg"),
    "Paul Warburg": ("Paul_M._Warburg_LCCN2016821709_(cropped).jpg", "paul_warburg.jpg"),
    "Frank Wisner": ("Frank_G._Wisner_as_Ambassador.png", "frank_wisner.jpg"),
    "David Ferrie": ("JFKferrie2.jpg", "david_ferrie.jpg"),
    "Jim Garrison": ("Garrison_Jim.jpg", "jim_garrison.jpg"),
    "Clay Shaw": ("Clay_Shaw.jpg", "clay_shaw.jpg"),
}

BATCH_3 = {
    "E. Howard Hunt": ("E._Howard_Hunt_(cropped).jpg", "e_howard_hunt.jpg"),
    "Guy Banister": ("Guy_Banister_photo_from_House_Select_Committee_on_Assassination.jpg", "guy_banister.jpg"),
    "Jack Parsons": ("Jack_Parsons_2.jpg", "jack_parsons.jpg"),
    "Jacobo Árbenz": ("Jacobo_Arbenz_1951_(cropped).jpg", "jacobo_arbenz.jpg"),
    "James Earl Ray": ("James_Earl_Ray_1968_Photograph.jpg", "james_earl_ray.jpg"),
    "John McCone": ("John_McCone.jpg", "john_mccone.jpg"),
    "Khalid Sheikh Mohammed": ("Khalid_Shaikh_Mohammed_after_capture.jpg", "khalid_sheikh_mohammed.jpg"),
    "Luis Elizondo": ("Luis_Elizondo.jpg", "luis_elizondo.jpg"),
    "Michael Aquino": ("Michael_A._Aquino.jpg", "michael_aquino.jpg"),
    "Mohamed Atta": ("Mohamed_Atta.jpg", "mohamed_atta.jpg"),
    "Mohammad Mossadegh": ("Prime_Minister_Mohammed_Mossadegh_of_Iran_speaking_with_Dean_Acheson.jpg", "mohammad_mossadegh.jpg"),
    "Norman Augustine": ("Norman_Ralph_Augustine.jpg", "norman_augustine.jpg"),
    "Philip Zelikow": ("Philip_D_Zelikow,_University_of_Virginia_(4799290374).jpg", "philip_zelikow.jpg"),
    "David Grusch": ("David_Grusch_giving_testimony_on_26_July_2023_before_the_US_House_Subcommittee_on_National_Security_the_Border_and_Foreign_Affairs.png", "david_grusch.jpg"),
    "Ryan Graves": ("Ryan_Graves.jpg", "ryan_graves.jpg"),
    "Graham Hancock": ("Graham-Hancock_(cropped).jpg", "graham_hancock.jpg"),
    "Hal Puthoff": ("Hal_Puthoff.png", "hal_puthoff.jpg"),
    "Jacques Vallée": ("Jacques_Vallée_by_Christopher_Michel_12112024_4.jpg", "jacques_vallee.jpg"),
    "Robert Bigelow": ("Robert_Bigelow.jpg", "robert_bigelow.jpg"),
    "Peter Daszak": ("Peter_Daszak_2017_01.jpg", "peter_daszak.jpg"),
    "Steven Greer": ("Dr_Steven_Greer_Picwiki.jpg", "steven_greer.jpg"),
    "William Binney": ("William_Binney-IMG_9040.jpg", "william_binney.jpg"),
    "Sibel Edmonds": ("Sibel_edmonds_on_RT.png", "sibel_edmonds.jpg"),
}

BATCH_4 = {
    "Admiral Thomas Moorer": ("KN-15045_Admiral_Thomas_H._Moorer,_USN_(cropped).jpg", "thomas_moorer.jpg"),
    "Arthur Sackler": ("Arthur_M._Sackler.jpg", "arthur_sackler.jpg"),
    "Børge Brende": ("Børge_Brende_on_October_17,_2023_(cropped).jpg", "borge_brende.jpg"),
    "Daniele Ganser": ("Dr._Daniele_Ganser_(cropped)_JD.jpg", "daniele_ganser.jpg"),
    "Donald Ewen Cameron": ("Donald_Ewen_Cameron_canmedaj01237-0046-a.jpg", "donald_ewen_cameron.jpg"),
    "Dorothy Kilgallen": ("Dorothy_Kilgallen_1952.png", "dorothy_kilgallen.jpg"),
    "George Knapp": ("George_Knapp_(8221331696)_(cropped).jpg", "george_knapp.jpg"),
    "Masoud Pezeshkian": ("Masoud_Pezeshkian_2024.jpg", "masoud_pezeshkian.jpg"),
    "Mike Rounds": ("Mike_Rounds_official_Senate_portrait.jpg", "mike_rounds.jpg"),
    "Randall Carlson": ("Randall_Carlson_1969_yearbook_photograph.jpg", "randall_carlson.jpg"),
    "Robert Bauval": ("Robert_Bauval,_Belintash_2014.jpg", "robert_bauval.jpg"),
    "Robert Schoch": ("Robert_M._Schoch_in_Turkey,_Photo_by_Catherine_Ulissey.jpg", "robert_schoch.jpg"),
    "Royal Raymond Rife": ("Royal_Raymond_Rife_in_his_Lab_-_November_1929.jpg", "royal_raymond_rife.jpg"),
    "Russell Targ": ("Russell_Targ,_physicist.jpg", "russell_targ.jpg"),
    "Sidney Gottlieb": ("Sidney_Gottlieb_photo.jpg", "sidney_gottlieb.jpg"),
    "Tim Burchett": ("Rep._Tim_Burchett_official_photo,_116th_congress.jpg", "tim_burchett.jpg"),
    "Michael Cremo": ("Michael_Cremo.jpg", "michael_cremo.jpg"),
    "Daniel Sheehan": ("Daniel_Sheehan.png", "daniel_sheehan.jpg"),
    "Mark Klein": ("Mark_Klein.jpg", "mark_klein.jpg"),
    "Eric Davis": ("Eric_Davis.jpg", "eric_davis.jpg"),
    "Pat Price": ("Pat_Price.jpg", "pat_price.jpg"),
}

BATCH_5 = {
    "Abdul Rahim Mousavi": ("1th_Anniversary_of_awarding_the_Fadakari_badge_to_Imam_Ali_Military_University_25_(cropped).jpg", "abdul_rahim_mousavi.jpg"),
    "Ali Shamkhani": ("Ali_Shamkhani_by_Tasnim_01_(cropped).jpg", "ali_shamkhani.jpg"),
    "Aziz Nasirzadeh": ("Aziz_Nasirzadeh.jpg", "aziz_nasirzadeh.jpg"),
    "Danny Hilman Natawidjaja": ("Danny_Hilman_Natawidjaja_LIPI.jpg", "danny_hilman_natawidjaja.jpg"),
    "John Mack": ("John_Mack,_1986.jpg", "john_mack.jpg"),
    "Klaus Schmidt": ("Klaus_Schmidt_Monumento_2014_(cropped).jpg", "klaus_schmidt.jpg"),
    "Mohammad Pakpour": ("Sardar_Mohammad_Pakpour-by_Tasnimnews.com_02.jpg", "mohammad_pakpour.jpg"),
    "Nawaf al-Hazmi": ("Nawaf_al-Hazmi.jpg", "nawaf_al_hazmi.jpg"),
    "Khalid al-Mihdhar": ("Khalid_al-mihdhar_2.jpg", "khalid_al_mihdhar.jpg"),
}

# ── All batches ──────────────────────────────────────────────────
ALL_BATCHES = [
    ("Batch 1", BATCH_1),
    ("Batch 2", BATCH_2),
    ("Batch 3", BATCH_3),
    ("Batch 4", BATCH_4),
    ("Batch 5", BATCH_5),
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
    # Filter to only those not yet downloaded
    todo = {}
    for name, (wiki_file, out_file) in batch_data.items():
        if not (PHOTOS_DIR / out_file).exists():
            todo[name] = (wiki_file, out_file)

    if not todo:
        print(f"\n=== {batch_name}: All {len(batch_data)} photos already exist ===")
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

    # Select batch from CLI arg or run all
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

        # Final count
        with open(STATIC_DATA / "entities.json") as f:
            entities = json.load(f)
        with_photo = sum(1 for e in entities.values()
                        if e.get("metadata", {}).get("photo_url"))
        print(f"  Entities with photos: {with_photo}/{len(entities)}")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
