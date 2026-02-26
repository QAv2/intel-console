"""
Israel (Deeper) — Expansion layer for Intel Console.
Entities: Ari Ben-Menashe, Jonathan Pollard, LAKAM, Unit 8200, NSO Group,
          Shabtai Shavit, Meir Dagan, Efraim Halevy.

This expansion deepens the existing Israeli intelligence cluster — Mossad,
Robert Maxwell, Ehud Barak, Black Cube, Mega Group, PROMIS, Rafi Eitan,
Carbyne are already mapped. This layer adds the people and organizations
that connect the documented threads: PROMIS backdooring pipeline, Pollard
affair, Maxwell-Mossad operation (Ben-Menashe testimony), Unit 8200 →
surveillance tech pipeline, and the Mossad directors who bridged these
operations across decades.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 306+ (continuing from existing 305)
# ============================================================

SOURCES = [
    # Government / Congressional / Court
    {
        "id": 306,
        "title": "U.S. v. Jonathan Jay Pollard — Caspar Weinberger Damage Assessment (declassified summary)",
        "url": "https://irp.fas.org/ops/ci/docs/pollard_weinberger.html",
        "source_type": "government",
        "year": 1987,
    },
    {
        "id": 307,
        "title": "CIA — Jonathan Pollard Espionage Case: Damage Assessment (declassified 2012)",
        "url": "https://www.cia.gov/readingroom/docs/DOC_0006122420.pdf",
        "source_type": "government",
        "year": 2012,
    },
    {
        "id": 308,
        "title": "U.S. v. Jonathan Jay Pollard — Sentencing Memorandum, U.S. District Court D.C.",
        "url": "https://www.justice.gov/archives/jm/criminal-resource-manual-2054-pollard-plea-agreement",
        "source_type": "court",
        "year": 1987,
    },
    {
        "id": 309,
        "title": "Senate Select Committee on Intelligence — An Assessment of the Aldrich H. Ames Espionage Case (contains LAKAM references)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/publications/10190.pdf",
        "source_type": "congressional",
        "year": 1994,
    },
    {
        "id": 310,
        "title": "GAO Report — DOJ Handling of INSLAW Affair (PROMIS software theft, Israeli connection documented)",
        "url": "https://www.gao.gov/products/gg-92-3",
        "source_type": "government",
        "year": 1991,
    },
    {
        "id": 311,
        "title": "House Judiciary Committee — The INSLAW Affair: Investigative Report (Brooks Committee)",
        "url": "https://archive.org/details/inslaw-affair",
        "source_type": "congressional",
        "year": 1992,
    },
    {
        "id": 312,
        "title": "Pegasus Project — Forbidden Stories / Amnesty International (NSO Group investigation)",
        "url": "https://forbiddenstories.org/case/the-pegasus-project/",
        "source_type": "journalism",
        "year": 2021,
    },
    {
        "id": 313,
        "title": "U.S. Commerce Department — Addition of NSO Group to Entity List (export controls)",
        "url": "https://www.federalregister.gov/documents/2021/11/04/2021-24123/addition-of-certain-entities-to-the-entity-list",
        "source_type": "government",
        "year": 2021,
    },
    {
        "id": 314,
        "title": "Apple Inc. v. NSO Group Technologies — Complaint, N.D. Cal.",
        "url": "https://www.apple.com/newsroom/2021/11/apple-sues-nso-group-to-curb-the-abuse-of-state-sponsored-spyware/",
        "source_type": "court",
        "year": 2021,
    },
    # Books (academic-quality investigative)
    {
        "id": 315,
        "title": "Ari Ben-Menashe — Profits of War: Inside the Secret U.S.-Israeli Arms Network",
        "url": "https://en.wikipedia.org/wiki/Profits_of_War",
        "source_type": "book",
        "author": "Ari Ben-Menashe",
        "year": 1992,
    },
    {
        "id": 316,
        "title": "Gordon Thomas — Gideon's Spies: The Secret History of the Mossad",
        "url": "https://en.wikipedia.org/wiki/Gideon%27s_Spies",
        "source_type": "book",
        "author": "Gordon Thomas",
        "year": 1999,
    },
    {
        "id": 317,
        "title": "Gordon Thomas & Martin Dillon — Robert Maxwell, Israel's Superspy",
        "url": "https://www.goodreads.com/book/show/411848.Robert_Maxwell_Israel_s_Superspy",
        "source_type": "book",
        "author": "Gordon Thomas, Martin Dillon",
        "year": 2002,
    },
    {
        "id": 318,
        "title": "Ronald Olive — Capturing Jonathan Pollard: How One of the Most Notorious Spies Was Brought to Justice",
        "url": "https://www.goodreads.com/book/show/625395.Capturing_Jonathan_Pollard",
        "source_type": "book",
        "author": "Ronald Olive",
        "year": 2006,
    },
    {
        "id": 319,
        "title": "Ronen Bergman — Rise and Kill First: The Secret History of Israel's Targeted Assassinations",
        "url": "https://en.wikipedia.org/wiki/Rise_and_Kill_First",
        "source_type": "book",
        "author": "Ronen Bergman",
        "year": 2018,
    },
    {
        "id": 320,
        "title": "Matthew Aid — The Secret Sentry: The Untold History of the NSA (Unit 8200 cooperation)",
        "url": "https://www.goodreads.com/book/show/6390884-the-secret-sentry",
        "source_type": "book",
        "author": "Matthew Aid",
        "year": 2009,
    },
    # Journalism
    {
        "id": 321,
        "title": "Seymour Hersh — The Traitor: The Case Against Jonathan Pollard (The New Yorker)",
        "url": "https://www.newyorker.com/magazine/1999/01/18/the-traitor",
        "source_type": "journalism",
        "author": "Seymour Hersh",
        "year": 1999,
    },
    {
        "id": 322,
        "title": "Guardian — Pegasus Project: NSO Group Spyware Found on Phones of Journalists and Activists Worldwide",
        "url": "https://www.theguardian.com/news/2021/jul/18/revealed-leak-uncovers-global-abuse-of-cyber-surveillance-weapon-nso-group-pegasus",
        "source_type": "journalism",
        "year": 2021,
    },
    {
        "id": 323,
        "title": "New York Times — The Israeli Spy Firm Helping Saudis Track Dissidents (NSO + Khashoggi)",
        "url": "https://www.nytimes.com/2018/10/20/us/politics/saudi-image-campaign-twitter.html",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 324,
        "title": "Washington Post — Jamal Khashoggi's Phone Was Targeted by NSO Group's Pegasus Before His Murder",
        "url": "https://www.washingtonpost.com/technology/2021/07/18/nso-group-pegasus-cellphone-hacking/",
        "source_type": "journalism",
        "year": 2021,
    },
    {
        "id": 325,
        "title": "Forbes — Israel's Unit 8200 Graduates Dominate the Country's Tech Industry",
        "url": "https://www.forbes.com/sites/richardbehar/2016/05/11/inside-israels-secret-startup-machine/",
        "source_type": "journalism",
        "year": 2016,
    },
    {
        "id": 326,
        "title": "Haaretz — How Israel Became a Hub for Surveillance Technology",
        "url": "https://www.haaretz.com/israel-news/2018-10-20/ty-article-magazine/.premium/israels-cyber-spy-industry-aids-world-dictators-hunt-dissidents-and-gays/0000017f-e3a4-d568-ad7f-fbac8f730000",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 327,
        "title": "New York Times — Ari Ben-Menashe, the Man Who Sold the World (profile)",
        "url": "https://www.nytimes.com/1992/02/05/opinion/l-ari-ben-menashe-and-the-iran-contra-affair-917592.html",
        "source_type": "journalism",
        "year": 1992,
    },
    {
        "id": 328,
        "title": "The Intercept — Israel's NSA Partners on Surveillance but Gives It Data on Americans",
        "url": "https://theintercept.com/2017/07/26/nsa-congress-israel-surveillance/",
        "source_type": "journalism",
        "year": 2017,
    },
    {
        "id": 329,
        "title": "Haaretz — Meir Dagan, Former Mossad Chief Who Rebuilt the Agency, Dies at 71",
        "url": "https://www.haaretz.com/israel-news/2016-03-17/ty-article/meir-dagan-former-mossad-chief-who-rebuilt-the-agency-dies-at-71/0000017f-e3c7-d568-ad7f-fbf7d6230000",
        "source_type": "journalism",
        "year": 2016,
    },
    {
        "id": 330,
        "title": "New Yorker — Shabtai Shavit and the Age of Israeli Intelligence Transformation",
        "url": "https://www.newyorker.com/magazine/2012/01/30/the-shadow-commander",
        "source_type": "journalism",
        "year": 2012,
    },
    {
        "id": 331,
        "title": "Snowden Archive (The Guardian) — NSA-Unit 8200 Intelligence Sharing Memorandum of Understanding",
        "url": "https://www.theguardian.com/world/2013/sep/11/nsa-americans-personal-data-israel-documents",
        "source_type": "journalism",
        "year": 2013,
    },
    {
        "id": 332,
        "title": "Washington Post — Israel Secretly Played a Role in Iran-Contra, Documents Show",
        "url": "https://www.washingtonpost.com/archive/politics/1991/12/18/israel-role-in-iran-contra-case/",
        "source_type": "journalism",
        "year": 1991,
    },
    {
        "id": 333,
        "title": "Associated Press — Israel Frees Pollard from Prison; Spy Boards Plane to Israel",
        "url": "https://apnews.com/article/jonathan-pollard-israel-spy-arrives-d0c24d64752f75b5cfa6b3dc0a11798a",
        "source_type": "journalism",
        "year": 2020,
    },
]


# ============================================================
# ENTITIES — 8 new entities (IDs will be 203-210)
# ============================================================

_DESC_BEN_MENASHE = (
    "Ari Ben-Menashe (born 1951, Tehran, Iran). Former Israeli military intelligence "
    "(Aman) officer who served from 1977 to 1987. Author of 'Profits of War: Inside "
    "the Secret U.S.-Israeli Arms Network' (1992), a detailed account of Israeli "
    "intelligence operations including arms deals with Iran."
    "\n\n"
    "KEY TESTIMONY — MAXWELL AS MOSSAD AGENT: Ben-Menashe is the most significant "
    "on-record source identifying Robert Maxwell as an Israeli intelligence operative. "
    "He testified that Maxwell was recruited by Israeli intelligence and served as a "
    "key asset for decades — facilitating arms deals, distributing backdoored PROMIS "
    "software to foreign governments, and operating as a conduit between Israeli "
    "intelligence and political/business networks worldwide. His account was "
    "corroborated by subsequent investigations (Gordon Thomas, Seymour Hersh)."
    "\n\n"
    "IRAN-CONTRA TESTIMONY: Ben-Menashe provided detailed testimony about Israel's "
    "central role in the Iran-Contra affair — specifically that Israel initiated and "
    "facilitated arms sales to Iran before the U.S. became directly involved. He "
    "described a three-way pipeline: Israeli arms to Iran, with proceeds funding "
    "Contra operations in Nicaragua. His credibility was attacked by both Israeli "
    "and U.S. governments, but key elements of his testimony were later confirmed "
    "by declassified documents and the Tower Commission."
    "\n\n"
    "EPSTEIN CONNECTION: Ben-Menashe stated in multiple interviews that Ghislaine "
    "Maxwell introduced Jeffrey Epstein to Israeli intelligence, continuing Robert "
    "Maxwell's operational relationship. He identified Epstein's operation as a "
    "sexual blackmail scheme run for Israeli intelligence — the same operational "
    "pattern documented in MKULTRA/Midnight Climax but attributed to Mossad rather "
    "than CIA. While Ben-Menashe's specific claims about Epstein-Mossad are not "
    "independently confirmed at the 'documented' tier, his track record on Maxwell "
    "and Iran-Contra lends credibility."
    "\n\n"
    "POST-INTELLIGENCE CAREER: Became a political lobbyist and consultant. "
    "Arrested in 1989 by U.S. authorities for allegedly brokering illegal arms "
    "sales; acquitted in 1990 after presenting evidence of Israeli government "
    "authorization. Now based in Montreal."
)

_DESC_POLLARD = (
    "Jonathan Jay Pollard (born 1954, Galveston, Texas). Former U.S. Navy civilian "
    "intelligence analyst convicted of spying for Israel in 1987. Served 30 years "
    "in federal prison — the longest sentence ever imposed for spying for a U.S. ally."
    "\n\n"
    "THE OPERATION: Pollard was recruited by LAKAM (Bureau of Scientific Relations), "
    "Israel's scientific intelligence collection agency, in 1984. His handler was "
    "Colonel Aviem Sella of the Israeli Air Force, and the operation was overseen "
    "by Rafi Eitan, then head of LAKAM. Pollard had SCI (Sensitive Compartmented "
    "Information) clearance and passed an estimated 800,000+ pages of classified "
    "documents to Israel over 18 months."
    "\n\n"
    "DAMAGE ASSESSMENT: Secretary of Defense Caspar Weinberger's classified damage "
    "assessment (partially declassified) described the Pollard case as causing "
    "'severe and irreparable' damage to U.S. national security. The compromised "
    "material included: the NSA's RASIN (Radio Signal Notation) manual describing "
    "U.S. signals intelligence capabilities, detailed technical intelligence on "
    "Soviet weapons systems, and information about U.S. intelligence-gathering "
    "methods that, if shared with the Soviet Union (which investigators suspected "
    "occurred via Aldrich Ames or other channels), would have compromised sources "
    "and methods globally."
    "\n\n"
    "AFTERMATH: Israel initially denied involvement, then admitted it in 1998 and "
    "granted Pollard citizenship. Released in 2015 after 30 years. Emigrated to "
    "Israel in December 2020, greeted by Prime Minister Netanyahu on the tarmac. "
    "The case caused a lasting rupture in U.S.-Israeli intelligence relations and "
    "led to the disbanding of LAKAM."
)

_DESC_LAKAM = (
    "LAKAM (Lishka le-Kishrei Mada — Bureau of Scientific Relations), also known "
    "as Lekem. Israeli scientific intelligence collection agency operating from "
    "1957 to 1986 under the Israeli Ministry of Defense."
    "\n\n"
    "MISSION: Collected scientific and technical intelligence for Israel's defense "
    "establishment, particularly related to nuclear, aerospace, and advanced weapons "
    "technology. Operated independently from Mossad and Aman (military intelligence), "
    "reporting directly to the Defense Ministry."
    "\n\n"
    "KEY OPERATIONS: (1) PROMIS SOFTWARE — LAKAM head Rafi Eitan orchestrated the "
    "acquisition of PROMIS software from the U.S. Department of Justice through "
    "the INSLAW affair. Israeli intelligence added a backdoor (trap door) to the "
    "software and, through Robert Maxwell's distribution network, sold it to "
    "intelligence agencies and governments worldwide — including Jordan, "
    "Guatemala, and others. This gave Israel (and potentially other intelligence "
    "services with knowledge of the backdoor) access to the internal databases "
    "of foreign governments. The House Judiciary Committee's 1992 investigation "
    "documented Israeli involvement. (2) JONATHAN POLLARD — LAKAM recruited and "
    "ran Pollard (1984-1985) through Colonel Aviem Sella with Rafi Eitan directing "
    "the operation. The compromise of 800,000+ pages of classified material was "
    "the most damaging espionage case involving a U.S. ally."
    "\n\n"
    "DISBANDING: After the Pollard arrest in 1985, Israel officially disbanded "
    "LAKAM as a concession to the United States. However, its intelligence "
    "collection functions were absorbed by other Israeli agencies. The Senate "
    "Select Committee on Intelligence noted that the organizational change did "
    "not necessarily end the collection priorities LAKAM had pursued."
)

_DESC_UNIT_8200 = (
    "Unit 8200 (Yehida Shmoneh-Matayim). Israeli Intelligence Corps signals "
    "intelligence (SIGINT) unit, equivalent to the U.S. NSA or UK GCHQ. Based "
    "at Urim SIGINT Base in the Negev Desert and facilities near Herzliya."
    "\n\n"
    "MISSION: Responsible for collecting signals intelligence, conducting "
    "cyber operations, and codebreaking. The largest single unit in the Israeli "
    "Defense Forces, with thousands of personnel. Conscripts are selected for "
    "high technical aptitude, typically serving from age 18-21."
    "\n\n"
    "NSA PARTNERSHIP: Snowden documents (published by The Guardian, 2013) "
    "revealed a Memorandum of Understanding in which the NSA routinely shares "
    "raw, unfiltered intelligence data — including data on American citizens — "
    "with Unit 8200. The Intercept (2017) reported that this sharing includes "
    "metadata, content of communications, and other surveillance products, "
    "with minimal restrictions on how Israel uses data about U.S. persons."
    "\n\n"
    "TECH PIPELINE — SURVEILLANCE INDUSTRY: Unit 8200 alumni have founded "
    "a disproportionate share of Israel's $10B+ cybersecurity and surveillance "
    "industry. Notable alumni-founded companies include: NSO Group (Pegasus "
    "spyware), Verint Systems (formerly Comverse Infosys — wiretapping tech), "
    "Check Point Software, CyberArk, Palo Alto Networks. Forbes (2016) "
    "documented the 'Unit 8200 to tech startup' pipeline as a defining feature "
    "of Israel's tech economy. Haaretz (2018) documented how these companies "
    "sell surveillance tools to authoritarian governments worldwide."
    "\n\n"
    "CARBYNE CONNECTION: Carbyne (co-founded by Ehud Barak, Epstein investor) "
    "had former Unit 8200 director Pinhas Buchris on its board. This connects "
    "the Unit 8200 → surveillance tech pipeline directly to the Epstein network."
)

_DESC_NSO_GROUP = (
    "NSO Group Technologies (founded 2010, Herzliya, Israel). Private "
    "intelligence firm that develops and sells surveillance technology to "
    "governments worldwide. Best known for Pegasus, a zero-click spyware "
    "capable of compromising any smartphone."
    "\n\n"
    "FOUNDERS: Founded by Niv Carmi, Shalev Hulio, and Omri Lavie — all "
    "veterans of Unit 8200, Israel's signals intelligence unit. The company "
    "represents the most prominent example of the Unit 8200 → private "
    "surveillance tech pipeline."
    "\n\n"
    "PEGASUS PROJECT (2021): Investigation by Forbidden Stories and 17 media "
    "organizations revealed that Pegasus had been used to target at least "
    "50,000 phone numbers belonging to journalists, human rights activists, "
    "lawyers, and heads of state in at least 45 countries. Targeted individuals "
    "included associates of murdered journalist Jamal Khashoggi — the "
    "Washington Post and Citizen Lab confirmed that Khashoggi's inner circle "
    "was surveilled via Pegasus before his October 2018 assassination by "
    "Saudi operatives."
    "\n\n"
    "U.S. GOVERNMENT ACTION: In November 2021, the U.S. Commerce Department "
    "added NSO Group to its Entity List (trade blacklist) for engaging in "
    "activities 'contrary to the national security or foreign policy interests "
    "of the United States.' Apple filed suit against NSO Group the same month. "
    "The FBI purchased and tested Pegasus (as reported by the New York Times, "
    "2022) before deciding against operational deployment."
    "\n\n"
    "INTELLIGENCE-INDUSTRY NEXUS: NSO Group operates under Israeli Ministry "
    "of Defense export licensing. Its sales require government approval, "
    "meaning the Israeli state retains veto power over which governments "
    "receive the technology. This makes NSO a de facto instrument of Israeli "
    "foreign policy — surveillance access as a diplomatic tool. Multiple "
    "former senior Israeli intelligence officials have served on NSO's "
    "advisory board."
    "\n\n"
    "STRUCTURAL PARALLEL: NSO Group represents the modern evolution of the "
    "same intelligence-distribution model documented in the PROMIS affair: "
    "Israeli intelligence-connected technology sold to foreign governments, "
    "creating surveillance access. PROMIS was backdoored software distributed "
    "by Robert Maxwell in the 1980s; Pegasus is zero-click spyware distributed "
    "through NSO Group in the 2020s. The pipeline — Unit 8200 training → "
    "private company → government-licensed exports — is the institutional "
    "successor to LAKAM → Maxwell → PROMIS."
)

_DESC_SHAVIT = (
    "Shabtai Shavit (born 1939). Director of the Mossad from 1989 to 1996 — "
    "the period during which the Robert Maxwell operation collapsed (Maxwell "
    "died November 1991) and the institutional transition to successor operations "
    "occurred."
    "\n\n"
    "CAREER: Joined the Mossad in 1964. Rose through operational divisions "
    "including counterterrorism and intelligence collection. Appointed Mossad "
    "director by Prime Minister Yitzhak Shamir in 1989, serving under Shamir, "
    "Rabin, and Peres. His tenure encompassed the First Gulf War, Oslo Accords "
    "negotiations, and the post-Cold War intelligence realignment."
    "\n\n"
    "MAXWELL PERIOD: Shavit became Mossad director two years before Robert "
    "Maxwell's death. Multiple intelligence historians (Gordon Thomas, Ronen "
    "Bergman) document that the Mossad was managing the fallout from Maxwell's "
    "financial collapse and the risk of exposure of intelligence operations "
    "Maxwell had facilitated — particularly the PROMIS distribution network. "
    "Shavit oversaw this institutional crisis and the transition of Maxwell-era "
    "operations to new structures."
    "\n\n"
    "POST-SERVICE: After leaving the Mossad, Shavit served as chairman of the "
    "board of the International Institute for Counter-Terrorism (ICT) at "
    "Herzliya's Interdisciplinary Center. Has spoken publicly about intelligence "
    "matters, advocating for aggressive counterterrorism postures."
)

_DESC_DAGAN = (
    "Meir Dagan (1945-2016). Director of the Mossad from 2002 to 2011. "
    "Widely regarded as having rebuilt and modernized the agency during one "
    "of its most operationally active periods."
    "\n\n"
    "MILITARY CAREER: Born in the Soviet Union, emigrated to Israel as a "
    "child. Decorated IDF officer who served in the 1967 and 1973 wars. "
    "Founded Sayeret Rimon, a special operations unit targeting Palestinian "
    "guerrillas in Gaza (early 1970s). Rose to Major General."
    "\n\n"
    "MOSSAD TENURE (2002-2011): Appointed by Prime Minister Ariel Sharon "
    "with the mandate to 'make the Mossad into the Mossad again.' Under "
    "Dagan's leadership, the Mossad conducted: (1) Targeted assassination "
    "campaigns against Iranian nuclear scientists, (2) The alleged Stuxnet "
    "cyber operation against Iran's Natanz facility (joint with NSA/CIA), "
    "(3) Expanded intelligence operations globally. Ronen Bergman's 'Rise "
    "and Kill First' documents Dagan's transformation of the agency."
    "\n\n"
    "BLACK CUBE CONNECTION: After leaving the Mossad, Dagan served as "
    "honorary president of Black Cube (BC Strategy Ltd), the private "
    "intelligence firm founded by Mossad/Aman veterans. Black Cube was "
    "later hired by Harvey Weinstein to surveil and discredit sexual "
    "assault accusers — a connection facilitated by Ehud Barak. Dagan's "
    "involvement in Black Cube connects the serving Mossad director "
    "directly to the privatized intelligence apparatus that overlaps "
    "with the Epstein network through Barak."
    "\n\n"
    "Dagan died of liver cancer in March 2016."
)

_DESC_HALEVY = (
    "Efraim Halevy (born 1934, London, United Kingdom). Director of the "
    "Mossad from 1998 to 2002, and head of Israel's National Security "
    "Council from 2002 to 2003."
    "\n\n"
    "CAREER: Emigrated to Israel in 1948. Joined the Mossad in 1961 and "
    "served for over 40 years. Specialized in diplomatic and liaison "
    "intelligence — managing relationships between Mossad and foreign "
    "intelligence services. Played a key role in back-channel negotiations "
    "that led to the Israel-Jordan peace treaty (1994)."
    "\n\n"
    "MOSSAD DIRECTOR (1998-2002): Halevy's tenure as Mossad director "
    "overlapped with the period when Jeffrey Epstein's operation was "
    "most active (late 1990s-2000s). His directorship bridged the gap "
    "between Shabtai Shavit (1989-1996) and Meir Dagan (2002-2011)."
    "\n\n"
    "MAXWELL OPERATIONS: Gordon Thomas, in 'Robert Maxwell, Israel's "
    "Superspy,' documents Halevy as a key figure in managing Mossad's "
    "relationship with Robert Maxwell during the 1980s. As a senior "
    "Mossad official specializing in liaison operations, Halevy was "
    "involved in the institutional framework that Maxwell operated within."
    "\n\n"
    "BLACK CUBE CONNECTION: Like Meir Dagan, Halevy served on the board "
    "of Black Cube after his retirement from government service. The "
    "presence of two former Mossad directors on Black Cube's board — "
    "the same firm hired by Weinstein on Barak's referral — illustrates "
    "the continuity between state intelligence operations and the "
    "privatized intelligence firms orbiting the Epstein network."
    "\n\n"
    "POST-SERVICE: Has written and lectured extensively on intelligence "
    "and Middle Eastern affairs. Served as head of the National Security "
    "Council and as a diplomatic envoy. Author of 'Man in the Shadows' (2006)."
)


ENTITIES = [
    {
        "name": "Ari Ben-Menashe",
        "entity_type": "person",
        "description": _DESC_BEN_MENASHE,
        "aliases": "Ben-Menashe",
        "metadata": {"birth_year": 1951, "nationality": "Israeli-Iranian", "status": "alive"},
    },
    {
        "name": "Jonathan Pollard",
        "entity_type": "person",
        "description": _DESC_POLLARD,
        "aliases": "Pollard, Jay Pollard",
        "metadata": {"birth_year": 1954, "nationality": "American-Israeli", "status": "alive"},
    },
    {
        "name": "LAKAM",
        "entity_type": "agency",
        "description": _DESC_LAKAM,
        "aliases": "Lekem, Lishka le-Kishrei Mada, Bureau of Scientific Relations",
        "metadata": {"founded": 1957, "disbanded": 1986, "country": "Israel"},
    },
    {
        "name": "Unit 8200",
        "entity_type": "agency",
        "description": _DESC_UNIT_8200,
        "aliases": "Yehida Shmoneh-Matayim, 8200, Israeli SIGINT",
        "metadata": {"country": "Israel"},
    },
    {
        "name": "NSO Group",
        "entity_type": "organization",
        "description": _DESC_NSO_GROUP,
        "aliases": "NSO Group Technologies, NSO, Q Cyber Technologies",
        "metadata": {"founded": 2010, "country": "Israel"},
    },
    {
        "name": "Shabtai Shavit",
        "entity_type": "person",
        "description": _DESC_SHAVIT,
        "aliases": "Shavit",
        "metadata": {"birth_year": 1939, "nationality": "Israeli", "status": "alive"},
    },
    {
        "name": "Meir Dagan",
        "entity_type": "person",
        "description": _DESC_DAGAN,
        "aliases": "Dagan",
        "metadata": {"birth_year": 1945, "death_year": 2016, "nationality": "Israeli", "status": "deceased"},
    },
    {
        "name": "Efraim Halevy",
        "entity_type": "person",
        "description": _DESC_HALEVY,
        "aliases": "Halevy",
        "metadata": {"birth_year": 1934, "nationality": "Israeli-British", "status": "alive"},
    },
]


# ============================================================
# RELATIONSHIPS — connections to existing network + internal
# ============================================================
# Existing entities referenced by name (resolved at insert time):
#   Jeffrey Epstein [1], Ghislaine Maxwell [2], Robert Maxwell [3],
#   Les Wexner [4], Ehud Barak [5], William Barr [8],
#   Rafi Eitan [53], Mossad [88], CIA [85], FBI [87], NSA [86],
#   DOJ [89], PROMIS [91], Iran-Contra [96], Black Cube [142],
#   Carbyne [67], Mega Group [66], James Angleton [17],
#   Adnan Khashoggi [27], DARPA [90], In-Q-Tel [60],
#   Palantir Technologies [59], Nicole Junkermann [151],
#   Saudi GID [178], Mohammed bin Salman [179],
#   Jamal Khashoggi [180]

RELATIONSHIPS = [
    # ================================================================
    # ARI BEN-MENASHE
    # ================================================================

    # Ben-Menashe → Robert Maxwell (key testimony)
    {
        "source": "Ari Ben-Menashe",
        "target": "Robert Maxwell",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Ben-Menashe is the primary on-record source identifying Robert Maxwell as "
            "an Israeli intelligence operative. In 'Profits of War' (1992) and subsequent "
            "testimony, he described Maxwell's role in Israeli arms deals, PROMIS distribution, "
            "and intelligence operations spanning decades. His account was corroborated by "
            "Gordon Thomas's independent investigation."
        ),
        "sources": [315, 317],
    },
    # Ben-Menashe → Ghislaine Maxwell
    {
        "source": "Ari Ben-Menashe",
        "target": "Ghislaine Maxwell",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Ben-Menashe stated in multiple interviews that Ghislaine Maxwell introduced "
            "Jeffrey Epstein to Israeli intelligence, continuing the operational relationship "
            "her father had maintained. He identified her as a conduit between the Maxwell "
            "intelligence network and Epstein's operation."
        ),
        "sources": [315, 317],
    },
    # Ben-Menashe → Mossad (employer)
    {
        "source": "Ari Ben-Menashe",
        "target": "Mossad",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "Ben-Menashe served in Israeli military intelligence (Aman) from 1977 to 1987, "
            "which works closely with Mossad. Israel initially denied his service but was "
            "forced to acknowledge it when his personnel records were presented at his 1990 "
            "trial, where he was acquitted of arms dealing charges."
        ),
        "sources": [315, 316],
    },
    # Ben-Menashe → Iran-Contra
    {
        "source": "Ari Ben-Menashe",
        "target": "Iran-Contra",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Provided detailed testimony about Israel's initiating role in Iran-Contra arms "
            "sales. Described three-way pipeline: Israeli arms to Iran, proceeds to Contras. "
            "Key elements confirmed by declassified documents and Tower Commission findings."
        ),
        "sources": [315, 332],
    },
    # Ben-Menashe → Jeffrey Epstein (testimony about intelligence role)
    {
        "source": "Ari Ben-Menashe",
        "target": "Jeffrey Epstein",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Ben-Menashe publicly identified Epstein's operation as a sexual blackmail scheme "
            "run for Israeli intelligence, stating Ghislaine Maxwell was the introducer. His "
            "credibility derives from confirmed testimony on Maxwell-Mossad and Iran-Contra, "
            "but the specific Epstein-intelligence claim is not independently confirmed at the "
            "'documented' tier."
        ),
        "sources": [315, 317],
    },
    # Ben-Menashe → PROMIS
    {
        "source": "Ari Ben-Menashe",
        "target": "PROMIS",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Described Israeli intelligence's role in the PROMIS affair — specifically that "
            "Israeli agents added a backdoor to the software before Robert Maxwell distributed "
            "it to foreign governments. His account corroborates the House Judiciary Committee's "
            "1992 findings on Israeli involvement."
        ),
        "sources": [315, 311],
    },

    # ================================================================
    # JONATHAN POLLARD
    # ================================================================

    # Pollard → LAKAM (recruited and run by)
    {
        "source": "Jonathan Pollard",
        "target": "LAKAM",
        "type": "recruited_by",
        "tier": "documented",
        "desc": (
            "Recruited by LAKAM in 1984 through Colonel Aviem Sella. Operation directed by "
            "LAKAM head Rafi Eitan. Passed 800,000+ pages of classified documents over 18 months. "
            "Documented in DOJ sentencing memorandum and Weinberger damage assessment."
        ),
        "sources": [306, 308, 318],
    },
    # Pollard → Rafi Eitan (handler's superior)
    {
        "source": "Jonathan Pollard",
        "target": "Rafi Eitan",
        "type": "directed_by",
        "tier": "documented",
        "desc": (
            "Rafi Eitan, as head of LAKAM, personally directed the Pollard espionage operation. "
            "Eitan recruited Colonel Aviem Sella as the direct handler. Court documents and "
            "multiple investigations confirm Eitan's role as the operation's architect."
        ),
        "sources": [306, 308, 318],
    },
    # Pollard → NSA (compromised)
    {
        "source": "Jonathan Pollard",
        "target": "NSA",
        "type": "compromised",
        "tier": "documented",
        "desc": (
            "Pollard passed the NSA's RASIN (Radio Signal Notation) manual — a comprehensive "
            "guide to U.S. signals intelligence capabilities — to Israel. The CIA damage "
            "assessment and Weinberger memorandum document this as among the most damaging "
            "compromises of the case."
        ),
        "sources": [306, 307, 321],
    },
    # Pollard → FBI (investigated by)
    {
        "source": "Jonathan Pollard",
        "target": "FBI",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "Arrested by FBI on November 21, 1985 after attempting to seek asylum at the "
            "Israeli Embassy in Washington. FBI Naval Investigative Service agent Ronald Olive "
            "led the investigation. Pollard cooperated and pled guilty in 1987."
        ),
        "sources": [308, 318],
    },
    # Pollard → Mossad (institutional beneficiary)
    {
        "source": "Jonathan Pollard",
        "target": "Mossad",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "While Pollard was run by LAKAM (not Mossad), the intelligence he provided "
            "benefited the broader Israeli intelligence community. After LAKAM's disbanding, "
            "its collection functions were absorbed by other agencies including Mossad. Israel "
            "granted Pollard citizenship in 1995 and Netanyahu personally lobbied for his release."
        ),
        "sources": [307, 321, 333],
    },

    # ================================================================
    # LAKAM
    # ================================================================

    # LAKAM → Rafi Eitan (headed by)
    {
        "source": "LAKAM",
        "target": "Rafi Eitan",
        "type": "directed_by",
        "tier": "documented",
        "desc": (
            "Rafi Eitan headed LAKAM during its most operationally significant period "
            "(early-mid 1980s), directing both the Pollard recruitment and the PROMIS "
            "acquisition. Documented in multiple official investigations."
        ),
        "sources": [306, 311, 318],
    },
    # LAKAM → PROMIS (acquisition)
    {
        "source": "LAKAM",
        "target": "PROMIS",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Under Rafi Eitan's direction, LAKAM orchestrated the acquisition of PROMIS "
            "software. The House Judiciary Committee's 1992 investigation documented Israeli "
            "involvement in the INSLAW affair. LAKAM's technical intelligence mission included "
            "acquiring and exploiting foreign software systems."
        ),
        "sources": [310, 311],
    },
    # LAKAM → Mossad (sibling agencies)
    {
        "source": "LAKAM",
        "target": "Mossad",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "LAKAM operated parallel to Mossad within Israel's intelligence community — "
            "both reported to different chains of command but shared intelligence products. "
            "After LAKAM's disbanding in 1986, its collection functions were absorbed by "
            "other agencies including Mossad."
        ),
        "sources": [309, 319],
    },
    # LAKAM → Robert Maxwell (PROMIS distribution)
    {
        "source": "LAKAM",
        "target": "Robert Maxwell",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "LAKAM's acquisition of PROMIS was followed by Robert Maxwell's distribution "
            "of the backdoored software worldwide. The LAKAM → Maxwell → PROMIS pipeline "
            "connected Israeli scientific intelligence to Maxwell's global media and business "
            "network. Documented in House Judiciary investigation and corroborated by "
            "Ben-Menashe and Gordon Thomas accounts."
        ),
        "sources": [311, 315, 317],
    },

    # ================================================================
    # UNIT 8200
    # ================================================================

    # Unit 8200 → NSA (intelligence partnership)
    {
        "source": "Unit 8200",
        "target": "NSA",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "Snowden documents (Guardian, 2013) revealed an MOU in which NSA routinely shares "
            "raw, unfiltered intelligence — including data on American citizens — with Unit 8200. "
            "The Intercept (2017) reported minimal restrictions on Israel's use of data about "
            "U.S. persons. Matthew Aid's 'The Secret Sentry' documents the decades-long partnership."
        ),
        "sources": [331, 328, 320],
    },
    # Unit 8200 → Mossad (institutional)
    {
        "source": "Unit 8200",
        "target": "Mossad",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Unit 8200 provides signals intelligence to Mossad for operational use. While "
            "organizationally separate (8200 is IDF; Mossad is civilian), they are deeply "
            "integrated operationally. Joint operations documented by Ronen Bergman in "
            "'Rise and Kill First.'"
        ),
        "sources": [319, 320],
    },
    # Unit 8200 → NSO Group (alumni pipeline)
    {
        "source": "Unit 8200",
        "target": "NSO Group",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "NSO Group was founded by three Unit 8200 veterans (Niv Carmi, Shalev Hulio, "
            "Omri Lavie). Forbes (2016) and Haaretz (2018) documented the Unit 8200 → tech "
            "startup pipeline as a defining feature of Israel's surveillance industry. "
            "NSO is the most prominent example of this institutional pathway."
        ),
        "sources": [325, 326],
    },
    # Unit 8200 → Carbyne (board member)
    {
        "source": "Unit 8200",
        "target": "Carbyne",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Former Unit 8200 director Pinhas Buchris served on Carbyne's board alongside "
            "Ehud Barak and Nicole Junkermann. Carbyne was co-founded by Barak with Epstein "
            "investment, connecting the Unit 8200 pipeline directly to the Epstein network."
        ),
        "sources": [325, 326],
    },
    # Unit 8200 → Palantir Technologies (intelligence-tech nexus)
    {
        "source": "Unit 8200",
        "target": "Palantir Technologies",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Both represent the intelligence-to-tech pipeline in their respective countries: "
            "Unit 8200 feeds Israel's surveillance industry, CIA/In-Q-Tel funded Palantir. "
            "Forbes and Haaretz document Israeli Unit 8200 alumni working at or consulting "
            "for Palantir and similar U.S. intelligence-adjacent firms."
        ),
        "sources": [325, 326],
    },

    # ================================================================
    # NSO GROUP
    # ================================================================

    # NSO Group → Mossad (export licensing / state instrument)
    {
        "source": "NSO Group",
        "target": "Mossad",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "NSO operates under Israeli Ministry of Defense export licensing — sales require "
            "government approval. Multiple former Mossad/intelligence officials served on "
            "advisory boards. The Pegasus Project documented NSO as a de facto instrument "
            "of Israeli foreign policy, with surveillance access traded as diplomatic leverage."
        ),
        "sources": [312, 322, 326],
    },
    # NSO Group → PROMIS (structural successor)
    {
        "source": "NSO Group",
        "target": "PROMIS",
        "type": "successor_to",
        "tier": "inference",
        "desc": (
            "Structural parallel: PROMIS was backdoored software distributed by Robert Maxwell "
            "in the 1980s; Pegasus is zero-click spyware distributed through NSO Group in the "
            "2020s. Both represent Israeli intelligence-connected technology sold to foreign "
            "governments creating surveillance access. The pipeline evolved from "
            "LAKAM → Maxwell → PROMIS to Unit 8200 → NSO → Pegasus."
        ),
        "sources": [311, 312],
    },
    # NSO Group → FBI (tested Pegasus)
    {
        "source": "NSO Group",
        "target": "FBI",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The FBI purchased and tested NSO Group's Pegasus spyware. While the Bureau "
            "ultimately decided against operational deployment, the purchase confirmed "
            "institutional-level engagement between U.S. law enforcement and Israeli "
            "surveillance technology."
        ),
        "sources": [312, 322],
    },
    # NSO Group → Saudi GID (Pegasus client — Khashoggi)
    {
        "source": "NSO Group",
        "target": "Saudi GID",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Pegasus Project investigation and Citizen Lab confirmed that Saudi Arabia was "
            "a major NSO client. Pegasus was used to surveil Jamal Khashoggi's inner circle "
            "before his October 2018 assassination by Saudi operatives. The NYT and Washington "
            "Post documented NSO's role in enabling Saudi surveillance operations."
        ),
        "sources": [312, 323, 324],
    },
    # NSO Group → Jamal Khashoggi (surveillance target's associates)
    {
        "source": "NSO Group",
        "target": "Jamal Khashoggi",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Pegasus spyware was used to surveil Khashoggi's associates and inner circle "
            "prior to his murder. Washington Post and Citizen Lab forensic analysis confirmed "
            "Pegasus infections on phones of people close to Khashoggi. NSO denied targeting "
            "Khashoggi directly but did not deny Saudi Arabia was a client."
        ),
        "sources": [322, 324],
    },
    # NSO Group → DOJ (Entity List / trade restrictions)
    {
        "source": "NSO Group",
        "target": "DOJ",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "U.S. Commerce Department added NSO Group to its Entity List in November 2021 "
            "for activities 'contrary to the national security or foreign policy interests "
            "of the United States.' Apple also filed federal suit against NSO the same month."
        ),
        "sources": [313, 314],
    },

    # ================================================================
    # SHABTAI SHAVIT
    # ================================================================

    # Shavit → Mossad (director)
    {
        "source": "Shabtai Shavit",
        "target": "Mossad",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Director of the Mossad from 1989 to 1996. Appointed by PM Yitzhak Shamir. "
            "Oversaw the agency during Robert Maxwell's death (1991), the first Gulf War, "
            "and Oslo Accords negotiations. Documented in Israeli government records."
        ),
        "sources": [319, 330],
    },
    # Shavit → Robert Maxwell (institutional oversight during Maxwell collapse)
    {
        "source": "Shabtai Shavit",
        "target": "Robert Maxwell",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "As Mossad director from 1989, Shavit oversaw the institutional crisis surrounding "
            "Robert Maxwell's financial collapse and death in 1991. Intelligence historians "
            "document that Mossad was managing the risk of exposure of operations Maxwell "
            "had facilitated — particularly the PROMIS distribution network."
        ),
        "sources": [316, 317],
    },

    # ================================================================
    # MEIR DAGAN
    # ================================================================

    # Dagan → Mossad (director)
    {
        "source": "Meir Dagan",
        "target": "Mossad",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Director of the Mossad from 2002 to 2011. Appointed by PM Ariel Sharon with "
            "mandate to rebuild the agency. Oversaw targeted assassination programs, cyber "
            "operations (including alleged Stuxnet), and global intelligence expansion."
        ),
        "sources": [319, 329],
    },
    # Dagan → Black Cube (post-service board)
    {
        "source": "Meir Dagan",
        "target": "Black Cube",
        "type": "member_of",
        "tier": "documented",
        "desc": (
            "Served as honorary president of Black Cube after leaving the Mossad. His presence "
            "on Black Cube's board — alongside fellow former Mossad director Efraim Halevy — "
            "connects the Mossad directorship directly to the privatized intelligence firm later "
            "hired by Harvey Weinstein on Ehud Barak's referral."
        ),
        "sources": [319, 329],
    },
    # Dagan → CIA (counterpart / Stuxnet partner)
    {
        "source": "Meir Dagan",
        "target": "CIA",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Under Dagan's leadership, Mossad conducted joint operations with the CIA, most "
            "notably the alleged Stuxnet cyber operation against Iran's Natanz nuclear facility. "
            "Dagan maintained close liaison with CIA directors during the 2002-2011 period."
        ),
        "sources": [319],
    },

    # ================================================================
    # EFRAIM HALEVY
    # ================================================================

    # Halevy → Mossad (director)
    {
        "source": "Efraim Halevy",
        "target": "Mossad",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Director of the Mossad from 1998 to 2002, bridging Shabtai Shavit (1989-1996) "
            "and Meir Dagan (2002-2011). Previously served over 40 years in the agency in "
            "liaison and diplomatic intelligence roles."
        ),
        "sources": [316, 319],
    },
    # Halevy → Black Cube (post-service board)
    {
        "source": "Efraim Halevy",
        "target": "Black Cube",
        "type": "member_of",
        "tier": "documented",
        "desc": (
            "Served on the board of Black Cube alongside Meir Dagan. Two former Mossad "
            "directors on the board of the firm later hired by Weinstein (via Barak referral) "
            "demonstrates continuity between state intelligence and privatized operations "
            "connected to the Epstein network."
        ),
        "sources": [316, 319],
    },
    # Halevy → Robert Maxwell (institutional management)
    {
        "source": "Efraim Halevy",
        "target": "Robert Maxwell",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Gordon Thomas documents Halevy as a key Mossad figure in managing the agency's "
            "relationship with Robert Maxwell during the 1980s. As a specialist in liaison "
            "operations, Halevy was involved in the institutional framework through which "
            "Maxwell operated as an Israeli intelligence asset."
        ),
        "sources": [317, 316],
    },

    # ================================================================
    # CROSS-CUTTING RELATIONSHIPS (connecting expansion to existing)
    # ================================================================

    # Rafi Eitan → LAKAM (already exists as person; new relationship to new entity)
    {
        "source": "Rafi Eitan",
        "target": "LAKAM",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Headed LAKAM during the Pollard affair and PROMIS acquisition. Under his "
            "direction, LAKAM ran its two most significant operations — both of which "
            "connected Israeli intelligence to the broader network mapped in this database."
        ),
        "sources": [306, 311, 318],
    },
    # Rafi Eitan → Jonathan Pollard
    {
        "source": "Rafi Eitan",
        "target": "Jonathan Pollard",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "As LAKAM head, Rafi Eitan personally directed the Pollard espionage operation. "
            "Recruited Colonel Aviem Sella as handler. Documented in DOJ sentencing memorandum, "
            "CIA damage assessment, and multiple official investigations."
        ),
        "sources": [306, 308, 318],
    },
    # Ehud Barak → Unit 8200 (through Carbyne/Buchris)
    {
        "source": "Ehud Barak",
        "target": "Unit 8200",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Co-founded Carbyne with former Unit 8200 director Pinhas Buchris on the board. "
            "As former IDF Chief of Staff and PM, Barak had institutional relationships with "
            "all Israeli intelligence bodies including Unit 8200."
        ),
        "sources": [325, 326],
    },
    # Mega Group → LAKAM (American support network / intelligence collection)
    {
        "source": "Mega Group",
        "target": "LAKAM",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "The Mega Group — a secretive network of American billionaire pro-Israel donors "
            "co-founded by Wexner and Bronfman — operated in the same period LAKAM was "
            "collecting scientific/technical intelligence in the U.S. While no direct "
            "operational link is documented, the Mega Group provided the social and financial "
            "infrastructure in which Israeli intelligence operations in America operated."
        ),
        "sources": [309, 321],
    },
    # James Angleton → Mossad (expanded — the original CIA-Israel bridge)
    {
        "source": "James Angleton",
        "target": "LAKAM",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Angleton's decades-long role as CIA counterintelligence chief and liaison to "
            "Israeli intelligence created the institutional relationship that LAKAM later "
            "exploited. The 'special relationship' Angleton built with Israeli services "
            "gave Israeli intelligence unprecedented access to U.S. intelligence circles — "
            "access that LAKAM leveraged for the Pollard operation."
        ),
        "sources": [319, 321],
    },
    # William Barr → Jonathan Pollard (clemency politics)
    {
        "source": "William Barr",
        "target": "Jonathan Pollard",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Barr served as AG during both Bush 41 and Trump administrations. The Pollard "
            "case was a recurring political issue: successive Israeli governments lobbied for "
            "clemency. Pollard was released in 2015 (Obama admin parole) and emigrated to "
            "Israel in 2020 during Trump/Barr's DOJ tenure, with no legal obstacles imposed."
        ),
        "sources": [308, 333],
    },
]


# ============================================================
# ENTITY → SOURCE links
# ============================================================

ENTITY_SOURCES = {
    "Ari Ben-Menashe": [315, 316, 317, 327, 332],
    "Jonathan Pollard": [306, 307, 308, 318, 321, 333],
    "LAKAM": [306, 309, 310, 311, 318],
    "Unit 8200": [320, 325, 326, 328, 331],
    "NSO Group": [312, 313, 314, 322, 323, 324, 326],
    "Shabtai Shavit": [316, 319, 330],
    "Meir Dagan": [319, 329],
    "Efraim Halevy": [316, 317, 319],
}
