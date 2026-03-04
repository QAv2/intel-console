#!/usr/bin/env python3
"""Geocode intel-console entities and export geo-enriched JSON for WorldView globe."""

import json
import os
import sqlite3

# Hand-curated coordinate lookup — no API calls, no geocoding services.
# Keyed by entity NAME (not ID) so coordinates survive DB rebuilds.
# Evidence tiers: exact address = documented, org HQ = credible, person association = inference.
GEO_COORDS = {
    # ══════════════════════════════════════════════════════════════════════
    # FACILITIES — exact addresses / physical locations
    # ══════════════════════════════════════════════════════════════════════
    "9 East 71st Street":       (40.7719, -73.9639, "documented"),   # NYC
    "Little Saint James":       (18.2999, -64.8257, "documented"),   # USVI
    "Mar-a-Lago":               (26.6777, -80.0367, "documented"),   # Palm Beach FL
    "Zorro Ranch":              (34.8889, -105.8578, "documented"),  # Stanley NM
    "MCC New York":             (40.7149, -74.0010, "documented"),   # NYC federal jail
    "George Town Club":         (38.9076, -77.0603, "documented"),   # Washington DC
    "22 Avenue Foch":           (48.8717, 2.2888, "documented"),     # Paris
    "Dealey Plaza":             (32.7787, -96.8083, "documented"),   # Dallas TX
    "World Trade Center":       (40.7116, -74.0133, "documented"),   # NYC
    "The Pentagon":             (38.8711, -77.0562, "documented"),   # Arlington VA
    "Skinwalker Ranch":         (40.2588, -109.8880, "documented"),  # Ballard UT
    "Area 51":                  (37.2350, -115.8111, "documented"),  # Groom Lake NV
    "Wright-Patterson AFB":     (39.8261, -84.0483, "documented"),   # Dayton OH
    "Natanz Nuclear Facility":  (33.7250, 51.7270, "documented"),    # Iran
    "Fordow Enrichment Plant":  (34.8820, 51.2590, "documented"),    # Iran
    "Parchin Military Complex": (35.5200, 51.7700, "documented"),    # Iran
    "Konarak Naval Base":       (25.3500, 60.3800, "documented"),    # Iran
    "USS Abraham Lincoln":      (24.5000, 60.0000, "credible"),      # North Arabian Sea
    "USS Gerald R. Ford":       (25.5000, 57.0000, "credible"),      # Gulf of Oman
    "Dalton School":            (40.7822, -73.9540, "credible"),     # NYC

    # ══════════════════════════════════════════════════════════════════════
    # AGENCIES — headquarters locations
    # ══════════════════════════════════════════════════════════════════════
    "CIA":                               (38.9517, -77.1467, "documented"),  # Langley VA
    "NSA":                               (39.1086, -76.7714, "documented"),  # Fort Meade MD
    "FBI":                               (38.8977, -77.0248, "documented"),  # Hoover Building DC
    "DOJ":                               (38.8934, -77.0249, "documented"),  # Washington DC
    "DARPA":                             (38.8806, -77.1085, "documented"),  # Arlington VA
    "Mossad":                            (32.0490, 34.7625, "credible"),     # Tel Aviv
    "MI6":                               (51.4871, -0.1245, "documented"),   # Vauxhall Cross London
    "MI5":                               (51.4959, -0.1264, "documented"),   # Thames House London
    "DGSE":                              (48.8337, 2.3835, "credible"),      # Paris
    "BND":                               (52.5131, 13.3651, "credible"),     # Berlin
    "FSB":                               (55.7601, 37.6261, "credible"),     # Lubyanka Moscow
    "MSS":                               (39.9053, 116.3977, "credible"),    # Beijing
    "Saudi GID":                         (24.6949, 46.7241, "credible"),     # Riyadh
    "LAKAM":                             (32.0684, 34.7916, "credible"),     # Tel Aviv
    "Unit 8200":                         (31.2530, 34.7915, "credible"),     # Beersheba
    "Crown Prosecution Service":         (51.5017, -0.1270, "credible"),     # London
    "Metropolitan Police":               (51.4988, -0.1341, "credible"),     # London
    "Islamic Revolutionary Guard Corps": (35.6892, 51.3890, "credible"),     # Tehran
    "Quds Force":                        (35.6892, 51.3890, "credible"),     # Tehran
    "CENTCOM":                           (27.9506, -82.4572, "documented"),  # MacDill AFB Tampa FL
    "Atomic Energy Organization of Iran": (35.7300, 51.3400, "credible"),    # Tehran
    "Iranian Ministry of Intelligence":  (35.6997, 51.4230, "credible"),     # Tehran
    "DIA":                               (38.8425, -77.0147, "credible"),    # Anacostia-Bolling DC
    "FDA":                               (39.0346, -76.9781, "credible"),    # Silver Spring MD
    "CDC":                               (33.7990, -84.3264, "credible"),    # Atlanta GA
    "NIH":                               (38.9996, -77.1024, "credible"),    # Bethesda MD

    # ══════════════════════════════════════════════════════════════════════
    # ORGANIZATIONS — HQ / primary locations
    # ══════════════════════════════════════════════════════════════════════
    "JPMorgan Chase":            (40.7580, -73.9713, "credible"),    # NYC
    "Deutsche Bank":             (50.1100, 8.6703, "credible"),      # Frankfurt
    "Palantir Technologies":     (39.7539, -104.9994, "credible"),   # Denver CO
    "NSO Group":                 (32.1632, 34.7916, "credible"),     # Herzliya Israel
    "Apollo Global Management":  (40.7627, -73.9736, "credible"),    # NYC
    "In-Q-Tel":                  (38.8807, -77.1060, "credible"),    # Arlington VA
    "Hill & Knowlton":           (40.7527, -73.9818, "credible"),    # NYC
    "The Limited":               (40.0848, -82.8968, "credible"),    # Columbus OH
    "Victoria's Secret":         (40.0848, -82.8968, "credible"),    # Columbus OH
    "Carbyne":                   (32.0853, 34.7818, "credible"),     # Tel Aviv
    "Kissinger Associates":      (40.7587, -73.9706, "credible"),    # NYC
    "BCCI":                      (51.5127, -0.0891, "credible"),     # London (historical)
    "Carlyle Group":             (38.9044, -77.0398, "credible"),    # Washington DC
    "Heritage Foundation":       (38.9034, -77.0148, "credible"),    # Washington DC
    "Bechtel Corporation":       (38.9544, -77.3490, "credible"),    # Reston VA
    "Hollinger International":   (41.8823, -87.6254, "credible"),    # Chicago
    "Rose Law Firm":             (34.7465, -92.2896, "credible"),    # Little Rock AR
    "Systematics":               (34.7465, -92.2896, "credible"),    # Little Rock AR
    "Resorts International":     (39.3643, -74.4229, "credible"),    # Atlantic City NJ
    "Glencore":                  (47.1934, 8.5166, "credible"),      # Baar Switzerland
    "Kingdom Holding":           (24.7136, 46.6753, "credible"),     # Riyadh
    "MC2 Model Management":      (25.7750, -80.1868, "credible"),    # Miami
    "Elite Model Management":    (48.8726, 2.3124, "credible"),      # Paris
    "Bayrock Group":             (40.7614, -73.9776, "credible"),    # NYC
    "Bear Stearns":              (40.7551, -73.9744, "credible"),    # NYC
    "Towers Financial":          (40.7580, -73.9717, "credible"),    # NYC
    "Seagram":                   (40.7580, -73.9750, "credible"),    # NYC (historical)
    "First American Bank":       (38.9035, -77.0429, "credible"),    # Washington DC
    "Mega Group":                (40.7580, -73.9717, "credible"),    # NYC
    "Mirror Group Newspapers":   (51.5256, -0.0776, "credible"),     # London
    "Pergamon Press":            (51.7520, -1.2577, "credible"),     # Oxford
    "Saudi Binladin Group":      (21.5433, 39.1728, "credible"),     # Jeddah
    "Lippo Group":               (-6.1751, 106.8650, "credible"),    # Jakarta
    "CITIC Group":               (39.9192, 116.4614, "credible"),    # Beijing
    "Black Cube":                (32.0853, 34.7818, "credible"),     # Tel Aviv
    "TerraMar Project":          (40.7580, -73.9717, "credible"),    # NYC
    "Southern Air Transport":    (25.7959, -80.2870, "credible"),    # Miami
    "Safari Club":               (30.0444, 31.2357, "credible"),     # Cairo (historical)
    "New Paradigm Institute":    (38.9072, -77.0369, "credible"),    # Washington DC
    "Disclosure Project":        (38.0293, -78.4767, "credible"),    # Charlottesville VA
    "Americans for Safe Aerospace": (38.9007, -77.0302, "credible"), # Washington DC
    "CAPCOM":                    (51.5074, -0.1278, "credible"),     # London (CAPCOM Financial)
    "The Commission":            (40.7128, -74.0060, "credible"),    # NYC (Mafia)
    "Gambino Crime Family":      (40.7128, -74.0060, "credible"),    # NYC
    "Genovese Crime Family":     (40.7128, -74.0060, "credible"),    # NYC
    "Lucchese Crime Family":     (40.7128, -74.0060, "credible"),    # NYC
    "Philadelphia Crime Family": (39.9526, -75.1652, "credible"),    # Philadelphia
    "Murder Incorporated":       (40.6782, -73.9442, "credible"),    # Brooklyn NYC
    "Scarf Inc":                 (40.7128, -74.0060, "credible"),    # NYC (Gambino front)
    "S&A Concrete":              (40.7128, -74.0060, "credible"),    # NYC (Gambino front)
    "Birthright Israel":         (40.7580, -73.9717, "credible"),    # NYC HQ
    "Colony Capital":            (34.0549, -118.2578, "credible"),   # Los Angeles
    "Solntsevskaya Bratva":      (55.6445, 37.3728, "credible"),     # Solntsevo Moscow
    "Karin Models":              (48.8566, 2.3522, "credible"),      # Paris
    "Medellín Cartel":           (6.2518, -75.5636, "credible"),     # Medellín Colombia
    "SETCO Aviation":            (14.0818, -87.2068, "credible"),    # Honduras
    "School of the Americas":    (32.3584, -84.9489, "credible"),    # Fort Benning GA
    "Bohemian Club":             (38.5038, -122.9742, "credible"),   # Monte Rio CA (Grove)
    "Hezbollah":                 (33.8938, 35.5018, "credible"),     # Beirut Lebanon
    "Ansar Allah (Houthis)":     (15.3694, 44.1910, "credible"),     # Sana'a Yemen
    "Christic Institute":        (38.9072, -77.0369, "credible"),    # Washington DC
    "News Corp":                 (40.7580, -73.9717, "credible"),    # NYC
    "Fox Corporation":           (40.7580, -73.9717, "credible"),    # NYC
    "The Walt Disney Company":   (34.1564, -118.3255, "credible"),   # Burbank CA
    "Comcast Corporation":       (39.9537, -75.1697, "credible"),    # Philadelphia
    "Warner Bros. Discovery":    (40.7614, -73.9776, "credible"),    # NYC
    "Paramount Global":          (40.7614, -73.9776, "credible"),    # NYC
    "WikiLeaks":                 (51.5074, -0.1278, "credible"),     # London
    "Tavistock Institute":       (51.5235, -0.1280, "credible"),     # London
    "Atlantic Council":          (38.9072, -77.0369, "credible"),    # Washington DC
    "WHO":                       (46.2339, 6.1340, "credible"),      # Geneva
    "GAVI":                      (46.2339, 6.1340, "credible"),      # Geneva
    "EcoHealth Alliance":        (40.7580, -73.9717, "credible"),    # NYC
    "Purdue Pharma":             (41.0534, -73.5387, "credible"),    # Stamford CT
    "Pfizer":                    (40.7614, -73.9776, "credible"),    # NYC
    "Monsanto":                  (38.6270, -90.1994, "credible"),    # St. Louis MO
    "Warren Commission":         (38.8977, -77.0365, "credible"),    # White House DC
    "HSCA":                      (38.8899, -77.0091, "credible"),    # US Capitol
    "ARRB":                      (38.8977, -77.0365, "credible"),    # Washington DC
    "9/11 Commission":           (38.8977, -77.0365, "credible"),    # Washington DC
    "PNAC":                      (38.9072, -77.0369, "credible"),    # Washington DC
    "Al-Qaeda":                  (31.6133, 65.7101, "credible"),     # Kandahar Afghanistan
    "Lockheed Martin":           (38.9920, -77.0798, "credible"),    # Bethesda MD
    "Raytheon":                  (42.3765, -71.2356, "credible"),    # Waltham MA
    "Northrop Grumman":          (38.8829, -77.1717, "credible"),    # Falls Church VA
    "Boeing Defense":            (38.8816, -77.1024, "credible"),    # Arlington VA
    "General Dynamics":          (38.9586, -77.3570, "credible"),    # Reston VA
    "BAE Systems":               (51.2757, -0.7569, "credible"),     # Farnborough UK
    "L3Harris Technologies":     (28.0836, -80.6081, "credible"),    # Melbourne FL
    "Booz Allen Hamilton":       (38.9339, -77.1773, "credible"),    # McLean VA
    "Halliburton":               (29.7604, -95.3698, "credible"),    # Houston TX
    "Blackwater":                (36.5226, -76.1777, "credible"),    # Moyock NC
    "DynCorp":                   (32.7555, -97.3308, "credible"),    # Fort Worth TX
    "Bilderberg Group":          (52.1601, 4.4970, "credible"),      # Leiden Netherlands
    "Trilateral Commission":     (40.7580, -73.9717, "credible"),    # NYC
    "Council on Foreign Relations": (40.7688, -73.9675, "credible"), # NYC
    "Club of Rome":              (47.5006, 8.7245, "credible"),      # Winterthur Switzerland
    "Chatham House":             (51.5074, -0.1340, "credible"),     # London
    "Brookings Institution":     (38.9175, -77.0392, "credible"),    # Washington DC
    "RAND Corporation":          (34.0195, -118.4912, "credible"),   # Santa Monica CA
    "SRI International":         (37.4530, -122.1817, "credible"),   # Menlo Park CA
    "Monroe Institute":          (37.7201, -78.8756, "credible"),    # Faber VA
    "NIDS":                      (36.1699, -115.1398, "credible"),   # Las Vegas NV
    "Bigelow Aerospace":         (36.2468, -115.1827, "credible"),   # North Las Vegas NV
    "Battelle Memorial Institute": (39.9945, -82.9876, "credible"),  # Columbus OH
    "Sol Foundation":            (37.4275, -122.1697, "credible"),   # Stanford area CA
    "Standard Oil":              (40.7580, -73.9717, "credible"),    # NYC (historical)
    "Brown Brothers Harriman":   (40.7075, -74.0113, "credible"),    # Wall Street NYC
    "Federal Reserve System":    (38.8928, -77.0454, "credible"),    # Washington DC
    "Skull and Bones":           (41.3083, -72.9279, "credible"),    # New Haven CT
    "DuPont Family":             (39.7391, -75.5398, "credible"),    # Wilmington DE
    "World Economic Forum":      (46.2260, 6.1866, "credible"),      # Cologny Switzerland

    # ══════════════════════════════════════════════════════════════════════
    # FOUNDATIONS
    # ══════════════════════════════════════════════════════════════════════
    "Wexner Foundation":                       (40.0848, -82.8968, "credible"),  # Columbus OH
    "Bill & Melinda Gates Foundation":          (47.6240, -122.3474, "credible"),  # Seattle WA
    "Open Society Foundations":                (40.7614, -73.9776, "credible"),  # NYC
    "Rockefeller Foundation":                  (40.7580, -73.9717, "credible"),  # NYC
    "Carnegie Endowment for International Peace": (38.9072, -77.0369, "credible"),  # Washington DC
    "Ford Foundation":                         (40.7576, -73.9702, "credible"),  # NYC

    # ══════════════════════════════════════════════════════════════════════
    # LEGISLATION — US Capitol
    # ══════════════════════════════════════════════════════════════════════
    "UAP Disclosure Act":                         (38.8899, -77.0091, "credible"),  # US Capitol
    "Enhanced UAP Whistleblower Protection Act":  (38.8899, -77.0091, "credible"),  # US Capitol
    "Telecommunications Act of 1996":             (38.8899, -77.0091, "credible"),  # US Capitol
    "Smith-Mundt Modernization Act":              (38.8899, -77.0091, "credible"),  # US Capitol
    "USA PATRIOT Act":                            (38.8899, -77.0091, "credible"),  # US Capitol
    "Authorization for Use of Military Force (2001)": (38.8899, -77.0091, "credible"),  # US Capitol

    # ══════════════════════════════════════════════════════════════════════
    # PROGRAMS — mapped to operating agency HQ
    # ══════════════════════════════════════════════════════════════════════
    "PROMIS":                     (38.8934, -77.0249, "credible"),   # DOJ DC
    "Main Core":                  (39.1086, -76.7714, "credible"),   # NSA Fort Meade
    "Total Information Awareness": (38.8806, -77.1085, "credible"),  # DARPA Arlington
    "MKULTRA":                    (38.9517, -77.1467, "credible"),   # CIA Langley
    "COINTELPRO":                 (38.8977, -77.0248, "credible"),   # FBI DC
    "Iran-Contra":                (38.8977, -77.0365, "credible"),   # White House DC
    "Operation Midnight Climax":  (37.7749, -122.4194, "credible"),  # San Francisco
    "LifeLog":                    (38.8806, -77.1085, "credible"),   # DARPA Arlington
    "Operation Condor":           (-33.4489, -70.6693, "credible"),  # Santiago Chile
    "AATIP":                      (38.8711, -77.0562, "credible"),   # Pentagon
    "Operation Mockingbird":      (38.9517, -77.1467, "credible"),   # CIA Langley
    "PRISM":                      (39.1086, -76.7714, "credible"),   # NSA Fort Meade
    "Pentagon Military Analyst Program": (38.8711, -77.0562, "credible"),  # Pentagon
    "Tuskegee Syphilis Study":    (32.4308, -85.7077, "credible"),   # Tuskegee AL
    "Guatemala Syphilis Experiments": (14.6349, -90.5069, "credible"),  # Guatemala City
    "Gain-of-Function Research":  (38.9996, -77.1024, "credible"),   # NIH Bethesda
    "Operation Mongoose":         (25.7617, -80.1918, "credible"),   # CIA Miami Station
    "ZR/RIFLE":                   (38.9517, -77.1467, "credible"),   # CIA Langley
    "Operation 40":               (25.7617, -80.1918, "credible"),   # Miami
    "Operation Able Danger":      (38.8711, -77.0562, "credible"),   # Pentagon
    "Stellar Wind":               (39.1086, -76.7714, "credible"),   # NSA Fort Meade
    "Special Access Programs":    (38.8711, -77.0562, "credible"),   # Pentagon
    "F-35 Joint Strike Fighter":  (32.7627, -97.3281, "credible"),   # Lockheed Fort Worth TX
    "Project Stargate":           (39.1086, -76.7714, "credible"),   # Fort Meade
    "Gateway Process":            (39.1086, -76.7714, "credible"),   # Fort Meade
    "First Earth Battalion":      (35.1390, -79.0030, "credible"),   # Fort Bragg NC
    "AAWSAP":                     (38.8711, -77.0562, "credible"),   # Pentagon/DIA
    "Project Blue Book":          (39.8261, -84.0483, "credible"),   # Wright-Patterson AFB
    "UAP Task Force":             (38.8711, -77.0562, "credible"),   # Pentagon

    # ══════════════════════════════════════════════════════════════════════
    # EVENTS — location where they occurred
    # ══════════════════════════════════════════════════════════════════════
    "BCCI Shutdown (1991)":                  (49.6116, 6.1319, "credible"),     # Luxembourg
    "Epstein NPA (2007)":                    (26.7153, -80.0534, "credible"),   # West Palm Beach FL
    "Epstein Arrest (2019)":                 (40.8501, -74.0608, "credible"),   # Teterboro NJ
    "Epstein Death (2019)":                  (40.7149, -74.0010, "documented"), # MCC New York
    "Danny Casolaro Death (1991)":           (39.4562, -77.9639, "credible"),   # Martinsburg WV
    "Robert Maxwell Death (1991)":           (28.1235, -15.4363, "credible"),   # Canary Islands
    "Wexner House Oversight Deposition (2026)": (38.8899, -77.0091, "credible"),  # US Capitol
    "Commission Trial (1986)":               (40.7142, -74.0011, "credible"),   # Manhattan Federal Court
    "Castellano Assassination (1985)":       (40.7524, -73.9728, "credible"),   # Sparks Steak House NYC
    "Prince Andrew Civil Settlement (2022)": (40.7128, -74.0060, "credible"),   # NYC
    "Berger Archives Theft (2003)":          (38.8937, -77.0230, "credible"),   # National Archives DC
    "Jean-Luc Brunel Death (2022)":          (48.8341, 2.3374, "credible"),     # La Santé Prison Paris
    "Epstein Palm Beach Investigation (2005)": (26.7056, -80.0364, "credible"), # Palm Beach FL
    "Maxwell Trial (2021)":                  (40.6882, -73.9903, "credible"),   # Brooklyn Federal Court
    "BAE Al-Yamamah Deal":                   (51.5074, -0.1278, "credible"),    # London
    "Cox Report (1999)":                     (38.8899, -77.0091, "credible"),   # US Capitol
    "French Epstein Investigation":          (48.8566, 2.3522, "credible"),     # Paris
    "DFS Deutsche Bank Consent Order (2020)": (40.7128, -74.0060, "credible"),  # NYC (DFS)
    "Deutsche Bank Russian Mirror Trading":  (50.1100, 8.6703, "credible"),     # Frankfurt
    "Project 2025":                          (38.9034, -77.0148, "credible"),   # Heritage Foundation DC
    "Social Security Reform 1983":           (38.8977, -77.0365, "credible"),   # White House DC
    "Newsnight Interview":                   (51.5074, -0.1278, "credible"),    # BBC London
    "Operation Epic Fury":                   (35.6892, 51.3890, "credible"),    # Tehran theater
    "Operation Roaring Lion":                (33.8938, 35.5018, "credible"),    # Beirut theater
    "Operation Midnight Hammer":             (35.6892, 51.3890, "credible"),    # Iran theater
    "Strait of Hormuz Blockade":             (26.5667, 56.2500, "credible"),    # Strait of Hormuz
    "B-2 Spirit Strike Package":             (35.5200, 51.7700, "credible"),    # Parchin target
    "Church Committee":                      (38.8899, -77.0091, "credible"),   # US Capitol
    "Twitter Files":                         (37.7749, -122.4194, "credible"),  # San Francisco
    "JFK Assassination":                     (32.7787, -96.8083, "documented"), # Dallas TX
    "RFK Assassination":                     (34.0599, -118.2970, "documented"),# Ambassador Hotel LA
    "MLK Assassination":                     (35.1346, -90.0575, "documented"), # Lorraine Motel Memphis
    "September 11 Attacks":                  (40.7116, -74.0133, "documented"), # WTC NYC
    "WTC Building 7 Collapse":              (40.7133, -74.0131, "documented"), # WTC NYC
    "Eisenhower Farewell Address":           (38.8977, -77.0365, "credible"),   # White House DC
    "Pentagon Audit Failures":               (38.8711, -77.0562, "credible"),   # Pentagon
    "Gateway Process Report":                (39.1086, -76.7714, "credible"),   # Fort Meade
    "Stargate Declassification":             (38.9517, -77.1467, "credible"),   # CIA Langley
    "Wilson-Davis Memo":                     (36.1699, -115.1398, "credible"),  # Las Vegas
    "Roswell Incident":                      (33.3943, -104.5230, "documented"),# Roswell NM
    "Jekyll Island Meeting":                 (31.0557, -81.4270, "documented"), # Jekyll Island GA
    "Business Plot":                         (38.8899, -77.0091, "credible"),   # US Capitol
    "Pujo Committee":                        (38.8899, -77.0091, "credible"),   # US Capitol
    "Kerry Committee Investigation":         (38.8899, -77.0091, "credible"),   # US Capitol
    "Grusch Congressional Hearing":          (38.8899, -77.0091, "credible"),   # US Capitol
    "Davos Annual Meeting":                  (46.8027, 9.8360, "documented"),   # Davos Switzerland

    # ══════════════════════════════════════════════════════════════════════
    # PERSONS — primary associated location
    # ══════════════════════════════════════════════════════════════════════

    # ── Epstein Core Network ──
    "Jeffrey Epstein":           (40.7719, -73.9639, "inference"),   # NYC (9 E 71st St)
    "Ghislaine Maxwell":         (40.7677, -73.9650, "inference"),   # Upper East Side NYC
    "Robert Maxwell":            (51.5256, -0.0776, "inference"),    # London (Mirror Group)
    "Les Wexner":                (40.0848, -82.8968, "inference"),   # Columbus OH
    "Ehud Barak":                (32.0853, 34.7818, "inference"),    # Tel Aviv
    "Donald Barr":               (40.7822, -73.9540, "inference"),   # Dalton School NYC
    "Virginia Giuffre":          (26.7056, -80.0364, "inference"),   # West Palm Beach FL
    "Jean-Luc Brunel":           (48.8566, 2.3522, "inference"),     # Paris
    "Sarah Kellen":              (40.7128, -74.0060, "inference"),   # NYC
    "Nadia Marcinkova":          (40.7128, -74.0060, "inference"),   # NYC
    "Lesley Groff":              (40.7128, -74.0060, "inference"),   # NYC
    "Maria Farmer":              (40.7128, -74.0060, "inference"),   # NYC
    "Courtney Wild":             (26.7056, -80.0364, "inference"),   # Palm Beach FL
    "Nicole Junkermann":         (51.5074, -0.1278, "inference"),    # London
    "Eva Andersson-Dubin":       (40.7580, -73.9717, "inference"),   # NYC
    "Celina Midelfart":          (59.9139, 10.7522, "inference"),    # Oslo Norway

    # ── Intelligence & Government ──
    "William Barr":              (38.8934, -77.0249, "inference"),   # DOJ DC
    "William Casey":             (38.9517, -77.1467, "inference"),   # CIA Langley
    "Roy Cohn":                  (40.7625, -73.9710, "inference"),   # Midtown NYC
    "J. Edgar Hoover":           (38.8977, -77.0248, "inference"),   # FBI HQ DC
    "James Angleton":            (38.9517, -77.1467, "inference"),   # CIA Langley
    "Richard Helms":             (38.9517, -77.1467, "inference"),   # CIA Langley
    "Rafi Eitan":                (32.0684, 34.7916, "inference"),    # Tel Aviv (LAKAM)
    "Jonathan Pollard":          (38.8719, -77.0163, "inference"),   # Washington Navy Yard DC
    "Sandy Berger":              (38.9007, -77.0517, "inference"),   # White House DC
    "Henry Kissinger":           (40.7587, -73.9706, "inference"),   # NYC (Kissinger Assoc)
    "Prince Andrew":             (51.4194, -0.6052, "inference"),    # Royal Lodge Windsor
    "Alexander Acosta":          (25.7617, -80.1918, "inference"),   # Miami FL
    "Allen Dulles":              (38.9517, -77.1467, "inference"),   # CIA Langley
    "John McCone":               (38.9517, -77.1467, "inference"),   # CIA Langley
    "Sidney Gottlieb":           (38.9517, -77.1467, "inference"),   # CIA Langley (MKULTRA)
    "Frank Wisner":              (38.9517, -77.1467, "inference"),   # CIA (Mockingbird)
    "David Atlee Phillips":      (19.4326, -99.1332, "inference"),   # CIA Mexico City station
    "E. Howard Hunt":            (25.7617, -80.1918, "inference"),   # CIA Miami
    "Donald Ewen Cameron":       (45.5017, -73.5673, "inference"),   # Allan Memorial Montreal
    "George Tenet":              (38.9517, -77.1467, "inference"),   # CIA Langley

    # ── Politicians & Officials ──
    "Bill Clinton":              (34.7465, -92.2896, "inference"),   # Little Rock AR
    "Hillary Clinton":           (38.9007, -77.0369, "inference"),   # Washington DC
    "Donald Trump":              (26.6777, -80.0367, "inference"),   # Mar-a-Lago Palm Beach
    "Bill Richardson":           (35.6870, -105.9378, "inference"),  # Santa Fe NM
    "George Mitchell":           (38.9072, -77.0369, "inference"),   # Washington DC
    "Larry Summers":             (42.3736, -71.1097, "inference"),   # Harvard Cambridge MA
    "Rudy Giuliani":             (40.7128, -74.0060, "inference"),   # NYC
    "Ronald Reagan":             (38.8977, -77.0365, "inference"),   # White House DC
    "George H.W. Bush":          (29.7604, -95.3698, "inference"),   # Houston TX
    "George W. Bush":            (32.7767, -96.7970, "inference"),   # Dallas TX
    "Dick Cheney":               (38.9072, -77.0369, "inference"),   # Washington DC
    "Donald Rumsfeld":           (38.8711, -77.0562, "inference"),   # Pentagon
    "Colin Powell":              (38.8977, -77.0365, "inference"),   # State Dept DC
    "Caspar Weinberger":         (38.8711, -77.0562, "inference"),   # Pentagon
    "George Shultz":             (38.8977, -77.0365, "inference"),   # State Dept DC
    "Edwin Meese":               (38.8934, -77.0249, "inference"),   # DOJ DC
    "Condoleezza Rice":          (38.8977, -77.0365, "inference"),   # White House DC
    "Richard Clarke":            (38.8977, -77.0365, "inference"),   # White House NSC
    "Dwight D. Eisenhower":      (38.8977, -77.0365, "inference"),   # White House DC
    "Nelson Rockefeller":        (40.7580, -73.9717, "inference"),   # NYC
    "Robert F. Kennedy":         (38.9072, -77.0369, "inference"),   # DOJ/Senate DC
    "Bob Graham":                (30.4383, -84.2807, "inference"),   # Tallahassee FL
    "Chuck Schumer":             (38.8899, -77.0091, "inference"),   # US Capitol
    "Mike Rounds":               (38.8899, -77.0091, "inference"),   # US Capitol
    "Tim Burchett":              (38.8899, -77.0091, "inference"),   # US Capitol
    "Clarence Thomas":           (38.8906, -77.0044, "inference"),   # Supreme Court DC
    "Alan Greenspan":            (38.8928, -77.0454, "inference"),   # Federal Reserve DC
    "Jack Lang":                 (48.8566, 2.3522, "inference"),     # Paris

    # ── Financial & Business ──
    "Peter Thiel":               (37.4419, -122.1430, "inference"),  # Palo Alto CA
    "Alex Karp":                 (39.7539, -104.9994, "inference"),  # Denver CO (Palantir)
    "Leon Black":                (40.7627, -73.9736, "inference"),   # NYC (Apollo)
    "Charles Bronfman":          (40.7614, -73.9706, "inference"),   # NYC
    "Edgar Bronfman Sr.":        (40.7580, -73.9717, "inference"),   # NYC (Seagram)
    "Ronald Lauder":             (40.7688, -73.9625, "inference"),   # NYC
    "Michael Steinhardt":        (40.7580, -73.9717, "inference"),   # NYC
    "Glenn Dubin":               (40.7580, -73.9717, "inference"),   # NYC
    "Jes Staley":                (40.7580, -73.9713, "inference"),   # JPMorgan NYC
    "Steven Hoffenberg":         (40.7580, -73.9717, "inference"),   # NYC (Towers Financial)
    "Lynn Forester de Rothschild": (40.7614, -73.9776, "inference"), # NYC
    "Mort Zuckerman":            (40.7580, -73.9717, "inference"),   # NYC
    "Tom Barrack":               (34.0549, -118.2578, "inference"),  # Colony Capital LA
    "David Rockefeller":         (40.7580, -73.9717, "inference"),   # NYC
    "George Soros":              (40.7614, -73.9776, "inference"),   # NYC
    "John D. Rockefeller":       (40.7580, -73.9717, "inference"),   # NYC (historical)
    "J.P. Morgan":               (40.7075, -74.0113, "inference"),   # Wall Street NYC
    "Andrew Carnegie":           (40.7580, -73.9717, "inference"),   # NYC
    "Averell Harriman":          (40.7580, -73.9717, "inference"),   # NYC
    "Prescott Bush":             (41.0262, -73.6282, "inference"),   # Greenwich CT
    "Paul Warburg":              (40.7580, -73.9717, "inference"),   # NYC
    "Michael Bloomberg":         (40.7614, -73.9776, "inference"),   # NYC
    "Jeff Bezos":                (38.9072, -77.0369, "inference"),   # Washington DC (WaPo)
    "David McCormick":           (38.9072, -77.0369, "inference"),   # DC (Senator)
    "Joseph Coors Sr":           (39.7555, -105.2211, "inference"),  # Golden CO
    "Charles Koch":              (37.6872, -97.3301, "inference"),   # Wichita KS
    "Harlan Crow":               (32.7767, -96.7970, "inference"),   # Dallas TX
    "Steven Bechtel Sr":         (37.7749, -122.4194, "inference"),  # San Francisco
    "Brendan Bechtel":           (38.9544, -77.3490, "inference"),   # Reston VA (Bechtel)
    "Edwin Fuelner":             (38.9034, -77.0148, "inference"),   # Heritage Foundation DC
    "Norman Augustine":          (38.9920, -77.0798, "inference"),   # Bethesda MD (Lockheed)
    "Thomas Bowers":             (34.0259, -118.7798, "inference"),  # Malibu CA
    "Rosemary Vrablic":          (40.7128, -74.0060, "inference"),   # NYC (Deutsche Bank)
    "Tammy McFadden":            (30.3322, -81.6557, "inference"),   # Jacksonville FL
    "William Broeksmit":         (51.5074, -0.1278, "inference"),    # London (Deutsche Bank)
    "Val Broeksmit":             (34.0549, -118.2578, "inference"),  # Los Angeles
    "Philippa Sigl-Glöckner":    (52.5200, 13.4050, "inference"),    # Berlin

    # ── Organized Crime ──
    "Meyer Lansky":              (25.7907, -80.1300, "inference"),   # Miami Beach FL
    "Fat Tony Salerno":          (40.7580, -73.9717, "inference"),   # NYC
    "Paul Castellano":           (40.7524, -73.9728, "inference"),   # NYC
    "Felix Sater":               (40.7614, -73.9776, "inference"),   # NYC (Bayrock)
    "John Gotti":                (40.6575, -73.8437, "inference"),   # Howard Beach Queens
    "Angelo Bruno":              (39.9526, -75.1652, "inference"),   # Philadelphia
    "Nicky Scarfo":              (39.3643, -74.4229, "inference"),   # Atlantic City
    "John Stanfa":               (39.9526, -75.1652, "inference"),   # Philadelphia
    "Joey Merlino":              (39.9526, -75.1652, "inference"),   # Philadelphia
    "John-John Veasey":          (39.9526, -75.1652, "inference"),   # Philadelphia
    "Lucky Luciano":             (40.7128, -74.0060, "inference"),   # Manhattan NYC
    "Bugsy Siegel":              (36.1699, -115.1398, "inference"),  # Las Vegas
    "Sammy Gravano":             (40.6782, -73.9442, "inference"),   # Brooklyn NYC
    "Frankie Carbo":             (40.7128, -74.0060, "inference"),   # NYC
    "Blinky Palermo":            (39.9526, -75.1652, "inference"),   # Philadelphia
    "Kenneth Shapiro":           (39.3643, -74.4229, "inference"),   # Atlantic City
    "Salvatore Testa":           (39.9526, -75.1652, "inference"),   # Philadelphia
    "Robert LiButti":            (39.3643, -74.4229, "inference"),   # Atlantic City
    "Carlos Marcello":           (29.9511, -90.0715, "inference"),   # New Orleans
    "Santos Trafficante":        (27.9506, -82.4572, "inference"),   # Tampa FL
    "Sam Giancana":              (41.8781, -87.6298, "inference"),   # Chicago
    "Semion Mogilevich":         (55.7558, 37.6173, "inference"),    # Moscow

    # ── Intelligence-connected ──
    "Robert Keith Gray":         (38.9072, -77.0369, "inference"),   # Washington DC
    "Craig Spence":              (38.9072, -77.0369, "inference"),   # Washington DC
    "Edwin Wilson":              (38.9517, -77.1467, "inference"),   # CIA Langley
    "Frank Terpil":              (38.9072, -77.0369, "inference"),   # Washington DC
    "Kamal Adham":               (24.7136, 46.6753, "inference"),    # Riyadh (Saudi GID)
    "Agha Hasan Abedi":          (51.5074, -0.1278, "inference"),    # London (BCCI)
    "Clark Clifford":            (38.9072, -77.0369, "inference"),   # Washington DC
    "Jackson Stephens":          (34.7465, -92.2896, "inference"),   # Little Rock AR
    "Barry Seal":                (30.4515, -91.1871, "inference"),   # Baton Rouge LA
    "Bill Hamilton":             (38.9072, -77.0369, "inference"),   # DC (Inslaw)
    "Danny Casolaro":            (39.4562, -77.9639, "inference"),   # Martinsburg WV
    "John Poindexter":           (38.8977, -77.0365, "inference"),   # White House DC
    "Marc Rich":                 (47.1660, 8.5155, "inference"),     # Zug Switzerland
    "Adnan Khashoggi":           (36.5100, -4.8829, "inference"),    # Marbella Spain
    "Oliver North":              (38.9072, -77.0369, "inference"),   # Washington DC

    # ── Israel / Middle East ──
    "Ari Ben-Menashe":           (45.5017, -73.5673, "inference"),   # Montreal
    "Shabtai Shavit":            (32.0853, 34.7818, "inference"),    # Tel Aviv
    "Meir Dagan":                (32.0853, 34.7818, "inference"),    # Tel Aviv
    "Efraim Halevy":             (32.0853, 34.7818, "inference"),    # Tel Aviv
    "Prince Bandar bin Sultan":  (38.9072, -77.0558, "inference"),   # Saudi Embassy DC
    "Prince Turki al-Faisal":    (24.7136, 46.6753, "inference"),    # Riyadh
    "Mohammed bin Salman":       (24.7136, 46.6753, "inference"),    # Riyadh
    "Jamal Khashoggi":           (38.9072, -77.0369, "inference"),   # Washington DC (WaPo)
    "Al-Waleed bin Talal":       (24.7136, 46.6753, "inference"),    # Riyadh
    "Prince Mohammed bin Fahd":  (26.4367, 50.1033, "inference"),    # Dhahran Saudi
    "Wafic Said":                (51.5074, -0.1278, "inference"),    # London

    # ── UK figures ──
    "Peter Mandelson":           (51.5074, -0.1278, "inference"),    # London
    "Sarah Ferguson":            (51.5074, -0.1278, "inference"),    # London
    "Jimmy Savile":              (53.7997, -1.5492, "inference"),    # Leeds (BBC)
    "Mark Thompson":             (51.5074, -0.1278, "inference"),    # London (BBC)
    "Stuart Roffey":             (51.5074, -0.1278, "inference"),    # London
    "Evgeny Lebedev":            (51.5074, -0.1278, "inference"),    # London

    # ── Russia / Eastern Europe ──
    "Vladimir Putin":            (55.7520, 37.6175, "inference"),    # Moscow (Kremlin)
    "Dmitry Rybolovlev":         (43.7384, 7.4246, "inference"),     # Monaco

    # ── China / Asia ──
    "Johnny Chung":              (34.0549, -118.2578, "inference"),  # Los Angeles
    "John Huang":                (38.9072, -77.0369, "inference"),   # Washington DC
    "Charlie Trie":              (34.7465, -92.2896, "inference"),   # Little Rock AR
    "Bernard Schwartz":          (40.7580, -73.9717, "inference"),   # NYC (Loral Space)
    "Liu Chaoying":              (39.9053, 116.3977, "inference"),   # Beijing
    "Wang Jun":                  (39.9192, 116.4614, "inference"),   # Beijing (CITIC)
    "Desmond Shum":              (51.5074, -0.1278, "inference"),    # London (exile)

    # ── France / modeling ──
    "Gérald Marie":              (48.8566, 2.3522, "inference"),     # Paris (Elite Models)
    "John Casablancas":          (48.8566, 2.3522, "inference"),     # Paris (Elite Models)
    "Eileen Ford":               (40.7580, -73.9717, "inference"),   # NYC (Ford Models)
    "Claude Haddad":             (48.8566, 2.3522, "inference"),     # Paris
    "Manuel Noriega":            (8.9824, -79.5199, "inference"),    # Panama City

    # ── Latin America ──
    "Felix Rodriguez":           (25.7617, -80.1918, "inference"),   # Miami (CIA)
    "Augusto Pinochet":          (-33.4489, -70.6693, "inference"),  # Santiago Chile
    "Gary Webb":                 (38.5816, -121.4944, "inference"),  # Sacramento CA
    "Andres Pastrana":           (4.7110, -74.0721, "inference"),    # Bogotá Colombia

    # ── Iran figures ──
    "Ali Khamenei":              (35.7050, 51.4180, "inference"),    # Tehran
    "Ali Shamkhani":             (35.6997, 51.4230, "inference"),    # Tehran
    "Mohammad Pakpour":          (35.5200, 51.7700, "inference"),    # Parchin
    "Aziz Nasirzadeh":           (35.7219, 51.3897, "inference"),    # Tehran
    "Abdul Rahim Mousavi":       (35.7050, 51.4180, "inference"),    # Tehran
    "Masoud Pezeshkian":         (35.6892, 51.3890, "inference"),    # Tehran

    # ── Hollywood / Entertainment ──
    "Harvey Weinstein":          (40.7195, -74.0089, "inference"),   # Tribeca NYC
    "Kevin Spacey":              (40.7128, -74.0060, "inference"),   # NYC
    "Woody Allen":               (40.7753, -73.9618, "inference"),   # Upper East Side NYC
    "Naomi Campbell":            (51.5074, -0.1278, "inference"),    # London
    "Ari Emanuel":               (34.0736, -118.4004, "inference"),  # Beverly Hills CA (WME)
    "Les Moonves":               (40.7614, -73.9776, "inference"),   # NYC (CBS)
    "Steve Bing":                (34.0549, -118.2578, "inference"),  # Los Angeles
    "Alan Dershowitz":           (42.3736, -71.1097, "inference"),   # Harvard Cambridge MA

    # ── Media / Journalists ──
    "Rupert Murdoch":            (40.7580, -73.9717, "inference"),   # NYC (News Corp)
    "Edward Bernays":            (40.7580, -73.9717, "inference"),   # NYC (historical)
    "Carl Bernstein":            (38.9072, -77.0369, "inference"),   # Washington DC
    "Anderson Cooper":           (40.7614, -73.9776, "inference"),   # NYC (CNN)
    "Julian Assange":            (51.5074, -0.1278, "inference"),    # London
    "Edward Snowden":            (55.7558, 37.6173, "inference"),    # Moscow (exile)
    "Chelsea Manning":           (39.1086, -76.7714, "inference"),   # Fort Meade area
    "William Binney":            (39.1086, -76.7714, "inference"),   # Fort Meade area (NSA)
    "Dorothy Kilgallen":         (40.7580, -73.9717, "inference"),   # NYC

    # ── Health / Science ──
    "Anthony Fauci":             (38.9996, -77.1024, "inference"),   # NIH Bethesda
    "Bill Gates":                (47.6062, -122.3321, "inference"),  # Seattle WA
    "Peter Daszak":              (40.7580, -73.9717, "inference"),   # NYC (EcoHealth)
    "Ralph Baric":               (35.9132, -79.0558, "inference"),   # UNC Chapel Hill NC
    "Arthur Sackler":            (40.7580, -73.9717, "inference"),   # NYC
    "Royal Raymond Rife":        (32.7157, -117.1611, "inference"),  # San Diego CA

    # ── JFK / Assassinations ──
    "Lee Harvey Oswald":         (32.7787, -96.8083, "inference"),   # Dallas TX
    "Jack Ruby":                 (32.7787, -96.8083, "inference"),   # Dallas TX
    "Clay Shaw":                 (29.9511, -90.0715, "inference"),   # New Orleans
    "David Ferrie":              (29.9511, -90.0715, "inference"),   # New Orleans
    "Guy Banister":              (29.9511, -90.0715, "inference"),   # New Orleans
    "Jim Garrison":              (29.9511, -90.0715, "inference"),   # New Orleans (DA)
    "George de Mohrenschildt":   (32.7767, -96.7970, "inference"),   # Dallas TX
    "Sirhan Sirhan":             (34.0599, -118.2970, "inference"),  # Los Angeles
    "Martin Luther King Jr.":    (33.7490, -84.3880, "inference"),   # Atlanta GA
    "James Earl Ray":            (35.1495, -90.0490, "inference"),   # Memphis TN

    # ── 9/11 figures ──
    "Osama bin Laden":           (34.1688, 73.2215, "inference"),    # Abbottabad Pakistan
    "Khalid Sheikh Mohammed":    (19.9025, -75.0966, "inference"),   # Guantánamo
    "Mohamed Atta":              (53.5511, 9.9937, "inference"),     # Hamburg Germany
    "Nawaf al-Hazmi":            (32.7157, -117.1611, "inference"),  # San Diego CA
    "Khalid al-Mihdhar":         (32.7157, -117.1611, "inference"),  # San Diego CA
    "Philip Zelikow":            (38.9072, -77.0369, "inference"),   # Washington DC
    "Sibel Edmonds":             (38.9072, -77.0369, "inference"),   # Washington DC

    # ── MIC ──
    "Erik Prince":               (36.5226, -76.1777, "inference"),   # Moyock NC (Blackwater)

    # ── Supranational / Power Structures ──
    "Zbigniew Brzezinski":       (38.9072, -77.0369, "inference"),   # Washington DC
    "Klaus Schwab":              (46.2260, 6.1866, "inference"),     # WEF Cologny
    "Børge Brende":              (46.2260, 6.1866, "inference"),     # WEF Cologny
    "Alois Zwinggi":             (46.2260, 6.1866, "inference"),     # WEF Cologny
    "Smedley Butler":            (39.9526, -75.1652, "inference"),   # Philadelphia

    # ── UAP Disclosure ──
    "Daniel Sheehan":            (38.0293, -78.4767, "inference"),   # Charlottesville VA
    "John Mack":                 (42.3736, -71.1097, "inference"),   # Harvard Cambridge MA
    "Steven Greer":              (38.0293, -78.4767, "inference"),   # Charlottesville VA
    "Luis Elizondo":             (38.9072, -77.0369, "inference"),   # Washington DC
    "David Grusch":              (38.9072, -77.0369, "inference"),   # Washington DC
    "David Fravor":              (38.7849, -121.2358, "inference"),   # Lemoore NAS area CA
    "Ryan Graves":               (38.9007, -77.0302, "inference"),   # DC (ASA)

    # ── Consciousness / Remote Viewing ──
    "Ingo Swann":                (40.7580, -73.9717, "inference"),   # NYC
    "Hal Puthoff":               (37.4530, -122.1817, "inference"),  # Menlo Park CA (SRI)
    "Russell Targ":              (37.4530, -122.1817, "inference"),  # Menlo Park CA (SRI)
    "Pat Price":                 (37.4530, -122.1817, "inference"),  # Menlo Park CA (SRI)
    "Joseph McMoneagle":         (39.1086, -76.7714, "inference"),   # Fort Meade MD
    "Edwin May":                 (37.4530, -122.1817, "inference"),  # Menlo Park CA (SRI)
    "Dale Graff":                (39.8261, -84.0483, "inference"),   # Wright-Patterson AFB
    "Albert Stubblebine":        (39.1086, -76.7714, "inference"),   # Fort Meade (INSCOM)
    "Jim Channon":               (35.1390, -79.0030, "inference"),   # Fort Bragg NC
    "Robert Monroe":             (37.7201, -78.8756, "inference"),   # Faber VA (Monroe Institute)

    # ── UAP Programs ──
    "Robert Bigelow":            (36.2468, -115.1827, "inference"),  # Las Vegas (Bigelow Aero)
    "Eric Davis":                (36.1699, -115.1398, "inference"),  # Las Vegas (NIDS)
    "Colm Kelleher":             (36.1699, -115.1398, "inference"),  # Las Vegas (NIDS)
    "Jacques Vallée":            (37.7749, -122.4194, "inference"),  # San Francisco
    "Kit Green":                 (42.3314, -83.0458, "inference"),   # Detroit MI (Wayne State)
    "James Lacatski":            (38.8425, -77.0147, "inference"),   # DIA DC
    "George Knapp":              (36.1699, -115.1398, "inference"),  # Las Vegas

    # ── Dynasties ──
    # (Rockefellers, Morgan, etc. already covered in Financial section above)

    # ══════════════════════════════════════════════════════════════════════
    # RITUAL & OCCULT
    # ══════════════════════════════════════════════════════════════════════
    "Jack Parsons":                  (34.1478, -118.1445, "inference"),   # Pasadena CA (JPL)
    "Aleister Crowley":              (51.5074, -0.1278, "inference"),     # London (born/lived)
    "Michael Aquino":                (37.7749, -122.4194, "inference"),   # San Francisco (Presidio)
    "L. Ron Hubbard":                (34.0522, -118.2437, "inference"),   # Los Angeles
    "Anton LaVey":                   (37.7749, -122.4194, "inference"),   # San Francisco
    "Larry King":                    (41.2565, -95.9345, "inference"),    # Omaha NE (Franklin)
    "Paul Bonacci":                  (41.2565, -95.9345, "inference"),    # Omaha NE
    "John DeCamp":                   (40.8136, -96.7026, "inference"),    # Lincoln NE
    "Ordo Templi Orientis":          (51.5074, -0.1278, "credible"),     # London (historic HQ)
    "Temple of Set":                 (37.7749, -122.4194, "credible"),    # San Francisco
    "Church of Scientology":         (34.0979, -118.3106, "credible"),    # Los Angeles (HQ)
    "Thule Society":                 (48.1351, 11.5820, "credible"),      # Munich Germany
    "Process Church of the Final Judgment": (51.5074, -0.1278, "credible"), # London (founded)
    "The Finders":                   (38.9072, -77.0369, "credible"),     # Washington DC
    "Presidio Abuse Case":           (37.7985, -122.4580, "documented"),  # Presidio SF
    "Franklin Cover-Up":             (41.2565, -95.9345, "credible"),     # Omaha NE
    "Operation Snow White":          (34.0979, -118.3106, "credible"),    # Los Angeles (Scientology HQ)
    "Babalon Working":               (34.1478, -118.1445, "credible"),    # Pasadena CA

    # ══════════════════════════════════════════════════════════════════════
    # FALSE FLAGS & COVERT OPS
    # ══════════════════════════════════════════════════════════════════════
    "Operation Northwoods":          (38.8711, -77.0562, "documented"),   # Pentagon (JCS)
    "Gulf of Tonkin Incident":       (19.8000, 106.5000, "documented"),   # Gulf of Tonkin, Vietnam
    "Gulf of Tonkin Resolution":     (38.8899, -77.0091, "documented"),   # US Capitol
    "Operation Gladio":              (41.9028, 12.4964, "credible"),      # Rome (primary theater)
    "USS Liberty Attack":            (31.4000, 33.3000, "documented"),    # Eastern Mediterranean
    "Operation Ajax":                (35.6892, 51.3890, "documented"),    # Tehran Iran
    "Operation PBSuccess":           (14.6349, -90.5069, "documented"),   # Guatemala City
    "Operation Paperclip":           (38.9072, -77.0369, "credible"),     # Washington DC (coordinated)
    "Strategy of Tension":           (41.9028, 12.4964, "credible"),      # Italy (primary theater)
    "Lyman Lemnitzer":               (38.8711, -77.0562, "inference"),    # Pentagon
    "Mohammad Mossadegh":            (35.6892, 51.3890, "documented"),    # Tehran Iran
    "Jacobo Árbenz":                 (14.6349, -90.5069, "documented"),   # Guatemala City
    "Daniele Ganser":                (47.5596, 7.5886, "inference"),      # Basel Switzerland
    "Fred Hampton":                  (41.8781, -87.6298, "documented"),   # Chicago IL
    "NATO":                          (50.8773, 4.3209, "documented"),     # Brussels Belgium
    "Joint Chiefs of Staff":         (38.8711, -77.0562, "documented"),   # Pentagon
    "United Fruit Company":          (42.3601, -71.0589, "credible"),     # Boston MA (HQ)
    "Wernher von Braun":             (34.7304, -86.5861, "inference"),    # Huntsville AL (NASA)
    "Admiral Thomas Moorer":         (38.8711, -77.0562, "inference"),    # Pentagon

    # ══════════════════════════════════════════════════════════════════════
    # FINANCIAL SYSTEM DEEP
    # ══════════════════════════════════════════════════════════════════════
    "Bank for International Settlements": (47.5530, 7.5920, "documented"), # Basel Switzerland
    "BlackRock":                     (40.7527, -73.9772, "documented"),   # NYC (HQ)
    "Vanguard":                      (40.0493, -75.5131, "documented"),   # Malvern PA
    "State Street Corporation":      (42.3601, -71.0589, "documented"),   # Boston MA
    "International Monetary Fund":   (38.8991, -77.0432, "documented"),   # Washington DC
    "World Bank":                    (38.8993, -77.0422, "documented"),   # Washington DC
    "SWIFT":                         (50.6803, 4.3642, "documented"),     # La Hulpe Belgium
    "Goldman Sachs":                 (40.7143, -74.0144, "documented"),   # NYC (HQ)
    "Citigroup":                     (40.7205, -74.0112, "documented"),   # NYC (HQ)
    "Plunge Protection Team":        (38.8977, -77.0365, "credible"),     # Treasury DC
    "Exchange Stabilization Fund":   (38.8977, -77.0365, "credible"),     # Treasury DC
    "Larry Fink":                    (40.7527, -73.9772, "inference"),    # NYC (BlackRock)
    "Timothy Geithner":              (40.7143, -74.0144, "inference"),    # NYC (NY Fed)
    "Hank Paulson":                  (40.7143, -74.0144, "inference"),    # NYC (Goldman)
    "Robert Rubin":                  (40.7143, -74.0144, "inference"),    # NYC (Goldman→Treasury)
    "Ben Bernanke":                  (38.8928, -77.0450, "inference"),    # Federal Reserve DC
    "Glass-Steagall Repeal":         (38.8899, -77.0091, "documented"),   # US Capitol
    "2008 Financial Crisis":         (40.7068, -74.0090, "credible"),     # Wall Street NYC
    "LIBOR Scandal":                 (51.5130, -0.0890, "documented"),    # City of London
    "Petrodollar System":            (24.7136, 46.6753, "credible"),      # Riyadh Saudi Arabia

    # ══════════════════════════════════════════════════════════════════════
    # TECH SURVEILLANCE
    # ══════════════════════════════════════════════════════════════════════
    "Five Eyes":                     (38.9517, -77.1467, "credible"),     # CIA Langley (coordination hub)
    "GCHQ":                          (51.8986, -2.1245, "documented"),    # Cheltenham UK
    "XKeyscore":                     (39.1086, -76.7714, "credible"),     # NSA Fort Meade
    "ECHELON":                       (-35.3225, 148.9988, "credible"),    # Pine Gap Australia
    "Room 641A":                     (37.7876, -122.3999, "documented"),  # 611 Folsom St SF
    "Vault 7":                       (38.9517, -77.1467, "credible"),     # CIA Langley
    "MYSTIC":                        (39.1086, -76.7714, "credible"),     # NSA Fort Meade
    "Tempora":                       (50.8280, -0.1375, "credible"),      # Bude Cornwall UK (cable tap)
    "Carnivore":                     (38.8977, -77.0248, "credible"),     # FBI DC
    "ThinThread":                    (39.1086, -76.7714, "credible"),     # NSA Fort Meade
    "Thomas Drake":                  (39.1086, -76.7714, "inference"),    # NSA Fort Meade
    "Mark Klein":                    (37.7876, -122.3999, "inference"),   # San Francisco (AT&T)
    "Keith Alexander":               (39.1086, -76.7714, "inference"),    # NSA Fort Meade
    "USA FREEDOM Act":               (38.8899, -77.0091, "documented"),   # US Capitol
    "FISA Amendments Act":           (38.8899, -77.0091, "documented"),   # US Capitol
    "Jewel v. NSA":                  (37.7876, -122.3999, "documented"),  # SF Federal Court
    "ACLU v. Clapper":               (40.7143, -74.0144, "documented"),   # NYC Federal Court

    # ══════════════════════════════════════════════════════════════════════
    # COSMOLOGY & ORIGINS
    # ══════════════════════════════════════════════════════════════════════
    "Gobekli Tepe":                  (37.2233, 38.9225, "documented"),    # Sanliurfa Turkey
    "Puma Punku":                    (-16.5617, -68.6800, "documented"),   # Tiwanaku Bolivia
    "Great Sphinx":                  (29.9753, 31.1376, "documented"),    # Giza Egypt
    "Younger Dryas Impact Hypothesis": (42.3601, -71.0589, "credible"),   # Boston (research center)
    "Gunung Padang":                 (-6.9943, 107.0567, "documented"),   # West Java Indonesia
    "Baalbek":                       (34.0067, 36.2039, "documented"),    # Baalbek Lebanon
    "Graham Hancock":                (51.7520, -1.2577, "inference"),     # Bath UK
    "Randall Carlson":               (33.7490, -84.3880, "inference"),    # Atlanta GA
    "Robert Schoch":                 (42.3505, -71.1054, "inference"),    # Boston (Boston U)
    "John Anthony West":             (40.7128, -74.0060, "inference"),    # New York
    "Klaus Schmidt":                 (48.1327, 11.5760, "inference"),     # Munich (DAI)
    "Danny Hilman Natawidjaja":      (-6.2088, 106.8456, "inference"),    # Jakarta Indonesia
    "Robert Bauval":                 (36.7670, 3.0477, "inference"),      # Alexandria Egypt origin
    "Michael Cremo":                 (26.1420, -81.7948, "inference"),    # Florida
    "Smithsonian Institution":       (38.8881, -77.0260, "documented"),   # Washington DC
    "Geological Society of America": (39.7576, -105.2206, "documented"),  # Boulder CO

    # ══════════════════════════════════════════════════════════════════════
    # EXPANSION: FREEMASONRY (19 entities)
    # ══════════════════════════════════════════════════════════════════════
    "Albert Pike":                       (38.8977, -77.0365, "documented"),   # Washington DC (lived/buried there)
    "Manly P. Hall":                     (34.0522, -118.2437, "inference"),   # Los Angeles CA
    "Licio Gelli":                       (43.3188, 11.3308, "inference"),     # Arezzo Italy
    "Roberto Calvi":                     (51.5074, -0.0784, "documented"),    # Blackfriars Bridge London
    "P.D. Houston":                      (38.8977, -77.0365, "inference"),    # Washington DC
    "Albert Mackey":                     (32.7765, -79.9311, "inference"),    # Charleston SC
    "William Donovan":                   (38.8977, -77.0365, "documented"),   # Washington DC (OSS HQ)
    "Scottish Rite Southern Jurisdiction": (38.9027, -77.0365, "documented"), # House of the Temple DC
    "York Rite":                         (38.8977, -77.0365, "inference"),    # Washington DC
    "Propaganda Due":                    (41.9028, 12.4964, "documented"),    # Rome Italy
    "United Grand Lodge of England":     (51.5167, -0.1321, "documented"),    # Great Queen St London
    "Grand Orient de France":            (48.8649, 2.3391, "documented"),     # Rue Cadet Paris
    "Shriners":                          (33.5207, -86.8025, "inference"),    # Tampa FL HQ
    "Sovereign Military Order of Malta": (41.9053, 12.4793, "documented"),    # Via Condotti Rome
    "Knights Templar":                   (31.7788, 35.2346, "documented"),    # Jerusalem (Temple Mount)
    "P2 Lodge Scandal":                  (41.9028, 12.4964, "documented"),    # Rome Italy
    "Calvi Murder":                      (51.5081, -0.1038, "documented"),    # Blackfriars Bridge London
    "Banco Ambrosiano Collapse":         (45.4642, 9.1900, "documented"),     # Milan Italy
    "House of the Temple":               (38.9064, -77.0313, "documented"),   # 1733 16th St NW DC

    # ══════════════════════════════════════════════════════════════════════
    # EXPANSION: PEDOPHILE NETWORKS (19 entities)
    # ══════════════════════════════════════════════════════════════════════
    "Marc Dutroux":                      (50.4669, 3.8817, "documented"),     # Charleroi Belgium
    "Keith Raniere":                     (42.6526, -73.7562, "documented"),   # Albany NY (NXIVM HQ)
    "Peter Scully":                      (8.4542, 124.6319, "documented"),    # Cagayan de Oro Philippines
    "Cardinal Bernard Law":              (42.3601, -71.0589, "documented"),   # Boston MA
    "Leon Brittan":                      (51.5074, -0.1278, "documented"),    # London
    "Cyril Smith":                       (53.5956, -2.1575, "documented"),    # Rochdale UK
    "Peter Hayman":                      (51.5074, -0.1278, "inference"),     # London
    "Peter Ball":                        (50.8688, -0.0832, "documented"),    # Lewes UK
    "NXIVM":                             (42.6526, -73.7562, "documented"),   # Albany NY
    "Dutroux Network":                   (50.4669, 3.8817, "documented"),     # Belgium
    "Dutroux Affair":                    (50.4669, 3.8817, "documented"),     # Belgium
    "Boston Globe Spotlight Team":       (42.3601, -71.0589, "documented"),   # Boston MA
    "Westminster Dossier Disappearance": (51.4995, -0.1248, "documented"),    # Westminster London
    "NXIVM Trial":                       (40.6815, -73.9761, "documented"),   # Brooklyn Federal Court
    "Spotlight Investigation":           (42.3601, -71.0589, "documented"),   # Boston MA
    "Australian Royal Commission":       (-35.2820, 149.1287, "documented"),  # Canberra Australia
    "Independent Inquiry into Child Sexual Abuse": (51.5074, -0.1278, "documented"), # London
    "Operation Yewtree":                 (51.5074, -0.1278, "documented"),    # London (Met Police)
    "Operation Midland":                 (51.5074, -0.1278, "documented"),    # London (Met Police)

    # ══════════════════════════════════════════════════════════════════════
    # EXPANSION: DRUG TRAFFICKING (19 entities)
    # ══════════════════════════════════════════════════════════════════════
    "Freeway Rick Ross":                 (33.9425, -118.2551, "documented"),  # South Central LA
    "Michael Levine":                    (40.7128, -74.0060, "inference"),    # New York
    "Cele Castillo":                     (29.4241, -98.4936, "inference"),    # San Antonio TX
    "Bo Gritz":                          (43.6150, -116.2023, "inference"),   # Boise ID
    "Khun Sa":                           (20.0000, 99.0000, "credible"),      # Shan State Myanmar
    "Oscar Danilo Blandon":              (34.0195, -118.4912, "inference"),   # Los Angeles CA
    "Norwin Meneses":                    (12.1150, -86.2362, "inference"),    # Managua Nicaragua
    "Enrique Camarena":                  (20.6597, -103.3496, "documented"),  # Guadalajara Mexico (killed)
    "Air America":                       (17.9667, 102.6000, "documented"),   # Vientiane Laos (base)
    "Nugan Hand Bank":                   (-33.8688, 151.2093, "documented"), # Sydney Australia
    "Cali Cartel":                       (3.4516, -76.5320, "documented"),    # Cali Colombia
    "Los Zetas":                         (25.4260, -100.0029, "credible"),    # Monterrey Mexico
    "DEA":                               (38.8859, -77.0243, "documented"),   # Arlington VA HQ
    "ATF":                               (38.8964, -77.0299, "documented"),   # Washington DC
    "Dark Alliance":                     (37.3382, -121.8863, "documented"),  # San Jose Mercury News
    "Operation Fast and Furious":        (32.2226, -110.9747, "documented"),  # Tucson AZ (ATF office)
    "Golden Triangle Drug Trade":        (20.5000, 100.0000, "documented"),   # Myanmar/Laos/Thailand
    "Mena Airport Operations":           (34.5456, -94.2024, "documented"),   # Mena AR
    "Mena Airport":                      (34.5456, -94.2024, "documented"),   # Mena AR

    # ══════════════════════════════════════════════════════════════════════
    # EXPANSION: ELECTION INTERFERENCE (19 entities)
    # ══════════════════════════════════════════════════════════════════════
    "Alexander Nix":                     (51.5074, -0.1278, "inference"),     # London (CA HQ)
    "Christopher Wylie":                 (51.5074, -0.1278, "inference"),     # London
    "Clint Curtis":                      (28.0395, -81.9498, "inference"),    # Florida
    "Bev Harris":                        (47.6062, -122.3321, "inference"),   # Seattle WA
    "Robert Mercer":                     (40.9176, -72.6621, "inference"),    # Head of the Harbor NY
    "John Bolton":                       (38.8977, -77.0365, "inference"),    # Washington DC
    "Cambridge Analytica":               (51.5156, -0.1419, "documented"),    # New Oxford St London
    "SCL Group":                         (51.5074, -0.1278, "documented"),    # London
    "Dominion Voting Systems":           (43.6510, -79.3470, "documented"),   # Toronto Canada HQ
    "ES&S":                              (41.2565, -95.9345, "documented"),   # Omaha NE
    "Internet Research Agency":          (59.9311, 30.3609, "documented"),    # St Petersburg Russia
    "Black Box Voting":                  (47.6062, -122.3321, "credible"),    # Seattle WA
    "Brooks Brothers Riot (2000)":       (25.7617, -80.1918, "documented"),   # Miami-Dade FL
    "Bush v. Gore (2000)":               (38.8907, -77.0043, "documented"),   # Supreme Court DC
    "Citizens United v. FEC (2010)":     (38.8907, -77.0043, "documented"),   # Supreme Court DC
    "2016 Russian Interference":         (38.8977, -77.0365, "documented"),   # Washington DC
    "Halderman Report (2021)":           (33.7490, -84.3880, "documented"),   # Atlanta GA (Curling v. Raffensperger)
    "Help America Vote Act":             (38.8977, -77.0365, "documented"),   # Washington DC
    "Project Alamo":                     (29.4241, -98.4936, "documented"),   # San Antonio TX

    # ══════════════════════════════════════════════════════════════════════
    # EXPANSION: ENERGY SUPPRESSION (19 entities)
    # ══════════════════════════════════════════════════════════════════════
    "Nikola Tesla":                      (40.7549, -73.9840, "documented"),   # New Yorker Hotel (died)
    "Thomas Townsend Brown":             (38.8977, -77.0365, "inference"),    # Washington DC area
    "Stanley Meyer":                     (39.9612, -82.9988, "documented"),   # Columbus OH (died)
    "Martin Fleischmann":                (50.9367, -1.3965, "documented"),    # Southampton UK
    "Stanley Pons":                      (40.7608, -111.8910, "documented"),  # University of Utah
    "Eugene Mallove":                    (41.7658, -72.6734, "documented"),   # Connecticut
    "Thomas Valone":                     (38.8977, -77.0365, "documented"),   # Washington DC (PTO)
    "John Hutchison":                    (49.2827, -123.1207, "credible"),    # Vancouver BC
    "General Electric":                  (42.3142, -73.2551, "documented"),   # Schenectady NY (HQ)
    "Westinghouse":                      (40.4406, -79.9959, "documented"),   # Pittsburgh PA
    "American Medical Association":      (41.8781, -87.6298, "documented"),   # Chicago IL (HQ)
    "Federation of American Scientists": (38.8977, -77.0365, "documented"),   # Washington DC
    "DOE":                               (38.8741, -77.0286, "documented"),   # Washington DC
    "Invention Secrecy Act of 1951":     (38.8977, -77.0365, "documented"),   # Washington DC
    "Patent Secrecy Orders":             (38.8811, -77.0239, "documented"),   # USPTO Alexandria VA
    "Electrogravitics Research Program": (38.8977, -77.0365, "inference"),    # classified (DC area)
    "Pons-Fleischmann Cold Fusion Announcement": (40.7608, -111.8910, "documented"), # U of Utah
    "Stan Meyer Water Fuel Cell":        (39.9612, -82.9988, "documented"),   # Columbus OH
    "Wardenclyffe Tower":                (40.9464, -72.8960, "documented"),   # Shoreham NY

    # ══════════════════════════════════════════════════════════════════════
    # CONSCIOUSNESS DEEP — expansion_consciousness_deep.py
    # ══════════════════════════════════════════════════════════════════════
    "Dean Radin":                        (38.2324, -122.6367, "credible"),    # Petaluma CA (IONS)
    "Jessica Utts":                      (33.6405, -117.8443, "credible"),    # UC Irvine CA
    "Jim Marrs":                         (32.7555, -97.3308, "credible"),     # Fort Worth TX
    "Paul Smith":                        (36.7783, -119.4179, "credible"),    # California (IRVA)
    "Lyn Buchanan":                      (34.7465, -92.2896, "credible"),     # Arkansas
    "David Morehouse":                   (38.8816, -77.0910, "credible"),     # Washington DC area
    "Angela Dellafiora Ford":            (38.8425, -77.0147, "credible"),     # DIA Anacostia-Bolling DC
    "Ed Dames":                          (38.8816, -77.0910, "credible"),     # Washington DC area
    "Andrija Puharich":                  (39.3218, -74.5901, "credible"),     # New Jersey
    "Edgar Mitchell":                    (28.5729, -80.6490, "documented"),   # Cape Canaveral FL
    "IONS":                              (38.2324, -122.6367, "documented"),  # Petaluma CA
    "SAIC":                              (32.8328, -117.1228, "credible"),    # San Diego CA
    "PSI Tech":                          (38.8816, -77.0910, "credible"),     # Washington DC area
    "Farsight Institute":               (33.7905, -84.3267, "credible"),     # Atlanta GA (Emory area)
    "Project Scanate":                   (37.4560, -122.1728, "documented"),  # SRI Menlo Park CA
    "Project Grill Flame":               (39.1086, -76.7714, "documented"),   # Fort Meade MD
    "Project Center Lane":               (39.1086, -76.7714, "documented"),   # Fort Meade MD
    "Project Sun Streak":                (39.1086, -76.7714, "documented"),   # Fort Meade MD

    # ══════════════════════════════════════════════════════════════════════
    # COSMOLOGY DEEP — expansion_cosmology_deep.py
    # ══════════════════════════════════════════════════════════════════════
    "Brien Foerster":                    (-13.5320, -71.9675, "credible"),    # Cusco Peru
    "Christopher Dunn":                  (38.7577, -90.0882, "credible"),     # Illinois (engineer)
    "Edgar Cayce":                       (36.8529, -75.9780, "documented"),   # Virginia Beach VA
    "Zecharia Sitchin":                  (40.7128, -74.0060, "credible"),     # New York NY
    "Michael Tellinger":                 (-25.7479, 30.4768, "credible"),     # Mpumalanga South Africa
    "Walter Cruttenden":                 (33.6189, -117.9298, "credible"),    # Newport Beach CA
    "Flinders Petrie":                   (29.9792, 31.1342, "documented"),    # Giza Egypt
    "Yonaguni Monument":                 (24.4350, 122.9870, "documented"),   # Yonaguni Japan
    "Derinkuyu":                         (38.3740, 34.7340, "documented"),    # Cappadocia Turkey
    "Sacsayhuamán":                      (-13.5094, -71.9828, "documented"),  # Cusco Peru
    "Nan Madol":                         (6.8433, 158.3339, "documented"),    # Pohnpei Micronesia
    "Carnac Stones":                     (47.5838, -3.0729, "documented"),    # Carnac Brittany France
    "Teotihuacan":                       (19.6925, -98.8438, "documented"),   # Mexico
    "Association for Research and Enlightenment": (36.8529, -75.9780, "documented"),  # Virginia Beach VA
    "Binary Research Institute":         (33.6189, -117.9298, "credible"),    # Newport Beach CA

    # ══════════════════════════════════════════════════════════════════════
    # BIOWEAPONS — expansion_bioweapons.py
    # ══════════════════════════════════════════════════════════════════════
    "Shirō Ishii":                       (45.7500, 126.6500, "documented"),   # Harbin Manchuria
    "Frank Olson":                       (39.4362, -77.4108, "documented"),   # Fort Detrick MD
    "Ken Alibek":                        (51.1605, 71.4704, "credible"),      # Nur-Sultan Kazakhstan (birth)
    "William Patrick III":               (39.4362, -77.4108, "documented"),   # Fort Detrick MD
    "Bruce Ivins":                       (39.4362, -77.4108, "documented"),   # Fort Detrick MD
    "USAMRIID":                          (39.4362, -77.4108, "documented"),   # Fort Detrick Frederick MD
    "DTRA":                              (39.0550, -77.4710, "documented"),   # Fort Belvoir VA
    "Biopreparat":                       (55.7558, 37.6173, "credible"),      # Moscow Russia (HQ)
    "Dugway Proving Ground":             (40.1750, -112.9910, "documented"),  # Tooele County UT
    "Gruinard Island":                   (57.8458, -5.4650, "documented"),    # Scotland UK
    "Unit 731":                          (45.7500, 126.6500, "documented"),   # Harbin Manchuria China
    "Project MKNaomi":                   (39.4362, -77.4108, "documented"),   # Fort Detrick MD
    "Amerithrax Investigation":          (38.8977, -77.0248, "documented"),   # FBI HQ Washington DC
    "Sverdlovsk Anthrax Leak":           (56.8389, 60.6057, "documented"),    # Yekaterinburg Russia
    "Unit 731 Immunity Deal":            (35.6764, 139.6500, "documented"),   # Tokyo (MacArthur HQ)
    "Fort Detrick Lab Shutdown":         (39.4362, -77.4108, "documented"),   # Fort Detrick MD
    "Biological Weapons Convention":     (46.2044, 6.1432, "documented"),     # Geneva Switzerland (UN)

    # ══════════════════════════════════════════════════════════════════════
    # WATER — expansion_water.py
    # ══════════════════════════════════════════════════════════════════════
    "Peter Brabeck-Letmathe":            (46.4650, 6.8413, "credible"),      # Vevey Switzerland (Nestlé HQ)
    "Maude Barlow":                      (45.4215, -75.6972, "credible"),     # Ottawa Canada
    "Vandana Shiva":                     (30.3165, 78.0322, "credible"),      # Dehradun India
    "T. Boone Pickens":                  (35.2072, -101.8338, "credible"),    # Amarillo TX (Panhandle)
    "Nestlé Waters":                     (46.4650, 6.8413, "credible"),      # Vevey Switzerland (Nestlé HQ)
    "Suez Group":                        (48.8967, 2.2522, "credible"),      # Paris France (La Défense)
    "Veolia":                            (48.8900, 2.2580, "credible"),      # Paris France (Aubervilliers)
    "Thames Water":                      (51.5301, -0.1248, "credible"),     # Reading/London UK
    "Cochabamba Water War":              (-17.3895, -66.1568, "documented"),  # Cochabamba Bolivia
    "Flint Water Crisis":                (43.0125, -83.6875, "documented"),   # Flint Michigan
    "Detroit Water Shutoffs":            (42.3314, -83.0458, "documented"),   # Detroit Michigan
    "Standing Rock Protests":            (46.0868, -100.6312, "documented"), # Standing Rock ND
    "Dublin Statement on Water":         (53.3498, -6.2603, "documented"),   # Dublin Ireland
    "Ogallala Aquifer":                  (37.5000, -101.0000, "credible"),   # Great Plains (centroid)
    "Great Lakes":                       (44.0000, -84.0000, "credible"),    # Great Lakes region (centroid)

    # ══════════════════════════════════════════════════════════════════════
    # FOOD SUPPLY — expansion_food_supply.py
    # ══════════════════════════════════════════════════════════════════════
    "Hugh Grant":                        (38.6270, -90.1994, "credible"),    # St. Louis MO (Monsanto HQ)
    "Robert Fraley":                     (38.6270, -90.1994, "credible"),    # St. Louis MO (Monsanto HQ)
    "Percy Schmeiser":                   (52.1579, -106.6702, "documented"), # Bruno Saskatchewan Canada
    "Tyrone Hayes":                      (37.8716, -122.2727, "credible"),   # UC Berkeley CA
    "Cargill":                           (44.9600, -93.3900, "credible"),    # Wayzata MN
    "ADM":                               (39.7817, -89.6501, "credible"),    # Decatur IL (original HQ)
    "Syngenta":                          (47.5596, 7.5886, "credible"),     # Basel Switzerland
    "Bayer":                             (51.0504, 6.9823, "credible"),     # Leverkusen Germany
    "USDA":                              (38.8863, -77.0311, "documented"),  # Washington DC
    "Codex Alimentarius Commission":     (41.3851, 2.1734, "credible"),     # Rome Italy (FAO HQ)
    "Indian Farmer Suicides":            (19.7515, 75.7139, "credible"),    # Maharashtra India
    "Terminator Seeds":                  (38.8863, -77.0311, "credible"),   # Washington DC (USDA)
    "ADM Price-Fixing Scandal":          (39.7817, -89.6501, "documented"), # Decatur IL (ADM HQ)
    "Monsanto Papers":                   (38.6270, -90.1994, "documented"), # St. Louis MO
    "Roundup Cancer Litigation":         (37.7749, -122.4194, "documented"),# San Francisco CA (first trial)
    "Monsanto Protection Act":           (38.8977, -77.0365, "documented"), # Washington DC
    "DARK Act":                          (38.8977, -77.0365, "documented"), # Washington DC
    "Plant Variety Protection Act":      (38.8977, -77.0365, "documented"), # Washington DC
}


def export_geo(db, out_dir):
    """Export geo-entities.json and geo-signals.json to out_dir."""
    db.row_factory = sqlite3.Row

    # ── Resolve entity names → current IDs ──
    name_to_row = {}
    for row in db.execute("SELECT id, name, entity_type, description FROM entities"):
        name_to_row[row["name"]] = row

    resolved = {}  # id → (lat, lon, tier)
    unresolved = []
    for name, (lat, lon, tier) in GEO_COORDS.items():
        row = name_to_row.get(name)
        if row:
            resolved[row["id"]] = (lat, lon, tier)
        else:
            unresolved.append(name)

    if unresolved:
        print(f"  WARNING: {len(unresolved)} geo names not found in DB:")
        for n in unresolved[:10]:
            print(f"    - {n}")

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
    for eid, (lat, lon, tier) in resolved.items():
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
    entity_coords = {eid: (lat, lon) for eid, (lat, lon, _) in resolved.items()}

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
