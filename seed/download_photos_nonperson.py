"""Download photos/logos/seals for non-person entities from Wikimedia Commons.

Covers agencies, facilities, organizations, events, programs, and foundations.
All images sourced from Wikimedia Commons (public domain, CC-BY, CC-BY-SA).

Usage:
    python3 -m seed.download_photos_nonperson
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
DOWNLOAD_DELAY = 2
API_DELAY = 0.5


# ─────────────────────────────────────────────────────────────
# Curated Wikimedia Commons filenames
# Format: "DB Entity Name": ("Wiki_Filename.ext", "output.jpg")
# ─────────────────────────────────────────────────────────────

CURATED = {
    # ══════════════════════════════════════════════════════════
    # AGENCIES — US gov seals are public domain
    # ══════════════════════════════════════════════════════════
    "ATF": (
        "Seal_of_the_Bureau_of_Alcohol,_Tobacco,_Firearms_and_Explosives.svg",
        "atf.jpg",
    ),
    "CDC": ("US_CDC_logo.svg", "cdc.jpg"),
    "CENTCOM": (
        "Seal_of_United_States_Central_Command.svg",
        "centcom.jpg",
    ),
    "CIA": (
        "Seal_of_the_Central_Intelligence_Agency.svg",
        "cia.jpg",
    ),
    "Crown Prosecution Service": (
        "Crown_Prosecution_Service_logo.svg",
        "crown_prosecution_service.jpg",
    ),
    "DARPA": ("DARPA_Logo.jpg", "darpa.jpg"),
    "DEA": (
        "Seal_of_the_United_States_Drug_Enforcement_Administration.svg",
        "dea.jpg",
    ),
    "DOE": (
        "Seal_of_the_United_States_Department_of_Energy.svg",
        "doe.jpg",
    ),
    "DOJ": (
        "Seal_of_the_United_States_Department_of_Justice.svg",
        "doj.jpg",
    ),
    "DTRA": ("US-DefenseThreatReductionAgency-Seal.svg", "dtra.jpg"),
    "FBI": (
        "Seal_of_the_Federal_Bureau_of_Investigation.svg",
        "fbi.jpg",
    ),
    "FDA": (
        "Logo_of_the_United_States_Food_and_Drug_Administration.svg",
        "fda.jpg",
    ),
    "FSB": ("Emblem_of_Federal_security_service.svg", "fsb.jpg"),
    "GCHQ": ("GCHQ_logo.svg", "gchq.jpg"),
    "Islamic Revolutionary Guard Corps": (
        "Seal_of_the_Army_of_the_Guardians_of_the_Islamic_Revolution.svg",
        "irgc.jpg",
    ),
    "MI5": ("MI5_crest_and_logotype.svg", "mi5.jpg"),
    "MI6": ("Secret_Intelligence_Service_logo.svg", "mi6.jpg"),
    "Metropolitan Police": (
        "Badge_of_the_Metropolitan_Police_Service.svg",
        "metropolitan_police.jpg",
    ),
    "Mossad": ("Mossad_seal.svg", "mossad.jpg"),
    "MSS": (
        "Ministry_of_State_Security_(China).svg",
        "mss.jpg",
    ),
    "NIH": ("US-NIH-NCCIH-Logo.svg", "nih.jpg"),
    "NSA": (
        "Seal_of_the_U.S._National_Security_Agency.svg",
        "nsa.jpg",
    ),
    "Quds Force": ("Flag_of_the_Quds_Force.svg", "quds_force.jpg"),
    "Saudi GID": (
        "Saudi_General_Intelligence_Presidency.png",
        "saudi_gid.jpg",
    ),
    "Unit 8200": ("8200_unit_logo.svg", "unit_8200.jpg"),
    "USAMRIID": (
        "Logo_of_the_United_States_Army_Medical_Research_Institute_of_Infectious_Diseases.svg",
        "usamriid.jpg",
    ),
    "USDA": (
        "Seal_of_the_United_States_Department_of_Agriculture.svg",
        "usda.jpg",
    ),
    "BND": ("Bundesnachrichtendienst_logo.svg", "bnd.jpg"),
    "Atomic Energy Organization of Iran": (
        "Seal_of_the_Atomic_Energy_Organization_of_Iran.svg",
        "aeoi.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # FACILITIES — location/building photos (CC-licensed)
    # ══════════════════════════════════════════════════════════
    "22 Avenue Foch": ("Paris_-_Avenue_Foch_-_20150530.jpg", "22_avenue_foch.jpg"),
    "Area 51": ("Wfm_area51_area51.jpg", "area_51.jpg"),
    "Baalbek": ("Baalbek-Bacchus.jpg", "baalbek.jpg"),
    "Carnac Stones": (
        "Alignements_du_Ménec_(Carnac).jpg",
        "carnac_stones.jpg",
    ),
    "Château de Ferrières": (
        "Château_de_Ferrières_(77).jpg",
        "chateau_de_ferrieres.jpg",
    ),
    "Dealey Plaza": ("Dealey_Plaza_2.jpg", "dealey_plaza.jpg"),
    "Derinkuyu": (
        "Derinkuyu_Underground_City_9843_Nevit.jpg",
        "derinkuyu.jpg",
    ),
    "Gobekli Tepe": ("Göbekli_Tepe,_Pair_of_pillars.jpg", "gobekli_tepe.jpg"),
    "Great Sphinx": (
        "Great_Sphinx_of_Giza_May_2015.JPG",
        "great_sphinx.jpg",
    ),
    "Gunung Padang": (
        "Gunung_Padang_Megalithic_Site.jpg",
        "gunung_padang.jpg",
    ),
    "House of the Temple": ("House_of_the_Temple.JPG", "house_of_the_temple.jpg"),
    "Mar-a-Lago": ("Mar-a-Lago_aerial.jpg", "mar_a_lago.jpg"),
    "MCC New York": ("MCC_New_York_jeh.JPG", "mcc_new_york.jpg"),
    "Mentmore Towers": ("Mentmore_Towers_01.jpg", "mentmore_towers.jpg"),
    "Nan Madol": ("Nan_Madol.jpg", "nan_madol.jpg"),
    "The Pentagon": (
        "The_Pentagon_January_2008.jpg",
        "the_pentagon.jpg",
    ),
    "Puma Punku": ("Puma_Punku.jpg", "puma_punku.jpg"),
    "Room 641A": ("Room_641A.jpg", "room_641a.jpg"),
    "Sacsayhuamán": (
        "Sacsayhuamán_Décembre_2006_-_Vue_Panoramique.jpg",
        "sacsayhuaman.jpg",
    ),
    "Skinwalker Ranch": ("Skinwalker_Ranch.jpg", "skinwalker_ranch.jpg"),
    "Teotihuacan": (
        "Piramide_del_Sol_-_Teotihuacán.jpg",
        "teotihuacan.jpg",
    ),
    "USS Abraham Lincoln": (
        "USS_Abraham_Lincoln_(CVN-72)_underway_in_the_Pacific_Ocean_on_22_February_2019_(190222-N-HD110-0127).jpg",
        "uss_abraham_lincoln.jpg",
    ),
    "USS Gerald R. Ford": (
        "USS_Gerald_R._Ford_(CVN-78)_underway_on_8_June_2017.jpg",
        "uss_gerald_r_ford.jpg",
    ),
    "Wardenclyffe Tower": (
        "Tesla_Broadcast_Tower_1904.jpeg",
        "wardenclyffe_tower.jpg",
    ),
    "World Trade Center": (
        "World_Trade_Center,_New_York_City_-_aerial_view_(March_2001).jpg",
        "world_trade_center.jpg",
    ),
    "Wright-Patterson AFB": (
        "Wright-Patterson_AFB_-_10sep2012.jpg",
        "wright_patterson_afb.jpg",
    ),
    "Yonaguni Monument": (
        "Yonaguni_Monument.jpg",
        "yonaguni_monument.jpg",
    ),
    "Zorro Ranch": (
        "GX-328_-_Zorro_Ranch.jpg",
        "zorro_ranch.jpg",
    ),
    "9 East 71st Street": (
        "9_East_71st_Street.jpg",
        "9_east_71st_street.jpg",
    ),
    "Fordow Enrichment Plant": (
        "Fordow_-_satellite_image_(2012).jpg",
        "fordow.jpg",
    ),
    "Natanz Nuclear Facility": (
        "Natanz_nuclear_enrichment_plant.jpg",
        "natanz.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # ORGANIZATIONS — logos, seals, flags
    # ══════════════════════════════════════════════════════════

    # Financial / Corporate
    "Federal Reserve System": (
        "Seal_of_the_United_States_Federal_Reserve_System.svg",
        "federal_reserve.jpg",
    ),
    "World Bank": ("World_Bank_logo.svg", "world_bank.jpg"),
    "International Monetary Fund": (
        "International_Monetary_Fund_logo.svg",
        "imf.jpg",
    ),
    "Goldman Sachs": ("Goldman_Sachs.svg", "goldman_sachs.jpg"),
    "JPMorgan Chase": ("JPMorgan_Chase.svg", "jpmorgan_chase.jpg"),
    "Deutsche Bank": ("Deutsche_Bank_logo_without_wordmark.svg", "deutsche_bank.jpg"),
    "BlackRock": ("BlackRock_wordmark.svg", "blackrock.jpg"),
    "Standard Oil": ("Standard_oil_co_logo.svg", "standard_oil.jpg"),
    "Carlyle Group": ("The_Carlyle_Group_Logo.svg", "carlyle_group.jpg"),
    "SWIFT": ("SWIFT_logo.svg", "swift.jpg"),
    "Citigroup": ("Citi.svg", "citigroup.jpg"),

    # Defense / MIC
    "Lockheed Martin": ("Lockheed_Martin.svg", "lockheed_martin.jpg"),
    "Northrop Grumman": (
        "Northrop_Grumman_logo_blue-on-clear_2020.svg",
        "northrop_grumman.jpg",
    ),
    "Raytheon": ("RTX_logo_2023.svg", "raytheon.jpg"),
    "Boeing Defense": ("Boeing_full_logo.svg", "boeing.jpg"),
    "General Dynamics": ("General_Dynamics_logo.svg", "general_dynamics.jpg"),
    "Halliburton": ("Halliburton_logo.svg", "halliburton.jpg"),
    "BAE Systems": ("BAE_Systems_logo.svg", "bae_systems.jpg"),
    "Blackwater": ("Xe_Services_logo.svg", "blackwater.jpg"),
    "Bechtel Corporation": ("Bechtel_logo.svg", "bechtel.jpg"),

    # Intelligence-adjacent
    "NATO": ("NATO_OTAN_landscape_logo.svg", "nato.jpg"),
    "WikiLeaks": ("Wikileaks_logo.svg", "wikileaks.jpg"),
    "Palantir Technologies": ("Palantir_Technologies_logo.svg", "palantir.jpg"),
    "In-Q-Tel": ("Logo_of_In-Q-Tel_(2010).svg", "in_q_tel.jpg"),
    "SRI International": ("SRI_International_logo.svg", "sri_international.jpg"),
    "Booz Allen Hamilton": ("Booz_Allen_Hamilton_logo.svg", "booz_allen_hamilton.jpg"),
    "SAIC": ("SAIC_logo.svg", "saic.jpg"),
    "Five Eyes": ("Five_Eyes.svg", "five_eyes.jpg"),
    "Cambridge Analytica": ("Cambridge_Analytica_logo.svg", "cambridge_analytica.jpg"),

    # Secret societies / Historical
    "Council on Foreign Relations": (
        "Council_on_Foreign_Relations.svg",
        "cfr.jpg",
    ),
    "Trilateral Commission": ("Trilateral_Commission_logo.svg", "trilateral.jpg"),
    "Bilderberg Group": ("Bilderberg_Hotel_Oosterbeek.jpg", "bilderberg.jpg"),
    "Bohemian Club": ("Bohemian_Club_logo.jpg", "bohemian_club.jpg"),
    "Skull and Bones": ("Bones_logo.jpg", "skull_and_bones.jpg"),
    "Knights Templar": ("Knights_Templar_Cross.svg", "knights_templar.jpg"),
    "Thule Society": ("Thule-Gesellschaft.svg", "thule_society.jpg"),
    "Sovereign Military Order of Malta": (
        "Insignia_Malta_Order_Sovereign_Military_Order_of_Malta.svg",
        "smom.jpg",
    ),
    "Ordo Templi Orientis": ("Lamen_of_O.T.O..svg", "oto.jpg"),
    "Scottish Rite Southern Jurisdiction": (
        "Scottish_Rite_of_Freemasonry_seal.svg",
        "scottish_rite.jpg",
    ),
    "Grand Orient de France": ("Grand_Orient_de_France_(logo).svg", "godf.jpg"),
    "United Grand Lodge of England": (
        "United_Grand_Lodge_of_England_logo.svg",
        "ugle.jpg",
    ),
    "Propaganda Due": ("Logo_P2_(Propaganda_Due).svg", "p2_lodge.jpg"),
    "Shriners": ("Shriners_logo.svg", "shriners.jpg"),

    # Media
    "News Corp": ("News_Corp.svg", "news_corp.jpg"),
    "Fox Corporation": ("Fox_Corporation_logo.svg", "fox_corp.jpg"),
    "Comcast Corporation": ("Comcast_Logo.svg", "comcast.jpg"),
    "The Walt Disney Company": ("TWDC_Logo.svg", "disney.jpg"),
    "Warner Bros. Discovery": ("Warner_Bros._Discovery_logo.svg", "wbd.jpg"),
    "Paramount Global": ("Paramount_Global.svg", "paramount.jpg"),

    # Health / Pharma
    "WHO": ("Flag_of_WHO.svg", "who.jpg"),
    "Pfizer": ("Pfizer_(2021).svg", "pfizer.jpg"),
    "Bayer": ("Logo_Bayer.svg", "bayer.jpg"),
    "Syngenta": ("Syngenta_Logo.svg", "syngenta.jpg"),
    "Purdue Pharma": ("Purdue_Pharma_logo.svg", "purdue_pharma.jpg"),

    # Think tanks / NGOs / Foundations
    "World Economic Forum": ("World_Economic_Forum_logo.svg", "wef.jpg"),
    "Heritage Foundation": ("The_Heritage_Foundation_logo.svg", "heritage_foundation.jpg"),
    "Brookings Institution": ("Brookings_logo_small.svg", "brookings.jpg"),
    "RAND Corporation": ("Rand_Corporation_logo.svg", "rand.jpg"),
    "Club of Rome": ("Club_of_Rome_Logo.svg", "club_of_rome.jpg"),
    "Atlantic Council": ("Atlantic_Council_logo.svg", "atlantic_council.jpg"),
    "Ford Foundation": ("Logo_of_the_Ford_Foundation.svg", "ford_foundation.jpg"),
    "Open Society Foundations": ("Open_Society_Foundations_logo.svg", "osf.jpg"),
    "Rockefeller Foundation": ("Rockefeller_Foundation_logo.svg", "rockefeller_foundation.jpg"),
    "Bill & Melinda Gates Foundation": (
        "Bill_&_Melinda_Gates_Foundation_logo.svg",
        "gates_foundation.jpg",
    ),
    "Carnegie Endowment for International Peace": (
        "Carnegie_Endowment_for_International_Peace_Logo.svg",
        "carnegie_endowment.jpg",
    ),

    # Military / Armed groups / Cartels
    "Al-Qaeda": ("Flag_of_al-Qaeda.svg", "al_qaeda.jpg"),
    "Hezbollah": ("Flag_of_Hezbollah.svg", "hezbollah.jpg"),
    "Ansar Allah (Houthis)": (
        "Emblem_of_the_Ansar_Allah.svg",
        "ansar_allah.jpg",
    ),

    # Tech / Surveillance
    "NSO Group": ("NSO_Group_logo.svg", "nso_group.jpg"),
    "General Electric": ("General_Electric_logo.svg", "general_electric.jpg"),
    "Westinghouse": ("Westinghouse_Electric_Company_LLC_logo.svg", "westinghouse.jpg"),

    # Crime / Intelligence fronts
    "Church of Scientology": ("Scientology_Logo.svg", "scientology.jpg"),
    "United Fruit Company": (
        "United_Fruit_Company.svg",
        "united_fruit.jpg",
    ),

    # Other orgs
    "Dominion Voting Systems": ("Dominion_Voting_Systems_logo.svg", "dominion_voting.jpg"),
    "Veolia": ("Veolia_logo.svg", "veolia.jpg"),
    "Glencore": ("Glencore_logo.svg", "glencore.jpg"),
    "ADM": ("Archer-Daniels-Midland_logo.svg", "adm.jpg"),
    "Seagram": ("Seagram_building.jpg", "seagram.jpg"),
    "Tavistock Institute": ("Tavistock_Institute_logo.svg", "tavistock.jpg"),
    "School of the Americas": (
        "WHINSEC_logo.svg",
        "school_of_americas.jpg",
    ),
    "Monroe Institute": ("The_Monroe_Institute_logo.svg", "monroe_institute.jpg"),
    "ES&S": ("Election_Systems_&_Software_logo.svg", "ess.jpg"),
    "Gaia, Inc.": ("Gaia_Inc_logo.svg", "gaia_inc.jpg"),

    # ══════════════════════════════════════════════════════════
    # EVENTS — iconic photographs (public domain / CC)
    # ══════════════════════════════════════════════════════════
    "September 11 Attacks": (
        "National_Park_Service_9-11_Statue_of_Liberty_and_WTC_fire.jpg",
        "september_11.jpg",
    ),
    "JFK Assassination": (
        "JFK_limousine.png",
        "jfk_assassination.jpg",
    ),
    "Younger Dryas Impact Hypothesis": (
        "Younger_Dryas_temperature_graph.svg",
        "younger_dryas.jpg",
    ),
    "Standing Rock Protests": (
        "NoDAPL_protest_at_ND_State_Capitol.jpg",
        "standing_rock.jpg",
    ),
    "Flint Water Crisis": (
        "Flint_water_crisis.jpg",
        "flint_water_crisis.jpg",
    ),
    "Grusch Congressional Hearing": (
        "US_congressional_hearing_on_UAPs_on_26_July_2023_with_Grusch_Graves_and_Fravor.png",
        "grusch_hearing.jpg",
    ),
    "Eisenhower Farewell Address": (
        "Eisenhower_farewell_address.jpg",
        "eisenhower_farewell.jpg",
    ),
    "Cochabamba Water War": (
        "Cochabamba_water_wars.jpg",
        "cochabamba.jpg",
    ),
    "Roswell Incident": (
        "RoswellDailyRecordJuly8,1947.jpg",
        "roswell.jpg",
    ),
    "Met Gala": (
        "Anna_Wintour_Shankbone_Metropolitan_Museum_of_Art_2009.jpg",
        "met_gala.jpg",
    ),
    "Epstein NPA (2007)": (
        "Jeffrey_Epstein_mug_shot.jpg",
        "epstein_npa.jpg",
    ),
    "2008 Financial Crisis": (
        "Lehman_Brothers_Times_Square_by_David_Shankbone.jpg",
        "financial_crisis_2008.jpg",
    ),
    "Gulf of Tonkin Incident": (
        "USS_Maddox_(DD-731).jpg",
        "gulf_of_tonkin.jpg",
    ),
    "Rothschild Surrealist Ball (1972)": (
        "Château_de_Ferrières_(77).jpg",
        "surrealist_ball.jpg",
    ),
    "Indian Farmer Suicides": (
        "Protesting_farmer_India.jpg",
        "indian_farmer_suicides.jpg",
    ),
    "Church Committee": (
        "Church_Committee.jpg",
        "church_committee.jpg",
    ),

    # ══════════════════════════════════════════════════════════
    # PROGRAMS — declassified docs, logos, photos
    # ══════════════════════════════════════════════════════════
    "MKULTRA": (
        "MKULTRA_Subproject_List,_June_1964.jpg",
        "mkultra.jpg",
    ),
    "Operation Paperclip": (
        "Project_Paperclip_Team_at_Fort_Bliss.jpg",
        "operation_paperclip.jpg",
    ),
    "Project Blue Book": (
        "Project_Blue_Book.jpg",
        "project_blue_book.jpg",
    ),
    "F-35 Joint Strike Fighter": (
        "F-35A_flight_(cropped).jpg",
        "f35.jpg",
    ),
    "Tuskegee Syphilis Study": (
        "Tuskegee-syphilis-study_doctor-injecting-subject.jpg",
        "tuskegee.jpg",
    ),
    "Iran-Contra": (
        "Iran-contra-televised-hearings.png",
        "iran_contra.jpg",
    ),
    "PRISM": (
        "PRISM_logo.jpg",
        "prism.jpg",
    ),
    "Operation Mockingbird": (
        "Operation_Mockingbird.jpg",
        "operation_mockingbird.jpg",
    ),
    "Total Information Awareness": (
        "IAO-logo.png",
        "tia.jpg",
    ),
    "Project Stargate": (
        "Stargate_Project.svg",
        "project_stargate.jpg",
    ),
    "Gateway Process": (
        "Analysis_and_Assessment_of_Gateway_Process.pdf",
        "gateway_process.jpg",
    ),
    "Operation Gladio": (
        "Emblem_of_the_stay-behind_paramilitary_organization_Gladio.svg",
        "operation_gladio.jpg",
    ),
    "Unit 731": (
        "Building_on_the_site_of_the_Gruesome_Unit_731.jpg",
        "unit_731.jpg",
    ),
    "ECHELON": (
        "Menwith-hill-radomes.jpg",
        "echelon.jpg",
    ),
    "Golden Triangle Drug Trade": (
        "Golden_Triangle.png",
        "golden_triangle.jpg",
    ),
    "XKeyscore": (
        "XKeyscore_logo.svg",
        "xkeyscore.jpg",
    ),
    "Operation Northwoods": (
        "Northwoods_MoD.jpg",
        "operation_northwoods.jpg",
    ),
    "COINTELPRO": (
        "COINTELPRO-FBI_Coverage_of_MLK_Jr.jpg",
        "cointelpro.jpg",
    ),
    "Patent Secrecy Orders": (
        "Invention_Secrecy_Act_orders.svg",
        "patent_secrecy.jpg",
    ),
}


def get_wiki_url(wiki_filename):
    """Use Wikimedia API to get the actual image URL (thumbnail for SVGs)."""
    title = f"File:{wiki_filename}"
    api_url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&titles={quote(title)}&prop=imageinfo"
        f"&iiprop=url&iiurlwidth={MAX_SIZE}&format=json"
    )
    result = subprocess.run(
        ["curl", "-s", "-A", "IntelConsole/1.0 (OSINT research)", api_url],
        capture_output=True,
        text=True,
    )
    try:
        data = json.loads(result.stdout)
        pages = data["query"]["pages"]
        for pid, page in pages.items():
            if pid == "-1":
                return None  # File doesn't exist
            if "imageinfo" in page:
                info = page["imageinfo"][0]
                return info.get("thumburl") or info.get("url")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"  [API error] {wiki_filename}: {e}")
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
        [
            "curl", "-s", "-o", tmpfile, "-w", "%{http_code}",
            "-A", ua, "-L", "--max-time", "30", url,
        ],
        capture_output=True,
        text=True,
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
                try:
                    meta = json.loads(meta)
                except (json.JSONDecodeError, TypeError):
                    meta = {}
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

    # Separate existing from new
    todo = {}
    already = {}
    for name, (wiki_file, out_file) in CURATED.items():
        if (PHOTOS_DIR / out_file).exists():
            already[name] = out_file
        else:
            todo[name] = (wiki_file, out_file)

    print(f"{'=' * 60}")
    print(f"Non-Person Entity Photo Download")
    print(f"{'=' * 60}")
    print(f"  Curated entries: {len(CURATED)}")
    print(f"  Already on disk: {len(already)}")
    print(f"  Need to download: {len(todo)}")
    print()

    if not todo and not already:
        print("Nothing to do.")
        return

    # Phase 1: Resolve Wikimedia URLs
    print(f"--- Phase 1: Resolving {len(todo)} Wikimedia URLs ---")
    urls = {}
    not_found = []
    for i, (name, (wiki_file, out_file)) in enumerate(todo.items()):
        url = get_wiki_url(wiki_file)
        if url:
            urls[name] = (url, out_file)
            print(f"  [{i+1}/{len(todo)}] {name}: OK")
        else:
            not_found.append(name)
            print(f"  [{i+1}/{len(todo)}] {name}: NOT FOUND ({wiki_file})")
        time.sleep(API_DELAY)

    # Phase 2: Download
    print(f"\n--- Phase 2: Downloading {len(urls)} images ---")
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

    # Include pre-existing files
    for name, out_file in already.items():
        downloaded.append((name, out_file))

    # Phase 3: Update JSON
    if downloaded:
        ue, un = update_json(downloaded)
        print(f"\n  Updated {ue} entities, {un} graph nodes")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"  RESULTS")
    print(f"{'=' * 60}")
    print(f"  Downloaded:     {len(downloaded) - len(already)}")
    print(f"  Already existed: {len(already)}")
    print(f"  Not on Commons: {len(not_found)}")
    print(f"  Download failed: {len(failed)}")
    print(f"  Total with photos: {len(downloaded)}")

    if not_found:
        print(f"\n  Not found on Wikimedia:")
        for name in not_found:
            print(f"    - {name}")
    if failed:
        print(f"\n  Download failures:")
        for name in failed:
            print(f"    - {name}")

    # Final photo count
    with open(STATIC_DATA / "entities.json") as f:
        entities = json.load(f)
    with_photo = sum(
        1
        for e in entities.values()
        if (
            e.get("metadata", {})
            if isinstance(e.get("metadata", {}), dict)
            else json.loads(e.get("metadata", "{}"))
        ).get("photo_url")
    )
    print(f"\n  Total entities with photos: {with_photo}/{len(entities)}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
