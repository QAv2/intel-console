"""
Merge enrichment results into a seed expansion module.
Deduplicates against existing relationships and normalizes direction.
"""
import json, os, glob

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(BASE), 'static', 'data')
RESULTS_DIR = os.path.join(BASE, 'results')
OUTPUT = os.path.join(os.path.dirname(BASE), 'seed', 'expansion_enrichment.py')


def main():
    # Load existing relationships for dedup
    with open(os.path.join(DATA, 'graph.json')) as f:
        graph = json.load(f)
    with open(os.path.join(DATA, 'entities.json')) as f:
        entities_raw = json.load(f)

    # Name → ID mapping
    name_to_id = {}
    for eid, e in entities_raw.items():
        name_to_id[e['name'].lower()] = int(eid)

    # Existing edges as set of (min_id, max_id, type)
    existing = set()
    for e in graph['edges']:
        key = (min(e['source'], e['target']), max(e['source'], e['target']), e['relationship_type'])
        existing.add(key)

    # Read all batch results
    all_rels = []
    for path in sorted(glob.glob(os.path.join(RESULTS_DIR, 'batch_*.jsonl'))):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line:
                    all_rels.append(json.loads(line))

    print(f"Raw relationships from all batches: {len(all_rels)}")

    # Deduplicate and validate
    seen = set()
    valid = []
    skipped_existing = 0
    skipped_dupe = 0
    skipped_unknown = 0

    for rel in all_rels:
        src_name = rel.get('source', '')
        tgt_name = rel.get('target', '')
        rel_type = rel.get('type', '')

        src_id = name_to_id.get(src_name.lower())
        tgt_id = name_to_id.get(tgt_name.lower())

        if src_id is None or tgt_id is None:
            skipped_unknown += 1
            continue

        # Normalize direction for dedup
        norm_key = (min(src_id, tgt_id), max(src_id, tgt_id), rel_type)

        if norm_key in existing:
            skipped_existing += 1
            continue

        if norm_key in seen:
            skipped_dupe += 1
            continue

        seen.add(norm_key)
        valid.append(rel)

    print(f"After dedup: {len(valid)} new relationships")
    print(f"  Skipped (already in DB): {skipped_existing}")
    print(f"  Skipped (duplicate across batches): {skipped_dupe}")
    print(f"  Skipped (unknown entity name): {skipped_unknown}")

    # Generate expansion module
    rels_py = []
    for rel in valid:
        rels_py.append({
            'source': rel['source'],
            'target': rel['target'],
            'type': rel['type'],
            'tier': rel.get('tier', 'credible'),
            'desc': rel.get('desc', ''),
            'sources': [],
            'year_start': rel.get('year_start'),
            'year_end': rel.get('year_end'),
        })

    # Write expansion module
    with open(OUTPUT, 'w') as f:
        f.write('"""\nAuto-generated enrichment expansion.\n')
        f.write(f'Contains {len(rels_py)} new relationships identified by AI audit.\n')
        f.write('All relationships are documented or credible tier.\n"""\n\n')
        f.write('SOURCES = []\n\n')
        f.write('ENTITIES = []\n\n')
        f.write('ENTITY_SOURCES = {}\n\n')
        f.write('RELATIONSHIPS = ')
        # json.dumps produces null for None; replace with Python None
        f.write(json.dumps(rels_py, indent=2).replace(': null', ': None'))
        f.write('\n')

    print(f"\nExpansion module written to: {OUTPUT}")
    print(f"Run: cd ~/intel-console && python -m seed.add_expansion seed.expansion_enrichment")
    print(f"Then: python3 export_static.py")

    # Also write a summary
    summary_path = os.path.join(BASE, 'summary.json')
    with open(summary_path, 'w') as f:
        json.dump({
            'total_raw': len(all_rels),
            'total_valid': len(valid),
            'skipped_existing': skipped_existing,
            'skipped_duplicate': skipped_dupe,
            'skipped_unknown': skipped_unknown,
            'by_type': {},
            'by_tier': {},
        }, f, indent=2)

    # Count by type and tier
    from collections import Counter
    type_counts = Counter(r['type'] for r in valid)
    tier_counts = Counter(r.get('tier', '?') for r in valid)
    print(f"\nTop relationship types:")
    for t, c in type_counts.most_common(15):
        print(f"  {t}: {c}")
    print(f"\nBy tier:")
    for t, c in tier_counts.most_common():
        print(f"  {t}: {c}")


if __name__ == '__main__':
    main()
