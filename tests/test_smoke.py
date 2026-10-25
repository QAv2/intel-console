"""Smoke tests: catch a broken seed, a broken export, or a broken site.

Run with: uv run pytest
These never touch data/intel.db or static/data/ — everything is built in a
temp directory.
"""

import asyncio
import importlib
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"

EXPORT_FILES = [
    "graph.json", "stats.json", "entities.json", "relationships.json",
    "sources.json", "centrality.json", "signals.json",
    "geo-entities.json", "geo-signals.json",
]
TIERS = {"documented", "credible", "inference", "speculative"}

# Loaded by seed_db.py itself; every other expansion_*.py goes through add_expansion.
BASE_LAYERS = {"expansion_political", "expansion_financial", "expansion_hollywood", "expansion_inner_circle"}


def _expansion_modules():
    """Remaining expansion modules, in source-ID order (the order they were added)."""
    mods = []
    for path in sorted((ROOT / "seed").glob("expansion_*.py")):
        if path.stem in BASE_LAYERS:
            continue
        mod = importlib.import_module(f"seed.{path.stem}")
        first_id = min((s["id"] for s in mod.SOURCES), default=0)
        mods.append((first_id, f"seed.{path.stem}"))
    return [name for _, name in sorted(mods)]


@pytest.fixture(scope="session")
def seeded_db(tmp_path_factory):
    """Seed a fresh DB from seed/ (base + every expansion)."""
    import server.db
    from seed import seed_db
    from seed.add_expansion import add_expansion

    db_path = tmp_path_factory.mktemp("db") / "intel.db"
    original = server.db.DB_PATH
    server.db.DB_PATH = db_path
    try:
        asyncio.run(seed_db.seed())
        for mod in _expansion_modules():
            asyncio.run(add_expansion(mod))
    finally:
        server.db.DB_PATH = original
    return db_path


@pytest.fixture(scope="session")
def exported(seeded_db, tmp_path_factory, monkeypatch_session):
    """Run export_static.py against the seeded DB into a temp dir."""
    import export_static

    out_dir = tmp_path_factory.mktemp("export")
    monkeypatch_session.setattr(export_static, "DB_PATH", str(seeded_db))
    monkeypatch_session.setattr(export_static, "OUT_DIR", str(out_dir))
    export_static.main()
    return out_dir


@pytest.fixture(scope="session")
def monkeypatch_session():
    mp = pytest.MonkeyPatch()
    yield mp
    mp.undo()


def _load(d, name):
    return json.loads((Path(d) / name).read_text())


def test_export_from_seeds(exported):
    for name in EXPORT_FILES:
        assert (exported / name).is_file(), f"export did not write {name}"
        _load(exported, name)  # valid JSON

    graph = _load(exported, "graph.json")
    stats = _load(exported, "stats.json")
    assert len(graph["nodes"]) >= 250, "seeding produced far fewer entities than expected"
    assert len(graph["edges"]) >= 600
    assert stats["entities"] == len(graph["nodes"])
    assert stats["relationships"] == len(graph["edges"])
    assert {e["evidence_tier"] for e in graph["edges"]} <= TIERS


def test_committed_static_data_consistent():
    """The JSON the site actually serves is complete and self-consistent."""
    for name in EXPORT_FILES:
        assert (STATIC / "data" / name).is_file(), f"static/data/{name} missing"

    graph = _load(STATIC / "data", "graph.json")
    stats = _load(STATIC / "data", "stats.json")
    assert graph["nodes"] and graph["edges"]
    assert stats["entities"] == len(graph["nodes"])
    assert stats["relationships"] == len(graph["edges"])

    ids = {n["id"] for n in graph["nodes"]}
    dangling = [e["id"] for e in graph["edges"] if e["source"] not in ids or e["target"] not in ids]
    assert not dangling, f"edges point at missing entities: {dangling[:10]}"
    assert {e["evidence_tier"] for e in graph["edges"]} <= TIERS

    missing = [n["photo_url"] for n in graph["nodes"]
               if n.get("photo_url") and not (STATIC / n["photo_url"]).is_file()]
    assert not missing, f"photo files missing: {missing[:10]}"


def test_index_assets_exist():
    html = (STATIC / "index.html").read_text()
    refs = re.findall(r'(?:src|href)="([^"#:]+)"', html)
    assert refs
    missing = [r for r in refs if not (STATIC / r).is_file()]
    assert not missing, f"index.html references missing files: {missing}"


def test_api_and_site_serve(seeded_db, monkeypatch):
    import server.db
    from fastapi.testclient import TestClient
    from server.app import app

    monkeypatch.setattr(server.db, "DB_PATH", seeded_db)
    with TestClient(app) as client:
        for path in ["/", "/css/style.css", "/js/app.js", "/data/graph.json", "/static/css/style.css"]:
            assert client.get(path).status_code == 200, path
        stats = client.get("/api/graph/stats").json()
        assert stats["entities"] >= 250
        assert client.get("/api/entities/search", params={"q": "epstein"}).json()
        assert client.get("/api/graph/full").json()["edges"]


def test_site_in_headless_browser():
    """Runs tests/browser_smoke.js (Node + Playwright). Skipped if unavailable."""
    import shutil
    import subprocess

    node = shutil.which("node")
    if not node or subprocess.run([node, "-e", "require('playwright')"], capture_output=True).returncode:
        pytest.skip("node + playwright not installed")
    result = subprocess.run([node, str(ROOT / "tests" / "browser_smoke.js")],
                            capture_output=True, text=True, timeout=120)
    assert result.returncode == 0, result.stdout + result.stderr
