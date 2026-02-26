#!/usr/bin/env bash
# Intel Console — one-command launcher
set -euo pipefail
cd "$(dirname "$0")"

# Seed database if empty
if [ ! -f data/intel.db ]; then
    echo "[*] Initializing database and seeding data..."
    uv run python -m seed.seed_db
fi

echo "[*] Starting Intel Console on http://localhost:8800"
exec uv run uvicorn server.app:app --host 0.0.0.0 --port 8800 --reload
