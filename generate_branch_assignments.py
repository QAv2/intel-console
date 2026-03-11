#!/usr/bin/env python3
"""
Generate branch assignments for all 825 entities in the Intel Console.

Reads entities.json + graph.json + expansion scripts to:
1. Map expansion scripts → 11 thematic branches
2. Remap base entities (1-107) from old 7-branch system to new 11
3. Auto-assign rings by degree centrality within each branch
4. Output branch_assignments.json + audit CSV

Usage:
    python3 generate_branch_assignments.py
"""

import json
import os
import re
import csv

# ============================================================
# 11 NEW BRANCHES
# ============================================================

BRANCHES = {
    'power':         'Power Architecture',
    'intelligence':  'Intelligence & Covert',
    'financial':     'Financial Control',
    'hidden_history':'Hidden History',
    'consciousness': 'Consciousness & Anomalous',
    'exploitation':  'Exploitation Networks',
    'narrative':     'Narrative Control',
    'health':        'Health & Bio',
    'resource':      'Resource Control',
    'cosmology':     'Cosmology & Origins',
    'elite_social':  'Elite Social Architecture',
}

# ============================================================
# EXPANSION SCRIPT → BRANCH MAPPING
# ============================================================

EXPANSION_TO_BRANCH = {
    'expansion_political':            'power',
    'expansion_bohemian_grove':       'power',
    'expansion_dynasties':            'power',
    'expansion_supranational':        'power',
    'expansion_wef':                  'power',
    'expansion_china':                'power',

    'expansion_911':                  'intelligence',
    'expansion_false_flags':          'intelligence',
    'expansion_tech_surveillance':    'intelligence',
    'expansion_israel':               'intelligence',
    'expansion_latin_america':        'intelligence',
    'expansion_iran_conflict':        'intelligence',

    'expansion_financial':            'financial',
    'expansion_financial_deep':       'financial',
    'expansion_germany':              'financial',

    'expansion_jfk':                  'hidden_history',
    'expansion_freemasonry':          'hidden_history',
    'expansion_ritual_occult':        'hidden_history',

    'expansion_consciousness':        'consciousness',
    'expansion_consciousness_deep':   'consciousness',
    'expansion_uap_disclosure':       'consciousness',
    'expansion_uap_programs':         'consciousness',

    'expansion_inner_circle':         'exploitation',
    'expansion_hollywood':            'exploitation',
    'expansion_hollywood_predators':  'exploitation',
    'expansion_pedophile_networks':   'exploitation',
    'expansion_france':               'exploitation',

    'expansion_media':                'narrative',
    'expansion_election_interference':'narrative',
    'expansion_new_age_psyops':       'narrative',

    'expansion_health':               'health',
    'expansion_bioweapons':           'health',
    'expansion_food_supply':          'health',

    'expansion_water':                'resource',
    'expansion_energy_suppression':   'resource',
    'expansion_drug_trafficking':     'resource',
    'expansion_mic':                  'resource',

    'expansion_cosmology_origins':    'cosmology',
    'expansion_cosmology_deep':       'cosmology',

    'expansion_surrealist_ball':      'elite_social',
    'expansion_russia':               'elite_social',
    'expansion_saudi':                'elite_social',
    'expansion_uk':                   'elite_social',
}

# ============================================================
# BASE ENTITY (1-107 + 823-825) → BRANCH MAPPING
# Old 7-branch → new 11-branch conversion
# ============================================================

OLD_TO_NEW = {
    'political':       'power',
    'financial':       'financial',
    'hollywood':       'elite_social',
    'inner_circle':    'exploitation',
    'organized_crime': 'hidden_history',
    'intelligence':    'intelligence',
    'legal':           'power',
}

