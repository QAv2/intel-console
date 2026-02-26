"""Import curated entities, relationships, and sources into SQLite.

Combines the base curated_entities layer with 4 expansion layers:
  - expansion_political    (Political & Government cluster)
  - expansion_financial    (Financial Elite & Mega Group cluster)
  - expansion_hollywood    (Hollywood, Media & Modeling cluster)
  - expansion_inner_circle (Inner Circle & Enablers)
"""

import asyncio
import json
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from server.db import get_db, init_db, close_db

# ---- Base layer ----
from seed.curated_entities import (
    SOURCES as BASE_SOURCES,
    ENTITIES as BASE_ENTITIES,
    RELATIONSHIPS as BASE_RELATIONSHIPS,
    ENTITY_SOURCES as BASE_ENTITY_SOURCES,
)

# ---- Expansion layers ----
from seed.expansion_political import (
    SOURCES as POL_SOURCES,
    ENTITIES as POL_ENTITIES,
    RELATIONSHIPS as POL_RELATIONSHIPS,
    ENTITY_SOURCES as POL_ENTITY_SOURCES,
)
from seed.expansion_financial import (
    SOURCES as FIN_SOURCES,
    ENTITIES as FIN_ENTITIES,
    RELATIONSHIPS as FIN_RELATIONSHIPS,
    ENTITY_SOURCES as FIN_ENTITY_SOURCES,
)
from seed.expansion_hollywood import (
    SOURCES as HOL_SOURCES,
    ENTITIES as HOL_ENTITIES,
    RELATIONSHIPS as HOL_RELATIONSHIPS,
    ENTITY_SOURCES as HOL_ENTITY_SOURCES,
)
from seed.expansion_inner_circle import (
    SOURCES as IC_SOURCES,
    ENTITIES as IC_ENTITIES,
    RELATIONSHIPS as IC_RELATIONSHIPS,
    ENTITY_SOURCES as IC_ENTITY_SOURCES,
)

# ---- Combine all layers ----
SOURCES = BASE_SOURCES + POL_SOURCES + FIN_SOURCES + HOL_SOURCES + IC_SOURCES
ENTITIES = BASE_ENTITIES + POL_ENTITIES + FIN_ENTITIES + HOL_ENTITIES + IC_ENTITIES
RELATIONSHIPS = BASE_RELATIONSHIPS + POL_RELATIONSHIPS + FIN_RELATIONSHIPS + HOL_RELATIONSHIPS + IC_RELATIONSHIPS

# Merge entity_sources dicts
ENTITY_SOURCES = {}
for es_dict in [BASE_ENTITY_SOURCES, POL_ENTITY_SOURCES, FIN_ENTITY_SOURCES, HOL_ENTITY_SOURCES, IC_ENTITY_SOURCES]:
    for name, sids in es_dict.items():
        if name not in ENTITY_SOURCES:
            ENTITY_SOURCES[name] = []
        for sid in sids:
            if sid not in ENTITY_SOURCES[name]:
                ENTITY_SOURCES[name].append(sid)


async def seed():
    await init_db()
    db = await get_db()

    # Check if already seeded
    count = (await db.execute_fetchall("SELECT COUNT(*) as c FROM entities"))[0]["c"]
    if count > 0:
        print(f"[!] Database already has {count} entities. Skipping seed.")
        await close_db()
        return

    print(f"[*] Seeding {len(SOURCES)} sources...")
    for s in SOURCES:
        await db.execute(
            "INSERT INTO sources (id, title, url, source_type, author, year) VALUES (?, ?, ?, ?, ?, ?)",
            (s["id"], s["title"], s.get("url", ""), s.get("source_type", "journalism"),
             s.get("author", ""), s.get("year")),
        )

    print(f"[*] Seeding {len(ENTITIES)} entities...")
    entity_id_map = {}  # name -> id
    for e in ENTITIES:
        cur = await db.execute(
            "INSERT INTO entities (name, entity_type, description, aliases, metadata) VALUES (?, ?, ?, ?, ?)",
            (e["name"], e["entity_type"], e.get("description", ""),
             e.get("aliases", ""), json.dumps(e.get("metadata", {}))),
        )
        entity_id_map[e["name"]] = cur.lastrowid

    print(f"[*] Seeding {len(RELATIONSHIPS)} relationships...")
    skipped = 0
    for r in RELATIONSHIPS:
        src_id = entity_id_map.get(r["source"])
        tgt_id = entity_id_map.get(r["target"])
        if src_id is None or tgt_id is None:
            print(f"  [!] Skipping: {r['source']} -> {r['target']} (entity not found)")
            skipped += 1
            continue
        cur = await db.execute(
            """INSERT INTO relationships
               (source_id, target_id, relationship_type, evidence_tier, description)
               VALUES (?, ?, ?, ?, ?)""",
            (src_id, tgt_id, r["type"], r["tier"], r.get("desc", "")),
        )
        rel_id = cur.lastrowid
        for sid in r.get("sources", []):
            await db.execute(
                "INSERT OR IGNORE INTO relationship_sources (relationship_id, source_id) VALUES (?, ?)",
                (rel_id, sid),
            )

    # Seed entity_sources junction table
    es_count = 0
    for entity_name, source_ids in ENTITY_SOURCES.items():
        eid = entity_id_map.get(entity_name)
        if eid is None:
            print(f"  [!] entity_sources: entity '{entity_name}' not found")
            continue
        for sid in source_ids:
            await db.execute(
                "INSERT OR IGNORE INTO entity_sources (entity_id, source_id) VALUES (?, ?)",
                (eid, sid),
            )
            es_count += 1

    await db.commit()
    await close_db()

    total_rels = len(RELATIONSHIPS) - skipped
    print(f"[+] Seeded: {len(ENTITIES)} entities, {total_rels} relationships, {len(SOURCES)} sources, {es_count} entity-source links")
    if skipped:
        print(f"[!] Skipped {skipped} relationships due to missing entities")


if __name__ == "__main__":
    asyncio.run(seed())
