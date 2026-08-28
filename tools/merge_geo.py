#!/usr/bin/env python3
"""Merge GEO_COORDS declared by expansion modules into geo_enrich.py's GEO_COORDS
table (appended as a clearly-marked block, keyed by entity name, idempotent).

Usage:  cd ~/intel-console && python3 tools/merge_geo.py seed.expansion_a seed.expansion_b ...
"""

import importlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
GEO_PY = os.path.join(ROOT, "geo_enrich.py")


def main():
    mods = [a for a in sys.argv[1:] if not a.startswith("--")]
    src = open(GEO_PY).read()
    existing = set(re.findall(r'^\s+"([^"]+)":\s*\(', src, flags=re.M))
    new_lines = []
    for modname in mods:
        mod = importlib.import_module(modname)
        geo = getattr(mod, "GEO_COORDS", {})
        for name, val in geo.items():
            if name in existing:
                continue
            lat, lon, tier = val[0], val[1], val[2]
            note = val[3] if len(val) > 3 else ""
            key = f'"{name}":'
            new_lines.append(f'    {key:44s} ({lat:.4f}, {lon:.4f}, "{tier}"),' + (f"   # {note}" if note else ""))
            existing.add(name)
    if not new_lines:
        print("nothing to merge")
        return
    block = (
        "\n    # ══════════════════════════════════════════════════════════════════════\n"
        "    # 2026-08 REFRESH PASS — merged from expansion modules by tools/merge_geo.py\n"
        "    # ══════════════════════════════════════════════════════════════════════\n"
        + "\n".join(new_lines) + "\n"
    )
    # insert before the closing brace of GEO_COORDS: find "GEO_COORDS = {" then its matching top-level "}"
    start = src.index("GEO_COORDS = {")
    end = src.index("\n}", start)
    src = src[:end] + "\n" + block + src[end:]
    open(GEO_PY, "w").write(src)
    print(f"merged {len(new_lines)} geo entries into geo_enrich.py")


if __name__ == "__main__":
    main()
