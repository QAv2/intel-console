"""
Resource Control — August 2026 uplift expansion for Intel Console.

Covers energy suppression, oil geopolitics, cartel designations, the MIC,
geoengineering, water privatization, and related 2025-2026 developments.
Wires dozens of zero-connection entities that were previously orphaned in
the resource branch.

NEW ENTITIES: Sinaloa Cartel, PDVSA, ENI, Royal Dutch Shell, Kerr-McGee
Corporation, Anduril Industries, Boeing F-47, Chris Wright, Energy Transfer
v. Greenpeace (2025), Cartel FTO Designations (2025), Primo Brands Corporation.

EXISTING ENTITIES referenced (exact DB names, NOT duplicated):
  Nikola Tesla, Thomas Townsend Brown, Bernard J. Eastlund, HAARP, SCoPEx,
  David Keith, Frank Keutsch, Ken Caldeira, Alan Robock, Luke Iseman,
  Make Sunsets, Hughes Aircraft, NOAA, Stardust Solutions, Karen Silkwood,
  Enrico Mattei, Ida Tarbell, Henri Deterding, Hugo Chávez, Muammar Gaddafi,
  Nicolas Sarkozy, John Perkins, Standard Oil, DOE, Lockheed Martin, Raytheon,
  Northrop Grumman, Boeing Defense, General Dynamics, Halliburton, Bechtel
  Corporation, Steven Bechtel Sr, Erik Prince, Blackwater, Palantir Technologies,
  Peter Thiel, Alex Karp, In-Q-Tel, DARPA, Booz Allen Hamilton, Glencore,
  Nestlé Waters, Veolia, Suez Group, Thames Water, Flint Water Crisis,
  Standing Rock Protests, Cochabamba Water War, Ogallala Aquifer,
  Medellín Cartel, Los Zetas, Freeway Rick Ross, Oscar Danilo Blandon,
  Donald Trump, Dick Cheney, CIA, DEA, NSA, FBI, World Bank,
  Nicolás Maduro, DOGE, Elon Musk

Evidence tiers:
  documented = court filings, congressional record, FOIA, official government docs
  credible   = quality investigative journalism, on-record testimony, academic work
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence (almost never used)
"""

# ============================================================
# SOURCES — IDs 2400–2499
# ============================================================

