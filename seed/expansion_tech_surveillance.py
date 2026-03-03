"""
Tech Surveillance — Mass Surveillance Infrastructure — Expansion layer for Intel Console.

Maps the architecture of mass surveillance: the NSA/GCHQ programs exposed by
Edward Snowden and earlier whistleblowers, the Five Eyes alliance, the corporate
surveillance pipeline (AT&T, Palantir, In-Q-Tel), the CIA's hacking arsenal
(Vault 7), and the legal/legislative battles over warrantless surveillance.

This is the operational layer of the intelligence map — not who controls the
system, but what the system can actually do to any person on earth.

Entities (~20): Programs (XKeyscore, ECHELON, Room 641A, Vault 7, MYSTIC,
Tempora, Carnivore/DCS1000, ThinThread), alliances (Five Eyes), agencies (GCHQ),
people (Thomas Drake, Mark Klein, Keith Alexander), legislation (USA FREEDOM Act,
FISA Amendments Act), court cases (Jewel v. NSA, ACLU v. Clapper).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], NSA [86], FBI [84], DARPA [90], Mossad [88],
  Edward Snowden [321], William Binney [322], Peter Thiel [30],
  Palantir Technologies [59], In-Q-Tel [60], Alex Karp [31],
  PRISM [media], Stellar Wind [911], USA PATRIOT Act [911],
  Church Committee [338], WikiLeaks [media], Booz Allen Hamilton [mic],
  MI5 [uk], MI6 [uk], NSO Group [israel], Unit 8200 [israel],
  George W. Bush [grove]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 931-960
# ============================================================

SOURCES = [
    # --- Snowden Archive / NSA Programs ---
    {
        "id": 931,
        "title": "Glenn Greenwald — No Place to Hide: Edward Snowden, the NSA, and the U.S. Surveillance State",
        "url": "https://en.wikipedia.org/wiki/No_Place_to_Hide_(Greenwald_book)",
        "source_type": "book",
        "author": "Glenn Greenwald",
        "year": 2014,
    },
    {
        "id": 932,
        "title": "The Guardian — XKeyscore: NSA tool collects 'nearly everything a user does on the internet'",
        "url": "https://www.theguardian.com/world/2013/jul/31/nsa-top-secret-program-online-data",
        "source_type": "journalism",
        "author": "Glenn Greenwald",
        "year": 2013,
    },
    {
        "id": 933,
        "title": "The Intercept — NSA's MYSTIC program records every cell phone call in entire countries",
        "url": "https://theintercept.com/2014/05/19/data-pirates-caribbean-nsa-recording-every-cell-phone-call-bahamas/",
        "source_type": "journalism",
        "author": "Ryan Devereaux, Glenn Greenwald, Laura Poitras",
        "year": 2014,
    },
    # --- ECHELON / Five Eyes ---
    {
        "id": 934,
        "title": "European Parliament — Report on the existence of a global system for the interception of private and commercial communications (ECHELON)",
        "url": "https://www.europarl.europa.eu/sides/getDoc.do?pubRef=-//EP//TEXT+REPORT+A5-2001-0264+0+DOC+XML+V0//EN",
        "source_type": "government",
        "year": 2001,
    },
    {
        "id": 935,
        "title": "James Bamford — The Shadow Factory: The NSA from 9/11 to the Eavesdropping on America",
        "url": "https://en.wikipedia.org/wiki/The_Shadow_Factory",
        "source_type": "book",
        "author": "James Bamford",
        "year": 2008,
    },
    {
        "id": 936,
        "title": "James Bamford — Body of Secrets: Anatomy of the Ultra-Secret National Security Agency",
        "url": "https://en.wikipedia.org/wiki/Body_of_Secrets",
        "source_type": "book",
        "author": "James Bamford",
        "year": 2001,
    },
    {
        "id": 937,
        "title": "UKUSA Agreement declassified — full text of 1946 signals intelligence pact (released 2010)",
        "url": "https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/ukusa/ukusa_comint_agree.pdf",
        "source_type": "government",
        "year": 1946,
    },
    # --- Room 641A / AT&T ---
    {
        "id": 938,
        "title": "Mark Klein — Wiring Up the Big Brother Machine... And Fighting It (AT&T whistleblower memoir)",
        "url": "https://en.wikipedia.org/wiki/Room_641A",
        "source_type": "book",
        "author": "Mark Klein",
        "year": 2009,
    },
    {
        "id": 939,
        "title": "Wired — NSA's Domestic Spying Grows as Agency Sweeps Up Data (Room 641A / AT&T)",
        "url": "https://www.wired.com/2006/05/nsa-2/",
        "source_type": "journalism",
        "author": "Ryan Singel",
        "year": 2006,
    },
    {
        "id": 940,
        "title": "EFF — Jewel v. NSA: challenging NSA's warrantless wiretapping of millions of Americans",
        "url": "https://www.eff.org/cases/jewel",
        "source_type": "court",
        "year": 2008,
    },
    # --- Vault 7 / CIA Hacking ---
    {
        "id": 941,
        "title": "WikiLeaks — Vault 7: CIA hacking tools (Year Zero release, 8,761 documents)",
        "url": "https://wikileaks.org/ciav7p1/",
        "source_type": "archive",
        "year": 2017,
    },
    {
        "id": 942,
        "title": "Washington Post — WikiLeaks publishes CIA trove alleging wide-scale hacking (Vault 7 analysis)",
        "url": "https://www.washingtonpost.com/world/national-security/wikileaks-says-it-has-obtained-trove-of-cia-hacking-tools/2017/03/07/c8c50c5c-0345-11e7-b1e9-a76d3a32f60a_story.html",
        "source_type": "journalism",
        "year": 2017,
    },
    # --- Tempora / GCHQ ---
    {
        "id": 943,
        "title": "The Guardian — GCHQ taps fibre-optic cables for secret access to world's communications (Tempora)",
        "url": "https://www.theguardian.com/uk/2013/jun/21/gchq-cables-secret-world-communications-nsa",
        "source_type": "journalism",
        "author": "Ewen MacAskill, Julian Borger, Nick Hopkins, Nick Davies, James Ball",
        "year": 2013,
    },
    {
        "id": 944,
        "title": "The Guardian — GCHQ: inside the top secret world of Britain's biggest spy agency",
        "url": "https://www.theguardian.com/world/2013/aug/02/gchq-spy-agency-nsa-snowden",
        "source_type": "journalism",
        "year": 2013,
    },
    # --- Carnivore / FBI ---
    {
        "id": 945,
        "title": "EPIC (Electronic Privacy Information Center) — Carnivore / DCS1000 FOIA documents",
        "url": "https://epic.org/privacy/carnivore/",
        "source_type": "foia",
        "year": 2000,
    },
    {
        "id": 946,
        "title": "IIT Research Institute — Independent Technical Review of the Carnivore System (DOJ-commissioned)",
        "url": "https://www.justice.gov/archive/jmd/publications/carnivore_draft_1.pdf",
        "source_type": "government",
        "year": 2000,
    },
    # --- Thomas Drake / ThinThread ---
    {
        "id": 947,
        "title": "Jane Mayer — 'The Secret Sharer: Is Thomas Drake an enemy of the state?' (The New Yorker)",
        "url": "https://www.newyorker.com/magazine/2011/05/23/the-secret-sharer",
        "source_type": "journalism",
        "author": "Jane Mayer",
        "year": 2011,
    },
    {
        "id": 948,
        "title": "DOJ — United States v. Thomas Andrews Drake (indictment under Espionage Act, 2010)",
        "url": "https://fas.org/sgp/jud/drake/indict.pdf",
        "source_type": "court",
        "year": 2010,
    },
    # --- Keith Alexander / NSA ---
    {
        "id": 949,
        "title": "Foreign Policy — 'The Cowboy of the NSA' (Keith Alexander profile)",
        "url": "https://foreignpolicy.com/2013/09/09/the-cowboy-of-the-nsa/",
        "source_type": "journalism",
        "author": "Shane Harris",
        "year": 2013,
    },
    {
        "id": 950,
        "title": "Senate Judiciary Committee — Oversight of the Foreign Intelligence Surveillance Act (Keith Alexander testimony)",
        "url": "https://www.judiciary.senate.gov/meetings/oversight-of-the-foreign-intelligence-surveillance-act",
        "source_type": "congressional",
        "year": 2013,
    },
    # --- USA FREEDOM Act ---
    {
        "id": 951,
        "title": "Congress.gov — USA FREEDOM Act (H.R. 2048, 114th Congress, signed June 2, 2015)",
        "url": "https://www.congress.gov/bill/114th-congress/house-bill/2048",
        "source_type": "congressional",
        "year": 2015,
    },
    # --- FISA Amendments Act / Section 702 ---
    {
        "id": 952,
        "title": "Congress.gov — FISA Amendments Act of 2008 (H.R. 6304, 110th Congress)",
        "url": "https://www.congress.gov/bill/110th-congress/house-bill/6304",
        "source_type": "congressional",
        "year": 2008,
    },
    # --- ACLU v. Clapper ---
    {
        "id": 953,
        "title": "ACLU — ACLU v. Clapper: challenging NSA mass phone surveillance (Second Circuit ruling)",
        "url": "https://www.aclu.org/cases/aclu-v-clapper",
        "source_type": "court",
        "year": 2015,
    },
    # --- James Bamford — The Puzzle Palace (ECHELON precursors) ---
    {
        "id": 954,
        "title": "James Bamford — The Puzzle Palace: Inside the National Security Agency",
        "url": "https://en.wikipedia.org/wiki/The_Puzzle_Palace",
        "source_type": "book",
        "author": "James Bamford",
        "year": 1982,
    },
    # --- PCLOB Section 215 Report ---
    {
        "id": 955,
        "title": "Privacy and Civil Liberties Oversight Board — Report on the Telephone Records Program under Section 215",
        "url": "https://documents.pclob.gov/prod/Documents/OversightReport/ec542143-1079-424a-84b3-acc354698560/215-Report_on_the_Telephone_Records_Program.pdf",
        "source_type": "government",
        "year": 2014,
    },
    # --- Snowden documentary ---
    {
        "id": 956,
        "title": "Laura Poitras — Citizenfour (documentary, Academy Award 2015)",
        "url": "https://en.wikipedia.org/wiki/Citizenfour",
        "source_type": "documentary",
        "author": "Laura Poitras",
        "year": 2014,
    },
    # --- Barton Gellman / Dark Mirror ---
    {
        "id": 957,
        "title": "Barton Gellman — Dark Mirror: Edward Snowden and the American Surveillance State",
        "url": "https://en.wikipedia.org/wiki/Dark_Mirror_(book)",
        "source_type": "book",
        "author": "Barton Gellman",
        "year": 2020,
    },
    # --- Senate Intelligence Committee report on CIA torture/surveillance overlap ---
    {
        "id": 958,
        "title": "Senate Select Committee on Intelligence — Study of the CIA's Detention and Interrogation Program (executive summary)",
        "url": "https://www.intelligence.senate.gov/publications/committee-study-central-intelligence-agencys-detention-and-interrogation-program",
        "source_type": "congressional",
        "year": 2014,
    },
    # --- Duncan Campbell / ECHELON journalism ---
    {
        "id": 959,
        "title": "Duncan Campbell — 'Somebody's Listening' (first ECHELON exposé, New Statesman, 1988)",
        "url": "https://www.duncancampbell.org/content/echelon",
        "source_type": "journalism",
        "author": "Duncan Campbell",
        "year": 1988,
    },
    # --- Nicky Hager / Secret Power ---
    {
        "id": 960,
        "title": "Nicky Hager — Secret Power: New Zealand's Role in the International Spy Network",
        "url": "https://en.wikipedia.org/wiki/Secret_Power_(book)",
        "source_type": "book",
        "author": "Nicky Hager",
        "year": 1996,
    },
]

# ============================================================
# ENTITIES — ~20 new (do NOT duplicate existing)
# ============================================================

ENTITIES = [

    # ============ PROGRAMS ============

    {
        "name": "XKeyscore",
        "entity_type": "program",
        "description": (
            "NSA's most comprehensive internet surveillance tool, described internally as "
            "the agency's 'Google for surveillance.' Revealed by Edward Snowden documents "
            "published in The Guardian (July 2013). Allows analysts to search, with no "
            "prior authorization, through vast databases of emails, online chats, browsing "
            "histories, metadata, and the content of online activity collected from over "
            "700 servers at 150 worldwide sites. Training materials stated analysts could "
            "search 'nearly everything a typical user does on the internet.' Operated under "
            "Executive Order 12333 and Section 702 of the FISA Amendments Act. Shared with "
            "Five Eyes partners including GCHQ, ASD (Australia), GCSB (New Zealand), and CSE "
            "(Canada). James Bamford described it as the final piece in the NSA's total "
            "surveillance architecture — the search engine sitting atop the collection."
        ),
        "aliases": "XKEYSCORE, XKS",
        "metadata": {"type": "surveillance program", "years_active": "2008-present"},
    },
    {
        "name": "ECHELON",
        "entity_type": "program",
        "description": (
            "Global signals intelligence collection and analysis network operated by the "
            "Five Eyes alliance (NSA, GCHQ, CSE, ASD, GCSB). Originally established during "
            "the Cold War to monitor Soviet military and diplomatic communications. First "
            "publicly exposed by journalist Duncan Campbell in 1988 ('Somebody's Listening') "
            "and detailed by New Zealand journalist Nicky Hager in 'Secret Power' (1996). The "
            "European Parliament conducted a formal investigation (2001 Temporary Committee "
            "on the ECHELON Interception System) and confirmed its existence, concluding that "
            "ECHELON was used not only for military intelligence but for commercial espionage "
            "against European companies. The system intercepts satellite communications, "
            "microwave links, and fiber optic cables using ground stations including Menwith "
            "Hill (UK), Pine Gap (Australia), Waihopai (NZ), and Sugar Grove (US). Automated "
            "keyword filtering ('Dictionary' systems) processes intercepted communications "
            "at scale. ECHELON represents the Five Eyes signals intelligence backbone that "
            "predates and underpins the programs Snowden later revealed."
        ),
        "aliases": "ECHELON System, Five Eyes SIGINT Network",
        "metadata": {"type": "intelligence network", "years_active": "1966-present"},
    },
    {
        "name": "Room 641A",
        "entity_type": "facility",
        "description": (
            "Secret room at AT&T's Folsom Street switching facility in San Francisco, "
            "exposed by AT&T technician Mark Klein in 2006. The room contained a Narus "
            "STA 6400 beam splitter installed in 2003 that copied all internet traffic "
            "passing through AT&T's fiber optic backbone — including domestic communications "
            "— and routed it to NSA equipment. Klein's sworn declaration described the "
            "physical setup: fiber optic splitter cables running from the main trunk lines "
            "into a sealed room accessible only to personnel with NSA clearance. Klein "
            "provided his evidence to the EFF, which used it in the Jewel v. NSA lawsuit "
            "(filed 2008). The facility demonstrated that NSA's domestic surveillance was "
            "not targeted but rather a wholesale tap of the American internet backbone. "
            "AT&T received retroactive legal immunity through the FISA Amendments Act of "
            "2008. Similar rooms were reportedly installed at other AT&T facilities in "
            "Seattle, San Jose, Los Angeles, and San Diego."
        ),
        "aliases": "AT&T Room 641A, SG3 Secure Room",
        "metadata": {"location": "611 Folsom Street, San Francisco", "years_active": "2003-present"},
    },
    {
        "name": "Vault 7",
        "entity_type": "program",
        "description": (
            "Series of CIA hacking tools and documents leaked by WikiLeaks beginning "
            "March 7, 2017. The initial 'Year Zero' release comprised 8,761 documents "
            "from the CIA's Center for Cyber Intelligence (CCI) in Langley, Virginia. "
            "Revealed that the CIA had developed malware, viruses, trojans, weaponized "
            "'zero-day' exploits, and remote control systems targeting iPhones, Android "
            "phones, Samsung smart TVs (Weeping Angel — joint with MI5), Windows, macOS, "
            "Linux, and internet routers. The 'Marble' tool framework could disguise CIA "
            "hacking to appear as if conducted by Russia, China, North Korea, Iran, or "
            "Arabic-speaking actors. The leak revealed the CIA had lost control of the "
            "majority of its hacking arsenal. Former CIA software engineer Joshua Schulte "
            "was convicted in 2022 for the leak. The scale of the arsenal — with the CIA "
            "developing its own signals intelligence capability parallel to NSA — raised "
            "questions about interagency redundancy and oversight."
        ),
        "aliases": "Vault7, CIA Hacking Tools, Year Zero",
        "metadata": {"type": "cyber operations", "years_active": "2013-2017"},
    },
    {
        "name": "MYSTIC",
        "entity_type": "program",
        "description": (
            "NSA program capable of recording 100 percent of a foreign country's telephone "
            "calls and storing them for 30 days for retroactive retrieval. Revealed by "
            "Snowden documents published by The Intercept (2014). The companion program "
            "RETRO (Retrospective Retrieval) allowed analysts to rewind and listen to any "
            "call made in the target country during the storage window. The Intercept "
            "initially withheld the names of target countries at the request of U.S. "
            "officials; later reporting identified the Bahamas and Afghanistan. The program "
            "demonstrated that the NSA had achieved the capability to record every phone "
            "call in an entire nation — a technical capacity that, once built, could be "
            "deployed against any country, including domestically."
        ),
        "aliases": "MYSTIC/RETRO",
        "metadata": {"type": "surveillance program", "years_active": "2009-present"},
    },
    {
        "name": "Tempora",
        "entity_type": "program",
        "description": (
            "GCHQ program that taps transatlantic fiber optic cables to intercept internet "
            "and telephone traffic at massive scale. Revealed by Snowden documents published "
            "in The Guardian (June 2013). Tempora placed intercept probes on over 200 fiber "
            "optic cables landing in the UK, each carrying 10 gigabits per second — giving "
            "GCHQ access to roughly 21 petabytes of data per day. Content was stored for "
            "3 days and metadata for 30 days. GCHQ shared the take with the NSA — the "
            "arrangement allowed the NSA to access data on communications transiting UK "
            "infrastructure that would be more legally constrained to collect domestically. "
            "By 2012, GCHQ had the largest internet surveillance program of any Five Eyes "
            "partner. Operated under Section 8(4) of RIPA (Regulation of Investigatory "
            "Powers Act 2000), which authorizes interception of 'external' communications — "
            "a broad category that encompasses most internet traffic passing through UK cables."
        ),
        "aliases": "GCHQ Tempora",
        "metadata": {"type": "surveillance program", "years_active": "2011-present"},
    },
    {
        "name": "Carnivore",
        "entity_type": "program",
        "description": (
            "FBI internet surveillance system deployed from 1997, officially renamed "
            "DCS1000 (Digital Collection System) in 2001 after public backlash. Installed "
            "at ISP facilities to monitor email and internet traffic of surveillance targets. "
            "The system was a customized packet sniffer running on Windows that could filter "
            "network traffic by IP address, email address, protocol, or content. An "
            "independent review commissioned by the DOJ (IIT Research Institute, 2000) "
            "found that Carnivore's broad filtering capabilities created the risk of "
            "overcollection — capturing communications of non-targets. The EPIC (Electronic "
            "Privacy Information Center) obtained documents through FOIA showing the FBI "
            "deployed Carnivore without adequate judicial oversight in multiple cases. "
            "Replaced by commercial software around 2005, though the underlying capability "
            "— ISP-level packet interception — continued under National Security Letters "
            "and Section 215 orders."
        ),
        "aliases": "DCS1000, Digital Collection System 1000",
        "metadata": {"type": "surveillance program", "years_active": "1997-2005"},
    },
    {
        "name": "ThinThread",
        "entity_type": "program",
        "description": (
            "NSA signals intelligence program designed by William Binney and colleagues "
            "in the late 1990s. ThinThread could analyze massive volumes of communications "
            "data while automatically encrypting the identities of U.S. persons — a built-in "
            "privacy protection that required a court order to unmask. After 9/11, NSA "
            "Director Michael Hayden killed ThinThread in favor of the Trailblazer Project "
            "(a $1.2 billion contractor-driven program that ultimately failed) and the "
            "warrantless Stellar Wind program, which stripped out ThinThread's privacy "
            "safeguards. Thomas Drake, who tried to report the waste and illegality through "
            "official channels, was prosecuted under the Espionage Act. The DOD Inspector "
            "General's report (2004) confirmed ThinThread was technically superior and far "
            "cheaper than Trailblazer. The decision to kill ThinThread and choose warrantless "
            "mass collection was, as Binney has testified, a deliberate policy choice — not "
            "a technical one."
        ),
        "aliases": "Thin Thread",
        "metadata": {"type": "surveillance program", "years_active": "1999-2001"},
    },

    # ============ ORGANIZATIONS / ALLIANCES ============

    {
        "name": "Five Eyes",
        "entity_type": "organization",
        "description": (
            "Intelligence alliance comprising the United States (NSA), United Kingdom (GCHQ), "
            "Canada (CSE), Australia (ASD), and New Zealand (GCSB). Formalized by the UKUSA "
            "Agreement signed in 1946 (declassified in 2010), building on the BRUSA Agreement "
            "of 1943. The five nations agree to collect, analyze, and share signals intelligence, "
            "and — crucially — to not spy on each other's citizens. In practice, Snowden "
            "documents revealed that Five Eyes members spy on each other's populations and "
            "share the results, thereby circumventing domestic legal restrictions on surveillance. "
            "ECHELON was the Five Eyes' original global interception system. The alliance extends "
            "beyond SIGINT to include HUMINT, defense, and cybersecurity cooperation. Secondary "
            "rings include Nine Eyes (+Denmark, France, Netherlands, Norway) and Fourteen Eyes "
            "(+Germany, Belgium, Italy, Spain, Sweden). The Five Eyes structure means that "
            "programs like PRISM (NSA) and Tempora (GCHQ) are not isolated national capabilities "
            "but components of a single, integrated global surveillance system."
        ),
        "aliases": "FVEY, Five Eyes Alliance, UKUSA, Anglosphere Intelligence Alliance",
        "metadata": {"type": "intelligence alliance", "years_active": "1946-present"},
    },
    {
        "name": "GCHQ",
        "entity_type": "agency",
        "description": (
            "Government Communications Headquarters — the United Kingdom's signals intelligence "
            "and information assurance agency, headquartered in Cheltenham, Gloucestershire. "
            "Successor to the Government Code and Cypher School (GC&CS) at Bletchley Park, "
            "which broke the Enigma cipher in WWII. GCHQ is the UK's equivalent of the NSA "
            "and a core member of the Five Eyes alliance. Snowden documents (2013) revealed "
            "that GCHQ operated Tempora — tapping over 200 transatlantic fiber optic cables "
            "and sharing the take with the NSA. GCHQ also developed tools for mass social "
            "media manipulation (JTRIG — Joint Threat Research Intelligence Group) and "
            "collaborated with the NSA on XKeyscore and other collection programs. The "
            "agency operates under the Regulation of Investigatory Powers Act (RIPA) 2000 "
            "and the Investigatory Powers Act 2016 ('Snoopers' Charter'). Budget and staff "
            "classified, though estimated at over 6,000 employees. Works closely with MI5 "
            "(domestic intelligence) and MI6 (foreign intelligence) as part of the UK "
            "intelligence community."
        ),
        "aliases": "Government Communications Headquarters",
        "metadata": {"location": "Cheltenham, UK", "founded": 1919},
    },

    # ============ PEOPLE ============

    {
        "name": "Thomas Drake",
        "entity_type": "person",
        "description": (
            "Former senior executive at the NSA who attempted to report waste, fraud, and "
            "unconstitutional surveillance through official channels — the DOD Inspector General, "
            "the NSA Inspector General, and the congressional intelligence committees. After "
            "his internal complaints were ignored or suppressed, he spoke to Baltimore Sun "
            "reporter Siobhan Gorman about the NSA's failure to deploy ThinThread (a cheaper, "
            "privacy-protecting alternative to the failed $1.2 billion Trailblazer program) "
            "and the agency's choice of warrantless mass surveillance under Stellar Wind. In "
            "2010, the Obama administration indicted Drake under the Espionage Act on 10 felony "
            "counts — the most aggressive use of the Espionage Act against a whistleblower at "
            "that time. All felony charges were dropped in 2011; Drake pled to a single "
            "misdemeanor of exceeding authorized use of a computer. Jesselyn Radack (Government "
            "Accountability Project) represented him. Drake's prosecution was widely seen as "
            "retaliation and became a landmark case for national security whistleblower "
            "protections. His case predated Snowden by three years and revealed the same "
            "underlying pattern: the apparatus punishes those who expose its illegality."
        ),
        "aliases": "Thomas Andrews Drake",
        "metadata": {
            "nationality": "American",
            "born": "1957-04-22",
            "role": "NSA whistleblower",
        },
    },
    {
        "name": "Mark Klein",
        "entity_type": "person",
        "description": (
            "Former AT&T communications technician who in 2006 blew the whistle on NSA's "
            "domestic internet surveillance by revealing the existence of Room 641A at AT&T's "
            "Folsom Street facility in San Francisco. Klein, a 22-year AT&T employee, provided "
            "a detailed sworn declaration describing the physical infrastructure: a Narus STA "
            "6400 beam splitter that copied all internet traffic — including purely domestic "
            "communications — from AT&T's fiber optic backbone and routed it to an NSA-controlled "
            "room. Klein's evidence formed the basis of the EFF's Jewel v. NSA lawsuit (2008). "
            "His disclosure proved that the NSA was not conducting targeted surveillance but "
            "rather a wholesale tap of the American internet. AT&T was subsequently granted "
            "retroactive immunity through the FISA Amendments Act of 2008, effectively shielding "
            "the company from legal consequences. Klein later published 'Wiring Up the Big Brother "
            "Machine... And Fighting It' (2009), documenting his experience."
        ),
        "metadata": {
            "nationality": "American",
            "role": "AT&T whistleblower",
        },
    },
    {
        "name": "Keith Alexander",
        "entity_type": "person",
        "description": (
            "U.S. Army four-star general who served as Director of the NSA and Chief of the "
            "Central Security Service from 2005 to 2014 — the longest tenure in the agency's "
            "history. Also the first commander of U.S. Cyber Command (2010-2014). Under his "
            "leadership, the NSA dramatically expanded its surveillance capabilities, adopting "
            "what former officials described as a 'collect it all' doctrine — the ambition to "
            "intercept and store every electronic communication on earth. Foreign Policy profiled "
            "him as 'The Cowboy of the NSA' (2013), describing his aggressive expansion of both "
            "signals intelligence collection and offensive cyber operations. The mass surveillance "
            "programs exposed by Snowden — PRISM, XKeyscore, Upstream, Boundless Informant — were "
            "developed and scaled during Alexander's tenure. He testified before Congress that "
            "the programs had prevented 'dozens of terrorist events,' a claim later significantly "
            "walked back by the PCLOB (Privacy and Civil Liberties Oversight Board) and the "
            "President's Review Group. After retirement, Alexander founded IronNet Cybersecurity, "
            "which went public via SPAC in 2021 and filed for bankruptcy in 2023."
        ),
        "aliases": "Gen. Keith Alexander, Keith B. Alexander",
        "metadata": {
            "nationality": "American",
            "born": "1951-12-02",
            "role": "NSA Director (2005-2014)",
        },
    },

    # ============ LEGISLATION ============

    {
        "name": "USA FREEDOM Act",
        "entity_type": "legislation",
        "description": (
            "Signed by President Obama on June 2, 2015. The Uniting and Strengthening America "
            "by Fulfilling Rights and Ensuring Effective Discipline Over Monitoring Act. Enacted "
            "as a direct legislative response to the Snowden revelations. Ended the NSA's bulk "
            "collection of domestic phone metadata under Section 215 of the USA PATRIOT Act, "
            "replacing it with a system requiring telecoms to retain the records and the NSA "
            "to obtain a FISA court order for specific queries. Also introduced a limited "
            "advocate (amicus curiae) to argue before the FISA Court in novel cases. Civil "
            "liberties groups criticized the act as insufficient — it did not address Section "
            "702 (PRISM's legal authority), Executive Order 12333 (the primary authority for "
            "foreign surveillance), or the Five Eyes data-sharing arrangements that circumvent "
            "domestic restrictions. Nonetheless, it was the first law to impose any constraint "
            "on the NSA's post-9/11 surveillance authorities."
        ),
        "aliases": "USA FREEDOM Act of 2015",
        "metadata": {"type": "legislation", "year": 2015},
    },
    {
        "name": "FISA Amendments Act",
        "entity_type": "legislation",
        "description": (
            "Signed by President George W. Bush on July 10, 2008. Amended the Foreign "
            "Intelligence Surveillance Act (FISA) of 1978 to add Section 702, which authorizes "
            "the NSA to collect communications of non-U.S. persons located abroad — even when "
            "those communications involve Americans. Section 702 is the primary legal authority "
            "for PRISM and the Upstream collection program. The act also provided retroactive "
            "legal immunity to telecommunications companies (AT&T, Verizon, etc.) that had "
            "participated in the NSA's warrantless wiretapping program (Stellar Wind) since "
            "2001 — effectively killing dozens of pending lawsuits, including aspects of "
            "Jewel v. NSA. Civil liberties organizations (ACLU, EFF) argued the immunity "
            "provision was unconstitutional. The act has been reauthorized multiple times, "
            "most recently in April 2024. Section 702 remains the most contested authority "
            "in U.S. surveillance law — it permits warrantless collection of Americans' "
            "communications so long as the 'target' is a foreigner abroad."
        ),
        "aliases": "FAA, FISA Amendments Act of 2008, Section 702",
        "metadata": {"type": "legislation", "year": 2008},
    },

    # ============ COURT CASES ============

    {
        "name": "Jewel v. NSA",
        "entity_type": "event",
        "description": (
            "Class-action lawsuit filed by the Electronic Frontier Foundation (EFF) in 2008 "
            "against the NSA, challenging the agency's mass interception of domestic internet "
            "communications. The case was built on Mark Klein's evidence of Room 641A at AT&T's "
            "San Francisco facility — the physical proof that the NSA was copying all internet "
            "traffic on AT&T's backbone, not just targeted foreign communications. Named "
            "plaintiff Carolyn Jewel, an AT&T customer, represented millions of Americans "
            "whose communications were intercepted without warrants. The government invoked "
            "the state secrets privilege to shield evidence. The case survived multiple "
            "dismissal attempts but was ultimately limited by the FISA Amendments Act's "
            "telecom immunity provision. The case remains one of the most significant "
            "legal challenges to mass surveillance in U.S. history and established that "
            "standing exists for ordinary citizens to challenge bulk collection programs."
        ),
        "aliases": "Jewel v. National Security Agency",
        "metadata": {"type": "court case", "year": 2008},
    },
    {
        "name": "ACLU v. Clapper",
        "entity_type": "event",
        "description": (
            "Lawsuit filed by the ACLU in June 2013 — within days of the first Snowden "
            "revelations — challenging the NSA's bulk collection of telephone metadata under "
            "Section 215 of the USA PATRIOT Act. Named defendant James Clapper, the Director "
            "of National Intelligence, who had testified to Congress in March 2013 that the "
            "NSA did 'not wittingly' collect data on millions of Americans — a statement the "
            "Snowden documents proved false. In May 2015, the Second Circuit Court of Appeals "
            "ruled that the bulk phone records program exceeded what Congress authorized under "
            "Section 215 — the first federal appellate court to find the program unlawful. "
            "The ruling contributed directly to the passage of the USA FREEDOM Act (June 2015), "
            "which ended bulk metadata collection. Clapper was never prosecuted for his false "
            "testimony to Congress, leading critics to note the two-tier justice system: "
            "whistleblowers face Espionage Act charges while officials who lie to Congress "
            "face no consequences."
        ),
        "aliases": "ACLU v. James Clapper",
        "metadata": {"type": "court case", "year": 2013},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [

    # ==== SNOWDEN → PROGRAMS ====
    {
        "source": "Edward Snowden",
        "target": "XKeyscore",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Leaked classified NSA training slides revealing XKeyscore as the agency's "
            "most comprehensive internet surveillance tool. Published by The Guardian, July 2013."
        ),
        "year_start": 2013,
        "sources": [931, 932],
    },
    {
        "source": "Edward Snowden",
        "target": "MYSTIC",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Snowden documents revealed MYSTIC program recording 100% of phone calls "
            "in entire countries. Published by The Intercept, 2014."
        ),
        "year_start": 2013,
        "sources": [931, 933],
    },
    {
        "source": "Edward Snowden",
        "target": "Tempora",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Snowden documents revealed GCHQ's Tempora program tapping 200+ transatlantic "
            "fiber optic cables and sharing the take with the NSA. Published by The Guardian, June 2013."
        ),
        "year_start": 2013,
        "sources": [931, 943],
    },
    {
        "source": "Edward Snowden",
        "target": "Five Eyes",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Snowden disclosures revealed the full scope of Five Eyes surveillance cooperation, "
            "including mutual spying on each other's citizens to circumvent domestic legal restrictions."
        ),
        "year_start": 2013,
        "sources": [931, 956, 957],
    },

    # ==== NSA PROGRAMS → NSA ====
    {
        "source": "XKeyscore",
        "target": "NSA",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "NSA's real-time internet surveillance system. Over 700 servers at 150 sites worldwide. "
            "Shared with Five Eyes partners."
        ),
        "year_start": 2008,
        "sources": [932, 935],
    },
    {
        "source": "MYSTIC",
        "target": "NSA",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "NSA program capable of recording 100% of a country's phone calls for 30-day "
            "retroactive retrieval."
        ),
        "year_start": 2009,
        "sources": [933],
    },
    {
        "source": "ECHELON",
        "target": "Five Eyes",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "Five Eyes' global signals intelligence network. Confirmed by European Parliament "
            "investigation (2001). Uses ground stations across UKUSA member nations."
        ),
        "year_start": 1966,
        "sources": [934, 959, 960],
    },
    {
        "source": "ECHELON",
        "target": "NSA",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "NSA is the primary operator and largest contributor to the ECHELON system. "
            "U.S. ground stations at Sugar Grove, Yakima, and others."
        ),
        "year_start": 1966,
        "sources": [934, 936, 954],
    },

    # ==== FIVE EYES STRUCTURE ====
    {
        "source": "NSA",
        "target": "Five Eyes",
        "type": "member_of",
        "tier": "documented",
        "desc": (
            "NSA is the U.S. SIGINT component of the Five Eyes alliance, the largest "
            "and most capable member. UKUSA Agreement (1946)."
        ),
        "year_start": 1946,
        "sources": [937],
    },
    {
        "source": "GCHQ",
        "target": "Five Eyes",
        "type": "member_of",
        "tier": "documented",
        "desc": (
            "GCHQ is the UK SIGINT component of Five Eyes. Co-signatory of the original "
            "UKUSA Agreement (1946). Second-largest Five Eyes member."
        ),
        "year_start": 1946,
        "sources": [937],
    },

    # ==== GCHQ → TEMPORA → NSA ====
    {
        "source": "Tempora",
        "target": "GCHQ",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "GCHQ's fiber optic cable tapping program. Intercepted 21 petabytes/day from "
            "200+ cables. Largest internet surveillance program of any Five Eyes partner by 2012."
        ),
        "year_start": 2011,
        "sources": [943, 944],
    },
    {
        "source": "GCHQ",
        "target": "NSA",
        "type": "intelligence_sharing",
        "tier": "documented",
        "desc": (
            "GCHQ shared Tempora intercepts with NSA, giving the NSA access to communications "
            "transiting UK infrastructure that would be more legally constrained to collect domestically."
        ),
        "year_start": 2011,
        "sources": [943, 937],
    },

    # ==== ROOM 641A / AT&T / KLEIN ====
    {
        "source": "Mark Klein",
        "target": "Room 641A",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "AT&T technician who blew the whistle on Room 641A in 2006, providing a sworn "
            "declaration describing NSA's fiber optic splitter copying all domestic internet traffic."
        ),
        "year_start": 2006,
        "sources": [938, 939],
    },
    {
        "source": "Room 641A",
        "target": "NSA",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "NSA equipment installed in AT&T's San Francisco facility. Narus STA 6400 beam "
            "splitter copied all internet traffic on AT&T's backbone. Only NSA-cleared personnel had access."
        ),
        "year_start": 2003,
        "sources": [938, 939, 940],
    },
    {
        "source": "Room 641A",
        "target": "Jewel v. NSA",
        "type": "evidence_in",
        "tier": "documented",
        "desc": (
            "Klein's evidence of Room 641A formed the factual basis of EFF's Jewel v. NSA "
            "lawsuit challenging mass domestic internet surveillance."
        ),
        "year_start": 2008,
        "sources": [938, 940],
    },

    # ==== VAULT 7 → CIA ====
    {
        "source": "Vault 7",
        "target": "CIA",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "CIA's Center for Cyber Intelligence developed the hacking tools. 8,761 documents "
            "leaked to WikiLeaks in 2017, revealing parallel SIGINT capability to NSA."
        ),
        "year_start": 2013,
        "year_end": 2017,
        "sources": [941, 942],
    },
    {
        "source": "WikiLeaks",
        "target": "Vault 7",
        "type": "published",
        "tier": "documented",
        "desc": (
            "WikiLeaks published the Vault 7 archive beginning March 7, 2017 — the largest "
            "leak of CIA documents in history. Revealed CIA's full hacking arsenal."
        ),
        "year_start": 2017,
        "sources": [941, 942],
    },
    {
        "source": "Vault 7",
        "target": "MI5",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Vault 7 documents revealed 'Weeping Angel' — a joint CIA-MI5 tool that turned "
            "Samsung smart TVs into covert listening devices even when appearing powered off."
        ),
        "sources": [941],
    },

    # ==== CARNIVORE → FBI ====
    {
        "source": "Carnivore",
        "target": "FBI",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "FBI internet surveillance system deployed at ISPs from 1997. Renamed DCS1000 in 2001. "
            "DOJ-commissioned review found risk of overcollection."
        ),
        "year_start": 1997,
        "year_end": 2005,
        "sources": [945, 946],
    },

    # ==== THINTHREAD / DRAKE / BINNEY ====
    {
        "source": "William Binney",
        "target": "ThinThread",
        "type": "created",
        "tier": "documented",
        "desc": (
            "Designed ThinThread as a privacy-protecting surveillance system. Automatic encryption "
            "of U.S. person identities, requiring court order to unmask. Killed in favor of Trailblazer."
        ),
        "year_start": 1999,
        "year_end": 2001,
        "sources": [947, 931],
    },
    {
        "source": "Thomas Drake",
        "target": "NSA",
        "type": "served_in",
        "tier": "documented",
        "desc": (
            "Senior executive at NSA. Attempted to report waste and illegality through official "
            "channels. Prosecuted under Espionage Act (2010), all felony charges dropped (2011)."
        ),
        "year_start": 2001,
        "year_end": 2008,
        "sources": [947, 948],
    },
    {
        "source": "Thomas Drake",
        "target": "ThinThread",
        "type": "advocated_for",
        "tier": "documented",
        "desc": (
            "Tried to report through official channels that NSA chose the $1.2B failed Trailblazer "
            "over the cheaper, privacy-protecting ThinThread. Prosecuted for his efforts."
        ),
        "sources": [947, 948],
    },
    {
        "source": "Thomas Drake",
        "target": "William Binney",
        "type": "corroborated",
        "tier": "documented",
        "desc": (
            "Both independently reported NSA's illegal surveillance and the killing of ThinThread. "
            "Both faced retaliation — FBI raid (Binney, 2007) and Espionage Act prosecution (Drake, 2010)."
        ),
        "sources": [947, 948, 931],
    },
    {
        "source": "ThinThread",
        "target": "Stellar Wind",
        "type": "replaced_by",
        "tier": "documented",
        "desc": (
            "After 9/11, NSA Director Hayden killed ThinThread (privacy-protecting) in favor of "
            "Stellar Wind (warrantless mass collection). DOD IG confirmed ThinThread was technically superior."
        ),
        "year_start": 2001,
        "sources": [947, 955],
    },

    # ==== KEITH ALEXANDER → NSA ====
    {
        "source": "Keith Alexander",
        "target": "NSA",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Longest-serving NSA Director (2005-2014). Implemented 'collect it all' doctrine. "
            "All major programs exposed by Snowden were developed or scaled under his leadership."
        ),
        "year_start": 2005,
        "year_end": 2014,
        "sources": [949, 950],
    },
    {
        "source": "Keith Alexander",
        "target": "XKeyscore",
        "type": "authorized",
        "tier": "credible",
        "desc": (
            "XKeyscore was developed and deployed during Alexander's tenure as NSA Director. "
            "Consistent with his 'collect it all' philosophy described by former officials."
        ),
        "year_start": 2008,
        "sources": [949, 932],
    },

    # ==== PALANTIR / IN-Q-TEL / THIEL ====
    {
        "source": "Palantir Technologies",
        "target": "NSA",
        "type": "contracted_with",
        "tier": "documented",
        "desc": (
            "Palantir provides data analytics platforms to NSA and other intelligence agencies. "
            "The analytical layer sitting atop the collection programs."
        ),
        "sources": [949, 935],
    },
    {
        "source": "Peter Thiel",
        "target": "In-Q-Tel",
        "type": "funded_by",
        "tier": "documented",
        "desc": (
            "In-Q-Tel (CIA venture arm) provided seed funding for Palantir Technologies, "
            "co-founded by Thiel. The investment established the CIA-Silicon Valley surveillance pipeline."
        ),
        "year_start": 2004,
        "sources": [935],
    },

    # ==== LEGISLATION ====
    {
        "source": "USA FREEDOM Act",
        "target": "USA PATRIOT Act",
        "type": "amended",
        "tier": "documented",
        "desc": (
            "Ended NSA bulk metadata collection under Section 215 of the PATRIOT Act. "
            "Direct legislative response to Snowden revelations. Signed June 2, 2015."
        ),
        "year_start": 2015,
        "sources": [951],
    },
    {
        "source": "USA FREEDOM Act",
        "target": "ACLU v. Clapper",
        "type": "resulted_from",
        "tier": "credible",
        "desc": (
            "The Second Circuit's ruling in ACLU v. Clapper (May 2015) finding bulk collection "
            "unlawful contributed directly to congressional passage of the USA FREEDOM Act weeks later."
        ),
        "year_start": 2015,
        "sources": [951, 953],
    },
    {
        "source": "Edward Snowden",
        "target": "USA FREEDOM Act",
        "type": "catalyzed",
        "tier": "credible",
        "desc": (
            "Snowden's 2013 disclosures triggered the public and congressional pressure that "
            "led to the USA FREEDOM Act — the first law to constrain NSA's post-9/11 authorities."
        ),
        "year_start": 2013,
        "year_end": 2015,
        "sources": [931, 951, 956],
    },
    {
        "source": "FISA Amendments Act",
        "target": "PRISM",
        "type": "authorized",
        "tier": "documented",
        "desc": (
            "Section 702 of the FISA Amendments Act (2008) is the primary legal authority for "
            "PRISM. Permits warrantless collection of non-U.S. persons' communications — including "
            "those involving Americans."
        ),
        "year_start": 2008,
        "sources": [952],
    },
    {
        "source": "FISA Amendments Act",
        "target": "Room 641A",
        "type": "legalized",
        "tier": "documented",
        "desc": (
            "Provided retroactive legal immunity to AT&T and other telecoms that participated "
            "in warrantless wiretapping, effectively shielding Room 641A operations from legal consequences."
        ),
        "year_start": 2008,
        "sources": [940, 952],
    },
    {
        "source": "George W. Bush",
        "target": "FISA Amendments Act",
        "type": "authorized",
        "tier": "documented",
        "desc": (
            "Signed the FISA Amendments Act on July 10, 2008, providing the legal framework "
            "for PRISM and retroactive immunity for telecoms involved in Stellar Wind."
        ),
        "year_start": 2008,
        "sources": [952],
    },

    # ==== ACLU v. CLAPPER ====
    {
        "source": "ACLU v. Clapper",
        "target": "NSA",
        "type": "challenged",
        "tier": "documented",
        "desc": (
            "ACLU lawsuit challenged NSA bulk phone metadata collection. Second Circuit ruled "
            "program exceeded Section 215 authority — first federal appellate finding of unlawfulness."
        ),
        "year_start": 2013,
        "year_end": 2015,
        "sources": [953],
    },

    # ==== JEWEL v. NSA ====
    {
        "source": "Jewel v. NSA",
        "target": "NSA",
        "type": "challenged",
        "tier": "documented",
        "desc": (
            "EFF class-action lawsuit challenging mass domestic internet surveillance, "
            "built on Mark Klein's Room 641A evidence. Government invoked state secrets privilege."
        ),
        "year_start": 2008,
        "sources": [940],
    },
    {
        "source": "Mark Klein",
        "target": "Jewel v. NSA",
        "type": "source_for",
        "tier": "documented",
        "desc": (
            "Klein's sworn declaration about Room 641A provided the factual basis for the "
            "EFF's Jewel v. NSA lawsuit — physical proof of mass domestic internet surveillance."
        ),
        "year_start": 2008,
        "sources": [938, 940],
    },

    # ==== CROSS-LINKS TO EXISTING ENTITIES ====
    {
        "source": "Five Eyes",
        "target": "ECHELON",
        "type": "operated",
        "tier": "documented",
        "desc": (
            "ECHELON is the Five Eyes' original global SIGINT collection network. Confirmed by "
            "European Parliament investigation (2001). Predates Snowden-era programs by decades."
        ),
        "year_start": 1966,
        "sources": [934, 960],
    },
    {
        "source": "Church Committee",
        "target": "NSA",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Church Committee (1975-76) investigated NSA's Operation SHAMROCK (bulk collection "
            "of international telegrams) and Operation MINARET (watchlisting of U.S. citizens). "
            "Led to the Foreign Intelligence Surveillance Act (FISA) of 1978."
        ),
        "year_start": 1975,
        "year_end": 1976,
        "sources": [954, 936],
    },
    {
        "source": "Booz Allen Hamilton",
        "target": "Edward Snowden",
        "type": "employed",
        "tier": "documented",
        "desc": (
            "Snowden was employed as an infrastructure analyst at Booz Allen Hamilton, "
            "working on an NSA contract in Hawaii, when he copied and leaked classified documents in 2013."
        ),
        "year_start": 2013,
        "year_end": 2013,
        "sources": [931, 956],
    },
    {
        "source": "NSA",
        "target": "Booz Allen Hamilton",
        "type": "contracted_with",
        "tier": "documented",
        "desc": (
            "Booz Allen Hamilton is one of NSA's largest contractors. Snowden's access to "
            "top-secret surveillance programs while employed by a private contractor highlighted "
            "the risks of intelligence outsourcing."
        ),
        "sources": [931, 935],
    },
    {
        "source": "Unit 8200",
        "target": "NSA",
        "type": "intelligence_sharing",
        "tier": "documented",
        "desc": (
            "Snowden documents revealed NSA shares raw SIGINT with Unit 8200 under a memorandum "
            "of understanding — including data on American citizens, with minimal privacy protections."
        ),
        "year_start": 2009,
        "sources": [931, 957],
    },
    {
        "source": "NSO Group",
        "target": "GCHQ",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "NSO Group (founded by Unit 8200 alumni) and GCHQ operate in overlapping domains — "
            "offensive cyber capabilities and SIGINT. Five Eyes members are documented users of "
            "commercial spyware alongside government SIGINT tools."
        ),
        "sources": [944, 935],
    },
]

# ============================================================
# ENTITY_SOURCES — link entities to their primary sources
# ============================================================

ENTITY_SOURCES = {
    # Programs
    "XKeyscore": [931, 932, 935],
    "ECHELON": [934, 936, 954, 959, 960],
    "Room 641A": [938, 939, 940],
    "Vault 7": [941, 942],
    "MYSTIC": [933],
    "Tempora": [943, 944],
    "Carnivore": [945, 946],
    "ThinThread": [947, 955],
    # Organizations / Alliances
    "Five Eyes": [934, 937, 960],
    "GCHQ": [943, 944, 937],
    # People
    "Thomas Drake": [947, 948],
    "Mark Klein": [938, 939, 940],
    "Keith Alexander": [949, 950],
    # Legislation
    "USA FREEDOM Act": [951],
    "FISA Amendments Act": [952],
    # Court Cases
    "Jewel v. NSA": [938, 940],
    "ACLU v. Clapper": [953],
}
