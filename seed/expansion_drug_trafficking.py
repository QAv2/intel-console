"""
Drug Trafficking & Intelligence — Expansion layer for Intel Console.

Maps the documented history of CIA involvement in the global narcotics trade,
from the Golden Triangle heroin pipeline through Air America in the 1960s-70s,
to the Iran-Contra cocaine nexus in the 1980s, to Operation Fast and Furious
in the 2010s. This expansion focuses on the institutional mechanisms — front
airlines, cutout banks, complicit cartels, and the whistleblowers who exposed
them.

The pattern is consistent across decades: intelligence agencies use drug
trafficking networks as covert funding mechanisms and leverage points, protect
traffickers who serve operational goals, and destroy the careers (or lives) of
anyone who documents the connection.

DOCUMENTED (congressional/court/FOIA):
- Kerry Committee (1989): 1,166-page Senate report documenting Contra drug links
- CIA Inspector General (1998): confirmed CIA failed to investigate Contra cocaine
- Air America: declassified CIA records confirm proprietary airline operated in
  Laos/Vietnam; McCoy's academic work documents heroin facilitation
- Nugan Hand Bank: Australian Royal Commission (1985) documented CIA connections
- Dark Alliance: Gary Webb's reporting substantiated by CIA IG report
- Operation Fast and Furious: DOJ IG report (2012), congressional investigation
- Freeway Rick Ross: federal court records, CIA IG Vol. II names Blandon/Meneses
- Khun Sa: offered to name CIA officials to DEA; Bo Gritz interview on tape

CREDIBLE (journalism/testimony/academic):
- Michael Levine's DEA testimony on CIA obstruction of drug investigations
- Cele Castillo's documentation of drug flights from Ilopango
- McCoy's academic research on CIA-heroin nexus (peer-reviewed, Yale)

INFERENCE:
- Mena Airport operations pattern (multiple independent witnesses, no single
  declassified confirmation of CIA role at Mena specifically)

Entities (19 new): People (Freeway Rick Ross, Michael Levine, Cele Castillo,
Bo Gritz, Khun Sa), organizations (Air America, Nugan Hand Bank, Cali Cartel,
Los Zetas), programs/events (Dark Alliance, Operation Fast and Furious, Golden
Triangle Drug Trade, Mena Airport Operations, Kerry Committee Investigation
[already exists — referenced only]), facilities (Mena Airport), publications
(Dark Alliance series).

NOTE: Kerry Committee Investigation, Medellin Cartel, Oliver North, Manuel
Noriega, Gary Webb, Augusto Pinochet, SETCO Aviation, School of the Americas,
Operation Condor, Felix Rodriguez, and Andres Pastrana are defined in
expansion_latin_america.py and are referenced by name only.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], FBI [87], DEA [not in DB — will create], NSA [86], DOJ [89],
  Barry Seal [curated], Southern Air Transport [curated], Oliver North [latin_america],
  Iran-Contra [curated], School of the Americas [latin_america], BCCI [curated],
  Gary Webb [latin_america], Bill Clinton [curated], George H.W. Bush [bohemian_grove],
  Manuel Noriega [latin_america], Augusto Pinochet [latin_america],
  Medellin Cartel [latin_america], Kerry Committee Investigation [latin_america],
  SETCO Aviation [latin_america], Felix Rodriguez [latin_america]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1051-1080
# ============================================================

SOURCES = [
    # --- Air America / Golden Triangle ---
    {
        "id": 1051,
        "title": "Alfred W. McCoy — The Politics of Heroin: CIA Complicity in the Global Drug Trade (1972, revised 2003). Definitive academic study documenting CIA facilitation of opium/heroin trafficking in Southeast Asia through Air America and allied warlords. Yale University Press.",
        "url": "https://yalebooks.yale.edu/book/9780300143720/the-politics-of-heroin/",
        "source_type": "academic",
        "author": "Alfred W. McCoy",
        "year": 2003,
    },
    {
        "id": 1052,
        "title": "CIA FOIA Reading Room — Air America declassified records. Documents confirming Air America as CIA proprietary airline operating in Laos, Thailand, and Vietnam from 1950-1976.",
        "url": "https://www.cia.gov/readingroom/collection/air-america",
        "source_type": "foia",
        "year": 2013,
    },
    {
        "id": 1053,
        "title": "William M. Leary — 'CIA Air Operations in Laos, 1955-1974: Supporting the Secret War' (Studies in Intelligence, Winter 1999-2000). CIA's own declassified history of Air America operations.",
        "url": "https://www.cia.gov/static/a743608236d2fbb7bbb87b54db8bf8fe/CIA-Air-Operations-in-Laos.pdf",
        "source_type": "government",
        "author": "William M. Leary",
        "year": 1999,
    },
    {
        "id": 1054,
        "title": "Senate Foreign Relations Committee — 'Opium and Politics in Laos' (Staff Report, 1971). Early congressional documentation of the opium trade in Laos and U.S. involvement.",
        "url": "https://catalog.hathitrust.org/Record/000553019",
        "source_type": "congressional",
        "year": 1971,
    },
    # --- Nugan Hand Bank ---
    {
        "id": 1055,
        "title": "Joint Task Force on Drug Trafficking (Stewart Royal Commission) — Royal Commission of Inquiry into Drug Trafficking (Australia, 1983). Investigated Nugan Hand Bank's CIA connections and drug money laundering. Found the bank was a 'vehicle for CIA activities.'",
        "url": "https://en.wikipedia.org/wiki/Nugan_Hand_Bank#Royal_Commission",
        "source_type": "government",
        "year": 1985,
    },
    {
        "id": 1056,
        "title": "Jonathan Kwitny — The Crimes of Patriots: A True Tale of Dope, Dirty Money, and the CIA (1987). Wall Street Journal reporter's investigation of Nugan Hand Bank, documenting CIA officers in bank management and heroin money laundering.",
        "url": "https://archive.org/details/crimesofpatriots00kwit",
        "source_type": "book",
        "author": "Jonathan Kwitny",
        "year": 1987,
    },
    # --- Freeway Rick Ross / Dark Alliance ---
    {
        "id": 1057,
        "title": "CIA Inspector General — 'Report of Investigation: Allegations of Connections Between CIA and the Contras in Cocaine Trafficking to the United States, Volume II: The Contra Story' (1998). Names Oscar Danilo Blandon and Norwin Meneses as Contra fundraisers who supplied Rick Ross.",
        "url": "https://irp.fas.org/cia/product/cocaine2/",
        "source_type": "government",
        "year": 1998,
    },
    {
        "id": 1058,
        "title": "Gary Webb — Dark Alliance: The CIA, the Contras, and the Crack Cocaine Explosion (Seven Stories Press, 1998). Book-length expansion of the San Jose Mercury News series, documenting the Blandon-Meneses-Ross pipeline.",
        "url": "https://archive.org/details/darkalliance0000webb",
        "source_type": "book",
        "author": "Gary Webb",
        "year": 1998,
    },
    {
        "id": 1059,
        "title": "U.S. v. Ricky Donnell Ross — Federal sentencing documents and court proceedings (C.D. Cal., 1996). Blandon testified as government witness; acknowledged receiving CIA-connected Contra supply money while selling cocaine to Ross.",
        "url": "https://law.justia.com/cases/federal/appellate-courts/F3/210/916/510529/",
        "source_type": "court",
        "year": 1996,
    },
    # --- Michael Levine (DEA whistleblower) ---
    {
        "id": 1060,
        "title": "Michael Levine — The Big White Lie: The Deep Cover Operation That Exposed the CIA Sabotage of the Drug War (1993). 25-year DEA veteran documents CIA obstruction of Operation Hun, the largest cocaine investigation of the 1980s targeting the Bolivian government's cocaine operation.",
        "url": "https://archive.org/details/bigwhiteliedeep00levi",
        "source_type": "book",
        "author": "Michael Levine",
        "year": 1993,
    },
    {
        "id": 1061,
        "title": "Michael Levine — 'Expert Witness: The Big White Lie' (PBS Frontline interview transcript, 2000). Levine's on-record testimony that CIA repeatedly sabotaged DEA operations targeting major traffickers who were CIA assets.",
        "url": "https://www.pbs.org/wgbh/pages/frontline/shows/drugs/interviews/levine.html",
        "source_type": "journalism",
        "author": "Michael Levine",
        "year": 2000,
    },
    # --- Cele Castillo ---
    {
        "id": 1062,
        "title": "Celerino Castillo III — Powderburns: Cocaine, Contras & the Drug War (1994). DEA agent stationed in El Salvador documents drug-laden flights from Ilopango Air Base, reports to superiors ignored, warned by U.S. Embassy to stop reporting.",
        "url": "https://archive.org/details/powderburnscoca100cast",
        "source_type": "book",
        "author": "Celerino Castillo III",
        "year": 1994,
    },
    {
        "id": 1063,
        "title": "C-SPAN — Cele Castillo testimony at Senate hearing on drug enforcement (1996). On-record congressional testimony describing drug flights from Ilopango, Felix Rodriguez involvement, and DEA/Embassy obstruction.",
        "url": "https://www.c-span.org/video/?72018-1/us-drug-enforcement",
        "source_type": "congressional",
        "year": 1996,
    },
    # --- Bo Gritz / Khun Sa ---
    {
        "id": 1064,
        "title": "James 'Bo' Gritz — A Nation Betrayed (1989). Retired Lt. Col. and Green Beret documents his 1986-87 meetings with Khun Sa in the Golden Triangle, where Khun Sa offered to name CIA officials involved in the heroin trade and offered to end opium production for $20 million/year crop substitution.",
        "url": "https://archive.org/details/nationbetrayed00grit",
        "source_type": "book",
        "author": "James 'Bo' Gritz",
        "year": 1989,
    },
    {
        "id": 1065,
        "title": "Khun Sa — Video deposition to U.S. government (1987). Recorded statement by Khun Sa naming Richard Armitage and others as facilitating heroin trade. Gritz delivered tape to DEA and Congressional offices; no investigation followed.",
        "url": "https://archive.org/details/KhunSaIdentifiesRichardArmitage",
        "source_type": "other",
        "year": 1987,
    },
    {
        "id": 1066,
        "title": "Bertil Lintner — Burma in Revolt: Opium and Insurgency Since 1948 (Silkworm Books, 2003). Academic study of Burma's opium economy, Khun Sa's Shan United Army, and the Golden Triangle drug trade in geopolitical context.",
        "url": "https://archive.org/details/burmainrevoltopi0000lint",
        "source_type": "academic",
        "author": "Bertil Lintner",
        "year": 2003,
    },
    # --- Mena Airport ---
    {
        "id": 1067,
        "title": "Arkansas Committee — The Mena Cover-Up (documentary, 1995). Compiles witness testimony, financial records, and investigative reporting on CIA/drug operations at Mena Intermountain Municipal Airport, including Barry Seal's operations.",
        "url": "https://archive.org/details/TheMenaCoverup",
        "source_type": "documentary",
        "year": 1995,
    },
    {
        "id": 1068,
        "title": "Ambrose Evans-Pritchard — 'Clinton and the Mena Airport Affair' (The Telegraph, 1995). British journalist's investigation of drug-running and money laundering at Mena, Barry Seal's connection to the Arkansas Development Finance Authority, and state/federal obstruction of investigation.",
        "url": "https://www.telegraph.co.uk/news/worldnews/northamerica/usa/1360168/Clinton-and-the-Mena-Airport-affair.html",
        "source_type": "journalism",
        "author": "Ambrose Evans-Pritchard",
        "year": 1995,
    },
    {
        "id": 1069,
        "title": "IRS Investigator William Duncan — Congressional testimony on Mena Airport money laundering investigation (House Banking Committee, 1994). Duncan testified that his investigation into millions of dollars laundered through Mena was obstructed by DOJ and Arkansas state officials.",
        "url": "https://irp.fas.org/congress/1994_hr/940621-mena.htm",
        "source_type": "congressional",
        "year": 1994,
    },
    # --- Cali Cartel ---
    {
        "id": 1070,
        "title": "Senate Permanent Subcommittee on Investigations — 'The Drug Cartel: The Impact of the Cali Cartel on the United States' (1994). Report documenting the Cali Cartel's rise as the dominant cocaine supplier after the Medellin Cartel's collapse.",
        "url": "https://catalog.hathitrust.org/Record/003431457",
        "source_type": "congressional",
        "year": 1994,
    },
    {
        "id": 1071,
        "title": "Los Angeles Times — 'CIA, Contras and Drugs: Questions on Links Linger' (October 21, 1996). Reports on Colombian National Police commander General Rosso Jose Serrano's cooperation with CIA while CIA's Cali informant network overlapped with the cartel.",
        "url": "https://www.latimes.com/archives/la-xpm-1996-10-21-mn-56185-story.html",
        "source_type": "journalism",
        "year": 1996,
    },
    # --- Los Zetas ---
    {
        "id": 1072,
        "title": "Narco News — 'The Zetas: How U.S.-Trained Commandos Became Mexico's Deadliest Cartel' (2010). Documents how Los Zetas were founded by Mexican special forces soldiers trained at Fort Bragg and the School of the Americas.",
        "url": "https://narconews.com/issue67/article4216.html",
        "source_type": "journalism",
        "year": 2010,
    },
    {
        "id": 1073,
        "title": "George W. Grayson — 'Los Zetas: The Ruthless Army Spawned by a Mexican Drug Cartel' (Praeger, 2014). Academic study documenting the military-to-cartel pipeline and U.S. training of GAFE commandos who became Los Zetas founders.",
        "url": "https://publisher.abc-clio.com/9780313398322",
        "source_type": "academic",
        "author": "George W. Grayson",
        "year": 2014,
    },
    # --- Operation Fast and Furious ---
    {
        "id": 1074,
        "title": "DOJ Office of Inspector General — 'A Review of ATF's Operation Fast and Furious and Related Matters' (September 2012). 471-page report documenting ATF's deliberate facilitation of 2,000+ firearms to Mexican cartels, DOJ obstruction, and resulting death of Border Patrol Agent Brian Terry.",
        "url": "https://oig.justice.gov/sites/default/files/reports/2012/s1209.pdf",
        "source_type": "government",
        "year": 2012,
    },
    {
        "id": 1075,
        "title": "House Committee on Oversight and Government Reform — 'Fast and Furious: The Anatomy of a Failed Operation' (Joint Staff Report, July 2011). Congressional investigation documenting ATF's gunwalking program and DOJ cover-up.",
        "url": "https://oversight.house.gov/report/fast-and-furious-the-anatomy-of-a-failed-operation/",
        "source_type": "congressional",
        "year": 2011,
    },
    {
        "id": 1076,
        "title": "House Resolution 711 — Contempt of Congress citation against Attorney General Eric Holder for refusal to produce documents related to Operation Fast and Furious (June 28, 2012). First sitting AG held in contempt.",
        "url": "https://www.congress.gov/bill/112th-congress/house-resolution/711",
        "source_type": "congressional",
        "year": 2012,
    },
    # --- Kerry Committee / broader context ---
    {
        "id": 1077,
        "title": "Kerry Committee — 'Drugs, Law Enforcement and Foreign Policy' (April 13, 1989). 1,166-page Senate report. Chapter 2 covers State Department payments to drug traffickers for Contra aid. Chapter 4 covers SETCO, Hull ranch, and pilot drug trafficking.",
        "url": "https://archive.org/details/Kerry-Report-Drugs-Contras",
        "source_type": "congressional",
        "author": "Senate Subcommittee on Terrorism, Narcotics, and International Operations",
        "year": 1989,
    },
    {
        "id": 1078,
        "title": "The Intercept — 'Managing a Nightmare: How the CIA Watched Over the Destruction of Gary Webb' (September 25, 2014). FOIA-obtained CIA internal memo titled 'Managing a Nightmare' showing CIA actively tracked and facilitated media attacks on Webb.",
        "url": "https://theintercept.com/2014/09/25/managing-nightmare-cia-media-destruction-gary-webb/",
        "source_type": "journalism",
        "year": 2014,
    },
    {
        "id": 1079,
        "title": "Peter Dale Scott — 'Drugs, Oil, and War: The United States in Afghanistan, Colombia, and Indochina' (Rowman & Littlefield, 2003). Academic study connecting CIA drug facilitation across theaters — Golden Triangle, Contra cocaine, Afghan heroin — as structural feature rather than aberration.",
        "url": "https://rowman.com/ISBN/9780742525221",
        "source_type": "academic",
        "author": "Peter Dale Scott",
        "year": 2003,
    },
    {
        "id": 1080,
        "title": "Senate Caucus on International Narcotics Control — 'U.S. International Drug Control Policy' (hearing, 1988). Testimony on DEA operations in Latin America, CIA interference with drug investigations, and Noriega's dual role as CIA asset and drug trafficker.",
        "url": "https://catalog.hathitrust.org/Record/007610714",
        "source_type": "congressional",
        "year": 1988,
    },
]


# ============================================================
# ENTITIES — 19 new
# ============================================================

ENTITIES = [
    # --- PEOPLE ---
    {
        "name": "Freeway Rick Ross",
        "entity_type": "person",
        "description": (
            "Ricky Donnell Ross. Born January 26, 1960, Tyler, Texas. Became the largest "
            "crack cocaine dealer in Los Angeles in the early-to-mid 1980s, distributing an "
            "estimated $600 million worth of crack between 1982 and 1989.\n\n"
            "The CIA connection: Ross's primary cocaine supplier was Oscar Danilo Blandon, a "
            "Nicaraguan exile who had been fundraising for the CIA-backed Contras. Blandon's "
            "supplier was Norwin Meneses, the head of Nicaraguan drug operations and a known "
            "Contra fundraiser. The CIA Inspector General's 1998 Volume II confirmed that "
            "Blandon and Meneses 'ichanneled money to the Contras' while simultaneously "
            "supplying cocaine that fueled the LA crack epidemic.\n\n"
            "Gary Webb's 'Dark Alliance' series (1996) traced this pipeline: Meneses → "
            "Blandon → Ross → LA streets. The crack epidemic devastated Black communities "
            "in South Central LA, Compton, and beyond.\n\n"
            "At trial (1996), Blandon — who had been granted immunity and became a paid DEA "
            "informant ($45,000/year) — testified as a government witness against Ross. "
            "Blandon admitted under oath to selling cocaine to fund the Contras. Ross was "
            "sentenced to life (later reduced to 20 years on appeal). Released 2009."
        ),
        "aliases": "Freeway Ricky Ross, Rick Ross",
        "metadata": {},
    },
    {
        "name": "Michael Levine",
        "entity_type": "person",
        "description": (
            "DEA special agent for 25 years (1965-1990). Became the most decorated agent "
            "in DEA history. Ran some of the largest undercover drug operations in U.S. "
            "history, including Operation Hun — the 1980 investigation that targeted "
            "Bolivia's military junta and its cocaine operation.\n\n"
            "Turned whistleblower after documenting repeated CIA sabotage of DEA "
            "investigations. In 'The Big White Lie' (1993), Levine detailed how CIA "
            "protected major drug traffickers who served as intelligence assets:\n"
            "- Operation Hun (1980): Levine infiltrated the Bolivian government's cocaine "
            "  operation at the highest levels. CIA intervened to protect the Bolivian "
            "  military junta (which had just staged the 'Cocaine Coup'), sabotaging the "
            "  investigation. The junta's chief of intelligence was on the CIA payroll.\n"
            "- Roberto Suarez: Bolivia's largest cocaine trafficker, offered to sell Levine "
            "  the entire annual Bolivian cocaine output. Investigation killed by CIA.\n"
            "- Testified to Congress and in media that CIA obstruction was not aberrational "
            "  but systematic — traffickers who served CIA interests were untouchable.\n\n"
            "Published 'The Big White Lie' (1993) and 'Deep Cover' (1990). Hosted 'The "
            "Expert Witness Show' radio program. His testimony corroborated Webb, Castillo, "
            "and Kerry Committee findings from a DEA insider perspective."
        ),
        "metadata": {},
    },
    {
        "name": "Cele Castillo",
        "entity_type": "person",
        "description": (
            "Celerino Castillo III. DEA special agent stationed in Guatemala and El Salvador "
            "during the Iran-Contra era (1985-1990). Vietnam veteran and decorated agent.\n\n"
            "Witnessed and documented drug-laden flights departing from Ilopango Air Base "
            "in El Salvador — the same base used by Felix Rodriguez and Oliver North's "
            "Contra resupply operation. In 'Powderburns: Cocaine, Contras & the Drug War' "
            "(1994), Castillo detailed:\n"
            "- Pilots on the Contra resupply flights were landing in South America, loading "
            "  cocaine, and flying it back through Ilopango to the United States.\n"
            "- Flight logs at the hangar were in the name of the NSC (Oliver North's office).\n"
            "- When Castillo reported the drug flights to his DEA superiors and the U.S. "
            "  Embassy, he was told to look the other way.\n"
            "- Ambassador Edwin Corr warned him to stop reporting.\n"
            "- At a 1986 reception in Guatemala, Castillo confronted Vice President George "
            "  H.W. Bush directly about the drug flights. Bush's response, according to "
            "  Castillo: 'That's one of those situations where you just have to go with it.'\n\n"
            "Testified before Congress (1996). Career effectively ended after whistleblowing. "
            "His account corroborates the Kerry Committee findings and Webb's reporting."
        ),
        "aliases": "Celerino Castillo III",
        "metadata": {},
    },
    {
        "name": "Bo Gritz",
        "entity_type": "person",
        "description": (
            "James Gordon 'Bo' Gritz. Born January 18, 1939. Retired U.S. Army Lieutenant "
            "Colonel, Special Forces. Most decorated Green Beret of the Vietnam War. Led "
            "private POW rescue missions to Laos in the 1980s.\n\n"
            "In 1986-87, Gritz traveled to Burma's Golden Triangle to meet with Khun Sa, "
            "the world's largest opium producer. During videotaped meetings, Khun Sa named "
            "specific U.S. government officials — including Richard Armitage (then Assistant "
            "Secretary of Defense) — as being involved in facilitating the heroin trade.\n\n"
            "Gritz delivered Khun Sa's video deposition and documentation to the DEA, "
            "multiple congressional offices, and the White House. No investigation was "
            "opened. Gritz publicly accused the government of protecting the heroin trade "
            "to fund covert operations.\n\n"
            "The Armitage allegations remain at the 'credible' tier — Khun Sa's claims are "
            "on video and consistent with McCoy's academic research, but no official "
            "investigation confirmed or refuted them. The pattern of non-investigation "
            "itself is documented."
        ),
        "aliases": "James Gordon Gritz",
        "metadata": {},
    },
    {
        "name": "Khun Sa",
        "entity_type": "person",
        "description": (
            "Chang Chi-fu, known as Khun Sa. Born February 17, 1934, Loi Maw, Shan State, "
            "Burma. Died October 26, 2007, Rangoon. Burmese warlord and the dominant figure "
            "in the Golden Triangle opium trade from the 1970s through the 1990s.\n\n"
            "Commanded the Mong Tai Army (MTA) — a Shan ethnic insurgent group that "
            "controlled up to 70% of the world's opium supply at its peak. The U.S. "
            "indicted him in 1989 on heroin trafficking charges.\n\n"
            "In 1986-87 meetings with Bo Gritz (videotaped), Khun Sa offered to:\n"
            "1. Name CIA and U.S. government officials who facilitated the heroin trade\n"
            "2. End all opium production in his territory in exchange for $20 million/year "
            "   in crop substitution aid\n\n"
            "Neither offer was accepted. No investigation was opened into his allegations. "
            "Khun Sa named Richard Armitage and others as CIA-connected facilitators. The "
            "DEA, which received the evidence, took no action.\n\n"
            "Surrendered to the Burmese military junta in 1996. Lived freely in Rangoon "
            "until his death — never extradited despite the U.S. indictment. His "
            "comfortable retirement suggested a deal was made."
        ),
        "aliases": "Chang Chi-fu",
        "metadata": {},
    },
    # --- ORGANIZATIONS ---
    {
        "name": "Air America",
        "entity_type": "organization",
        "description": (
            "CIA proprietary airline that operated in Southeast Asia from 1950 to 1976. "
            "Successor to Civil Air Transport (CAT), which was founded in 1946 by General "
            "Claire Chennault and purchased by the CIA in 1950.\n\n"
            "Primary mission: logistics support for CIA covert operations in Laos, Vietnam, "
            "Thailand, and across the region. The airline flew combat support, supplied "
            "irregular forces, conducted search and rescue, and moved personnel and materiel "
            "in support of the 'Secret War' in Laos (1955-1975).\n\n"
            "Drug facilitation: Alfred McCoy's seminal academic work 'The Politics of "
            "Heroin' (1972, revised 2003) documented that Air America aircraft transported "
            "opium for CIA-allied Hmong and Lao warlords, particularly General Vang Pao's "
            "forces. CIA's own declassified records confirm Air America was a CIA "
            "proprietary. The 1971 Senate staff report 'Opium and Politics in Laos' raised "
            "the issue in Congress.\n\n"
            "CIA's position: denied direct heroin trafficking while acknowledging the "
            "airline operated in opium-producing regions alongside drug-trafficking allies. "
            "McCoy's research showed CIA chose to accommodate the drug trade of its "
            "anti-communist allies rather than disrupt it.\n\n"
            "Dissolved 1976. Its operational model — CIA proprietary airline facilitating "
            "both covert ops and drug trafficking — was replicated by Southern Air Transport "
            "in the Iran-Contra era."
        ),
        "aliases": "CAT, Civil Air Transport",
        "metadata": {},
    },
    {
        "name": "Nugan Hand Bank",
        "entity_type": "organization",
        "description": (
            "Australian merchant bank (1973-1980) that served as a CIA financial front for "
            "laundering drug money and funding covert operations. Founded by Frank Nugan "
            "(Australian lawyer) and Michael Hand (U.S. Green Beret, CIA operative).\n\n"
            "CIA penetration of bank management:\n"
            "- President: Rear Admiral Earl Yates (USN, ret.) — former head of strategic "
            "  planning for the Pacific Command\n"
            "- Legal counsel: William Colby — former CIA Director (1973-76)\n"
            "- Hawaii branch: General Edwin Black — former commander of U.S. forces in "
            "  Thailand during Vietnam War\n"
            "- Washington representative: General Erle Cocke — former head of the American "
            "  Legion\n"
            "- Consultant: Walter McDonald — former CIA Deputy Director for Finance\n\n"
            "Operations: laundered heroin money from the Golden Triangle (McCoy documents "
            "the Chiang Mai branch specifically), moved money for CIA operations, offered "
            "tax evasion and currency manipulation services.\n\n"
            "Collapse: Frank Nugan found dead in his car on January 27, 1980 (rifle shot, "
            "ruled suicide). William Colby's business card was in his pocket. Michael Hand "
            "disappeared and was never seen again. The Australian Royal Commission (Stewart "
            "Commission, 1985) found the bank was 'a vehicle for CIA activities' but could "
            "not compel testimony from U.S. officials.\n\n"
            "Pattern match: Nugan Hand is the precursor to BCCI — a CIA-connected bank "
            "laundering drug money that collapsed under the weight of its own criminality."
        ),
        "aliases": "Nugan Hand Limited",
        "metadata": {},
    },
    {
        "name": "Cali Cartel",
        "entity_type": "organization",
        "description": (
            "Colombian drug trafficking organization based in Cali. Active 1975-1995. Led "
            "by the Rodriguez Orejuela brothers (Gilberto and Miguel) and Jose Santacruz "
            "Londono. Became the dominant cocaine supplier after the Medellin Cartel's "
            "collapse, controlling an estimated 80% of cocaine exports to the U.S. and 90% "
            "to Europe by the early 1990s.\n\n"
            "Intelligence connections: Unlike the violent Medellin Cartel, the Cali Cartel "
            "operated through bribery, political influence, and institutional penetration. "
            "The cartel infiltrated the Colombian government at the highest levels — the "
            "'Proceso 8000' scandal revealed that President Ernesto Samper's 1994 campaign "
            "received $6 million from the Cali Cartel.\n\n"
            "CIA relationship: The CIA worked with Colombian National Police (under General "
            "Rosso Jose Serrano) to dismantle the Cali Cartel in 1995-96, but reports "
            "indicate CIA maintained informants within the cartel throughout its existence. "
            "Los Pepes — the vigilante group that helped destroy the Medellin Cartel — "
            "included Cali Cartel members working alongside CIA-supported Colombian forces.\n\n"
            "Senate Permanent Subcommittee on Investigations documented the cartel's impact "
            "in a 1994 report. The Rodriguez Orejuela brothers surrendered in 1995-96 and "
            "received reduced sentences."
        ),
        "metadata": {},
    },
    {
        "name": "Los Zetas",
        "entity_type": "organization",
        "description": (
            "Mexican criminal organization, originally the paramilitary enforcement arm of "
            "the Gulf Cartel, later became an independent cartel (2010). Founded in 1999 "
            "by approximately 30 deserters from the Mexican Army's GAFE (Grupo "
            "Aeromovil de Fuerzas Especiales) — elite commandos.\n\n"
            "The U.S. training pipeline: GAFE soldiers who became Los Zetas founders had "
            "been trained by U.S. military at Fort Bragg, North Carolina, and at the School "
            "of the Americas at Fort Benning, Georgia. They received training in counter-"
            "insurgency, rapid deployment, intelligence gathering, and marksmanship — skills "
            "they applied directly to cartel operations.\n\n"
            "Founding members: Arturo Guzman Decena ('Z-1,' killed 2002), Heriberto Lazcano "
            "('Z-3,' killed 2012), and Miguel Angel Trevino Morales ('Z-40,' captured 2013). "
            "At peak strength, Los Zetas were considered the most powerful and violent cartel "
            "in Mexico.\n\n"
            "Pattern: identical to School of the Americas graduates in Latin America — U.S. "
            "trains foreign military forces in counterinsurgency, those forces apply the "
            "training to drug trafficking, political repression, or both. The training-to-"
            "cartel pipeline is documented by Grayson (2014) and multiple journalists."
        ),
        "metadata": {},
    },
    {
        "name": "DEA",
        "entity_type": "agency",
        "description": (
            "Drug Enforcement Administration. Established July 1, 1973 by President Nixon "
            "under Reorganization Plan No. 2 of 1973. Consolidated Bureau of Narcotics and "
            "Dangerous Drugs, Office for Drug Abuse Law Enforcement, and other agencies.\n\n"
            "Central tension: DEA agents in the field repeatedly ran into CIA protection of "
            "drug traffickers who served intelligence objectives. This institutional "
            "conflict is documented by multiple DEA whistleblowers:\n"
            "- Michael Levine: 25-year agent, documented CIA sabotage of Operation Hun and "
            "  other investigations targeting CIA-protected traffickers\n"
            "- Cele Castillo: documented drug flights from Ilopango, reports to superiors "
            "  ignored\n"
            "- Enrique 'Kiki' Camarena: DEA agent murdered in Mexico (1985) while "
            "  investigating cartel-government links; CIA accused of knowledge of his "
            "  abduction\n\n"
            "DEA also facilitated the Dark Alliance cover-up: Blandon — who admitted under "
            "oath to selling cocaine to fund the Contras — was given immunity, became a "
            "paid DEA informant ($45,000/year), and testified as government witness against "
            "Freeway Rick Ross.\n\n"
            "Khun Sa offered to name CIA officials to DEA in 1987; DEA took no action. "
            "The pattern: individual DEA agents investigated honestly, but the institution "
            "deferred to CIA at the policy level."
        ),
        "aliases": "Drug Enforcement Administration",
        "metadata": {},
    },
    # --- EVENTS / PROGRAMS ---
    {
        "name": "Dark Alliance",
        "entity_type": "publication",
        "description": (
            "Three-part investigative series by Gary Webb, published August 18-20, 1996 in "
            "the San Jose Mercury News. One of the first major investigative series "
            "published simultaneously on the web, reaching millions directly.\n\n"
            "Core claims:\n"
            "1. Nicaraguan Contra-linked drug dealers (Oscar Danilo Blandon, Norwin Meneses) "
            "   funneled cocaine profits to CIA-backed Contras\n"
            "2. Their cocaine supplied Freeway Rick Ross, fueling the LA crack epidemic\n"
            "3. CIA was aware of and facilitated these drug connections\n\n"
            "Media response: Washington Post, New York Times, and Los Angeles Times each "
            "assigned teams to attack the series. Mercury News editor Jerry Ceppos published "
            "a partial retraction. Webb was reassigned to a bureau 150 miles from home. He "
            "resigned.\n\n"
            "CIA response: FOIA documents obtained by The Intercept (2014) revealed CIA "
            "internal memo titled 'Managing a Nightmare,' showing CIA actively tracked and "
            "facilitated media destruction of Webb. CIA PR staff cultivated 'ichannels' "
            "with journalists at the Post, Times, and other outlets.\n\n"
            "Vindication: 1998 CIA Inspector General Frederick Hitz released two volumes "
            "confirming CIA 'failed to fully investigate or act upon allegations that the "
            "anti-Sandinista forces it supported were engaged in drug trafficking.' Volume "
            "II specifically named Blandon and Meneses.\n\n"
            "Expanded into book 'Dark Alliance: The CIA, the Contras, and the Crack Cocaine "
            "Explosion' (Seven Stories Press, 1998). Webb died December 10, 2004. Two "
            "gunshot wounds to the head. Ruled suicide."
        ),
        "aliases": "Dark Alliance series",
        "metadata": {},
    },
    {
        "name": "Operation Fast and Furious",
        "entity_type": "program",
        "description": (
            "ATF (Bureau of Alcohol, Tobacco, Firearms and Explosives) operation run from "
            "the Phoenix Field Division, 2009-2011. Part of the broader 'Project Gunrunner' "
            "initiative. ATF deliberately allowed 2,000+ firearms to be purchased by straw "
            "buyers and 'walked' across the border to Mexican cartels, supposedly to track "
            "them to cartel leadership.\n\n"
            "Results: weapons were lost track of almost immediately. At least 150 Mexican "
            "civilians and 1 U.S. Border Patrol agent (Brian Terry, killed December 14, "
            "2010) were killed with Fast and Furious weapons. Weapons from the program were "
            "found at crime scenes in Mexico for years afterward.\n\n"
            "Cover-up: DOJ initially denied the program existed. Attorney General Eric "
            "Holder refused to produce documents; held in contempt of Congress on June 28, "
            "2012 — the first sitting Attorney General to receive a contempt citation. "
            "President Obama asserted executive privilege over the documents.\n\n"
            "DOJ Inspector General report (September 2012, 471 pages) documented systemic "
            "failures and found 14 DOJ/ATF employees bore responsibility. No senior "
            "officials were criminally charged.\n\n"
            "Pattern: government agencies facilitating weapons flows to cartels, then "
            "obstructing investigation — echoing the Iran-Contra weapons pipeline."
        ),
        "metadata": {},
    },
    {
        "name": "Golden Triangle Drug Trade",
        "entity_type": "program",
        "description": (
            "The opium and heroin production zone spanning the mountainous borderlands of "
            "Burma (Myanmar), Thailand, and Laos. Produced the majority of the world's "
            "illicit opium from the 1950s through the 1990s.\n\n"
            "CIA involvement documented by Alfred McCoy (Yale University Press): during the "
            "Cold War, CIA allied with opium-producing warlords to fight communist "
            "insurgencies. Air America transported opium for CIA-allied commanders, "
            "particularly Hmong General Vang Pao in Laos. CIA facilitated the "
            "infrastructure — airstrips, transportation, protection — that enabled the "
            "trade to industrialize.\n\n"
            "Key figures:\n"
            "- Vang Pao: CIA's principal Hmong asset, whose troops grew opium and used Air "
            "  America to transport it\n"
            "- Khun Sa: dominated the trade from the 1970s-90s, offered to name CIA "
            "  officials to DEA\n"
            "- Li Mi: KMT general, CIA-supported, ran opium operations in Burma in the 1950s\n\n"
            "The 1971 Senate staff report 'Opium and Politics in Laos' raised the issue in "
            "Congress but produced no policy change. McCoy's book was subjected to CIA "
            "suppression attempts before publication.\n\n"
            "The Golden Triangle model — CIA allies with drug-producing forces, provides "
            "logistical support, looks the other way on trafficking — was replicated in "
            "Latin America (Contras, Noriega) and Afghanistan (mujahideen)."
        ),
        "metadata": {},
    },
    {
        "name": "Mena Airport Operations",
        "entity_type": "event",
        "description": (
            "Alleged CIA covert operations and drug trafficking centered at Mena "
            "Intermountain Municipal Airport in Mena, Arkansas during the 1980s.\n\n"
            "Documented elements:\n"
            "- Barry Seal based his drug smuggling and DEA/CIA informant operations at Mena "
            "  from 1982 until his assassination in 1986\n"
            "- Seal used Mena for aircraft maintenance and modifications through Rich "
            "  Mountain Aviation, run by Freddie Hampton\n"
            "- IRS investigator William Duncan testified to Congress (1994) that his "
            "  investigation into millions of dollars laundered through Mena-area banks was "
            "  obstructed by DOJ and Arkansas state officials\n"
            "- State police investigator Russell Welch investigated drug activity at the "
            "  airport for years; his files were confiscated\n\n"
            "Contested elements (inference tier):\n"
            "- Whether CIA ran operations directly from Mena beyond Seal's activities\n"
            "- The extent of Governor Bill Clinton's knowledge or involvement\n"
            "- Whether Mena served as a nexus for Iran-Contra resupply and drug return "
            "  flights\n\n"
            "Multiple independent witnesses (Duncan, Welch, journalist Ambrose Evans-"
            "Pritchard) corroborate unusual activity and institutional obstruction. No "
            "single declassified document confirms a CIA operational presence at Mena "
            "beyond Seal's activities, placing the broader claims at inference tier."
        ),
        "metadata": {},
    },
    {
        "name": "Mena Airport",
        "entity_type": "facility",
        "description": (
            "Mena Intermountain Municipal Airport (FAA: MEZ). Located in Mena, Polk County, "
            "Arkansas. Small regional airport that became central to the Iran-Contra drug "
            "trafficking narrative.\n\n"
            "Barry Seal — CIA drug pilot and DEA informant — based his operations at Mena "
            "from approximately 1982 until his assassination in February 1986. Seal used "
            "the airport for aircraft maintenance, modifications, and as a base for his "
            "cocaine smuggling flights from Central and South America.\n\n"
            "Key features: Rich Mountain Aviation (aircraft maintenance), remote location "
            "ideal for covert operations, proximity to Nella (unincorporated community "
            "where Seal maintained a base). IRS investigator William Duncan documented "
            "suspicious financial flows through local banks.\n\n"
            "The airport's role extends beyond Seal: multiple witnesses reported unusual "
            "late-night flights, military-style operations, and institutional obstruction "
            "of investigations. Arkansas state police investigator Russell Welch spent "
            "years investigating but his investigation was shut down.\n\n"
            "Became politically significant due to its location in Arkansas during Bill "
            "Clinton's governorship (1979-81, 1983-92). The question of what Clinton knew "
            "about Mena operations remains contested."
        ),
        "aliases": "Mena Intermountain Municipal Airport, MEZ",
        "metadata": {},
    },
    # --- Additional entities to flesh out network ---
    {
        "name": "Oscar Danilo Blandon",
        "entity_type": "person",
        "description": (
            "Nicaraguan exile and cocaine trafficker. Key link in the CIA-Contra-crack "
            "pipeline documented in Gary Webb's 'Dark Alliance' and confirmed by the CIA "
            "Inspector General's 1998 report.\n\n"
            "Blandon was the primary cocaine supplier to Freeway Rick Ross in Los Angeles. "
            "His own supplier was Norwin Meneses, head of Nicaraguan drug operations. "
            "Blandon admitted under oath at Ross's 1996 trial that he had sold cocaine to "
            "raise money for the CIA-backed Contras.\n\n"
            "Despite admitting to importing tons of cocaine into the United States, Blandon "
            "received extraordinary leniency: granted immunity from prosecution, became a "
            "paid DEA informant ($45,000/year), and testified as a government witness "
            "against his former client Rick Ross. His cocaine proceeds went to the Contras; "
            "his testimony put Ross away for life (later reduced).\n\n"
            "CIA IG Volume II (1998) confirmed Blandon and Meneses were Contra fundraisers "
            "who simultaneously trafficked cocaine. The IG found CIA 'failed to investigate' "
            "these connections."
        ),
        "aliases": "Danilo Blandon",
        "metadata": {},
    },
    {
        "name": "Norwin Meneses",
        "entity_type": "person",
        "description": (
            "Nicaraguan drug lord known as 'Rey de la Droga' (King of Drugs) in Nicaragua. "
            "Head of a cocaine trafficking network that operated from Central America to "
            "California. Identified by the CIA Inspector General as a Contra fundraiser.\n\n"
            "Meneses supplied cocaine to Oscar Danilo Blandon, who in turn supplied Freeway "
            "Rick Ross in Los Angeles. This pipeline — Meneses → Blandon → Ross → LA crack "
            "market — was the core of Webb's 'Dark Alliance' reporting.\n\n"
            "Despite being identified by DEA as a major trafficker as early as 1978, "
            "Meneses operated freely in the San Francisco Bay Area throughout the 1980s. "
            "Multiple DEA and FBI investigations into Meneses were closed without "
            "prosecution during the Contra war period.\n\n"
            "CIA IG Volume II confirmed Meneses's Contra connections. He was eventually "
            "arrested in Nicaragua in 1991, convicted and sentenced to 30 years, but "
            "released in 1996 after serving only 5 years."
        ),
        "aliases": "Rey de la Droga",
        "metadata": {},
    },
    {
        "name": "ATF",
        "entity_type": "agency",
        "description": (
            "Bureau of Alcohol, Tobacco, Firearms and Explosives. Federal law enforcement "
            "agency within the Department of Justice (transferred from Treasury in 2003).\n\n"
            "Central to the Operation Fast and Furious scandal: ATF's Phoenix Field Division "
            "deliberately allowed 2,000+ firearms to be purchased by straw buyers and walked "
            "to Mexican cartels between 2009-2011. The operation resulted in the death of "
            "Border Patrol Agent Brian Terry and at least 150 Mexican civilians.\n\n"
            "ATF agents who objected internally — particularly John Dodson — were retaliated "
            "against. Dodson ultimately became a whistleblower, testifying before Congress "
            "and triggering the DOJ Inspector General investigation.\n\n"
            "The DOJ IG report (2012) found systemic failures and identified 14 ATF/DOJ "
            "employees who bore responsibility. No senior officials were criminally charged."
        ),
        "aliases": "Bureau of Alcohol, Tobacco, Firearms and Explosives",
        "metadata": {},
    },
    {
        "name": "Enrique Camarena",
        "entity_type": "person",
        "description": (
            "Enrique 'Kiki' Camarena Salazar. DEA special agent. Born July 26, 1947, "
            "Mexicali, Mexico. Kidnapped, tortured, and murdered in Guadalajara, Mexico on "
            "February 7, 1985.\n\n"
            "Camarena had been investigating the Guadalajara Cartel, particularly Rafael "
            "Caro Quintero and Miguel Angel Felix Gallardo. His investigation led to the "
            "discovery and destruction of the Rancho Bufalo marijuana plantation — 2,500 "
            "acres, worth an estimated $8 billion.\n\n"
            "After his kidnapping, DEA's investigation uncovered disturbing connections:\n"
            "- Mexican DFS (Direccion Federal de Seguridad) agents — trained and supported "
            "  by CIA — participated in the kidnapping and cover-up\n"
            "- DFS was simultaneously protecting drug traffickers and serving as a CIA "
            "  liaison for intelligence on Central America\n"
            "- Former DEA agent Hector Berrellez (Operation Leyenda) later alleged that a "
            "  CIA operative was present at Camarena's interrogation\n\n"
            "The Camarena case exemplified the DEA-CIA conflict: DEA agents investigating "
            "drug traffickers kept running into CIA assets and protected networks. DEA "
            "Administrator Jack Lawn publicly accused CIA of withholding information about "
            "the murder."
        ),
        "aliases": "Kiki Camarena",
        "metadata": {},
    },
]


# ============================================================
# RELATIONSHIPS — ~40 connections
# ============================================================

RELATIONSHIPS = [
    # =========================================
    # GROUP 1: GOLDEN TRIANGLE / AIR AMERICA (7)
    # =========================================
    {
        "source": "Air America",
        "target": "CIA",
        "type": "front_for",
        "tier": "documented",
        "desc": "CIA proprietary airline, 1950-1976. Declassified CIA records confirm ownership. Operated in Laos, Vietnam, Thailand. McCoy documented opium transport for CIA-allied warlords. CIA's own declassified history acknowledges Air America as a proprietary.",
        "sources": [1051, 1052, 1053],
        "year_start": 1950,
        "year_end": 1976,
    },
    {
        "source": "Air America",
        "target": "Golden Triangle Drug Trade",
        "type": "facilitated",
        "tier": "documented",
        "desc": "Air America aircraft transported opium for CIA-allied commanders in Laos and Burma. McCoy documents the Hmong opium-to-heroin pipeline. 1971 Senate staff report raised the issue in Congress. CIA position: denied direct trafficking while acknowledging operations alongside drug-trafficking allies.",
        "sources": [1051, 1054],
        "year_start": 1960,
        "year_end": 1975,
    },
    {
        "source": "Khun Sa",
        "target": "Golden Triangle Drug Trade",
        "type": "operated",
        "tier": "documented",
        "desc": "Dominated Golden Triangle opium trade from the 1970s through 1990s, controlling up to 70% of world opium supply through the Mong Tai Army. Indicted by U.S. in 1989 but never extradited.",
        "sources": [1064, 1066],
        "year_start": 1970,
        "year_end": 1996,
    },
    {
        "source": "Khun Sa",
        "target": "CIA",
        "type": "accused",
        "tier": "credible",
        "desc": "In videotaped 1986-87 meetings with Bo Gritz, Khun Sa named specific CIA-connected U.S. officials facilitating the heroin trade and offered to end opium production for $20M/year crop substitution. Neither offer accepted. Video delivered to DEA and Congress — no investigation opened.",
        "sources": [1064, 1065],
        "year_start": 1986,
    },
    {
        "source": "Bo Gritz",
        "target": "Khun Sa",
        "type": "interviewed",
        "tier": "documented",
        "desc": "Retired Lt. Col. and most decorated Green Beret of Vietnam War traveled to Burma's Golden Triangle in 1986-87 to meet Khun Sa. Videotaped Khun Sa's allegations naming U.S. officials in heroin trade. Delivered evidence to DEA and Congress.",
        "sources": [1064, 1065],
        "year_start": 1986,
        "year_end": 1987,
    },
    {
        "source": "Golden Triangle Drug Trade",
        "target": "CIA",
        "type": "facilitated_by",
        "tier": "documented",
        "desc": "McCoy's academic research (Yale UP) documents CIA alliance with opium-producing warlords throughout the Cold War in Southeast Asia. CIA provided infrastructure — airstrips, transportation, protection — that industrialized the trade. 1971 Senate report raised the issue. CIA attempted to suppress McCoy's book before publication.",
        "sources": [1051, 1054, 1079],
        "year_start": 1950,
        "year_end": 1975,
    },
    {
        "source": "Air America",
        "target": "Southern Air Transport",
        "type": "preceded",
        "tier": "credible",
        "desc": "Air America (1950-76) and Southern Air Transport (1960-98) were both CIA proprietary airlines. Air America ran the Golden Triangle logistics; SAT ran Iran-Contra logistics. Same institutional model — CIA front airline facilitating both covert ops and drug trafficking — replicated across decades.",
        "sources": [1051, 1079],
    },

    # =========================================
    # GROUP 2: NUGAN HAND BANK (5)
    # =========================================
    {
        "source": "Nugan Hand Bank",
        "target": "CIA",
        "type": "front_for",
        "tier": "documented",
        "desc": "Australian Royal Commission (1985) found bank was 'a vehicle for CIA activities.' Co-founder Michael Hand was a CIA operative. Bank management staffed with retired U.S. military/intelligence: legal counsel was former CIA Director William Colby, president was Rear Admiral Yates, consultant was former CIA Deputy Director for Finance Walter McDonald.",
        "sources": [1055, 1056],
        "year_start": 1973,
        "year_end": 1980,
    },
    {
        "source": "Nugan Hand Bank",
        "target": "Golden Triangle Drug Trade",
        "type": "laundered_for",
        "tier": "documented",
        "desc": "Laundered heroin money from the Golden Triangle. McCoy documents the Chiang Mai branch specifically as a drug money laundering point. Kwitny's investigation traces the money flows from Southeast Asian heroin through Nugan Hand to covert operations.",
        "sources": [1055, 1056, 1051],
        "year_start": 1976,
        "year_end": 1980,
    },
    {
        "source": "Nugan Hand Bank",
        "target": "BCCI",
        "type": "preceded",
        "tier": "inference",
        "desc": "Same structural pattern: CIA-connected bank laundering drug money that collapsed under criminal weight. Nugan Hand (1973-80) preceded BCCI's exposure (1991). Both had senior intelligence/military figures in management. Both laundered narcotics proceeds. Both collapsed when criminality became undeniable.",
        "sources": [1055, 1056],
    },
    {
        "source": "Nugan Hand Bank",
        "target": "Air America",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Financial and logistical overlap in Southeast Asia. Nugan Hand's Chiang Mai branch laundered Golden Triangle heroin money; Air America provided the transportation infrastructure. Both were CIA-connected operations serving the same theater and timeline.",
        "sources": [1055, 1051],
        "year_start": 1976,
    },

    # =========================================
    # GROUP 3: DARK ALLIANCE / CRACK PIPELINE (8)
    # =========================================
    {
        "source": "Dark Alliance",
        "target": "Gary Webb",
        "type": "authored_by",
        "tier": "documented",
        "desc": "Three-part series published August 18-20, 1996 in the San Jose Mercury News. Expanded into book (1998, Seven Stories Press). Documented CIA-Contra-crack cocaine pipeline through Blandon and Meneses to Freeway Rick Ross.",
        "sources": [1058, 1078],
        "year_start": 1996,
    },
    {
        "source": "Dark Alliance",
        "target": "CIA",
        "type": "investigated",
        "tier": "documented",
        "desc": "Documented CIA's role in the Contra cocaine pipeline. CIA responded with internal memo 'Managing a Nightmare' (FOIA-obtained 2014) — actively facilitated media destruction of Webb. 1998 CIA IG confirmed core claims: CIA 'failed to investigate' Contra drug trafficking.",
        "sources": [1057, 1058, 1078],
        "year_start": 1996,
    },
    {
        "source": "Freeway Rick Ross",
        "target": "Oscar Danilo Blandon",
        "type": "supplied_by",
        "tier": "documented",
        "desc": "Blandon was Ross's primary cocaine supplier throughout the 1980s. Blandon admitted under oath at Ross's 1996 trial to selling cocaine to fund the CIA-backed Contras. Despite admitting to importing tons of cocaine, Blandon received immunity and became a paid DEA informant.",
        "sources": [1057, 1058, 1059],
        "year_start": 1982,
        "year_end": 1989,
    },
    {
        "source": "Oscar Danilo Blandon",
        "target": "Norwin Meneses",
        "type": "supplied_by",
        "tier": "documented",
        "desc": "Meneses was Blandon's cocaine supplier. CIA IG Volume II confirmed both were Contra fundraisers who simultaneously trafficked cocaine. Pipeline: Meneses → Blandon → Ross → LA crack market.",
        "sources": [1057, 1058],
        "year_start": 1981,
    },
    {
        "source": "Norwin Meneses",
        "target": "CIA",
        "type": "associated_with",
        "tier": "documented",
        "desc": "CIA IG Volume II identified Meneses as a Contra fundraiser. Despite being identified by DEA as a major trafficker since 1978, Meneses operated freely in San Francisco throughout the 1980s. Multiple DEA/FBI investigations closed without prosecution during the Contra war period.",
        "sources": [1057, 1058],
        "year_start": 1978,
    },
    {
        "source": "Oscar Danilo Blandon",
        "target": "Iran-Contra",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Blandon admitted under oath that cocaine proceeds went to fund the CIA-backed Contras. CIA IG confirmed he was a Contra fundraiser. His drug trafficking was part of the broader Contra funding network documented by the Kerry Committee.",
        "sources": [1057, 1059, 1077],
        "year_start": 1981,
        "year_end": 1986,
    },
    {
        "source": "Oscar Danilo Blandon",
        "target": "DEA",
        "type": "informant_for",
        "tier": "documented",
        "desc": "Despite admitting to importing tons of cocaine, Blandon was granted immunity, became a paid DEA informant ($45,000/year), and testified as government witness against his former client Rick Ross. The man who supplied crack to LA became a government asset.",
        "sources": [1057, 1059],
    },
    {
        "source": "Freeway Rick Ross",
        "target": "Iran-Contra",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Unwitting end-user of the Contra cocaine pipeline. Ross distributed $600M worth of crack in LA; his supplier Blandon was funding the Contras. Ross was not aware of the CIA/Contra connection — he was the distribution mechanism, not a knowing participant.",
        "sources": [1057, 1058, 1059],
        "year_start": 1982,
        "year_end": 1989,
    },

    # =========================================
    # GROUP 4: DEA WHISTLEBLOWERS (7)
    # =========================================
    {
        "source": "Michael Levine",
        "target": "DEA",
        "type": "member_of",
        "tier": "documented",
        "desc": "25-year DEA special agent (1965-1990), most decorated agent in DEA history. Ran major undercover operations including Operation Hun targeting Bolivia's cocaine junta. Turned whistleblower after documenting repeated CIA sabotage of DEA investigations.",
        "sources": [1060, 1061],
        "year_start": 1965,
        "year_end": 1990,
    },
    {
        "source": "Michael Levine",
        "target": "CIA",
        "type": "accused",
        "tier": "credible",
        "desc": "Documented CIA sabotage of Operation Hun (1980) — his infiltration of the Bolivian government's cocaine operation. CIA protected the Bolivian junta's intelligence chief (CIA payroll). Testified to Congress and media that CIA obstruction of DEA drug investigations was systematic, not aberrational.",
        "sources": [1060, 1061],
        "year_start": 1980,
    },
    {
        "source": "Cele Castillo",
        "target": "DEA",
        "type": "member_of",
        "tier": "documented",
        "desc": "DEA special agent stationed in Guatemala and El Salvador during Iran-Contra era (1985-1990). Vietnam veteran. Documented drug-laden flights from Ilopango Air Base. Testified before Congress (1996). Career ended after whistleblowing.",
        "sources": [1062, 1063],
        "year_start": 1985,
        "year_end": 1990,
    },
    {
        "source": "Cele Castillo",
        "target": "CIA",
        "type": "accused",
        "tier": "credible",
        "desc": "Documented drug flights from Ilopango Air Base where Felix Rodriguez ran Contra resupply. Flight logs in the name of NSC (Oliver North's office). Reports to DEA superiors and U.S. Embassy ignored. Ambassador warned him to stop reporting. Confronted VP Bush directly about drug flights at 1986 Guatemala reception.",
        "sources": [1062, 1063],
        "year_start": 1985,
    },
    {
        "source": "Cele Castillo",
        "target": "George H.W. Bush",
        "type": "confronted",
        "tier": "credible",
        "desc": "At a 1986 reception in Guatemala, Castillo confronted VP Bush directly about the drug flights from Ilopango. Bush's response according to Castillo: 'That's one of those situations where you just have to go with it.' Castillo documented this in 'Powderburns' (1994) and congressional testimony.",
        "sources": [1062, 1063],
        "year_start": 1986,
    },
    {
        "source": "Enrique Camarena",
        "target": "DEA",
        "type": "member_of",
        "tier": "documented",
        "desc": "DEA special agent investigating the Guadalajara Cartel in Mexico. Led to discovery of 2,500-acre Rancho Bufalo marijuana plantation ($8B estimated value). Kidnapped, tortured, and murdered February 7, 1985. DEA Administrator Jack Lawn publicly accused CIA of withholding information.",
        "sources": [1080],
        "year_start": 1980,
        "year_end": 1985,
    },
    {
        "source": "Enrique Camarena",
        "target": "CIA",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Mexican DFS agents — trained and supported by CIA as intelligence liaison — participated in Camarena's kidnapping and cover-up. DFS simultaneously protected drug traffickers and served CIA. Former DEA agent Hector Berrellez later alleged a CIA operative was present at Camarena's interrogation.",
        "sources": [1079, 1080],
        "year_start": 1985,
    },

    # =========================================
    # GROUP 5: MENA AIRPORT (4)
    # =========================================
    {
        "source": "Barry Seal",
        "target": "Mena Airport",
        "type": "operated_from",
        "tier": "documented",
        "desc": "Based drug smuggling and DEA/CIA informant operations at Mena from approximately 1982 until his assassination in February 1986. Used Rich Mountain Aviation for aircraft maintenance and modifications.",
        "sources": [1067, 1068],
        "year_start": 1982,
        "year_end": 1986,
    },
    {
        "source": "Mena Airport Operations",
        "target": "Mena Airport",
        "type": "located_at",
        "tier": "documented",
        "desc": "Operations centered at Mena Intermountain Municipal Airport in Polk County, Arkansas. IRS investigator Duncan testified to Congress about money laundering through local banks. State police investigator Welch's files confiscated.",
        "sources": [1067, 1068, 1069],
        "year_start": 1982,
        "year_end": 1986,
    },
    {
        "source": "Mena Airport Operations",
        "target": "CIA",
        "type": "associated_with",
        "tier": "inference",
        "desc": "Multiple independent witnesses (IRS investigator Duncan, state police investigator Welch, journalist Evans-Pritchard) corroborate unusual activity and institutional obstruction at Mena. Barry Seal's CIA/DEA connections documented. No single declassified document confirms broader CIA operational presence beyond Seal's activities.",
        "sources": [1067, 1068, 1069],
        "year_start": 1982,
    },
    {
        "source": "Mena Airport Operations",
        "target": "Bill Clinton",
        "type": "associated_with",
        "tier": "inference",
        "desc": "Operations occurred during Clinton's governorship of Arkansas (1979-81, 1983-92). IRS investigator Duncan testified that Arkansas state officials obstructed his money laundering investigation. Evans-Pritchard investigated the Clinton-Mena connection. The extent of Clinton's knowledge remains contested — no direct evidence of participation, but documented obstruction at state level.",
        "sources": [1068, 1069],
    },

    # =========================================
    # GROUP 6: CALI CARTEL / LOS ZETAS (4)
    # =========================================
    {
        "source": "Cali Cartel",
        "target": "CIA",
        "type": "associated_with",
        "tier": "credible",
        "desc": "CIA maintained informants within the cartel. Cali Cartel members participated in Los Pepes — the CIA-supported vigilante group that helped destroy the Medellin Cartel alongside Colombian military. CIA worked with Colombian police to dismantle Cali after Medellin fell.",
        "sources": [1070, 1071],
        "year_start": 1992,
        "year_end": 1996,
    },
    {
        "source": "Cali Cartel",
        "target": "Medellín Cartel",
        "type": "competed_with",
        "tier": "documented",
        "desc": "Rival Colombian cocaine organizations. Cali became dominant after Medellin's collapse (Escobar killed December 1993). Cali Cartel members joined Los Pepes to help destroy Medellin rival. Controlled 80% of U.S. cocaine supply and 90% of European supply by early 1990s.",
        "sources": [1070, 1071],
        "year_start": 1988,
        "year_end": 1995,
    },
    {
        "source": "Los Zetas",
        "target": "School of the Americas",
        "type": "trained_at",
        "tier": "documented",
        "desc": "Los Zetas founders were Mexican GAFE commandos trained at Fort Bragg and the School of the Americas. U.S.-provided counterinsurgency, rapid deployment, and intelligence training was applied directly to cartel operations. Pattern identical to SOA graduates in Latin America.",
        "sources": [1072, 1073],
        "year_start": 1994,
        "year_end": 1999,
    },
    {
        "source": "Los Zetas",
        "target": "DEA",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "DEA targeted Los Zetas as a primary threat after their split from the Gulf Cartel (2010). Irony: U.S. military trained the commandos, then U.S. law enforcement had to fight them. Multiple Z-leaders captured or killed through DEA intelligence operations.",
        "sources": [1072, 1073],
        "year_start": 2003,
    },

    # =========================================
    # GROUP 7: FAST AND FURIOUS (3)
    # =========================================
    {
        "source": "Operation Fast and Furious",
        "target": "ATF",
        "type": "operated_by",
        "tier": "documented",
        "desc": "ATF Phoenix Field Division ran Fast and Furious (2009-2011). 2,000+ firearms deliberately walked to Mexican cartels. DOJ IG report (471 pages, 2012) found 14 ATF/DOJ employees bore responsibility. No senior officials criminally charged.",
        "sources": [1074, 1075],
        "year_start": 2009,
        "year_end": 2011,
    },
    {
        "source": "Operation Fast and Furious",
        "target": "DOJ",
        "type": "covered_up_by",
        "tier": "documented",
        "desc": "DOJ initially denied the program existed. AG Eric Holder refused to produce documents — held in contempt of Congress June 28, 2012 (first sitting AG to receive contempt citation). President Obama asserted executive privilege over Fast and Furious documents.",
        "sources": [1074, 1076],
        "year_start": 2011,
        "year_end": 2012,
    },
    {
        "source": "Operation Fast and Furious",
        "target": "Los Zetas",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Fast and Furious weapons were walked to multiple Mexican cartels including the Sinaloa Cartel and Gulf Cartel/Los Zetas. Weapons from the program were found at crime scenes across Mexico for years. At least 150 Mexican civilians killed with walked weapons.",
        "sources": [1074, 1075],
        "year_start": 2009,
    },

    # =========================================
    # GROUP 8: CROSS-CONNECTIONS (4)
    # =========================================
    {
        "source": "DEA",
        "target": "CIA",
        "type": "obstructed_by",
        "tier": "credible",
        "desc": "Institutional conflict documented by multiple DEA whistleblowers (Levine, Castillo, Camarena case). CIA repeatedly protected drug traffickers who served intelligence objectives, sabotaging DEA investigations. Pattern spans decades: Golden Triangle, Bolivia, Central America, Mexico.",
        "sources": [1060, 1061, 1062, 1063, 1080],
        "year_start": 1973,
    },
    {
        "source": "Nugan Hand Bank",
        "target": "Iran-Contra",
        "type": "preceded",
        "tier": "inference",
        "desc": "Nugan Hand (1973-80) established the template that Iran-Contra replicated: CIA-connected financial institution laundering drug money to fund covert operations. Same actors (military/intelligence retirees), same methods (drug money laundering), same theater shift (Southeast Asia → Latin America).",
        "sources": [1055, 1056, 1079],
    },
    {
        "source": "Golden Triangle Drug Trade",
        "target": "Iran-Contra",
        "type": "preceded",
        "tier": "credible",
        "desc": "Peter Dale Scott documents the structural continuity: CIA facilitation of drug trafficking to fund covert operations in the Golden Triangle (1950s-70s) was replicated in Latin America (1980s). Same model — ally with drug-producing forces, provide logistics, look the other way — different theater.",
        "sources": [1051, 1079],
    },
    {
        "source": "Kerry Committee Investigation",
        "target": "Dark Alliance",
        "type": "preceded",
        "tier": "documented",
        "desc": "Kerry Committee (1989) documented Contra drug trafficking seven years before Webb's 'Dark Alliance' (1996). Webb's reporting built on Kerry's congressional findings but reached a mass audience via the web. Both were marginalized: Kerry's report was buried; Webb was destroyed. CIA IG (1998) confirmed both.",
        "sources": [1057, 1077, 1078],
    },
]


# ============================================================
# ENTITY-SOURCE LINKS — which sources document each entity
# ============================================================

ENTITY_SOURCES = {
    "Freeway Rick Ross": [1057, 1058, 1059],
    "Michael Levine": [1060, 1061],
    "Cele Castillo": [1062, 1063],
    "Bo Gritz": [1064, 1065],
    "Khun Sa": [1064, 1065, 1066],
    "Air America": [1051, 1052, 1053, 1054],
    "Nugan Hand Bank": [1055, 1056],
    "Cali Cartel": [1070, 1071],
    "Los Zetas": [1072, 1073],
    "DEA": [1060, 1061, 1062, 1063, 1080],
    "Dark Alliance": [1057, 1058, 1078],
    "Operation Fast and Furious": [1074, 1075, 1076],
    "Golden Triangle Drug Trade": [1051, 1054, 1066, 1079],
    "Mena Airport Operations": [1067, 1068, 1069],
    "Mena Airport": [1067, 1068, 1069],
    "Oscar Danilo Blandon": [1057, 1058, 1059],
    "Norwin Meneses": [1057, 1058],
    "ATF": [1074, 1075, 1076],
    "Enrique Camarena": [1079, 1080],
}