# Individual overrides for base entities that don't fit the default conversion
BASE_OVERRIDES = {
    # Epstein network core → exploitation
    1:   'exploitation',   # Jeffrey Epstein
    38:  'exploitation',   # Alan Dershowitz (legal enabler of exploitation)
    13:  'exploitation',   # Craig Spence (sex trafficking)
    37:  'power',          # Alexander Acosta (political, NPA)
    100: 'exploitation',   # Epstein NPA
    101: 'exploitation',   # Epstein Arrest
    102: 'exploitation',   # Epstein Death
    105: 'exploitation',   # Wexner Deposition

    # Narrative control
    61:  'narrative',      # Hill & Knowlton

    # Resource control
    71:  'resource',       # Glencore

    # Elite social
    72:  'elite_social',   # George Town Club
    75:  'elite_social',   # Mar-a-Lago

    # Financial
    54:  'financial',      # BCCI
    55:  'financial',      # First American Bank
    70:  'financial',      # CAPCOM
    73:  'financial',      # Bayrock Group
    99:  'financial',      # BCCI Shutdown

    # Hidden history
    74:  'hidden_history', # Resorts International

    # Direct inserts (823-825)
    823: 'elite_social',   # Stanley Kubrick
    824: 'elite_social',   # Eyes Wide Shut
    825: 'elite_social',   # Mentmore Towers
}

# ============================================================
# EXPANSION ENTITY OVERRIDES
# Entities from expansion scripts that belong in a different branch
# than their expansion's default
# ============================================================