SOURCES = [
    # ---- Government / Legal / Congressional ----
    {
        "id": 2400,
        "title": "Executive Order: Designating Cartels and Other Organizations as Foreign Terrorist Organizations and Specially Designated Global Terrorists",
        "url": "https://www.federalregister.gov/d/2025-03295",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 2401,
        "title": "Silkwood v. Kerr-McGee Corp., 464 U.S. 238 (1984) — Supreme Court Opinion",
        "url": "https://supreme.justia.com/cases/federal/us/464/238/",
        "source_type": "court",
        "year": 1984,
    },
    {
        "id": 2402,
        "title": "US Patent US4686605A — Method and apparatus for altering a region in the earth's atmosphere, ionosphere, and/or magnetosphere (Eastlund)",
        "url": "https://patents.google.com/patent/US4686605A",
        "source_type": "government",
        "year": 1987,
    },
    {
        "id": 2403,
        "title": "Tennessee SB 2691 — Prohibition on geoengineering activities (signed into law April 2024)",
        "url": "https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=SB2691",
        "source_type": "government",
        "year": 2024,
    },
    {
        "id": 2404,
        "title": "National Security Archive — CIA Documents on Venezuela, April 2002 Coup (declassified 2004)",
        "url": "https://nsarchive.gwu.edu/briefing-book/venezuela/2004-11-24/cias-venezuela-eyewitness-account",
        "source_type": "archive",
        "year": 2004,
    },
    {
        "id": 2405,
        "title": "National Endowment for Democracy — Annual Report 2001 (Venezuela grants)",
        "url": "https://www.ned.org/publications/annual-reports/2001-annual-report/",
        "source_type": "government",
        "year": 2001,
    },
    {
        "id": 2406,
        "title": "SEC Filing — Primo Water Corporation and BlueTriton Brands Merger Completion (PRMB)",
        "url": "https://www.sec.gov/cgi-bin/browse-edgar?company=primo+brands&CIK=&type=8-K&dateb=&owner=include&count=10&search_text=&action=getcompany",
        "source_type": "government",
        "year": 2024,
    },
    # ---- Journalism ----
    {
        "id": 2407,
        "title": "Sinaloa cartel co-founder 'El Mayo' Zambada pleads guilty, faces life — Reuters",
        "url": "https://www.reuters.com/world/americas/sinaloa-cartel-leader-el-mayo-zambada-pleads-guilty-us-court-2025-08-25/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2408,
        "title": "Ovidio Guzmán López pleads guilty to drug charges in Chicago — Reuters",
        "url": "https://www.reuters.com/world/americas/ovidio-guzman-lopez-pleads-guilty-drug-charges-chicago-2025-07-11/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2409,
        "title": "Trump revokes Chevron's Venezuela operating license — Reuters",
        "url": "https://www.reuters.com/business/energy/trump-revokes-chevrons-venezuela-operating-license-2025-02-26/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2410,
        "title": "Chevron resumes Venezuelan oil exports after receiving new Treasury license — Reuters",
        "url": "https://www.reuters.com/business/energy/chevron-resumes-venezuelan-oil-exports-new-treasury-license-2025-08-15/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2411,
        "title": "Harvard will shut down its solar geoengineering research program — MIT Technology Review",
        "url": "https://www.technologyreview.com/2024/03/18/1089813/harvard-will-shut-down-its-solar-geoengineering-research-program/",
        "source_type": "journalism",
        "author": "James Temple",
        "year": 2024,
    },
    {
        "id": 2412,
        "title": "Jury awards Energy Transfer $667M in lawsuit against Greenpeace over DAPL protests — Reuters",
        "url": "https://www.reuters.com/legal/jury-awards-energy-transfer-667-mln-lawsuit-against-greenpeace-2025-02/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2413,
        "title": "Trump designates Mexican cartels as foreign terrorist organizations — AP News",
        "url": "https://apnews.com/article/trump-cartels-foreign-terrorist-organizations-sinaloa-cjng",
        "source_type": "journalism",
        "author": "AP News",
        "year": 2025,
    },
    {
        "id": 2414,
        "title": "Boeing wins $20 billion-plus contract for F-47 sixth-gen fighter — Defense News",
        "url": "https://www.defensenews.com/air/2025/03/21/boeing-wins-ngad-fighter-contract/",
        "source_type": "journalism",
        "author": "Defense News",
        "year": 2025,
    },
    {
        "id": 2415,
        "title": "Palantir wins Army enterprise software deal worth up to $10 billion — Reuters",
        "url": "https://www.reuters.com/technology/palantir-wins-army-enterprise-software-deal-worth-up-10-billion-2025-07/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2416,
        "title": "Sarkozy convicted in Gaddafi campaign finance case, sentenced to five years — Reuters",
        "url": "https://www.reuters.com/world/europe/sarkozy-convicted-gaddafi-campaign-finance-case-2025-09/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2417,
        "title": "Anduril takes over Army IVAS program from Microsoft — Defense News",
        "url": "https://www.defensenews.com/land/2025/02/anduril-takes-over-army-ivas-program/",
        "source_type": "journalism",
        "author": "Defense News",
        "year": 2025,
    },
    {
        "id": 2418,
        "title": "NOAA faces mass layoffs as DOGE targets agency — Washington Post",
        "url": "https://www.washingtonpost.com/weather/2025/02/noaa-layoffs-doge-trump/",
        "source_type": "journalism",
        "author": "Washington Post",
        "year": 2025,
    },
    {
        "id": 2419,
        "title": "KKR pulls out of Thames Water deal, raising nationalization prospect — Financial Times",
        "url": "https://www.ft.com/content/thames-water-kkr-deal-collapse-2025",
        "source_type": "journalism",
        "author": "Financial Times",
        "year": 2025,
    },
    {
        "id": 2420,
        "title": "Flint water crisis settlement: Payments reach majority of claimants — AP News",
        "url": "https://apnews.com/article/flint-water-crisis-settlement-payments",
        "source_type": "journalism",
        "author": "AP News",
        "year": 2024,
    },
    {
        "id": 2421,
        "title": "Trump signs executive order declaring national energy emergency — Reuters",
        "url": "https://www.reuters.com/business/energy/trump-declares-national-energy-emergency-2025-01-20/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2422,
        "title": "Trump reverses Biden LNG export pause, approves pending projects — Reuters",
        "url": "https://www.reuters.com/business/energy/trump-reverses-biden-lng-export-pause-2025-01/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2423,
        "title": "FY2026 defense budget request tops $1 trillion — Defense One",
        "url": "https://www.defenseone.com/policy/2025/05/fy2026-defense-budget-request/",
        "source_type": "journalism",
        "author": "Defense One",
        "year": 2025,
    },
    {
        "id": 2424,
        "title": "Anduril raises $5 billion at $61 billion valuation — Bloomberg",
        "url": "https://www.bloomberg.com/news/articles/2026-05-anduril-raises-5-billion",
        "source_type": "journalism",
        "author": "Bloomberg",
        "year": 2026,
    },
    {
        "id": 2425,
        "title": "Zambada sentenced to life in prison for leading Sinaloa Cartel — Reuters",
        "url": "https://www.reuters.com/world/americas/zambada-sentenced-life-sinaloa-cartel-2026-07-20/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2026,
    },
    {
        "id": 2426,
        "title": "Palantir wins £240M UK Ministry of Defence contract — Reuters",
        "url": "https://www.reuters.com/technology/palantir-wins-uk-mod-contract-2025-12/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    # ---- Books ----
    {
        "id": 2427,
        "title": "Daniel Yergin, 'The Prize: The Epic Quest for Oil, Money & Power' (Simon & Schuster, 1991)",
        "url": "https://www.simonandschuster.com/books/The-Prize/Daniel-Yergin/9781439110126",
        "source_type": "book",
        "author": "Daniel Yergin",
        "year": 1991,
    },
    {
        "id": 2428,
        "title": "Eva Golinger, 'The Chávez Code: Cracking US Intervention in Venezuela' (Olive Branch Press, 2006)",
        "url": "https://www.goodreads.com/book/show/544851.The_Ch_vez_Code",
        "source_type": "book",
        "author": "Eva Golinger",
        "year": 2006,
    },
    {
        "id": 2429,
        "title": "John Perkins, 'Confessions of an Economic Hit Man' (Berrett-Koehler, 2004)",
        "url": "https://www.bkconnection.com/books/title/confessions-of-an-economic-hit-man-3rd-edition",
        "source_type": "book",
        "author": "John Perkins",
        "year": 2004,
    },
    {
        "id": 2430,
        "title": "Ida Tarbell, 'The History of the Standard Oil Company' (McClure, Phillips & Co., 1904)",
        "url": "https://archive.org/details/historyofstandar00tarbuoft",
        "source_type": "book",
        "author": "Ida Tarbell",
        "year": 1904,
    },
    {
        "id": 2431,
        "title": "Richard Rashke, 'The Killing of Karen Silkwood' (Houghton Mifflin, 1981; updated 2000)",
        "url": "https://www.goodreads.com/book/show/1016879.The_Killing_of_Karen_Silkwood",
        "source_type": "book",
        "author": "Richard Rashke",
        "year": 2000,
    },
    # ---- Wikipedia / Reference ----
    {
        "id": 2432,
        "title": "Sinaloa Cartel — Wikipedia (history, leadership, FTO designation)",
        "url": "https://en.wikipedia.org/wiki/Sinaloa_Cartel",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2433,
        "title": "PDVSA — Wikipedia (history, nationalization, production data)",
        "url": "https://en.wikipedia.org/wiki/PDVSA",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2434,
        "title": "Enrico Mattei — Wikipedia (ENI, death investigation, sabotage finding)",
        "url": "https://en.wikipedia.org/wiki/Enrico_Mattei",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2435,
        "title": "Anduril Industries — Wikipedia (founding, contracts, valuation)",
        "url": "https://en.wikipedia.org/wiki/Anduril_Industries",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2436,
        "title": "Karen Silkwood — Wikipedia (Kerr-McGee case, SCOTUS ruling, settlement)",
        "url": "https://en.wikipedia.org/wiki/Karen_Silkwood",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2437,
        "title": "Nicolas Sarkozy — Wikipedia (Libyan financing case, convictions, imprisonment)",
        "url": "https://en.wikipedia.org/wiki/Nicolas_Sarkozy",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2438,
        "title": "Hugo Chávez — Wikipedia (2002 coup, PDVSA nationalization, CIA foreknowledge)",
        "url": "https://en.wikipedia.org/wiki/Hugo_Ch%C3%A1vez",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2439,
        "title": "Royal Dutch Shell — Wikipedia (Deterding era, history, controversies)",
        "url": "https://en.wikipedia.org/wiki/Shell_plc",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2440,
        "title": "Kerr-McGee — Wikipedia (history, Silkwood case, acquisitions)",
        "url": "https://en.wikipedia.org/wiki/Kerr-McGee",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2441,
        "title": "Palantir Technologies — Wikipedia (founding, contracts, government work)",
        "url": "https://en.wikipedia.org/wiki/Palantir_Technologies",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2442,
        "title": "HAARP — Wikipedia (Eastlund patents, APTI, University of Alaska)",
        "url": "https://en.wikipedia.org/wiki/High-frequency_Active_Auroral_Research_Program",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2443,
        "title": "Thames Water — Wikipedia (financial crisis, KKR, restructuring 2025-2026)",
        "url": "https://en.wikipedia.org/wiki/Thames_Water",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2444,
        "title": "Veolia — Wikipedia (Suez acquisition, global water operations)",
        "url": "https://en.wikipedia.org/wiki/Veolia",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2445,
        "title": "Blackwater (company) — Wikipedia (founding, CIA contracts, Nisour Square)",
        "url": "https://en.wikipedia.org/wiki/Blackwater_(company)",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2446,
        "title": "Erik Prince — Wikipedia (Blackwater founder, FSG, CIA connections)",
        "url": "https://en.wikipedia.org/wiki/Erik_Prince",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2447,
        "title": "Bechtel — Wikipedia (Cochabamba, Iraq reconstruction, revolving door)",
        "url": "https://en.wikipedia.org/wiki/Bechtel",
        "source_type": "other",
        "year": 2026,
    },
]

# ============================================================
# ENTITIES — 11 new
# ============================================================

ENTITIES = [
    {
        "name": "Sinaloa Cartel",
        "entity_type": "organization",
        "description": (
            "Mexican drug trafficking organization based in Culiacn, Sinaloa. "
            "Founded in the late 1980s as the Guadalajara Cartel fragmented. Led by "
            "Joaquin 'El Chapo' Guzman (captured 2016, convicted 2019, life sentence) "
            "and Ismael 'El Mayo' Zambada (captured July 25, 2024; pleaded guilty "
            "August 25, 2025 to racketeering conspiracy and running a continuing "
            "criminal enterprise; sentenced to life July 20, 2026). Ovidio Guzman "
            "Lopez, El Chapo's son, pleaded guilty July 11, 2025 to drug distribution "
            "charges and is reportedly cooperating with US authorities. On February 20, "
            "2025, President Trump designated the Sinaloa Cartel as a Foreign Terrorist "
            "Organization via executive order, alongside CJNG. The cartel is the primary "
            "Mexican fentanyl trafficking organization and has been a target of "
            "escalating US enforcement actions."
        ),
        "aliases": "CDS, Sinaloa Federation, Cartel de Sinaloa",
        "metadata": {
            "nationality": "Mexican",
            "role": "Drug trafficking organization",
            "status": "active",
        },
    },
    {
        "name": "PDVSA",
        "entity_type": "organization",
        "description": (
            "Petroleos de Venezuela, S.A., Venezuela's state-owned petroleum company "
            "controlling the world's largest proven oil reserves. Founded in 1976 during "
            "Carlos Andres Perez's first nationalization. Hugo Chavez reasserted state "
            "control in 2007, firing 18,000 workers after a 2002-2003 management strike. "
            "Under Nicolas Maduro (2013-), PDVSA production collapsed from approximately "
            "3 million barrels per day to under 900,000 bpd due to corruption, "
            "mismanagement, and US sanctions. Chevron operated under OFAC License 41 "
            "(granted November 2022) until Trump revoked it February 26, 2025. A new "
            "Treasury license was issued August 2025, allowing Chevron to resume "
            "Venezuelan crude exports. Citgo Petroleum, PDVSA's US refining subsidiary, "
            "faces court-ordered auction proceedings from international creditors."
        ),
        "aliases": "Petroleos de Venezuela, Petróleos de Venezuela",
        "metadata": {
            "nationality": "Venezuelan",
            "type": "state oil company",
            "founded": 1976,
        },
    },
    {
        "name": "ENI",
        "entity_type": "organization",
        "description": (
            "Ente Nazionale Idrocarburi, Italy's state-controlled multinational oil and "
            "gas company. Founded in 1953 by Enrico Mattei, who as chairman challenged "
            "the dominance of the 'Seven Sisters' oil cartel by negotiating directly "
            "with oil-producing nations, offering 75-25 profit splits versus the "
            "industry standard 50-50. Mattei struck deals with the Soviet Union, "
            "Algeria, Iran, and Egypt, undermining the Anglo-American oil order. His "
            "October 27, 1962 death in a plane crash near Bascape was initially ruled "
            "accidental, but a 1990s Italian judicial investigation found explosive "
            "residue in exhumed remains and reclassified the case as homicide with "
            "unknown perpetrators. ENI remains one of the world's largest integrated "
            "energy companies, operating in 62 countries."
        ),
        "aliases": "Ente Nazionale Idrocarburi, ENI SpA",
        "metadata": {
            "nationality": "Italian",
            "type": "state oil company",
            "founded": 1953,
            "location": "Rome, Italy",
        },
    },
    {
        "name": "Royal Dutch Shell",
        "entity_type": "organization",
        "description": (
            "Anglo-Dutch multinational oil and gas company, one of the original 'Seven "
            "Sisters' that dominated the global petroleum industry. Formed from the 1907 "
            "merger of Royal Dutch Petroleum and Shell Transport and Trading Company. "
            "Under Henri Deterding's leadership (1900-1936), the company became Standard "
            "Oil's chief global rival. Deterding became a Nazi sympathizer in the 1930s, "
            "reportedly donating to the NSDAP; his 1939 funeral was attended by Nazi "
            "officials and Hitler sent a wreath. Shell has been involved in numerous "
            "environmental and human rights controversies, including its role in "
            "Nigeria's Ogoniland. Rebranded as Shell plc in 2022, headquartered in "
            "London."
        ),
        "aliases": "Shell, Shell plc, Royal Dutch Petroleum",
        "metadata": {
            "type": "multinational oil company",
            "founded": 1907,
            "location": "London, UK",
        },
    },
    {
        "name": "Kerr-McGee Corporation",
        "entity_type": "organization",
        "description": (
            "American energy company founded in 1929, based in Oklahoma City. Operated "
            "uranium mining, nuclear fuel processing, and oil and gas extraction. "
            "Central to the Karen Silkwood case: Silkwood, a chemical technician at "
            "Kerr-McGee's Cimarron plutonium plant near Crescent, Oklahoma, discovered "
            "safety violations and plutonium contamination of workers. She died in a "
            "suspicious car crash on November 13, 1974. A 1979 federal jury awarded "
            "$10.5 million against the company. The Supreme Court ruled in Silkwood v. "
            "Kerr-McGee Corp. (464 U.S. 238, 1984) that federal nuclear regulation does "
            "not preempt state tort law. The case settled for $1.38 million in 1986 "
            "without admission of liability. Kerr-McGee was acquired by Anadarko "
            "Petroleum in 2006, later absorbed by Occidental Petroleum in 2019."
        ),
        "aliases": "Kerr-McGee, KMG",
        "metadata": {
            "type": "energy company (defunct)",
            "founded": 1929,
            "status": "acquired",
            "location": "Oklahoma City, OK",
        },
    },
    {
        "name": "Anduril Industries",
        "entity_type": "organization",
        "description": (
            "American defense technology company founded April 20, 2017 by Palmer "
            "Luckey (previously founder of Oculus VR), Trae Stephens, Matt Grimm, and "
            "Brian Schimpf (CEO). Backed by Peter Thiel's Founders Fund, Andreessen "
            "Horowitz, and other Silicon Valley investors. Develops autonomous weapons "
            "systems, counter-drone technology, and AI-driven military hardware. Won the "
            "US Army's IVAS (Integrated Visual Augmentation System) contract in February "
            "2025, taking over from Microsoft. Announced Arsenal-1, a $1 billion "
            "autonomous weapons manufacturing facility in Ohio (January 2025). Valued at "
            "$61 billion following a $5 billion fundraise in May 2026. Represents the "
            "new generation of defense technology companies that challenge legacy "
            "contractors by applying Silicon Valley methods to military systems."
        ),
        "aliases": "Anduril",
        "metadata": {
            "type": "defense technology",
            "founded": 2017,
            "location": "Costa Mesa, CA",
        },
    },
    {
        "name": "Boeing F-47",
        "entity_type": "program",
        "description": (
            "Sixth-generation stealth air superiority fighter under the US Air Force's "
            "Next Generation Air Dominance (NGAD) program, intended to replace the F-22 "
            "Raptor. Boeing was awarded the engineering and manufacturing development "
            "contract, valued at over $20 billion, announced March 21, 2025. President "
            "Trump revealed the selection and the F-47 designation, which references the "
            "P-47 Thunderbolt, the Air Force's 1947 founding year, and the 47th "
            "president. The award marked a significant victory for Boeing's defense "
            "division and a notable loss for Lockheed Martin, which had built both the "
            "F-22 and F-35. The F-47 is expected to incorporate advanced stealth, "
            "autonomous capabilities, and networking with collaborative combat aircraft."
        ),
        "aliases": "F-47, NGAD, Next Generation Air Dominance",
    },
    {
        "name": "Chris Wright",
        "entity_type": "person",
        "description": (
            "American energy executive, CEO of Liberty Energy (formerly Liberty Oilfield "
            "Services), confirmed as United States Secretary of Energy in early 2025. A "
            "vocal advocate for fossil fuels and critic of renewable energy transition "
            "narratives. As DOE Secretary under President Trump, Wright oversaw "
            "implementation of the national energy emergency executive order signed "
            "January 20, 2025, expansion of LNG export approvals reversing Biden's 2024 "
            "pause, and nuclear energy executive orders to streamline reactor permitting. "
            "Wright represents the fossil fuel industry's direct entry into the cabinet "
            "position that oversees the national nuclear weapons complex, national "
            "laboratories, and energy policy."
        ),
        "aliases": "Christopher Wright",
        "metadata": {
            "nationality": "American",
            "role": "US Secretary of Energy (2025-)",
            "prior_role": "CEO, Liberty Energy",
            "status": "active",
        },
    },
    {
        "name": "Energy Transfer v. Greenpeace (2025)",
        "entity_type": "event",
        "description": (
            "Civil lawsuit filed by Energy Transfer LP against Greenpeace USA and "
            "affiliates over their role in organizing opposition to the Dakota Access "
            "Pipeline at Standing Rock. In February 2025, a North Dakota jury found "
            "Greenpeace liable and awarded Energy Transfer $666.8 million in damages. "
            "The verdict, one of the largest against an environmental organization, was "
            "based on claims that Greenpeace orchestrated a misleading campaign about "
            "threats to tribal sacred sites. Environmental groups condemned the verdict "
            "as a strategic lawsuit against public participation (SLAPP) designed to "
            "chill environmental activism. Greenpeace is appealing the ruling. A prior "
            "RICO-based federal lawsuit by Energy Transfer was dismissed in 2019."
        ),
        "aliases": "Energy Transfer DAPL Lawsuit",
        "metadata": {
            "date": "2025-02",
            "location": "Morton County, North Dakota",
        },
    },
    {
        "name": "Cartel FTO Designations (2025)",
        "entity_type": "legislation",
        "description": (
            "Executive order signed by President Trump on February 20, 2025, designating "
            "the Sinaloa Cartel and Jalisco New Generation Cartel (CJNG) as Foreign "
            "Terrorist Organizations (FTOs) and Specially Designated Global Terrorists. "
            "Tren de Aragua was designated a Transnational Criminal Organization. The "
            "FTO designation, typically reserved for groups like al-Qaeda and ISIS, "
            "enables expanded legal authorities including the material support statute "
            "(18 U.S.C. 2339B), enhanced financial sanctions, and immigration bars. The "
            "designation accompanied broader Trump administration moves including 25% "
            "tariffs on Mexico citing fentanyl flows and deployment of additional "
            "military assets to the southern border."
        ),
        "aliases": "Cartel FTO Executive Order",
        "metadata": {
            "date": "2025-02-20",
        },
    },
    {
        "name": "Primo Brands Corporation",
        "entity_type": "organization",
        "description": (
            "American beverage company formed from the November 8, 2024 merger of Primo "
            "Water Corporation and BlueTriton Brands, the former Nestle Waters North "
            "America division sold by Nestle in 2021 for $4.3 billion to One Rock "
            "Capital Partners. Trades on NYSE as PRMB. Owns major US bottled water "
            "brands including Poland Spring, Deer Park, Arrowhead, Zephyrhills, Ozarka, "
            "and Ice Mountain, along with Primo's water dispenser and refill business. "
            "The merger consolidated a significant portion of the US bottled water "
            "market under one corporate umbrella, raising concentration concerns in an "
            "industry criticized for commodifying public water resources."
        ),
        "aliases": "PRMB, Primo Water, BlueTriton Brands",
        "metadata": {
            "type": "beverage/water company",
            "founded": 2024,
            "location": "Stamford, CT",
        },
    },
]

# ============================================================
# RELATIONSHIPS — 43 edges
# ============================================================

RELATIONSHIPS = [
    # ---- Energy Suppression / Geoengineering ----
    {
        "source": "Bernard J. Eastlund",
        "target": "HAARP",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Eastlund's patent US4686605A (1987) described using high-power radio "
            "frequency energy to modify the ionosphere and is the foundational "
            "technology underlying HAARP. The patent was assigned to APTI Inc. "
            "(formerly ARCO Power Technologies). APTI was acquired by E-Systems "
            "(1994), then Raytheon (1995). The patent chain runs through ARCO and "
            "Raytheon, not Hughes Aircraft."
        ),
        "sources": [2402, 2442],
    },
    {
        "source": "David Keith",
        "target": "SCoPEx",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Co-created Harvard Solar Geoengineering Research Program and the SCoPEx "
            "experiment. Keith left Harvard for the University of Chicago circa 2023. "
            "Harvard shut down the program in March 2024. Keith also co-founded Carbon "
            "Engineering, acquired by Occidental Petroleum subsidiary 1PointFive for "
            "approximately $1.1 billion in 2023."
        ),
        "year_start": 2017,
        "year_end": 2024,
        "sources": [2411],
    },
    {
        "source": "Frank Keutsch",
        "target": "SCoPEx",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Principal investigator of the SCoPEx project at Harvard. The experiment "
            "aimed to test small-scale aerosol injection in the stratosphere but faced "
            "massive opposition, particularly from Swedish indigenous groups (Saami "
            "Council). The advisory committee recommended against outdoor testing."
        ),
        "sources": [2411],
    },
    {
        "source": "Ken Caldeira",
        "target": "David Keith",
        "type": "associate_of",
        "tier": "credible",
        "desc": (
            "Leading colleagues in solar geoengineering research. Both published "
            "foundational modeling work on stratospheric aerosol injection effects. "
            "Caldeira at Carnegie Institution / Breakthrough Energy; Keith at Harvard "
            "then University of Chicago."
        ),
        "sources": [2411],
    },
    {
        "source": "Alan Robock",
        "target": "SCoPEx",
        "type": "exposed",
        "tier": "credible",
        "desc": (
            "Rutgers climate scientist and prominent critic of solar geoengineering. "
            "Published extensively on risks of stratospheric aerosol injection, "
            "including '20 reasons why geoengineering may be a bad idea.' Opposed "
            "SCoPEx outdoor testing and has argued the governance frameworks are "
            "insufficient to prevent unilateral deployment."
        ),
        "sources": [2411],
    },
    {
        "source": "Luke Iseman",
        "target": "Make Sunsets",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Founded and serves as CEO of Make Sunsets, launching unauthorized sulfur "
            "dioxide balloons into the stratosphere beginning in 2022. The launches "
            "were conducted without regulatory approval, prompting Mexico to ban the "
            "company's operations in January 2023."
        ),
        "year_start": 2022,
        "sources": [2435],
    },
    {
        "source": "Hughes Aircraft",
        "target": "Raytheon",
        "type": "acquired",
        "tier": "documented",
        "desc": (
            "Raytheon acquired Hughes Aircraft Company's defense electronics "
            "operations in 1997 for $9.5 billion. Separately, Raytheon also acquired "
            "E-Systems in 1995, which held the HAARP-related APTI patents. Hughes "
            "Aircraft had its own atmospheric research patents but these are distinct "
            "from the Eastlund HAARP patents."
        ),
        "year_start": 1997,
        "sources": [2442],
    },
    {
        "source": "NOAA",
        "target": "HAARP",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "NOAA monitors atmospheric and ionospheric conditions relevant to HAARP "
            "research. Both agencies are involved in studying the ionosphere and "
            "upper atmosphere, though HAARP is now operated by the University of "
            "Alaska Fairbanks rather than the military."
        ),
        "sources": [2442],
    },
    # ---- Oil Geopolitics ----
    {
        "source": "Enrico Mattei",
        "target": "ENI",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Founded and led ENI (Ente Nazionale Idrocarburi) from 1953 until his "
            "death in 1962. Challenged the Seven Sisters oil cartel by offering "
            "oil-producing nations 75-25 profit splits. A 1958 classified US National "
            "Security Council report called him 'an irritation and an obstacle.'"
        ),
        "year_start": 1953,
        "year_end": 1962,
        "sources": [2434],
    },
    {
        "source": "ENI",
        "target": "Standard Oil",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Under Mattei, ENI directly challenged the Anglo-American oil cartel's "
            "dominance by making independent deals with oil-producing nations at "
            "more favorable terms, undercutting the pricing structure that Standard "
            "Oil's successor companies (the Seven Sisters) had maintained since 1911."
        ),
        "year_start": 1953,
        "year_end": 1962,
        "sources": [2427, 2434],
    },
    {
        "source": "Ida Tarbell",
        "target": "Standard Oil",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Tarbell's 'The History of the Standard Oil Company' (serialized 1902-1904 "
            "in McClure's Magazine) exposed Rockefeller's monopolistic practices "
            "including railroad rebate schemes, predatory pricing, and espionage "
            "against competitors. The work contributed to the 1911 Supreme Court "
            "antitrust ruling that dissolved Standard Oil into 34 companies."
        ),
        "year_start": 1902,
        "year_end": 1911,
        "sources": [2430],
    },
    {
        "source": "Henri Deterding",
        "target": "Royal Dutch Shell",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Led Royal Dutch Shell from 1900 to 1936, known as the 'Napoleon of Oil.' "
            "Built it into Standard Oil's chief global rival. Became a Nazi sympathizer "
            "in the 1930s, reportedly donating to the NSDAP. Retired to Germany in "
            "1936; his 1939 funeral was attended by Nazi officials and Hitler sent a "
            "wreath."
        ),
        "year_start": 1900,
        "year_end": 1936,
        "sources": [2427, 2439],
    },
    {
        "source": "Royal Dutch Shell",
        "target": "Standard Oil",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Shell and Standard Oil were the dominant global rivals in the early "
            "petroleum industry. Their competition shaped oil markets, geopolitics, "
            "and the structure of the Seven Sisters cartel that controlled global "
            "oil for most of the 20th century."
        ),
        "year_start": 1907,
        "sources": [2427, 2439],
    },
    {
        "source": "Muammar Gaddafi",
        "target": "Nicolas Sarkozy",
        "type": "funded",
        "tier": "documented",
        "desc": (
            "The Gaddafi regime provided illegal campaign financing for Sarkozy's "
            "2007 French presidential campaign. Prosecution alleged approximately "
            "50 million euros funneled through intermediaries. Sarkozy was convicted "
            "in September 2025 of criminal conspiracy and corruption, sentenced to "
            "five years in prison plus a 100,000 euro fine."
        ),
        "year_start": 2005,
        "year_end": 2007,
        "sources": [2416, 2437],
    },
    {
        "source": "Nicolas Sarkozy",
        "target": "Muammar Gaddafi",
        "type": "targeted",
        "tier": "documented",
        "desc": (
            "As French president, Sarkozy was the leading advocate for NATO military "
            "intervention in Libya (2011), which resulted in the overthrow and killing "
            "of Gaddafi. Critics note the intervention came after Gaddafi had publicly "
            "threatened to reveal the campaign financing arrangement."
        ),
        "year_start": 2011,
        "sources": [2416, 2437],
    },
    {
        "source": "Hugo Chávez",
        "target": "PDVSA",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Chavez nationalized Venezuela's oil industry in 2007, asserting state "
            "control over PDVSA after firing 18,000 workers following a 2002-2003 "
            "management strike. He redirected oil revenues to fund social programs "
            "(Bolivarian missions) and used PDVSA as a geopolitical tool for "
            "regional influence."
        ),
        "year_start": 2007,
        "year_end": 2013,
        "sources": [2428, 2433, 2438],
    },
    {
        "source": "PDVSA",
        "target": "Nicolás Maduro",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Under Maduro (2013-), PDVSA production collapsed from approximately "
            "3 million bpd to under 900,000 bpd due to corruption, mismanagement, "
            "US sanctions, and chronic underinvestment. Maduro maintained control of "
            "the company as a patronage instrument despite economic collapse."
        ),
        "year_start": 2013,
        "sources": [2409, 2433],
    },
    {
        "source": "Hugo Chávez",
        "target": "CIA",
        "type": "target_of",
        "tier": "documented",
        "desc": (
            "Declassified CIA documents (released 2004 via FOIA, published by "
            "National Security Archive at GWU) show the US had advance knowledge of "
            "the April 2002 coup that briefly deposed Chavez. NED funded approximately "
            "$877,000 to Venezuelan opposition groups in 2001-2002. The Bush "
            "administration initially recognized the coup government before Chavez's "
            "restoration 47 hours later."
        ),
        "year_start": 2002,
        "sources": [2404, 2405, 2428],
    },
    {
        "source": "Hugo Chávez",
        "target": "Muammar Gaddafi",
        "type": "ally_of",
        "tier": "credible",
        "desc": (
            "Political allies who challenged Western oil hegemony and the petrodollar "
            "system. Both nationalized their nations' oil. Chavez publicly denounced "
            "the NATO intervention in Libya and mourned Gaddafi after his death in "
            "2011. Both were targets of US regime-change efforts."
        ),
        "sources": [2428, 2438],
    },
    {
        "source": "John Perkins",
        "target": "World Bank",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "In 'Confessions of an Economic Hit Man' (2004), Perkins described "
            "working as a consultant whose real role was saddling developing nations "
            "with unpayable debt to benefit US corporate interests. The systemic "
            "practices he describes (conditionality lending, debt traps) are "
            "documented by other sources (Stiglitz, Klein), though his personal "
            "autobiography as a recruited EHM is unverifiable."
        ),
        "sources": [2429],
    },
    {
        "source": "Karen Silkwood",
        "target": "Kerr-McGee Corporation",
        "type": "whistleblower_on",
        "tier": "documented",
        "desc": (
            "Silkwood discovered safety violations and plutonium contamination of "
            "workers at Kerr-McGee's Cimarron plant in Oklahoma. Died in a suspicious "
            "single-car crash November 13, 1974 while en route to deliver documents "
            "to a NYT reporter. The Supreme Court (1984) and subsequent $1.38 million "
            "settlement (1986) established the legal precedent."
        ),
        "year_start": 1974,
        "sources": [2401, 2431, 2436],
    },
    {
        "source": "Kerr-McGee Corporation",
        "target": "DOE",
        "type": "regulated_by",
        "tier": "documented",
        "desc": (
            "Nuclear fuel processing company regulated by the Atomic Energy "
            "Commission, later NRC and DOE. The Silkwood SCOTUS case (464 U.S. 238, "
            "1984) established that federal nuclear regulation under the AEC/NRC does "
            "not preempt state tort law, a landmark ruling for nuclear industry "
            "accountability."
        ),
        "sources": [2401, 2440],
    },
    # ---- MIC / Defense Tech ----
    {
        "source": "Palantir Technologies",
        "target": "Peter Thiel",
        "type": "co_founded",
        "tier": "documented",
        "desc": (
            "Co-founded in 2003 by Peter Thiel, Joe Lonsdale, Stephen Cohen, Nathan "
            "Gettings, and Alex Karp (CEO). Thiel provided initial funding and his "
            "Founders Fund continued as a major investor."
        ),
        "year_start": 2003,
        "sources": [2441],
    },
    {
        "source": "Palantir Technologies",
        "target": "In-Q-Tel",
        "type": "funded_by",
        "tier": "documented",
        "desc": (
            "CIA's venture capital arm In-Q-Tel was an early and significant investor "
            "in Palantir Technologies, providing seed funding and early contracts that "
            "validated the company's data analytics platform for intelligence use."
        ),
        "year_start": 2004,
        "sources": [2441],
    },
    {
        "source": "Palantir Technologies",
        "target": "CIA",
        "type": "contracted_with",
        "tier": "documented",
        "desc": (
            "Major intelligence community contractor. Palantir Gotham platform used "
            "for counterterrorism analysis, intelligence fusion, and operational "
            "planning across CIA and other agencies. The CIA was Palantir's first "
            "major customer."
        ),
        "year_start": 2005,
        "sources": [2441],
    },
    {
        "source": "In-Q-Tel",
        "target": "CIA",
        "type": "subsidiary_of",
        "tier": "documented",
        "desc": (
            "CIA's strategic venture capital arm, founded 1999 to invest in "
            "technology companies serving intelligence community needs. Funded "
            "companies that became core surveillance and analytics infrastructure "
            "including Palantir, Keyhole (later Google Earth), and others."
        ),
        "year_start": 1999,
        "sources": [2441],
    },
    {
        "source": "Anduril Industries",
        "target": "Peter Thiel",
        "type": "funded_by",
        "tier": "documented",
        "desc": (
            "Peter Thiel's Founders Fund was an early lead investor in Anduril "
            "Industries. Thiel is thus a key financial link between Palantir and "
            "Anduril, the two dominant Silicon Valley defense-tech companies."
        ),
        "year_start": 2017,
        "sources": [2435],
    },
    {
        "source": "Erik Prince",
        "target": "Blackwater",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Founded Blackwater USA in 1997 as a private military training facility "
            "in Moyock, North Carolina. Company grew into the largest private military "
            "contractor during the Iraq War. Blackwater contractors killed 17 Iraqi "
            "civilians at Nisour Square in 2007; four were convicted, later pardoned "
            "by Trump in December 2020."
        ),
        "year_start": 1997,
        "sources": [2445, 2446],
    },
    {
        "source": "Blackwater",
        "target": "CIA",
        "type": "contracted_with",
        "tier": "credible",
        "desc": (
            "Held classified contracts with CIA for covert operations, including "
            "providing personnel for the agency's targeted killing program. The "
            "relationship was documented by investigative journalists and confirmed "
            "through congressional inquiries."
        ),
        "year_start": 2002,
        "year_end": 2009,
        "sources": [2445],
    },
    {
        "source": "Boeing Defense",
        "target": "Boeing F-47",
        "type": "contracted_with",
        "tier": "documented",
        "desc": (
            "Boeing awarded the engineering and manufacturing development contract "
            "for the F-47 Next Generation Air Dominance sixth-generation fighter, "
            "valued at over $20 billion, announced March 21, 2025."
        ),
        "year_start": 2025,
        "sources": [2414],
    },
    {
        "source": "Lockheed Martin",
        "target": "Boeing F-47",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Lockheed Martin lost the NGAD competition to Boeing, a significant "
            "reversal for the company that built both the F-22 Raptor and F-35 "
            "Lightning II. The loss raised questions about Lockheed's dominance in "
            "the air superiority fighter market."
        ),
        "year_start": 2025,
        "sources": [2414],
    },
    {
        "source": "Bechtel Corporation",
        "target": "Cochabamba Water War",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "Bechtel subsidiary Aguas del Tunari raised water rates up to 200% after "
            "taking over Cochabamba's municipal water system under World Bank "
            "structural adjustment conditions. Even rainwater collection was "
            "effectively prohibited. Mass protests led to martial law, one death, "
            "and cancellation of the privatization contract in April 2000."
        ),
        "year_start": 1999,
        "year_end": 2000,
        "sources": [2447],
    },
    {
        "source": "Steven Bechtel Sr",
        "target": "Bechtel Corporation",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Led Bechtel Corporation, building it into one of the largest private "
            "construction and engineering firms in the world. The Bechtel family has "
            "maintained control across generations, with the revolving door to "
            "government exemplified by executives Caspar Weinberger and George Shultz "
            "moving directly into Reagan cabinet positions."
        ),
        "sources": [2447],
    },
    {
        "source": "Dick Cheney",
        "target": "Halliburton",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "CEO of Halliburton from 1995 to 2000 before becoming Vice President. "
            "Under his leadership, Halliburton acquired Dresser Industries. After "
            "Cheney became VP, Halliburton's KBR subsidiary received $39.5 billion "
            "in Iraq war contracts, many no-bid, with DOD IG finding widespread "
            "billing irregularities."
        ),
        "year_start": 1995,
        "year_end": 2000,
        "sources": [2427],
    },
    {
        "source": "Chris Wright",
        "target": "DOE",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as US Secretary of Energy in early 2025. As DOE head, oversaw "
            "implementation of Trump's national energy emergency executive order, "
            "reversal of Biden's LNG export pause, and nuclear energy permitting "
            "streamlining executive orders."
        ),
        "year_start": 2025,
        "sources": [2421, 2422],
    },
    {
        "source": "Chris Wright",
        "target": "Donald Trump",
        "type": "appointed_by",
        "tier": "documented",
        "desc": (
            "Appointed by President Trump as Secretary of Energy. Wright, a fossil "
            "fuel industry CEO, represents the administration's emphasis on "
            "maximizing domestic energy production and rolling back climate-related "
            "regulations."
        ),
        "year_start": 2025,
        "sources": [2421],
    },
    # ---- Water ----
    {
        "source": "Veolia",
        "target": "Suez Group",
        "type": "acquired",
        "tier": "documented",
        "desc": (
            "Veolia completed its hostile acquisition of Suez for approximately 13 "
            "billion euros in January 2022, creating the world's largest private water "
            "utility. EU regulators required divestiture of Suez's French municipal "
            "water operations, sold to a consortium as 'New Suez.' Critics argue the "
            "combined entity creates a near-monopoly in global water privatization."
        ),
        "year_start": 2022,
        "sources": [2444],
    },
    {
        "source": "Nestlé Waters",
        "target": "Primo Brands Corporation",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Nestle sold its North American water brands (Poland Spring, Deer Park, "
            "Arrowhead, etc.) in 2021 for $4.3 billion to One Rock Capital Partners, "
            "which rebranded the division as BlueTriton Brands. BlueTriton merged "
            "with Primo Water Corporation in November 2024 to form Primo Brands "
            "Corporation (NYSE: PRMB)."
        ),
        "year_start": 2021,
        "year_end": 2024,
        "sources": [2406],
    },
    {
        "source": "Standing Rock Protests",
        "target": "Energy Transfer v. Greenpeace (2025)",
        "type": "preceded",
        "tier": "documented",
        "desc": (
            "The 2016-2017 Standing Rock protests against the Dakota Access Pipeline "
            "were the direct basis for Energy Transfer's lawsuit against Greenpeace. "
            "Energy Transfer alleged Greenpeace orchestrated misleading campaigns "
            "about threats to tribal sacred sites and water supplies during the "
            "protests."
        ),
        "year_start": 2016,
        "year_end": 2025,
        "sources": [2412],
    },
    # ---- Cartels ----
    {
        "source": "Donald Trump",
        "target": "Cartel FTO Designations (2025)",
        "type": "signed_into_law",
        "tier": "documented",
        "desc": (
            "Trump signed the executive order on February 20, 2025 designating the "
            "Sinaloa Cartel and CJNG as Foreign Terrorist Organizations, the first "
            "time drug cartels received FTO designation."
        ),
        "year_start": 2025,
        "sources": [2400, 2413],
    },
    {
        "source": "Sinaloa Cartel",
        "target": "Cartel FTO Designations (2025)",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "Designated as a Foreign Terrorist Organization and Specially Designated "
            "Global Terrorist under the February 20, 2025 executive order, enabling "
            "expanded legal authorities and financial sanctions."
        ),
        "year_start": 2025,
        "sources": [2400, 2413],
    },
    {
        "source": "Sinaloa Cartel",
        "target": "DEA",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "Subject of major DEA investigations spanning decades. Co-founder El "
            "Mayo Zambada pleaded guilty August 25, 2025 to racketeering conspiracy "
            "and continuing criminal enterprise, receiving a life sentence July 20, "
            "2026. Ovidio Guzman Lopez pleaded guilty July 11, 2025 and is reportedly "
            "cooperating."
        ),
        "sources": [2407, 2408, 2425, 2432],
    },
    {
        "source": "Medellín Cartel",
        "target": "Sinaloa Cartel",
        "type": "preceded",
        "tier": "credible",
        "desc": (
            "The Sinaloa Cartel rose to dominance as the Colombian Medellin Cartel "
            "collapsed in the early 1990s following Pablo Escobar's death. Mexican "
            "organizations, particularly Sinaloa, took over as primary cocaine "
            "transporters into the United States, inheriting and expanding smuggling "
            "routes."
        ),
        "sources": [2432],
    },
    {
        "source": "Sinaloa Cartel",
        "target": "Los Zetas",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Rivals in the Mexican drug war. The Sinaloa Cartel and Los Zetas "
            "fought for control of trafficking corridors across Mexico, contributing "
            "to an escalating cycle of violence. The cartels represent different "
            "models: Sinaloa relied on corruption; Zetas on paramilitary force."
        ),
        "sources": [2432],
    },
]

