"""
China Cluster — Expansion layer for Intel Console.
Entities: Johnny Chung, John Huang, Charlie Trie, Bernard Schwartz, Liu Chaoying,
Wang Jun, Desmond Shum, MSS, CITIC Group, Lippo Group, Cox Report (1999).

Maps the documented China–Epstein–Clinton–intelligence nexus: 1990s campaign finance
scandal (Chinagate), satellite technology transfer to China, PLA intelligence operations
targeting U.S. elections, and Epstein's documented cultivation of Chinese
military-intelligence-linked entities through intermediaries.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 208+ (continuing from existing 207)
# ============================================================

SOURCES = [
    # Government / Congressional
    {
        "id": 208,
        "title": "Senate Committee on Governmental Affairs — Investigation of Illegal or Improper Activities in Connection with 1996 Federal Election Campaigns (Thompson Committee Report)",
        "url": "https://www.govinfo.gov/content/pkg/CRPT-105srpt167/html/CRPT-105srpt167-pt4.htm",
        "source_type": "congressional",
        "year": 1998,
    },
    {
        "id": 209,
        "title": "House Select Committee Report — U.S. National Security and Military/Commercial Concerns with the People's Republic of China (Cox Report)",
        "url": "https://www.govinfo.gov/content/pkg/GPO-CRPT-105hrpt851/html/ch1bod.html",
        "source_type": "congressional",
        "year": 1999,
    },
    {
        "id": 210,
        "title": "H. Rept. 105-829 — Investigation of Political Fundraising Improprieties and Possible Violations of Law (Burton Committee Interim Report)",
        "url": "https://www.congress.gov/congressional-report/105th-congress/house-report/829/1",
        "source_type": "congressional",
        "year": 1998,
    },
    {
        "id": 211,
        "title": "Senate Governmental Affairs Committee — The China Connection: Summary of Findings Relating to Efforts of the PRC to Influence U.S. Policies and Elections",
        "url": "https://fas.org/irp/congress/1998_rpt/sgo-sir/2-18.htm",
        "source_type": "congressional",
        "year": 1998,
    },
    {
        "id": 212,
        "title": "Senate Governmental Affairs Committee — John Huang at Commerce",
        "url": "https://irp.fas.org/congress/1998_rpt/sgo-sir/1-14.htm",
        "source_type": "congressional",
        "year": 1998,
    },
    {
        "id": 213,
        "title": "Senate Governmental Affairs Committee — John Huang's Years at Lippo",
        "url": "https://irp.fas.org/congress/1998_rpt/sgo-sir/1-13.htm",
        "source_type": "congressional",
        "year": 1998,
    },
    {
        "id": 214,
        "title": "House Committee on Government Reform — The Role of Yah Lin 'Charlie' Trie in Illegal Political Fundraising (Hearing, 106th Congress)",
        "url": "https://www.govinfo.gov/content/pkg/CHRG-106hhrg68344/html/CHRG-106hhrg68344.htm",
        "source_type": "congressional",
        "year": 2000,
    },
    {
        "id": 215,
        "title": "CRS Report 98-485 — China: Possible Missile Technology Transfers from U.S. Satellite Export Policy",
        "url": "https://www.everycrsreport.com/reports/98-485.html",
        "source_type": "government",
        "year": 1998,
    },
    {
        "id": 216,
        "title": "CRS Report RL30220 — China's Technology Acquisitions: Cox Committee's Report — Findings, Issues, and Recommendations",
        "url": "https://www.everycrsreport.com/reports/RL30220.html",
        "source_type": "government",
        "year": 1999,
    },
    {
        "id": 217,
        "title": "DOJ — Loral Space & Communications Settlement: $14 Million Fine for ITAR Violations (Satellite Technology Transfer to China)",
        "url": "https://learnexportcompliance.com/insights/loral-agrees-to-a-14-million-settlement-for-alleged-itar-violations",
        "source_type": "government",
        "year": 2002,
    },
    {
        "id": 218,
        "title": "CRS Report RL30143 — China: Suspected Acquisition of U.S. Nuclear Weapon Secrets",
        "url": "https://www.everycrsreport.com/reports/RL30143.html",
        "source_type": "government",
        "year": 1999,
    },
    # Court / DOJ
    {
        "id": 219,
        "title": "DOJ — United States v. Yah Lin 'Charlie' Trie: Conviction for Campaign Finance Violations",
        "url": "https://www.govinfo.gov/content/pkg/CHRG-106hhrg68344/html/CHRG-106hhrg68344.htm",
        "source_type": "court",
        "year": 1999,
    },
    {
        "id": 220,
        "title": "DOJ — United States v. John Huang: Guilty Plea to Felony Campaign Finance Violation",
        "url": "https://en.wikipedia.org/wiki/1996_United_States_campaign_finance_controversy",
        "source_type": "court",
        "year": 1999,
    },
    {
        "id": 221,
        "title": "DOJ — United States v. James Riady: Guilty Plea, $8.6 Million Fine for Campaign Finance Violations",
        "url": "https://en.wikipedia.org/wiki/James_Riady",
        "source_type": "court",
        "year": 2001,
    },
    # Journalism
    {
        "id": 222,
        "title": "Washington Post — Findings Link Clinton Allies to Chinese Intelligence",
        "url": "https://www.washingtonpost.com/archive/politics/1998/02/10/findings-link-clinton-allies-to-chinese-intelligence/87265d5d-7452-41f2-ad2f-aa4abe7e579e/",
        "source_type": "journalism",
        "year": 1998,
    },
    {
        "id": 223,
        "title": "Washington Post — Chung Links '96 Campaign Funds to Beijing",
        "url": "https://www.washingtonpost.com/archive/politics/1999/04/04/chung-links-96-campaign-funds-to-beijing/cef4fa1c-f7a6-4ec3-a63a-c4456f8a7cde/",
        "source_type": "journalism",
        "year": 1999,
    },
    {
        "id": 224,
        "title": "Chicago Tribune — China Arms Dealer Guest of Clinton",
        "url": "https://www.chicagotribune.com/news/ct-xpm-1996-12-21-9612210093-story.html",
        "source_type": "journalism",
        "year": 1996,
    },
    {
        "id": 225,
        "title": "Washington Post — Campaign Finance Key Player: Wang Jun",
        "url": "https://www.washingtonpost.com/wp-srv/politics/special/campfin/players/jun.htm",
        "source_type": "journalism",
        "year": 1998,
    },
    {
        "id": 226,
        "title": "The Wire China — Epstein and China",
        "url": "https://www.thewirechina.com/2026/02/13/epstein-and-china/",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 227,
        "title": "The Bureau — The CITIC Files: Epstein Introduced to China's Military-Intelligence Complex Through a Network Launched by Lord Peter Mandelson",
        "url": "https://www.thebureau.news/p/the-citic-files-epstein-introduced",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 228,
        "title": "Asia Sentinel — Epstein Advised Former Top Morgan Banker on China Strategy",
        "url": "https://www.asiasentinel.com/p/jeffrey-epstein-advised-jes-staley-china-strategy",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 229,
        "title": "Baltimore Sun — Clinton Backers Grow Wary: Waivers for Transfer of Technology to China Raise Deep Concerns",
        "url": "https://www.baltimoresun.com/news/bs-xpm-1998-05-24-1998144026-story.html",
        "source_type": "journalism",
        "year": 1998,
    },
    {
        "id": 230,
        "title": "Capital Research Center — When the Chinese Weapons Merchant Visited the Clinton White House",
        "url": "https://capitalresearch.org/article/when-the-chinese-weapons-merchant-visited-the-clinton-white-house/",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 231,
        "title": "Bloomberg — UK Ambassador Mandelson Expressed Support for Epstein, Emails Reveal",
        "url": "https://www.bloomberg.com/features/2025-jeffrey-epstein-emails-peter-mandelson/",
        "source_type": "journalism",
        "year": 2025,
    },
    # Books
    {
        "id": 232,
        "title": "Desmond Shum — Red Roulette: An Insider's Story of Wealth, Power, Corruption, and Vengeance in Today's China",
        "url": "https://en.wikipedia.org/wiki/Red_Roulette",
        "source_type": "book",
        "author": "Desmond Shum",
        "year": 2021,
    },
    {
        "id": 233,
        "title": "CSIS — Survey of Chinese Espionage in the United States Since 2000",
        "url": "https://www.csis.org/programs/strategic-technologies-program/survey-chinese-espionage-united-states-2000",
        "source_type": "journalism",
        "year": 2021,
    },
]


# ============================================================
# ENTITIES — 11 new entities
# ============================================================

_DESC_JOHNNY_CHUNG = (
    "Zhongwen 'Johnny' Chung (born c. 1955). Taiwanese-American businessman from Torrance, "
    "California, who became a central figure in the 1996 campaign finance controversy "
    "('Chinagate'). Owner of a fax broadcasting business before entering Democratic fundraising."
    "\n\n"
    "FUNDRAISING ACTIVITIES: Between 1994 and 1996, Chung donated $366,000 to the Democratic "
    "National Committee. Made 49 separate visits to the White House between February 1994 and "
    "February 1996. Testified before the House Government Reform Committee (Burton Committee) "
    "in May 1999."
    "\n\n"
    "PLA INTELLIGENCE CONNECTION: Chung testified under oath that he was introduced to General "
    "Ji Shengde, then head of PLA military intelligence (Second Department of the General Staff), "
    "by Liu Chaoying, a PLA Lieutenant Colonel and executive at China Aerospace International "
    "Holdings. Chung testified that Ji told him: 'I will give you 300,000 U.S. dollars. You can "
    "give it to the president and the Democrat Party.' Chung told federal investigators that "
    "$35,000 of his DNC donations came from Liu Chaoying and, in turn, China's military intelligence."
    "\n\n"
    "LEGAL OUTCOME: Cooperated with federal investigators. Pled guilty to bank fraud, tax evasion, "
    "and two misdemeanor counts of conspiring to violate election law. Sentenced to five years' "
    "probation and 3,000 hours of community service."
)

_DESC_JOHN_HUANG = (
    "John Huang (born c. 1945). Taiwanese-American political fundraiser and former U.S. "
    "Commerce Department official. Key figure in the 1996 campaign finance controversy."
    "\n\n"
    "LIPPO GROUP: Before government service, Huang worked for the Lippo Group, a multi-billion-dollar "
    "Indonesian conglomerate controlled by the Riady family (Mochtar and James Riady). The 1998 "
    "Senate Governmental Affairs Committee report stated that both Riadys 'had a long-term "
    "relationship with a Chinese intelligence agency,' based on classified CIA and FBI intelligence."
    "\n\n"
    "COMMERCE DEPARTMENT: Appointed Deputy Assistant Secretary of Commerce for International "
    "Economic Affairs by President Clinton in December 1993, responsible for Asia-U.S. trade. "
    "This position gave Huang access to classified intelligence on China. While at Commerce, "
    "Huang met nine times with Chinese embassy officials (documented in committee records)."
    "\n\n"
    "DNC FUNDRAISING: After leaving Commerce, joined DNC as vice chairman of finance. Raised "
    "$3.4 million for the Democratic Party; more than half was returned because of foreign sourcing. "
    "Solicited approximately $1.6 million later returned by DNC as illegal foreign contributions."
    "\n\n"
    "LEGAL OUTCOME: Pled guilty to a single felony count of campaign finance violation in 1999."
)

_DESC_CHARLIE_TRIE = (
    "Yah Lin 'Charlie' Trie (born c. 1950). Little Rock restaurateur and longtime friend of "
    "Bill Clinton from Arkansas. Became a key intermediary between Chinese government-connected "
    "entities and the Clinton White House."
    "\n\n"
    "WHITE HOUSE ACCESS: Trie arranged the February 6, 1996 White House 'coffee' meeting at "
    "which Wang Jun — chairman of both CITIC and Poly Technologies (PLA arms trading company) — "
    "met President Clinton. This occurred while federal agents were building the 'Dragon Fire' "
    "case against Poly Technologies for smuggling 2,000 AK-47s into the United States."
    "\n\n"
    "CAMPAIGN FINANCE: Delivered $460,000 in questionable contributions to the DNC and Clinton's "
    "legal defense fund. When congressional investigations focused on him in late 1996, Trie "
    "fled to China."
    "\n\n"
    "LEGAL OUTCOME: Returned to the U.S. in 1998. Convicted of violating federal campaign finance "
    "laws — making political contributions in someone else's name and causing a false statement "
    "to be made to the FEC. Sentenced to three years' probation and four months' home detention."
)

_DESC_BERNARD_SCHWARTZ = (
    "Bernard L. Schwartz (1925-2024). Chairman and CEO of Loral Space & Communications "
    "(1972-2006). During the 1996 election cycle, Schwartz was the single largest individual "
    "donor to the Democratic Party — he and his wife contributed $1,122,000, of which $1,089,750 "
    "went to Democratic candidates and committees."
    "\n\n"
    "TECHNOLOGY TRANSFER: Loral and Hughes Electronics were found by the Cox Committee (1999) to "
    "have 'illegally' provided China with technical assistance that improved the reliability of "
    "Chinese ballistic missiles used to launch satellites — and potentially nuclear warheads. "
    "In 1996, Loral helped Chinese engineers diagnose a Long March 3B rocket failure, sharing "
    "information on guidance and fairing design without the legally required State Department "
    "export license, in violation of the International Traffic in Arms Regulations (ITAR)."
    "\n\n"
    "CLINTON CONNECTION: Between October 1995 and March 1996 — while Clinton was deciding "
    "whether to grant Loral waivers to export satellite technology to China — Schwartz injected "
    "more than $150,000 into DNC coffers. In 1996, Clinton transferred satellite export licensing "
    "from State Department to Commerce Department (less restrictive). Schwartz celebrated his "
    "71st birthday at the White House with the Clintons."
    "\n\n"
    "LEGAL OUTCOME: Exonerated by DOJ in campaign finance matter. Loral settled the missile "
    "technology transfer case in 2002, paying a $14 million fine. Hughes Electronics fined $32 "
    "million in 2003 for the same technology transfer."
)

_DESC_LIU_CHAOYING = (
    "Liu Chaoying (born c. 1962). Former Lieutenant Colonel in the People's Liberation Army and "
    "executive at China Aerospace International Holdings (CASIL), the Hong Kong-based subsidiary "
    "of China Aerospace Science and Technology Corporation (CASC) — China's premier satellite "
    "launch company."
    "\n\n"
    "FAMILY: Daughter of General Liu Huaqing, former Vice Chairman of the Central Military "
    "Commission and one of the most powerful figures in the PLA. Her elder brother is a vice "
    "admiral in the PLA Navy."
    "\n\n"
    "CAMPAIGN FINANCE CONNECTION: Johnny Chung befriended Liu during a U.S. Commerce Department "
    "trade mission to China. When Liu visited the U.S. in July 1996, Chung introduced her to "
    "President Clinton at a Los Angeles fundraiser. Chung testified under oath that Liu introduced "
    "him to General Ji Shengde (head of PLA military intelligence), and that $35,000 of the money "
    "he donated to the DNC came from Liu and China's military intelligence."
    "\n\n"
    "Liu also invested $300,000 in Chung's company, Automated Intelligent Systems. Both Liu and "
    "the Chinese government denied the campaign finance allegations."
)

_DESC_WANG_JUN = (
    "Wang Jun (born c. 1941). Son of former Chinese Vice President Wang Zhen. Simultaneously "
    "served as Chairman of CITIC (China International Trust and Investment Corporation) and "
    "Chairman of Poly Technologies/Poly Group."
    "\n\n"
    "CITIC: State-owned investment conglomerate established in 1979 at the direction of Deng "
    "Xiaoping. The Rand Corporation identified CITIC as a front for the PLA in 1997. CITIC's "
    "vice chair Xiong Xianghui was drawn from the Intelligence Bureau of the Joint Staff "
    "Department, and significant CITIC leadership had intelligence backgrounds."
    "\n\n"
    "POLY TECHNOLOGIES: The commercial arm of the PLA's global munitions operations. Spun off "
    "from CITIC in 1984. Under Wang Jun's leadership, Poly was implicated in Operation Dragon "
    "Fire — the largest seizure of smuggled automatic weapons in U.S. law enforcement history. "
    "Federal agents seized 2,000 illegally imported AK-47 rifles linked to Poly. The suspects "
    "had to call PLA headquarters in Beijing to authorize the shipment."
    "\n\n"
    "CLINTON WHITE HOUSE VISIT: On February 6, 1996, Wang attended a White House coffee meeting "
    "with President Clinton, arranged by Charlie Trie. This occurred while the Dragon Fire "
    "investigation was active. Clinton later called it 'clearly inappropriate.' The Washington "
    "Post reported that U.S. intelligence had suspected Wang's companies of arming rogue states "
    "and funneling American military technology back to China."
)

_DESC_DESMOND_SHUM = (
    "Desmond Shum (born 1968, Shanghai). Chinese-Canadian businessman, real estate developer, "
    "and author of 'Red Roulette: An Insider's Story of Wealth, Power, Corruption, and "
    "Vengeance in Today's China' (2021). Former husband of Whitney Duan (Duan Weihong), a "
    "well-connected Chinese businesswoman with close ties to the CCP Politburo."
    "\n\n"
    "EPSTEIN CONNECTION: Lord Peter Mandelson introduced Desmond Shum to Jeffrey Epstein in "
    "New York in February 2010. Documented in DOJ-released Epstein files (3+ million pages). "
    "In September 2010, Mandelson asked Epstein to 'nurture' his relationship with Shum."
    "\n\n"
    "CITIC BRIDGE: In April 2011, Shum and Epstein discussed creating an 'offshore banking' "
    "business in China. Shum told Epstein he had discussed the idea with the chairman of CITIC, "
    "the vice mayor of Shanghai, and a 'top decision maker' at the State Administration of "
    "Foreign Exchange (SAFE). Email evidence shows Shum introduced CITIC senior leadership "
    "directly to Epstein — connecting Epstein to a conglomerate identified by the Rand "
    "Corporation as a PLA front."
    "\n\n"
    "Shum later published 'Red Roulette' exposing corruption at the highest levels of the CCP. "
    "His ex-wife Whitney Duan disappeared in China in 2017."
)

_DESC_MSS = (
    "Ministry of State Security (Guojia Anquan Bu, MSS). The People's Republic of China's "
    "intelligence, security, and secret police agency. Established in 1983 by merging the "
    "Central Investigation Department with counterintelligence elements of the Ministry of "
    "Public Security."
    "\n\n"
    "FUNCTION: A DOJ document described the MSS as combining the functions of the CIA and FBI. "
    "Responsible for foreign intelligence, counterintelligence, and domestic political security. "
    "The 18th Bureau is dedicated specifically to espionage operations against the United States."
    "\n\n"
    "DOCUMENTED OPERATIONS: CSIS documented hundreds of Chinese espionage cases in the U.S. "
    "since 2000. Notable penetrations include Katrina Leung (codename 'Parlor Maid'), an FBI "
    "informant who was simultaneously a double agent for the MSS from 1982 to 2003, compromising "
    "20 years of FBI counterintelligence on China."
    "\n\n"
    "NETWORK RELEVANCE: The MSS operates alongside PLA military intelligence (Second Department "
    "of the General Staff) — the entity that, through General Ji Shengde, funneled money to "
    "Clinton's DNC via Johnny Chung. The Thompson Committee (1998) documented a PRC 'Central "
    "Leading Group for U.S. Congressional Affairs' coordinating China's influence operations. "
    "The MSS relationship with Western intelligence agencies (CIA, MI6, Mossad) is primarily "
    "adversarial, with limited cooperation on counter-terrorism."
)

_DESC_CITIC = (
    "China International Trust and Investment Corporation (CITIC Group). State-owned "
    "investment conglomerate established in 1979 at the direction of Deng Xiaoping. One of "
    "China's largest and most influential financial and industrial conglomerates."
    "\n\n"
    "MILITARY-INTELLIGENCE CONNECTIONS: The Rand Corporation identified CITIC as a front for "
    "the PLA in 1997. CITIC's vice chair Xiong Xianghui was drawn from the Intelligence Bureau "
    "of the Joint Staff Department. Poly Group — the PLA's global munitions arm — started in "
    "1983 as a CITIC subsidiary before spinning off. Wang Jun simultaneously chaired both CITIC "
    "and Poly Technologies."
    "\n\n"
    "EPSTEIN CONNECTION: DOJ-released emails (2025) document that Desmond Shum introduced CITIC "
    "senior leadership directly to Jeffrey Epstein, facilitated by Lord Peter Mandelson. Shum "
    "discussed creating an 'offshore banking' business in China with Epstein, involving the "
    "CITIC chairman and senior Chinese government financial officials."
    "\n\n"
    "Represents the institutional fusion of Chinese state capital, military interests, and "
    "intelligence operations — a state-level parallel to the Western intelligence-finance "
    "nexus already mapped in this network."
)

_DESC_LIPPO = (
    "Lippo Group. Multi-billion-dollar Indonesian conglomerate controlled by the Riady family "
    "(Mochtar Riady and his son James Riady). Operations span banking, real estate, "
    "manufacturing, insurance, securities, and retail across Southeast Asia."
    "\n\n"
    "CHINESE INTELLIGENCE CONNECTION: The 1998 Senate Governmental Affairs Committee reported "
    "that both Mochtar and James Riady 'had a long-term relationship with a Chinese intelligence "
    "agency.' According to journalist Bob Woodward, this finding was based on highly classified "
    "intelligence from both the CIA and FBI."
    "\n\n"
    "CLINTON CONNECTION: James Riady first met Bill Clinton in the late 1970s in Arkansas. "
    "According to White House logs, James Riady visited the White House 20 times and met with "
    "President Clinton on six of those visits. John Huang worked for Lippo before his appointment "
    "to the Commerce Department. Campaign contributions made by Huang had been reimbursed with "
    "funds wired from a foreign Lippo entity."
    "\n\n"
    "LEGAL OUTCOME: In 2001, James Riady pled guilty to a felony campaign finance charge and "
    "paid an $8.6 million fine — the largest fine for a campaign finance violation in U.S. history "
    "at the time."
)

_DESC_COX_REPORT = (
    "Cox Report (formally: Report of the Select Committee on U.S. National Security and "
    "Military/Commercial Concerns with the People's Republic of China). Classified January 3, "
    "1999; declassified version released May 25, 1999. 3-volume, 871-page investigation "
    "commissioned by a 409-10 vote of the U.S. House of Representatives on June 18, 1998."
    "\n\n"
    "KEY FINDINGS: (1) China stole design information on the seven most advanced U.S. "
    "thermonuclear weapons, including the W-88 miniaturized warhead for the Trident II "
    "submarine-launched missile. (2) Hughes and Loral 'illegally' transferred missile technology "
    "to China — improving fairing design (1993, 1995) and rocket guidance (1996) — violating "
    "ITAR without required State Department licenses. (3) The stolen secrets enabled the PLA "
    "to accelerate development of its own nuclear weapons."
    "\n\n"
    "RECOMMENDATIONS: 38 recommendations including strengthening Energy Department "
    "counterintelligence, tightening export controls on dual-use technologies, and giving "
    "State and Defense more oversight of satellite exports."
    "\n\n"
    "The Cox Report represents the most comprehensive official investigation of Chinese "
    "technology acquisition from the United States, documenting both espionage and legal "
    "technology transfer facilitated by corporate lobbying and campaign finance connections."
)


ENTITIES = [
    {
        "name": "Johnny Chung",
        "entity_type": "person",
        "description": _DESC_JOHNNY_CHUNG,
        "aliases": "Zhongwen Chung",
        "metadata": {},
    },
    {
        "name": "John Huang",
        "entity_type": "person",
        "description": _DESC_JOHN_HUANG,
        "aliases": "Huang",
        "metadata": {},
    },
    {
        "name": "Charlie Trie",
        "entity_type": "person",
        "description": _DESC_CHARLIE_TRIE,
        "aliases": "Yah Lin Trie",
        "metadata": {},
    },
    {
        "name": "Bernard Schwartz",
        "entity_type": "person",
        "description": _DESC_BERNARD_SCHWARTZ,
        "aliases": "Bernie Schwartz, Bernard L. Schwartz",
        "metadata": {},
    },
    {
        "name": "Liu Chaoying",
        "entity_type": "person",
        "description": _DESC_LIU_CHAOYING,
        "aliases": "Liu",
        "metadata": {},
    },
    {
        "name": "Wang Jun",
        "entity_type": "person",
        "description": _DESC_WANG_JUN,
        "aliases": "",
        "metadata": {},
    },
    {
        "name": "Desmond Shum",
        "entity_type": "person",
        "description": _DESC_DESMOND_SHUM,
        "aliases": "",
        "metadata": {},
    },
    {
        "name": "MSS",
        "entity_type": "agency",
        "description": _DESC_MSS,
        "aliases": "Ministry of State Security, Guojia Anquan Bu, Chinese Intelligence",
        "metadata": {},
    },
    {
        "name": "CITIC Group",
        "entity_type": "organization",
        "description": _DESC_CITIC,
        "aliases": "CITIC, China International Trust and Investment Corporation",
        "metadata": {},
    },
    {
        "name": "Lippo Group",
        "entity_type": "organization",
        "description": _DESC_LIPPO,
        "aliases": "Lippo",
        "metadata": {},
    },
    {
        "name": "Cox Report (1999)",
        "entity_type": "event",
        "description": _DESC_COX_REPORT,
        "aliases": "Cox Committee Report",
        "metadata": {},
    },
]


# ============================================================
# RELATIONSHIPS — connections to existing network + internal
# ============================================================
# Reference existing entities by name (resolved at insert time):
#   Bill Clinton [32], Hillary Clinton [31], Donald Trump [33],
#   CIA [85], FBI [87], Mossad [88], DOJ [89], NSA [86],
#   BCCI [54], Nicole Junkermann [151], Jes Staley [124],
#   JPMorgan Chase [56], Deutsche Bank [57]

RELATIONSHIPS = [
    # ---- Johnny Chung connections ----
    {
        "source": "Johnny Chung",
        "target": "Bill Clinton",
        "type": "financial_connection",
        "tier": "documented",
        "desc": (
            "Between 1994 and 1996, Chung donated $366,000 to the DNC supporting Clinton's "
            "reelection. Made 49 White House visits (Feb 1994 - Feb 1996). Testified before "
            "Burton Committee (1999). All donations later returned by DNC."
        ),
        "sources": [210, 223],
    },
    {
        "source": "Johnny Chung",
        "target": "Liu Chaoying",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Chung befriended Liu during a U.S. Commerce Department trade mission to China. "
            "Liu invested $300,000 in Chung's company, Automated Intelligent Systems. Chung "
            "introduced Liu to President Clinton at a Los Angeles fundraiser in July 1996. "
            "Chung testified under oath that $35,000 of his DNC donations came from Liu."
        ),
        "sources": [210, 223],
    },
    {
        "source": "Johnny Chung",
        "target": "MSS",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "Chung testified under oath (1999) that Liu Chaoying introduced him to General "
            "Ji Shengde, head of PLA military intelligence (2nd Dept of General Staff — "
            "a parallel service to the MSS). Ji told Chung: 'I will give you 300,000 U.S. "
            "dollars. You can give it to the president and the Democrat Party.' Documented "
            "PLA intelligence operation to influence U.S. elections through campaign finance."
        ),
        "sources": [223, 211],
    },
    {
        "source": "Johnny Chung",
        "target": "FBI",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "FBI investigated Chung as part of the 1996 campaign finance scandal. Chung "
            "cooperated with federal investigators and testified before Congress. Pled guilty "
            "to bank fraud, tax evasion, and campaign finance violations."
        ),
        "sources": [210, 223],
    },

    # ---- John Huang connections ----
    {
        "source": "John Huang",
        "target": "Bill Clinton",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Clinton appointed Huang Deputy Assistant Secretary of Commerce (Dec 1993). "
            "Huang later joined DNC as vice chairman of finance, raising $3.4M for Democrats. "
            "More than half was returned due to foreign sourcing."
        ),
        "sources": [212, 208],
    },
    {
        "source": "John Huang",
        "target": "Lippo Group",
        "type": "employed_by",
        "tier": "documented",
        "desc": (
            "Huang worked for the Lippo Group before his government appointment. Senate "
            "committee documented that campaign contributions made by Huang were reimbursed "
            "with funds wired from a foreign Lippo entity into a Riady-maintained account "
            "at Lippo Bank, then distributed to Huang in cash."
        ),
        "sources": [213, 222],
    },
    {
        "source": "John Huang",
        "target": "MSS",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Senate Governmental Affairs Committee (1998) reported that Huang's employers, "
            "the Riadys, 'had a long-term relationship with a Chinese intelligence agency' "
            "(based on classified CIA/FBI intelligence). While at Commerce, Huang met 9 times "
            "with Chinese embassy officials. However, the committee stated evidence did not "
            "support the charge that Huang himself served as a spy."
        ),
        "sources": [212, 222, 208],
    },
    {
        "source": "John Huang",
        "target": "DOJ",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "DOJ investigated Huang for campaign finance violations. Pled guilty to a single "
            "felony count in 1999."
        ),
        "sources": [220],
    },

    # ---- Charlie Trie connections ----
    {
        "source": "Charlie Trie",
        "target": "Bill Clinton",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Longtime friend from Little Rock, Arkansas. Trie delivered $460,000 in "
            "questionable contributions to the DNC and Clinton's legal defense fund. "
            "Arranged Wang Jun's February 1996 White House meeting with Clinton."
        ),
        "sources": [214, 224],
    },
    {
        "source": "Charlie Trie",
        "target": "Wang Jun",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Trie arranged Wang Jun's February 6, 1996 White House coffee meeting with "
            "President Clinton. Wang was chairman of both CITIC and Poly Technologies "
            "(PLA arms company). This occurred while the 'Dragon Fire' investigation was "
            "actively targeting Poly Technologies for weapons smuggling."
        ),
        "sources": [224, 225, 230],
    },
    {
        "source": "Charlie Trie",
        "target": "DOJ",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "Fled to China when congressional investigations focused on him (late 1996). "
            "Returned 1998. Convicted of campaign finance violations — making contributions "
            "in someone else's name. Sentenced to three years' probation and four months' "
            "home detention."
        ),
        "sources": [214, 219],
    },

    # ---- Bernard Schwartz connections ----
    {
        "source": "Bernard Schwartz",
        "target": "Bill Clinton",
        "type": "financial_connection",
        "tier": "documented",
        "desc": (
            "Largest individual donor to Democrats in 1996 cycle ($1,122,000 total, $1,089,750 "
            "to Democrats). Between Oct 1995 and March 1996, while Clinton mulled Loral export "
            "waivers for China, Schwartz injected $150,000+ into DNC. Celebrated 71st birthday "
            "at White House with Clintons. Harold Ickes memo to Clinton identified Schwartz "
            "as someone who could raise $3M in two weeks."
        ),
        "sources": [229, 209],
    },
    {
        "source": "Bernard Schwartz",
        "target": "Cox Report (1999)",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Schwartz's company Loral Space & Communications was a primary subject of the "
            "Cox Committee investigation. Cox Report found Loral 'illegally' transferred "
            "missile technology to China in 1996 — helping Chinese engineers diagnose a "
            "Long March 3B rocket failure without required State Department license."
        ),
        "sources": [209, 215, 217],
    },
    {
        "source": "Bernard Schwartz",
        "target": "DOJ",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "DOJ investigated Schwartz for campaign finance violations (exonerated). Loral "
            "separately settled the ITAR missile technology transfer case in 2002, paying "
            "a $14 million fine. Hughes Electronics fined $32 million for the same transfer."
        ),
        "sources": [217],
    },

    # ---- Liu Chaoying connections ----
    {
        "source": "Liu Chaoying",
        "target": "MSS",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "PLA Lieutenant Colonel and executive at China Aerospace International Holdings "
            "(CASIL). Daughter of General Liu Huaqing, former Vice Chairman of the Central "
            "Military Commission. Testified by Chung to have introduced him to PLA military "
            "intelligence chief Ji Shengde. PLA military intelligence operates parallel to MSS."
        ),
        "sources": [223, 211],
    },
    {
        "source": "Liu Chaoying",
        "target": "Bill Clinton",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Johnny Chung introduced Liu to President Clinton at a Los Angeles fundraiser "
            "in July 1996. Liu was a PLA Lieutenant Colonel and daughter of one of China's "
            "most senior military officials."
        ),
        "sources": [223, 210],
    },

    # ---- Wang Jun connections ----
    {
        "source": "Wang Jun",
        "target": "CITIC Group",
        "type": "controls",
        "tier": "documented",
        "desc": (
            "Wang Jun served as Chairman of CITIC (China International Trust and Investment "
            "Corporation). Simultaneously chaired Poly Technologies/Poly Group, the commercial "
            "arm of the PLA's global munitions operations."
        ),
        "sources": [225, 230],
    },
    {
        "source": "Wang Jun",
        "target": "Bill Clinton",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Attended White House coffee meeting with Clinton on February 6, 1996, arranged "
            "by Charlie Trie. Clinton later called it 'clearly inappropriate.' At the time, "
            "federal agents were building the Dragon Fire case against Wang's Poly Technologies "
            "for smuggling 2,000 AK-47s into the U.S."
        ),
        "sources": [224, 225, 230],
    },
    {
        "source": "Wang Jun",
        "target": "CIA",
        "type": "adversarial",
        "tier": "credible",
        "desc": (
            "U.S. intelligence officials suspected Wang's Poly Technologies of arming rogue "
            "states and funneling American military technology back to China for years before "
            "his White House visit. Poly Technologies was subsequently targeted in Operation "
            "Dragon Fire. CITIC identified by Rand Corporation as PLA front (1997)."
        ),
        "sources": [224, 225],
    },

    # ---- Desmond Shum connections ----
    {
        "source": "Desmond Shum",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Lord Peter Mandelson introduced Shum to Epstein in New York, February 2010. "
            "In September 2010, Mandelson asked Epstein to 'nurture' his relationship with "
            "Shum. In April 2011, Shum and Epstein discussed creating an 'offshore banking' "
            "business in China. Documented in DOJ-released Epstein files (3M+ pages)."
        ),
        "sources": [226, 227],
    },
    {
        "source": "Desmond Shum",
        "target": "CITIC Group",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Email evidence from Epstein files shows Shum introduced CITIC senior leadership "
            "directly to Epstein. Shum told Epstein he had discussed offshore banking plans "
            "with the CITIC chairman, vice mayor of Shanghai, and a 'top decision maker' at "
            "SAFE (State Administration of Foreign Exchange)."
        ),
        "sources": [227],
    },
    {
        "source": "Desmond Shum",
        "target": "Nicole Junkermann",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Both operated in Epstein's orbit with Chinese business interests. Junkermann's "
            "major investment in Shanghai Really Sports (2005) — one of the largest direct "
            "foreign investments in China at the time — and Shum's Beijing real estate empire "
            "placed both in overlapping circles of Epstein's China-facing network. Epstein "
            "introduced Junkermann to Robert Kuhn for China business in December 2018."
        ),
        "sources": [226, 228],
    },
    {
        "source": "Desmond Shum",
        "target": "Jes Staley",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Epstein advised former JPMorgan CEO Jes Staley on China strategy. Shum's CITIC "
            "connections and Epstein's cultivation of JPMorgan relationships placed Shum and "
            "Staley in overlapping network positions as Epstein pursued financial operations "
            "in China through JPMorgan's infrastructure."
        ),
        "sources": [228, 227],
    },

    # ---- MSS connections ----
    {
        "source": "MSS",
        "target": "CIA",
        "type": "adversarial",
        "tier": "documented",
        "desc": (
            "Primary adversaries. MSS 18th Bureau dedicated to espionage against the U.S. "
            "CSIS documented hundreds of Chinese espionage cases. Katrina Leung case (2003) "
            "demonstrated MSS penetration of FBI counterintelligence for 20 years. The Cox "
            "Report documented Chinese acquisition of U.S. nuclear secrets."
        ),
        "sources": [209, 233],
    },
    {
        "source": "MSS",
        "target": "FBI",
        "type": "adversarial",
        "tier": "documented",
        "desc": (
            "FBI is primary domestic counterintelligence agency against MSS operations in the "
            "U.S. The Katrina Leung double agent case ('Parlor Maid') compromised FBI Chinese "
            "counterintelligence for 20 years (1982-2003). MSS exploited intimate relationship "
            "between Leung and her FBI handler."
        ),
        "sources": [233],
    },
    {
        "source": "MSS",
        "target": "Mossad",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "China-Israel intelligence cooperation is documented but limited. Israel has been "
            "a significant source of military technology transfer to China, creating friction "
            "with the U.S. The same technology transfer patterns (dual-use tech, missile "
            "components) documented in the Cox Report involved Israeli as well as American "
            "technology reaching China."
        ),
        "sources": [209, 233],
    },

    # ---- CITIC Group connections ----
    {
        "source": "CITIC Group",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "DOJ-released Epstein emails document that Desmond Shum introduced CITIC senior "
            "leadership directly to Epstein (2010-2011). Epstein pursued offshore banking "
            "operations in China through CITIC connections, facilitated by Mandelson and Shum."
        ),
        "sources": [227, 226],
    },
    {
        "source": "CITIC Group",
        "target": "JPMorgan Chase",
        "type": "financial_connection",
        "tier": "credible",
        "desc": (
            "Epstein emails reference JPMorgan in connection with proposed China operations "
            "through CITIC. Mandelson wrote to Epstein about associating with JPM in China "
            "for two years. Epstein's documented role advising Jes Staley on China strategy "
            "places JPMorgan in the same network as CITIC."
        ),
        "sources": [228, 227],
    },

    # ---- Lippo Group connections ----
    {
        "source": "Lippo Group",
        "target": "Bill Clinton",
        "type": "financial_connection",
        "tier": "documented",
        "desc": (
            "James Riady met Clinton in late 1970s in Arkansas. Pledged $1M to Clinton's 1992 "
            "campaign. Visited White House 20 times, met Clinton 6 times. Riady pled guilty "
            "to felony campaign finance charge in 2001, paying record $8.6M fine."
        ),
        "sources": [221, 222, 208],
    },
    {
        "source": "Lippo Group",
        "target": "MSS",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Senate Governmental Affairs Committee (1998) reported that Mochtar and James Riady "
            "'had a long-term relationship with a Chinese intelligence agency,' based on "
            "classified CIA and FBI intelligence provided to the committee."
        ),
        "sources": [222, 208],
    },
    {
        "source": "Lippo Group",
        "target": "BCCI",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "Pattern-based: Lippo Group and BCCI both operated as international financial "
            "vehicles with documented intelligence agency relationships, both penetrated "
            "U.S. politics through campaign contributions and political access, and both "
            "maintained operations across Southeast Asia. BCCI operated in Indonesia (Lippo's "
            "home base). Both documented as conduits between foreign intelligence services "
            "and American political power."
        ),
        "sources": [208, 222],
    },

    # ---- Cox Report connections ----
    {
        "source": "Cox Report (1999)",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "CIA provided classified intelligence to the Cox Committee. The committee's "
            "findings on Chinese nuclear espionage relied on CIA and DOE counterintelligence "
            "assessments regarding theft of W-88 warhead design and other nuclear secrets."
        ),
        "sources": [209, 218],
    },
    {
        "source": "Cox Report (1999)",
        "target": "MSS",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The Cox Report documented Chinese intelligence operations targeting U.S. nuclear "
            "weapons laboratories and satellite technology. The committee found China stole "
            "design information on seven U.S. thermonuclear weapons including the W-88."
        ),
        "sources": [209, 216, 218],
    },
    {
        "source": "Cox Report (1999)",
        "target": "DOJ",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "DOJ conducted investigations into technology transfer violations documented by "
            "the Cox Committee. Resulted in Loral ($14M fine, 2002) and Hughes ($32M fine, "
            "2003) settlements for ITAR violations."
        ),
        "sources": [209, 217],
    },
]


# ============================================================
# ENTITY → SOURCE links
# ============================================================

ENTITY_SOURCES = {
    "Johnny Chung": [208, 210, 211, 223],
    "John Huang": [208, 212, 213, 220, 222],
    "Charlie Trie": [208, 214, 219, 224, 230],
    "Bernard Schwartz": [209, 215, 217, 229],
    "Liu Chaoying": [210, 211, 223],
    "Wang Jun": [224, 225, 230],
    "Desmond Shum": [226, 227, 228, 231, 232],
    "MSS": [209, 211, 218, 233],
    "CITIC Group": [225, 226, 227, 230],
    "Lippo Group": [208, 213, 221, 222],
    "Cox Report (1999)": [209, 215, 216, 218],
}
