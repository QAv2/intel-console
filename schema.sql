-- Intel Console Schema
-- SQLite with FTS5 full-text search

PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

-- ============================================================
-- Core Tables
-- ============================================================

CREATE TABLE IF NOT EXISTS entities (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    entity_type TEXT NOT NULL CHECK (entity_type IN (
        'person','organization','agency','program','contract',
        'shell_company','foundation','event','legislation','facility','publication'
    )),
    description TEXT DEFAULT '',
    aliases     TEXT DEFAULT '',          -- comma-separated alternate names
    metadata    TEXT DEFAULT '{}',        -- JSON blob for flexible fields
    created_at  TEXT DEFAULT (datetime('now')),
    updated_at  TEXT DEFAULT (datetime('now'))
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_entities_name_type
    ON entities(name, entity_type);

CREATE TABLE IF NOT EXISTS relationships (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id       INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    target_id       INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    relationship_type TEXT NOT NULL,
    evidence_tier   TEXT NOT NULL CHECK (evidence_tier IN (
        'documented','credible','inference','speculative'
    )),
    description     TEXT DEFAULT '',
    year_start      INTEGER,
    year_end        INTEGER,
    created_at      TEXT DEFAULT (datetime('now')),
    CHECK (source_id != target_id)
);

CREATE INDEX IF NOT EXISTS idx_rel_source ON relationships(source_id);
CREATE INDEX IF NOT EXISTS idx_rel_target ON relationships(target_id);
CREATE INDEX IF NOT EXISTS idx_rel_tier   ON relationships(evidence_tier);

CREATE TABLE IF NOT EXISTS sources (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL,
    url         TEXT DEFAULT '',
    source_type TEXT DEFAULT 'journalism' CHECK (source_type IN (
        'congressional','court','foia','government','journalism',
        'academic','archive','documentary','book','other'
    )),
    author      TEXT DEFAULT '',
    year        INTEGER,
    created_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS relationship_sources (
    relationship_id INTEGER NOT NULL REFERENCES relationships(id) ON DELETE CASCADE,
    source_id       INTEGER NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    PRIMARY KEY (relationship_id, source_id)
);

CREATE TABLE IF NOT EXISTS entity_sources (
    entity_id   INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    source_id   INTEGER NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    PRIMARY KEY (entity_id, source_id)
);

CREATE TABLE IF NOT EXISTS tags (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS entity_tags (
    entity_id INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    tag_id    INTEGER NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (entity_id, tag_id)
);

CREATE TABLE IF NOT EXISTS notes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id   INTEGER REFERENCES entities(id) ON DELETE CASCADE,
    rel_id      INTEGER REFERENCES relationships(id) ON DELETE CASCADE,
    content     TEXT NOT NULL,
    created_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS seed_provenance (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id   INTEGER REFERENCES entities(id) ON DELETE CASCADE,
    rel_id      INTEGER REFERENCES relationships(id) ON DELETE CASCADE,
    origin      TEXT NOT NULL,               -- 'curated', 'ai_extracted', 'osint_scraper'
    origin_ref  TEXT DEFAULT '',             -- e.g. node ID from disclosure-data.json
    confidence  REAL DEFAULT 1.0,
    reviewed    INTEGER DEFAULT 0,
    created_at  TEXT DEFAULT (datetime('now'))
);

-- ============================================================
-- Signals (temporal news/feed layer)
-- ============================================================

CREATE TABLE IF NOT EXISTS signals (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id     INTEGER NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    source_feed   TEXT NOT NULL,
    headline      TEXT NOT NULL,
    url           TEXT NOT NULL,
    snippet       TEXT DEFAULT '',
    matched_name  TEXT DEFAULT '',
    published_at  TEXT DEFAULT '',
    collected_at  TEXT DEFAULT (datetime('now')),
    relevance     TEXT DEFAULT 'auto' CHECK (relevance IN ('auto','confirmed','dismissed'))
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_signals_dedup ON signals(url, entity_id);
CREATE INDEX IF NOT EXISTS idx_signals_entity ON signals(entity_id);
CREATE INDEX IF NOT EXISTS idx_signals_collected ON signals(collected_at);

-- ============================================================
-- FTS5 Virtual Table
-- ============================================================

CREATE VIRTUAL TABLE IF NOT EXISTS entities_fts USING fts5(
    name, description, aliases,
    content='entities',
    content_rowid='id'
);

-- Triggers to keep FTS in sync
CREATE TRIGGER IF NOT EXISTS entities_ai AFTER INSERT ON entities BEGIN
    INSERT INTO entities_fts(rowid, name, description, aliases)
    VALUES (new.id, new.name, new.description, new.aliases);
END;

CREATE TRIGGER IF NOT EXISTS entities_ad AFTER DELETE ON entities BEGIN
    INSERT INTO entities_fts(entities_fts, rowid, name, description, aliases)
    VALUES ('delete', old.id, old.name, old.description, old.aliases);
END;

CREATE TRIGGER IF NOT EXISTS entities_au AFTER UPDATE ON entities BEGIN
    INSERT INTO entities_fts(entities_fts, rowid, name, description, aliases)
    VALUES ('delete', old.id, old.name, old.description, old.aliases);
    INSERT INTO entities_fts(rowid, name, description, aliases)
    VALUES (new.id, new.name, new.description, new.aliases);
END;
