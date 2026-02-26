"""Incremental expansion inserter for Intel Console.

Inserts entities, relationships, and sources from an expansion module
into a live database. Handles deduplication — safe to re-run.

Usage:
    python -m seed.add_expansion seed.expansion_russia
    python -m seed.add_expansion seed.expansion_china
"""

import asyncio
import importlib
import json
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from server.db import get_db, init_db, close_db


async def add_expansion(module_name: str):
    mod = importlib.import_module(module_name)

    SOURCES = getattr(mod, "SOURCES", [])
    ENTITIES = getattr(mod, "ENTITIES", [])
    RELATIONSHIPS = getattr(mod, "RELATIONSHIPS", [])
    ENTITY_SOURCES = getattr(mod, "ENTITY_SOURCES", {})

    await init_db()
    db = await get_db()

    # ---- Sources (dedup by id) ----
    src_added = 0
    for s in SOURCES:
        existing = await db.execute_fetchall(
            "SELECT id FROM sources WHERE id = ?", (s["id"],)
        )
        if existing:
            continue
        await db.execute(
            "INSERT INTO sources (id, title, url, source_type, author, year) VALUES (?, ?, ?, ?, ?, ?)",
            (s["id"], s["title"], s.get("url", ""), s.get("source_type", "journalism"),
             s.get("author", ""), s.get("year")),
        )
        src_added += 1

    # ---- Entities (dedup by name + entity_type) ----
    ent_added = 0
    for e in ENTITIES:
        existing = await db.execute_fetchall(
            "SELECT id FROM entities WHERE name = ? AND entity_type = ?",
            (e["name"], e["entity_type"]),
        )
        if existing:
            print(f"  [skip] Entity already exists: {e['name']}")
            continue
        await db.execute(
            "INSERT INTO entities (name, entity_type, description, aliases, metadata) VALUES (?, ?, ?, ?, ?)",
            (e["name"], e["entity_type"], e.get("description", ""),
             e.get("aliases", ""), json.dumps(e.get("metadata", {}))),
        )
        ent_added += 1

    # Build name→id map for relationship resolution
    rows = await db.execute_fetchall("SELECT id, name FROM entities")
    name_to_id = {row["name"]: row["id"] for row in rows}

    # ---- Relationships (dedup by source+target+type) ----
    rel_added = 0
    rel_skipped = 0
    for r in RELATIONSHIPS:
        src_id = name_to_id.get(r["source"])
        tgt_id = name_to_id.get(r["target"])
        if src_id is None or tgt_id is None:
            missing = r["source"] if src_id is None else r["target"]
            print(f"  [!] Skipping relationship: entity '{missing}' not found")
            rel_skipped += 1
            continue

        # Dedup check
        existing = await db.execute_fetchall(
            "SELECT id FROM relationships WHERE source_id = ? AND target_id = ? AND relationship_type = ?",
            (src_id, tgt_id, r["type"]),
        )
        if existing:
            continue

        cur = await db.execute(
            """INSERT INTO relationships
               (source_id, target_id, relationship_type, evidence_tier, description, year_start, year_end)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (src_id, tgt_id, r["type"], r["tier"], r.get("desc", ""),
             r.get("year_start"), r.get("year_end")),
        )
        rel_id = cur.lastrowid
        for sid in r.get("sources", []):
            await db.execute(
                "INSERT OR IGNORE INTO relationship_sources (relationship_id, source_id) VALUES (?, ?)",
                (rel_id, sid),
            )
        rel_added += 1

    # ---- Entity-source links ----
    es_added = 0
    for entity_name, source_ids in ENTITY_SOURCES.items():
        eid = name_to_id.get(entity_name)
        if eid is None:
            print(f"  [!] entity_sources: entity '{entity_name}' not found")
            continue
        for sid in source_ids:
            await db.execute(
                "INSERT OR IGNORE INTO entity_sources (entity_id, source_id) VALUES (?, ?)",
                (eid, sid),
            )
            es_added += 1

    await db.commit()
    await close_db()

    print(f"\n[+] Expansion complete:")
    print(f"    Sources:       +{src_added} (of {len(SOURCES)})")
    print(f"    Entities:      +{ent_added} (of {len(ENTITIES)})")
    print(f"    Relationships: +{rel_added} (of {len(RELATIONSHIPS)}, {rel_skipped} skipped)")
    print(f"    Entity-source: +{es_added} links")

    # Print new entity IDs for branches.js update
    print(f"\n[*] Entity IDs for branches.js:")
    for e in ENTITIES:
        eid = name_to_id.get(e["name"])
        if eid is None:
            # Re-fetch in case we just inserted it
            rows2 = await get_db() if False else None  # db closed, use sync
        print(f"    {eid}: '{e['name']}'")


async def main():
    if len(sys.argv) < 2:
        print("Usage: python -m seed.add_expansion <module_name>")
        print("Example: python -m seed.add_expansion seed.expansion_russia")
        sys.exit(1)

    module_name = sys.argv[1]
    print(f"[*] Loading expansion module: {module_name}")
    await add_expansion(module_name)


if __name__ == "__main__":
    asyncio.run(main())
