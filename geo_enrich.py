#!/usr/bin/env python3
"""Geocode intel-console entities and export geo-enriched JSON for WorldView globe."""

import json
import os
import sqlite3

# Hand-curated coordinate lookup — no API calls, no geocoding services.
# Evidence tiers: exact address = documented, org HQ = credible, person association = inference.
GEO_COORDS = {
    # ── Facilities (exact addresses) ──
    156: (40.7719, -73.9639, "documented"),   # 9 East 71st Street, NYC
    76:  (18.2999, -64.8257, "documented"),   # Little Saint James, USVI
    75:  (26.6777, -80.0367, "documented"),   # Mar-a-Lago, Palm Beach FL
    155: (34.8889, -105.8578, "documented"),  # Zorro Ranch, Stanley NM
    157: (40.7149, -74.0010, "documented"),   # MCC New York
    72:  (38.9076, -77.0603, "documented"),   # George Town Club, DC
    243: (48.8717, 2.2888, "documented"),     # 22 Avenue Foch, Paris

    # ── Agencies (HQ coordinates) ──
    85:  (38.9517, -77.1467, "documented"),   # CIA, Langley VA
    86:  (39.1086, -76.7714, "documented"),   # NSA, Fort Meade MD
    87:  (38.8977, -77.0248, "documented"),   # FBI, Hoover Building DC
    89:  (38.8934, -77.0249, "documented"),   # DOJ, DC
    90:  (38.8806, -77.1085, "documented"),   # DARPA, Arlington VA
    88:  (32.0490, 34.7625, "credible"),      # Mossad, Tel Aviv
    191: (51.4871, -0.1245, "documented"),    # MI6, Vauxhall Cross London
    190: (51.4959, -0.1264, "documented"),    # MI5, Thames House London
    242: (48.8337, 2.3835, "credible"),       # DGSE, Paris
    251: (52.5131, 13.3651, "credible"),      # BND, Berlin
    161: (55.7601, 37.6261, "credible"),      # FSB, Lubyanka Moscow
    172: (39.9053, 116.3977, "credible"),     # MSS, Beijing
    178: (24.6949, 46.7241, "credible"),      # Saudi GID, Riyadh
    205: (32.0684, 34.7916, "credible"),      # LAKAM, Tel Aviv
    206: (31.2530, 34.7915, "credible"),      # Unit 8200, Beersheba
    197: (51.5017, -0.1270, "credible"),      # Crown Prosecution Service, London
    194: (51.4988, -0.1341, "credible"),      # Metropolitan Police, London

    # ── Organizations (HQ locations) ──
    56:  (40.7580, -73.9713, "credible"),     # JPMorgan Chase, NYC
    57:  (50.1100, 8.6703, "credible"),       # Deutsche Bank, Frankfurt
    59:  (39.7539, -104.9994, "credible"),    # Palantir Technologies, Denver
    207: (32.1632, 34.7916, "credible"),      # NSO Group, Herzliya Israel
    285: (46.2260, 6.1866, "credible"),       # World Economic Forum, Cologny
    69:  (40.7627, -73.9736, "credible"),     # Apollo Global Management, NYC
    60:  (38.8807, -77.1060, "credible"),     # In-Q-Tel, Arlington VA
    61:  (40.7527, -73.9818, "credible"),     # Hill & Knowlton, NYC
    65:  (40.0848, -82.8968, "credible"),     # The Limited, Columbus OH
    143: (40.0848, -82.8968, "credible"),     # Victoria's Secret, Columbus OH
    67:  (32.0853, 34.7818, "credible"),      # Carbyne, Tel Aviv
    115: (40.7587, -73.9706, "credible"),     # Kissinger Associates, NYC
    54:  (51.5127, -0.0891, "credible"),      # BCCI, London (historical)
    184: (38.9044, -77.0398, "credible"),     # Carlyle Group, DC
    231: (38.9034, -77.0148, "credible"),     # Heritage Foundation, DC
    232: (38.9544, -77.3490, "credible"),     # Bechtel Corporation, Reston VA
    116: (41.8823, -87.6254, "credible"),     # Hollinger International, Chicago
    62:  (34.7465, -92.2896, "credible"),     # Rose Law Firm, Little Rock AR
    63:  (34.7465, -92.2896, "credible"),     # Systematics, Little Rock AR
    74:  (39.3643, -74.4229, "credible"),     # Resorts International, Atlantic City
    71:  (47.1934, 8.5166, "credible"),       # Glencore, Baar Switzerland
    182: (24.7136, 46.6753, "credible"),      # Kingdom Holding, Riyadh
    141: (25.7750, -80.1868, "credible"),     # MC2 Model Management, Miami
    240: (48.8726, 2.3124, "credible"),       # Elite Model Management, Paris
    73:  (40.7614, -73.9776, "credible"),     # Bayrock Group, NYC
    58:  (40.7551, -73.9744, "credible"),     # Bear Stearns, NYC
    154: (40.7822, -73.9540, "credible"),     # Dalton School, NYC
    130: (40.7580, -73.9717, "credible"),     # Towers Financial, NYC
    131: (40.7580, -73.9750, "credible"),     # Seagram, NYC (historical)
    275: (38.9072, -77.0369, "credible"),     # New Paradigm Institute, DC
    277: (38.0293, -78.4767, "credible"),     # Disclosure Project, Charlottesville VA
    278: (38.9007, -77.0302, "credible"),     # Americans for Safe Aerospace, DC
    55:  (38.9035, -77.0429, "credible"),     # First American Bank, DC
    66:  (40.7580, -73.9717, "credible"),     # Mega Group, NYC
    196: (51.5256, -0.0776, "credible"),      # Mirror Group Newspapers, London
    195: (51.7520, -1.2577, "credible"),      # Pergamon Press, Oxford
    183: (21.5433, 39.1728, "credible"),      # Saudi Binladin Group, Jeddah
    174: (6.1751, 106.8650, "credible"),      # Lippo Group, Jakarta (note: S hemisphere but positive for simplicity)
    173: (39.9192, 116.4614, "credible"),     # CITIC Group, Beijing
    142: (32.0853, 34.7818, "credible"),      # Black Cube, Tel Aviv
    201: (40.7580, -73.9717, "credible"),     # TerraMar Project, NYC
    64:  (25.7959, -80.2870, "credible"),     # Southern Air Transport, Miami
    186: (30.0444, 31.2357, "credible"),      # Safari Club, Cairo (historical origin)

    # ── High-centrality persons tied to a single dominant location ──
    4:   (40.0848, -82.8968, "inference"),    # Les Wexner → Columbus OH
    111: (40.7587, -73.9706, "inference"),    # Henry Kissinger → NYC (Kissinger Associates)
    287: (46.2260, 6.1866, "inference"),      # Klaus Schwab → WEF, Cologny
}

