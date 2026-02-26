"""SQLite connection management with schema initialization."""

import aiosqlite
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "intel.db"
SCHEMA_PATH = Path(__file__).parent.parent / "schema.sql"

_db: aiosqlite.Connection | None = None


async def get_db() -> aiosqlite.Connection:
    global _db
    if _db is None:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        _db = await aiosqlite.connect(str(DB_PATH))
        _db.row_factory = aiosqlite.Row
        await _db.execute("PRAGMA journal_mode=WAL")
        await _db.execute("PRAGMA foreign_keys=ON")
    return _db


async def init_db():
    """Run schema.sql to create tables if they don't exist."""
    db = await get_db()
    schema = SCHEMA_PATH.read_text()
    await db.executescript(schema)
    await db.commit()


async def close_db():
    global _db
    if _db is not None:
        await _db.close()
        _db = None
