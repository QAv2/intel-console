"""
World Economic Forum — Expansion layer for Intel Console.

Breaking news (Feb 26, 2026): WEF President Børge Brende steps down
after Epstein files reveal three business dinners, emails, and texts
with Jeffrey Epstein. WEF launched independent investigation by outside
counsel — found "no additional concerns beyond what has been previously
disclosed." Alois Zwinggi named interim president/CEO.

Entities: Børge Brende, World Economic Forum, Klaus Schwab,
Alois Zwinggi, Davos Annual Meeting

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Jeffrey Epstein [1], Henry Kissinger [111], Kissinger Associates [115]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 444+ (continuing from existing 443)
# ============================================================

SOURCES = [
    {
        "id": 444,
        "title": "World Economic Forum Chief Brende Steps Down Amid Epstein Links — Bloomberg",
        "url": "https://www.bloomberg.com/news/articles/2026-02-26/world-economic-forum-chief-brende-steps-down-amid-epstein-links",
        "source_type": "journalism",
        "author": "Bloomberg News",
        "year": 2026,
    },
    {
        "id": 445,
        "title": "World Economic Forum head Borge Brende quits after Epstein links revealed — Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/2/26/world-economic-forum-head-borge-brende-quits-after-epstein-links-revealed",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    {
        "id": 446,
        "title": "Davos forum chief Brende steps down after WEF probes Epstein links — Euronews",
        "url": "https://www.euronews.com/2026/02/26/davos-forum-chief-brende-steps-down-after-wef-probes-epstein-links",
        "source_type": "journalism",
        "author": "Euronews",
        "year": 2026,
    },
    {
        "id": 447,
        "title": "WEF CEO Børge Brende steps down as the Epstein files claim another top executive — CNN Business",
        "url": "https://www.cnn.com/2026/02/26/business/borge-brende-wef-epstein-files-intl",
        "source_type": "journalism",
        "author": "CNN Business",
        "year": 2026,
    },
    {
        "id": 448,
        "title": "World Economic Forum head to resign over Epstein ties — Fortune",
        "url": "https://fortune.com/2026/02/26/world-economic-forum-head-to-resign-over-epstein-ties-borge-brende/",
        "source_type": "journalism",
        "author": "Fortune",
        "year": 2026,
    },
    {
        "id": 449,
        "title": "WEF CEO Brende resigns amid growing global fallout — Axios",
        "url": "https://www.axios.com/2026/02/26/wef-ceo-resigns-epstein-files-fallout-brende",
        "source_type": "journalism",
        "author": "Axios",
        "year": 2026,
    },
    {
        "id": 450,
        "title": "World Economic Forum head Børge Brende resigns over Epstein ties — Semafor",
        "url": "https://www.semafor.com/article/02/26/2026/world-economic-forum-head-brge-brende-resigns-over-epstein-ties",
        "source_type": "journalism",
        "author": "Semafor",
        "year": 2026,
    },
    {
        "id": 451,
        "title": "World Economic Forum — Wikipedia (founding, structure, Davos history)",
        "url": "https://en.wikipedia.org/wiki/World_Economic_Forum",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 452,
        "title": "Klaus Schwab — Wikipedia (WEF founder biography)",
        "url": "https://en.wikipedia.org/wiki/Klaus_Schwab",
        "source_type": "other",
        "year": 2026,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    {
        "name": "World Economic Forum",
        "entity_type": "organization",
        "description": (
            "International non-governmental organization founded in 1971 by Klaus Schwab, "
            "headquartered in Cologny, Geneva, Switzerland. Hosts the annual Davos meeting — "
            "the world's premier gathering of political leaders, CEOs, central bankers, and "
            "billionaires. Known for shaping global policy through public-private partnerships. "
            "Henry Kissinger was instrumental in the Forum's early years, helping transform it "
            "from a European management symposium into a global geopolitical institution. "
            "On February 26, 2026, WEF President/CEO Børge Brende stepped down after Epstein "
            "files revealed he had three business dinners and exchanged emails/texts with "
            "Jeffrey Epstein. WEF co-chairs André Hoffmann and Larry Fink announced the "
            "completion of an independent investigation by outside counsel. Alois Zwinggi "
            "appointed interim president/CEO."
        ),
        "aliases": "WEF, Davos Forum, World Economic Forum",
    },
    {
        "name": "Børge Brende",
        "entity_type": "person",
        "description": (
            "Norwegian politician and business executive. Former Foreign Minister of Norway "
            "(2013-2017). Became President and CEO of the World Economic Forum in 2017. "
            "On February 26, 2026, Brende resigned after Epstein files revealed he had three "
            "business dinners with Jeffrey Epstein and communicated via email and text. WEF "
            "launched an independent investigation by outside counsel which concluded there "
            "were 'no additional concerns beyond what has been previously disclosed.' Brende "
            "stated he decided 'after careful consideration' that stepping down was appropriate, "
            "saying: 'I believe now is the right moment for the Forum to continue its important "
            "work without distractions.' Second WEF chief to depart due to scandal. One of "
            "several prominent Norwegians facing scrutiny following Epstein files release "
            "(others include a former PM and the Crown Princess)."
        ),
        "aliases": "Borge Brende",
        "metadata": {
            "nationality": "Norwegian",
            "born": "1965-01-25",
            "role": "WEF President/CEO 2017-2026",
            "prior_role": "Foreign Minister of Norway 2013-2017",
        },
    },
    {
        "name": "Klaus Schwab",
        "entity_type": "person",
        "description": (
            "German engineer, economist, and founder of the World Economic Forum (1971). "
            "Executive Chairman of WEF from founding until transitioning leadership to Brende. "
            "Architect of the 'Great Reset' initiative and 'Fourth Industrial Revolution' "
            "framework. Under Schwab's leadership, Davos became the premier gathering point "
            "for global elites — heads of state, central bankers, Fortune 500 CEOs, and "
            "billionaires. Henry Kissinger was a key early adviser who helped elevate the Forum "
            "from the European Management Forum into a global institution."
        ),
        "aliases": "Klaus Martin Schwab",
        "metadata": {
            "nationality": "German",
            "born": "1938-03-30",
            "role": "WEF Founder & Executive Chairman",
        },
    },
    {
        "name": "Alois Zwinggi",
        "entity_type": "person",
        "description": (
            "Swiss executive, longtime World Economic Forum Managing Director. Appointed "
            "interim President and CEO of WEF on February 26, 2026, following the resignation "
            "of Børge Brende over Epstein file revelations. WEF board of trustees to oversee "
            "the search for a permanent replacement."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "Swiss",
            "role": "WEF Interim President/CEO (Feb 2026-)",
        },
    },
    {
        "name": "Davos Annual Meeting",
        "entity_type": "event",
        "description": (
            "Annual gathering hosted by the World Economic Forum in Davos-Klosters, Switzerland, "
            "typically in January. Convenes ~3,000 participants including heads of state, CEOs, "
            "central bankers, and media figures. The invitation-only event functions as the "
            "premier global coordination mechanism for political-economic elites. Attendance "
            "is a marker of establishment access. The Epstein network intersected with multiple "
            "regular Davos attendees."
        ),
        "aliases": "Davos, WEF Annual Meeting",
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ---- Børge Brende ----
    {
        "source": "Børge Brende",
        "target": "World Economic Forum",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "President and CEO of WEF from 2017 until resignation on February 26, 2026. "
            "Stepped down after Epstein files revealed three business dinners and email/text "
            "exchanges with Jeffrey Epstein."
        ),
        "year_start": 2017,
        "year_end": 2026,
        "sources": [444, 445, 448],
    },
    {
        "source": "Børge Brende",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Epstein files revealed Brende had three business dinners with Jeffrey Epstein "
            "and communicated with him via email and text messages. WEF independent investigation "
            "by outside counsel found 'no additional concerns beyond what has been previously "
            "disclosed.' No indication of wrongdoing beyond the contact itself. Brende claimed "
            "he only met Epstein in business settings and was unaware of criminal background."
        ),
        "sources": [444, 445, 446, 447, 448, 449, 450],
    },
    # ---- Klaus Schwab ----
    {
        "source": "Klaus Schwab",
        "target": "World Economic Forum",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Founded the European Management Forum in 1971 (renamed World Economic Forum "
            "in 1987). Served as Executive Chairman from founding until leadership transition. "
            "Transformed a regional management conference into the premier global elite gathering."
        ),
        "sources": [451, 452],
    },
    # ---- Alois Zwinggi ----
    {
        "source": "Alois Zwinggi",
        "target": "World Economic Forum",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Appointed interim President and CEO of WEF on February 26, 2026, following "
            "Brende's resignation. WEF board of trustees overseeing search for permanent "
            "replacement."
        ),
        "year_start": 2026,
        "sources": [444, 448, 450],
    },
    # ---- WEF connections to existing entities ----
    {
        "source": "Henry Kissinger",
        "target": "World Economic Forum",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": (
            "Kissinger was instrumental in the early development of the World Economic Forum, "
            "helping elevate it from the European Management Forum into a global geopolitical "
            "institution. Regular Davos attendee and adviser to Schwab for decades."
        ),
        "sources": [451, 452],
    },
    {
        "source": "World Economic Forum",
        "target": "Davos Annual Meeting",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "WEF hosts the annual Davos meeting in Davos-Klosters, Switzerland. The invitation-only "
            "event convenes ~3,000 global leaders, CEOs, and media figures annually since 1971."
        ),
        "sources": [451],
    },
    {
        "source": "Jeffrey Epstein",
        "target": "World Economic Forum",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "The Epstein network intersected with multiple regular Davos/WEF attendees. "
            "WEF President Brende had three documented business dinners with Epstein. "
            "The Epstein files release triggered a WEF internal investigation and ultimately "
            "Brende's resignation on February 26, 2026."
        ),
        "sources": [444, 445, 446, 447, 448, 449, 450],
    },
]

# ============================================================
# ENTITY → SOURCE mappings
# ============================================================

ENTITY_SOURCES = {
    "World Economic Forum": [444, 445, 446, 447, 448, 449, 450, 451],
    "Børge Brende": [444, 445, 446, 447, 448, 449, 450],
    "Klaus Schwab": [451, 452],
    "Alois Zwinggi": [444, 448, 450],
    "Davos Annual Meeting": [451],
}
