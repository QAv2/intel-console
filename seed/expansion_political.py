"""
Political & Government Cluster — Expansion layer for Intel Console.
Entities: Politicians, diplomats, and government figures connected to the Epstein network.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# POLITICAL & GOVERNMENT CLUSTER — Sources 56-75
# ============================================================

SOURCES = [
    # Court / Legal
    {"id": 56, "title": "Virginia Giuffre v. Prince Andrew — Civil Settlement (SDNY)", "url": "https://en.wikipedia.org/wiki/Virginia_Giuffre_v._Prince_Andrew", "source_type": "court", "year": 2022},
    {"id": 57, "title": "DOJ Epstein Files — Phase One Release (2025)", "url": "https://www.justice.gov/epstein", "source_type": "government", "year": 2025},
    {"id": 58, "title": "Sandy Berger Guilty Plea — Unauthorized Removal of Classified Material", "url": "https://www.nbcnews.com/id/wbna7351422", "source_type": "court", "year": 2005},
    # Congressional
    {"id": 59, "title": "House Oversight Committee — Epstein Prosecutor Alex Acosta Testimony", "url": "https://oversightdemocrats.house.gov/news/press-releases/oversight-democrats-statement-public-release-epstein-prosecutor-and-former", "source_type": "congressional", "year": 2025},
    {"id": 60, "title": "Church Committee — Covert Action in Chile (1975)", "url": "https://nsarchive.gwu.edu/briefing-book/intelligence/2025-12-04/covert-action-chile-significance-church-committee-report-50", "source_type": "congressional", "year": 1975},
    # Journalism
    {"id": 61, "title": "Santa Fe New Mexican — Gov. Richardson Met with Epstein for Years After Conviction", "url": "https://www.santafenewmexican.com/news/local_news/records-show-gov-richardson-met-with-epstein-for-years-after-conviction/article_daf34b03-39af-4f6a-b016-5db73cc7f4b5.html", "source_type": "journalism", "year": 2025},
    {"id": 62, "title": "Harvard Crimson — Summers Visited Epstein's Island During 2005 Honeymoon", "url": "https://www.thecrimson.com/article/2025/11/21/summers-honeymoon-epstein-island/", "source_type": "journalism", "year": 2025},
    {"id": 63, "title": "Boston Globe — Harvard Report on Epstein Omitted Large Gift to Summers' Wife", "url": "https://www.bostonglobe.com/2025/11/18/metro/epstein-summers-wife-emails-harvard/", "source_type": "journalism", "year": 2025},
    {"id": 64, "title": "The Nation — How Jeffrey Epstein Captivated Harvard", "url": "https://www.thenation.com/article/society/jeffrey-epstein-harvard-summers/", "source_type": "journalism", "year": 2019},
    {"id": 65, "title": "NPR — Rudy Giuliani RICO Pioneer Claims Disputed by Former Prosecutors", "url": "https://www.npr.org/2023/08/29/1195552571/rudy-giuliani-rico-origin-story", "source_type": "journalism", "year": 2023},
    {"id": 66, "title": "CBS News — Rudy's Love/Hate Relationship With The Mob", "url": "https://www.cbsnews.com/news/rudys-love-hate-relationship-with-the-mob/", "source_type": "journalism", "year": 2008},
    {"id": 67, "title": "CNBC — Big Names in Epstein's Black Book", "url": "https://www.cnbc.com/2019/07/22/jeffrey-epsteins-black-book-trump-clintons-prince-andrew.html", "source_type": "journalism", "year": 2019},
    {"id": 68, "title": "Wall Street Journal — Epstein's Private Calendar (2023)", "url": "https://www.wsj.com/articles/jeffrey-epstein-calendar-cia-director-goldman-sachs-noam-chomsky-c9f6a3ff", "source_type": "journalism", "year": 2023},
    {"id": 69, "title": "National Security Archive — Kissinger and Chile: The Declassified Record", "url": "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB437/", "source_type": "government", "year": 2004},
    {"id": 70, "title": "NBC News — Third Epstein Files Release Takeaways", "url": "https://www.nbcnews.com/politics/justice-department/jeffrey-epstein-third-batch-release-takeaways-trump-prince-andrew-rcna250706", "source_type": "journalism", "year": 2026},
    {"id": 71, "title": "Irish Times — George Mitchell 'Declined or Deflected' Meeting Epstein", "url": "https://www.irishtimes.com/crime-law/2026/02/04/george-mitchell-says-he-declined-or-deflected-meeting-epstein-amid-renewed-giuffre-allegation/", "source_type": "journalism", "year": 2026},
    {"id": 72, "title": "Press Herald — Mitchell Denies Contact with Alleged Epstein Victim", "url": "https://www.pressherald.com/2019/08/09/former-u-s-sen-george-mitchell-denies-allegations-made-by-epstein-victim/", "source_type": "journalism", "year": 2019},
    {"id": 73, "title": "PBS — Prince Andrew & the Epstein Scandal Timeline", "url": "https://www.pbs.org/newshour/world/king-charles-iii-strips-prince-andrew-of-titles-evicts-him-from-royal-residence-over-epstein-ties", "source_type": "journalism", "year": 2025},
    {"id": 74, "title": "Kissinger Associates — Wikipedia/SourceWatch Corporate Profile", "url": "https://en.wikipedia.org/wiki/Kissinger_Associates", "source_type": "journalism", "year": 2023},
    {"id": 75, "title": "National Security Archive — Henry Kissinger Declassified Obituary", "url": "https://nsarchive.gwu.edu/briefing-book/chile-cold-war-henry-kissinger-indonesia-southern-cone-vietnam/2023-11-29/henry", "source_type": "government", "year": 2023},
]


# ============================================================
# ENTITIES — 7 people + 3 orgs + 2 events = 12 new entities
# ============================================================

_DESC_PRINCE_ANDREW = (
    "Andrew Albert Christian Edward Mountbatten-Windsor (born 1960), formerly styled "
    "Prince Andrew, Duke of York. Third child and second son of Queen Elizabeth II. "
    "Served in the Royal Navy 1979-2001, including as a helicopter pilot during the "
    "Falklands War."
    "\n\n"
    "EPSTEIN CONNECTION: Andrew stated he met Epstein in 1999 through Ghislaine Maxwell, "
    "with whom he had a longstanding friendship (and reportedly an intermittent romantic "
    "relationship) dating to her Oxford years. Flight logs place Andrew on Epstein's aircraft. "
    "He visited Epstein's Manhattan residence, was photographed at Epstein's New York home "
    "in 2010 (after Epstein's 2008 conviction), and attended events at Epstein's properties. "
    "Epstein and Maxwell attended Andrew's 40th birthday party at Windsor Castle in 2000."
    "\n\n"
    "GIUFFRE ALLEGATIONS: Virginia Giuffre alleged she was trafficked to Andrew on three "
    "occasions beginning in 2001 when she was 17 — in London (Maxwell's townhouse), "
    "New York, and on Little Saint James. A photograph shows Andrew with his arm around "
    "Giuffre's waist at Maxwell's London residence. An email from Maxwell to Epstein "
    "appeared to confirm the photo's authenticity. In the November 2019 BBC Newsnight "
    "interview, Andrew claimed he had no recollection of meeting Giuffre and offered "
    "widely discredited alibis (a Pizza Express visit in Woking, an inability to sweat)."
    "\n\n"
    "LEGAL & ROYAL CONSEQUENCES: Giuffre filed civil suit in August 2021 (SDNY). Andrew "
    "settled in February 2022 for an undisclosed sum (reported estimates range from "
    "3M-12M GBP) with no admission of liability. He was stripped of military affiliations "
    "and royal patronages by Queen Elizabeth in January 2022. In October 2025, King "
    "Charles III stripped him of all remaining titles including Duke of York and the "
    "style 'Prince.' In February 2026, he was arrested on suspicion of misconduct in "
    "public office in connection with his Epstein ties."
)

_DESC_RICHARDSON = (
    "William Blaine Richardson III (1947-2023). Democratic politician who served as "
    "U.S. Representative from New Mexico (1983-1997), U.S. Ambassador to the United "
    "Nations (1997-1998), Secretary of Energy (1998-2001), and Governor of New Mexico "
    "(2003-2011). Ran unsuccessfully for the 2008 Democratic presidential nomination. "
    "After leaving government, he became known as a freelance diplomat who helped "
    "negotiate the release of Americans detained abroad."
    "\n\n"
    "EPSTEIN CONNECTION: Epstein owned Zorro Ranch, a 7,500-acre property near Stanley, "
    "New Mexico. Virginia Giuffre testified in her 2016 deposition that Ghislaine "
    "Maxwell directed her to give Richardson a 'massage' at the ranch — testimony "
    "Giuffre has clarified meant providing sexual services. Richardson denied ever "
    "meeting Giuffre. Epstein contributed $50,000 to Richardson's 2002 gubernatorial "
    "campaign and again to his 2006 reelection; Richardson pledged to return or donate "
    "the money to charity after allegations surfaced."
    "\n\n"
    "POST-CONVICTION CONTACT: DOJ files released in 2025 revealed Richardson arranged "
    "to meet with Epstein at least nine times between 2010 and 2018 — years after "
    "Epstein's 2008 sex crime conviction in Florida. This included visits to Epstein's "
    "private island. The continued contact post-conviction is significant because it "
    "demonstrates awareness of Epstein's criminal history while maintaining the relationship."
    "\n\n"
    "KISSINGER ASSOCIATES: After leaving the governorship, Richardson served as Senior "
    "Managing Director at Kissinger McLarty Associates beginning in 2001, connecting "
    "him to the broader establishment power network. Richardson died in his sleep on "
    "September 1, 2023, at age 75."
)

_DESC_MITCHELL = (
    "George John Mitchell Jr. (born 1933). Democratic politician from Maine who served "
    "as U.S. Senator (1980-1995) and Senate Majority Leader (1989-1995). Appointed to "
    "the Senate in 1980 when Edmund Muskie resigned to become Secretary of State. As "
    "Majority Leader, he led passage of the Clean Air Act reauthorization and the "
    "Americans with Disabilities Act. After retiring from the Senate, he served as "
    "U.S. Special Envoy for Northern Ireland (1995-2000), helping broker the Good "
    "Friday Agreement, and as Special Envoy for Middle East Peace under Obama (2009-2011). "
    "Chairman of The Walt Disney Company (2004-2007)."
    "\n\n"
    "EPSTEIN ALLEGATIONS: In her 2016 deposition in the Maxwell civil case, Virginia "
    "Giuffre listed Mitchell among names of people Epstein and Maxwell allegedly "
    "directed her to have sexual contact with, stating: 'They instructed me to go to "
    "George Mitchell, Jean-Luc Brunel, Bill Richardson...' However, Giuffre did not "
    "provide specific details of encounters with Mitchell comparable to her descriptions "
    "of interactions with Prince Andrew or Richardson."
    "\n\n"
    "MITCHELL'S DENIALS: Mitchell has categorically denied the allegations, stating in "
    "2019 that he 'never met, spoke with, or had any contact of any kind with Ms. "
    "Giuffre or with any underage women.' In 2026, he said he 'declined or deflected' "
    "the 'small number of invitations' from Epstein. Despite this, the US-Ireland "
    "Alliance removed his name from the Mitchell Scholarship program, and the "
    "University of Maine considered renaming programs bearing his name."
    "\n\n"
    "EVIDENCE ASSESSMENT: Mitchell appears in Epstein's contacts and is named in the "
    "Giuffre deposition, but the evidence of direct personal misconduct is less "
    "specific than for other named individuals. The Epstein files released in 2025-2026 "
    "revealed continued contact between Epstein and Mitchell after Epstein's conviction, "
    "which Mitchell has disputed."
)

_DESC_KISSINGER = (
    "Heinz Alfred 'Henry' Kissinger (1923-2023). German-born American diplomat who "
    "served as National Security Advisor (1969-1975) and Secretary of State (1973-1977) "
    "under Presidents Nixon and Ford — the only person to hold both positions "
    "simultaneously. Nobel Peace Prize laureate (1973) for Vietnam negotiations. "
    "Emigrated from Nazi Germany in 1938 as a Jewish refugee."
    "\n\n"
    "INTELLIGENCE & COVERT OPERATIONS: As NSA, Kissinger chaired the '40 Committee' "
    "which oversaw CIA covert operations worldwide. Declassified documents show he "
    "supervised 'Track II' — the CIA operation to foment a coup in Chile that led to "
    "the assassination of General Rene Schneider and the overthrow of Salvador Allende "
    "(1973). He authorized Indonesia's invasion of East Timor (1975, ~200,000 deaths). "
    "Directed secret bombing of Cambodia. Supported Argentina's Dirty War and Pakistan "
    "during the Bangladesh genocide."
    "\n\n"
    "KISSINGER ASSOCIATES: Founded his geopolitical consulting firm in 1982. Members "
    "included Brent Scowcroft, L. Paul Bremer, Lawrence Eagleburger, Timothy Geithner, "
    "and Bill Richardson (Senior Managing Director). The firm connected corporate clients "
    "to government power globally. Joshua Cooper Ramo, a Kissinger Associates executive, "
    "appears in Epstein's private calendar for a scheduled meeting."
    "\n\n"
    "EPSTEIN CONNECTION: Kissinger appears in Epstein's black book (page 31, with 2 phone "
    "numbers and 2 addresses). Kissinger Associates executives appear in Epstein's "
    "private calendar. Kissinger sat on the board of Hollinger International alongside "
    "Les Wexner. Virginia Giuffre's forthcoming autobiography reportedly implicates "
    "Kissinger, with an 'intense legal fight' to keep his name out. However, there is "
    "no public evidence of Kissinger flying on Epstein's planes or visiting his properties. "
    "The connection appears institutional rather than personal — through overlapping "
    "board memberships, elite social networks, and the consulting firm. Died November 29, "
    "2023, at age 100."
)

_DESC_SUMMERS = (
    "Lawrence Henry Summers (born 1954). Economist who served as Secretary of the "
    "Treasury (1999-2001) under Clinton, President of Harvard University (2001-2006), "
    "and Director of the National Economic Council (2009-2010) under Obama. One of the "
    "youngest tenured professors in Harvard's history at age 28. Won the John Bates "
    "Clark Medal in 1993."
    "\n\n"
    "EPSTEIN-HARVARD NEXUS: As Harvard President, Summers approved Epstein's $6.5 "
    "million donation in 2003 to found the Program for Evolutionary Dynamics. Epstein "
    "pledged up to $25 million during Summers' tenure. Epstein was given a personal "
    "office at Harvard and appointed as a 'visiting fellow' in 2005. Flight logs show "
    "Summers first flew on Epstein's aircraft in September 1998 (Aspen to DC), with "
    "additional flights in April 2004 and September 2005."
    "\n\n"
    "HONEYMOON ON EPSTEIN'S ISLAND: In December 2005, days after their wedding, "
    "Summers and his wife Elisa New boarded Epstein's plane from Bedford, Massachusetts, "
    "to St. Thomas, USVI — gateway to Little Saint James — with Ghislaine Maxwell "
    "listed on the same manifest. This flight occurred after Epstein was already under "
    "investigation by Palm Beach police."
    "\n\n"
    "CONTINUED RELATIONSHIP: Epstein's schedules show planned meetings with Summers "
    "throughout 2011-2014. House Oversight Committee documents revealed thousands of "
    "emails between Summers and Epstein from 2013 to 2019. Epstein also donated "
    "$110,000 to a nonprofit tied to Summers' wife and helped broker a $500,000 "
    "donation from Leon Black to her poetry foundation. In November 2025, Summers "
    "declared himself 'deeply ashamed,' took leave from Harvard, resigned from the "
    "OpenAI board, and stepped away from public life as Harvard launched a new "
    "investigation into Epstein ties."
)

_DESC_GIULIANI = (
    "Rudolph William Louis Giuliani (born 1944). Former U.S. Attorney for the Southern "
    "District of New York (1983-1989) and Mayor of New York City (1994-2001). Known as "
    "'America's Mayor' after 9/11. Later served as Donald Trump's personal attorney "
    "(2018-2023)."
    "\n\n"
    "COMMISSION TRIAL — DESTROYING THE ITALIAN MOB: As SDNY U.S. Attorney, Giuliani "
    "led the landmark 1985-1986 Mafia Commission Trial (US v. Salerno et al.), using "
    "RICO to convict the bosses of all Five Families of the New York Mafia. Eight "
    "defendants received sentences up to 100 years. This prosecution effectively "
    "decapitated the Italian-American organized crime structure in New York. Giuliani "
    "also successfully prosecuted Stanley Friedman, a close associate of attorney Roy "
    "Cohn and client of Cohn's law firm."
    "\n\n"
    "STRUCTURAL OBSERVATION: Giuliani's prosecutions devastated the Italian Mafia but "
    "created a vacuum that was filled by Russian/Israeli organized crime networks "
    "during the 1990s — the same networks later connected to figures like Felix Sater "
    "and Bayrock Group, which operated out of Trump Tower. This pattern — the selective "
    "destruction of one crime network enabling another — is noted by organized crime "
    "historians, though whether this was intentional or incidental remains debated."
    "\n\n"
    "TRUMP ORBIT: After decades in public life, Giuliani became Trump's personal "
    "attorney, defending him during the Mueller investigation and the first impeachment. "
    "His firm Bracewell & Giuliani had business connections to Kazakhstan, overlapping "
    "with Bayrock Group's network. In 2023, Giuliani was himself indicted under Georgia's "
    "RICO statute for efforts to overturn the 2020 election — the same legal tool he "
    "had pioneered against the mob. He does not appear in Epstein's flight logs or "
    "contacts."
)

_DESC_BERGER = (
    "Samuel Richard 'Sandy' Berger (1945-2015). Democratic attorney and political "
    "operative who served as Deputy National Security Advisor (1993-1997) and National "
    "Security Advisor (1997-2001) under President Clinton. Born in Millerton, New York. "
    "Cornell University BA (1967), Harvard Law JD (1971). Co-founded the Albright "
    "Stonebridge Group in 2001."
    "\n\n"
    "NATIONAL ARCHIVES THEFT: In 2003, while preparing to testify before the 9/11 "
    "Commission on behalf of the Clinton administration, Berger was caught removing "
    "classified documents from a National Archives reading room — physically stuffing "
    "papers into his pants and socks. The stolen materials were five copies of a single "
    "report by Richard Clarke assessing the Clinton administration's handling of the "
    "2000 millennium bomb plot. Berger destroyed three copies by cutting them with "
    "scissors and placing them in trash."
    "\n\n"
    "LEGAL CONSEQUENCES: In April 2005, Berger pleaded guilty to a misdemeanor charge "
    "of unauthorized removal and retention of classified material. He was fined $50,000, "
    "sentenced to 2 years probation and 100 hours community service, stripped of his "
    "security clearance for 3 years, and disbarred. The question of what exactly was in "
    "those documents — and whether Berger was protecting the Clinton administration from "
    "9/11-related revelations — has never been fully resolved."
    "\n\n"
    "EPSTEIN CONNECTION: Claims from conservative media sources place Berger on an "
    "Epstein flight from St. Thomas to New Jersey in September 2005. However, this "
    "claim has not been independently verified by major news outlets or official court "
    "records reviewed for this database. The connection, if any, remains at the "
    "speculative tier pending verification. Berger died of cancer on December 2, 2015, "
    "at age 70."
)

ENTITIES = [
    # ---- People (7) ----
    {
        "name": "Prince Andrew",
        "entity_type": "person",
        "description": _DESC_PRINCE_ANDREW,
        "aliases": "Andrew Mountbatten-Windsor, Duke of York",
        "metadata": {
            "birth_date": "1960-02-19",
            "nationality": "British",
            "status": "alive",
        },
    },
    {
        "name": "Bill Richardson",
        "entity_type": "person",
        "description": _DESC_RICHARDSON,
        "aliases": "William Blaine Richardson III",
        "metadata": {
            "birth_date": "1947-11-15",
            "death_date": "2023-09-01",
            "nationality": "American",
            "status": "deceased",
        },
    },
    {
        "name": "George Mitchell",
        "entity_type": "person",
        "description": _DESC_MITCHELL,
        "aliases": "George John Mitchell Jr.",
        "metadata": {
            "birth_date": "1933-08-20",
            "nationality": "American",
            "status": "alive",
        },
    },
    {
        "name": "Henry Kissinger",
        "entity_type": "person",
        "description": _DESC_KISSINGER,
        "aliases": "Heinz Alfred Kissinger",
        "metadata": {
            "birth_date": "1923-05-27",
            "death_date": "2023-11-29",
            "nationality": "American",
            "status": "deceased",
        },
    },
    {
        "name": "Larry Summers",
        "entity_type": "person",
        "description": _DESC_SUMMERS,
        "aliases": "Lawrence Henry Summers",
        "metadata": {
            "birth_date": "1954-11-30",
            "nationality": "American",
            "status": "alive",
        },
    },
    {
        "name": "Rudy Giuliani",
        "entity_type": "person",
        "description": _DESC_GIULIANI,
        "aliases": "Rudolph William Louis Giuliani, America's Mayor",
        "metadata": {
            "birth_date": "1944-05-28",
            "nationality": "American",
            "status": "alive",
        },
    },
    {
        "name": "Sandy Berger",
        "entity_type": "person",
        "description": _DESC_BERGER,
        "aliases": "Samuel Richard Berger",
        "metadata": {
            "birth_date": "1945-10-28",
            "death_date": "2015-12-02",
            "nationality": "American",
            "status": "deceased",
        },
    },
    # ---- Organizations (3) ----
    {
        "name": "Kissinger Associates",
        "entity_type": "organization",
        "description": (
            "International geopolitical consulting firm founded by Henry Kissinger "
            "in 1982 and headquartered in New York City. The firm provided strategic "
            "advisory services to multinational corporations navigating global political "
            "risks. Key members included Brent Scowcroft (president, former NSA), "
            "Lawrence Eagleburger (former Secretary of State), L. Paul Bremer (former "
            "Iraq reconstruction director), Timothy Geithner (later Treasury Secretary), "
            "and Bill Richardson (Senior Managing Director from 2001). In 1999, expanded "
            "as Kissinger McLarty Associates with Mack McLarty (Clinton's Chief of Staff). "
            "Joshua Cooper Ramo, vice chairman and co-CEO, appears in Epstein's private "
            "calendar for a scheduled meeting. Kissinger ran the firm until his death in "
            "2023. The firm represents a nexus of government-to-private-sector power "
            "conversion, where former officials monetize access and relationships."
        ),
        "aliases": "Kissinger McLarty Associates, KA",
        "metadata": {"founded": 1982, "status": "active"},
    },
    {
        "name": "Hollinger International",
        "entity_type": "organization",
        "description": (
            "Media holding company controlled by Conrad Black that owned the Daily "
            "Telegraph, Chicago Sun-Times, and the Jerusalem Post. Its board of directors "
            "included Henry Kissinger and Les Wexner. The International Advisory Board "
            "was chaired by Margaret Thatcher and included Richard Perle and William F. "
            "Buckley Jr. The overlap of Kissinger and Wexner on this board is significant "
            "because it places a key Epstein network figure (Wexner) in direct corporate "
            "governance alongside a central establishment power broker (Kissinger). "
            "Conrad Black was later convicted of fraud and obstruction of justice (2007). "
            "The company represents one node in the overlapping board memberships that "
            "characterized elite network connections in this era."
        ),
        "aliases": "Hollinger Inc.",
        "metadata": {"status": "defunct"},
    },
    # ---- Events (2) ----
    {
        "name": "Prince Andrew Civil Settlement (2022)",
        "entity_type": "event",
        "description": (
            "On February 15, 2022, Prince Andrew and Virginia Giuffre reached an "
            "out-of-court settlement in the civil lawsuit (Giuffre v. Prince Andrew, "
            "SDNY) that had accused Andrew of sexually abusing Giuffre when she was "
            "a minor. The financial terms were undisclosed, with media estimates "
            "ranging from 3M to 12M GBP. Andrew made no admission of liability but "
            "acknowledged 'that Jeffrey Epstein trafficked countless young girls over "
            "many years' and stated he 'regrets his association with Epstein.' Andrew "
            "also pledged a 'substantial donation' to Giuffre's charity for victims' "
            "rights. In January 2022, Queen Elizabeth had stripped Andrew of military "
            "affiliations and royal patronages. The settlement effectively ended the "
            "civil proceedings but did not prevent the later criminal investigation."
        ),
        "aliases": "Giuffre v. Prince Andrew Settlement",
        "metadata": {"date": "2022-02-15"},
    },
    {
        "name": "Berger Archives Theft (2003)",
        "entity_type": "event",
        "description": (
            "In October 2003, while preparing to testify before the 9/11 Commission "
            "on behalf of the Clinton administration, National Security Advisor Sandy "
            "Berger was caught removing classified documents from the National Archives. "
            "He physically stuffed papers into his pants and socks. The stolen materials "
            "were five copies of a report by Richard Clarke on the Clinton administration's "
            "handling of the 2000 millennium bomb plots. Berger destroyed three copies "
            "by cutting them with scissors. He pled guilty in 2005 to a misdemeanor, "
            "was fined $50,000, sentenced to probation, and stripped of his security "
            "clearance. The event is significant because it suggests the Clinton "
            "administration had something in its counter-terrorism record worth "
            "destroying prior to the 9/11 Commission's review."
        ),
        "aliases": "Sandy Berger Archives Scandal",
        "metadata": {"date": "2003-10-01"},
    },
]


# ============================================================
# RELATIONSHIPS — 35 new connections
# ============================================================

RELATIONSHIPS = [
    # ---- Prince Andrew relationships ----
    {
        "source": "Prince Andrew",
        "target": "Jeffrey Epstein",
        "type": "associate_of",
        "tier": "documented",
        "desc": "Met Epstein in 1999 through Ghislaine Maxwell. Flight logs document travel on Epstein's aircraft. Visited Epstein's residences including post-2008 conviction. Photographed with Epstein in New York in 2010.",
        "sources": [30, 56, 70],
    },
    {
        "source": "Prince Andrew",
        "target": "Ghislaine Maxwell",
        "type": "associate_of",
        "tier": "documented",
        "desc": "Longstanding friendship dating to Maxwell's Oxford years. Reportedly intermittent lovers in the early 2000s. Maxwell introduced Andrew to Epstein. They were frequently photographed together at royal events, Ascot, and society functions.",
        "sources": [56, 73],
    },
    {
        "source": "Ghislaine Maxwell",
        "target": "Prince Andrew",
        "type": "introduced_by",
        "tier": "documented",
        "desc": "Maxwell introduced Prince Andrew to Jeffrey Epstein in 1999. Andrew confirmed this in his BBC Newsnight interview.",
        "sources": [56, 73],
    },
    {
        "source": "Prince Andrew",
        "target": "Little Saint James",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Giuffre alleged sexual abuse occurred on Epstein's private island. Flight logs show travel to St. Thomas, the gateway to Little Saint James.",
        "sources": [29, 30, 56],
    },
    {
        "source": "Prince Andrew",
        "target": "Prince Andrew Civil Settlement (2022)",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Settled Virginia Giuffre's civil lawsuit for undisclosed sum (reported 3M-12M GBP) with no admission of liability in February 2022.",
        "sources": [56],
    },

    # ---- Bill Richardson relationships ----
    {
        "source": "Bill Richardson",
        "target": "Jeffrey Epstein",
        "type": "associate_of",
        "tier": "documented",
        "desc": "DOJ files show Richardson arranged at least 9 meetings with Epstein between 2010-2018, years after Epstein's conviction. Epstein donated $50K to Richardson's 2002 and 2006 gubernatorial campaigns. Richardson visited Epstein's private island.",
        "sources": [57, 61],
    },
    {
        "source": "Bill Richardson",
        "target": "Zorro Ranch",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Richardson visited Epstein's Zorro Ranch in New Mexico. Giuffre testified in 2016 deposition that Maxwell directed her to provide sexual services to Richardson at the ranch.",
        "sources": [29, 61],
    },
    {
        "source": "Jeffrey Epstein",
        "target": "Zorro Ranch",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Epstein owned the 7,500-acre Zorro Ranch near Stanley, New Mexico. The property served as one of his primary residences and a site where trafficking allegedly occurred.",
        "sources": [57, 61],
    },
    {
        "source": "Bill Richardson",
        "target": "Kissinger Associates",
        "type": "employed_by",
        "tier": "documented",
        "desc": "Richardson served as Senior Managing Director at Kissinger McLarty Associates beginning in 2001, after leaving the Clinton administration.",
        "sources": [74],
    },
    {
        "source": "Bill Richardson",
        "target": "Bill Clinton",
        "type": "associate_of",
        "tier": "documented",
        "desc": "Served in Clinton administration as UN Ambassador (1997-1998) and Secretary of Energy (1998-2001). Part of Clinton's political network in the Democratic Party.",
        "sources": [61],
    },

    # ---- George Mitchell relationships ----
    {
        "source": "George Mitchell",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Named in Giuffre's 2016 deposition as someone Epstein and Maxwell directed her toward. Epstein files released in 2025-2026 revealed continued contact after conviction. Mitchell denies all allegations and says he 'declined or deflected' Epstein invitations.",
        "sources": [29, 71, 72],
    },
    {
        "source": "George Mitchell",
        "target": "Bill Clinton",
        "type": "associate_of",
        "tier": "documented",
        "desc": "As Senate Majority Leader (1989-1995), Mitchell was a key Clinton legislative ally. Later served as Clinton's Special Envoy for Northern Ireland peace process.",
        "sources": [72],
    },

    # ---- Henry Kissinger relationships ----
    {
        "source": "Henry Kissinger",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Kissinger listed in Epstein's black book (page 31, 2 phone numbers, 2 addresses). Kissinger Associates executive appears in Epstein's private calendar. No evidence of flights on Epstein's planes or property visits. Connection appears institutional rather than personal.",
        "sources": [67, 68],
    },
    {
        "source": "Henry Kissinger",
        "target": "Kissinger Associates",
        "type": "member_of",
        "tier": "documented",
        "desc": "Founded and ran Kissinger Associates from 1982 until his death in 2023. The firm was the primary vehicle for converting government power into private consulting influence.",
        "sources": [74],
    },
    {
        "source": "Henry Kissinger",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "As NSA, chaired the 40 Committee overseeing CIA covert operations. Supervised Track II (Chile coup/Schneider assassination), authorized Indonesia's East Timor invasion, directed Cambodia bombing. Declassified NSA documents confirm operational control.",
        "sources": [60, 69, 75],
    },
    {
        "source": "Henry Kissinger",
        "target": "Les Wexner",
        "type": "associate_of",
        "tier": "documented",
        "desc": "Both served on the Board of Directors of Hollinger International (Conrad Black's media company) until 2002. This placed a key Epstein network figure in direct corporate governance alongside a central establishment power broker.",
        "sources": [11, 74],
    },
    {
        "source": "Henry Kissinger",
        "target": "Hollinger International",
        "type": "member_of",
        "tier": "documented",
        "desc": "Served on the board and International Advisory Board of Hollinger International alongside Les Wexner, Margaret Thatcher, Richard Perle, and William F. Buckley Jr.",
        "sources": [74],
    },
    {
        "source": "Les Wexner",
        "target": "Hollinger International",
        "type": "member_of",
        "tier": "documented",
        "desc": "Served on the Board of Directors of Hollinger International, Conrad Black's media empire, alongside Henry Kissinger.",
        "sources": [74],
    },

    # ---- Larry Summers relationships ----
    {
        "source": "Larry Summers",
        "target": "Jeffrey Epstein",
        "type": "associate_of",
        "tier": "documented",
        "desc": "Flight logs show Summers flew on Epstein's planes from 1998 through 2005. Approved Epstein's $6.5M Harvard donation. Thousands of emails exchanged 2013-2019 per House Oversight. Honeymooned on Epstein's island in December 2005 with Ghislaine Maxwell on the manifest.",
        "sources": [30, 62, 63, 64],
    },
    {
        "source": "Larry Summers",
        "target": "Ghislaine Maxwell",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Maxwell was listed on the same flight manifest as Summers and his wife during their December 2005 honeymoon trip to Epstein's island in St. Thomas.",
        "sources": [30, 62],
    },
    {
        "source": "Larry Summers",
        "target": "Little Saint James",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Flight logs show Summers and his wife flew on Epstein's plane from Bedford, MA to St. Thomas (Little Saint James gateway) in December 2005 for their honeymoon, with Maxwell on the same flight.",
        "sources": [30, 62],
    },
    {
        "source": "Larry Summers",
        "target": "Leon Black",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Epstein brokered a $500,000 donation from Leon Black to a poetry foundation run by Summers' wife Elisa New, per Boston Globe reporting on released emails.",
        "sources": [63],
    },
    {
        "source": "Larry Summers",
        "target": "Bill Clinton",
        "type": "employed_by",
        "tier": "documented",
        "desc": "Served as Secretary of the Treasury (1999-2001) in the Clinton administration, after serving as Under-Secretary (1993-1995) and Deputy Secretary (1995-1999).",
        "sources": [64],
    },

    # ---- Rudy Giuliani relationships ----
    {
        "source": "Rudy Giuliani",
        "target": "The Commission",
        "type": "connected_to",
        "tier": "documented",
        "desc": "As U.S. Attorney for SDNY, led the Mafia Commission Trial (1985-1986) that convicted bosses of all Five Families under RICO. Eight defendants received sentences up to 100 years. Effectively destroyed the Italian-American organized crime command structure.",
        "sources": [41, 65, 66],
    },
    {
        "source": "Rudy Giuliani",
        "target": "Commission Trial (1986)",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Giuliani personally led the prosecution using RICO statutes, indicting 11 organized crime figures in what became the landmark case against the Mafia's ruling body.",
        "sources": [41, 65],
    },
    {
        "source": "Rudy Giuliani",
        "target": "Donald Trump",
        "type": "advisor_to",
        "tier": "documented",
        "desc": "Served as Trump's personal attorney from approximately 2018-2023, defending Trump during the Mueller investigation, first impeachment, and efforts to overturn the 2020 election. Later indicted under Georgia RICO statute.",
        "sources": [66],
    },
    {
        "source": "Rudy Giuliani",
        "target": "Roy Cohn",
        "type": "connected_to",
        "tier": "credible",
        "desc": "As SDNY U.S. Attorney, Giuliani prosecuted Stanley Friedman, a close associate of Roy Cohn. A former colleague noted the irony: 'If you had told me that Rudy would be doing dirty work for Roy Cohn's protege, I wouldn't have been able to fathom it.'",
        "sources": [66],
    },
    {
        "source": "Rudy Giuliani",
        "target": "Felix Sater",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Giuliani's law firm Bracewell & Giuliani opened an office in Kazakhstan in 2007 and provided legal services to a Kazakh couple with deep ties to Sater and Bayrock Group. Both operated in overlapping Trump Organization business networks.",
        "sources": [40],
    },

    # ---- Sandy Berger relationships ----
    {
        "source": "Sandy Berger",
        "target": "Bill Clinton",
        "type": "advisor_to",
        "tier": "documented",
        "desc": "Served as Clinton's Deputy National Security Advisor (1993-1997) and National Security Advisor (1997-2001). One of Clinton's closest foreign policy advisors.",
        "sources": [58],
    },
    {
        "source": "Sandy Berger",
        "target": "Berger Archives Theft (2003)",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Berger removed and destroyed classified documents from the National Archives in 2003 while preparing to testify before the 9/11 Commission. Pleaded guilty to misdemeanor in 2005.",
        "sources": [58],
    },
    {
        "source": "Sandy Berger",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "speculative",
        "desc": "Claims from conservative media place Berger on an Epstein flight from St. Thomas to New Jersey in September 2005. This has not been independently verified by major outlets or official court records. Connection, if any, is unverified.",
        "sources": [57],
    },
    {
        "source": "Sandy Berger",
        "target": "DOJ",
        "type": "connected_to",
        "tier": "documented",
        "desc": "DOJ investigated and prosecuted Berger for unauthorized removal of classified material from the National Archives. Pleaded guilty 2005, fined $50,000, stripped of security clearance.",
        "sources": [58],
    },

    # ---- Cross-network connections ----
    {
        "source": "Kissinger Associates",
        "target": "CIA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Founded by former NSA/SecState who oversaw CIA covert ops. Staffed by former government officials with intelligence community ties. Brent Scowcroft (president) was former NSA. L. Paul Bremer was managing director. The firm represents the revolving door between intelligence oversight and private consulting.",
        "sources": [74, 75],
    },
    {
        "source": "Bill Richardson",
        "target": "Henry Kissinger",
        "type": "employed_by",
        "tier": "documented",
        "desc": "Richardson served as Senior Managing Director of Kissinger McLarty Associates from 2001. Both men are also connected to Epstein — Kissinger through his black book listing and board overlap with Wexner; Richardson through direct visits and campaign donations.",
        "sources": [74],
    },
    {
        "source": "Zorro Ranch",
        "target": "Little Saint James",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both properties served as Epstein trafficking venues per victim testimony. Zorro Ranch functioned as the mainland counterpart to Little Saint James, providing geographic redundancy and political cover through state-level connections (Richardson as governor).",
        "sources": [29, 61],
    },
]


# ============================================================
# ENTITY-SOURCE LINKS
# ============================================================

ENTITY_SOURCES = {
    'Berger Archives Theft (2003)': [58],
    'Bill Richardson': [29, 57, 61, 74],
    'George Mitchell': [29, 71, 72],
    'Henry Kissinger': [60, 67, 68, 69, 74, 75],
    'Hollinger International': [74],
    'Kissinger Associates': [68, 74],
    'Larry Summers': [30, 62, 63, 64],
    'Prince Andrew': [29, 30, 56, 67, 70, 73],
    'Prince Andrew Civil Settlement (2022)': [56],
    'Rudy Giuliani': [41, 65, 66],
    'Sandy Berger': [57, 58],
}
