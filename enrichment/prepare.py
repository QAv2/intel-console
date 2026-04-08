"""
Prepare batch assignments and shared data for enrichment workers.
Run once before spawning agents.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(BASE), 'static', 'data')

def main():
    # Load entities
    with open(os.path.join(DATA, 'entities.json')) as f:
        entities_raw = json.load(f)
    entities = {int(k): v for k, v in entities_raw.items()}

    # Load graph for existing edges
    with open(os.path.join(DATA, 'graph.json')) as f:
        graph = json.load(f)

    # Build existing connections per entity
    existing = {}  # { entity_id: set of (other_id, rel_type) }
    for e in graph['edges']:
        s, t, rt = e['source'], e['target'], e['relationship_type']
        existing.setdefault(s, set()).add((t, rt))
        existing.setdefault(t, set()).add((s, rt))

    # Serialize existing connections
    existing_ser = {}
    for eid, conns in existing.items():
        existing_ser[eid] = [{'entity_id': c[0], 'type': c[1]} for c in conns]

    # People to audit
    people = []
    for eid, e in sorted(entities.items()):
        if e.get('entity_type') == 'person':
            people.append({
                'id': eid,
                'name': e['name'],
                'description': (e.get('description') or '')[:200],
                'current_connections': existing_ser.get(eid, []),
            })

    # Full entity name list (compact)
    entity_list = []
    for eid, e in sorted(entities.items()):
        entity_list.append({
            'id': eid,
            'name': e['name'],
            'type': e.get('entity_type', 'unknown'),
        })

    # Divide into 5 batches
    n_batches = 5
    batches = [[] for _ in range(n_batches)]
    for i, p in enumerate(people):
        batches[i % n_batches].append(p)

    # Write shared data
    with open(os.path.join(BASE, 'entity_list.json'), 'w') as f:
        json.dump(entity_list, f, separators=(',', ':'))

    with open(os.path.join(BASE, 'existing_connections.json'), 'w') as f:
        json.dump(existing_ser, f, separators=(',', ':'))

    for i, batch in enumerate(batches):
        with open(os.path.join(BASE, f'batch_{i}.json'), 'w') as f:
            json.dump(batch, f, indent=2)

    # Create empty ledger
    open(os.path.join(BASE, 'ledger.jsonl'), 'w').close()

    print(f"Prepared {len(people)} people in {n_batches} batches:")
    for i, batch in enumerate(batches):
        print(f"  Batch {i}: {len(batch)} people")
    print(f"Entity list: {len(entity_list)} entities")
    print(f"Shared data written to {BASE}/")

if __name__ == '__main__':
    main()