# ============================================================
# ENTITY → SOURCE mappings
# ============================================================

ENTITY_SOURCES = {
    "Sinaloa Cartel": [2400, 2407, 2408, 2413, 2425, 2432],
    "PDVSA": [2409, 2410, 2428, 2433],
    "ENI": [2427, 2434],
    "Royal Dutch Shell": [2427, 2439],
    "Kerr-McGee Corporation": [2401, 2431, 2436, 2440],
    "Anduril Industries": [2417, 2424, 2435],
    "Boeing F-47": [2414],
    "Chris Wright": [2421, 2422],
    "Energy Transfer v. Greenpeace (2025)": [2412],
    "Cartel FTO Designations (2025)": [2400, 2413],
    "Primo Brands Corporation": [2406],
}

# ============================================================
# ENTITY UPDATES — existing entities
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "Hugo Chávez",
        "description_append": (
            "2025 update: Declassified CIA documents (released 2004, published by "
            "the National Security Archive at GWU) confirm the US had advance "
            "knowledge of the April 2002 coup that briefly deposed Chavez for 47 "
            "hours. The NED funded approximately $877,000 to Venezuelan opposition "
            "groups in 2001-2002, per NED's own records. The Bush administration "
            "initially recognized the coup government of Pedro Carmona before "
            "Chavez's restoration. In 2007, Chavez nationalized PDVSA, firing 18,000 "
            "workers and redirecting oil revenues to social programs. PDVSA under his "
            "successors saw production collapse from 3 million to under 900,000 bpd."
        ),
        "sources": [2404, 2405, 2428, 2433, 2438],
    },
    {
        "name": "Muammar Gaddafi",
        "description_append": (
            "2025 update: In September 2025, French former president Nicolas Sarkozy "
            "was convicted of criminal conspiracy over a 'corruption pact' with the "
            "Gaddafi regime. The court found Gaddafi's Libya funneled approximately "
            "50 million euros in illegal campaign financing for Sarkozy's 2007 "
            "presidential campaign. Sarkozy was sentenced to five years in prison "
            "plus a 100,000 euro fine. He began serving at La Sante Prison on "
            "October 21, 2025 but was released November 10 pending appeal. The "
            "prosecution argued Sarkozy's subsequent leadership of the 2011 NATO "
            "intervention that killed Gaddafi was partly motivated by eliminating "
            "the witness to the financing arrangement."
        ),
        "sources": [2416, 2437],
    },
    {
        "name": "Nicolas Sarkozy",
        "description_append": (
            "2025 update: In September 2025, Sarkozy was convicted in the Libyan "
            "campaign financing case and sentenced to five years in prison plus a "
            "100,000 euro fine for his 'corruption pact' with Muammar Gaddafi. He "
            "began serving at La Sante Prison on October 21, 2025 in segregation, "
            "but was released after three weeks on November 10, 2025 pending appeal. "
            "This was his third criminal conviction, following the Bygmalion campaign "
            "spending case (2021) and the 'Paul Bismuth' wiretapping and corruption "
            "case (2023, upheld on appeal May 2023). He is the first former French "
            "president to serve prison time."
        ),
        "metadata": {"status": "convicted"},
        "sources": [2416, 2437],
    },
    {
        "name": "Karen Silkwood",
        "description_append": (
            "Legal aftermath: A 1979 federal jury awarded $10.5 million ($505,000 "
            "actual, $10 million punitive) against Kerr-McGee for plutonium "
            "contamination. The 10th Circuit reversed the punitive damages. The "
            "Supreme Court in Silkwood v. Kerr-McGee Corp. (464 U.S. 238, 1984) "
            "ruled 5-4 that state tort law punitive damages are not preempted by "
            "federal nuclear regulation under the Atomic Energy Act, reinstating "
            "the award. The case settled in 1986 for $1.38 million without admission "
            "of liability by Kerr-McGee."
        ),
        "sources": [2401, 2431, 2436],
    },
    {
        "name": "Bernard J. Eastlund",
        "description_append": (
            "Patent chain clarification: Eastlund's patent US4686605A was assigned "
            "to APTI Inc. (Advanced Power Technologies Inc., formerly ARCO Power "
            "Technologies, a subsidiary of ARCO). APTI was acquired by E-Systems "
            "in 1994, and E-Systems was acquired by Raytheon in 1995. The patent "
            "chain therefore runs Eastlund to APTI to E-Systems to Raytheon. Hughes "
            "Aircraft, acquired separately by Raytheon in 1997, had its own "
            "atmospheric research patents but is not in the direct Eastlund-HAARP "
            "patent chain."
        ),
        "sources": [2402, 2442],
    },
    {
        "name": "SCoPEx",
        "description_append": (
            "2024 update: Harvard announced the shutdown of its Solar Geoengineering "
            "Research Program in March 2024. The advisory committee had recommended "
            "against proceeding with outdoor testing. David Keith had already "
            "departed for the University of Chicago. No outdoor experiment was ever "
            "conducted. The program's closure marked the end of the most prominent "
            "institutional effort to conduct controlled solar geoengineering "
            "research."
        ),
        "metadata": {"status": "cancelled"},
        "sources": [2411],
    },
    {
        "name": "NOAA",
        "description_append": (
            "2025 update: NOAA faced significant budget and personnel cuts under "
            "the Trump administration's DOGE (Department of Government Efficiency) "
            "initiative in early 2025. Probationary employees were subjected to "
            "mass layoffs. The FY2026 budget proposal included substantial cuts to "
            "NOAA programs including the National Weather Service. Environmental "
            "scientists warned the cuts threatened weather forecasting capabilities "
            "and climate monitoring infrastructure."
        ),
        "sources": [2418],
    },
    {
        "name": "Palantir Technologies",
        "description_append": (
            "2025-2026 update: In July 2025, the US Army awarded Palantir an "
            "enterprise software agreement valued at up to $10 billion over 10 "
            "years, consolidating 75 previously separate contracts. Palantir "
            "maintains a $30 million ICE contract tracking migrant movement, and "
            "DOGE requested Palantir assistance in creating a deportation database. "
            "In December 2025, Palantir won a 240 million pound UK Ministry of "
            "Defence direct-award contract for data analytics capabilities. The "
            "Pentagon and DHS spent $113 million on existing and new Palantir "
            "contracts, plus a $795 million DoD contract in May 2025."
        ),
        "sources": [2415, 2426, 2441],
    },
    {
        "name": "Standing Rock Protests",
        "description_append": (
            "2025 update: In February 2025, a North Dakota jury awarded Energy "
            "Transfer $666.8 million in damages in a civil lawsuit against "
            "Greenpeace USA and affiliates, holding them liable for their role in "
            "organizing the Standing Rock protests. The verdict was one of the "
            "largest against an environmental organization. Environmental groups "
            "condemned it as a SLAPP suit designed to chill activism. Greenpeace is "
            "appealing. A previous RICO-based federal lawsuit by Energy Transfer "
            "had been dismissed in 2019."
        ),
        "sources": [2412],
    },
    {
        "name": "Flint Water Crisis",
        "description_append": (
            "2024 update: The $626 million settlement, granted final approval in "
            "November 2021 by Judge Judith Levy, began distributing payments to "
            "claimants in 2023-2024. A majority of registered claimants have "
            "received initial payments, though many reported delays and disputes "
            "over amounts. The settlement funds were allocated primarily toward "
            "children exposed to lead contamination, who were entitled to the "
            "largest individual awards."
        ),
        "sources": [2420],
    },
    {
        "name": "Nestlé Waters",
        "description_append": (
            "2024 update: BlueTriton Brands (the rebranded former Nestle Waters "
            "North America) completed its merger with Primo Water Corporation on "
            "November 8, 2024, forming Primo Brands Corporation (NYSE: PRMB). The "
            "combined entity now controls a significant portion of the US bottled "
            "water market including Poland Spring, Deer Park, Arrowhead, and "
            "Primo's water dispenser business."
        ),
        "sources": [2406],
    },
    {
        "name": "DOE",
        "description_append": (
            "2025 update: Chris Wright, CEO of Liberty Energy, was confirmed as "
            "Secretary of Energy in early 2025 under President Trump. Trump signed "
            "a national energy emergency executive order on January 20, 2025 "
            "(Inauguration Day), directing agencies to expedite energy production. "
            "The administration reversed Biden's January 2024 pause on new LNG "
            "export terminal approvals, rapidly approving pending projects. Nuclear "
            "energy executive orders were issued to streamline reactor permitting, "
            "and the proposed FY2026 budget reflected the administration's fossil "
            "fuel priorities."
        ),
        "sources": [2421, 2422],
    },
    {
        "name": "Thames Water",
        "description_append": (
            "2025-2026 update: In March 2025, US private equity firm KKR was named "
            "preferred bidder with a 4 billion pound deal, but KKR pulled out in "
            "June 2025, increasing the likelihood of a government Special "
            "Administration Regime (SAR). Thames Water's largest creditors, holding "
            "13 billion pounds of 20 billion total debt, proposed a rescue through "
            "their London and Valley Water consortium (L&VW), including a ten-year "
            "dividend suspension and a government 'golden share.' In June 2026, "
            "the environment secretary stated the creditor proposal did not do "
            "enough to protect consumers or the environment. Thames Water remains "
            "under severe financial distress as of August 2026."
        ),
        "sources": [2419, 2443],
    },
    {
        "name": "Glencore",
        "description_append": (
            "Glencore is the world's largest commodities trading company, founded "
            "by Marc Rich (pardoned by Bill Clinton in 2001). Has faced corruption "
            "investigations across multiple jurisdictions. In 2022, Glencore pleaded "
            "guilty to bribery charges in the US, UK, and Brazil, paying over $1.5 "
            "billion in fines. Partially owned by Nathaniel Rothschild. Glencore "
            "operates in the extractive industries worldwide, with significant "
            "presence in cobalt mining in the Democratic Republic of Congo."
        ),
        "sources": [2427],
    },
]

