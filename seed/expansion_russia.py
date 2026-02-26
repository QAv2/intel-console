"""
Russia / Putin Cluster — Expansion layer for Intel Console.
Entities: Vladimir Putin, FSB, Semion Mogilevich, Solntsevskaya Bratva, Dmitry Rybolovlev.

Bridge nodes connecting Intelligence & Organized Crime branches through the Russian pipeline —
the mirror image of the American CIA-Lansky-Cohn-Epstein synthesis already mapped.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 190+ (continuing from existing 189)
# ============================================================

SOURCES = [
    # Government / Congressional
    {
        "id": 190,
        "title": "Senate Select Committee on Intelligence — Report on Russian Active Measures (Vol. 5)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/documents/report_volume5.pdf",
        "source_type": "congressional",
        "year": 2020,
    },
    {
        "id": 191,
        "title": "Mueller Report — Report on the Investigation into Russian Interference in the 2016 Presidential Election",
        "url": "https://www.justice.gov/archives/sco/file/1373816/dl",
        "source_type": "government",
        "year": 2019,
    },
    {
        "id": 192,
        "title": "DOJ — United States v. Semion Mogilevich et al., Indictment (E.D. Pa.)",
        "url": "https://www.justice.gov/criminal/criminal-oia/selected-case-information-ymb-fraud-inc",
        "source_type": "court",
        "year": 2003,
    },
    {
        "id": 193,
        "title": "FBI — Semion Mogilevich, Ten Most Wanted Fugitives (removed 2015)",
        "url": "https://archives.fbi.gov/archives/news/stories/2009/october/mogilevich_102109",
        "source_type": "government",
        "year": 2009,
    },
    {
        "id": 194,
        "title": "UK Home Office — The Litvinenko Inquiry: Report (Sir Robert Owen)",
        "url": "https://www.gov.uk/government/publications/the-litvinenko-inquiry-report-into-the-death-of-alexander-litvinenko",
        "source_type": "government",
        "year": 2016,
    },
    {
        "id": 195,
        "title": "FinCEN Files — Leaked Suspicious Activity Reports (BuzzFeed News / ICIJ)",
        "url": "https://www.icij.org/investigations/fincen-files/",
        "source_type": "journalism",
        "year": 2020,
    },
    {
        "id": 196,
        "title": "Panama Papers — Offshore Accounts of Putin Associates (ICIJ)",
        "url": "https://www.icij.org/investigations/panama-papers/20160403-putin-russia-offshore-network/",
        "source_type": "journalism",
        "year": 2016,
    },
    # Books (academic-quality investigative)
    {
        "id": 197,
        "title": "Karen Dawisha — Putin's Kleptocracy: Who Owns Russia?",
        "url": "https://en.wikipedia.org/wiki/Putin%27s_Kleptocracy",
        "source_type": "book",
        "author": "Karen Dawisha",
        "year": 2014,
    },
    {
        "id": 198,
        "title": "Catherine Belton — Putin's People: How the KGB Took Back Russia and Then Took on the West",
        "url": "https://en.wikipedia.org/wiki/Putin%27s_People",
        "source_type": "book",
        "author": "Catherine Belton",
        "year": 2020,
    },
    # Journalism
    {
        "id": 199,
        "title": "Palm Beach Post — Russian Fertilizer King Pays Trump $95M for Palm Beach Mansion",
        "url": "https://www.palmbeachpost.com/story/news/local/2019/04/01/he-bought-trump-estate-for-95-million-then-he-began-tearing-it-down/5498498007/",
        "source_type": "journalism",
        "year": 2008,
    },
    {
        "id": 200,
        "title": "New York Times — Deutsche Bank Fined $630 Million Over Russia Mirror-Trading Scheme",
        "url": "https://www.nytimes.com/2017/01/31/business/dealbook/deutsche-bank-fine-russia.html",
        "source_type": "journalism",
        "year": 2017,
    },
    {
        "id": 201,
        "title": "Senate Judiciary Committee — Bayrock Group / Felix Sater Testimony & Documents",
        "url": "https://www.judiciary.senate.gov/imo/media/doc/Sater%20Testimony.pdf",
        "source_type": "congressional",
        "year": 2017,
    },
    {
        "id": 202,
        "title": "Reuters — FBI Tracked Alleged Russian Mob Boss Mogilevich for Decade",
        "url": "https://www.reuters.com/article/us-usa-russia-mogilevich/fbi-tracked-alleged-russian-mob-boss-for-decade-idUSBREA0P1B720140126/",
        "source_type": "journalism",
        "year": 2014,
    },
    {
        "id": 203,
        "title": "BBC — Putin's Early Career: From KGB to Kremlin",
        "url": "https://www.bbc.com/news/world-europe-15047823",
        "source_type": "journalism",
        "year": 2022,
    },
    {
        "id": 204,
        "title": "ABC News — Rybolovlev Yacht Spotted Near Epstein's Private Island",
        "url": "https://abcnews.go.com/Politics/fbi-obtained-high-res-photos-epstein-island-visitors/story?id=107867070",
        "source_type": "journalism",
        "year": 2024,
    },
    {
        "id": 205,
        "title": "New York Times — How a Russian Oligarch's $95 Million Mansion Purchase Raised Questions",
        "url": "https://www.nytimes.com/2019/03/10/us/politics/trump-rybolovlev.html",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 206,
        "title": "Guardian — Robert Maxwell Was a KGB Spy, Says Former Russian Intelligence Officer",
        "url": "https://www.theguardian.com/world/2003/nov/10/pressandpublishing.booksnews",
        "source_type": "journalism",
        "year": 2003,
    },
    {
        "id": 207,
        "title": "Organized Crime and Corruption Reporting Project (OCCRP) — Mogilevich Profile",
        "url": "https://www.occrp.org/en/investigations/the-curious-case-of-semion-mogilevich",
        "source_type": "journalism",
        "year": 2019,
    },
]


# ============================================================
# ENTITIES — 5 new entities
# ============================================================

_DESC_PUTIN = (
    "Vladimir Vladimirovich Putin (born 1952). President of the Russian Federation "
    "(2000-2008, 2012-present), Prime Minister (1999-2000, 2008-2012). Career intelligence "
    "officer in the KGB (1975-1991), stationed in Dresden, East Germany coordinating with "
    "the Stasi. Resigned from KGB with rank of Lieutenant Colonel."
    "\n\n"
    "POST-KGB CAREER: Deputy Mayor of St. Petersburg under Anatoly Sobchak (1991-1996). "
    "Multiple investigative accounts (Dawisha, Belton) document extensive ties to organized "
    "crime during this period — specifically the Tambov and Malyshev gangs controlling "
    "St. Petersburg's port and export licensing. Moved to Moscow 1996, rose through "
    "presidential administration. Appointed FSB Director (July 1998), Prime Minister "
    "(August 1999), Acting President (December 1999)."
    "\n\n"
    "INTELLIGENCE-CRIME NEXUS: Putin represents the institutional fusion of state intelligence "
    "and organized crime in post-Soviet Russia — the same pattern documented in the American "
    "context through CIA-Lansky-Cohn. Multiple documented connections to this network: "
    "Felix Sater (Russian-born FBI/GRU asset operating through Bayrock Group on Trump "
    "properties), Deutsche Bank (fined $630M for Russian mirror-trading scheme, same bank "
    "serving Epstein and Trump), and the broader oligarch financial architecture."
    "\n\n"
    "PERSONAL WEALTH: Estimated $40-200 billion held through oligarch cutouts. "
    "Panama Papers (2016) documented $2B in offshore accounts linked to cellist Sergei "
    "Roldugin, a childhood friend of Putin."
)

_DESC_FSB = (
    "Federal Security Service of the Russian Federation (Federalnaya Sluzhba Bezopasnosti). "
    "Domestic intelligence and security agency, primary successor to the KGB's Second Chief "
    "Directorate (counterintelligence) and Fifth Directorate (dissidents). Established 1995."
    "\n\n"
    "Putin served as FSB Director from July 1998 to August 1999, using the position as "
    "launchpad to the presidency. The Litvinenko Inquiry (2016, UK) documented FSB involvement "
    "in the 2006 polonium poisoning of Alexander Litvinenko, 'probably approved by Putin.' "
    "The 1999 Russian apartment bombings that precipitated the Second Chechen War and Putin's "
    "rise were attributed to Chechen terrorists by the government; Litvinenko and others "
    "alleged FSB involvement before being killed."
    "\n\n"
    "Institutional successor to the KGB in domestic operations. Maintains documented "
    "relationships with organized crime networks, particularly through the 'krysha' "
    "(protection) system documented by Dawisha and Belton."
)

_DESC_MOGILEVICH = (
    "Semion Yudkovich Mogilevich (born 1946, Kyiv, Ukrainian SSR). Known as the 'Boss of "
    "Bosses' of Russian organized crime. FBI Ten Most Wanted Fugitives list (2009-2015). "
    "Indicted by DOJ in 2003 on 45 counts of racketeering, fraud, and money laundering "
    "related to a $150M stock fraud scheme through YBM Magnex International."
    "\n\n"
    "OPERATIONS: Controls or influences the Solntsevskaya Bratva, the largest Russian "
    "organized crime group. Specializes in weapons trafficking, nuclear materials, drug "
    "trafficking, and large-scale money laundering. Interpol Red Notice issued. Despite "
    "brief arrest in Moscow (2008, released same year), has never been extradited."
    "\n\n"
    "NETWORK CONNECTIONS: FBI and DOJ documents identify Mogilevich as operating with "
    "de facto protection of Russian state security services. Connected to the broader "
    "network through: (1) Felix Sater — Bayrock Group linked to Russian organized crime "
    "money flows documented in Senate testimony, (2) Deutsche Bank — mirror-trading scheme "
    "moved $10B of Russian money, (3) Energy sector — natural gas intermediaries between "
    "Russia and Ukraine."
    "\n\n"
    "Represents the Russian equivalent of Meyer Lansky — the financial architect of "
    "organized crime operating at the intersection of state power and the criminal underworld."
)

_DESC_SOLNTSEVSKAYA = (
    "Solntsevskaya Bratva (Solntsevo Brotherhood). Moscow-based Russian organized crime "
    "syndicate, considered the largest and most powerful Russian mafia organization. "
    "Founded in the late 1980s in the Solntsevo District of Moscow."
    "\n\n"
    "Estimated 5,000-9,000 members worldwide. Operations span extortion, drug trafficking, "
    "arms dealing, human trafficking, and large-scale money laundering. Documented by FBI, "
    "Europol, and DOJ as Semion Mogilevich's organizational base, though the group operates "
    "through a decentralized cell structure."
    "\n\n"
    "The Solntsevskaya Bratva represents the post-Soviet evolution of organized crime — where "
    "American organized crime families (Gambino, Genovese, etc.) operated alongside but "
    "separate from intelligence agencies, the Russian model fused the two. Former KGB officers "
    "joined or directed criminal enterprises after 1991, creating an intelligence-crime hybrid "
    "that mirrors the CIA-Lansky pattern but with institutional integration rather than "
    "parallel operation."
)

_DESC_RYBOLOVLEV = (
    "Dmitry Evgenievich Rybolovlev (born 1966). Russian oligarch, potash fertilizer magnate, "
    "former owner of AS Monaco football club. Forbes-estimated net worth ~$6.8B."
    "\n\n"
    "TRUMP CONNECTION: In 2008, purchased Donald Trump's Palm Beach estate (Maison de "
    "l'Amitié) for $95 million — more than double what Trump paid ($41.35M in 2004) — "
    "during the financial crisis when real estate values were collapsing. The transaction "
    "raised questions about whether the premium represented a legitimate investment or "
    "something else. Rybolovlev never lived in the property and demolished the mansion."
    "\n\n"
    "PROXIMITY PATTERN: McClatchy and other outlets documented that Rybolovlev's private "
    "plane appeared at the same airports as Trump's during the 2016 campaign on multiple "
    "occasions — Charlotte, Las Vegas, and Concord, NH. Rybolovlev's spokesman called "
    "the overlaps coincidental."
    "\n\n"
    "ISLAND PROXIMITY: ABC News reported FBI obtained high-resolution photos of visitors "
    "to Epstein's island; Rybolovlev's yacht was spotted in the vicinity of Little Saint "
    "James, though direct visitation is not confirmed."
)


ENTITIES = [
    {
        "name": "Vladimir Putin",
        "entity_type": "person",
        "description": _DESC_PUTIN,
        "aliases": "Putin, VVP",
        "metadata": {"photo_url": "/static/photos/vladimir_putin.jpg"},
    },
    {
        "name": "FSB",
        "entity_type": "agency",
        "description": _DESC_FSB,
        "aliases": "Federal Security Service, Federalnaya Sluzhba Bezopasnosti",
        "metadata": {},
    },
    {
        "name": "Semion Mogilevich",
        "entity_type": "person",
        "description": _DESC_MOGILEVICH,
        "aliases": "Mogilevich, Don Semyon, The Brainy Don, Boss of Bosses",
        "metadata": {"photo_url": "/static/photos/semion_mogilevich.jpg"},
    },
    {
        "name": "Solntsevskaya Bratva",
        "entity_type": "organization",
        "description": _DESC_SOLNTSEVSKAYA,
        "aliases": "Solntsevo Brotherhood, Russian Mafia",
        "metadata": {},
    },
    {
        "name": "Dmitry Rybolovlev",
        "entity_type": "person",
        "description": _DESC_RYBOLOVLEV,
        "aliases": "Rybolovlev",
        "metadata": {"photo_url": "/static/photos/dmitry_rybolovlev.jpg"},
    },
]


# ============================================================
# RELATIONSHIPS — connections to existing network + internal
# ============================================================
# Reference existing entities by name (resolved at insert time):
#   Felix Sater [36], Donald Trump [33], Deutsche Bank [57],
#   Bayrock Group [73], Robert Maxwell [3], Mossad [88], CIA [85],
#   Meyer Lansky [18], FBI [87], KGB → new, FSB → new,
#   Little Saint James [76], Mar-a-Lago [75]

RELATIONSHIPS = [
    # ---- Putin internal connections ----
    {
        "source": "Vladimir Putin",
        "target": "FSB",
        "type": "directed",
        "tier": "documented",
        "desc": "Putin served as FSB Director (July 1998 - August 1999), using the position as launchpad to presidency. Documented in official Russian government records.",
        "sources": [203, 198],
    },

    # ---- Putin → existing network ----
    {
        "source": "Vladimir Putin",
        "target": "Donald Trump",
        "type": "financial_connection",
        "tier": "documented",
        "desc": "Trump Moscow project (2015-2016) documented in Mueller Report and Michael Cohen congressional testimony. Trump Organization pursued building a Trump Tower in Moscow with letters of intent signed while Trump was running for president.",
        "sources": [191, 190],
    },
    {
        "source": "Vladimir Putin",
        "target": "Deutsche Bank",
        "type": "financial_connection",
        "tier": "documented",
        "desc": "Deutsche Bank fined $630M (2017) for $10B Russian mirror-trading scheme that moved money out of Russia. FinCEN files document additional suspicious Russian transactions through DB. Same bank served Epstein and Trump.",
        "sources": [200, 195],
    },
    {
        "source": "Vladimir Putin",
        "target": "Robert Maxwell",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": "Robert Maxwell documented as KGB asset (codename reported in multiple accounts). Putin was KGB officer during Maxwell's active period. Institutional connection — Maxwell served the same intelligence apparatus Putin rose through. Former Russian intelligence officer confirmed Maxwell's KGB ties (Guardian, 2003).",
        "sources": [206, 198],
    },
    {
        "source": "Vladimir Putin",
        "target": "CIA",
        "type": "adversarial",
        "tier": "documented",
        "desc": "Institutional adversary. Putin was KGB counterintelligence in Dresden during Cold War. As president, expelled CIA officers, shuttered USAID/NGOs used as intelligence cover. Mueller Report documents Russian intelligence operations against U.S. elections.",
        "sources": [191, 194],
    },

    # ---- FSB connections ----
    {
        "source": "FSB",
        "target": "CIA",
        "type": "adversarial",
        "tier": "documented",
        "desc": "Institutional adversaries and occasional cooperators. FSB is successor to KGB's domestic counterintelligence directorate. Senate Intelligence Committee and Mueller Report document FSB cyber operations against U.S. targets.",
        "sources": [190, 191],
    },
    {
        "source": "FSB",
        "target": "Felix Sater",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": "Sater born in Moscow (1966), emigrated to U.S. as child. DOJ and Senate documents confirm Sater provided intelligence to FBI and CIA on Russian organized crime and terrorism. His Russian connections intersected both U.S. and Russian intelligence interests. Senate Judiciary testimony details Bayrock's Russian financial networks.",
        "sources": [201, 191],
    },
    {
        "source": "FSB",
        "target": "Mossad",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": "Documented intelligence liaison relationship. Israel-Russia intelligence cooperation increased significantly under Putin, particularly regarding counter-terrorism and Syria. Putin-Netanyahu met dozens of times (documented in diplomatic records).",
        "sources": [198],
    },

    # ---- Mogilevich connections ----
    {
        "source": "Semion Mogilevich",
        "target": "Solntsevskaya Bratva",
        "type": "controls",
        "tier": "documented",
        "desc": "FBI and DOJ identify Mogilevich as controlling or directing the Solntsevskaya Bratva, the largest Russian organized crime syndicate. DOJ 2003 indictment and FBI Most Wanted listing detail his leadership role.",
        "sources": [192, 193],
    },
    {
        "source": "Semion Mogilevich",
        "target": "FSB",
        "type": "protected_by",
        "tier": "credible",
        "desc": "Multiple investigative sources (OCCRP, Belton, FBI assessments) document that Mogilevich operates with de facto protection of Russian state security. Briefly arrested in Moscow (2008), released same year on reduced charges. FBI removed him from Most Wanted in 2015 citing inability to apprehend him in Russia.",
        "sources": [193, 207, 198],
    },
    {
        "source": "Semion Mogilevich",
        "target": "FBI",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "FBI Ten Most Wanted Fugitives (2009-2015). DOJ indictment (2003) on 45 counts including racketeering and $150M fraud through YBM Magnex International. Never extradited despite Interpol Red Notice.",
        "sources": [192, 193, 202],
    },
    {
        "source": "Semion Mogilevich",
        "target": "Meyer Lansky",
        "type": "successor_to",
        "tier": "inference",
        "desc": "Pattern-based: Mogilevich is widely described (FBI, DOJ, OCCRP) as the 'Russian Meyer Lansky' — the financial architect of organized crime operating at the intersection of state power and criminal networks. Both specialized in money laundering at industrial scale. Both operated with intelligence agency relationships. Not a personal connection — Lansky died 1983 — but a functional lineage in the intelligence-crime nexus.",
        "sources": [193, 207],
    },
    {
        "source": "Semion Mogilevich",
        "target": "Deutsche Bank",
        "type": "financial_connection",
        "tier": "inference",
        "desc": "Deutsche Bank's $10B Russian mirror-trading scheme (fined 2017) moved money from Russia through DB's Moscow, London, and New York operations. FinCEN files document broader Russian money laundering through DB. While Mogilevich is not named in the DB fine, FBI and OCCRP document him as controlling major Russian money laundering pipelines operating through the same financial channels.",
        "sources": [200, 195, 207],
    },

    # ---- Solntsevskaya Bratva connections ----
    {
        "source": "Solntsevskaya Bratva",
        "target": "Bayrock Group",
        "type": "financial_connection",
        "tier": "inference",
        "desc": "Senate Judiciary testimony and investigative reporting document that Bayrock Group's funding sources included Russian and ex-Soviet money flows. Felix Sater's connections to Russian organized crime are documented in DOJ filings. The financial pipeline from Russian organized crime through real estate development entities like Bayrock is a documented pattern, though direct Solntsevskaya-Bayrock links are inferential.",
        "sources": [201, 190],
    },

    # ---- Rybolovlev connections ----
    {
        "source": "Dmitry Rybolovlev",
        "target": "Donald Trump",
        "type": "financial_connection",
        "tier": "documented",
        "desc": "Rybolovlev purchased Trump's Palm Beach estate (Maison de l'Amitié) for $95M in 2008 — more than double Trump's $41.35M purchase price (2004) — during the financial crisis. Property was never inhabited and was demolished. Transaction documented in Palm Beach County records, widely reported.",
        "sources": [199, 205],
    },
    {
        "source": "Dmitry Rybolovlev",
        "target": "Vladimir Putin",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Rybolovlev is a Russian oligarch whose wealth derives from potash fertilizer (Uralkali). As with all major Russian oligarchs, his ability to operate and maintain wealth is contingent on Kremlin relationships. Was convicted of murder in Russia (1996, overturned on appeal 1997) during the period of oligarchic consolidation. Multiple investigative accounts place him within Putin's oligarch architecture.",
        "sources": [198, 205],
    },
    {
        "source": "Dmitry Rybolovlev",
        "target": "Little Saint James",
        "type": "proximity",
        "tier": "credible",
        "desc": "ABC News reported FBI obtained high-resolution photos of visitors to Epstein's island; Rybolovlev's yacht was spotted in the vicinity of Little Saint James. Direct visitation not confirmed — classified as proximity, not visitation.",
        "sources": [204],
    },
]


# ============================================================
# ENTITY → SOURCE links
# ============================================================

ENTITY_SOURCES = {
    "Vladimir Putin": [190, 191, 194, 196, 197, 198, 203],
    "FSB": [190, 191, 194, 198],
    "Semion Mogilevich": [192, 193, 202, 207],
    "Solntsevskaya Bratva": [192, 193, 207],
    "Dmitry Rybolovlev": [199, 204, 205],
}