ENTITY_OVERRIDES = {
    # 9/11 expansion — some entities belong in power, not intelligence
    # (entity IDs from expansion_911)

    # UK expansion — split between branches
    # MI5/MI6 → intelligence, Savile → exploitation, Mandelson → power
    762: 'intelligence',   # MI5
    763: 'intelligence',   # MI6
    764: 'exploitation',   # Jimmy Savile
    761: 'power',          # Peter Mandelson
    766: 'power',          # Metropolitan Police
    769: 'power',          # Crown Prosecution Service
    770: 'narrative',      # Mark Thompson (BBC)
    772: 'narrative',      # Evgeny Lebedev (media)
    774: 'narrative',      # Newsnight Interview
    773: 'exploitation',   # TerraMar Project
    771: 'exploitation',   # Stuart Roffey
    767: 'narrative',      # Pergamon Press
    768: 'narrative',      # Mirror Group Newspapers

    # Saudi expansion — split
    657: 'intelligence',   # Saudi GID
    656: 'intelligence',   # Prince Turki al-Faisal
    659: 'narrative',      # Jamal Khashoggi (journalist)
    664: 'intelligence',   # BAE Al-Yamamah Deal
    665: 'intelligence',   # Safari Club
    666: 'intelligence',   # Wafic Said
    663: 'financial',      # Carlyle Group
    661: 'financial',      # Kingdom Holding
    662: 'financial',      # Saudi Binladin Group

    # Russia expansion — split
    651: 'intelligence',   # FSB
    650: 'power',          # Vladimir Putin
    652: 'hidden_history', # Semion Mogilevich (organized crime)
    653: 'hidden_history', # Solntsevskaya Bratva
    654: 'financial',      # Dmitry Rybolovlev

    # Latin America expansion — some are resource (drug trade)
    564: 'resource',       # Medellín Cartel
    565: 'intelligence',   # SETCO Aviation
    566: 'intelligence',   # School of the Americas
    562: 'narrative',      # Gary Webb (journalist)

    # Germany expansion — Philippa Sigl-Glöckner is power/political
    466: 'power',          # Philippa Sigl-Glöckner

    # Bohemian Grove expansion — some financial figures
    # Already in power by default, which is correct for most

    # Supranational — some are financial
    679: 'financial',      # Open Society Foundations
    680: 'financial',      # Rockefeller Foundation
    681: 'financial',      # Carnegie Endowment
    682: 'financial',      # Ford Foundation

    # MIC expansion — some intelligence
    604: 'intelligence',   # Blackwater
    605: 'exploitation',   # DynCorp (trafficking ties)
    606: 'intelligence',   # Erik Prince

    # Media expansion — some intelligence
    575: 'intelligence',   # Julian Assange
    576: 'intelligence',   # Edward Snowden
    577: 'intelligence',   # Chelsea Manning
    578: 'intelligence',   # William Binney
    585: 'intelligence',   # WikiLeaks
    588: 'intelligence',   # Operation Mockingbird
    589: 'intelligence',   # PRISM

    # Health expansion — some intelligence
    475: 'intelligence',   # Sidney Gottlieb (MKULTRA)
    476: 'intelligence',   # Donald Ewen Cameron (MKULTRA)
    488: 'intelligence',   # Tuskegee Syphilis Study
    489: 'intelligence',   # Guatemala Syphilis Experiments

    # False flags expansion — some hidden_history
    382: 'hidden_history', # Operation Paperclip
    392: 'hidden_history', # Wernher von Braun
    388: 'power',          # NATO
    389: 'power',          # Joint Chiefs of Staff
    391: 'financial',      # United Fruit Company

    # Drug trafficking — some intelligence
    308: 'intelligence',   # Air America
    309: 'intelligence',   # Nugan Hand Bank
    312: 'power',          # DEA
    320: 'power',          # ATF

    # Election interference — some intelligence
    347: 'intelligence',   # Internet Research Agency

    # Consciousness deep — some intelligence
    # SRI International etc. are correctly in consciousness

    # Food supply — Monsanto to resource/health (default health is fine)
    487: 'health',         # Monsanto

    # Energy suppression — Tesla etc. correctly in resource

    # Dynasties — some financial
    331: 'financial',      # Federal Reserve System
    329: 'financial',      # Standard Oil
    330: 'financial',      # Brown Brothers Harriman
    332: 'hidden_history', # Skull and Bones
    333: 'financial',      # DuPont Family
}


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, 'static', 'data')
    seed_dir = os.path.join(base_dir, 'seed')

    # Load data
    with open(os.path.join(data_dir, 'entities.json')) as f:
        entities = json.load(f)

    with open(os.path.join(data_dir, 'graph.json')) as f:
        graph = json.load(f)

    # Build name → ID map
    name_to_id = {v['name']: int(k) for k, v in entities.items()}

    # Count degree per entity
    degree = {}
    for e in graph['edges']:
        degree[e['source']] = degree.get(e['source'], 0) + 1
        degree[e['target']] = degree.get(e['target'], 0) + 1

    # Parse expansion scripts → entity IDs
    expansion_entities = {}
    for fname in sorted(os.listdir(seed_dir)):
        if not fname.startswith('expansion_') or not fname.endswith('.py'):
            continue
        key = fname.replace('.py', '')
        with open(os.path.join(seed_dir, fname)) as f:
            content = f.read()
        ent_names = re.findall(r'"name":\s*"([^"]+)"', content)
        ids = [name_to_id[n] for n in ent_names if n in name_to_id]
        expansion_entities[key] = ids

    all_expansion_ids = set()
    for ids in expansion_entities.values():
        all_expansion_ids.update(ids)

    # ---- Step 1: Assign branches ----
    assignments = {}  # entity_id → branch_key

    # Old branches.js mapping (for base entities)
    OLD_BRANCH_MAP = {
        # political
        32: 'political', 33: 'political', 108: 'political', 8: 'political',
        38: 'political', 37: 'political', 5: 'political', 111: 'political',
        113: 'political', 31: 'political', 112: 'political', 109: 'political',
        110: 'political', 114: 'political', 29: 'political', 75: 'political',
        115: 'political', 117: 'political', 118: 'political',
        # financial
        4: 'financial', 30: 'financial', 125: 'financial', 124: 'financial',
        119: 'financial', 120: 'financial', 122: 'financial', 123: 'financial',
        126: 'financial', 129: 'financial', 121: 'financial', 6: 'financial',
        7: 'financial', 127: 'financial', 128: 'financial', 56: 'financial',
        57: 'financial', 58: 'financial', 65: 'financial', 66: 'financial',
        68: 'financial', 69: 'financial', 71: 'financial', 130: 'financial',
        131: 'financial', 132: 'financial', 133: 'financial',
        # hollywood
        134: 'hollywood', 135: 'hollywood', 136: 'hollywood', 137: 'hollywood',
        138: 'hollywood', 139: 'hollywood', 140: 'hollywood', 141: 'hollywood',
        142: 'hollywood', 143: 'hollywood', 116: 'hollywood', 144: 'hollywood',
        # inner_circle
        2: 'inner_circle', 145: 'inner_circle', 146: 'inner_circle',
        148: 'inner_circle', 149: 'inner_circle', 150: 'inner_circle',
        151: 'inner_circle', 147: 'inner_circle', 152: 'inner_circle',
        153: 'inner_circle', 67: 'inner_circle', 154: 'inner_circle',
        76: 'inner_circle', 155: 'inner_circle', 156: 'inner_circle',
        157: 'inner_circle', 102: 'inner_circle', 158: 'inner_circle',
        159: 'inner_circle',
        # organized_crime
        11: 'organized_crime', 18: 'organized_crime', 34: 'organized_crime',
        39: 'organized_crime', 35: 'organized_crime', 45: 'organized_crime',
        41: 'organized_crime', 36: 'organized_crime', 50: 'organized_crime',
        40: 'organized_crime', 42: 'organized_crime', 43: 'organized_crime',
        44: 'organized_crime', 46: 'organized_crime', 47: 'organized_crime',
        48: 'organized_crime', 49: 'organized_crime', 51: 'organized_crime',
        52: 'organized_crime', 73: 'organized_crime', 74: 'organized_crime',
        77: 'organized_crime', 78: 'organized_crime', 79: 'organized_crime',
        80: 'organized_crime', 81: 'organized_crime', 82: 'organized_crime',
        83: 'organized_crime', 84: 'organized_crime', 106: 'organized_crime',
        107: 'organized_crime',
        # intelligence
        3: 'intelligence', 10: 'intelligence', 85: 'intelligence',
        88: 'intelligence', 14: 'intelligence', 15: 'intelligence',
        16: 'intelligence', 17: 'intelligence', 53: 'intelligence',
        87: 'intelligence', 28: 'intelligence', 27: 'intelligence',
        9: 'intelligence', 12: 'intelligence', 13: 'intelligence',
        19: 'intelligence', 20: 'intelligence', 24: 'intelligence',
        25: 'intelligence', 26: 'intelligence', 54: 'intelligence',
        55: 'intelligence', 59: 'intelligence', 60: 'intelligence',
        61: 'intelligence', 63: 'intelligence', 64: 'intelligence',
        70: 'intelligence', 72: 'intelligence', 86: 'intelligence',
        90: 'intelligence', 91: 'intelligence', 92: 'intelligence',
        93: 'intelligence', 94: 'intelligence', 95: 'intelligence',
        96: 'intelligence', 97: 'intelligence', 98: 'intelligence',
        99: 'intelligence', 103: 'intelligence', 104: 'intelligence',
        # legal
        89: 'legal', 62: 'legal', 100: 'legal', 101: 'legal',
        105: 'legal', 21: 'legal', 22: 'legal', 23: 'legal',
    }

    # Base entities: use old branch → new mapping + overrides
    all_ids = sorted([int(k) for k in entities.keys()])

    for eid in all_ids:
        if eid in BASE_OVERRIDES:
            assignments[eid] = BASE_OVERRIDES[eid]
        elif eid in ENTITY_OVERRIDES:
            assignments[eid] = ENTITY_OVERRIDES[eid]
        elif eid in OLD_BRANCH_MAP:
            old_branch = OLD_BRANCH_MAP[eid]
            assignments[eid] = OLD_TO_NEW[old_branch]
        else:
            # Must be from an expansion script
            assigned = False
            for exp_name, exp_ids in expansion_entities.items():
                if eid in exp_ids:
                    assignments[eid] = EXPANSION_TO_BRANCH.get(exp_name, 'hidden_history')
                    assigned = True
                    break
            if not assigned:
                # Fallback — shouldn't happen, but catch it
                print(f'WARNING: Entity {eid} ({entities[str(eid)]["name"]}) has no assignment, defaulting to hidden_history')
                assignments[eid] = 'hidden_history'

    # Apply entity overrides on top (expansion overrides take precedence)
    for eid, branch in ENTITY_OVERRIDES.items():
        if eid in assignments:
            assignments[eid] = branch

    # Apply base overrides on top
    for eid, branch in BASE_OVERRIDES.items():
        if eid in assignments:
            assignments[eid] = branch

    # ---- Step 2: Assign rings by degree centrality within each branch ----
    # Group entities by branch
    branch_groups = {b: [] for b in BRANCHES}
    for eid, branch in assignments.items():
        deg = degree.get(eid, 0)
        branch_groups[branch].append((eid, deg))

    # Sort each branch by degree descending
    result = {}
    for branch, members in branch_groups.items():
        members.sort(key=lambda x: -x[1])
        n = len(members)
        ring1_cutoff = max(1, int(n * 0.15))
        ring2_cutoff = max(ring1_cutoff + 1, int(n * 0.50))

        for i, (eid, deg) in enumerate(members):
            if i < ring1_cutoff:
                ring = 1
            elif i < ring2_cutoff:
                ring = 2
            else:
                ring = 3
            result[eid] = {'branch': branch, 'ring': ring}

    # Force Epstein to exploitation ring 1
    result[1] = {'branch': 'exploitation', 'ring': 1}

    # ---- Step 3: Output ----
    # JSON output
    output_path = os.path.join(data_dir, 'branch_assignments.json')
    with open(output_path, 'w') as f:
        json.dump(result, f, separators=(',', ':'))
    print(f'Wrote {output_path} ({len(result)} entities)')

    # Stats
    for branch in BRANCHES:
        members = [(eid, r) for eid, r in result.items() if r['branch'] == branch]
        rings = {1: 0, 2: 0, 3: 0}
        for _, r in members:
            rings[r['ring']] += 1
        print(f'  {branch:20s}: {len(members):3d} entities  (R1:{rings[1]:2d}  R2:{rings[2]:2d}  R3:{rings[3]:2d})')

    # Audit CSV
    audit_path = os.path.join(base_dir, 'branch_audit.csv')
    with open(audit_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['entity_id', 'name', 'type', 'branch', 'ring', 'degree', 'source'])
        for eid in sorted(result.keys()):
            ent = entities[str(eid)]
            r = result[eid]
            # Determine source of assignment
            if eid in BASE_OVERRIDES:
                src = 'base_override'
            elif eid in ENTITY_OVERRIDES:
                src = 'entity_override'
            elif eid in OLD_BRANCH_MAP:
                src = f'old_branch:{OLD_BRANCH_MAP[eid]}'
            else:
                src = 'expansion'
                for exp_name, exp_ids in expansion_entities.items():
                    if eid in exp_ids:
                        src = f'expansion:{exp_name}'
                        break
            writer.writerow([
                eid, ent['name'], ent.get('entity_type', ''),
                r['branch'], r['ring'], degree.get(eid, 0), src
            ])
    print(f'Wrote {audit_path}')

    # Verify all 825 assigned
    missing = [eid for eid in all_ids if eid not in result]
    if missing:
        print(f'ERROR: {len(missing)} entities missing assignments: {missing[:10]}...')
    else:
        print(f'All {len(result)} entities assigned successfully.')


if __name__ == '__main__':
    main()