# Lippo Group latitude correction (South hemisphere)
GEO_COORDS[174] = (-6.1751, 106.8650, "credible")


def export_geo(db, out_dir):
    """Export geo-entities.json and geo-signals.json to out_dir."""
    db.row_factory = sqlite3.Row

    # ── Build connection counts + centrality ──
    edges = db.execute("SELECT source_id, target_id FROM relationships").fetchall()
    degree = {}
    for e in edges:
        degree[e["source_id"]] = degree.get(e["source_id"], 0) + 1
        degree[e["target_id"]] = degree.get(e["target_id"], 0) + 1

    n_entities = db.execute("SELECT COUNT(*) FROM entities").fetchone()[0]

    # ── Signal counts per entity ──
    sig_counts = {}
    for row in db.execute(
        "SELECT entity_id, COUNT(*) as c FROM signals "
        "WHERE relevance != 'dismissed' GROUP BY entity_id"
    ):
        sig_counts[row["entity_id"]] = row["c"]

    # ── Build geo-entities ──
    geo_entities = []
    for eid, (lat, lon, tier) in GEO_COORDS.items():
        row = db.execute(
            "SELECT id, name, entity_type, description FROM entities WHERE id = ?",
            (eid,),
        ).fetchone()
        if not row:
            continue

        desc = row["description"] or ""
        if len(desc) > 300:
            desc = desc[:297] + "..."

        conns = degree.get(eid, 0)
        cent = round(conns / (n_entities - 1), 4) if n_entities > 1 else 0

        geo_entities.append({
            "id": row["id"],
            "name": row["name"],
            "entity_type": row["entity_type"],
            "lat": lat,
            "lon": lon,
            "description": desc,
            "centrality": cent,
            "connection_count": conns,
            "signal_count": sig_counts.get(eid, 0),
            "evidence_tier": tier,
        })

    # Sort by centrality descending
    geo_entities.sort(key=lambda x: x["centrality"], reverse=True)

    # ── Build geo-signals ──
    # Map entity_id → coordinates from GEO_COORDS
    entity_coords = {eid: (lat, lon) for eid, (lat, lon, _) in GEO_COORDS.items()}

    sig_rows = db.execute(
        """SELECT s.entity_id, e.name, s.source_feed, s.headline, s.url, s.collected_at
           FROM signals s
           JOIN entities e ON s.entity_id = e.id
           WHERE s.relevance != 'dismissed'
           ORDER BY s.collected_at DESC
           LIMIT 200"""
    ).fetchall()

    geo_signals = []
    for s in sig_rows:
        coords = entity_coords.get(s["entity_id"])
        if not coords:
            continue
        geo_signals.append({
            "entity_id": s["entity_id"],
            "entity_name": s["name"],
            "lat": coords[0],
            "lon": coords[1],
            "source_feed": s["source_feed"],
            "headline": s["headline"],
            "url": s["url"],
            "collected_at": s["collected_at"],
        })

    # ── Write ──
    def write_json(filename, data):
        path = os.path.join(out_dir, filename)
        with open(path, "w") as f:
            json.dump(data, f, separators=(",", ":"))
        size = os.path.getsize(path)
        print(f"  {filename}: {size:,} bytes")

    write_json("geo-entities.json", geo_entities)
    write_json("geo-signals.json", geo_signals)

    print(f"  Geo: {len(geo_entities)} entities, {len(geo_signals)} signals with coordinates")


if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), "data", "intel.db")
    out_dir = os.path.join(os.path.dirname(__file__), "static", "data")
    os.makedirs(out_dir, exist_ok=True)

    db = sqlite3.connect(db_path)
    export_geo(db, out_dir)
    db.close()
