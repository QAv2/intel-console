"""Relationship CRUD with source linking."""

from fastapi import APIRouter, HTTPException, Query
from server.db import get_db
from server.models import RelationshipCreate, RelationshipOut

router = APIRouter(prefix="/api/relationships", tags=["relationships"])


async def _enrich_rel(db, row) -> RelationshipOut:
    sources = await db.execute_fetchall(
        """SELECT s.id, s.title, s.url, s.source_type
           FROM sources s
           JOIN relationship_sources rs ON rs.source_id = s.id
           WHERE rs.relationship_id = ?""",
        (row["id"],),
    )
    return RelationshipOut(
        id=row["id"],
        source_id=row["source_id"],
        target_id=row["target_id"],
        relationship_type=row["relationship_type"],
        evidence_tier=row["evidence_tier"],
        description=row["description"],
        year_start=row["year_start"],
        year_end=row["year_end"],
        sources=[dict(s) for s in sources],
    )


@router.get("", response_model=list[RelationshipOut])
async def list_relationships(
    entity_id: int | None = None,
    evidence_tier: str | None = None,
    limit: int = Query(500, le=2000),
):
    db = await get_db()
    query = "SELECT * FROM relationships WHERE 1=1"
    params: list = []
    if entity_id is not None:
        query += " AND (source_id=? OR target_id=?)"
        params += [entity_id, entity_id]
    if evidence_tier:
        query += " AND evidence_tier=?"
        params.append(evidence_tier)
    query += " LIMIT ?"
    params.append(limit)
    rows = await db.execute_fetchall(query, params)
    return [await _enrich_rel(db, r) for r in rows]


@router.post("", response_model=RelationshipOut, status_code=201)
async def create_relationship(body: RelationshipCreate):
    db = await get_db()
    # Validate entities exist
    for eid in (body.source_id, body.target_id):
        rows = await db.execute_fetchall("SELECT id FROM entities WHERE id=?", (eid,))
        if not rows:
            raise HTTPException(404, f"Entity {eid} not found")
    cur = await db.execute(
        """INSERT INTO relationships
           (source_id, target_id, relationship_type, evidence_tier, description, year_start, year_end)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (body.source_id, body.target_id, body.relationship_type,
         body.evidence_tier, body.description, body.year_start, body.year_end),
    )
    rel_id = cur.lastrowid
    # Link sources
    for sid in body.source_ids:
        await db.execute(
            "INSERT OR IGNORE INTO relationship_sources (relationship_id, source_id) VALUES (?, ?)",
            (rel_id, sid),
        )
    await db.commit()
    rows = await db.execute_fetchall("SELECT * FROM relationships WHERE id=?", (rel_id,))
    return await _enrich_rel(db, rows[0])
