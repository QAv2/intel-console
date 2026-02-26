"""Entity CRUD + FTS5 search."""

import json
from fastapi import APIRouter, HTTPException, Query
from server.db import get_db
from server.models import EntityCreate, EntityUpdate, EntityOut

router = APIRouter(prefix="/api/entities", tags=["entities"])


def _row_to_entity(row) -> EntityOut:
    return EntityOut(
        id=row["id"],
        name=row["name"],
        entity_type=row["entity_type"],
        description=row["description"],
        aliases=row["aliases"],
        metadata=json.loads(row["metadata"]) if row["metadata"] else {},
    )


@router.get("", response_model=list[EntityOut])
async def list_entities(
    entity_type: str | None = None,
    limit: int = Query(500, le=2000),
    offset: int = 0,
):
    db = await get_db()
    if entity_type:
        rows = await db.execute_fetchall(
            "SELECT * FROM entities WHERE entity_type=? ORDER BY name LIMIT ? OFFSET ?",
            (entity_type, limit, offset),
        )
    else:
        rows = await db.execute_fetchall(
            "SELECT * FROM entities ORDER BY name LIMIT ? OFFSET ?",
            (limit, offset),
        )
    return [_row_to_entity(r) for r in rows]


@router.post("", response_model=EntityOut, status_code=201)
async def create_entity(body: EntityCreate):
    db = await get_db()
    try:
        cur = await db.execute(
            """INSERT INTO entities (name, entity_type, description, aliases, metadata)
               VALUES (?, ?, ?, ?, ?)""",
            (body.name, body.entity_type, body.description, body.aliases, json.dumps(body.metadata)),
        )
        await db.commit()
    except Exception as e:
        if "UNIQUE" in str(e):
            raise HTTPException(409, f"Entity '{body.name}' ({body.entity_type}) already exists")
        raise
    row = await db.execute_fetchall("SELECT * FROM entities WHERE id=?", (cur.lastrowid,))
    return _row_to_entity(row[0])


@router.get("/search", response_model=list[EntityOut])
async def search_entities(q: str = Query(..., min_length=1), limit: int = 20):
    db = await get_db()
    # FTS5 match with prefix search
    fts_query = q.replace('"', '""') + "*"
    rows = await db.execute_fetchall(
        """SELECT e.* FROM entities_fts fts
           JOIN entities e ON e.id = fts.rowid
           WHERE entities_fts MATCH ?
           ORDER BY rank LIMIT ?""",
        (fts_query, limit),
    )
    return [_row_to_entity(r) for r in rows]


@router.get("/{entity_id}", response_model=EntityOut)
async def get_entity(entity_id: int):
    db = await get_db()
    rows = await db.execute_fetchall("SELECT * FROM entities WHERE id=?", (entity_id,))
    if not rows:
        raise HTTPException(404, "Entity not found")
    return _row_to_entity(rows[0])


@router.put("/{entity_id}", response_model=EntityOut)
async def update_entity(entity_id: int, body: EntityUpdate):
    db = await get_db()
    rows = await db.execute_fetchall("SELECT * FROM entities WHERE id=?", (entity_id,))
    if not rows:
        raise HTTPException(404, "Entity not found")
    existing = rows[0]
    updates = {}
    if body.name is not None:
        updates["name"] = body.name
    if body.entity_type is not None:
        updates["entity_type"] = body.entity_type
    if body.description is not None:
        updates["description"] = body.description
    if body.aliases is not None:
        updates["aliases"] = body.aliases
    if body.metadata is not None:
        updates["metadata"] = json.dumps(body.metadata)
    if updates:
        sets = ", ".join(f"{k}=?" for k in updates)
        vals = list(updates.values()) + [entity_id]
        await db.execute(f"UPDATE entities SET {sets}, updated_at=datetime('now') WHERE id=?", vals)
        await db.commit()
    rows = await db.execute_fetchall("SELECT * FROM entities WHERE id=?", (entity_id,))
    return _row_to_entity(rows[0])


@router.get("/{entity_id}/sources")
async def get_entity_sources(entity_id: int):
    db = await get_db()
    rows = await db.execute_fetchall(
        """SELECT s.id, s.title, s.url, s.source_type, s.author, s.year
           FROM sources s
           JOIN entity_sources es ON es.source_id = s.id
           WHERE es.entity_id = ?
           ORDER BY s.year""",
        (entity_id,),
    )
    return [dict(r) for r in rows]


@router.delete("/{entity_id}", status_code=204)
async def delete_entity(entity_id: int):
    db = await get_db()
    rows = await db.execute_fetchall("SELECT id FROM entities WHERE id=?", (entity_id,))
    if not rows:
        raise HTTPException(404, "Entity not found")
    await db.execute("DELETE FROM entities WHERE id=?", (entity_id,))
    await db.commit()
