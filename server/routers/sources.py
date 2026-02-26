"""Source CRUD."""

from fastapi import APIRouter, Query
from server.db import get_db
from server.models import SourceCreate, SourceOut

router = APIRouter(prefix="/api/sources", tags=["sources"])


@router.get("", response_model=list[SourceOut])
async def list_sources(limit: int = Query(500, le=2000)):
    db = await get_db()
    rows = await db.execute_fetchall("SELECT * FROM sources ORDER BY title LIMIT ?", (limit,))
    return [SourceOut(**dict(r)) for r in rows]


@router.post("", response_model=SourceOut, status_code=201)
async def create_source(body: SourceCreate):
    db = await get_db()
    cur = await db.execute(
        "INSERT INTO sources (title, url, source_type, author, year) VALUES (?, ?, ?, ?, ?)",
        (body.title, body.url, body.source_type, body.author, body.year),
    )
    await db.commit()
    rows = await db.execute_fetchall("SELECT * FROM sources WHERE id=?", (cur.lastrowid,))
    return SourceOut(**dict(rows[0]))