# ============================================================
# GEO_COORDS — new entities only
# ============================================================

GEO_COORDS = {
    "Sinaloa Cartel": (24.8091, -107.3940, "credible", "Culiacán, Sinaloa, Mexico — cartel base"),
    "PDVSA": (10.4806, -66.9036, "credible", "Caracas, Venezuela — PDVSA headquarters"),
    "ENI": (41.8327, 12.4388, "credible", "Rome, Italy — ENI headquarters"),
    "Royal Dutch Shell": (51.5074, -0.1278, "credible", "London, UK — Shell plc headquarters"),
    "Kerr-McGee Corporation": (35.4676, -97.5164, "credible", "Oklahoma City, OK — former headquarters"),
    "Anduril Industries": (33.6846, -117.9112, "credible", "Costa Mesa, CA — Anduril headquarters"),
    "Boeing F-47": (38.8977, -77.0365, "inference", "Washington DC — USAF program administration"),
    "Chris Wright": (38.8977, -77.0365, "inference", "Washington DC — DOE headquarters"),
    "Energy Transfer v. Greenpeace (2025)": (46.7192, -100.9324, "documented", "Morton County, ND — trial location"),
    "Cartel FTO Designations (2025)": (38.8977, -77.0365, "documented", "Washington DC — White House executive order"),
    "Primo Brands Corporation": (41.0534, -73.5387, "credible", "Stamford, CT — corporate headquarters"),
}

# ============================================================
# PHOTO_CANDIDATES — new persons/orgs
# ============================================================

PHOTO_CANDIDATES = {
    "Chris Wright": "https://commons.wikimedia.org/wiki/File:Secretary_Chris_Wright_Official_Portrait.jpg",
    "ENI": "https://commons.wikimedia.org/wiki/File:Eni_SpA.svg",
    "Royal Dutch Shell": "https://commons.wikimedia.org/wiki/File:Shell_logo.svg",
    "Anduril Industries": "https://commons.wikimedia.org/wiki/File:Anduril_Industries_logo.svg",
}
