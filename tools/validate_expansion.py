#!/usr/bin/env python3
"""Validate an expansion module BEFORE inserting it into the DB.

Usage (from ~/intel-console):
    python3 tools/validate_expansion.py seed.expansion_foo [--source-range 1500 1599]

Checks:
  * module imports; SOURCES / ENTITIES / RELATIONSHIPS / ENTITY_SOURCES present
  * source ids unique, inside the allotted range, and not already in the DB
  * source_type / entity_type / evidence tier values are schema-legal
  * every relationship references sources that exist in the module (or DB)
  * every relationship source/target name resolves to a module entity or an
    existing DB entity (exact-name match); no self-loops
  * relationship field names are the add_expansion names: type / tier / desc
  * ENTITY_SOURCES is a dict {entity_name: [source_ids]}
  * optional ENTITY_UPDATES entries reference existing DB entities
  * optional GEO_COORDS / PHOTO_CANDIDATES keys reference module or DB entities
Exit code 0 = clean, 1 = problems found.
"""

import importlib
import os
import sqlite3
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
DB = os.path.join(ROOT, "data", "intel.db")

ENTITY_TYPES = {
    "person", "organization", "agency", "program", "contract", "shell_company",
    "foundation", "event", "legislation", "facility", "publication",
}
SOURCE_TYPES = {
    "congressional", "court", "foia", "government", "journalism", "academic",
    "archive", "documentary", "book", "other",
}
TIERS = {"documented", "credible", "inference", "speculative"}


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    modname = sys.argv[1]
    rng = None
    if "--source-range" in sys.argv:
        i = sys.argv.index("--source-range")
        rng = (int(sys.argv[i + 1]), int(sys.argv[i + 2]))

    problems = []
    warn = []

    try:
        mod = importlib.import_module(modname)
    except Exception as e:  # noqa
        print(f"FAIL: cannot import {modname}: {e}")
        sys.exit(1)

    SOURCES = getattr(mod, "SOURCES", None)
    ENTITIES = getattr(mod, "ENTITIES", None)
    RELATIONSHIPS = getattr(mod, "RELATIONSHIPS", None)
    ENTITY_SOURCES = getattr(mod, "ENTITY_SOURCES", None)
    ENTITY_UPDATES = getattr(mod, "ENTITY_UPDATES", [])
    GEO = getattr(mod, "GEO_COORDS", {})
    PHOTOS = getattr(mod, "PHOTO_CANDIDATES", {})

    for nm, val, typ in (("SOURCES", SOURCES, list), ("ENTITIES", ENTITIES, list),
                         ("RELATIONSHIPS", RELATIONSHIPS, list), ("ENTITY_SOURCES", ENTITY_SOURCES, dict)):
        if not isinstance(val, typ):
            problems.append(f"{nm} missing or not a {typ.__name__}")
    if problems:
        for p in problems:
            print("FAIL:", p)
        sys.exit(1)

    db = sqlite3.connect(DB)
    db_names = {r[0]: r[1] for r in db.execute("SELECT name, entity_type FROM entities")}
    db_source_ids = {r[0] for r in db.execute("SELECT id FROM sources")}
    db_lower = {n.lower(): n for n in db_names}

    # ---- sources ----
    src_ids = set()
    for s in SOURCES:
        sid = s.get("id")
        if not isinstance(sid, int):
            problems.append(f"source without int id: {s}")
            continue
        if sid in src_ids:
            problems.append(f"duplicate source id in module: {sid}")
        src_ids.add(sid)
        if sid in db_source_ids:
            problems.append(f"source id {sid} already exists in DB (collision)")
        if rng and not (rng[0] <= sid <= rng[1]):
            problems.append(f"source id {sid} outside allotted range {rng}")
        if not s.get("title"):
            problems.append(f"source {sid} has no title")
        url = s.get("url", "")
        if not url or not url.startswith("http"):
            problems.append(f"source {sid} has no http URL")
        st = s.get("source_type", "journalism")
        if st not in SOURCE_TYPES:
            problems.append(f"source {sid} illegal source_type '{st}'")
        if s.get("year") is not None and not isinstance(s.get("year"), int):
            problems.append(f"source {sid} year must be int or None")

    # ---- entities ----
    mod_names = {}
    for e in ENTITIES:
        n = e.get("name")
        if not n:
            problems.append(f"entity without name: {e}")
            continue
        if n in mod_names:
            problems.append(f"duplicate entity name in module: {n}")
        mod_names[n] = e.get("entity_type")
        if e.get("entity_type") not in ENTITY_TYPES:
            problems.append(f"entity '{n}' illegal entity_type '{e.get('entity_type')}'")
        if n in db_names:
            warn.append(f"entity '{n}' already exists in DB as {db_names[n]} — add_expansion will SKIP it "
                        f"(fine if intentional; use ENTITY_UPDATES to change it)")
        elif n.lower() in db_lower:
            problems.append(f"entity '{n}' differs only by case from existing '{db_lower[n.lower()]}' — use exact name")
        if not (e.get("description") or "").strip():
            problems.append(f"entity '{n}' has empty description")
        if not isinstance(e.get("metadata", {}), dict):
            problems.append(f"entity '{n}' metadata must be a dict")

    def resolve(name):
        if name in mod_names or name in db_names:
            return True
        return False

    # ---- relationships ----
    seen = set()
    for i, r in enumerate(RELATIONSHIPS):
        for bad, good in (("rel_type", "type"), ("evidence_tier", "tier"), ("description", "desc")):
            if bad in r:
                problems.append(f"relationship #{i} uses '{bad}' — must be '{good}'")
        s, t = r.get("source"), r.get("target")
        if not s or not t:
            problems.append(f"relationship #{i} missing source/target")
            continue
        if s == t:
            problems.append(f"relationship #{i} self-loop '{s}'")
        for nm in (s, t):
            if not resolve(nm):
                hint = db_lower.get(nm.lower())
                problems.append(f"relationship #{i}: entity '{nm}' not in module or DB"
                                + (f" (did you mean '{hint}'?)" if hint else ""))
        if r.get("tier") not in TIERS:
            problems.append(f"relationship #{i} ({s} -> {t}) illegal tier '{r.get('tier')}'")
        if not r.get("type"):
            problems.append(f"relationship #{i} ({s} -> {t}) has no type")
        if not (r.get("desc") or "").strip():
            problems.append(f"relationship #{i} ({s} -> {t}) has empty desc")
        srcs = r.get("sources", [])
        if not srcs:
            problems.append(f"relationship #{i} ({s} -> {t}) has NO sources — every edge must be sourced")
        for sid in srcs:
            if sid not in src_ids and sid not in db_source_ids:
                problems.append(f"relationship #{i} ({s} -> {t}) references unknown source id {sid}")
        key = (s, t, r.get("type"))
        if key in seen:
            problems.append(f"duplicate relationship in module: {key}")
        seen.add(key)
        for yk in ("year_start", "year_end"):
            if r.get(yk) is not None and not isinstance(r.get(yk), int):
                problems.append(f"relationship #{i} {yk} must be int or None")

    # ---- entity sources ----
    for n, ids in ENTITY_SOURCES.items():
        if not resolve(n):
            problems.append(f"ENTITY_SOURCES: entity '{n}' not in module or DB")
        if not isinstance(ids, (list, tuple)):
            problems.append(f"ENTITY_SOURCES['{n}'] must be a list of source ids")
            continue
        for sid in ids:
            if sid not in src_ids and sid not in db_source_ids:
                problems.append(f"ENTITY_SOURCES['{n}'] unknown source id {sid}")
    for n in mod_names:
        if n not in ENTITY_SOURCES:
            warn.append(f"new entity '{n}' has no ENTITY_SOURCES entry")

    # ---- entity updates ----
    for u in ENTITY_UPDATES:
        n = u.get("name")
        if n not in db_names:
            problems.append(f"ENTITY_UPDATES: '{n}' is not an existing DB entity")
        if not any(k in u for k in ("description_append", "metadata", "aliases_add", "description_replace")):
            problems.append(f"ENTITY_UPDATES['{n}'] has nothing to apply")
        for sid in u.get("sources", []):
            if sid not in src_ids and sid not in db_source_ids:
                problems.append(f"ENTITY_UPDATES['{n}'] unknown source id {sid}")

    # ---- geo / photos ----
    for n, v in GEO.items():
        if not resolve(n):
            problems.append(f"GEO_COORDS: '{n}' not in module or DB")
        if not (isinstance(v, (tuple, list)) and len(v) >= 3 and v[2] in TIERS):
            problems.append(f"GEO_COORDS['{n}'] must be (lat, lon, tier[, note])")
    for n, v in PHOTOS.items():
        if not resolve(n):
            problems.append(f"PHOTO_CANDIDATES: '{n}' not in module or DB")
        if not (isinstance(v, str) and v.startswith("http")):
            problems.append(f"PHOTO_CANDIDATES['{n}'] must be an http URL")

    print(f"{modname}: {len(SOURCES)} sources, {len(ENTITIES)} entities, {len(RELATIONSHIPS)} relationships, "
          f"{len(ENTITY_UPDATES)} entity updates, {len(GEO)} geo, {len(PHOTOS)} photo candidates")
    for w in warn:
        print("WARN:", w)
    for p in problems:
        print("FAIL:", p)
    if problems:
        print(f"\n{len(problems)} problem(s).")
        sys.exit(1)
    print("OK — module validates clean.")


if __name__ == "__main__":
    main()
