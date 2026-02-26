"""Tag management."""

from fastapi import APIRouter, Query
from server.db import get_db

router = APIRouter(prefix="/api/tags", tags=["tags"])


@router.get("")
async def list_tags():
    db = await get_db()
    rows = await db.execute_fetchall("SELECT * FROM tags ORDER BY name")
    return [dict(r) for r in rows]


@router.post("", status_code=201)
async def create_tag(name: str = Query(...)):
    db = await get_db()
    cur = await db.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (name,))
    await db.commit()
    return {"id": cur.lastrowid, "name": name}
