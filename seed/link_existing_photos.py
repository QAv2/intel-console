"""Link existing photos on disk to entities that are missing photo_url.

Phase 1: Match photos already in static/photos/ to entities by name.
Updates both entities.json and graph.json.

Usage:
    python3 -m seed.link_existing_photos [--dry-run]
"""

import json
import os
import re
import sys
from pathlib import Path

PHOTOS_DIR = Path(__file__).parent.parent / "static" / "photos"
STATIC_DATA = Path(__file__).parent.parent / "static" / "data"


def name_to_slugs(name):
    """Generate possible filename slugs from an entity name."""
    slugs = []
    # Basic: lowercase, strip non-alpha, underscores
    base = name.lower()
    base = re.sub(r'[^a-z0-9\s]', '', base)
    base = re.sub(r'\s+', '_', base.strip())
    slugs.append(base)

    # Without common prefixes/suffixes
    for prefix in ['admiral_', 'prince_', 'cardinal_', 'dr_', 'sir_']:
        if base.startswith(prefix):
            slugs.append(base[len(prefix):])

    # Without Jr/Sr/III suffixes
    for suffix in ['_jr', '_sr', '_iii', '_ii']:
        if base.endswith(suffix):
            slugs.append(base[:-len(suffix)])

    # Handle "Edgar Bronfman Sr." -> "edgar_bronfman"
    base_no_suffix = re.sub(r'_(?:jr|sr|iii|ii|iv)$', '', base)
    if base_no_suffix != base:
        slugs.append(base_no_suffix)

    return slugs


# Manual overrides for tricky name->file mappings
MANUAL_MAP = {
    "Admiral Thomas Moorer": "thomas_moorer.jpg",
    "Dwight D. Eisenhower": "dwight_eisenhower.jpg",
    "E. Howard Hunt": "e_howard_hunt.jpg",
    "Edgar Bronfman Sr.": "edgar_bronfman.jpg",
    "Eva Andersson-Dubin": "eva_andersson_dubin.jpg",
    "George H.W. Bush": "george_hw_bush.jpg",
    "George W. Bush": "george_w_bush.jpg",
    "Henry Kissinger": "henry_kissinger.jpg",
    "J.P. Morgan": "jp_morgan.jpg",
    "Jean-Luc Brunel": "jean_luc_brunel.jpg",
    "John-John Veasey": "john_veasey.jpg",
    "Joseph Coors Sr": "joseph_coors_sr.jpg",
    "Lynn Forester de Rothschild": "lynn_rothschild.jpg",
    "Martin Luther King Jr.": "martin_luther_king.jpg",
    "Prince Andrew": "prince_andrew.jpg",
    "Prince Bandar bin Sultan": "bandar_bin_sultan.jpg",
    "Prince Mohammed bin Fahd": "mohammed_bin_fahd.jpg",
    "Prince Turki al-Faisal": "turki_al_faisal.jpg",
    "Santos Trafficante": "santos_trafficante.jpg",
    "Steven Bechtel Sr": "steven_bechtel_sr.jpg",
    "Al-Waleed bin Talal": "alwaleed_bin_talal.jpg",
    "Ari Ben-Menashe": "ari_ben_menashe.jpg",
    "Andres Pastrana": "andres-pastrana.jpg",
    "Augusto Pinochet": "augusto-pinochet.jpg",
    "Børge Brende": "borge_brende.jpg",
    "Eileen Ford": "eileen-ford.jpg",
    "Felix Rodriguez": "felix-rodriguez.jpg",
    "Gary Webb": "gary-webb.jpg",
    "Jack Lang": "jack-lang.jpg",
    "Jacobo Árbenz": "jacobo_arbenz.jpg",
    "Jacques Vallée": "jacques_vallee.jpg",
    "Khalid al-Mihdhar": "khalid_al_mihdhar.jpg",
    "Manuel Noriega": "manuel-noriega.jpg",
    "Nawaf al-Hazmi": "nawaf_al_hazmi.jpg",
    "Mohammed bin Salman": "mohammed_bin_salman.jpg",
    "Nadia Marcinkova": "nadia_marcinkova.jpg",
    "Nicole Junkermann": "nicole_junkermann.jpg",
    "Oliver North": "oliver-north.jpg",
    "Robert LiButti": "robert_libutti.jpg",
    "Agha Hasan Abedi": "agha_hasan_abedi.jpg",
}

