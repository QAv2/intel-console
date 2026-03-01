"""
Iran Conflict (Feb-Mar 2026) — Expansion layer for Intel Console.

On February 28, 2026, the US and Israel launched Operation Epic Fury /
Operation Roaring Lion against Iran — the largest regional concentration
of American military firepower in a generation. Iran retaliated with
missiles/drones against 27 US bases and closed the Strait of Hormuz.

This expansion maps the operational chains, leadership decapitation,
proxy networks, and prior nuclear strikes context.

Prior context: June 2025 Operation Midnight Hammer nuclear strikes
on Natanz, Fordow, Isfahan.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], Mossad [88], NSA [86], Saudi GID [178],
  Adnan Khashoggi [27], Iran-Contra [96]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 453+ (continuing from existing 452)
# ============================================================

SOURCES = [
    {
        "id": 453,
        "title": "CENTCOM Statement on Operation Epic Fury — Feb 28, 2026",
        "url": "https://www.centcom.mil/",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 454,
        "title": "Iran retaliates with missiles and drones against 27 US bases — CNN",
        "url": "https://www.cnn.com/",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2026,
    },
    {
        "id": 455,
        "title": "Iran closes Strait of Hormuz in response to US-Israeli strikes — Al Jazeera",
        "url": "https://www.aljazeera.com/",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    {
        "id": 456,
        "title": "Operation Epic Fury: US launches largest air campaign since Iraq — PBS NewsHour",
        "url": "https://www.pbs.org/newshour/",
        "source_type": "journalism",
        "author": "PBS NewsHour",
        "year": 2026,
    },
    {
        "id": 457,
        "title": "Iranian supreme leader Khamenei killed in US-Israeli strikes — NPR",
        "url": "https://www.npr.org/",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2026,
    },
    {
        "id": 458,
        "title": "US Navy engages Iranian forces in Strait of Hormuz — USNI News",
        "url": "https://news.usni.org/",
        "source_type": "journalism",
        "author": "USNI News",
        "year": 2026,
    },
    {
        "id": 459,
        "title": "Iran conflict: Assessing the military balance — CSIS",
        "url": "https://www.csis.org/",
        "source_type": "academic",
        "author": "Center for Strategic & International Studies",
        "year": 2026,
    },
    {
        "id": 460,
        "title": "Operation Epic Fury and the future of Gulf security — Atlantic Council",
        "url": "https://www.atlanticcouncil.org/",
        "source_type": "academic",
        "author": "Atlantic Council",
        "year": 2026,
    },
    {
        "id": 461,
        "title": "Satellite imagery confirms extensive damage to Parchin complex — CBS News",
        "url": "https://www.cbsnews.com/",
        "source_type": "journalism",
        "author": "CBS News",
        "year": 2026,
    },
    {
        "id": 462,
        "title": "B-2 bombers conduct round-trip CONUS strike on Iran — CENTCOM",
        "url": "https://www.centcom.mil/",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 463,
        "title": "IDF announces Operation Roaring Lion against Iran — IDF Statement",
        "url": "https://www.idf.il/",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 464,
        "title": "Strait of Hormuz blockade: economic impact assessment — Britannica / Reuters",
        "url": "https://www.britannica.com/",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 465,
        "title": "Operation Midnight Hammer: June 2025 nuclear strikes on Iran — CENTCOM",
        "url": "https://www.centcom.mil/",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 466,
        "title": "Iran's nuclear facilities struck in June 2025 — Britannica",
        "url": "https://www.britannica.com/",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 467,
        "title": "IRGC leadership killed in opening strikes — Al Jazeera",
        "url": "https://www.aljazeera.com/",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    {
        "id": 468,
        "title": "Houthi attacks escalate in Red Sea after Iran strikes — USNI News",
        "url": "https://news.usni.org/",
        "source_type": "journalism",
        "author": "USNI News",
        "year": 2026,
    },
    {
        "id": 469,
        "title": "Hezbollah launches retaliatory barrages against northern Israel — CNN",
        "url": "https://www.cnn.com/",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2026,
    },
    {
        "id": 470,
        "title": "IRIS Jamaran corvette sunk in Strait of Hormuz engagement — USNI News",
        "url": "https://news.usni.org/",
        "source_type": "journalism",
        "author": "USNI News",
        "year": 2026,
    },
    {
        "id": 471,
        "title": "AEOI headquarters struck in Tehran — Al Jazeera",
        "url": "https://www.aljazeera.com/",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    {
        "id": 472,
        "title": "Minab school strike: civilian casualties reported — CNN / Iranian state media",
        "url": "https://www.cnn.com/",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2026,
    },
    {
        "id": 473,
        "title": "USS Abraham Lincoln and Gerald R. Ford CSGs in North Arabian Sea — CENTCOM",
        "url": "https://www.centcom.mil/",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 474,
        "title": "Iran retaliation targets Al Udeid Air Base, Qatar — CENTCOM",
        "url": "https://www.centcom.mil/",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 475,
        "title": "Islamic Revolutionary Guard Corps — Britannica",
        "url": "https://www.britannica.com/topic/Islamic-Revolutionary-Guard-Corps",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 476,
        "title": "Quds Force: Iran's expeditionary arm — CSIS",
        "url": "https://www.csis.org/",
        "source_type": "academic",
        "year": 2024,
    },
    {
        "id": 477,
        "title": "Iran's Axis of Resistance: Hezbollah, Houthis, and proxy networks — Atlantic Council",
        "url": "https://www.atlanticcouncil.org/",
        "source_type": "academic",
        "year": 2024,
    },
    {
        "id": 478,
        "title": "Natanz nuclear facility — IAEA / Britannica",
        "url": "https://www.britannica.com/",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 479,
        "title": "Fordow Fuel Enrichment Plant — IAEA technical report",
        "url": "https://www.iaea.org/",
        "source_type": "government",
        "year": 2024,
    },
    {
        "id": 480,
        "title": "Pezeshkian assumes presidential duties after Khamenei death — Al Jazeera",
        "url": "https://www.aljazeera.com/",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    {
        "id": 481,
        "title": "CENTCOM organizational structure — US Central Command",
        "url": "https://www.centcom.mil/ABOUT-US/",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 482,
        "title": "Iranian cyber retaliation targets US/Israeli infrastructure — CSIS",
        "url": "https://www.csis.org/",
        "source_type": "academic",
        "year": 2026,
    },
]


# ============================================================
# ENTITIES — ~24 new
# ============================================================

ENTITIES = [
    # --- Iranian leadership ---
    {
        "name": "Islamic Revolutionary Guard Corps",
        "entity_type": "agency",
        "description": (
            "Iran's primary paramilitary force, established 1979 after the Islamic Revolution. "
            "Reports directly to the Supreme Leader. Controls Iran's ballistic missile program "
            "(IRGC Aerospace Force), naval forces in the Persian Gulf (IRGC Navy), ground forces, "
            "and the Quds Force for external operations. Designated a Foreign Terrorist Organization "
            "by the US in 2019. IRGC leadership was systematically targeted in the opening strikes "
            "of Operation Epic Fury on February 28, 2026, with Commander-in-Chief Mohammad Pakpour "
            "killed at Parchin and multiple senior commanders eliminated."
        ),
        "aliases": "IRGC, Sepah, Pasdaran, Iranian Revolutionary Guards",
    },
    {
        "name": "Quds Force",
        "entity_type": "agency",
        "description": (
            "The extraterritorial operations arm of the IRGC, responsible for intelligence "
            "and unconventional warfare outside Iran's borders. Manages Iran's relationships "
            "with proxy forces including Hezbollah, Hamas, Palestinian Islamic Jihad, Iraqi "
            "Shia militias, and Ansar Allah (Houthis). Previously commanded by Qasem Soleimani "
            "(killed by US drone strike January 2020) and then Esmail Qaani. The Quds Force is "
            "the operational backbone of Iran's 'Axis of Resistance' strategy."
        ),
        "aliases": "IRGC-QF, Jerusalem Force, Niru-ye Qods",
    },
    {
        "name": "Ali Khamenei",
        "entity_type": "person",
        "description": (
            "Supreme Leader of Iran from 1989 until his death on February 28, 2026. Succeeded "
            "Ayatollah Ruhollah Khomeini as Iran's highest political and religious authority. "
            "Held ultimate command authority over all Iranian military forces including the IRGC. "
            "Killed in the opening strikes of Operation Epic Fury, which targeted his compound "
            "in Tehran. His death created a succession crisis, with President Masoud Pezeshkian "
            "assuming temporary executive authority."
        ),
        "aliases": "Ayatollah Khamenei, Seyyed Ali Hosseini Khamenei",
        "metadata": {"birth_year": 1939, "death_year": 2026, "nationality": "Iranian"},
    },
    {
        "name": "Ali Shamkhani",
        "entity_type": "person",
        "description": (
            "Senior Iranian security official who served as Secretary of the Supreme National "
            "Security Council (2013-2023). Former IRGC Navy commander and Minister of Defense. "
            "Key figure in Iran's security apparatus. Killed in strikes on the Ministry of "
            "Intelligence (MOIS) headquarters in Tehran on February 28, 2026."
        ),
        "aliases": "Shamkhani",
        "metadata": {"birth_year": 1955, "death_year": 2026, "nationality": "Iranian"},
    },
    {
        "name": "Mohammad Pakpour",
        "entity_type": "person",
        "description": (
            "Commander-in-Chief of the IRGC Ground Forces. Brigadier General. Killed in "
            "the US/Israeli strike on the Parchin Military Complex on February 28, 2026, "
            "during Operation Epic Fury."
        ),
        "aliases": "Pakpour",
        "metadata": {"death_year": 2026, "nationality": "Iranian"},
    },
    {
        "name": "Aziz Nasirzadeh",
        "entity_type": "person",
        "description": (
            "Iranian Defence Minister (Brigadier General). Former commander of the Islamic "
            "Republic of Iran Air Force. Killed in strikes on the Defense Ministry compound "
            "in Tehran on February 28, 2026, during Operation Epic Fury."
        ),
        "aliases": "Nasirzadeh",
        "metadata": {"death_year": 2026, "nationality": "Iranian"},
    },
    {
        "name": "Abdul Rahim Mousavi",
        "entity_type": "person",
        "description": (
            "Chief of Staff of the Iranian Armed Forces. Major General. Killed alongside "
            "Supreme Leader Khamenei in the strike on the Supreme Leader's compound in "
            "Tehran on February 28, 2026."
        ),
        "aliases": "Mousavi",
        "metadata": {"death_year": 2026, "nationality": "Iranian"},
    },
    {
        "name": "Masoud Pezeshkian",
        "entity_type": "person",
        "description": (
            "President of the Islamic Republic of Iran (elected 2024). Former heart surgeon "
            "and Member of Parliament. Considered a reformist. Assumed temporary executive "
            "authority following the death of Supreme Leader Khamenei on February 28, 2026, "
            "pending the Assembly of Experts' selection of a new Supreme Leader."
        ),
        "aliases": "Pezeshkian",
        "metadata": {"birth_year": 1954, "nationality": "Iranian"},
    },

    # --- US/Coalition ---
    {
        "name": "CENTCOM",
        "entity_type": "agency",
        "description": (
            "United States Central Command. Unified combatant command responsible for US "
            "military operations in the Middle East, Central Asia, and parts of South Asia. "
            "Headquartered at MacDill AFB, Tampa, FL with forward HQ at Al Udeid Air Base, "
            "Qatar. CENTCOM directed Operation Epic Fury against Iran on February 28, 2026, "
            "coordinating air, naval, and ground-based strike operations across the theater."
        ),
        "aliases": "US Central Command, USCENTCOM",
    },

    # --- Operations ---
    {
        "name": "Operation Epic Fury",
        "entity_type": "event",
        "description": (
            "US codename for the combined military operation against Iran launched on "
            "February 28, 2026. The largest regional concentration of American military "
            "firepower in a generation. Strikes targeted Iran's military command structure, "
            "IRGC facilities, air defenses, missile sites, and naval bases. B-2 stealth "
            "bombers flew round-trip missions from CONUS (Whiteman AFB) to deliver GBU-57 "
            "Massive Ordnance Penetrators on hardened underground targets. Supreme Leader "
            "Khamenei and multiple senior military leaders were killed in the opening salvo."
        ),
        "aliases": "Epic Fury",
    },
    {
        "name": "Operation Roaring Lion",
        "entity_type": "event",
        "description": (
            "Israeli codename for the parallel military operation against Iran conducted "
            "in coordination with US Operation Epic Fury on February 28, 2026. Israeli Air "
            "Force contributed strike aircraft targeting military facilities in Tehran, "
            "Isfahan, and other locations."
        ),
        "aliases": "Roaring Lion",
    },
    {
        "name": "Operation Midnight Hammer",
        "entity_type": "event",
        "description": (
            "US/Israeli codename for the June 2025 nuclear strikes on Iran's nuclear "
            "infrastructure. Targeted Natanz uranium enrichment facility, Fordow enrichment "
            "plant (built inside a mountain near Qom), and Isfahan Nuclear Technology Center. "
            "This operation set the context for the broader military escalation culminating "
            "in Operation Epic Fury in February 2026."
        ),
        "aliases": "Midnight Hammer",
    },
    {
        "name": "Strait of Hormuz Blockade",
        "entity_type": "event",
        "description": (
            "IRGC Navy declared closure of the Strait of Hormuz to all shipping on "
            "February 28, 2026, following the start of Operation Epic Fury. Mine-laying "
            "operations and fast attack craft deployed across shipping lanes. Approximately "
            "21% of global oil transit was affected. The blockade triggered immediate global "
            "energy market disruption."
        ),
        "aliases": "Hormuz Blockade, Strait of Hormuz Closure",
    },
    {
        "name": "B-2 Spirit Strike Package",
        "entity_type": "event",
        "description": (
            "Four B-2 Spirit stealth bombers from the 509th Bomb Wing launched from "
            "Whiteman Air Force Base, Missouri on a round-trip mission to Iran (~30 hours "
            "with aerial refueling). Delivered GBU-57 Massive Ordnance Penetrators (30,000 lb "
            "bunker busters) against hardened underground missile production and storage "
            "facilities in the Natanz and Fordow areas."
        ),
        "aliases": "B-2 Strike, CONUS Strike Package",
    },

    # --- Facilities ---
    {
        "name": "Natanz Nuclear Facility",
        "entity_type": "facility",
        "description": (
            "Iran's primary uranium enrichment facility, located in Isfahan province. Houses "
            "thousands of centrifuges for uranium enrichment, with facilities both above ground "
            "and in hardened underground halls. Previously targeted by the Stuxnet cyber weapon "
            "(2010) and by Israeli sabotage (2021). Struck in June 2025 during Operation "
            "Midnight Hammer and again during Operation Epic Fury in February 2026."
        ),
        "aliases": "Natanz, Natanz Enrichment Facility",
    },
    {
        "name": "Fordow Enrichment Plant",
        "entity_type": "facility",
        "description": (
            "Iran's secondary uranium enrichment facility, built deep inside a mountain near "
            "Qom. Revealed publicly in 2009. Designed to be resistant to aerial bombardment. "
            "Struck during Operation Midnight Hammer (June 2025) using bunker-buster munitions "
            "and again targeted by B-2 delivered GBU-57 MOPs during Operation Epic Fury "
            "(February 2026)."
        ),
        "aliases": "Fordow, Fordo",
    },
    {
        "name": "Parchin Military Complex",
        "entity_type": "facility",
        "description": (
            "Major Iranian military-industrial complex located southeast of Tehran. Used for "
            "weapons development, testing, and production. Subject to IAEA scrutiny over "
            "suspected nuclear weapons-related high-explosive testing. Struck during Operation "
            "Epic Fury on February 28, 2026. IRGC Ground Forces Commander Mohammad Pakpour "
            "was killed in the strikes on this facility."
        ),
        "aliases": "Parchin",
    },
    {
        "name": "Konarak Naval Base",
        "entity_type": "facility",
        "description": (
            "Iranian Navy (IRIN) base in southeastern Iran on the Gulf of Oman. Key naval "
            "facility for operations in the Arabian Sea and Gulf of Oman. Struck during "
            "Operation Epic Fury on February 28, 2026, with multiple vessels destroyed at berth."
        ),
        "aliases": "Konarak",
    },
    {
        "name": "USS Abraham Lincoln",
        "entity_type": "facility",
        "description": (
            "Nimitz-class aircraft carrier (CVN-72). Flagship of Carrier Strike Group 3, "
            "operating in the North Arabian Sea during Operation Epic Fury. Provided air "
            "support and fleet defense during the February 2026 strikes on Iran."
        ),
        "aliases": "CVN-72, Abraham Lincoln CSG",
    },
    {
        "name": "USS Gerald R. Ford",
        "entity_type": "facility",
        "description": (
            "Gerald R. Ford-class aircraft carrier (CVN-78), the most advanced warship in "
            "the US Navy. Flagship of Carrier Strike Group 12, positioned in the Gulf of "
            "Oman during Operation Epic Fury. Together with CVN-72, represented the largest "
            "concentration of American carrier aviation in the region in a generation."
        ),
        "aliases": "CVN-78, Ford CSG",
    },

    # --- Proxy organizations ---
    {
        "name": "Hezbollah",
        "entity_type": "organization",
        "description": (
            "Lebanese Shia political party and paramilitary organization. Iran's most capable "
            "proxy force, armed and funded by the IRGC Quds Force since the 1980s. Designated "
            "a terrorist organization by the US, EU, and others. Launched retaliatory rocket "
            "and drone barrages against northern Israel in solidarity with Iran following "
            "Operation Epic Fury on March 1, 2026."
        ),
        "aliases": "Hizballah, Party of God",
    },
    {
        "name": "Ansar Allah (Houthis)",
        "entity_type": "organization",
        "description": (
            "Yemeni Shia rebel movement, part of Iran's 'Axis of Resistance.' Armed and "
            "supported by the IRGC Quds Force. Escalated attacks on commercial shipping in "
            "the Red Sea and Bab el-Mandeb strait in solidarity with Iran following Operation "
            "Epic Fury, disrupting global maritime trade."
        ),
        "aliases": "Houthis, Ansar Allah, Ansarallah",
    },

    # --- Iranian agencies ---
    {
        "name": "Atomic Energy Organization of Iran",
        "entity_type": "agency",
        "description": (
            "Iran's civilian nuclear energy agency (AEOI), headquartered in Tehran. Oversees "
            "Iran's nuclear program including enrichment facilities at Natanz and Fordow. "
            "AEOI headquarters in Tehran was struck during Operation Epic Fury on "
            "February 28, 2026."
        ),
        "aliases": "AEOI",
    },
    {
        "name": "Iranian Ministry of Intelligence",
        "entity_type": "agency",
        "description": (
            "Iran's primary civilian intelligence agency (MOIS / VEVAK). Responsible for "
            "domestic security, counterintelligence, and foreign intelligence collection. "
            "MOIS headquarters in Tehran was struck during Operation Epic Fury on "
            "February 28, 2026. Secretary Ali Shamkhani was among those killed."
        ),
        "aliases": "MOIS, VEVAK, Vezarat-e Ettela'at",
    },
]


# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ================================================================
    # OPERATIONAL CHAINS — CENTCOM → Epic Fury → targets
    # ================================================================
    {
        "source": "CENTCOM",
        "target": "Operation Epic Fury",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "CENTCOM directed and coordinated Operation Epic Fury, the combined US military "
            "operation against Iran launched February 28, 2026."
        ),
        "sources": [453, 481],
    },
    {
        "source": "Operation Epic Fury",
        "target": "Parchin Military Complex",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Parchin Military Complex was a primary target of Operation Epic Fury strikes "
            "on February 28, 2026. IRGC commander Pakpour killed."
        ),
        "sources": [453, 461],
    },
    {
        "source": "Operation Epic Fury",
        "target": "Konarak Naval Base",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Konarak Naval Base was struck during Operation Epic Fury, with multiple "
            "IRIN vessels destroyed at berth."
        ),
        "sources": [453, 458],
    },
    {
        "source": "Operation Epic Fury",
        "target": "Natanz Nuclear Facility",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "B-2 bombers delivered GBU-57 MOPs against underground facilities in the "
            "Natanz area during Epic Fury."
        ),
        "sources": [453, 462],
    },
    {
        "source": "Operation Epic Fury",
        "target": "Fordow Enrichment Plant",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Hardened mountain facilities near Fordow targeted by B-2 delivered "
            "bunker-buster munitions during Epic Fury."
        ),
        "sources": [453, 462],
    },
    {
        "source": "Operation Roaring Lion",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Israel's Operation Roaring Lion was conducted in parallel with and as part "
            "of the joint US-Israeli strike operation. Israeli Air Force contributed strike "
            "aircraft to the combined package."
        ),
        "sources": [453, 463],
    },
    {
        "source": "Operation Roaring Lion",
        "target": "Mossad",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Mossad intelligence supported targeting for Operation Roaring Lion, Israel's "
            "parallel strike operation against Iran."
        ),
        "sources": [463],
    },
    {
        "source": "B-2 Spirit Strike Package",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The B-2 strike package (4 bombers from Whiteman AFB) was a component of "
            "Operation Epic Fury, delivering GBU-57 MOPs against hardened underground targets."
        ),
        "sources": [453, 462],
    },

    # ================================================================
    # LEADERSHIP HIERARCHY & DECAPITATION
    # ================================================================
    {
        "source": "Ali Khamenei",
        "target": "Islamic Revolutionary Guard Corps",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "As Supreme Leader, Khamenei held ultimate command authority over the IRGC. "
            "The IRGC reports directly to the Supreme Leader, not the president or parliament."
        ),
        "sources": [475, 457],
    },
    {
        "source": "Ali Khamenei",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Khamenei was killed in the opening strikes of Operation Epic Fury on "
            "February 28, 2026, in a decapitation strike on his compound."
        ),
        "sources": [453, 457],
    },
    {
        "source": "Abdul Rahim Mousavi",
        "target": "Ali Khamenei",
        "type": "directed_by",
        "tier": "documented",
        "desc": (
            "As Chief of Staff of the Armed Forces, Mousavi served under Khamenei's "
            "command. Killed alongside Khamenei in the same strike."
        ),
        "sources": [453, 457],
    },
    {
        "source": "Mohammad Pakpour",
        "target": "Islamic Revolutionary Guard Corps",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Commander-in-Chief of the IRGC Ground Forces. Killed in strikes on "
            "Parchin Military Complex during Epic Fury."
        ),
        "sources": [453, 461],
    },
    {
        "source": "Aziz Nasirzadeh",
        "target": "Ali Khamenei",
        "type": "directed_by",
        "tier": "documented",
        "desc": (
            "As Defence Minister, Nasirzadeh served in the Iranian cabinet under the "
            "Supreme Leader's authority. Killed in Defense Ministry strike."
        ),
        "sources": [453, 467],
    },
    {
        "source": "Ali Shamkhani",
        "target": "Iranian Ministry of Intelligence",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Senior security official killed in strikes on MOIS headquarters. Previously "
            "served as Secretary of the Supreme National Security Council."
        ),
        "sources": [453, 467],
    },
    {
        "source": "Masoud Pezeshkian",
        "target": "Ali Khamenei",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As president, Pezeshkian assumed temporary executive authority following "
            "Khamenei's death, pending Assembly of Experts selection of new Supreme Leader."
        ),
        "sources": [480],
    },

    # ================================================================
    # IRGC → PROXY NETWORKS (Axis of Resistance)
    # ================================================================
    {
        "source": "Quds Force",
        "target": "Islamic Revolutionary Guard Corps",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The Quds Force is the extraterritorial operations branch of the IRGC, "
            "responsible for managing Iran's proxy network."
        ),
        "sources": [475, 476],
    },
    {
        "source": "Quds Force",
        "target": "Hezbollah",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "IRGC Quds Force arms, funds, and provides operational guidance to Hezbollah. "
            "Relationship dates to Hezbollah's founding in the 1980s."
        ),
        "sources": [476, 477],
    },
    {
        "source": "Quds Force",
        "target": "Ansar Allah (Houthis)",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "IRGC Quds Force provides weapons, training, and financial support to "
            "Ansar Allah. Houthi drone and missile capabilities reflect Iranian technology transfer."
        ),
        "sources": [476, 477],
    },
    {
        "source": "Hezbollah",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Hezbollah launched retaliatory barrages against northern Israel in solidarity "
            "with Iran following Operation Epic Fury, as part of the 'Axis of Resistance' response."
        ),
        "sources": [469],
    },
    {
        "source": "Ansar Allah (Houthis)",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Houthis escalated attacks on commercial shipping in the Red Sea in solidarity "
            "with Iran following Operation Epic Fury."
        ),
        "sources": [468],
    },

    # ================================================================
    # RETALIATION CHAINS
    # ================================================================
    {
        "source": "Islamic Revolutionary Guard Corps",
        "target": "Strait of Hormuz Blockade",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "IRGC Navy declared and enforced the closure of the Strait of Hormuz "
            "following the start of Epic Fury, deploying mines and fast attack craft."
        ),
        "sources": [455, 458],
    },
    {
        "source": "Islamic Revolutionary Guard Corps",
        "target": "CENTCOM",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "IRGC launched retaliatory missile and drone strikes against 27 US bases "
            "across the region, including CENTCOM's forward HQ at Al Udeid, Qatar."
        ),
        "sources": [454, 474],
    },

    # ================================================================
    # NUCLEAR FACILITIES & PRIOR CONTEXT
    # ================================================================
    {
        "source": "Operation Midnight Hammer",
        "target": "Natanz Nuclear Facility",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Natanz was struck during Operation Midnight Hammer in June 2025, "
            "the nuclear strikes that preceded Epic Fury."
        ),
        "sources": [465, 466],
    },
    {
        "source": "Operation Midnight Hammer",
        "target": "Fordow Enrichment Plant",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Fordow's mountain facility was struck during Operation Midnight Hammer "
            "in June 2025."
        ),
        "sources": [465, 466],
    },
    {
        "source": "Operation Midnight Hammer",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Operation Midnight Hammer (June 2025 nuclear strikes) set the context "
            "for the broader escalation culminating in Operation Epic Fury (February 2026)."
        ),
        "sources": [465, 453],
    },
    {
        "source": "Atomic Energy Organization of Iran",
        "target": "Natanz Nuclear Facility",
        "type": "directed",
        "tier": "documented",
        "desc": "AEOI oversees Natanz as part of Iran's civilian nuclear program.",
        "sources": [471, 478],
    },
    {
        "source": "Atomic Energy Organization of Iran",
        "target": "Fordow Enrichment Plant",
        "type": "directed",
        "tier": "documented",
        "desc": "AEOI oversees Fordow enrichment operations.",
        "sources": [471, 479],
    },

    # ================================================================
    # NAVAL OPERATIONS
    # ================================================================
    {
        "source": "USS Abraham Lincoln",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "CVN-72 CSG provided air support and fleet defense from the North Arabian Sea "
            "during Operation Epic Fury."
        ),
        "sources": [453, 473],
    },
    {
        "source": "USS Gerald R. Ford",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "CVN-78 CSG positioned in the Gulf of Oman, part of the largest carrier "
            "aviation concentration in the region in a generation."
        ),
        "sources": [453, 473],
    },
    {
        "source": "USS Abraham Lincoln",
        "target": "CENTCOM",
        "type": "directed_by",
        "tier": "documented",
        "desc": "CSG 3 operated under CENTCOM operational control during Epic Fury.",
        "sources": [453, 481],
    },
    {
        "source": "USS Gerald R. Ford",
        "target": "CENTCOM",
        "type": "directed_by",
        "tier": "documented",
        "desc": "CSG 12 operated under CENTCOM operational control during Epic Fury.",
        "sources": [453, 481],
    },

    # ================================================================
    # CROSS-CUTTING — connections to existing intel-console entities
    # ================================================================
    {
        "source": "CENTCOM",
        "target": "CIA",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "CIA provides intelligence support to CENTCOM operations. CIA targeting "
            "intelligence supported strike planning for Epic Fury."
        ),
        "sources": [453, 481],
    },
    {
        "source": "Iranian Ministry of Intelligence",
        "target": "Islamic Revolutionary Guard Corps",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "MOIS and IRGC are parallel but sometimes competing pillars of Iran's "
            "security apparatus, both reporting to the Supreme Leader."
        ),
        "sources": [475],
    },
    {
        "source": "Operation Midnight Hammer",
        "target": "Mossad",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Mossad intelligence on Iran's nuclear program supported targeting for "
            "Operation Midnight Hammer, building on decades of Israeli intelligence "
            "operations against Iran's nuclear infrastructure."
        ),
        "sources": [465, 463],
    },
    {
        "source": "Islamic Revolutionary Guard Corps",
        "target": "Iran-Contra",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The IRGC was the Iranian counterpart in the Iran-Contra arms deals of the "
            "1980s. Arms-for-hostages negotiations ran through IRGC-connected channels."
        ),
        "sources": [475],
    },
]


# ============================================================
# ENTITY → SOURCE links
# ============================================================

ENTITY_SOURCES = {
    "Islamic Revolutionary Guard Corps": [453, 454, 455, 467, 475],
    "Quds Force": [476, 477],
    "Ali Khamenei": [453, 457, 467],
    "Ali Shamkhani": [453, 467],
    "Mohammad Pakpour": [453, 461],
    "Aziz Nasirzadeh": [453, 467],
    "Abdul Rahim Mousavi": [453, 457],
    "Masoud Pezeshkian": [480],
    "CENTCOM": [453, 481],
    "Operation Epic Fury": [453, 454, 456, 458, 459, 460],
    "Operation Roaring Lion": [463],
    "Operation Midnight Hammer": [465, 466],
    "Strait of Hormuz Blockade": [455, 458, 464],
    "B-2 Spirit Strike Package": [453, 462],
    "Natanz Nuclear Facility": [465, 466, 478],
    "Fordow Enrichment Plant": [465, 466, 479],
    "Parchin Military Complex": [453, 461],
    "Konarak Naval Base": [453, 458],
    "USS Abraham Lincoln": [453, 473],
    "USS Gerald R. Ford": [453, 473],
    "Hezbollah": [469, 477],
    "Ansar Allah (Houthis)": [468, 477],
    "Atomic Energy Organization of Iran": [471, 478],
    "Iranian Ministry of Intelligence": [453, 467],
}
