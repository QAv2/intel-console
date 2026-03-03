"""
Defense Contractors / Military-Industrial Complex — Expansion layer for Intel Console.

Maps the military-industrial complex that Eisenhower warned about: the major
defense contractors, their revolving door with government, the Special Access
Programs that hide trillions in unaccountable spending, and the private military
companies that outsource warfare.

Entities (~18): Defense corporations (Lockheed Martin, Raytheon/RTX, Northrop Grumman,
Boeing Defense, General Dynamics, BAE Systems, L3Harris, Booz Allen Hamilton),
private military (Halliburton/KBR, Blackwater/Academi, DynCorp), key figures
(Eisenhower, Erik Prince, Norman Augustine), programs (Special Access Programs,
F-35), events (Eisenhower Farewell, Pentagon audit failures).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], NSA [86], DARPA [90], Dick Cheney [244],
  Donald Rumsfeld [245], Carlyle Group [176], Bechtel Corporation [262],
  Prince Bandar bin Sultan [168], BAE Al-Yamamah Deal [177],
  Edward Snowden [321]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 666-690
# ============================================================

SOURCES = [
    # --- Eisenhower ---
    {
        "id": 666,
        "title": "President Dwight D. Eisenhower — Farewell Address warning of military-industrial complex (Jan 17, 1961)",
        "url": "https://www.archives.gov/milestone-documents/president-dwight-d-eisenhowers-farewell-address",
        "source_type": "government",
        "year": 1961,
    },
    # --- Defense Industry Studies ---
    {
        "id": 667,
        "title": "William Hartung — Prophets of War: Lockheed Martin and the Making of the Military-Industrial Complex",
        "url": "https://en.wikipedia.org/wiki/Prophets_of_War",
        "source_type": "academic",
        "author": "William Hartung",
        "year": 2011,
    },
    {
        "id": 668,
        "title": "Andrew Feinstein — The Shadow World: Inside the Global Arms Trade",
        "url": "https://en.wikipedia.org/wiki/The_Shadow_World_(book)",
        "source_type": "journalism",
        "author": "Andrew Feinstein",
        "year": 2011,
    },
    {
        "id": 669,
        "title": "Nick Turse — The Complex: How the Military Invades Our Everyday Lives",
        "url": "https://en.wikipedia.org/wiki/Nick_Turse",
        "source_type": "journalism",
        "author": "Nick Turse",
        "year": 2008,
    },
    {
        "id": 670,
        "title": "Gordon Adams — The Iron Triangle: The Politics of Defense Contracting",
        "url": "https://en.wikipedia.org/wiki/Iron_triangle_(US_politics)",
        "source_type": "academic",
        "author": "Gordon Adams",
        "year": 1981,
    },
    # --- Pentagon Audit ---
    {
        "id": 671,
        "title": "DOD Inspector General — Summary of DOD Office of the Inspector General Audits of Financial Management",
        "url": "https://www.dodig.mil/reports.html",
        "source_type": "government",
        "year": 2023,
    },
    {
        "id": 672,
        "title": "Pentagon fails 6th consecutive audit — Reuters (Nov 2023)",
        "url": "https://www.reuters.com/business/aerospace-defense/pentagon-fails-sixth-audit-2023-11-15/",
        "source_type": "journalism",
        "year": 2023,
    },
    # --- F-35 Program ---
    {
        "id": 673,
        "title": "GAO — F-35 Joint Strike Fighter: DOD Needs to Update Modernization Schedule and Improve Data on Software Development",
        "url": "https://www.gao.gov/products/gao-22-105128",
        "source_type": "government",
        "year": 2022,
    },
    {
        "id": 674,
        "title": "F-35 Program — $1.7 trillion lifecycle cost estimate (DOD Selected Acquisition Report)",
        "url": "https://www.gao.gov/products/gao-21-439",
        "source_type": "government",
        "year": 2021,
    },
    # --- Special Access Programs ---
    {
        "id": 675,
        "title": "DOD Directive 5205.07 — Special Access Program (SAP) Policy",
        "url": "https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodd/520507p.pdf",
        "source_type": "government",
        "year": 2020,
    },
    # --- Revolving Door ---
    {
        "id": 676,
        "title": "POGO (Project on Government Oversight) — Pentagon Revolving Door Database",
        "url": "https://www.pogo.org/database/pentagon-revolving-door",
        "source_type": "other",
        "year": 2023,
    },
    # --- SIPRI ---
    {
        "id": 677,
        "title": "SIPRI — Top 100 Arms-Producing and Military Services Companies (2022 data)",
        "url": "https://www.sipri.org/databases/armsindustry",
        "source_type": "academic",
        "year": 2023,
    },
    # --- Private Military ---
    {
        "id": 678,
        "title": "Jeremy Scahill — Blackwater: The Rise of the World's Most Powerful Mercenary Army",
        "url": "https://en.wikipedia.org/wiki/Blackwater:_The_Rise_of_the_World%27s_Most_Powerful_Mercenary_Army",
        "source_type": "journalism",
        "author": "Jeremy Scahill",
        "year": 2007,
    },
    {
        "id": 679,
        "title": "Erik Prince — House Oversight Committee testimony on Blackwater operations",
        "url": "https://en.wikipedia.org/wiki/Erik_Prince",
        "source_type": "congressional",
        "year": 2007,
    },
    {
        "id": 680,
        "title": "Halliburton Iraq contracts — DOD Inspector General audit of KBR billing irregularities",
        "url": "https://www.dodig.mil/reports.html",
        "source_type": "government",
        "year": 2004,
    },
    {
        "id": 681,
        "title": "KBR electrocution incidents — Congressional investigation of electrical work in Iraq military facilities",
        "url": "https://en.wikipedia.org/wiki/KBR_(company)#Electrocution_incidents_in_Iraq",
        "source_type": "congressional",
        "year": 2008,
    },
    {
        "id": 682,
        "title": "DynCorp trafficking allegations — State Department Inspector General investigation (Bosnia, 2000s)",
        "url": "https://en.wikipedia.org/wiki/DynCorp#Sex_trafficking",
        "source_type": "government",
        "year": 2002,
    },
    # --- Booz Allen / Snowden ---
    {
        "id": 683,
        "title": "Booz Allen Hamilton — NSA contractor employing Edward Snowden at time of disclosures",
        "url": "https://en.wikipedia.org/wiki/Booz_Allen_Hamilton",
        "source_type": "journalism",
        "year": 2013,
    },
    # --- Pentagon Papers ---
    {
        "id": 684,
        "title": "Pentagon Papers — DOD history of Vietnam War decision-making (leaked by Daniel Ellsberg, 1971)",
        "url": "https://www.archives.gov/research/pentagon-papers",
        "source_type": "government",
        "year": 1971,
    },
    # --- Norman Augustine ---
    {
        "id": 685,
        "title": "Norman Augustine — 'Augustine's Laws' and consolidation of defense industry in 1990s",
        "url": "https://en.wikipedia.org/wiki/Norman_Ralph_Augustine",
        "source_type": "other",
        "year": 1997,
    },
    # --- Lockheed Merger ---
    {
        "id": 686,
        "title": "Lockheed Martin merger (1995) — creation of world's largest defense contractor from Lockheed Corp + Martin Marietta",
        "url": "https://en.wikipedia.org/wiki/Lockheed_Martin",
        "source_type": "other",
        "year": 1995,
    },
    # --- Nisour Square ---
    {
        "id": 687,
        "title": "Nisour Square massacre — Blackwater contractors kill 17 Iraqi civilians, pardoned by Trump (2020)",
        "url": "https://en.wikipedia.org/wiki/Nisour_Square_massacre",
        "source_type": "court",
        "year": 2007,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Major Defense Contractors ---
    {
        "name": "Lockheed Martin",
        "entity_type": "organization",
        "description": "World's largest defense contractor. Formed from 1995 merger of Lockheed Corporation and Martin Marietta. F-35, F-22, C-130, missile defense. Revenue ~$66B (2022). Spends ~$13M annually on lobbying. Revolving door with Pentagon is pervasive.",
        "aliases": "LMT, Lockheed",
        "metadata": {"type": "defense contractor", "founded": 1995},
    },
    {
        "name": "Raytheon",
        "entity_type": "organization",
        "description": "Major defense contractor, merged with United Technologies to form RTX (2020). Missiles (Tomahawk, Patriot, Stinger), radar systems, cyber. Former CEO Lloyd Austin became SecDef — then recused. Revenue ~$67B (2022).",
        "aliases": "RTX, Raytheon Technologies",
        "metadata": {"type": "defense contractor", "founded": 1922},
    },
    {
        "name": "Northrop Grumman",
        "entity_type": "organization",
        "description": "Major defense contractor. B-2 Spirit, B-21 Raider, Global Hawk, James Webb Space Telescope. Key player in classified programs including Special Access Programs. Revenue ~$37B (2022).",
        "aliases": "NOC",
        "metadata": {"type": "defense contractor", "founded": 1994},
    },
    {
        "name": "Boeing Defense",
        "entity_type": "organization",
        "description": "Defense arm of Boeing Company. F/A-18, AH-64 Apache, KC-46, Space Launch System. Multiple scandals including tanker contract corruption (Darleen Druyun), 737 MAX design failures. Revenue ~$23B defense (2022).",
        "aliases": "Boeing Defense, Space & Security",
        "metadata": {"type": "defense contractor"},
    },
    {
        "name": "General Dynamics",
        "entity_type": "organization",
        "description": "Major defense contractor. Submarines (Virginia-class, Columbia-class), Abrams tank, Gulfstream jets, IT systems. Revenue ~$39B (2022). Deep relationship with Navy submarine programs.",
        "aliases": "GD",
        "metadata": {"type": "defense contractor", "founded": 1899},
    },
    {
        "name": "BAE Systems",
        "entity_type": "organization",
        "description": "Europe's largest defense contractor (UK-based). Central to Al-Yamamah arms deal with Saudi Arabia — largest arms deal in UK history, with £1B+ in commissions to Prince Bandar. SFO investigation shut down by Tony Blair citing 'national security.'",
        "aliases": "British Aerospace, BAE",
        "metadata": {"type": "defense contractor", "founded": 1999},
    },
    {
        "name": "L3Harris Technologies",
        "entity_type": "organization",
        "description": "Defense and intelligence contractor formed from L3 Technologies + Harris Corporation merger (2019). ISR systems, communications, electronic warfare. Revenue ~$17B (2022). Major NSA and intelligence community contractor.",
        "aliases": "L3Harris, LHX",
        "metadata": {"type": "defense contractor", "founded": 2019},
    },
    {
        "name": "Booz Allen Hamilton",
        "entity_type": "organization",
        "description": "Management and IT consulting firm, major intelligence community contractor. Employed Edward Snowden at time of NSA disclosures. 70%+ revenue from government contracts. Called 'the world's most profitable spy organization' by Bloomberg.",
        "aliases": "Booz Allen, BAH",
        "metadata": {"type": "defense/intelligence contractor", "founded": 1914},
    },
    # --- Private Military ---
    {
        "name": "Halliburton",
        "entity_type": "organization",
        "description": "Oilfield services and military contractor. Dick Cheney was CEO (1995-2000) before becoming VP. KBR subsidiary received $39.5B in Iraq contracts, many no-bid. DOD IG found widespread billing irregularities. KBR electrocution incidents killed soldiers.",
        "aliases": "Halliburton, KBR",
        "metadata": {"type": "military contractor", "founded": 1919},
    },
    {
        "name": "Blackwater",
        "entity_type": "organization",
        "description": "Private military company founded by Erik Prince (1997). Renamed Xe Services (2009), then Academi (2011). Nisour Square massacre (2007): contractors killed 17 Iraqi civilians, convicted, then pardoned by Trump. Prince connected to CIA covert programs and later UAE/China private military ventures.",
        "aliases": "Xe Services, Academi",
        "metadata": {"type": "private military", "founded": 1997},
    },
    {
        "name": "DynCorp",
        "entity_type": "organization",
        "description": "Private military and security contractor. State Department Inspector General investigated employee involvement in human trafficking in Bosnia (2002). Also contracted for Colombia counter-narcotics. Pattern of misconduct with minimal accountability.",
        "aliases": "",
        "metadata": {"type": "private military", "founded": 1946},
    },
    # --- Key Figures ---
    {
        "name": "Erik Prince",
        "entity_type": "person",
        "description": "Founder of Blackwater. Brother of Betsy DeVos (Trump Education Secretary). Connected to CIA covert operations. Proposed private intelligence network to Trump admin bypassing official channels. Later founded Frontier Services Group with Chinese state-backed funding.",
        "aliases": "",
        "metadata": {"role": "Blackwater founder", "years_active": "1997-present"},
    },
    {
        "name": "Dwight D. Eisenhower",
        "entity_type": "person",
        "description": "34th President, five-star general, Supreme Allied Commander WWII. In farewell address (Jan 17, 1961) warned: 'In the councils of government, we must guard against the acquisition of unwarranted influence...by the military-industrial complex.' Original draft used 'military-industrial-congressional complex.'",
        "aliases": "Ike",
        "metadata": {"role": "President", "years_active": "1953-1961"},
    },
    {
        "name": "Norman Augustine",
        "entity_type": "person",
        "description": "CEO of Lockheed Martin during the 1995 merger. Author of 'Augustine's Laws' (satirical laws of defense procurement). Architect of defense industry consolidation in the 1990s — the 'Last Supper' where Pentagon encouraged mergers, reducing competitive bidding.",
        "aliases": "",
        "metadata": {"role": "Lockheed Martin CEO", "years_active": "1987-1997"},
    },
    # --- Programs ---
    {
        "name": "Special Access Programs",
        "entity_type": "program",
        "description": "DOD classification level above Top Secret. Includes Acknowledged SAPs and Unacknowledged SAPs (USAPs, also called 'waived' SAPs — exempt from normal congressional oversight). Estimated hundreds of SAPs active. USAPs are where 'black budget' programs reside, potentially including crash retrieval programs per Grusch testimony.",
        "aliases": "SAPs, USAPs, Black Programs",
        "metadata": {"type": "classification system"},
    },
    {
        "name": "F-35 Joint Strike Fighter",
        "entity_type": "program",
        "description": "Most expensive weapons program in history — $1.7 trillion estimated lifecycle cost. Lockheed Martin prime contractor. Plagued by delays, cost overruns, and technical problems. GAO has issued critical reports annually. Exemplifies defense procurement dysfunction.",
        "aliases": "F-35, Lightning II, JSF",
        "metadata": {"type": "weapons program", "years_active": "2001-present"},
    },
    # --- Events ---
    {
        "name": "Eisenhower Farewell Address",
        "entity_type": "event",
        "description": "Televised farewell address by President Eisenhower (Jan 17, 1961) warning of the 'military-industrial complex.' A five-star general and two-term president warning the nation about the very establishment he had led. Original draft said 'military-industrial-congressional complex.'",
        "aliases": "",
        "metadata": {"date": "1961-01-17"},
    },
    {
        "name": "Pentagon Audit Failures",
        "entity_type": "event",
        "description": "The Pentagon has failed every comprehensive audit since they began in 2018. Six consecutive failures through 2023. Trillions in transactions cannot be tracked. Rumsfeld announced $2.3 trillion in untracked transactions on Sept 10, 2001 — the day before 9/11.",
        "aliases": "",
        "metadata": {"date": "2018-present"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Eisenhower ---
    {
        "source": "Dwight D. Eisenhower",
        "target": "Eisenhower Farewell Address",
        "type": "authored",
        "tier": "documented",
        "desc": "Warned of 'military-industrial complex' gaining unwarranted influence. A five-star general warning about the system he had led.",
        "sources": [666],
        "year_start": 1961,
        "year_end": 1961,
    },
    # --- Lockheed Martin ---
    {
        "source": "Norman Augustine",
        "target": "Lockheed Martin",
        "type": "directed",
        "tier": "documented",
        "desc": "CEO who engineered the Lockheed-Martin Marietta merger, creating the world's largest defense contractor.",
        "sources": [685, 686],
        "year_start": 1987,
        "year_end": 1997,
    },
    {
        "source": "Lockheed Martin",
        "target": "F-35 Joint Strike Fighter",
        "type": "developed",
        "tier": "documented",
        "desc": "Prime contractor for $1.7T F-35 program — most expensive weapons system in history.",
        "sources": [673, 674],
        "year_start": 2001,
        "year_end": None,
    },
    {
        "source": "Lockheed Martin",
        "target": "DARPA",
        "type": "contracted_by",
        "tier": "documented",
        "desc": "Major DARPA contractor across multiple programs including stealth, hypersonics, and space systems.",
        "sources": [667, 677],
        "year_start": 1970,
        "year_end": None,
    },
    # --- Raytheon ---
    {
        "source": "Raytheon",
        "target": "DARPA",
        "type": "contracted_by",
        "tier": "documented",
        "desc": "Major DARPA contractor for missile defense, radar, and cyber systems.",
        "sources": [677],
        "year_start": 1960,
        "year_end": None,
    },
    # --- Northrop Grumman ---
    {
        "source": "Northrop Grumman",
        "target": "Special Access Programs",
        "type": "participated_in",
        "tier": "credible",
        "desc": "Known participant in classified SAPs including stealth programs (B-2, B-21). Key contractor for black budget programs.",
        "sources": [675, 677],
        "year_start": 1980,
        "year_end": None,
    },
    # --- Boeing ---
    {
        "source": "Boeing Defense",
        "target": "DARPA",
        "type": "contracted_by",
        "tier": "documented",
        "desc": "Major defense contractor and DARPA partner across aerospace and space programs.",
        "sources": [677],
        "year_start": 1960,
        "year_end": None,
    },
    # --- BAE Systems ---
    {
        "source": "BAE Systems",
        "target": "BAE Al-Yamamah Deal",
        "type": "participated_in",
        "tier": "documented",
        "desc": "BAE (formerly British Aerospace) was prime contractor in Al-Yamamah deal. SFO investigation into £1B+ commissions shut down by Blair government.",
        "sources": [668],
        "year_start": 1985,
        "year_end": None,
    },
    {
        "source": "BAE Systems",
        "target": "Prince Bandar bin Sultan",
        "type": "connected_to",
        "tier": "documented",
        "desc": "BAE made payments exceeding £1 billion to accounts controlled by or for Bandar via the Al-Yamamah deal.",
        "sources": [668],
        "year_start": 1985,
        "year_end": 2006,
    },
    # --- Booz Allen ---
    {
        "source": "Booz Allen Hamilton",
        "target": "NSA",
        "type": "contracted_by",
        "tier": "documented",
        "desc": "Major NSA contractor. Employed Snowden at time of 2013 disclosures. Called 'most profitable spy organization' by Bloomberg.",
        "sources": [683],
        "year_start": 2000,
        "year_end": None,
    },
    {
        "source": "Edward Snowden",
        "target": "Booz Allen Hamilton",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Employed as NSA contractor at Booz Allen when he disclosed mass surveillance programs in 2013.",
        "sources": [683],
        "year_start": 2013,
        "year_end": 2013,
    },
    # --- Halliburton / Cheney ---
    {
        "source": "Dick Cheney",
        "target": "Halliburton",
        "type": "directed",
        "tier": "documented",
        "desc": "CEO of Halliburton 1995-2000 before becoming VP. Company received $39.5B in Iraq contracts, many no-bid.",
        "sources": [680],
        "year_start": 1995,
        "year_end": 2000,
    },
    # --- Blackwater ---
    {
        "source": "Erik Prince",
        "target": "Blackwater",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded Blackwater in 1997. Company became largest private military contractor in Iraq/Afghanistan.",
        "sources": [678, 679],
        "year_start": 1997,
        "year_end": 2010,
    },
    {
        "source": "Erik Prince",
        "target": "CIA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Blackwater provided covert services for CIA including targeted killing program. Prince later proposed private spy network to Trump administration.",
        "sources": [678, 679],
        "year_start": 2002,
        "year_end": None,
    },
    {
        "source": "Blackwater",
        "target": "Halliburton",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Both major Iraq War contractors. Exemplified outsourcing of military functions to private companies with minimal oversight.",
        "sources": [678, 680],
        "year_start": 2003,
        "year_end": 2011,
    },
    # --- DynCorp ---
    {
        "source": "DynCorp",
        "target": "FBI",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "State Dept IG investigated DynCorp employees for involvement in human trafficking in Bosnia. Whistleblower Kathryn Bolkovac fired and vindicated in court.",
        "sources": [682],
        "year_start": 2002,
        "year_end": 2002,
    },
    # --- Pentagon Audit ---
    {
        "source": "Donald Rumsfeld",
        "target": "Pentagon Audit Failures",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Announced $2.3 trillion in untracked Pentagon transactions on Sept 10, 2001. Pentagon has failed every comprehensive audit since 2018.",
        "sources": [671, 672],
        "year_start": 2001,
        "year_end": 2001,
    },
    # --- Carlyle Group ---
    {
        "source": "Carlyle Group",
        "target": "Lockheed Martin",
        "type": "invested_in",
        "tier": "documented",
        "desc": "Carlyle Group is a major defense private equity investor. Invested in multiple defense companies and benefited from post-9/11 spending surge.",
        "sources": [667, 670],
        "year_start": 1990,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Lockheed Martin": [667, 673, 674, 677, 686],
    "Raytheon": [677],
    "Northrop Grumman": [675, 677],
    "Boeing Defense": [677],
    "General Dynamics": [677],
    "BAE Systems": [668],
    "L3Harris Technologies": [677],
    "Booz Allen Hamilton": [683],
    "Halliburton": [680, 681],
    "Blackwater": [678, 679, 687],
    "DynCorp": [682],
    "Erik Prince": [678, 679],
    "Dwight D. Eisenhower": [666],
    "Norman Augustine": [685, 686],
    "Special Access Programs": [675],
    "F-35 Joint Strike Fighter": [673, 674],
    "Eisenhower Farewell Address": [666],
    "Pentagon Audit Failures": [671, 672],
}
