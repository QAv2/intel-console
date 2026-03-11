"""Download photos for entities missing portraits.

Phase 1: Wikimedia Commons (verified free-license portraits)
Phase 2: Direct URLs from official/public sites

Usage:
    python3 -m seed.download_photos_expansion
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
API_DELAY = 1

# ── Phase 1: Verified Wikimedia Commons filenames ──
WIKIMEDIA = {
    # Ring 1
    "Guy de Rothschild": ("Guy_de_Rothschild_1964.jpg", "guy_de_rothschild.jpg"),

    # Ring 2
    "Shirō Ishii": ("Shiro-ishii.jpg", "shiro_ishii.jpg"),
    "Sean Combs": ("Sean_Combs_in_2023.png", "sean_combs.jpg"),
    "Salvador Dalí": ("Salvador_Dali_NYWTS.jpg", "salvador_dali.jpg"),
    "Gianni Agnelli": ("Gianni_Agnelli_portrait.jpg", "gianni_agnelli.jpg"),
    "Marisa Berenson": ("BERENSON_Marisa-24x30-2008_(cropped).jpg", "marisa_berenson.jpg"),

    # Ring 3
    "Leonardo DiCaprio": ("Leonardo_DiCaprio_crop.jpg", "leonardo_dicaprio.jpg"),
    "Oprah Winfrey": ("Oprah_Winfrey_2016.jpg", "oprah_winfrey.jpg"),
    "Russell Simmons": ("Russell_Simmons_2012_Shankbone.JPG", "russell_simmons.jpg"),
    "R. Kelly": ("R._Kelly_mug_shot.jpg", "r_kelly.jpg"),
    "Truman Capote": ("Truman_Capote_by_Jack_Mitchell.jpg", "truman_capote.jpg"),
    "Diana Vreeland": ("Diana_Vreeland_1978_©Lynn_Gilbert_(cropped).jpg", "diana_vreeland.jpg"),
    "Anna Wintour": ("Anna_Wintour_in_2024_(cropped).jpg", "anna_wintour.jpg"),
    "Audrey Hepburn": ("Audrey_Hepburn_1956_(2).jpg", "audrey_hepburn.jpg"),
    "Georges Pompidou": ("Georges_Pompidou_1969_(cropped).jpg", "georges_pompidou.jpg"),
    "François Mitterrand": ("President_François_Mitterrand_in_1983.jpg", "francois_mitterrand.jpg"),
    "Stanley Kubrick": ("Stanley_Kubrick_2.jpg", "stanley_kubrick.jpg"),
    "Mayer Amschel Rothschild": ("Mayer_Amschel_Rothschild.jpg", "mayer_amschel_rothschild.jpg"),
    "João Teixeira de Faria": ("João_de_Deus_-_John_of_God_-_Joao_Teixeira_de_Faria_2006.jpg", "joao_teixeira_de_faria.jpg"),
    "Elsa Maxwell": ("Elsa_Maxwell,_on_the_Conte_de_Savoia,_1935.jpg", "elsa_maxwell.jpg"),
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

    all_downloaded = []

    # ── Phase 1: Wikimedia Commons ──
    print("=" * 60)
    print("Phase 1: Wikimedia Commons")
    print("=" * 60)

    wiki_todo = {}
    wiki_already = {}
    for name, (wiki_file, out_file) in WIKIMEDIA.items():
        if (PHOTOS_DIR / out_file).exists():
            wiki_already[name] = out_file
        else:
            wiki_todo[name] = (wiki_file, out_file)

    print(f"  Total: {len(WIKIMEDIA)}, Already: {len(wiki_already)}, Need: {len(wiki_todo)}")

    # Resolve URLs
    urls = {}
    not_found = []
    for name, (wiki_file, out_file) in wiki_todo.items():
        url = get_wiki_url(wiki_file)
        if url:
            urls[name] = (url, out_file)
            print(f"  {name}: resolved")
        else:
            not_found.append(name)
            print(f"  {name}: [!] not found")
        time.sleep(API_DELAY)

    # Download
    wiki_failed = []
    for i, (name, (url, out_file)) in enumerate(urls.items()):
        ok = download_and_resize(url, out_file)
        if ok:
            all_downloaded.append((name, out_file))
        else:
            wiki_failed.append(name)
        if i < len(urls) - 1:
            time.sleep(DOWNLOAD_DELAY)

    for name, out_file in wiki_already.items():
        all_downloaded.append((name, out_file))

    print(f"\n  Downloaded: {len(urls) - len(wiki_failed)}")
    print(f"  Already existed: {len(wiki_already)}")
    print(f"  Failed: {len(wiki_failed)}")
    if wiki_failed:
        print(f"  Failed: {', '.join(wiki_failed)}")

    # ── Phase 2: Direct URL downloads ──
    print(f"\n{'=' * 60}")
    print("Phase 2: Direct URL downloads")
    print("=" * 60)

    DIRECT = {
        # Ring 1
        "Ingo Swann": (
            "https://upload.wikimedia.org/wikipedia/en/3/38/Ingo_Swann.jpg",
            "ingo_swann.jpg",
        ),
        "Robert Mercer": (
            "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Bob_Mercer.jpg/440px-Bob_Mercer.jpg",
            "robert_mercer.jpg",
        ),
        "Thomas Townsend Brown": (
            "https://upload.wikimedia.org/wikipedia/en/e/ef/Thomas_Townsend_Brown.jpg",
            "thomas_townsend_brown.jpg",
        ),

        # Ring 2
        "Joseph McMoneagle": (
            "https://upload.wikimedia.org/wikipedia/commons/f/f3/JoeMcMoneagle.jpg",
            "joseph_mcmoneagle.jpg",
        ),
        "Dean Radin": (
            "https://upload.wikimedia.org/wikipedia/commons/3/30/Dean_Radin%2C_researcher.jpg",
            "dean_radin.jpg",
        ),
        "John Anthony West": (
            "https://upload.wikimedia.org/wikipedia/en/c/cd/JohnAnthonyWest.jpg",
            "john_anthony_west.jpg",
        ),
        "John Casablancas": (
            "https://upload.wikimedia.org/wikipedia/en/4/41/John_Casablancas.jpg",
            "john_casablancas.jpg",
        ),
        "Alexis de Redé": (
            "https://upload.wikimedia.org/wikipedia/en/b/b3/Baron_Alexis_de_Red%C3%A9.jpg",
            "alexis_de_rede.jpg",
        ),

        # Ring 3
        "Robert Monroe": (
            "https://upload.wikimedia.org/wikipedia/en/2/2e/Bob_Monroe.jpg",
            "robert_monroe.jpg",
        ),
        "Zecharia Sitchin": (
            "https://upload.wikimedia.org/wikipedia/en/0/06/Zecharia_sitchin.jpg",
            "zecharia_sitchin.jpg",
        ),
        "Harlan Crow": (
            "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Harlan_Crow_%28cropped%29.jpg/440px-Harlan_Crow_%28cropped%29.jpg",
            "harlan_crow.jpg",
        ),
        "George de Mohrenschildt": (
            "https://upload.wikimedia.org/wikipedia/en/f/f9/George_de_Mohrenschildt.jpg",
            "george_de_mohrenschildt.jpg",
        ),
        "Truman Capote": (  # backup if wiki phase fails
            "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Capote3.jpg/440px-Capote3.jpg",
            "truman_capote.jpg",
        ),
        "Ralph Baric": (
            "https://upload.wikimedia.org/wikipedia/commons/c/ce/Ralph_S._Baric.jpg",
            "ralph_baric.jpg",
        ),
        "Colm Kelleher": (
            "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Colm_Kelleher_2023.jpg/440px-Colm_Kelleher_2023.jpg",
            "colm_kelleher.jpg",
        ),
        "Eleanor Lambert": (
            "https://upload.wikimedia.org/wikipedia/en/7/75/Eleanor_Lambert.jpg",
            "eleanor_lambert.jpg",
        ),
    }

    direct_downloaded = []
    direct_failed = []

    for name, (url, out_file) in DIRECT.items():
        if (PHOTOS_DIR / out_file).exists():
            print(f"  [skip] {out_file} already exists")
            all_downloaded.append((name, out_file))
            continue
        ok = download_and_resize(url, out_file)
        if ok:
            all_downloaded.append((name, out_file))
            direct_downloaded.append(name)
        else:
            direct_failed.append(name)
        time.sleep(DOWNLOAD_DELAY)

    print(f"\n  Downloaded: {len(direct_downloaded)}")
    print(f"  Failed: {len(direct_failed)}")
    if direct_failed:
        print(f"  Failed: {', '.join(direct_failed)}")

    # ── Update JSON ──
    if all_downloaded:
        ue, un = update_json(all_downloaded)
        print(f"\n  Updated {ue} entities, {un} graph nodes")

    # Final count
    with open(STATIC_DATA / "graph.json") as f:
        graph = json.load(f)
    with_photo = sum(1 for n in graph["nodes"] if n.get("photo_url"))
    print(f"\n{'=' * 60}")
    print(f"  Total entities with photos: {with_photo}/{len(graph['nodes'])}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
