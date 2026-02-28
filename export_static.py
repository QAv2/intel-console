#!/usr/bin/env python3
"""One-shot export: SQLite → static JSON for GitHub Pages deployment."""

import json
import os
import sqlite3

from geo_enrich import export_geo

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "intel.db")
OUT_DIR = os.path.join(os.path.dirname(__file__), "static", "data")

TIER_ORDER = {"documented": 0, "credible": 1, "inference": 2, "speculative": 3}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row

    # ---- Entities ----
    entities_raw = db.execute("SELECT * FROM entities ORDER BY name").fetchall()
    entities_by_id = {}
    for e in entities_raw:
        meta = e["metadata"]
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except (json.JSONDecodeError, TypeError):
                meta = {}
        # Strip /static/ prefix from photo URLs for static deploy
        if isinstance(meta, dict) and meta.get("photo_url", "").startswith("/static/"):
            meta["photo_url"] = meta["photo_url"][len("/static/"):]
        entities_by_id[e["id"]] = {
            "id": e["id"],
            "name": e["name"],
            "entity_type": e["entity_type"],
            "description": e["description"],
            "aliases": e["aliases"],
            "metadata": meta,
        }

    # ---- Relationships with sources ----
    rels_raw = db.execute("SELECT * FROM relationships").fetchall()
    all_rels = []
    rels_by_entity = {}  # entity_id → [rel, ...]
    for r in rels_raw:
        # Get relationship sources
        rel_sources = db.execute(
            """SELECT s.id, s.title, s.url, s.source_type
               FROM sources s
               JOIN relationship_sources rs ON rs.source_id = s.id
               WHERE rs.relationship_id = ?""",
            (r["id"],),
        ).fetchall()

        rel = {
            "id": r["id"],
            "source_id": r["source_id"],
            "target_id": r["target_id"],
            "relationship_type": r["relationship_type"],
            "evidence_tier": r["evidence_tier"],
            "description": r["description"],
            "year_start": r["year_start"],
            "year_end": r["year_end"],
            "sources": [dict(s) for s in rel_sources],
        }
        all_rels.append(rel)

        # Index by both entity IDs
        for eid in (r["source_id"], r["target_id"]):
            rels_by_entity.setdefault(eid, []).append(rel)

    # ---- Entity sources ----
    entity_sources = {}
    es_rows = db.execute(
        """SELECT es.entity_id, s.id, s.title, s.url, s.source_type, s.author, s.year
           FROM sources s
           JOIN entity_sources es ON es.source_id = s.id
           ORDER BY s.year"""
    ).fetchall()
    for row in es_rows:
        eid = row["entity_id"]
        entity_sources.setdefault(eid, []).append({
            "id": row["id"],
            "title": row["title"],
            "url": row["url"],
            "source_type": row["source_type"],
            "author": row["author"],
            "year": row["year"],
        })

    # ---- Graph (full) ----
    conn_count = {}
    edges = []
    for r in rels_raw:
        conn_count[r["source_id"]] = conn_count.get(r["source_id"], 0) + 1
        conn_count[r["target_id"]] = conn_count.get(r["target_id"], 0) + 1
        edges.append({
            "id": r["id"],
            "source": r["source_id"],
            "target": r["target_id"],
            "relationship_type": r["relationship_type"],
            "evidence_tier": r["evidence_tier"],
            "description": r["description"],
            "year_start": r["year_start"],
            "year_end": r["year_end"],
        })

    nodes = []
    for e in entities_raw:
        meta = e["metadata"]
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except (json.JSONDecodeError, TypeError):
                meta = {}
        photo = meta.get("photo_url", "") if isinstance(meta, dict) else ""
        if photo.startswith("/static/"):
            photo = photo[len("/static/"):]
        nodes.append({
            "id": e["id"],
            "name": e["name"],
            "entity_type": e["entity_type"],
            "connection_count": conn_count.get(e["id"], 0),
            "photo_url": photo,
        })

    graph = {"nodes": nodes, "edges": edges}

    # ---- Signals ----
    sig_rows = db.execute(
        """SELECT id, entity_id, source_feed, headline, url, snippet,
                  matched_name, published_at, collected_at
           FROM signals
           WHERE relevance != 'dismissed'
           ORDER BY collected_at DESC"""
    ).fetchall()
    signals_by_entity = {}
    for row in sig_rows:
        eid = str(row["entity_id"])
        signals_by_entity.setdefault(eid, []).append({
            "id": row["id"],
            "source_feed": row["source_feed"],
            "headline": row["headline"],
            "url": row["url"],
            "snippet": row["snippet"],
            "matched_name": row["matched_name"],
            "published_at": row["published_at"],
            "collected_at": row["collected_at"],
        })
    sig_count = len(sig_rows)

    # ---- Stats ----
    ent_count = db.execute("SELECT COUNT(*) as c FROM entities").fetchone()["c"]
    rel_count = db.execute("SELECT COUNT(*) as c FROM relationships").fetchone()["c"]
    src_count = db.execute("SELECT COUNT(*) as c FROM sources").fetchone()["c"]
    by_type = {
        r["entity_type"]: r["c"]
        for r in db.execute(
            "SELECT entity_type, COUNT(*) as c FROM entities GROUP BY entity_type"
        ).fetchall()
    }
    by_tier = {
        r["evidence_tier"]: r["c"]
        for r in db.execute(
            "SELECT evidence_tier, COUNT(*) as c FROM relationships GROUP BY evidence_tier"
        ).fetchall()
    }
    stats = {
        "entities": ent_count,
        "relationships": rel_count,
        "sources": src_count,
        "signals": sig_count,
        "by_type": by_type,
        "by_tier": by_tier,
    }

    # ---- Centrality (pre-compute degree centrality) ----
    degree = {}
    for e in edges:
        degree[e["source"]] = degree.get(e["source"], 0) + 1
        degree[e["target"]] = degree.get(e["target"], 0) + 1
    n = len(nodes)
    centrality = []
    if n > 1:
        for nid, deg in sorted(degree.items(), key=lambda x: x[1], reverse=True):
            ent = entities_by_id.get(nid)
            if ent:
                centrality.append({
                    "id": nid,
                    "name": ent["name"],
                    "entity_type": ent["entity_type"],
                    "centrality": round(deg / (n - 1), 4),
                })

    # ---- Write JSON files ----
    def write_json(filename, data):
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w") as f:
            json.dump(data, f, separators=(",", ":"))
        size = os.path.getsize(path)
        print(f"  {filename}: {size:,} bytes")

    print(f"Exporting to {OUT_DIR}/")
    write_json("graph.json", graph)
    write_json("stats.json", stats)
    write_json("entities.json", entities_by_id)
    write_json("relationships.json", {str(k): v for k, v in rels_by_entity.items()})
    write_json("sources.json", {str(k): v for k, v in entity_sources.items()})
    write_json("centrality.json", centrality)
    write_json("signals.json", signals_by_entity)

    # ---- Geo-enriched exports ----
    export_geo(db, OUT_DIR)

    db.close()
    print(f"\nDone. {len(nodes)} entities, {len(edges)} edges, {src_count} sources, {sig_count} signals exported.")


if __name__ == "__main__":
    main()
