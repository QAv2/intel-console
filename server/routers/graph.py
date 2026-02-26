"""Graph endpoints — full graph data + NetworkX algorithms."""

import json
from fastapi import APIRouter, Query, HTTPException
from server.db import get_db
from server.models import GraphData, GraphNode, GraphEdge, Stats
import networkx as nx

router = APIRouter(prefix="/api/graph", tags=["graph"])

TIER_ORDER = {"documented": 0, "credible": 1, "inference": 2, "speculative": 3}


async def _build_nx_graph(db, min_tier: str = "speculative") -> nx.Graph:
    """Build a NetworkX graph filtered by minimum evidence tier."""
    threshold = TIER_ORDER.get(min_tier, 3)
    rows = await db.execute_fetchall("SELECT * FROM relationships")
    G = nx.Graph()
    for r in rows:
        if TIER_ORDER.get(r["evidence_tier"], 3) <= threshold:
            G.add_edge(r["source_id"], r["target_id"], id=r["id"],
                       rel_type=r["relationship_type"], tier=r["evidence_tier"])
    # Add isolated entities
    entities = await db.execute_fetchall("SELECT id FROM entities")
    for e in entities:
        G.add_node(e["id"])
    return G


@router.get("/full", response_model=GraphData)
async def full_graph(min_tier: str = Query("speculative")):
    """Return full graph data for Cytoscape.js rendering."""
    db = await get_db()
    threshold = TIER_ORDER.get(min_tier, 3)

    entities = await db.execute_fetchall("SELECT * FROM entities")
    relationships = await db.execute_fetchall("SELECT * FROM relationships")

    # Count connections per entity
    conn_count: dict[int, int] = {}
    edges = []
    for r in relationships:
        if TIER_ORDER.get(r["evidence_tier"], 3) <= threshold:
            conn_count[r["source_id"]] = conn_count.get(r["source_id"], 0) + 1
            conn_count[r["target_id"]] = conn_count.get(r["target_id"], 0) + 1
            edges.append(GraphEdge(
                id=r["id"],
                source=r["source_id"],
                target=r["target_id"],
                relationship_type=r["relationship_type"],
                evidence_tier=r["evidence_tier"],
                description=r["description"],
                year_start=r["year_start"],
                year_end=r["year_end"],
            ))

    nodes = []
    for e in entities:
        meta = e["metadata"]
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except (json.JSONDecodeError, TypeError):
                meta = {}
        nodes.append(GraphNode(
            id=e["id"],
            name=e["name"],
            entity_type=e["entity_type"],
            connection_count=conn_count.get(e["id"], 0),
            photo_url=meta.get("photo_url", "") if isinstance(meta, dict) else "",
        ))
    return GraphData(nodes=nodes, edges=edges)


@router.get("/neighborhood/{entity_id}", response_model=GraphData)
async def neighborhood(entity_id: int, depth: int = Query(1, ge=1, le=3)):
    """Return ego graph around an entity."""
    db = await get_db()
    G = await _build_nx_graph(db)
    if entity_id not in G:
        raise HTTPException(404, "Entity not found in graph")
    ego = nx.ego_graph(G, entity_id, radius=depth)
    node_ids = set(ego.nodes())

    entities = await db.execute_fetchall(
        f"SELECT * FROM entities WHERE id IN ({','.join('?' * len(node_ids))})",
        list(node_ids),
    )
    relationships = await db.execute_fetchall("SELECT * FROM relationships")
    edges = [
        GraphEdge(id=r["id"], source=r["source_id"], target=r["target_id"],
                  relationship_type=r["relationship_type"],
                  evidence_tier=r["evidence_tier"], description=r["description"],
                  year_start=r["year_start"], year_end=r["year_end"])
        for r in relationships
        if r["source_id"] in node_ids and r["target_id"] in node_ids
    ]
    conn_count: dict[int, int] = {}
    for e in edges:
        conn_count[e.source] = conn_count.get(e.source, 0) + 1
        conn_count[e.target] = conn_count.get(e.target, 0) + 1
    nodes = []
    for e in entities:
        meta = e["metadata"]
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except (json.JSONDecodeError, TypeError):
                meta = {}
        nodes.append(GraphNode(
            id=e["id"], name=e["name"], entity_type=e["entity_type"],
            connection_count=conn_count.get(e["id"], 0),
            photo_url=meta.get("photo_url", "") if isinstance(meta, dict) else "",
        ))
    return GraphData(nodes=nodes, edges=edges)


@router.get("/shortest-path")
async def shortest_path(from_id: int = Query(..., alias="from"), to_id: int = Query(..., alias="to")):
    db = await get_db()
    G = await _build_nx_graph(db)
    try:
        path = nx.shortest_path(G, from_id, to_id)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        raise HTTPException(404, "No path found")
    return {"path": path, "length": len(path) - 1}


@router.get("/centrality")
async def centrality(limit: int = Query(20, le=100)):
    db = await get_db()
    G = await _build_nx_graph(db)
    bc = nx.betweenness_centrality(G)
    ranked = sorted(bc.items(), key=lambda x: x[1], reverse=True)[:limit]
    entities = await db.execute_fetchall("SELECT id, name, entity_type FROM entities")
    name_map = {e["id"]: {"name": e["name"], "type": e["entity_type"]} for e in entities}
    return [
        {"id": nid, "name": name_map.get(nid, {}).get("name", "?"),
         "entity_type": name_map.get(nid, {}).get("type", "?"),
         "centrality": round(score, 4)}
        for nid, score in ranked
    ]


@router.get("/stats", response_model=Stats)
async def stats():
    db = await get_db()
    ent_count = (await db.execute_fetchall("SELECT COUNT(*) as c FROM entities"))[0]["c"]
    rel_count = (await db.execute_fetchall("SELECT COUNT(*) as c FROM relationships"))[0]["c"]
    src_count = (await db.execute_fetchall("SELECT COUNT(*) as c FROM sources"))[0]["c"]
    by_type = {r["entity_type"]: r["c"] for r in await db.execute_fetchall(
        "SELECT entity_type, COUNT(*) as c FROM entities GROUP BY entity_type")}
    by_tier = {r["evidence_tier"]: r["c"] for r in await db.execute_fetchall(
        "SELECT evidence_tier, COUNT(*) as c FROM relationships GROUP BY evidence_tier")}
    return Stats(entities=ent_count, relationships=rel_count, sources=src_count,
                 by_type=by_type, by_tier=by_tier)
