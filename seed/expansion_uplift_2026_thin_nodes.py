"""
Thin Nodes — Relationships-only expansion for Intel Console.

Thickens entities with 0 or 1 relationships by adding well-sourced cross-links
to existing entities. No new entities. Source IDs 2600-2699.

Clusters covered:
  Defense/MIC, 9/11 legislation & events, think tanks, JFK programs,
  Stargate/remote viewing, food supply, UK abuse investigations,
  bioweapons, water, surveillance, organized crime, occult, other.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 2600-2699
# ============================================================

SOURCES = [
    # --- Defense / MIC ---
    {
        "id": 2600,
        "title": "BAE Systems plc — Wikipedia (company history, defense contracts, Al-Yamamah)",
        "url": "https://en.wikipedia.org/wiki/BAE_Systems",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2601,
        "title": "General Dynamics — Wikipedia (defense contracts, submarines, Gulfstream)",
        "url": "https://en.wikipedia.org/wiki/General_Dynamics",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2602,
        "title": "L3Harris Technologies — Wikipedia (ISR systems, defense electronics, intelligence contracts)",
        "url": "https://en.wikipedia.org/wiki/L3Harris_Technologies",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2603,
        "title": "Science Applications International Corporation — Wikipedia (defense contracting, intelligence work, Stargate)",
        "url": "https://en.wikipedia.org/wiki/Science_Applications_International_Corporation",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2604,
        "title": "Battelle Memorial Institute — Wikipedia (R&D, national lab management, DOE contracts)",
        "url": "https://en.wikipedia.org/wiki/Battelle_Memorial_Institute",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2605,
        "title": "RAND Corporation — Wikipedia (origins, defense analysis, nuclear strategy)",
        "url": "https://en.wikipedia.org/wiki/RAND_Corporation",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2606,
        "title": "DynCorp — Wikipedia (military contracting, State Dept contracts, Bosnia trafficking scandal)",
        "url": "https://en.wikipedia.org/wiki/DynCorp",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2607,
        "title": "Raytheon Technologies — Wikipedia (missile systems, defense electronics, mergers)",
        "url": "https://en.wikipedia.org/wiki/RTX_Corporation",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2608,
        "title": "Northrop Grumman — Wikipedia (B-2, B-21, stealth programs, defense contracting)",
        "url": "https://en.wikipedia.org/wiki/Northrop_Grumman",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2609,
        "title": "Boeing Defense, Space & Security — Wikipedia (military aircraft, contracts)",
        "url": "https://en.wikipedia.org/wiki/Boeing_Defense,_Space_%26_Security",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2610,
        "title": "F-35 Lightning II — Wikipedia (program history, cost, contractors)",
        "url": "https://en.wikipedia.org/wiki/Lockheed_Martin_F-35_Lightning_II",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2611,
        "title": "Norman R. Augustine — Wikipedia (Lockheed Martin CEO, Under Secretary of the Army)",
        "url": "https://en.wikipedia.org/wiki/Norman_R._Augustine",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2612,
        "title": "Special access program — Wikipedia (classification levels, oversight, black programs)",
        "url": "https://en.wikipedia.org/wiki/Special_access_program",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2613,
        "title": "GAO — F-35 Joint Strike Fighter: DOD Needs to Update Modernization Schedule (GAO-24-105051)",
        "url": "https://www.gao.gov/products/gao-24-105051",
        "source_type": "government",
        "year": 2024,
    },
    {
        "id": 2614,
        "title": "DOD Office of Inspector General — Financial Management and Audit Readiness",
        "url": "https://www.dodig.mil/reports.html/Article/3282788/",
        "source_type": "government",
        "year": 2023,
    },
    # --- 9/11 cluster ---
    {
        "id": 2615,
        "title": "Project for the New American Century — Wikipedia (founding, members, 'Rebuilding America's Defenses')",
        "url": "https://en.wikipedia.org/wiki/Project_for_the_New_American_Century",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2616,
        "title": "PNAC — Rebuilding America's Defenses: Strategy, Forces and Resources for a New Century (2000)",
        "url": "https://web.archive.org/web/20130501025028/http://www.newamericancentury.org/RebsuildingAmericasDefenses.pdf",
        "source_type": "other",
        "year": 2000,
    },
    {
        "id": 2617,
        "title": "Authorization for Use of Military Force — Public Law 107-40 (Sep 18, 2001)",
        "url": "https://www.congress.gov/107/plaws/publ40/PLAW-107publ40.htm",
        "source_type": "government",
        "year": 2001,
    },
    {
        "id": 2618,
        "title": "USA PATRIOT Act — Public Law 107-56 (Oct 26, 2001)",
        "url": "https://www.congress.gov/107/plaws/publ56/PLAW-107publ56.htm",
        "source_type": "government",
        "year": 2001,
    },
    {
        "id": 2619,
        "title": "WTC Building 7 — Wikipedia (collapse, investigations, NIST report)",
        "url": "https://en.wikipedia.org/wiki/7_World_Trade_Center",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2620,
        "title": "Able Danger — Wikipedia (DOD data-mining, Atta identification, cover-up allegations)",
        "url": "https://en.wikipedia.org/wiki/Able_Danger",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2621,
        "title": "Sandy Berger — Wikipedia (archives theft, 9/11 Commission testimony preparation)",
        "url": "https://en.wikipedia.org/wiki/Sandy_Berger",
        "source_type": "other",
        "year": 2026,
    },
    # --- Think tanks ---
    {
        "id": 2622,
        "title": "Brookings Institution — Wikipedia (history, funding, policy influence)",
        "url": "https://en.wikipedia.org/wiki/Brookings_Institution",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2623,
        "title": "Carnegie Endowment for International Peace — Wikipedia (founding, Alger Hiss, CFR overlap)",
        "url": "https://en.wikipedia.org/wiki/Carnegie_Endowment_for_International_Peace",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2624,
        "title": "Club of Rome — Wikipedia (founding, Limits to Growth, membership)",
        "url": "https://en.wikipedia.org/wiki/Club_of_Rome",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2625,
        "title": "Ford Foundation — Wikipedia (history, CIA conduit, Church Committee findings)",
        "url": "https://en.wikipedia.org/wiki/Ford_Foundation",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2626,
        "title": "Church Committee — Final Report, Book I: Foreign and Military Intelligence (1976, Ford Foundation-CIA)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/94755_I.pdf",
        "source_type": "congressional",
        "year": 1976,
    },
    {
        "id": 2627,
        "title": "Open Society Foundations — Wikipedia (founding, scope, Atlantic Council grants)",
        "url": "https://en.wikipedia.org/wiki/Open_Society_Foundations",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2628,
        "title": "Chatham House — Wikipedia (founding, Chatham House Rule, policy influence)",
        "url": "https://en.wikipedia.org/wiki/Chatham_House",
        "source_type": "other",
        "year": 2026,
    },
    # --- JFK ---
    {
        "id": 2629,
        "title": "Dealey Plaza — Wikipedia (JFK assassination site, historical landmark)",
        "url": "https://en.wikipedia.org/wiki/Dealey_Plaza",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2630,
        "title": "Assassination Records Review Board — Wikipedia (JFK Records Act, declassification)",
        "url": "https://en.wikipedia.org/wiki/Assassination_Records_Review_Board",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2631,
        "title": "ZR/RIFLE — Church Committee Final Report on Alleged Assassination Plots (1975)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/94465.pdf",
        "source_type": "congressional",
        "year": 1975,
    },
    {
        "id": 2632,
        "title": "Operation 40 — Wikipedia (CIA anti-Castro operations, Bay of Pigs)",
        "url": "https://en.wikipedia.org/wiki/Operation_40",
        "source_type": "other",
        "year": 2026,
    },
    # --- Stargate / Remote Viewing ---
    {
        "id": 2633,
        "title": "Stargate Project — Wikipedia (program history, SRI, DIA, participants)",
        "url": "https://en.wikipedia.org/wiki/Stargate_Project",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2634,
        "title": "Jessica Utts — 'An Assessment of the Evidence for Psychic Functioning' (AIR review, 1995)",
        "url": "https://www.ics.uci.edu/~jutts/air.pdf",
        "source_type": "academic",
        "author": "Jessica Utts",
        "year": 1995,
    },
    {
        "id": 2635,
        "title": "Project Scanate — Wikipedia (CIA remote viewing evaluation at SRI, 1973)",
        "url": "https://en.wikipedia.org/wiki/Project_Scanate",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2636,
        "title": "Angela Dellafiora Ford — DIA remote viewer, Charles Jordan fugitive location (1989)",
        "url": "https://en.wikipedia.org/wiki/Stargate_Project#Notable_sessions",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2637,
        "title": "Dale Graff — Tracks in the Psychic Wilderness (DIA Stargate program management)",
        "url": "https://en.wikipedia.org/wiki/Dale_E._Graff",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2638,
        "title": "Gateway Process — Wikipedia (Monroe Institute techniques, DIA analysis)",
        "url": "https://en.wikipedia.org/wiki/Gateway_Process",
        "source_type": "other",
        "year": 2026,
    },
    # --- Food / Agriculture ---
    {
        "id": 2639,
        "title": "Bayer — Wikipedia (Monsanto acquisition, Roundup litigation, corporate history)",
        "url": "https://en.wikipedia.org/wiki/Bayer",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2640,
        "title": "Robert Fraley — Wikipedia (Monsanto CTO, plant cell transformation, World Food Prize)",
        "url": "https://en.wikipedia.org/wiki/Robert_Fraley",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2641,
        "title": "National Bioengineered Food Disclosure Standard (DARK Act) — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/National_Bioengineered_Food_Disclosure_Standard",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2642,
        "title": "Farmer Assurance Provision (Monsanto Protection Act) — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Farmer_Assurance_Provision",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2643,
        "title": "Indian Farmer Suicides — Wikipedia (Bt cotton, seed debt, Monsanto link)",
        "url": "https://en.wikipedia.org/wiki/Farmer_suicides_in_India",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2644,
        "title": "Genetic use restriction technologies — Wikipedia (terminator seeds, Monsanto, USDA)",
        "url": "https://en.wikipedia.org/wiki/Genetic_use_restriction_technology",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2645,
        "title": "Roundup (herbicide) — Wikipedia (litigation, Bayer settlement, IARC classification)",
        "url": "https://en.wikipedia.org/wiki/Roundup_(herbicide)",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2646,
        "title": "Monsanto Papers — US Right to Know investigation (internal documents, ghostwriting)",
        "url": "https://usrtk.org/monsanto-papers/",
        "source_type": "journalism",
        "author": "US Right to Know",
        "year": 2017,
    },
    {
        "id": 2647,
        "title": "ADM price-fixing scandal — Wikipedia (lysine cartel, FBI informant Mark Whitacre)",
        "url": "https://en.wikipedia.org/wiki/Archer_Daniels_Midland#Price-fixing_scandal",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2648,
        "title": "Codex Alimentarius — Wikipedia (WHO/FAO food standards body)",
        "url": "https://en.wikipedia.org/wiki/Codex_Alimentarius",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2649,
        "title": "Vandana Shiva — Wikipedia (seed freedom activism, Indian farmer suicides advocacy)",
        "url": "https://en.wikipedia.org/wiki/Vandana_Shiva",
        "source_type": "other",
        "year": 2026,
    },
    # --- UK abuse investigations ---
    {
        "id": 2650,
        "title": "Cyril Smith — Wikipedia (abuse allegations, MI5 cover-up, police confirmed complaints)",
        "url": "https://en.wikipedia.org/wiki/Cyril_Smith",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2651,
        "title": "Operation Yewtree — Wikipedia (Jimmy Savile investigation, Metropolitan Police)",
        "url": "https://en.wikipedia.org/wiki/Operation_Yewtree",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2652,
        "title": "Operation Midland — Wikipedia (Metropolitan Police VIP abuse investigation)",
        "url": "https://en.wikipedia.org/wiki/Operation_Midland",
        "source_type": "other",
        "year": 2026,
    },
    # --- Bioweapons / health ---
    {
        "id": 2653,
        "title": "Defense Threat Reduction Agency — Wikipedia (WMD programs, Fort Detrick, CTR)",
        "url": "https://en.wikipedia.org/wiki/Defense_Threat_Reduction_Agency",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2654,
        "title": "CDC Shutdown of Fort Detrick USAMRIID Operations (2019) — federal inspection failures",
        "url": "https://en.wikipedia.org/wiki/Fort_Detrick#Temporary_shutdown_(2019)",
        "source_type": "other",
        "year": 2019,
    },
    {
        "id": 2655,
        "title": "Sverdlovsk anthrax leak — Wikipedia (1979 Soviet bioweapons accident)",
        "url": "https://en.wikipedia.org/wiki/Sverdlovsk_anthrax_leak",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2656,
        "title": "Ken Alibek — Wikipedia (Biopreparat defector, Sverdlovsk confirmation)",
        "url": "https://en.wikipedia.org/wiki/Ken_Alibek",
        "source_type": "other",
        "year": 2026,
    },
    # --- Water ---
    {
        "id": 2657,
        "title": "Flint water crisis — Wikipedia (lead contamination, CDC testing, emergency management)",
        "url": "https://en.wikipedia.org/wiki/Flint_water_crisis",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2658,
        "title": "Detroit water shutoffs — Wikipedia (2014 mass disconnections, Nestle controversy)",
        "url": "https://en.wikipedia.org/wiki/Water_supply_and_sanitation_in_the_Detroit_metropolitan_area",
        "source_type": "other",
        "year": 2026,
    },
    # --- Other ---
    {
        "id": 2659,
        "title": "Anderson Cooper — Wikipedia (CNN, Dalton School, CIA internship, Vanderbilt family)",
        "url": "https://en.wikipedia.org/wiki/Anderson_Cooper",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2660,
        "title": "DuPont family — Wikipedia (chemical dynasty, Nye Committee, Business Plot connections)",
        "url": "https://en.wikipedia.org/wiki/Du_Pont_family",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2661,
        "title": "Pujo Committee — Wikipedia (1912-1913 Money Trust investigation, Federal Reserve origins)",
        "url": "https://en.wikipedia.org/wiki/Pujo_Committee",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2662,
        "title": "Smedley Butler — War Is a Racket (1935, Standard Oil and war profiteering)",
        "url": "https://en.wikipedia.org/wiki/War_Is_a_Racket",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2663,
        "title": "United Fruit Company — Wikipedia (Guatemalan coup, Dulles connections)",
        "url": "https://en.wikipedia.org/wiki/United_Fruit_Company",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2664,
        "title": "Carnivore (FBI software) — Wikipedia (internet surveillance, DCS1000 rename)",
        "url": "https://en.wikipedia.org/wiki/Carnivore_(software)",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2665,
        "title": "Internet Research Agency — Wikipedia (Russian troll farm, Prigozhin, Mueller indictment)",
        "url": "https://en.wikipedia.org/wiki/Internet_Research_Agency",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2666,
        "title": "Mueller indictment of Internet Research Agency (U.S. v. Internet Research Agency LLC, 2018)",
        "url": "https://www.justice.gov/file/1035477/download",
        "source_type": "court",
        "year": 2018,
    },
    {
        "id": 2667,
        "title": "Eisenhower Farewell Address — Wikipedia (military-industrial complex warning, 1961)",
        "url": "https://en.wikipedia.org/wiki/Eisenhower%27s_farewell_address",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2668,
        "title": "Gulf of Tonkin Resolution — Wikipedia (1964, congressional authority, Vietnam War)",
        "url": "https://en.wikipedia.org/wiki/Gulf_of_Tonkin_Resolution",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2669,
        "title": "Smith-Mundt Modernization Act of 2012 — Wikipedia (domestic propaganda legalization)",
        "url": "https://en.wikipedia.org/wiki/Smith%E2%80%93Mundt_Act#Smith-Mundt_Modernization_Act_of_2012",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2670,
        "title": "Hill & Knowlton Strategies — Wikipedia (PR, CIA connections, Kuwait testimony)",
        "url": "https://en.wikipedia.org/wiki/Hill_%26_Knowlton_Strategies",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2671,
        "title": "Robert Maxwell — Wikipedia (death, Israeli state funeral, intelligence connections)",
        "url": "https://en.wikipedia.org/wiki/Robert_Maxwell#Death",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2672,
        "title": "Cali Cartel — Wikipedia (DEA operations, Rodriguez Orejuela brothers)",
        "url": "https://en.wikipedia.org/wiki/Cali_Cartel",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2673,
        "title": "Bureau of Alcohol, Tobacco, Firearms and Explosives — Wikipedia (DOJ transfer, Waco)",
        "url": "https://en.wikipedia.org/wiki/Bureau_of_Alcohol,_Tobacco,_Firearms_and_Explosives",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2674,
        "title": "Thule Society — Wikipedia (origins of Nazi Party, occult nationalism)",
        "url": "https://en.wikipedia.org/wiki/Thule_Society",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2675,
        "title": "Temple of Set — Wikipedia (Michael Aquino, Presidio connections)",
        "url": "https://en.wikipedia.org/wiki/Temple_of_Set",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2676,
        "title": "Process Church of the Final Judgment — Wikipedia (DeGrimstons, Scientology origins)",
        "url": "https://en.wikipedia.org/wiki/Process_Church_of_the_Final_Judgment",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2677,
        "title": "Wright-Patterson Air Force Base — Wikipedia (Project Blue Book, AFMC, Foreign Technology Division)",
        "url": "https://en.wikipedia.org/wiki/Wright-Patterson_Air_Force_Base",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2678,
        "title": "DynCorp — Department of State contracts, Latin America operations",
        "url": "https://en.wikipedia.org/wiki/DynCorp#Controversies",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2679,
        "title": "Craig Spence — Wikipedia (lobbyist, Georgetown Club, Franklin scandal connections)",
        "url": "https://en.wikipedia.org/wiki/Craig_Spence",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2680,
        "title": "Andrew Carnegie — Wikipedia (Carnegie Endowment founding, philanthropy)",
        "url": "https://en.wikipedia.org/wiki/Andrew_Carnegie",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2681,
        "title": "David Rockefeller — Wikipedia (Club of Rome, Trilateral Commission, globalist network)",
        "url": "https://en.wikipedia.org/wiki/David_Rockefeller",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2682,
        "title": "Prescott Bush — Wikipedia (banking, politics, Business Plot era connections)",
        "url": "https://en.wikipedia.org/wiki/Prescott_Bush",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2683,
        "title": "United Grand Lodge of England — Wikipedia (formation, governance of Freemasonry)",
        "url": "https://en.wikipedia.org/wiki/United_Grand_Lodge_of_England",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2684,
        "title": "Jacobo Árbenz — Wikipedia (Guatemala presidency, agrarian reform, United Fruit)",
        "url": "https://en.wikipedia.org/wiki/Jacobo_%C3%81rbenz",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2685,
        "title": "Nestlé Waters — Wikipedia (Michigan water extraction controversy)",
        "url": "https://en.wikipedia.org/wiki/Nestl%C3%A9_Waters",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2686,
        "title": "DGSE — Wikipedia (French external intelligence, NATO cooperation)",
        "url": "https://en.wikipedia.org/wiki/Directorate-General_for_External_Security",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2687,
        "title": "CDC — Wikipedia (US Centers for Disease Control and Prevention, NIH cooperation)",
        "url": "https://en.wikipedia.org/wiki/Centers_for_Disease_Control_and_Prevention",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2688,
        "title": "Blaise Metreweli — Wikipedia (MI6 Chief, Five Eyes leadership)",
        "url": "https://en.wikipedia.org/wiki/Chief_of_the_Secret_Intelligence_Service",
        "source_type": "other",
        "year": 2026,
    },
]


# ============================================================
# ENTITIES — none (relationships-only module)
# ============================================================

ENTITIES = []

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ================================================================
    # DEFENSE / MIC CLUSTER
    # ================================================================

    # --- BAE Systems (0 rels → 2) ---
    {
        "source": "BAE Systems",
        "target": "BAE Al-Yamamah Deal",
        "type": "participated_in",
        "tier": "documented",
        "desc": "BAE Systems (formerly British Aerospace) was the prime contractor in the Al-Yamamah arms deal with Saudi Arabia, the largest arms deal in British history. SFO investigation into payments exceeding one billion pounds in commissions was shut down by the Blair government in 2006.",
        "year_start": 1985,
        "sources": [2600],
    },
    {
        "source": "BAE Systems",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Major US defense supplier through BAE Systems Inc. (US subsidiary). Provides electronic warfare systems, armored vehicles, and munitions to the US military. Revenue from US defense contracts exceeds $10 billion annually.",
        "sources": [2600],
    },

    # --- General Dynamics (0 rels → 2) ---
    {
        "source": "General Dynamics",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Fifth-largest US defense contractor. Builds Virginia-class and Columbia-class submarines, Abrams tanks, Stryker vehicles, and Gulfstream business jets. Revenue approximately $39 billion (2022), heavily dependent on Pentagon contracts.",
        "sources": [2601],
    },
    {
        "source": "General Dynamics",
        "target": "Carlyle Group",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Carlyle Group, the defense-focused private equity firm, has extensive ties to the defense industrial base including companies in General Dynamics' supply chain. Both entities exemplify the revolving door between defense contracting and political power.",
        "sources": [2601],
    },

    # --- L3Harris Technologies (0 rels → 2) ---
    {
        "source": "L3Harris Technologies",
        "target": "NSA",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Major signals intelligence and surveillance technology contractor for the NSA. Provides ISR systems, communications equipment, electronic warfare, and classified intelligence platforms. Formed from 2019 merger of L3 Technologies and Harris Corporation.",
        "year_start": 2019,
        "sources": [2602],
    },
    {
        "source": "L3Harris Technologies",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Sixth-largest US defense contractor. Revenue approximately $18 billion. Supplies the Pentagon with ISR systems, tactical radios, electronic warfare, and night vision equipment across all military branches.",
        "sources": [2602],
    },

    # --- SAIC (0 rels → 2) ---
    {
        "source": "SAIC",
        "target": "Project Stargate",
        "type": "operated",
        "tier": "documented",
        "desc": "SAIC took over the remote viewing research program from SRI International in the mid-1980s. Managed operational remote viewing for DIA until the program's termination in 1995. Key SAIC personnel included Ed Dames and others who later commercialized the techniques.",
        "year_start": 1985,
        "year_end": 1995,
        "sources": [2603, 2633],
    },
    {
        "source": "SAIC",
        "target": "DIA",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Major defense intelligence contractor. SAIC held contracts with DIA for intelligence analysis, remote viewing research (Project Stargate), and other classified programs. Part of the broader intelligence community contractor ecosystem.",
        "sources": [2603],
    },

    # --- Battelle Memorial Institute (1 rel → 3) ---
    {
        "source": "Battelle Memorial Institute",
        "target": "DOE",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Manages or co-manages multiple DOE national laboratories including Pacific Northwest National Laboratory, Oak Ridge National Laboratory, Brookhaven National Laboratory, and Idaho National Laboratory. World's largest independent R&D organization.",
        "sources": [2604],
    },
    {
        "source": "Battelle Memorial Institute",
        "target": "Wright-Patterson AFB",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Both located in the Dayton, Ohio area. Battelle has conducted classified research at Wright-Patterson including Project Blue Book Special Report No. 14 (1955), the most comprehensive statistical analysis of UFO reports ever performed by the US government.",
        "sources": [2604, 2677],
    },

    # --- RAND Corporation (1 rel → 3) ---
    {
        "source": "RAND Corporation",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Created in 1948 by Douglas Aircraft Company for the US Air Force. Developed nuclear deterrence theory (Herman Kahn), game theory applications, systems analysis for Vietnam War, and continues as the Pentagon's premier policy research contractor.",
        "year_start": 1948,
        "sources": [2605],
    },
    {
        "source": "RAND Corporation",
        "target": "CIA",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Conducts classified and unclassified research for the CIA and broader intelligence community. RAND analysts have shaped US intelligence policy on topics from Soviet capabilities to counterterrorism to cyber warfare.",
        "sources": [2605],
    },

    # --- Boeing Defense (1 rel → 2) ---
    {
        "source": "Boeing Defense",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Major defense arm of Boeing Company. Produces F/A-18, AH-64 Apache, KC-46 tanker, Space Launch System. Revenue approximately $23 billion from defense contracts. Multiple procurement scandals including Darleen Druyun corruption case.",
        "sources": [2609],
    },

    # --- Northrop Grumman (1 rel → 3) ---
    {
        "source": "Northrop Grumman",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Fourth-largest US defense contractor. Builds B-2 Spirit, B-21 Raider, Global Hawk, and James Webb Space Telescope. Revenue approximately $37 billion. Key participant in classified programs and Special Access Programs.",
        "sources": [2608],
    },
    {
        "source": "Northrop Grumman",
        "target": "B-2 Spirit Strike Package",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Northrop Grumman manufactured the B-2 Spirit stealth bomber used in the February 2026 strike package against Iranian nuclear facilities during Operation Epic Fury. Four B-2s from the 509th Bomb Wing flew round-trip missions from Whiteman AFB.",
        "year_start": 1989,
        "sources": [2608],
    },

    # --- Raytheon (1 rel → 3) ---
    {
        "source": "Raytheon",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Second-largest US defense contractor (as RTX). Produces Tomahawk cruise missiles, Patriot air defense, Stinger missiles, and advanced radar systems. Merged with United Technologies in 2020. Former CEO Lloyd Austin became Secretary of Defense.",
        "sources": [2607],
    },
    {
        "source": "Raytheon",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Raytheon-manufactured Tomahawk cruise missiles and other precision munitions were employed in Operation Epic Fury strikes against Iranian military infrastructure in February-March 2026.",
        "year_start": 2026,
        "sources": [2607],
    },

    # --- Norman Augustine (1 rel → 2) ---
    {
        "source": "Norman Augustine",
        "target": "The Pentagon",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Served as Under Secretary of the Army (1975-1977) before becoming CEO of Martin Marietta and then Lockheed Martin. Architect of the 1990s defense industry consolidation. Exemplifies the revolving door between Pentagon and defense industry.",
        "year_start": 1975,
        "year_end": 1977,
        "sources": [2611],
    },

    # --- F-35 Joint Strike Fighter (1 rel → 3) ---
    {
        "source": "F-35 Joint Strike Fighter",
        "target": "The Pentagon",
        "type": "funded_by",
        "tier": "documented",
        "desc": "Most expensive weapons program in history with estimated lifecycle cost of $1.7 trillion. Chronically over budget and behind schedule. GAO has documented persistent cost overruns, software defects, and sustainment challenges across multiple reports.",
        "year_start": 2001,
        "sources": [2610, 2613],
    },
    {
        "source": "F-35 Joint Strike Fighter",
        "target": "Pentagon Audit Failures",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The F-35 program exemplifies the Pentagon's accountability failures. GAO has identified the program as high-risk since 2001. Cost overruns, schedule delays, and inability to track spending contribute to the broader pattern of Pentagon audit failures.",
        "sources": [2613, 2614],
    },

    # --- Special Access Programs (1 rel → 3) ---
    {
        "source": "Special Access Programs",
        "target": "The Pentagon",
        "type": "operated_by",
        "tier": "documented",
        "desc": "DOD classification level above Top Secret. Includes Acknowledged and Unacknowledged SAPs (USAPs). Congressional oversight is limited to the 'Gang of Eight.' Annual black budget estimated at $50+ billion. David Grusch's 2023 testimony alleged SAPs holding non-human technology.",
        "sources": [2612],
    },
    {
        "source": "Special Access Programs",
        "target": "CIA",
        "type": "operated_by",
        "tier": "documented",
        "desc": "The CIA operates its own Special Access Programs for intelligence activities, including covert action programs that require presidential finding. CIA SAPs have even more restricted oversight than DOD SAPs.",
        "sources": [2612],
    },

    # --- Pentagon Audit Failures (1 rel → 2) ---
    {
        "source": "Pentagon Audit Failures",
        "target": "The Pentagon",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Pentagon has failed every comprehensive financial audit since mandatory audits began in 2018. Six consecutive failures through 2023. Trillions in transactions cannot be tracked. DOD Inspector General has documented systematic inability to account for assets and expenditures.",
        "sources": [2614],
    },

    # --- DynCorp (1 rel → 3) ---
    {
        "source": "DynCorp",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "documented",
        "desc": "Private military contractor with extensive Pentagon contracts for logistics, maintenance, and training. Operated in Iraq, Afghanistan, and Latin America. State Department Inspector General investigated employee involvement in human trafficking in Bosnia (2002).",
        "sources": [2606, 2678],
    },
    {
        "source": "DynCorp",
        "target": "School of the Americas",
        "type": "connected_to",
        "tier": "credible",
        "desc": "DynCorp provided contract personnel for US military training operations in Latin America, overlapping with the mission of the School of the Americas (Western Hemisphere Institute for Security Cooperation). Both institutions trained Latin American security forces during the drug war era.",
        "sources": [2606],
    },

    # ================================================================
    # 9/11 CLUSTER
    # ================================================================

    # --- PNAC (0 rels → 3) ---
    {
        "source": "Dick Cheney",
        "target": "PNAC",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": "Signatory of PNAC's founding Statement of Principles (1997). PNAC's 2000 report 'Rebuilding America's Defenses' stated military transformation would require a 'new Pearl Harbor' as a catalyzing event.",
        "year_start": 1997,
        "sources": [2615, 2616],
    },
    {
        "source": "Donald Rumsfeld",
        "target": "PNAC",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": "Signatory of PNAC's founding Statement of Principles (1997). As Secretary of Defense on 9/11, implemented the military transformation agenda PNAC had outlined. Announced $2.3 trillion in untracked Pentagon transactions on September 10, 2001.",
        "year_start": 1997,
        "sources": [2615, 2616],
    },
    {
        "source": "PNAC",
        "target": "September 11 Attacks",
        "type": "connected_to",
        "tier": "inference",
        "desc": "PNAC's 2000 report 'Rebuilding America's Defenses' stated that military transformation of the scope it advocated would be slow 'absent some catastrophic and catalyzing event — like a new Pearl Harbor.' The 9/11 attacks provided exactly that catalyst, enabling rapid implementation of PNAC's policy agenda.",
        "year_start": 2000,
        "year_end": 2001,
        "sources": [2615, 2616],
    },

    # --- Authorization for Use of Military Force (2001) (0 rels → 2) ---
    {
        "source": "George W. Bush",
        "target": "Authorization for Use of Military Force (2001)",
        "type": "signed_into_law",
        "tier": "documented",
        "desc": "Signed Public Law 107-40 on September 18, 2001, one week after 9/11. Authorized the president to use 'all necessary and appropriate force' against those connected to 9/11. Has been used to justify military operations across multiple countries for over two decades.",
        "year_start": 2001,
        "sources": [2617],
    },
    {
        "source": "Authorization for Use of Military Force (2001)",
        "target": "September 11 Attacks",
        "type": "resulted_from",
        "tier": "documented",
        "desc": "Passed by Congress in direct response to 9/11. Senate vote was 98-0 (only dissent was Rep. Barbara Lee in the House). The AUMF has become the legal basis for US military operations in Afghanistan, Iraq, Syria, Yemen, Somalia, and Libya.",
        "year_start": 2001,
        "sources": [2617],
    },

    # --- USA PATRIOT Act (1 rel → 3) ---
    {
        "source": "George W. Bush",
        "target": "USA PATRIOT Act",
        "type": "signed_into_law",
        "tier": "documented",
        "desc": "Signed Public Law 107-56 on October 26, 2001, 45 days after 9/11. The 342-page bill passed with minimal debate. Dramatically expanded surveillance authority including roving wiretaps, business record access (Section 215), and elimination of barriers between foreign intelligence and criminal investigations.",
        "year_start": 2001,
        "sources": [2618],
    },
    {
        "source": "USA PATRIOT Act",
        "target": "September 11 Attacks",
        "type": "resulted_from",
        "tier": "documented",
        "desc": "Enacted in direct response to 9/11. Pre-drafted elements had been sought by intelligence agencies for years. NSA mass surveillance programs later revealed by Snowden were authorized under its provisions, particularly Section 215.",
        "year_start": 2001,
        "sources": [2618],
    },

    # --- WTC Building 7 Collapse (1 rel → 2) ---
    {
        "source": "WTC Building 7 Collapse",
        "target": "World Trade Center",
        "type": "located_at",
        "tier": "documented",
        "desc": "WTC 7 was a 47-story building in the World Trade Center complex that collapsed at 5:20 PM on September 11, 2001, at near free-fall speed despite not being hit by a plane. NIST attributed collapse to fire (2008). University of Alaska Fairbanks study (2020) concluded fire could not have caused the observed collapse.",
        "year_start": 2001,
        "sources": [2619],
    },

    # --- Operation Able Danger (1 rel → 2) ---
    {
        "source": "Operation Able Danger",
        "target": "The Pentagon",
        "type": "operated_by",
        "tier": "documented",
        "desc": "DOD data-mining program run by US Special Operations Command (SOCOM). Identified Mohamed Atta and three other 9/11 hijackers as Al-Qaeda members before September 11, 2001. Lt. Col. Anthony Shaffer testified that DOD lawyers blocked information-sharing with the FBI.",
        "year_start": 1999,
        "year_end": 2001,
        "sources": [2620],
    },

    # --- Berger Archives Theft (2003) (1 rel → 2) ---
    {
        "source": "Berger Archives Theft (2003)",
        "target": "9/11 Commission",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Sandy Berger was caught stealing and destroying classified documents from the National Archives in October 2003 while preparing to testify before the 9/11 Commission on behalf of the Clinton administration. The destroyed documents related to millennium terror threats and the Clinton administration's counterterrorism record.",
        "year_start": 2003,
        "sources": [2621],
    },

    # ================================================================
    # THINK TANKS
    # ================================================================

    # --- Brookings Institution (0 rels → 2) ---
    {
        "source": "Brookings Institution",
        "target": "Council on Foreign Relations",
        "type": "affiliated_with",
        "tier": "credible",
        "desc": "Extensive overlapping membership and policy influence with the Council on Foreign Relations. Both institutions shape US foreign and economic policy, with scholars frequently serving in both organizations. Together they form the core of the 'establishment' think tank network.",
        "sources": [2622],
    },
    {
        "source": "Brookings Institution",
        "target": "Ford Foundation",
        "type": "funded_by",
        "tier": "documented",
        "desc": "The Ford Foundation has been a major funder of the Brookings Institution since the mid-20th century. Ford Foundation grants supported Brookings' expansion into international affairs and economic policy research. This funding relationship is part of the broader philanthropic-policy complex.",
        "sources": [2622, 2625],
    },

    # --- Carnegie Endowment for International Peace (0 rels → 2) ---
    {
        "source": "Andrew Carnegie",
        "target": "Carnegie Endowment for International Peace",
        "type": "founder_of",
        "tier": "documented",
        "desc": "Founded the Carnegie Endowment in 1910 with $10 million. One of several Carnegie institutions (Corporation, Foundation, libraries) that shaped US education, research, and foreign policy. Alger Hiss served as president of the Endowment (1946-1949) before his espionage conviction.",
        "year_start": 1910,
        "sources": [2623, 2680],
    },
    {
        "source": "Carnegie Endowment for International Peace",
        "target": "Council on Foreign Relations",
        "type": "affiliated_with",
        "tier": "credible",
        "desc": "Overlapping leadership and membership with the CFR since both institutions' early years. Carnegie Endowment focuses on international affairs research, complementing CFR's policy coordination role. Together they form part of the 'Eastern Establishment' foreign policy consensus.",
        "sources": [2623],
    },

    # --- Club of Rome (0 rels → 2) ---
    {
        "source": "Club of Rome",
        "target": "David Rockefeller",
        "type": "connected_to",
        "tier": "documented",
        "desc": "David Rockefeller was a supporter and connected figure in the Club of Rome's network. The Club's emphasis on global governance, resource management, and population issues aligned with Rockefeller's broader internationalist agenda through the Trilateral Commission and Council on Foreign Relations.",
        "sources": [2624, 2681],
    },
    {
        "source": "Club of Rome",
        "target": "Bilderberg Group",
        "type": "affiliated_with",
        "tier": "credible",
        "desc": "Overlapping membership between Club of Rome and Bilderberg Group. Both are elite forums for discussing global governance, economic policy, and resource management. Founded within three years of each other (Bilderberg 1954, Club of Rome 1968), they represent complementary nodes in the supranational policy network.",
        "sources": [2624],
    },

    # --- Chatham House (1 rel → 2) ---
    {
        "source": "Chatham House",
        "target": "Bilderberg Group",
        "type": "affiliated_with",
        "tier": "credible",
        "desc": "Chatham House members have been regular participants in Bilderberg Group meetings since the group's founding in 1954. Both institutions emerged from the Anglo-American policy establishment. The Chatham House Rule was adopted by Bilderberg for its private discussions.",
        "sources": [2628],
    },

    # --- Ford Foundation (1 rel → 3) ---
    {
        "source": "Ford Foundation",
        "target": "Church Committee",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "The Church Committee (1975-1976) documented the CIA's use of the Ford Foundation as a conduit for covert funding of cultural and intellectual organizations. The Foundation channeled CIA money to the Congress for Cultural Freedom and other front organizations during the Cold War.",
        "year_start": 1975,
        "sources": [2625, 2626],
    },
    {
        "source": "Ford Foundation",
        "target": "Council on Foreign Relations",
        "type": "funded",
        "tier": "documented",
        "desc": "Major funder of the Council on Foreign Relations. Ford Foundation grants supported CFR's expansion of membership, publications, and policy studies from the 1950s onward. This philanthropic-policy nexus shaped US foreign policy consensus for decades.",
        "sources": [2625],
    },

    # --- Open Society Foundations (1 rel → 2) ---
    {
        "source": "Open Society Foundations",
        "target": "Atlantic Council",
        "type": "funded",
        "tier": "documented",
        "desc": "Open Society Foundations has provided funding to the Atlantic Council, the NATO-aligned think tank focused on transatlantic relations and security policy. The OSF grant portfolio spans democracy promotion, civil society, and policy research organizations across 120+ countries.",
        "sources": [2627],
    },

    # ================================================================
    # JFK CLUSTER
    # ================================================================

    # --- Dealey Plaza (0 rels → 2) ---
    {
        "source": "JFK Assassination",
        "target": "Dealey Plaza",
        "type": "located_at",
        "tier": "documented",
        "desc": "President Kennedy was assassinated in Dealey Plaza, Dallas, Texas, on November 22, 1963. The site includes the Texas School Book Depository (Warren Commission lone gunman conclusion), the grassy knoll (HSCA acoustics evidence of second shooter), and the triple underpass.",
        "year_start": 1963,
        "sources": [2629],
    },
    {
        "source": "Dealey Plaza",
        "target": "Warren Commission",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "The Warren Commission investigated the assassination site, concluding all shots came from the sixth floor of the Texas School Book Depository overlooking Dealey Plaza. The HSCA later found acoustics evidence suggesting a second shooter from the grassy knoll area.",
        "year_start": 1964,
        "sources": [2629],
    },

    # --- ARRB (1 rel → 2) ---
    {
        "source": "ARRB",
        "target": "Warren Commission",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Assassination Records Review Board (1994-1998) was created by the JFK Records Act to review and release assassination records, including Warren Commission materials. Released millions of pages previously withheld. Found that the Warren Commission had failed to pursue significant investigative leads.",
        "year_start": 1994,
        "year_end": 1998,
        "sources": [2630],
    },

    # --- Operation 40 (1 rel → 2) ---
    {
        "source": "Operation 40",
        "target": "CIA",
        "type": "operated_by",
        "tier": "documented",
        "desc": "CIA-sponsored group of anti-Castro Cuban exiles created for the Bay of Pigs invasion. Included intelligence, sabotage, and assassination capabilities. Authorized by Allen Dulles. Members later connected to Watergate and other covert operations.",
        "year_start": 1960,
        "sources": [2632],
    },

    # --- ZR/RIFLE (1 rel → 3) ---
    {
        "source": "ZR/RIFLE",
        "target": "CIA",
        "type": "operated_by",
        "tier": "documented",
        "desc": "CIA 'executive action' (assassination) program run by William Harvey under the authority of Richard Helms. Recruited foreign assets for 'ichneumon' (agent) operations targeting foreign leaders. Revealed by the Church Committee in 1975.",
        "year_start": 1961,
        "sources": [2631],
    },
    {
        "source": "ZR/RIFLE",
        "target": "Church Committee",
        "type": "exposed_by",
        "tier": "documented",
        "desc": "The Church Committee's 1975 report 'Alleged Assassination Plots Involving Foreign Leaders' revealed the existence of ZR/RIFLE and documented CIA assassination capabilities. The committee's findings led to Executive Order 12333 banning assassinations.",
        "year_start": 1975,
        "sources": [2631],
    },

    # ================================================================
    # STARGATE / REMOTE VIEWING CLUSTER
    # ================================================================

    # --- Angela Dellafiora Ford (0 rels → 2) ---
    {
        "source": "Angela Dellafiora Ford",
        "target": "DIA",
        "type": "worked_for",
        "tier": "documented",
        "desc": "DIA civilian employee who served as a remote viewer in the Stargate program. Most famous for her 1989 session that accurately located fugitive Charles Jordan, identifying his location in Lowell, Wyoming, which was confirmed by US Customs agents.",
        "year_start": 1989,
        "sources": [2633, 2636],
    },
    {
        "source": "Angela Dellafiora Ford",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "One of the operational remote viewers in the DIA's Stargate program. Her successful location of fugitive Charles Jordan in 1989 is one of the most well-documented operational successes of the program.",
        "sources": [2633, 2636],
    },

    # --- Jessica Utts (0 rels → 2) ---
    {
        "source": "Jessica Utts",
        "target": "Project Stargate",
        "type": "connected_to",
        "tier": "documented",
        "desc": "UC Irvine statistics professor commissioned by the American Institutes for Research to provide independent statistical evaluation of the Stargate program (1995). Her analysis concluded that the statistical evidence for psychic functioning was overwhelming, with effect sizes far beyond chance.",
        "year_start": 1995,
        "sources": [2634, 2633],
    },
    {
        "source": "Jessica Utts",
        "target": "Stargate Declassification",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Her statistical analysis was a key component of the 1995 AIR review that accompanied the CIA's declassification of Project Stargate. Utts confirmed statistically significant results; skeptic Ray Hyman agreed the results were anomalous but proposed methodological critiques. The CIA terminated the program despite the positive statistical findings.",
        "year_start": 1995,
        "sources": [2634],
    },

    # --- Dale Graff (1 rel → 3) ---
    {
        "source": "Dale Graff",
        "target": "Project Stargate",
        "type": "directed",
        "tier": "documented",
        "desc": "Managed the Stargate remote viewing program from the DIA side, serving as both project officer and program director. Oversaw the transition from Army INSCOM management to DIA management. Personally experienced anomalous cognition events.",
        "sources": [2637, 2633],
    },
    {
        "source": "Dale Graff",
        "target": "Project Sun Streak",
        "type": "directed",
        "tier": "documented",
        "desc": "Served as project director for Project Sun Streak (1986-1990), the DIA-managed successor to Center Lane after the program was transferred from Army INSCOM. Sun Streak was later renamed Stargate in 1991.",
        "year_start": 1986,
        "year_end": 1990,
        "sources": [2637, 2633],
    },

    # --- Ed Dames (1 rel → 2) ---
    {
        "source": "Ed Dames",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Major (ret.), US Army. Served in the Stargate remote viewing unit at Fort Meade. While still active duty, co-founded PSI Tech (1989), one of the first commercial remote viewing companies, raising conflict-of-interest concerns.",
        "sources": [2633],
    },

    # --- Project Scanate (1 rel → 2) ---
    {
        "source": "Project Scanate",
        "target": "SRI International",
        "type": "located_at",
        "tier": "documented",
        "desc": "CIA's initial remote viewing evaluation was conducted at SRI International (formerly Stanford Research Institute) in Menlo Park, California, beginning in 1973. Ingo Swann and Pat Price demonstrated remote viewing capabilities that persuaded the CIA to continue funding.",
        "year_start": 1973,
        "sources": [2635, 2633],
    },

    # --- Project Grill Flame (1 rel → 2) ---
    {
        "source": "Project Grill Flame",
        "target": "DIA",
        "type": "operated_by",
        "tier": "documented",
        "desc": "US Army INSCOM remote viewing program (1978-1983) managed in coordination with DIA. First operational military remote viewing unit, housed at Fort Meade, Maryland. Successor to initial CIA work at SRI.",
        "year_start": 1978,
        "year_end": 1983,
        "sources": [2633],
    },

    # --- Project Sun Streak (1 rel → 2) ---
    {
        "source": "Project Sun Streak",
        "target": "DIA",
        "type": "operated_by",
        "tier": "documented",
        "desc": "DIA remote viewing program (1986-1990). Successor to Center Lane after the program was transferred from Army INSCOM to DIA management. Dale Graff served as project director. Later renamed Star Gate in 1991.",
        "year_start": 1986,
        "year_end": 1990,
        "sources": [2633],
    },

    # --- Gateway Process Report (1 rel → 2) ---
    {
        "source": "Gateway Process Report",
        "target": "Monroe Institute",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Lt. Col. Wayne McDonnell's 29-page classified analysis (1983) explaining how Monroe Institute techniques work through physics of consciousness. The report describes the Hemi-Sync process and proposes a theoretical framework connecting human consciousness to holographic universe models.",
        "year_start": 1983,
        "sources": [2638],
    },

    # --- Stargate Declassification (1 rel → 2) ---
    {
        "source": "Stargate Declassification",
        "target": "Project Stargate",
        "type": "connected_to",
        "tier": "documented",
        "desc": "CIA declassified Project Stargate in 1995. The AIR review found: statistician Jessica Utts confirmed results showed statistical significance far beyond chance; skeptic Ray Hyman agreed results were anomalous. Despite positive findings, the CIA terminated the program and released 89,000+ pages of documents.",
        "year_start": 1995,
        "sources": [2633, 2634],
    },

    # ================================================================
    # FOOD / AGRICULTURE CLUSTER
    # ================================================================

    # --- Bayer (1 rel → 3) ---
    {
        "source": "Bayer",
        "target": "Monsanto",
        "type": "acquired",
        "tier": "documented",
        "desc": "Acquired Monsanto for $63 billion in 2018. Absorbed Monsanto's seed technology, herbicide business, and all legal liabilities. By 2024 had paid $10.9+ billion to settle Roundup cancer lawsuits, making it one of the most disastrous corporate acquisitions in history.",
        "year_start": 2018,
        "sources": [2639],
    },
    {
        "source": "Bayer",
        "target": "Roundup Cancer Litigation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Inherited approximately 100,000 Roundup cancer lawsuits when it acquired Monsanto. Bayer agreed to $10.9 billion settlement in 2020 but ongoing litigation continues. The litigation revealed internal Monsanto documents showing suppressed cancer risk data.",
        "year_start": 2018,
        "sources": [2639, 2645],
    },

    # --- Robert Fraley (0 rels → 2) ---
    {
        "source": "Robert Fraley",
        "target": "Monsanto",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Chief Technology Officer of Monsanto. Pioneer of plant cell transformation technology that enabled genetically modified crops. Co-recipient of the 2013 World Food Prize. Oversaw the company's GMO technology portfolio during its most aggressive period of patent enforcement and farmer litigation.",
        "sources": [2640],
    },
    {
        "source": "Robert Fraley",
        "target": "Monsanto Papers",
        "type": "connected_to",
        "tier": "credible",
        "desc": "As CTO during the period covered by the Monsanto Papers revelations, Fraley oversaw the scientific strategy that included ghostwriting academic papers and suppressing evidence of glyphosate health risks. The Monsanto Papers exposed the gap between internal knowledge and public messaging.",
        "sources": [2640, 2646],
    },

    # --- DARK Act (0 rels → 2) ---
    {
        "source": "DARK Act",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Monsanto was a leading corporate lobbyist for the National Bioengineered Food Disclosure Standard (2016), nicknamed the DARK Act ('Deny Americans the Right to Know'). The law preempted stronger state-level GMO labeling requirements including Vermont's pioneering mandatory labeling law.",
        "year_start": 2016,
        "sources": [2641],
    },
    {
        "source": "DARK Act",
        "target": "USDA",
        "type": "regulated_by",
        "tier": "documented",
        "desc": "Assigned USDA responsibility for implementing national GMO disclosure standards, which critics argued were deliberately weaker than the state-level labeling laws they preempted. The USDA's 'bioengineered' disclosure system allows QR codes rather than clear labels.",
        "year_start": 2016,
        "sources": [2641],
    },

    # --- Monsanto Protection Act (0 rels → 2) ---
    {
        "source": "Monsanto Protection Act",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Section 735 of H.R. 933 (2013), officially the 'Farmer Assurance Provision.' Anonymous rider widely attributed to Sen. Roy Blunt, reportedly drafted with Monsanto's input. Stripped federal courts of authority to halt the planting of GMO crops pending safety reviews.",
        "year_start": 2013,
        "year_end": 2013,
        "sources": [2642],
    },
    {
        "source": "Monsanto Protection Act",
        "target": "USDA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Required USDA to issue temporary permits for GMO crop planting even if a court found the crops had not been properly approved. Critics called it a direct attack on judicial oversight of agricultural biotechnology regulation.",
        "year_start": 2013,
        "sources": [2642],
    },

    # --- Indian Farmer Suicides (0 rels → 2) ---
    {
        "source": "Indian Farmer Suicides",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Over 300,000 Indian farmers have died by suicide since 1995, disproportionately in regions that adopted Bt cotton and other cash crops requiring purchased seeds and inputs. Monsanto's seed patents and the shift from saved seeds to purchased GMO seeds contributed to crushing debt cycles.",
        "sources": [2643],
    },
    {
        "source": "Indian Farmer Suicides",
        "target": "Vandana Shiva",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Vandana Shiva has been the most prominent international voice linking Indian farmer suicides to corporate seed monopolies. Her advocacy and research through the Research Foundation for Science, Technology and Ecology documented the connection between seed debt and farmer deaths.",
        "sources": [2643, 2649],
    },

    # --- Terminator Seeds (1 rel → 2) ---
    {
        "source": "Terminator Seeds",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Monsanto acquired Delta & Pine Land Company (2007), the company that co-developed terminator seed technology (GURT) with the USDA. Though Monsanto pledged not to commercialize sterile-seed technology, the acquisition gave it control of the patents.",
        "year_start": 2007,
        "sources": [2644],
    },

    # --- Monsanto Papers (1 rel → 2) ---
    {
        "source": "Monsanto Papers",
        "target": "Monsanto",
        "type": "exposed",
        "tier": "documented",
        "desc": "Internal Monsanto documents revealed through Roundup cancer litigation discovery (2017+). Showed Monsanto ghostwrote scientific papers published under academics' names, suppressed cancer risk evidence, orchestrated campaigns to discredit IARC, and maintained lists of 'friendly' scientists.",
        "year_start": 2017,
        "sources": [2646],
    },

    # --- Roundup Cancer Litigation (1 rel → 2) ---
    {
        "source": "Roundup Cancer Litigation",
        "target": "Bayer",
        "type": "targeted",
        "tier": "documented",
        "desc": "Approximately 100,000 plaintiffs alleged Monsanto/Bayer's Roundup herbicide caused non-Hodgkin lymphoma. Bayer inherited all liability through the $63B Monsanto acquisition. First verdict (Johnson v. Monsanto, 2018) awarded $289M. Bayer settled for $10.9B (2020).",
        "year_start": 2018,
        "sources": [2645, 2639],
    },

    # --- ADM Price-Fixing Scandal (1 rel → 2) ---
    {
        "source": "ADM Price-Fixing Scandal",
        "target": "FBI",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "FBI investigation based on informant Mark Whitacre, who secretly recorded ADM executives participating in a global lysine and citric acid price-fixing cartel (1992-1995). The FBI's wire recordings were among the most extensive white-collar crime evidence ever gathered.",
        "year_start": 1995,
        "sources": [2647],
    },

    # --- Codex Alimentarius Commission (1 rel → 2) ---
    {
        "source": "Codex Alimentarius Commission",
        "target": "WHO",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": "Joint body of the WHO and FAO established in 1963 to develop international food standards. Codex standards influence food regulation worldwide. Critics argue that corporate participation allows agrochemical and food industry interests to shape standards that affect public health.",
        "year_start": 1963,
        "sources": [2648],
    },

    # ================================================================
    # UK ABUSE INVESTIGATIONS
    # ================================================================

    # --- Cyril Smith (1 rel → 3) ---
    {
        "source": "Cyril Smith",
        "target": "Metropolitan Police",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "Lancashire Police confirmed after Smith's death in 2010 that they had received multiple complaints of abuse against children. Files were reportedly passed to MI5 and Special Branch rather than prosecutors. The Crown Prosecution Service later confirmed Smith should have been prosecuted.",
        "sources": [2650],
    },
    {
        "source": "Cyril Smith",
        "target": "MI5",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Multiple sources including former intelligence officers allege MI5 was aware of Smith's abuse and suppressed evidence to protect him as a politically useful figure. Smith was knighted in 1988 despite the accumulated complaints. The suppression pattern mirrors other cases in the Westminster dossier.",
        "sources": [2650],
    },

    # --- Operation Yewtree (1 rel → 3) ---
    {
        "source": "Operation Yewtree",
        "target": "Metropolitan Police",
        "type": "operated_by",
        "tier": "documented",
        "desc": "Metropolitan Police investigation established in October 2012 in the wake of the Jimmy Savile abuse revelations. Conducted under three strands investigating allegations directly against Savile, those related to Savile, and those involving other public figures.",
        "year_start": 2012,
        "sources": [2651],
    },
    {
        "source": "Operation Yewtree",
        "target": "Jimmy Savile",
        "type": "investigated",
        "tier": "documented",
        "desc": "Established in direct response to the ITV Exposure documentary (October 2012) that publicly exposed Jimmy Savile's decades of sexual abuse. The investigation identified over 450 victims across NHS hospitals, BBC facilities, and other institutions.",
        "year_start": 2012,
        "sources": [2651],
    },

    # --- Operation Midland (1 rel → 2) ---
    {
        "source": "Operation Midland",
        "target": "Metropolitan Police",
        "type": "operated_by",
        "tier": "documented",
        "desc": "Metropolitan Police investigation (2014-2016) into allegations of a VIP child abuse and murder ring at Dolphin Square and other London locations. Based primarily on the testimony of Carl Beech ('Nick'), who was later convicted of fabricating allegations. Investigation cost over three million pounds and was widely criticized.",
        "year_start": 2014,
        "year_end": 2016,
        "sources": [2652],
    },

    # ================================================================
    # BIOWEAPONS / HEALTH
    # ================================================================

    # --- DTRA (1 rel → 2) ---
    {
        "source": "DTRA",
        "target": "USAMRIID",
        "type": "connected_to",
        "tier": "documented",
        "desc": "DTRA and USAMRIID both operate within the defense biological research ecosystem. DTRA oversees the Cooperative Threat Reduction program (Nunn-Lugar) for dismantling former Soviet WMD infrastructure, while USAMRIID conducts biological defense research at Fort Detrick.",
        "sources": [2653],
    },

    # --- Fort Detrick Lab Shutdown (1 rel → 2) ---
    {
        "source": "Fort Detrick Lab Shutdown",
        "target": "CDC",
        "type": "connected_to",
        "tier": "documented",
        "desc": "In August 2019, the CDC ordered USAMRIID at Fort Detrick to halt all research on dangerous pathogens after inspection found failures in wastewater decontamination. The shutdown occurred months before the COVID-19 pandemic, prompting speculation about timing that remains unverified.",
        "year_start": 2019,
        "sources": [2654, 2687],
    },

    # --- Sverdlovsk Anthrax Leak (1 rel → 2) ---
    {
        "source": "Sverdlovsk Anthrax Leak",
        "target": "Ken Alibek",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Ken Alibek (Kanatjan Alibekov), as First Deputy Director of Biopreparat, later confirmed the Soviet government's cover story was false and that the 1979 Sverdlovsk anthrax release was from a military biological weapons facility, not contaminated meat as officially claimed.",
        "year_start": 1992,
        "sources": [2655, 2656],
    },

    # --- CDC (1 rel → 2) ---
    {
        "source": "CDC",
        "target": "NIH",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": "Both agencies operate within the Department of Health and Human Services. CDC focuses on disease control and public health while NIH leads biomedical research. Their coordinated response to public health emergencies and shared oversight of biosafety laboratories link them institutionally.",
        "sources": [2687],
    },

    # ================================================================
    # WATER
    # ================================================================

    # --- Flint Water Crisis (1 rel → 2) ---
    {
        "source": "Flint Water Crisis",
        "target": "CDC",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "CDC conducted health investigations and blood lead level testing during the Flint water crisis (2014-2019). Lead contamination from corroded pipes affected an estimated 100,000 residents after the city switched water sources under emergency management.",
        "year_start": 2014,
        "sources": [2657, 2687],
    },

    # --- Detroit Water Shutoffs (1 rel → 2) ---
    {
        "source": "Detroit Water Shutoffs",
        "target": "Nestlé Waters",
        "type": "connected_to",
        "tier": "credible",
        "desc": "While Detroit shut off water to over 100,000 residents for unpaid bills (some as low as $150), Nestle was paying approximately $200 per year to pump 400 gallons per minute from Michigan aquifers. The contrast between corporate water extraction and residential shutoffs became a focal point of water justice advocacy.",
        "year_start": 2014,
        "sources": [2658, 2685],
    },

    # ================================================================
    # OTHER
    # ================================================================

    # --- Anderson Cooper (1 rel → 2) ---
    {
        "source": "Anderson Cooper",
        "target": "Dalton School",
        "type": "attended",
        "tier": "documented",
        "desc": "Attended the elite Dalton School in Manhattan as a child. Dalton School was also where Donald Barr (father of AG William Barr) served as headmaster and where Jeffrey Epstein was hired as a teacher despite lacking a college degree.",
        "sources": [2659],
    },

    # --- Smedley Butler (1 rel → 2) ---
    {
        "source": "Smedley Butler",
        "target": "Standard Oil",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Butler's 1935 book 'War Is a Racket' specifically named Standard Oil among the corporations that profited from US military interventions he was ordered to conduct. He wrote: 'I helped make Mexico safe for American oil interests' and called himself 'a racketeer, a gangster for capitalism.'",
        "year_start": 1935,
        "sources": [2662],
    },

    # --- Jacobo Árbenz (1 rel → 2) ---
    {
        "source": "Jacobo Árbenz",
        "target": "United Fruit Company",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Árbenz's Decree 900 agrarian reform (1952) expropriated uncultivated land from large estates including 200,000+ acres held by the United Fruit Company. UFC lobbied the Eisenhower administration for intervention. Allen Dulles, whose law firm Sullivan & Cromwell had represented UFC, authorized the CIA coup.",
        "year_start": 1952,
        "year_end": 1954,
        "sources": [2663, 2684],
    },

    # --- Hill & Knowlton (1 rel → 2) ---
    {
        "source": "Hill & Knowlton",
        "target": "CIA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Under Robert Keith Gray's leadership, Hill & Knowlton served as a cover and conduit for CIA influence operations. The firm's work on the incubator babies testimony before Congress (1990, justifying Gulf War) is the most documented case of PR-intelligence convergence.",
        "sources": [2670],
    },

    # --- George Town Club (1 rel → 2) ---
    {
        "source": "George Town Club",
        "target": "Craig Spence",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Craig Spence, the Republican lobbyist connected to the Franklin Cover-Up scandal, used the George Town Club for hosting events and entertaining contacts. The club functioned as a nexus for Washington power brokers, intelligence operatives, and political fixers.",
        "sources": [2679],
    },

    # --- Internet Research Agency (1 rel → 3) ---
    {
        "source": "Internet Research Agency",
        "target": "Vladimir Putin",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Linked to Vladimir Putin through founder Yevgeny Prigozhin, a Putin ally known as 'Putin's chef.' Mueller investigation indicted the IRA and 13 Russian nationals for conspiracy to defraud the United States through social media interference in the 2016 election.",
        "sources": [2665, 2666],
    },
    {
        "source": "Internet Research Agency",
        "target": "FSB",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The IRA's operations were conducted alongside broader Russian state intelligence operations targeting US elections. GRU (military intelligence) conducted the DNC hack while the IRA handled social media operations, with FSB providing counterintelligence support for the overall campaign.",
        "sources": [2665, 2666],
    },

    # --- Eisenhower Farewell Address (1 rel → 2) ---
    {
        "source": "Eisenhower Farewell Address",
        "target": "The Pentagon",
        "type": "connected_to",
        "tier": "documented",
        "desc": "President Eisenhower's January 17, 1961 farewell address specifically warned about the 'military-industrial complex' and its 'unwarranted influence' — a five-star general and two-term president warning about the system he had led. The Pentagon was the institutional center of the complex he described.",
        "year_start": 1961,
        "sources": [2667],
    },

    # --- Gulf of Tonkin Resolution (1 rel → 2) ---
    {
        "source": "Gulf of Tonkin Resolution",
        "target": "Joint Chiefs of Staff",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Joint Chiefs of Staff had been seeking congressional authorization for expanded military operations in Vietnam. The Gulf of Tonkin Resolution (1964) provided exactly that, authorizing presidential use of military force without a formal declaration of war. Later revealed to be based on a fabricated second attack.",
        "year_start": 1964,
        "sources": [2668],
    },

    # --- Smith-Mundt Modernization Act (1 rel → 2) ---
    {
        "source": "Smith-Mundt Modernization Act",
        "target": "Pentagon Military Analyst Program",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The 2012 amendment legalizing domestic dissemination of US government-produced media came after the Pentagon Military Analyst Program scandal (2008), which revealed the Pentagon had recruited retired military officers to serve as media surrogates promoting administration policies on broadcast networks.",
        "year_start": 2012,
        "sources": [2669],
    },

    # --- DuPont Family (1 rel → 2) ---
    {
        "source": "DuPont Family",
        "target": "Prescott Bush",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The DuPont family's industrial and political networks overlapped with the Bush family through business and banking connections in the 1930s-1940s. Both families were implicated in the Business Plot era, with the McCormack-Dickstein Committee investigating Wall Street interests connected to DuPont, Morgan, and Remington.",
        "sources": [2660, 2682],
    },

    # --- Pujo Committee (1 rel → 2) ---
    {
        "source": "Pujo Committee",
        "target": "Federal Reserve System",
        "type": "preceded",
        "tier": "documented",
        "desc": "The Pujo Committee's 1913 findings on the 'money trust' directly led to the Federal Reserve Act of 1913. The Committee documented that Morgan, Rockefeller, and allied interests controlled the boards of 112 corporations worth $22.2 billion. The Federal Reserve was ostensibly created to diffuse this concentration of financial power.",
        "year_start": 1913,
        "sources": [2661],
    },

    # --- Carnivore (1 rel → 2) ---
    {
        "source": "Carnivore",
        "target": "ECHELON",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Carnivore (FBI internet surveillance) and ECHELON (Five Eyes signals intelligence) represented complementary pillars of the pre-9/11 surveillance apparatus. While Carnivore monitored domestic internet traffic at ISP facilities, ECHELON intercepted international communications. Both programs expanded dramatically after the USA PATRIOT Act.",
        "sources": [2664],
    },

    # --- ATF (1 rel → 2) ---
    {
        "source": "ATF",
        "target": "DOJ",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": "Bureau of Alcohol, Tobacco, Firearms and Explosives was transferred from the Department of the Treasury to the Department of Justice in 2003 under the Homeland Security Act. ATF's enforcement role in firearms and explosives placed it at the center of controversies including Waco and Operation Fast and Furious.",
        "year_start": 2003,
        "sources": [2673],
    },

    # --- Cali Cartel (1 rel → 3) ---
    {
        "source": "Cali Cartel",
        "target": "DEA",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "DEA's primary target in Colombia during the 1990s after the Medellin Cartel's decline. The Rodriguez Orejuela brothers (Gilberto and Miguel) were arrested in 1995 and extradited to the US in 2004. At its peak, the Cali Cartel controlled an estimated 80% of the world's cocaine supply.",
        "year_start": 1990,
        "year_end": 2004,
        "sources": [2672],
    },
    {
        "source": "Cali Cartel",
        "target": "Medellín Cartel",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Cali and Medellin cartels were rivals who competed for control of the global cocaine trade. The Cali Cartel covertly supported Colombian government efforts against Pablo Escobar's Medellin Cartel through the 'Los Pepes' vigilante group, then dominated the cocaine trade after Escobar's death in 1993.",
        "sources": [2672],
    },

    # --- Robert Maxwell Death (1991) (1 rel → 2) ---
    {
        "source": "Robert Maxwell Death (1991)",
        "target": "Mossad",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Robert Maxwell received an Israeli state funeral attended by six serving and former heads of Israeli intelligence, including Mossad directors. Former Mossad operative Ari Ben-Menashe has stated Maxwell was a Mossad asset. His death aboard his yacht Lady Ghislaine occurred as his financial empire was collapsing and his intelligence value was declining.",
        "year_start": 1991,
        "sources": [2671],
    },

    # --- Thule Society (1 rel → 2) ---
    {
        "source": "Thule Society",
        "target": "Operation Paperclip",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The Thule Society's volkisch-occult ideology fed directly into the Nazi Party apparatus. After WWII, Operation Paperclip recruited German scientists and intelligence operatives, some of whom had connections to the ideological networks that included the Thule Society's nationalist-esoteric worldview.",
        "sources": [2674],
    },

    # --- Temple of Set (1 rel → 2) ---
    {
        "source": "Temple of Set",
        "target": "Presidio Abuse Case",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Temple of Set founder Lt. Col. Michael Aquino was investigated by the Army CID in connection with the Presidio child abuse case (1986-1987). Aquino was stationed at the Presidio and was named in allegations by parents. No charges were filed. The case involved multiple children at the Presidio day care center.",
        "year_start": 1986,
        "sources": [2675],
    },

    # --- Process Church (1 rel → 2) ---
    {
        "source": "Process Church of the Final Judgment",
        "target": "L. Ron Hubbard",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Robert and Mary Ann DeGrimston, founders of the Process Church, were former Scientologists who applied L. Ron Hubbard's techniques to create their own movement. They met within the Church of Scientology and adapted Scientology processing methods for their new organization.",
        "year_start": 1963,
        "sources": [2676],
    },

    # --- Wright-Patterson AFB (1 rel → 2) ---
    {
        "source": "Wright-Patterson AFB",
        "target": "Project Blue Book",
        "type": "located_at",
        "tier": "documented",
        "desc": "Wright-Patterson Air Force Base in Dayton, Ohio was the headquarters of Project Blue Book (1952-1969), the US Air Force's systematic study of UFOs. The base's Foreign Technology Division also analyzed recovered foreign aerospace materials. Historical reports place alleged recovered UAP materials at the facility.",
        "year_start": 1952,
        "year_end": 1969,
        "sources": [2677],
    },

    # --- DGSE (1 rel → 2) ---
    {
        "source": "DGSE",
        "target": "NATO",
        "type": "connected_to",
        "tier": "documented",
        "desc": "France's external intelligence service cooperates with NATO allies on counterterrorism, military intelligence, and counterintelligence. Despite France's periodic tensions with NATO (De Gaulle withdrew from NATO military command 1966, France returned 2009), DGSE maintains intelligence-sharing relationships.",
        "sources": [2686],
    },

    # --- Blaise Metreweli (1 rel → 2) ---
    {
        "source": "Blaise Metreweli",
        "target": "Five Eyes",
        "type": "connected_to",
        "tier": "documented",
        "desc": "As Chief of MI6, Metreweli leads the UK's contribution to the Five Eyes intelligence alliance. The MI6 Chief is one of the senior officials in the anglophone intelligence partnership alongside the directors of CIA, NSA, GCHQ, ASIS, and counterpart agencies.",
        "year_start": 2025,
        "sources": [2688],
    },

    # --- United Grand Lodge of England (1 rel → 2) ---
    {
        "source": "United Grand Lodge of England",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Both are governing bodies of Freemasonry — UGLE for Craft Masonry in England, Wales, and the Channel Islands; the Scottish Rite SJ for the appendant Scottish Rite degrees in the US. Their recognition and correspondence relationships define the boundaries of 'regular' Freemasonry worldwide.",
        "sources": [2683],
    },
]

# ============================================================
# ENTITY → SOURCE mappings (empty — no new entities)
# ============================================================

ENTITY_SOURCES = {}

# ============================================================
# ENTITY UPDATES
# ============================================================

ENTITY_UPDATES = []

# ============================================================
# GEO_COORDS (empty — no new entities)
# ============================================================

GEO_COORDS = {}

# ============================================================
# PHOTO_CANDIDATES (empty — no new entities)
# ============================================================

PHOTO_CANDIDATES = {}
