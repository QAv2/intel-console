"""
False Flag Operations & Covert Regime Change — Expansion layer for Intel Console.

Maps the documented history of staged provocations, fabricated pretexts, and
CIA/military covert operations used to justify wars, topple governments, and
suppress domestic dissent. Every entry here is sourced from declassified
government documents, congressional investigations, FOIA releases, court
records, or peer-reviewed academic research.

The pattern: propose or execute a covert operation, control the narrative,
classify the evidence, wait 20-50 years, declassify when it no longer matters.
Northwoods was rejected — but the playbook it codified (stage an attack on
your own people, blame the enemy, use the crisis to justify military action)
recurs across decades.

Entities (~20): Operations (Northwoods, Gulf of Tonkin, Gladio, USS Liberty,
Ajax, PBSuccess, Paperclip), people (Lemnitzer, Mossadegh, Árbenz, Ganser,
Fred Hampton), organizations (NATO, Joint Chiefs of Staff), and the connecting
tissue between them.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], FBI [87], NSA [86], Mossad [88], DOJ [89],
  Allen Dulles [JFK expansion], J. Edgar Hoover [16],
  George H.W. Bush [242], Dick Cheney [244], Donald Rumsfeld [245],
  Henry Kissinger [111], Church Committee [media expansion],
  COINTELPRO [curated], Operation Mockingbird [media expansion],
  Operation Condor [latin_america expansion], PNAC [911 expansion],
  JFK Assassination [jfk expansion]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 871-900
# ============================================================

SOURCES = [
    # --- Northwoods ---
    {
        "id": 871,
        "title": "Memorandum from the Joint Chiefs of Staff to the Secretary of Defense — 'Justification for US Military Intervention in Cuba' (Operation Northwoods), March 13, 1962",
        "url": "https://nsarchive2.gwu.edu/news/20010430/northwoods.pdf",
        "source_type": "foia",
        "year": 1962,
    },
    {
        "id": 872,
        "title": "James Bamford — Body of Secrets: Anatomy of the Ultra-Secret National Security Agency (Chapter 4: Northwoods)",
        "url": "https://en.wikipedia.org/wiki/Body_of_Secrets",
        "source_type": "book",
        "author": "James Bamford",
        "year": 2001,
    },
    # --- Gulf of Tonkin ---
    {
        "id": 873,
        "title": "NSA Declassified Report — 'Skunks, Bogies, Silent Hounds, and the Flying Fish: The Gulf of Tonkin Mystery, 2-4 August 1964' by Robert J. Hanyok",
        "url": "https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/gulf-of-tonkin/articles/rel1_gulf_of_tonkin_article.pdf",
        "source_type": "foia",
        "author": "Robert J. Hanyok",
        "year": 2001,
    },
    {
        "id": 874,
        "title": "Senate Foreign Relations Committee — 'The Gulf of Tonkin, The 1964 Incidents' (hearing transcripts, declassified 2010)",
        "url": "https://www.govinfo.gov/content/pkg/CHRG-111shrg54772/pdf/CHRG-111shrg54772.pdf",
        "source_type": "congressional",
        "year": 2010,
    },
    {
        "id": 875,
        "title": "Gulf of Tonkin Resolution — Public Law 88-408 (signed August 10, 1964)",
        "url": "https://www.archives.gov/milestone-documents/gulf-of-tonkin-resolution",
        "source_type": "government",
        "year": 1964,
    },
    # --- Operation Gladio ---
    {
        "id": 876,
        "title": "Daniele Ganser — NATO's Secret Armies: Operation Gladio and Terrorism in Western Europe",
        "url": "https://en.wikipedia.org/wiki/NATO%27s_Secret_Armies",
        "source_type": "academic",
        "author": "Daniele Ganser",
        "year": 2005,
    },
    {
        "id": 877,
        "title": "European Parliament Resolution on Gladio (November 22, 1990) — condemned existence of clandestine stay-behind networks",
        "url": "https://www.europarl.europa.eu/sides/getDoc.do?pubRef=-//EP//TEXT+MOTION+B3-1990-2021+0+DOC+XML+V0//EN",
        "source_type": "government",
        "year": 1990,
    },
    {
        "id": 878,
        "title": "Italian Senate Commission on Terrorism — Investigation into the Strategy of Tension and Gladio networks in Italy",
        "url": "https://en.wikipedia.org/wiki/Strategy_of_tension#Italy",
        "source_type": "government",
        "year": 2000,
    },
    {
        "id": 879,
        "title": "Giulio Andreotti — Italian Prime Minister's disclosure to parliament confirming Gladio's existence (October 24, 1990)",
        "url": "https://en.wikipedia.org/wiki/Operation_Gladio#Disclosure",
        "source_type": "government",
        "year": 1990,
    },
    # --- USS Liberty ---
    {
        "id": 880,
        "title": "USS Liberty Memorial Library — declassified NSA intercepts, crew testimony, and Navy court of inquiry records",
        "url": "https://www.ussliberty.org/",
        "source_type": "archive",
        "year": 1967,
    },
    {
        "id": 881,
        "title": "James Scott — The Attack on the Liberty: The Untold Story of Israel's Deadly 1967 Assault on a U.S. Spy Ship",
        "url": "https://en.wikipedia.org/wiki/The_Attack_on_the_Liberty",
        "source_type": "book",
        "author": "James Scott",
        "year": 2009,
    },
    {
        "id": 882,
        "title": "Admiral Thomas Moorer (former JCS Chairman) — statement to USS Liberty Independent Commission of Inquiry finding Israel's attack was deliberate",
        "url": "https://www.ussliberty.org/findings.htm",
        "source_type": "other",
        "author": "Thomas Moorer",
        "year": 2003,
    },
    # --- Operation Ajax ---
    {
        "id": 883,
        "title": "CIA Declassified Internal History — 'Overthrow of Premier Mossadeq of Iran, November 1952 – August 1953' (written by Donald Wilber, declassified 2013)",
        "url": "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB435/",
        "source_type": "foia",
        "author": "Donald N. Wilber",
        "year": 2013,
    },
    {
        "id": 884,
        "title": "Ervand Abrahamian — The Coup: 1953, the CIA, and the Roots of Modern U.S.–Iranian Relations",
        "url": "https://en.wikipedia.org/wiki/The_Coup:_1953,_the_CIA,_and_the_Roots_of_Modern_U.S.%E2%80%93Iranian_Relations",
        "source_type": "academic",
        "author": "Ervand Abrahamian",
        "year": 2013,
    },
    {
        "id": 885,
        "title": "State Department — Foreign Relations of the United States, 1952–1954, Iran, 1951–1954 (declassified diplomatic history)",
        "url": "https://history.state.gov/historicaldocuments/frus1951-54Iran",
        "source_type": "government",
        "year": 2017,
    },
    # --- Operation PBSuccess ---
    {
        "id": 886,
        "title": "CIA Declassified Records — 'PBSUCCESS: The United States and Guatemala, 1952–1954' (CIA History Staff, Kate Doyle / National Security Archive)",
        "url": "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB4/",
        "source_type": "foia",
        "year": 1997,
    },
    {
        "id": 887,
        "title": "Stephen Schlesinger & Stephen Kinzer — Bitter Fruit: The Story of the American Coup in Guatemala",
        "url": "https://en.wikipedia.org/wiki/Bitter_Fruit:_The_Story_of_the_American_Coup_in_Guatemala",
        "source_type": "book",
        "author": "Stephen Schlesinger, Stephen Kinzer",
        "year": 1982,
    },
    {
        "id": 888,
        "title": "Guatemala Truth Commission (CEH) — 'Guatemala: Memory of Silence' — documented 200,000 killed, attributed 93% of human rights violations to state forces and CIA-backed paramilitaries",
        "url": "https://hrdag.org/wp-content/uploads/2013/01/CEHreport-english.pdf",
        "source_type": "government",
        "year": 1999,
    },
    # --- Operation Paperclip ---
    {
        "id": 889,
        "title": "Annie Jacobsen — Operation Paperclip: The Secret Intelligence Program That Brought Nazi Scientists to America",
        "url": "https://en.wikipedia.org/wiki/Operation_Paperclip_(book)",
        "source_type": "book",
        "author": "Annie Jacobsen",
        "year": 2014,
    },
    {
        "id": 890,
        "title": "National Archives — Records of the Joint Intelligence Objectives Agency (JIOA), Operation Paperclip Case Files",
        "url": "https://www.archives.gov/iwg/declassified-records/rg-330-defense-secretary",
        "source_type": "archive",
        "year": 2006,
    },
    {
        "id": 891,
        "title": "Linda Hunt — Secret Agenda: The United States Government, Nazi Scientists, and Project Paperclip, 1945 to 1990",
        "url": "https://en.wikipedia.org/wiki/Secret_Agenda_(book)",
        "source_type": "book",
        "author": "Linda Hunt",
        "year": 1991,
    },
    # --- COINTELPRO / Fred Hampton ---
    {
        "id": 892,
        "title": "Church Committee — 'Intelligence Activities and the Rights of Americans' (Book II) — FBI COINTELPRO findings",
        "url": "https://www.intelligence.senate.gov/sites/default/files/94755_II.pdf",
        "source_type": "congressional",
        "year": 1976,
    },
    {
        "id": 893,
        "title": "FBI COINTELPRO Files — declassified documents detailing disruption of Black Panther Party, SCLC, AIM, New Left (FOIA release)",
        "url": "https://vault.fbi.gov/cointel-pro",
        "source_type": "foia",
        "year": 1976,
    },
    {
        "id": 894,
        "title": "Hampton v. Hanrahan — Federal civil rights lawsuit establishing FBI/CPD conspiracy in Fred Hampton assassination ($1.85 million settlement)",
        "url": "https://law.justia.com/cases/federal/appellate-courts/F2/600/600/",
        "source_type": "court",
        "year": 1982,
    },
    {
        "id": 895,
        "title": "Jeffrey Haas — The Assassination of Fred Hampton: How the FBI and the Chicago Police Murdered a Black Panther",
        "url": "https://en.wikipedia.org/wiki/The_Assassination_of_Fred_Hampton_(book)",
        "source_type": "book",
        "author": "Jeffrey Haas",
        "year": 2010,
    },
    # --- General / Cross-Cutting ---
    {
        "id": 896,
        "title": "Stephen Kinzer — The Brothers: John Foster Dulles, Allen Dulles, and Their Secret World War (details Ajax, PBSuccess, and Dulles brothers' corporate-intelligence nexus)",
        "url": "https://en.wikipedia.org/wiki/The_Brothers_(Kinzer_book)",
        "source_type": "book",
        "author": "Stephen Kinzer",
        "year": 2013,
    },
    {
        "id": 897,
        "title": "Stephen Kinzer — Overthrow: America's Century of Regime Change from Hawaii to Iraq",
        "url": "https://en.wikipedia.org/wiki/Overthrow_(book)",
        "source_type": "book",
        "author": "Stephen Kinzer",
        "year": 2006,
    },
    {
        "id": 898,
        "title": "William Blum — Killing Hope: U.S. Military and CIA Interventions Since World War II",
        "url": "https://en.wikipedia.org/wiki/Killing_Hope",
        "source_type": "book",
        "author": "William Blum",
        "year": 1995,
    },
    {
        "id": 899,
        "title": "Pike Committee — House Select Committee on Intelligence (1975-76) — leaked report on CIA covert operations, assassination programs, and domestic surveillance",
        "url": "https://en.wikipedia.org/wiki/Pike_Committee",
        "source_type": "congressional",
        "year": 1976,
    },
    {
        "id": 900,
        "title": "Truman Directive on Nazi Scientists — original Truman order (September 1946) explicitly barred 'ardent Nazis,' later circumvented by JIOA bleaching of dossiers",
        "url": "https://www.archives.gov/iwg/declassified-records/rg-330-defense-secretary",
        "source_type": "government",
        "year": 1946,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Operations / Events ---
    {
        "name": "Operation Northwoods",
        "entity_type": "program",
        "description": (
            "Joint Chiefs of Staff proposal (March 13, 1962) to stage false flag attacks "
            "against US military and civilian targets — including sinking refugee boats, "
            "hijacking planes, bombing Miami, and attacking Guantanamo Bay — to manufacture "
            "a pretext for invading Cuba. Signed by JCS Chairman Lyman Lemnitzer and all "
            "Joint Chiefs. Rejected by Secretary of Defense Robert McNamara and President "
            "Kennedy. Declassified in 2001 via JFK Assassination Records Review Board. "
            "The document proves the highest level of US military leadership was willing to "
            "propose killing American citizens to justify a war."
        ),
        "aliases": "Northwoods",
        "metadata": {"type": "false flag proposal", "date": "1962-03-13"},
    },
    {
        "name": "Gulf of Tonkin Incident",
        "entity_type": "event",
        "description": (
            "Two alleged naval engagements between USS Maddox and North Vietnamese torpedo "
            "boats in August 1964. The first incident (Aug 2) was real but provoked by US/South "
            "Vietnamese covert raids. The second incident (Aug 4) — the one used to justify "
            "escalation — never happened. NSA historian Robert Hanyok's internal study (2001, "
            "declassified 2005) found NSA officers had deliberately falsified intelligence "
            "to support the claim of a second attack. The fabricated incident was used to pass "
            "the Gulf of Tonkin Resolution, which authorized military force in Vietnam without "
            "a formal declaration of war. Over 58,000 US and 2-3 million Vietnamese deaths "
            "followed."
        ),
        "aliases": "Tonkin Gulf, Gulf of Tonkin",
        "metadata": {"type": "fabricated provocation", "date": "1964-08-04"},
    },
    {
        "name": "Gulf of Tonkin Resolution",
        "entity_type": "legislation",
        "description": (
            "Joint resolution of Congress (Public Law 88-408, August 10, 1964) authorizing "
            "the president to use military force in Southeast Asia without a formal declaration "
            "of war. Passed 416-0 in the House and 88-2 in the Senate based on the fabricated "
            "Aug 4 Tonkin Gulf attack. Gave LBJ a blank check for Vietnam escalation. Repealed "
            "in January 1971 after the deception was exposed. Senators Wayne Morse and Ernest "
            "Gruening cast the only dissenting votes."
        ),
        "aliases": "Southeast Asia Resolution, Public Law 88-408",
        "metadata": {"type": "legislation", "year": 1964},
    },
    {
        "name": "Operation Gladio",
        "entity_type": "program",
        "description": (
            "NATO clandestine 'stay-behind' network established across Western Europe during "
            "the Cold War. Officially intended as resistance forces in case of Soviet invasion, "
            "the networks in Italy, Belgium, Turkey, Greece, and elsewhere were used to carry "
            "out terrorist attacks against civilians — the 'Strategy of Tension' — which were "
            "blamed on left-wing groups to discredit communism and justify authoritarian "
            "responses. Confirmed by Italian PM Giulio Andreotti (Oct 1990). European Parliament "
            "condemned the networks (Nov 1990). Italian parliamentary investigation linked "
            "Gladio to bombings including Bologna train station (1980, 85 killed) and Piazza "
            "Fontana (1969, 17 killed). Networks existed in at least 16 NATO countries."
        ),
        "aliases": "Gladio, Stay-Behind Armies",
        "metadata": {"type": "covert paramilitary network", "years_active": "1956-1990"},
    },
    {
        "name": "USS Liberty Attack",
        "entity_type": "event",
        "description": (
            "On June 8, 1967, during the Six-Day War, Israeli Air Force jets and Navy torpedo "
            "boats attacked the USS Liberty, a clearly marked US Navy signals intelligence ship "
            "in international waters off the Sinai Peninsula. The sustained assault lasted over "
            "two hours: napalm, rockets, torpedoes, and machine-gun fire on life rafts. 34 US "
            "sailors killed, 171 wounded. Israel claimed mistaken identity; surviving crew and "
            "multiple senior US military officials (including Admiral Thomas Moorer, former JCS "
            "Chairman) have stated the attack was deliberate. The Navy court of inquiry was "
            "completed in one week under orders from Admiral John McCain Sr. No Israeli was "
            "ever held accountable. NSA intercepts from the attack remain classified."
        ),
        "aliases": "Liberty Incident",
        "metadata": {"type": "military attack / coverup", "date": "1967-06-08"},
    },
    {
        "name": "Operation Ajax",
        "entity_type": "program",
        "description": (
            "Joint CIA-MI6 covert operation (August 1953) that overthrew the democratically "
            "elected Prime Minister of Iran, Mohammad Mossadegh, after he nationalized the "
            "Anglo-Iranian Oil Company (now BP). The CIA's own internal history (written by "
            "operative Donald Wilber, declassified 2013) details the operation: bribing "
            "politicians, planting propaganda in Iranian newspapers, hiring mobs, and "
            "orchestrating a military coup to install Shah Mohammad Reza Pahlavi as autocrat. "
            "Planned by Kermit Roosevelt Jr. under Allen Dulles. The Shah's 25-year dictatorship "
            "led directly to the 1979 Islamic Revolution. CIA formally acknowledged its role in "
            "2013. The template for PBSuccess and subsequent regime changes."
        ),
        "aliases": "TPAJAX, Ajax",
        "metadata": {"type": "coup / regime change", "date": "1953-08-19"},
    },
    {
        "name": "Operation PBSuccess",
        "entity_type": "program",
        "description": (
            "CIA covert operation (June 1954) that overthrew the democratically elected "
            "president of Guatemala, Jacobo Árbenz, after his agrarian reform threatened "
            "United Fruit Company landholdings. Allen Dulles authorized the operation; his "
            "brother John Foster Dulles (Secretary of State) had been a United Fruit legal "
            "counsel. CIA trained and armed a mercenary force in Honduras, broadcast fake "
            "radio reports of a massive invasion, and bombed Guatemala City. Árbenz resigned "
            "under duress. The military dictatorship that followed killed an estimated 200,000 "
            "Guatemalans over the next four decades, per the UN Truth Commission (1999), which "
            "attributed 93% of human rights violations to state forces and CIA-backed paramilitaries."
        ),
        "aliases": "PBSUCCESS",
        "metadata": {"type": "coup / regime change", "date": "1954-06-18"},
    },
    {
        "name": "Operation Paperclip",
        "entity_type": "program",
        "description": (
            "US military/intelligence program (1945-1959) that recruited over 1,600 German "
            "scientists, engineers, and technicians — many of them Nazi Party members, SS "
            "officers, and war criminals — and brought them to the United States. President "
            "Truman's original directive explicitly barred 'ardent Nazis,' but the Joint "
            "Intelligence Objectives Agency (JIOA) systematically 'bleached' dossiers by "
            "removing or rewriting Nazi affiliations. Notable recruits included Wernher von Braun "
            "(V-2 rocket designer, later NASA), Hubertus Strughold (aerospace medicine, used "
            "Dachau data), and Kurt Blome (biological weapons, human experiments). The program "
            "prioritized Cold War utility over accountability for war crimes."
        ),
        "aliases": "Paperclip, Project Paperclip",
        "metadata": {"type": "recruitment program", "years_active": "1945-1959"},
    },
    # --- People ---
    {
        "name": "Lyman Lemnitzer",
        "entity_type": "person",
        "description": (
            "Chairman of the Joint Chiefs of Staff (1960-1962). Signed the Operation Northwoods "
            "memorandum proposing false flag attacks on US citizens to justify invading Cuba. "
            "After Kennedy rejected Northwoods and removed him as JCS Chairman, Lemnitzer was "
            "reassigned as NATO Supreme Allied Commander Europe (1963-1969) — where he oversaw "
            "the very NATO stay-behind networks later exposed as Operation Gladio. His career "
            "arc connects the two largest documented false flag programs in US/NATO history."
        ),
        "aliases": "",
        "metadata": {"role": "JCS Chairman / NATO SACEUR", "years_active": "1960-1969"},
    },
    {
        "name": "Mohammad Mossadegh",
        "entity_type": "person",
        "description": (
            "Democratically elected Prime Minister of Iran (1951-1953). Nationalized the "
            "Anglo-Iranian Oil Company (now BP), which had been extracting Iranian oil under "
            "terms widely seen as exploitative. Named TIME's Man of the Year in 1951. "
            "Overthrown by CIA-MI6 Operation Ajax in August 1953. Spent the rest of his life "
            "under house arrest until his death in 1967. His overthrow is the foundational "
            "grievance of US-Iranian relations and a documented case of democracy destroyed "
            "for corporate interests."
        ),
        "aliases": "Mosaddegh, Mosaddeq, Mossadeq",
        "metadata": {"role": "Prime Minister of Iran", "years_active": "1951-1953"},
    },
    {
        "name": "Jacobo Árbenz",
        "entity_type": "person",
        "description": (
            "Democratically elected President of Guatemala (1951-1954). His agrarian reform "
            "(Decree 900) redistributed uncultivated land from large estates — including "
            "United Fruit Company holdings — to landless peasants. Overthrown by CIA Operation "
            "PBSuccess in June 1954. Forced into exile, dying in Mexico in 1971. The Dulles "
            "brothers (Allen at CIA, John Foster at State) both had financial and legal ties "
            "to United Fruit Company. Guatemala's Truth Commission documented 200,000 killed "
            "in the ensuing civil war."
        ),
        "aliases": "Jacobo Arbenz Guzmán",
        "metadata": {"role": "President of Guatemala", "years_active": "1951-1954"},
    },
    {
        "name": "Daniele Ganser",
        "entity_type": "person",
        "description": (
            "Swiss historian and academic at the University of Basel. His 2005 book 'NATO's "
            "Secret Armies: Operation Gladio and Terrorism in Western Europe' is the most "
            "comprehensive academic study of the Gladio networks, drawing on parliamentary "
            "investigations in Italy, Belgium, Switzerland, and other NATO countries. "
            "Documented the existence of clandestine stay-behind armies in at least 16 NATO "
            "nations and their connection to terrorist attacks attributed to left-wing groups."
        ),
        "aliases": "",
        "metadata": {"role": "historian", "years_active": "2005-present"},
    },
    {
        "name": "Fred Hampton",
        "entity_type": "person",
        "description": (
            "Chairman of the Illinois chapter of the Black Panther Party. Assassinated on "
            "December 4, 1969 in a pre-dawn raid by Chicago police working with the FBI. "
            "He was 21 years old. FBI informant William O'Neal provided the floor plan of "
            "Hampton's apartment and drugged him before the raid. COINTELPRO documents show "
            "the FBI targeted Hampton for his effectiveness as an organizer — particularly "
            "his Rainbow Coalition uniting Black, Puerto Rican, and poor white communities. "
            "Federal civil rights lawsuit (Hampton v. Hanrahan) established FBI/CPD conspiracy; "
            "settled for $1.85 million in 1982."
        ),
        "aliases": "Chairman Fred",
        "metadata": {"role": "Black Panther Party Chairman (Illinois)", "years_active": "1968-1969"},
    },
    # --- Organizations ---
    {
        "name": "NATO",
        "entity_type": "organization",
        "description": (
            "North Atlantic Treaty Organization, established 1949. In the Gladio context: "
            "NATO's Allied Clandestine Committee (ACC) and Clandestine Planning Committee (CPC) "
            "coordinated the stay-behind networks across member states. Italian PM Andreotti "
            "confirmed to parliament that Gladio operated under NATO coordination. European "
            "Parliament resolution (1990) condemned 'the existence for 40 years of a clandestine "
            "parallel intelligence and armed operations organization in several Member States.' "
            "Lyman Lemnitzer served as NATO Supreme Allied Commander Europe (1963-1969) after "
            "authoring Northwoods."
        ),
        "aliases": "North Atlantic Treaty Organization",
        "metadata": {"type": "military alliance", "years_active": "1949-present"},
    },
    {
        "name": "Joint Chiefs of Staff",
        "entity_type": "organization",
        "description": (
            "Body of senior uniformed leaders advising the president on military matters. "
            "In March 1962, the Joint Chiefs unanimously signed the Operation Northwoods "
            "memorandum proposing false flag attacks on US citizens and military personnel "
            "to create a pretext for invading Cuba. The proposal included sinking refugee "
            "boats, staging bombings in Miami and Washington, hijacking aircraft, and attacking "
            "Guantanamo Bay. Rejected by Secretary McNamara and President Kennedy. Chairman "
            "Lemnitzer was subsequently reassigned to NATO."
        ),
        "aliases": "JCS",
        "metadata": {"type": "military leadership body"},
    },
    {
        "name": "Strategy of Tension",
        "entity_type": "program",
        "description": (
            "Political doctrine used primarily in Italy and other NATO countries during the "
            "Cold War: carry out terrorist attacks against civilians, blame them on left-wing "
            "groups, use the resulting fear and chaos to justify authoritarian crackdowns and "
            "prevent communist electoral gains. Documented in Italian parliamentary investigations. "
            "Connected to Operation Gladio stay-behind networks. Key attacks include Piazza "
            "Fontana bombing (Milan, 1969, 17 killed), Peteano car bomb (1972), Italicus Express "
            "bombing (1974), and Bologna train station massacre (1980, 85 killed). Italian "
            "neo-fascist Vincenzo Vinciguerra testified that Gladio agents carried out the "
            "attacks."
        ),
        "aliases": "Strategia della tensione",
        "metadata": {"type": "political doctrine", "years_active": "1960s-1980s"},
    },
    {
        "name": "United Fruit Company",
        "entity_type": "organization",
        "description": (
            "American corporation whose vast landholdings in Guatemala were threatened by "
            "President Árbenz's agrarian reform. Allen Dulles (CIA Director) was a former "
            "president of the United Fruit Company board-connected Sullivan & Cromwell law "
            "firm. John Foster Dulles (Secretary of State) had been a United Fruit legal "
            "counsel. The company's PR campaign framed Árbenz as a communist threat, providing "
            "cover for the CIA coup. A textbook case of corporate interests driving regime change."
        ),
        "aliases": "UFCO, Chiquita Brands (successor)",
        "metadata": {"type": "corporation", "years_active": "1899-1970"},
    },
    {
        "name": "Wernher von Braun",
        "entity_type": "person",
        "description": (
            "German-American rocket engineer. Designed the V-2 rocket for Nazi Germany using "
            "forced labor from concentration camps (estimated 20,000 slave laborers died at "
            "Mittelwerk factory). SS Sturmbannführer (Major). Brought to US under Operation "
            "Paperclip with his Nazi record 'bleached.' Became director of NASA's Marshall "
            "Space Flight Center and chief architect of the Saturn V rocket that took Americans "
            "to the Moon. The most prominent example of Paperclip's moral calculus: Cold War "
            "utility outweighed accountability for war crimes."
        ),
        "aliases": "",
        "metadata": {"role": "rocket engineer / NASA director", "years_active": "1945-1977"},
    },
    {
        "name": "Admiral Thomas Moorer",
        "entity_type": "person",
        "description": (
            "Chairman of the Joint Chiefs of Staff (1970-1974). In retirement, chaired the "
            "independent USS Liberty commission of inquiry (2003), which found that Israel's "
            "attack on the USS Liberty was 'a deliberate attempt to destroy an American ship "
            "and kill her entire crew' and that the US government 'ordered the crew to remain "
            "silent and covered up the truth.' His status as former JCS Chairman gave the "
            "finding unique authority."
        ),
        "aliases": "",
        "metadata": {"role": "JCS Chairman", "years_active": "1970-1974"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # === OPERATION NORTHWOODS ===
    {
        "source": "Lyman Lemnitzer",
        "target": "Operation Northwoods",
        "type": "authored",
        "tier": "documented",
        "desc": "As JCS Chairman, signed the Northwoods memorandum proposing false flag attacks on US citizens to justify Cuba invasion. Declassified document bears his signature.",
        "sources": [871, 872],
        "year_start": 1962,
        "year_end": 1962,
    },
    {
        "source": "Joint Chiefs of Staff",
        "target": "Operation Northwoods",
        "type": "proposed",
        "tier": "documented",
        "desc": "All Joint Chiefs unanimously signed the Northwoods proposal. Included plans to sink refugee boats, bomb Miami, attack Guantanamo, and hijack aircraft.",
        "sources": [871, 872],
        "year_start": 1962,
        "year_end": 1962,
    },
    {
        "source": "Operation Northwoods",
        "target": "JFK Assassination",
        "type": "related_to",
        "tier": "inference",
        "desc": "Kennedy rejected Northwoods and removed Lemnitzer as JCS Chairman. The proposal demonstrated the willingness of military leadership to stage attacks — 20 months before Kennedy was assassinated in a conspiracy (per HSCA findings).",
        "sources": [871, 872],
        "year_start": 1962,
        "year_end": 1963,
    },
    {
        "source": "Lyman Lemnitzer",
        "target": "NATO",
        "type": "commanded",
        "tier": "documented",
        "desc": "After Kennedy rejected Northwoods and removed him as JCS Chairman, Lemnitzer became NATO Supreme Allied Commander Europe (1963-1969) — overseeing the same NATO structure that coordinated Gladio stay-behind networks.",
        "sources": [871, 876],
        "year_start": 1963,
        "year_end": 1969,
    },

    # === GULF OF TONKIN ===
    {
        "source": "Gulf of Tonkin Incident",
        "target": "Gulf of Tonkin Resolution",
        "type": "triggered",
        "tier": "documented",
        "desc": "The fabricated Aug 4 attack was used to pass the resolution authorizing Vietnam War escalation. NSA internal study confirmed intelligence was deliberately falsified.",
        "sources": [873, 874, 875],
        "year_start": 1964,
        "year_end": 1964,
    },
    {
        "source": "NSA",
        "target": "Gulf of Tonkin Incident",
        "type": "connected_to",
        "tier": "documented",
        "desc": "NSA historian Robert Hanyok found that NSA officers deliberately falsified SIGINT reports to support the claim of a second attack on Aug 4, 1964. NSA suppressed Hanyok's report for four years before declassification.",
        "sources": [873],
        "year_start": 1964,
        "year_end": 1964,
    },

    # === OPERATION GLADIO ===
    {
        "source": "NATO",
        "target": "Operation Gladio",
        "type": "coordinated",
        "tier": "documented",
        "desc": "NATO's Allied Clandestine Committee and Clandestine Planning Committee coordinated Gladio stay-behind networks across at least 16 member states. Confirmed by Italian PM Andreotti and condemned by European Parliament.",
        "sources": [876, 877, 879],
        "year_start": 1956,
        "year_end": 1990,
    },
    {
        "source": "CIA",
        "target": "Operation Gladio",
        "type": "operated",
        "tier": "documented",
        "desc": "CIA provided funding, training, arms caches, and operational coordination for Gladio stay-behind networks across Western Europe. Confirmed in multiple parliamentary investigations.",
        "sources": [876, 877, 879],
        "year_start": 1956,
        "year_end": 1990,
    },
    {
        "source": "Operation Gladio",
        "target": "Strategy of Tension",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Italian parliamentary investigation linked Gladio operatives to Strategy of Tension bombings including Piazza Fontana (1969) and Bologna station (1980). Neo-fascist Vincenzo Vinciguerra testified Gladio agents carried out attacks.",
        "sources": [876, 878],
        "year_start": 1969,
        "year_end": 1980,
    },
    {
        "source": "Daniele Ganser",
        "target": "Operation Gladio",
        "type": "investigated",
        "tier": "documented",
        "desc": "Published the most comprehensive academic study of Gladio networks — 'NATO's Secret Armies' (2005) — documenting stay-behind armies in 16 NATO countries using parliamentary records and declassified documents.",
        "sources": [876],
        "year_start": 2005,
        "year_end": 2005,
    },
    {
        "source": "Lyman Lemnitzer",
        "target": "Operation Gladio",
        "type": "connected_to",
        "tier": "inference",
        "desc": "As NATO Supreme Allied Commander Europe (1963-1969), Lemnitzer oversaw the NATO command structure that coordinated Gladio stay-behind networks. The Northwoods author moved to the organization running Europe's false flag infrastructure.",
        "sources": [871, 876],
        "year_start": 1963,
        "year_end": 1969,
    },

    # === USS LIBERTY ===
    {
        "source": "Mossad",
        "target": "USS Liberty Attack",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Israeli intelligence was aware the Liberty was a US signals intelligence ship. The attack occurred during the Six-Day War while the Liberty monitored Israeli military communications. Multiple investigations concluded the attack was deliberate.",
        "sources": [880, 881, 882],
        "year_start": 1967,
        "year_end": 1967,
    },
    {
        "source": "Admiral Thomas Moorer",
        "target": "USS Liberty Attack",
        "type": "investigated",
        "tier": "documented",
        "desc": "As former JCS Chairman, led independent commission that found Israel's attack was 'a deliberate attempt to destroy an American ship and kill her entire crew' and that the US government covered up the truth.",
        "sources": [882],
        "year_start": 2003,
        "year_end": 2003,
    },

    # === OPERATION AJAX ===
    {
        "source": "CIA",
        "target": "Operation Ajax",
        "type": "executed",
        "tier": "documented",
        "desc": "CIA planned and executed the 1953 coup against Mossadegh, as detailed in the agency's own declassified internal history (Wilber document). CIA formally acknowledged its role in 2013.",
        "sources": [883, 884, 885],
        "year_start": 1953,
        "year_end": 1953,
    },
    {
        "source": "Allen Dulles",
        "target": "Operation Ajax",
        "type": "authorized",
        "tier": "documented",
        "desc": "As CIA Director, authorized Operation Ajax to overthrow Mossadegh. Dulles brothers' firm Sullivan & Cromwell had represented Anglo-Iranian Oil Company interests — the very company Mossadegh nationalized.",
        "sources": [883, 896],
        "year_start": 1953,
        "year_end": 1953,
    },
    {
        "source": "Operation Ajax",
        "target": "Mohammad Mossadegh",
        "type": "overthrew",
        "tier": "documented",
        "desc": "CIA-MI6 coup overthrew democratically elected PM Mossadegh after he nationalized Anglo-Iranian Oil Company. Replaced with Shah's autocracy, leading directly to 1979 Islamic Revolution.",
        "sources": [883, 884, 885],
        "year_start": 1953,
        "year_end": 1953,
    },

    # === OPERATION PBSUCCESS ===
    {
        "source": "CIA",
        "target": "Operation PBSuccess",
        "type": "executed",
        "tier": "documented",
        "desc": "CIA trained mercenary force, conducted bombing campaign, and broadcast fake radio reports to overthrow Árbenz. Declassified CIA records detail the full operation.",
        "sources": [886, 887, 888],
        "year_start": 1954,
        "year_end": 1954,
    },
    {
        "source": "Allen Dulles",
        "target": "Operation PBSuccess",
        "type": "authorized",
        "tier": "documented",
        "desc": "As CIA Director, authorized the Guatemala coup. His brother John Foster Dulles (Secretary of State) had been United Fruit Company legal counsel — the company whose landholdings Árbenz's reform threatened.",
        "sources": [886, 887, 896],
        "year_start": 1954,
        "year_end": 1954,
    },
    {
        "source": "Operation PBSuccess",
        "target": "Jacobo Árbenz",
        "type": "overthrew",
        "tier": "documented",
        "desc": "CIA coup forced Árbenz to resign and go into exile. Guatemala's Truth Commission documented 200,000 killed in ensuing civil war, attributing 93% of violations to state forces and CIA-backed paramilitaries.",
        "sources": [886, 887, 888],
        "year_start": 1954,
        "year_end": 1954,
    },
    {
        "source": "United Fruit Company",
        "target": "Operation PBSuccess",
        "type": "connected_to",
        "tier": "documented",
        "desc": "United Fruit's lobbying and PR campaign framed Árbenz as communist, providing political cover for the CIA coup. Dulles brothers had financial and legal ties to the company.",
        "sources": [887, 896, 897],
        "year_start": 1952,
        "year_end": 1954,
    },

    # === OPERATION PAPERCLIP ===
    {
        "source": "CIA",
        "target": "Operation Paperclip",
        "type": "participated_in",
        "tier": "documented",
        "desc": "CIA recruited Paperclip scientists for intelligence purposes, including biological weapons experts and mind control researchers. Some Paperclip recruits were later involved in MKULTRA.",
        "sources": [889, 890, 891],
        "year_start": 1945,
        "year_end": 1959,
    },
    {
        "source": "Wernher von Braun",
        "target": "Operation Paperclip",
        "type": "recruited_by",
        "tier": "documented",
        "desc": "V-2 rocket designer and SS Major, brought to US under Paperclip with Nazi record bleached. Became NASA director, designed Saturn V. Most prominent Paperclip recruit.",
        "sources": [889, 890, 900],
        "year_start": 1945,
        "year_end": 1945,
    },

    # === COINTELPRO / HAMPTON (references existing COINTELPRO entity) ===
    {
        "source": "FBI",
        "target": "Fred Hampton",
        "type": "assassinated",
        "tier": "documented",
        "desc": "FBI COINTELPRO operation coordinated with Chicago police to assassinate Hampton in pre-dawn raid (Dec 4, 1969). FBI informant drugged Hampton and provided his apartment floor plan. Federal court established FBI/CPD conspiracy.",
        "sources": [892, 893, 894, 895],
        "year_start": 1969,
        "year_end": 1969,
    },
    {
        "source": "COINTELPRO",
        "target": "Fred Hampton",
        "type": "targeted",
        "tier": "documented",
        "desc": "COINTELPRO documents show FBI targeted Hampton for his effectiveness as an organizer — particularly his Rainbow Coalition uniting Black, Puerto Rican, and poor white communities.",
        "sources": [892, 893, 894],
        "year_start": 1968,
        "year_end": 1969,
    },
    {
        "source": "Church Committee",
        "target": "COINTELPRO",
        "type": "investigated",
        "tier": "documented",
        "desc": "Church Committee investigation (1975-76) exposed COINTELPRO's full scope: 2,370 approved disruptive actions targeting civil rights leaders, anti-war activists, and domestic political organizations.",
        "sources": [892, 899],
        "year_start": 1975,
        "year_end": 1976,
    },

    # === OPERATION CONDOR → KISSINGER (existing entities) ===
    {
        "source": "Henry Kissinger",
        "target": "Operation Ajax",
        "type": "related_to",
        "tier": "inference",
        "desc": "Kissinger's later support for Condor and Chilean coup followed the Ajax template — CIA regime change dressed in Cold War anti-communist framing. The playbook was established by Dulles and inherited by Kissinger's generation.",
        "sources": [897, 898],
        "year_start": 1969,
        "year_end": 1977,
    },

    # === CROSS-CUTTING CONNECTIONS ===
    {
        "source": "Allen Dulles",
        "target": "Operation Paperclip",
        "type": "connected_to",
        "tier": "credible",
        "desc": "As CIA Director, Dulles inherited and expanded intelligence relationships with Paperclip scientists. Some recruited for MKULTRA and other CIA programs during his tenure.",
        "sources": [889, 896],
        "year_start": 1953,
        "year_end": 1961,
    },
    {
        "source": "Operation Ajax",
        "target": "Operation PBSuccess",
        "type": "related_to",
        "tier": "documented",
        "desc": "Ajax (Iran 1953) served as the operational template for PBSuccess (Guatemala 1954). Same CIA Director (Dulles), same playbook (propaganda + local assets + military coup), executed one year apart.",
        "sources": [896, 897],
        "year_start": 1953,
        "year_end": 1954,
    },
    {
        "source": "Operation Northwoods",
        "target": "Gulf of Tonkin Incident",
        "type": "related_to",
        "tier": "inference",
        "desc": "Northwoods (1962) proposed fabricating attacks to justify military action. Two years later, the Gulf of Tonkin incident used a fabricated naval engagement for the same purpose — to authorize military escalation. The pattern Northwoods codified was executed at Tonkin.",
        "sources": [871, 873],
        "year_start": 1962,
        "year_end": 1964,
    },
    {
        "source": "Operation Mockingbird",
        "target": "Operation Ajax",
        "type": "supported",
        "tier": "credible",
        "desc": "CIA media assets planted anti-Mossadegh propaganda in US and Iranian press as part of Ajax. Mockingbird's media infiltration infrastructure provided the channels for manufacturing public consent for the coup.",
        "sources": [883, 884, 896],
        "year_start": 1953,
        "year_end": 1953,
    },
    {
        "source": "Operation Mockingbird",
        "target": "Operation PBSuccess",
        "type": "supported",
        "tier": "credible",
        "desc": "CIA media assets framed Árbenz as a communist threat to justify the Guatemala coup. United Fruit Company's PR campaign worked through the same channels Mockingbird had established.",
        "sources": [886, 887, 896],
        "year_start": 1954,
        "year_end": 1954,
    },
]

# ============================================================
# ENTITY_SOURCES — links entities to their key sources
# ============================================================

ENTITY_SOURCES = {
    "Operation Northwoods": [871, 872],
    "Gulf of Tonkin Incident": [873, 874, 875],
    "Gulf of Tonkin Resolution": [874, 875],
    "Operation Gladio": [876, 877, 878, 879],
    "USS Liberty Attack": [880, 881, 882],
    "Operation Ajax": [883, 884, 885],
    "Operation PBSuccess": [886, 887, 888],
    "Operation Paperclip": [889, 890, 891, 900],
    "Lyman Lemnitzer": [871, 872, 876],
    "Mohammad Mossadegh": [883, 884, 885],
    "Jacobo Árbenz": [886, 887, 888],
    "Daniele Ganser": [876],
    "Fred Hampton": [892, 893, 894, 895],
    "NATO": [876, 877, 879],
    "Joint Chiefs of Staff": [871, 872],
    "Strategy of Tension": [876, 878],
    "United Fruit Company": [886, 887, 896],
    "Wernher von Braun": [889, 890, 900],
    "Admiral Thomas Moorer": [882],
}