# Entities that should NOT match (false positives from substring matching)
SKIP_ENTITIES = {
    "CIA", "DIA", "Mossad", "NSA", "FBI", "MI5", "MI6",
    "Prince Andrew Civil Settlement (2022)",
    "Gérald Marie",  # no photo on disk yet
}


def main():
    dry_run = "--dry-run" in sys.argv

    # Load data
    with open(STATIC_DATA / "entities.json") as f:
        entities = json.load(f)
    with open(STATIC_DATA / "graph.json") as f:
        graph = json.load(f)

    # Get photos on disk
    on_disk = set(f for f in os.listdir(PHOTOS_DIR)
                  if f.endswith(('.jpg', '.jpeg', '.png')))

    # Get currently linked photos
    already_linked = set()
    for e in entities.values():
        meta = e.get('metadata', {})
        if isinstance(meta, str):
            meta = json.loads(meta)
        url = meta.get('photo_url', '')
        if url:
            already_linked.add(e['name'])

    # Build entity name -> id lookup (only those without photos)
    needs_photo = {}
    for eid, e in entities.items():
        if e['name'] not in already_linked and e['name'] not in SKIP_ENTITIES:
            needs_photo[e['name']] = eid

    print(f"Photos on disk: {len(on_disk)}")
    print(f"Already linked: {len(already_linked)}")
    print(f"Entities needing photos: {len(needs_photo)}")

    # Match entities to photos
    matches = {}

    # Phase 1: Manual overrides
    for name, filename in MANUAL_MAP.items():
        if name in needs_photo and filename in on_disk:
            matches[name] = filename

    # Phase 2: Auto-match by slug
    matched_files = set(matches.values())
    for name in needs_photo:
        if name in matches:
            continue
        if name in SKIP_ENTITIES:
            continue

        slugs = name_to_slugs(name)
        for slug in slugs:
            fname = f"{slug}.jpg"
            if fname in on_disk and fname not in matched_files:
                matches[name] = fname
                matched_files.add(fname)
                break

    print(f"\nMatched: {len(matches)} entities to existing photos")

    if dry_run:
        print("\n[DRY RUN] Would link:")
        for name in sorted(matches):
            print(f"  {name} -> {matches[name]}")
        return

    # Update entities.json
    updated_e = 0
    for eid, e in entities.items():
        if e['name'] in matches:
            meta = e.get('metadata', {})
            if isinstance(meta, str):
                meta = json.loads(meta)
            meta['photo_url'] = f"photos/{matches[e['name']]}"
            e['metadata'] = meta
            updated_e += 1

    # Update graph.json
    updated_n = 0
    for node in graph['nodes']:
        if node['name'] in matches:
            node['photo_url'] = f"photos/{matches[node['name']]}"
            updated_n += 1

    # Write back
    with open(STATIC_DATA / "entities.json", "w") as f:
        json.dump(entities, f, indent=2)
    with open(STATIC_DATA / "graph.json", "w") as f:
        json.dump(graph, f, indent=2)

    print(f"\nUpdated {updated_e} entities, {updated_n} graph nodes")

    # Report what's still missing (people only)
    still_missing = []
    for name, eid in needs_photo.items():
        if name not in matches:
            e = entities[eid]
            if e['entity_type'] == 'person':
                still_missing.append(name)

    still_missing.sort()
    print(f"\nPeople still without photos: {len(still_missing)}")
    for name in still_missing:
        print(f"  {name}")


if __name__ == "__main__":
    main()
