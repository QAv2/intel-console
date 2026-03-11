"""Download photos for remaining Ring 1 + Ring 2 gaps.

Targets all 24 Ring 1 missing + Ring 2 persons + Ring 2 orgs/programs.
Uses Wikimedia Commons curated filenames + search API fallback.

Usage:
    python3 -m seed.download_photos_remaining
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
DOWNLOAD_DELAY = 1.5
API_DELAY = 0.5


# ─────────────────────────────────────────────────────────────
# Curated Wikimedia Commons filenames
# Format: "DB Entity Name": ("Wiki_Filename.ext", "output.jpg")
# ─────────────────────────────────────────────────────────────

CURATED = {
    # ══════════════════════════════════════════════════════════
    # RING 1 — PERSONS (5)
    # ══════════════════════════════════════════════════════════
    "Ingo Swann": (
        "Ingo_Swann.jpg",
        "ingo_swann.jpg",
    ),
    "Robert Mercer": (
        "Robert_Mercer.jpg",
        "robert_mercer.jpg",
    ),
    "Thomas Townsend Brown": (
        "Thomas_Townsend_Brown.jpg",
        "thomas_townsend_brown.jpg",
    ),
    # William Patrick III — bioweapons expert, unlikely on Commons
    # Oscar Danilo Blandon — Contra drug trafficker, unlikely on Commons

    # ══════════════════════════════════════════════════════════
    # RING 1 — EVENTS (6)
    # ══════════════════════════════════════════════════════════
    "Pons-Fleischmann Cold Fusion Announcement": (
        "Martin_Fleischmann_and_Stanley_Pons_in_1989.jpg",
        "ponsfleischmann_cold_fusion_announcement.jpg",
    ),
    "Franklin Cover-Up": (
        "Boys_Town_entrance.jpg",
        "franklin_coverup.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # RING 1 — FACILITY (1)
    # ══════════════════════════════════════════════════════════
    "22 Avenue Foch": (
        "Avenue_Foch_from_Arc_de_Triomphe,_13_August_2013.jpg",
        "22_avenue_foch.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # RING 1 — ORGANIZATIONS (6)
    # ══════════════════════════════════════════════════════════
    "The Commission": (
        "Five_Families.svg",
        "the_commission.jpg",
    ),
    "ES&S": (
        "Election_Systems_&_Software_logo.svg",
        "ess.jpg",
    ),
    "Philadelphia Crime Family": (
        "Philadelphia_crime_family.svg",
        "philadelphia_crime_family.jpg",
    ),
    # Mega Group — private org, no Commons image expected
    # MC2 Model Management — defunct agency, no Commons image expected
    # Biopreparat — Soviet bioweapons, unlikely on Commons
    # Gaia, Inc. — streaming service, logo may not be on Commons

    # ══════════════════════════════════════════════════════════
    # RING 1 — PROGRAMS (4)
    # ══════════════════════════════════════════════════════════
    "PROMIS": (
        "Inslaw_PROMIS.jpg",
        "promis.jpg",
    ),
    "AAWSAP": (
        "AAWSAP_DIA_logo.png",
        "aawsap.jpg",
    ),
    "Project Stargate": (
        "Stargate_Project.svg",
        "project_stargate.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # RING 2 — PERSONS (23)
    # ══════════════════════════════════════════════════════════
    "Joseph McMoneagle": (
        "Joseph_McMoneagle.jpg",
        "joseph_mcmoneagle.jpg",
    ),
    "Dean Radin": (
        "Dean_Radin.jpg",
        "dean_radin.jpg",
    ),
    "Ed Dames": (
        "Ed_Dames.jpg",
        "ed_dames.jpg",
    ),
    "Brien Foerster": (
        "Brien_Foerster.jpg",
        "brien_foerster.jpg",
    ),
    "Christopher Dunn": (
        "Christopher_Dunn.jpg",
        "christopher_dunn.jpg",
    ),
    "John Anthony West": (
        "John_Anthony_West.jpg",
        "john_anthony_west.jpg",
    ),
    "Stanley Meyer": (
        "Stanley_Meyer.jpg",
        "stanley_meyer.jpg",
    ),
    "Stanley Pons": (
        "Stanley_Pons_1989.jpg",
        "stanley_pons.jpg",
    ),
    "John Casablancas": (
        "John_Casablancas.jpg",
        "john_casablancas.jpg",
    ),
    "Gérald Marie": (
        "Gérald_Marie.jpg",
        "grald_marie.jpg",
    ),
    "Peggy Siegal": (
        "Peggy_Siegal.jpg",
        "peggy_siegal.jpg",
    ),
    "Thomas Bowers": (
        "Thomas_Bowers_banker.jpg",
        "thomas_bowers.jpg",
    ),
    "Val Broeksmit": (
        "Val_Broeksmit.jpg",
        "val_broeksmit.jpg",
    ),
    "Michael Levine": (
        "Michael_Levine_(DEA).jpg",
        "michael_levine.jpg",
    ),
    "Eugene Mallove": (
        "Eugene_Mallove.jpg",
        "eugene_mallove.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # RING 2 — ORGANIZATIONS (31)
    # ══════════════════════════════════════════════════════════
    "Monroe Institute": (
        "The_Monroe_Institute.jpg",
        "monroe_institute.jpg",
    ),
    "Seagram": (
        "Seagram_Building.jpg",
        "seagram.jpg",
    ),
    "Black Cube": (
        "Black_Cube_(company)_logo.png",
        "black_cube.jpg",
    ),
    "Standard Oil": (
        "Standard_Oil_Co._Logo.svg",
        "standard_oil.jpg",
    ),
    "Kissinger Associates": (
        "Henry_Kissinger.jpg",
        "kissinger_associates.jpg",
    ),
    "Elite Model Management": (
        "Elite_Model_Management_logo.svg",
        "elite_model_management.jpg",
    ),
    "CITIC Group": (
        "CITIC_Group_logo.svg",
        "citic_group.jpg",
    ),
    "Nestlé Waters": (
        "Nestlé_logo.svg",
        "nestl_waters.jpg",
    ),
    "World Economic Forum": (
        "World_Economic_Forum_logo.svg",
        "world_economic_forum.jpg",
    ),
    "Crown Sterling": (
        "Crown_Sterling_logo.png",
        "crown_sterling.jpg",
    ),
    "Propaganda Due": (
        "P2-symbol.svg",
        "propaganda_due.jpg",
    ),
    "Sovereign Military Order of Malta": (
        "Coat_of_arms_of_the_Sovereign_Military_Order_of_Malta.svg",
        "sovereign_military_order_of_malta.jpg",
    ),
    "Dominion Voting Systems": (
        "Dominion_Voting_Systems_logo.svg",
        "dominion_voting_systems.jpg",
    ),
    "Bechtel Corporation": (
        "Bechtel_logo.svg",
        "bechtel_corporation.jpg",
    ),
    "Southern Air Transport": (
        "Southern_Air_Transport_Boeing_747.jpg",
        "southern_air_transport.jpg",
    ),
    "Smithsonian Institution": (
        "Smithsonian_logo_color.svg",
        "smithsonian_institution.jpg",
    ),
    "EcoHealth Alliance": (
        "EcoHealth_Alliance_logo.png",
        "ecohealth_alliance.jpg",
    ),
    "School of the Americas": (
        "School_of_the_Americas_entrance.jpg",
        "school_of_the_americas.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # RING 2 — PROGRAMS (14)
    # ══════════════════════════════════════════════════════════
    "Unit 731": (
        "Building_on_the_site_of_the_Gruesome_Unit_731.jpg",
        "unit_731.jpg",
    ),
    "Operation Ajax": (
        "Mossadegh_US04.jpg",
        "operation_ajax.jpg",
    ),
    "Operation Mockingbird": (
        "Operation_Mockingbird.jpg",
        "operation_mockingbird.jpg",
    ),
    "XKeyscore": (
        "XKeyscore_logo.svg",
        "xkeyscore.jpg",
    ),
    "AATIP": (
        "AATIP_slide.jpg",
        "aatip.jpg",
    ),
    "Project Blue Book": (
        "Project_Blue_Book_(sign).jpg",
        "project_blue_book.jpg",
    ),
    "Operation Fast and Furious": (
        "ATF_Fast_and_Furious.jpg",
        "operation_fast_and_furious.jpg",
    ),
    "Operation Condor": (
        "Operación_Cóndor.svg",
        "operation_condor.jpg",
    ),
    "Total Information Awareness": (
        "IAO-logo.png",
        "total_information_awareness.jpg",
    ),
    "ECHELON": (
        "Menwith-hill-radomes.jpg",
        "echelon.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # RING 2 — FACILITIES (2)
    # ══════════════════════════════════════════════════════════
    "Mena Airport": (
        "Mena_Intermountain_Municipal_Airport.jpg",
        "mena_airport.jpg",
    ),
    "Fordow Enrichment Plant": (
        "Fordow_Fuel_Enrichment_Plant.jpg",
        "fordow_enrichment_plant.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # RING 2 — EVENTS (21)
    # ══════════════════════════════════════════════════════════
    "MLK Assassination": (
        "Martin_Luther_King_Jr_Memorial.jpg",
        "mlk_assassination.jpg",
    ),
    "Maxwell Trial (2021)": (
        "Ghislaine_Maxwell_trial_sketch.jpg",
        "maxwell_trial_2021.jpg",
    ),
    "Bush v. Gore (2000)": (
        "Bush_v._Gore_(2000).jpg",
        "bush_v_gore_2000.jpg",
    ),
    "Citizens United v. FEC (2010)": (
        "Citizens_United_v._Federal_Election_Commission.jpg",
        "citizens_united_v_fec_2010.jpg",
    ),
    "Church Committee": (
        "Church_Committee.jpg",
        "church_committee_event.jpg",
    ),
    "Gulf of Tonkin Incident": (
        "Maddox_Tonkin.jpg",
        "gulf_of_tonkin_incident.jpg",
    ),
    "Amerithrax Investigation": (
        "Amerithrax_-_anthrax_letter.jpg",
        "amerithrax_investigation.jpg",
    ),
    "Banco Ambrosiano Collapse": (
        "Banco_Ambrosiano.jpg",
        "banco_ambrosiano_collapse.jpg",
    ),
    "BAE Al-Yamamah Deal": (
        "BAE_Systems_logo.svg",
        "bae_alyamamah_deal.jpg",
    ),
}


# ─────────────────────────────────────────────────────────────
# Search API targets — for entities without known Wiki filenames
# Uses Wikimedia Commons search to find relevant images
# ─────────────────────────────────────────────────────────────

SEARCH_TARGETS = {
    # Ring 1 events
    "2016 Russian Interference": ("Russian interference 2016 election", "2016_russian_interference.jpg"),
    "French Epstein Investigation": ("Epstein Paris investigation", "french_epstein_investigation.jpg"),
    "Operation Epic Fury": ("Iran 2026 military operation", "operation_epic_fury.jpg"),
    "Rothschild Surrealist Ball (1972)": ("Rothschild surrealist ball 1972", "rothschild_surrealist_ball_1972.jpg"),

    # Ring 1 orgs
    "Mega Group": ("Mega Group Bronfman Wexner", "mega_group.jpg"),
    "MC2 Model Management": ("MC2 Model Management", "mc2_model_management.jpg"),
    "Biopreparat": ("Biopreparat Soviet biological weapons", "biopreparat.jpg"),
    "Gaia, Inc.": ("Gaia TV streaming", "gaia_inc.jpg"),

    # Ring 1 persons
    "William Patrick III": ("William Patrick III bioweapons", "william_patrick_iii.jpg"),
    "Oscar Danilo Blandon": ("Blandon Contra drugs", "oscar_danilo_blandon.jpg"),

    # Ring 1 programs
    "Patent Secrecy Orders": ("Invention Secrecy Act patent", "patent_secrecy_orders.jpg"),

    # Ring 2 persons (remaining after curated)
    "Edwin May": ("Edwin May parapsychology", "edwin_may.jpg"),
    "Jessica Utts": ("Jessica Utts statistician", "jessica_utts.jpg"),
    "Paul Smith": ("Paul Smith remote viewing", "paul_smith.jpg"),
    "Angela Dellafiora Ford": ("Angela Ford remote viewing CIA", "angela_dellafiora_ford.jpg"),
    "Cele Castillo": ("Celerino Castillo DEA", "cele_castillo.jpg"),
    "Norwin Meneses": ("Norwin Meneses Contra", "norwin_meneses.jpg"),
    "Bev Harris": ("Bev Harris Black Box Voting", "bev_harris.jpg"),
    "Thomas Valone": ("Thomas Valone energy inventor", "thomas_valone.jpg"),

    # Ring 2 orgs (remaining)
    "Rose Law Firm": ("Rose Law Firm Little Rock", "rose_law_firm.jpg"),
    "Systematics": ("Systematics Inc Arkansas PROMIS", "systematics.jpg"),
    "Carbyne": ("Carbyne 911 technology Ehud Barak", "carbyne.jpg"),
    "Bayrock Group": ("Bayrock Group Trump Soho", "bayrock_group.jpg"),
    "Resorts International": ("Resorts International Atlantic City", "resorts_international.jpg"),
    "Hollinger International": ("Hollinger International Conrad Black", "hollinger_international.jpg"),
    "Towers Financial": ("Towers Financial Hoffenberg", "towers_financial.jpg"),
    "PSI Tech": ("PSI Tech remote viewing", "psi_tech.jpg"),
    "Nugan Hand Bank": ("Nugan Hand Bank CIA", "nugan_hand_bank.jpg"),
    "Lippo Group": ("Lippo Group Indonesia", "lippo_group.jpg"),
    "Safari Club": ("Safari Club intelligence", "safari_club.jpg"),
    "Pergamon Press": ("Pergamon Press Robert Maxwell", "pergamon_press.jpg"),
    "NIDS": ("National Institute Discovery Science Bigelow", "nids.jpg"),
    "Banque Rothschild": ("Banque Rothschild Paris", "banque_rothschild.jpg"),
    "Geological Society of America": ("Geological Society America logo", "geological_society_of_america.jpg"),
    "Murder Incorporated": ("Murder Inc organized crime", "murder_incorporated.jpg"),
    "S&A Concrete": ("S&A Concrete Trump mob", "sa_concrete.jpg"),
    "Gambino Crime Family": ("Gambino crime family", "gambino_crime_family.jpg"),
    "Genovese Crime Family": ("Genovese crime family", "genovese_crime_family.jpg"),
    "Karin Models": ("Karin Models Paris agency", "karin_models.jpg"),
    "Black Box Voting": ("Black Box Voting Bev Harris", "black_box_voting.jpg"),
    "SETCO Aviation": ("SETCO Aviation Honduras", "setco_aviation.jpg"),
    "Suez Group": ("Suez SA water utility", "suez_group.jpg"),

    # Ring 2 programs (remaining)
    "Project MKNaomi": ("MKNaomi CIA biological", "project_mknaomi.jpg"),
    "First Earth Battalion": ("First Earth Battalion Jim Channon", "first_earth_battalion.jpg"),
    "Project Grill Flame": ("Grill Flame remote viewing", "project_grill_flame.jpg"),
    "Project Center Lane": ("Center Lane DIA remote viewing", "project_center_lane.jpg"),
    "Project Alamo": ("Project Alamo Puthoff", "project_alamo.jpg"),
    "Gain-of-Function Research": ("gain-of-function virus research", "gainoffunction_research.jpg"),
    "Pentagon Military Analyst Program": ("Pentagon military analyst program", "pentagon_military_analyst_program.jpg"),
    "ThinThread": ("ThinThread NSA Binney", "thinthread.jpg"),

    # Ring 2 events (remaining)
    "Epstein Death (2019)": ("Epstein death MCC 2019", "epstein_death_2019.jpg"),
    "Commission Trial (1986)": ("Commission Trial 1986 mafia", "commission_trial_1986.jpg"),
    "Jean-Luc Brunel Death (2022)": ("Brunel death prison 2022", "jeanluc_brunel_death_2022.jpg"),
    "Unit 731 Immunity Deal": ("Unit 731 immunity MacArthur", "unit_731_immunity_deal.jpg"),
    "Cox Report (1999)": ("Cox Report China espionage", "cox_report_1999.jpg"),
    "Stargate Declassification": ("Stargate Project declassified CIA", "stargate_declassification.jpg"),
    "Mena Airport Operations": ("Mena Airport CIA drug smuggling", "mena_airport_operations.jpg"),
    "Brooks Brothers Riot (2000)": ("Brooks Brothers riot Florida 2000", "brooks_brothers_riot_2000.jpg"),
    "Halderman Report (2021)": ("Halderman voting machine report", "halderman_report_2021.jpg"),
    "Glass-Steagall Repeal": ("Glass-Steagall Act repeal", "glassssteagall_repeal.jpg"),
    "LIBOR Scandal": ("LIBOR scandal rate manipulation", "libor_scandal.jpg"),
    "Operation Midnight Hammer": ("Operation Midnight Hammer Iran", "operation_midnight_hammer.jpg"),
    "Kerry Committee Investigation": ("Kerry Committee drugs Contras", "kerry_committee_investigation.jpg"),
    "Westminster Dossier Disappearance": ("Westminster dossier child abuse", "westminster_dossier_disappearance.jpg"),
    "Independent Inquiry into Child Sexual Abuse": ("IICSA inquiry UK", "independent_inquiry_into_child_sexual_abuse.jpg"),
    "Newsnight Interview": ("Prince Andrew Newsnight interview", "newsnight_interview.jpg"),
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
            if pid == "-1":
                return None
            if "imageinfo" in page:
                info = page["imageinfo"][0]
                return info.get("thumburl") or info.get("url")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"  [API error] {wiki_filename}: {e}")
    return None


def search_commons(query, out_file):
    """Search Wikimedia Commons for an image matching query."""
    api_url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&list=search&srnamespace=6"
        f"&srsearch={quote(query)}&srlimit=5&format=json"
    )
    result = subprocess.run(
        ["curl", "-s", "-A", "IntelConsole/1.0 (OSINT research)", api_url],
        capture_output=True, text=True,
    )
    try:
        data = json.loads(result.stdout)
        results = data.get("query", {}).get("search", [])
        for r in results:
            title = r["title"]
            # Only accept image files
            lower = title.lower()
            if any(lower.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".svg", ".tif", ".tiff"]):
                # Get the URL
                wiki_filename = title.replace("File:", "")
                url = get_wiki_url(wiki_filename)
                if url:
                    return url
    except (json.JSONDecodeError, KeyError) as e:
        print(f"  [Search error] {query}: {e}")
    return None


def download_and_resize(url, filename):
    """Download and resize to 400px max, save as JPEG."""
    filepath = PHOTOS_DIR / filename
    if filepath.exists():
        print(f"  [skip] {filename} already exists")
        return True

    tmpfile = f"/tmp/photo_{filename}"
    ua = "IntelConsole/1.0 (OSINT research; contact: qav2@github)"

    result = subprocess.run(
        ["curl", "-s", "-o", tmpfile, "-w", "%{http_code}",
         "-L", "--max-time", "30", "-A", ua, url],
        capture_output=True, text=True,
    )
    code = result.stdout.strip()
    if code != "200":
        print(f"  [HTTP {code}] {filename}")
        return False

    try:
        img = Image.open(tmpfile)
        if img.mode in ("RGBA", "P", "LA"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            bg.paste(img, mask=img.split()[-1] if "A" in img.mode else None)
            img = bg
        elif img.mode != "RGB":
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
    """Update graph.json with photo URLs."""
    with open(STATIC_DATA / "graph.json") as f:
        graph = json.load(f)

    photo_map = {name: fname for name, fname in downloaded}

    updated = 0
    for node in graph["nodes"]:
        if node["name"] in photo_map and not node.get("photo_url"):
            node["photo_url"] = f"photos/{photo_map[node['name']]}"
            updated += 1

    with open(STATIC_DATA / "graph.json", "w") as f:
        json.dump(graph, f, indent=2)

    return updated


def main():
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

    downloaded = []

    # ── Phase 1: Curated Wikimedia filenames ──
    curated_todo = {}
    curated_skip = {}
    for name, (wiki_file, out_file) in CURATED.items():
        if (PHOTOS_DIR / out_file).exists():
            curated_skip[name] = out_file
        else:
            curated_todo[name] = (wiki_file, out_file)

    print(f"{'=' * 60}")
    print(f"Remaining Photo Gap Download")
    print(f"{'=' * 60}")
    print(f"  Curated: {len(CURATED)} ({len(curated_skip)} exist, {len(curated_todo)} to download)")
    print(f"  Search targets: {len(SEARCH_TARGETS)}")
    print()

    # Include pre-existing
    for name, out_file in curated_skip.items():
        downloaded.append((name, out_file))

    print(f"--- Phase 1: Curated downloads ({len(curated_todo)}) ---")
    for i, (name, (wiki_file, out_file)) in enumerate(curated_todo.items()):
        url = get_wiki_url(wiki_file)
        if url:
            ok = download_and_resize(url, out_file)
            if ok:
                downloaded.append((name, out_file))
            else:
                print(f"  [{i+1}] {name}: download failed")
        else:
            print(f"  [{i+1}] {name}: NOT FOUND on Commons ({wiki_file})")
        time.sleep(API_DELAY)

    # ── Phase 2: Search API ──
    search_todo = {}
    for name, (query, out_file) in SEARCH_TARGETS.items():
        if (PHOTOS_DIR / out_file).exists():
            downloaded.append((name, out_file))
        else:
            search_todo[name] = (query, out_file)

    print(f"\n--- Phase 2: Search API ({len(search_todo)}) ---")
    search_found = 0
    search_failed = []
    for i, (name, (query, out_file)) in enumerate(search_todo.items()):
        print(f"  [{i+1}/{len(search_todo)}] Searching: {name}...")
        url = search_commons(query, out_file)
        if url:
            ok = download_and_resize(url, out_file)
            if ok:
                downloaded.append((name, out_file))
                search_found += 1
            else:
                search_failed.append(name)
        else:
            search_failed.append(name)
            print(f"    No result for: {query}")
        time.sleep(DOWNLOAD_DELAY)

    # ── Phase 3: Update JSON ──
    if downloaded:
        updated = update_json(downloaded)
        print(f"\n  Updated {updated} graph nodes")

    # ── Summary ──
    curated_new = len([d for d in downloaded if d[0] in CURATED]) - len(curated_skip)
    print(f"\n{'=' * 60}")
    print(f"  RESULTS")
    print(f"{'=' * 60}")
    print(f"  Curated downloaded: {curated_new}")
    print(f"  Curated skipped:    {len(curated_skip)}")
    print(f"  Search found:       {search_found}")
    print(f"  Search failed:      {len(search_failed)}")
    print(f"  Total new:          {curated_new + search_found}")

    if search_failed:
        print(f"\n  Search failures:")
        for name in search_failed:
            print(f"    - {name}")

    # Final photo count
    with open(STATIC_DATA / "graph.json") as f:
        graph = json.load(f)
    existing = set(PHOTOS_DIR.iterdir())
    with_photo = sum(1 for n in graph["nodes"] if n.get("photo_url"))
    print(f"\n  Total entities with photos: {with_photo}/{len(graph['nodes'])}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
