"""
Election Interference & Manipulation — Expansion layer for Intel Console.

Maps the infrastructure of election manipulation: electronic voting machine
vulnerabilities (Diebold/ES&S, Dominion, Smartmatic), data-driven psyops
(Cambridge Analytica/SCL Group), Russian interference operations (Internet
Research Agency), dark money pipelines (Citizens United ruling), and the
contested 2000 Florida recount that set the template for disputed elections.

This expansion tracks how elections are influenced through three vectors:
1. TECHNICAL: Proprietary voting machines with no audit trails, demonstrated
   vulnerabilities (Halderman academic research), and corporate consolidation
   of election infrastructure under a handful of companies.
2. INFORMATIONAL: Military-grade psychological operations adapted for civilian
   campaigns (SCL Group → Cambridge Analytica), social media manipulation
   (IRA troll farms, Facebook data harvesting), and micro-targeted propaganda.
3. STRUCTURAL: Legal frameworks that enable unlimited dark money (Citizens
   United v. FEC), voter suppression mechanisms, and the revolving door
   between campaign operatives and election administration.

Entities (19): People (Alexander Nix, Christopher Wylie, Clint Curtis,
Bev Harris, Robert Mercer, John Bolton), organizations (Cambridge Analytica,
SCL Group, Dominion Voting Systems, ES&S, Internet Research Agency,
Black Box Voting), events (Brooks Brothers Riot, Bush v. Gore, Citizens
United v. FEC, 2016 Russian Interference, Halderman Report), legislation
(Help America Vote Act), programs (Project Alamo).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], FBI [84], NSA [86], DOJ [89], Unit 8200 [israel],
  Mossad [88], GCHQ [tech_surveillance], FSB [russia],
  Facebook (referenced in text, not entity), Google (referenced in text),
  Twitter Files [media], Donald Trump [curated],
  George W. Bush [grove], Fox Corporation [media],
  Rudy Giuliani [political]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence

TIER NOTES:
  - Cambridge Analytica: DOCUMENTED. UK ICO investigation, Parliamentary inquiry,
    Wylie's sworn testimony, FTC consent decree against Facebook, SEC filings.
  - Russian interference: DOCUMENTED. Mueller Report (Vol. I), Senate Intelligence
    Committee Report (Vols. 1-5), DOJ indictments of IRA and GRU officers.
  - Voting machine vulnerabilities: DOCUMENTED. Halderman academic research (peer-
    reviewed), DEFCON Voting Village findings, EAC certification reports.
  - Citizens United: DOCUMENTED. Supreme Court ruling, FEC records, OpenSecrets data.
  - Brooks Brothers Riot: DOCUMENTED. Contemporary news coverage, participant
    identification, congressional staff payroll records.
  - Clint Curtis affidavit: CREDIBLE. Sworn testimony under oath, but allegations
    unverified by independent investigation. Curtis passed a polygraph.
  - SCL Group military contracts: CREDIBLE. Companies House filings, defence
    ministry confirmations, but classified contract details unavailable.
  - ES&S/Diebold corporate-political ties: CREDIBLE. FEC filings, investigative
    journalism (Bev Harris), but direct vote manipulation unproven at scale.
  - Project Alamo as psyop: INFERENCE. Documented digital operation, but
    characterization as military-grade psyop is analytical conclusion.
"""

# ============================================================
# SOURCES — IDs 1081-1110
# ============================================================

SOURCES = [
    # --- UK Parliamentary / Regulatory (Cambridge Analytica) ---
    {
        "id": 1081,
        "title": "UK House of Commons DCMS Committee — Disinformation and 'Fake News': Final Report (Feb 2019)",
        "url": "https://publications.parliament.uk/pa/cm201719/cmselect/cmcumeds/1791/1791.pdf",
        "source_type": "congressional",
        "year": 2019,
    },
    {
        "id": 1082,
        "title": "UK Information Commissioner's Office — Investigation into the use of data analytics in political campaigns (Nov 2018)",
        "url": "https://ico.org.uk/media/action-weve-taken/2260271/investigation-into-the-use-of-data-analytics-in-political-campaigns-final-20181105.pdf",
        "source_type": "government",
        "year": 2018,
    },
    {
        "id": 1083,
        "title": "Christopher Wylie — Testimony before UK DCMS Select Committee (March 2018)",
        "url": "https://www.parliamentlive.tv/Event/Index/4b0876c5-f867-445e-8c96-2628a82e5b7c",
        "source_type": "congressional",
        "year": 2018,
    },
    # --- Mueller / Senate Intelligence (Russian Interference) ---
    {
        "id": 1084,
        "title": "Mueller Report — Report on the Investigation into Russian Interference in the 2016 Presidential Election, Vol. I (March 2019)",
        "url": "https://www.justice.gov/archives/sco/file/1373816/dl",
        "source_type": "government",
        "year": 2019,
    },
    {
        "id": 1085,
        "title": "Senate Select Committee on Intelligence — Report on Russian Active Measures, Vol. 2: Russia's Use of Social Media (Oct 2019)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/documents/Report_Volume2__Russian_Use_of_Social_Media.pdf",
        "source_type": "congressional",
        "year": 2019,
    },
    {
        "id": 1086,
        "title": "DOJ — United States v. Internet Research Agency LLC et al., Indictment (D.D.C., Feb 2018)",
        "url": "https://www.justice.gov/file/1035477/dl",
        "source_type": "court",
        "year": 2018,
    },
    {
        "id": 1087,
        "title": "DOJ — United States v. Netyksho et al. (GRU Officers Indictment, July 2018)",
        "url": "https://www.justice.gov/file/1080281/dl",
        "source_type": "court",
        "year": 2018,
    },
    # --- Supreme Court / Legal (Citizens United, Bush v. Gore) ---
    {
        "id": 1088,
        "title": "Supreme Court of the United States — Citizens United v. Federal Election Commission, 558 U.S. 310 (Jan 2010)",
        "url": "https://www.supremecourt.gov/opinions/09pdf/08-205.pdf",
        "source_type": "court",
        "year": 2010,
    },
    {
        "id": 1089,
        "title": "Supreme Court of the United States — Bush v. Gore, 531 U.S. 98 (Dec 2000)",
        "url": "https://www.supremecourt.gov/opinions/00pdf/00-949.pdf",
        "source_type": "court",
        "year": 2000,
    },
    # --- Voting Machine Security (Academic / Government) ---
    {
        "id": 1090,
        "title": "J. Alex Halderman et al. — Security Analysis of the Dominion ImageCast X Ballot Marking Device (Curling v. Raffensperger expert report, July 2021)",
        "url": "https://www.courtlistener.com/docket/6467714/curling-v-raffensperger/",
        "source_type": "court",
        "year": 2021,
    },
    {
        "id": 1091,
        "title": "DEFCON Voting Village — Report on Cyber Vulnerabilities in U.S. Election Infrastructure (2017-2019)",
        "url": "https://www.defcon.org/images/defcon-25/DEF%20CON%2025%20voting%20village%20report.pdf",
        "source_type": "academic",
        "year": 2017,
    },
    {
        "id": 1092,
        "title": "Brennan Center for Justice — The Machinery of Democracy: Protecting Elections in an Electronic World (2006)",
        "url": "https://www.brennancenter.org/our-work/research-reports/machinery-democracy-protecting-elections-electronic-world",
        "source_type": "academic",
        "year": 2006,
    },
    {
        "id": 1093,
        "title": "Bev Harris — Black Box Voting: Ballot Tampering in the 21st Century (2004, investigative report and book)",
        "url": "https://blackboxvoting.org/",
        "source_type": "book",
        "year": 2004,
    },
    # --- Journalism (Cambridge Analytica / Election Manipulation) ---
    {
        "id": 1094,
        "title": "The Guardian / Observer — Revealed: 50 million Facebook profiles harvested for Cambridge Analytica (Carole Cadwalladr / Emma Graham-Harrison, March 2018)",
        "url": "https://www.theguardian.com/news/2018/mar/17/cambridge-analytica-facebook-influence-us-election",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 1095,
        "title": "The New York Times — How Trump Consultants Exploited the Facebook Data of Millions (March 2018)",
        "url": "https://www.nytimes.com/2018/03/17/us/politics/cambridge-analytica-trump-campaign.html",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 1096,
        "title": "Channel 4 News — Cambridge Analytica Uncovered: Secret filming reveals election tricks (Undercover investigation, March 2018)",
        "url": "https://www.channel4.com/news/cambridge-analytica-revealed-trumps-election-consultants-filmed-saying-they-use-bribes-and-sex-workers-to-entrap-politicians-investigation",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 1097,
        "title": "OpenSecrets — Outside Spending since Citizens United (Center for Responsive Politics, ongoing tracker)",
        "url": "https://www.opensecrets.org/outsidespending/",
        "source_type": "journalism",
        "year": 2024,
    },
    # --- Congressional / Government (HAVA, Election Administration) ---
    {
        "id": 1098,
        "title": "U.S. Congress — Help America Vote Act of 2002 (Pub.L. 107-252, 42 U.S.C. ch. 146)",
        "url": "https://www.congress.gov/bill/107th-congress/house-bill/3295",
        "source_type": "congressional",
        "year": 2002,
    },
    {
        "id": 1099,
        "title": "U.S. Election Assistance Commission — Voluntary Voting System Guidelines (VVSG 2.0, Feb 2021)",
        "url": "https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines",
        "source_type": "government",
        "year": 2021,
    },
    # --- Journalism (Brooks Brothers Riot / 2000 Florida) ---
    {
        "id": 1100,
        "title": "The Wall Street Journal — The 'Brooks Brothers Riot' of 2000: How GOP operatives halted the Miami-Dade recount (Nov 2000, republished 2020)",
        "url": "https://www.wsj.com/articles/SB975017426618299136",
        "source_type": "journalism",
        "year": 2000,
    },
    {
        "id": 1101,
        "title": "The New York Times — Examining the Vote: How Bush Took Florida (July 2001, consortium recount analysis)",
        "url": "https://www.nytimes.com/2001/11/12/us/examining-vote-overview-study-disputed-florida-ballots-finds-justices-did-not.html",
        "source_type": "journalism",
        "year": 2001,
    },
    # --- Clint Curtis / Vote Rigging Allegations ---
    {
        "id": 1102,
        "title": "Clint Curtis — Sworn Affidavit and Testimony before House Judiciary Committee Democrats (Dec 2004)",
        "url": "https://www.bradblog.com/Docs/CurtisAffidavit110504.pdf",
        "source_type": "congressional",
        "year": 2004,
    },
    # --- Cambridge Analytica / SCL Group Corporate ---
    {
        "id": 1103,
        "title": "UK Companies House — SCL Group Limited (Company No. 02458946) and Cambridge Analytica LLC filings",
        "url": "https://find-and-update.company-information.service.gov.uk/company/02458946",
        "source_type": "government",
        "year": 2018,
    },
    {
        "id": 1104,
        "title": "Jane Mayer — Dark Money: The Hidden History of the Billionaires Behind the Rise of the Radical Right (Doubleday, 2016)",
        "url": "https://www.penguinrandomhouse.com/books/215462/dark-money-by-jane-mayer/",
        "source_type": "book",
        "year": 2016,
    },
    # --- FEC / Campaign Finance ---
    {
        "id": 1105,
        "title": "Federal Election Commission — Advisory Opinions and Enforcement Actions re: Super PACs post-Citizens United",
        "url": "https://www.fec.gov/data/legal/advisory-opinions/",
        "source_type": "government",
        "year": 2010,
    },
    # --- Project Alamo ---
    {
        "id": 1106,
        "title": "Bloomberg Businessweek — Inside the Trump Bunker, With Days to Go (Joshua Green, Oct 2016)",
        "url": "https://www.bloomberg.com/news/articles/2016-10-27/inside-the-trump-bunker-with-12-days-to-go",
        "source_type": "journalism",
        "year": 2016,
    },
    {
        "id": 1107,
        "title": "Channel 4 News — Revealed: Trump campaign's unprecedented data operation (Sept 2020, leaked database analysis)",
        "url": "https://www.channel4.com/news/revealed-trump-campaign-strategy-to-deter-millions-of-black-americans-from-voting-in-2016",
        "source_type": "journalism",
        "year": 2020,
    },
    # --- ES&S / Diebold ---
    {
        "id": 1108,
        "title": "The New Yorker — Can Our Ballots Be Hacked? (Sue Halpern, Nov 2018)",
        "url": "https://www.newyorker.com/magazine/2018/11/05/how-voting-machine-lobbyists-undermine-the-democratic-process",
        "source_type": "journalism",
        "year": 2018,
    },
    # --- John Bolton / NSA ---
    {
        "id": 1109,
        "title": "Bolton PAC — FEC filings for John Bolton Super PAC and Cambridge Analytica consulting contracts",
        "url": "https://www.fec.gov/data/committee/C00542464/",
        "source_type": "government",
        "year": 2014,
    },
    # --- IRA / Russian Operations Detail ---
    {
        "id": 1110,
        "title": "New Knowledge / Oxford Internet Institute — The Tactics & Tropes of the Internet Research Agency (Senate Intelligence Committee commissioned report, Dec 2018)",
        "url": "https://digitalcommons.unl.edu/senatedocs/2/",
        "source_type": "academic",
        "year": 2018,
    },
]


# ============================================================
# ENTITIES — 6 people + 6 organizations + 5 events + 1 legislation + 1 program = 19
# ============================================================

_DESC_NIX = (
    "Alexander James Ashburner Nix (born 1975). British businessman who served as CEO "
    "of Cambridge Analytica (2014-2018) and a director of its parent company, SCL Group. "
    "Educated at Eton College and the University of Manchester."
    "\n\n"
    "CAMBRIDGE ANALYTICA: Nix oversaw the company's operations combining psychographic "
    "profiling (based on the OCEAN personality model) with harvested Facebook data to "
    "build micro-targeting capabilities for political campaigns. Under his leadership, "
    "Cambridge Analytica worked on the 2016 Trump presidential campaign, the Ted Cruz "
    "primary campaign, and the Leave.EU Brexit referendum campaign. The company claimed "
    "it could identify 'persuadable' voters in swing states using personality profiles "
    "derived from Facebook data."
    "\n\n"
    "UNDERCOVER FOOTAGE: In March 2018, Channel 4 News broadcast secretly filmed footage "
    "of Nix boasting about using bribes, honey traps with sex workers, and fabricated "
    "scandals to entrap political opponents. Nix described these as services Cambridge "
    "Analytica could offer prospective clients. He also claimed the company had run "
    "'all of the [Trump] campaign's digital campaign, television campaign, and our data "
    "informed all the strategy.'"
    "\n\n"
    "DOWNFALL: Cambridge Analytica suspended Nix in March 2018, then fired him. He was "
    "found in contempt by the UK Parliament's DCMS Committee for providing misleading "
    "evidence about Cambridge Analytica's work with Facebook data. The UK Information "
    "Commissioner's Office fined Cambridge Analytica and referred Nix for criminal "
    "prosecution. He was banned from serving as a company director in the UK for seven "
    "years (2020). Nix later founded Auspex International, a 'due diligence' firm."
)

_DESC_WYLIE = (
    "Christopher Frederick Wylie (born 1989). Canadian data scientist and whistleblower "
    "who exposed Cambridge Analytica's harvesting of Facebook user data for political "
    "targeting. Born in Victoria, British Columbia. Studied law at the London School of "
    "Economics."
    "\n\n"
    "ROLE AT CAMBRIDGE ANALYTICA: Wylie joined SCL Group in 2013 and was instrumental "
    "in creating the research program that became Cambridge Analytica. He helped design "
    "the psychographic profiling methodology, working with Cambridge University academic "
    "Aleksandr Kogan to build the 'thisisyourdigitallife' Facebook app that harvested "
    "data from approximately 87 million Facebook profiles. Users who installed the app "
    "unwittingly gave access to their friends' data as well, under Facebook's API rules "
    "at the time."
    "\n\n"
    "WHISTLEBLOWING: Wylie left Cambridge Analytica in 2014 and went public in March "
    "2018, providing internal documents and testimony to The Guardian/Observer journalist "
    "Carole Cadwalladr, The New York Times, and the UK Parliament's DCMS Select Committee. "
    "His disclosures triggered: Facebook's $5 billion FTC fine (2019), the ICO "
    "investigation, Cambridge Analytica's bankruptcy and dissolution, criminal referrals "
    "for Alexander Nix, and Mark Zuckerberg's congressional testimony."
    "\n\n"
    "KEY INSIGHT: Wylie described SCL Group/Cambridge Analytica as 'Steve Bannon's "
    "psychological warfare mindfuck tool.' He testified that the company's real "
    "capability was not mere data analytics but the weaponization of personal data "
    "for information warfare — techniques adapted from SCL Group's military psyops "
    "work for NATO and defence ministries."
)

_DESC_CURTIS = (
    "Clinton Eugene Curtis (born c. 1958). American computer programmer and attorney "
    "who testified under oath in 2004 that he was asked to write vote-rigging software "
    "for electronic voting machines. Former employee of Yang Enterprises, Inc. (YEI), "
    "a NASA/DOT contractor in Oviedo, Florida."
    "\n\n"
    "SWORN AFFIDAVIT: In a sworn affidavit filed November 5, 2004, and subsequent "
    "testimony before Democratic members of the House Judiciary Committee on December "
    "13, 2004, Curtis stated that in October 2000, Florida Republican Congressman Tom "
    "Feeney — then Speaker-designate of the Florida House of Representatives — visited "
    "Yang Enterprises and asked Curtis to build a prototype program that could 'flip "
    "the vote 51-49 to whoever you wanted to win' on touch-screen voting machines. "
    "Curtis said he initially believed this was to detect fraud, but Feeney clarified "
    "he wanted the program to actually rig elections."
    "\n\n"
    "EVIDENCE ASSESSMENT: Curtis produced a working prototype demonstrating the concept "
    "was technically feasible. He passed a polygraph test administered by a former FBI "
    "agent. However, Tom Feeney denied the allegations, and no independent investigation "
    "corroborated Curtis's specific claims. The Florida Department of Law Enforcement "
    "investigated but did not file charges. Yang Enterprises' owner, Mrs. Li Woan Yang, "
    "was later convicted of tax fraud (2010) and espionage-related charges (attempting "
    "to pass NAVAIR data to Chinese agents)."
    "\n\n"
    "SIGNIFICANCE: Whether or not Feeney specifically commissioned vote-rigging software, "
    "Curtis's testimony demonstrated the technical feasibility of undetectable vote "
    "manipulation on proprietary electronic voting machines — a vulnerability that J. Alex "
    "Halderman and other computer scientists have repeatedly confirmed through independent "
    "academic research."
)

_DESC_HARRIS = (
    "Beverly Raye Harris (born 1956). American journalist, author, and founder of "
    "Black Box Voting, a nonprofit election watchdog organization. Pioneer of "
    "investigative reporting on electronic voting machine security."
    "\n\n"
    "BLACK BOX VOTING: In 2003, Harris discovered Diebold Election Systems' proprietary "
    "voting software source code on an unprotected public FTP server. Her analysis — "
    "later confirmed by computer scientists at Johns Hopkins and Rice University — "
    "revealed fundamental security flaws: no encryption on ballot data, easily guessable "
    "passwords (often '1111'), Microsoft Access databases that could be edited without "
    "audit trail detection, and no hash verification on executables."
    "\n\n"
    "BOOK AND RESEARCH: Harris's 2004 book 'Black Box Voting: Ballot Tampering in the "
    "21st Century' documented the corporate consolidation of American election "
    "infrastructure. She traced how a small number of companies — Diebold, ES&S, and "
    "Sequoia Voting Systems — came to control vote counting for the majority of American "
    "jurisdictions, with proprietary code exempt from public inspection under trade "
    "secret protections."
    "\n\n"
    "KEY FINDINGS: Harris documented that Diebold CEO Walden O'Dell was a major "
    "Republican fundraiser who wrote in a 2003 letter that he was 'committed to helping "
    "Ohio deliver its electoral votes to the president' — while his company manufactured "
    "and maintained Ohio's voting machines. She also revealed revolving door connections "
    "between ES&S executives and elected officials, including Chuck Hagel, who had been "
    "chairman of American Information Systems (later ES&S) before winning his Nebraska "
    "Senate race on machines his former company manufactured."
)

_DESC_MERCER = (
    "Robert Leroy Mercer (born 1946). American computer scientist and billionaire hedge "
    "fund manager. Co-CEO of Renaissance Technologies (with Peter Brown) from 2010 until "
    "his retirement in 2017. Known for pioneering computational linguistics and AI-based "
    "trading strategies at Renaissance's Medallion Fund."
    "\n\n"
    "POLITICAL FUNDING: Mercer became one of the most consequential political donors in "
    "American history. Through the Mercer Family Foundation and personal contributions, "
    "he funded: Cambridge Analytica ($15 million investment, with his daughter Rebekah "
    "on the board), Breitbart News ($10 million), the Government Accountability Institute "
    "(GAI, which produced the 'Clinton Cash' research), and multiple Super PACs supporting "
    "Ted Cruz and later Donald Trump."
    "\n\n"
    "BANNON-MERCER AXIS: Mercer's chief political operative was Steve Bannon, who sat "
    "on the boards of Cambridge Analytica, Breitbart, and GAI simultaneously. Bannon "
    "served as Mercer's conduit between conservative media, data analytics, and the Trump "
    "campaign. When Cambridge Analytica collapsed, Mercer's $15 million investment was "
    "reportedly recycled into successor firms (Emerdata, then Data Propria, later Auspex "
    "International under Alexander Nix)."
    "\n\n"
    "JOHN BOLTON: Mercer's Super PAC also funded John Bolton's PAC, which hired Cambridge "
    "Analytica for psychographic targeting before Bolton joined the Trump administration "
    "as National Security Advisor (2018-2019). FEC filings show Bolton's PAC paid Cambridge "
    "Analytica approximately $1.2 million for data services."
    "\n\n"
    "PATTERN: Mercer represents the post-Citizens United model of political influence — "
    "unlimited funds flowing through PACs and nonprofits to build an integrated media, "
    "data, and campaign infrastructure outside official party structures. Renaissance "
    "Technologies employees collectively gave more to political campaigns than employees "
    "of any other hedge fund."
)

_DESC_BOLTON = (
    "John Robert Bolton (born 1948). American attorney, diplomat, and Republican foreign "
    "policy hawk. Served as U.S. Ambassador to the United Nations (2005-2006, recess "
    "appointment), Under Secretary of State for Arms Control (2001-2005), and National "
    "Security Advisor (2018-2019)."
    "\n\n"
    "CAMBRIDGE ANALYTICA CONNECTION: Bolton's Super PAC (The John Bolton Super PAC) hired "
    "Cambridge Analytica in 2014 for psychographic voter-targeting. FEC filings show "
    "approximately $1.2 million in payments. Bolton's PAC was one of Cambridge Analytica's "
    "earliest American political clients, predating the Trump campaign. Robert Mercer was "
    "a major donor to both Bolton's PAC and Cambridge Analytica itself."
    "\n\n"
    "NEOCONSERVATIVE NEXUS: Bolton was a signatory to the Project for the New American "
    "Century (PNAC) founding statement and a key advocate for the Iraq War. His career "
    "spans the intersection of neoconservative foreign policy ideology, the Republican "
    "donor class (Mercer, Adelson), and data-driven political operations. As NSA under "
    "Trump, he pushed for regime change in Iran and Venezuela, following the PNAC playbook."
    "\n\n"
    "ELECTION RELEVANCE: Bolton's use of Cambridge Analytica demonstrates that the "
    "psychographic targeting infrastructure was not unique to the Trump campaign but was "
    "being deployed across the Republican establishment. The Bolton PAC's early adoption "
    "(2014) predates the 2016 election cycle and suggests systematic capability-building "
    "within the Republican donor network."
)

ENTITIES = [
    # ---- People (6) ----
    {
        "name": "Alexander Nix",
        "entity_type": "person",
        "description": _DESC_NIX,
        "aliases": "Alexander James Ashburner Nix",
        "metadata": {
            "birth_date": "1975",
            "nationality": "British",
            "status": "alive",
        },
    },
    {
        "name": "Christopher Wylie",
        "entity_type": "person",
        "description": _DESC_WYLIE,
        "aliases": "Chris Wylie",
        "metadata": {
            "birth_date": "1989-06-19",
            "nationality": "Canadian",
            "status": "alive",
        },
    },
    {
        "name": "Clint Curtis",
        "entity_type": "person",
        "description": _DESC_CURTIS,
        "aliases": "Clinton Eugene Curtis",
        "metadata": {
            "birth_date": "c. 1958",
            "nationality": "American",
            "status": "alive",
        },
    },
    {
        "name": "Bev Harris",
        "entity_type": "person",
        "description": _DESC_HARRIS,
        "aliases": "Beverly Raye Harris",
        "metadata": {
            "birth_date": "1956",
            "nationality": "American",
            "status": "alive",
        },
    },
    {
        "name": "Robert Mercer",
        "entity_type": "person",
        "description": _DESC_MERCER,
        "aliases": "Robert Leroy Mercer, Bob Mercer",
        "metadata": {
            "birth_date": "1946-07-11",
            "nationality": "American",
            "status": "alive",
        },
    },
    {
        "name": "John Bolton",
        "entity_type": "person",
        "description": _DESC_BOLTON,
        "aliases": "John Robert Bolton",
        "metadata": {
            "birth_date": "1948-11-20",
            "nationality": "American",
            "status": "alive",
        },
    },
    # ---- Organizations (7) ----
    {
        "name": "Cambridge Analytica",
        "entity_type": "organization",
        "description": (
            "British political consulting firm founded in 2013 as a subsidiary of SCL Group, "
            "funded by Robert Mercer ($15 million) and chaired by Steve Bannon. Headquartered "
            "in London with offices in New York and Washington, D.C. The company combined "
            "psychographic profiling using the OCEAN (Big Five) personality model with harvested "
            "Facebook user data to build micro-targeted political advertising capabilities."
            "\n\n"
            "FACEBOOK DATA HARVEST: Through Cambridge University academic Aleksandr Kogan's "
            "'thisisyourdigitallife' app, Cambridge Analytica harvested data from approximately "
            "87 million Facebook profiles. Users who installed the app unknowingly provided "
            "access to their entire friends list under Facebook's pre-2015 API permissions. "
            "This data was used to build psychographic profiles for political targeting — "
            "identifying 'persuadable' voters by personality type and serving them tailored "
            "political content."
            "\n\n"
            "CLIENTS: 2016 Trump presidential campaign (via Project Alamo), Ted Cruz primary "
            "campaign, John Bolton Super PAC, Leave.EU Brexit campaign (though the company "
            "denied direct Brexit work, whistleblower testimony and emails suggest otherwise), "
            "and political campaigns in Kenya, Nigeria, India, and other countries."
            "\n\n"
            "COLLAPSE: After The Guardian/Observer and NYT exposés in March 2018, followed by "
            "the Channel 4 undercover investigation, Cambridge Analytica filed for Chapter 7 "
            "bankruptcy on May 1, 2018. The UK ICO fined Facebook £500,000 (the maximum under "
            "pre-GDPR law). The FTC fined Facebook $5 billion (2019). Alexander Nix was banned "
            "as a director. Several successor entities (Emerdata, Data Propria) were formed by "
            "former Cambridge Analytica staff."
        ),
        "aliases": "CA, Cambridge Analytica LLC",
        "metadata": {"founded": 2013, "dissolved": 2018, "status": "defunct"},
    },
    {
        "name": "SCL Group",
        "entity_type": "organization",
        "description": (
            "Strategic Communication Laboratories Group Limited. British behavioural research "
            "and strategic communications company founded in 1993 by Nigel Oakes. Parent "
            "company of Cambridge Analytica. Registered at Companies House (No. 02458946)."
            "\n\n"
            "MILITARY PSYOPS: SCL Group's original business was military and defence "
            "psychological operations. The company held contracts with the UK Ministry of "
            "Defence, NATO, and various governments for 'influence operations' — using "
            "behavioural science to shape target populations' attitudes and behaviours. SCL "
            "developed what it called 'Target Audience Analysis' (TAA) methodology, combining "
            "demographic data with psychological profiling for military information campaigns."
            "\n\n"
            "TRANSITION TO POLITICS: Under Alexander Nix's leadership, SCL pivoted its military "
            "psyops capabilities to civilian political campaigns. Cambridge Analytica was the "
            "American-facing political division, while SCL Elections handled international work. "
            "Christopher Wylie described the relationship: 'Cambridge Analytica is an offshoot "
            "of a military contractor called SCL Group. SCL has been involved in elections "
            "around the world from the developing world. What Bannon wanted was an arsenal of "
            "weapons to wage a culture war.'"
            "\n\n"
            "DISSOLUTION: SCL Group entered administration on May 1, 2018, the same day as "
            "Cambridge Analytica. UK Companies House records show a web of related entities "
            "including SCL Elections, SCL Social, SCL Analytics, and SCL Defence. Successor "
            "entity Emerdata was incorporated in August 2017 — months before the public scandal "
            "— with Rebekah Mercer joining its board."
        ),
        "aliases": "Strategic Communication Laboratories, SCL Elections, SCL Defence",
        "metadata": {"founded": 1993, "dissolved": 2018, "status": "defunct"},
    },
    {
        "name": "Dominion Voting Systems",
        "entity_type": "organization",
        "description": (
            "Canadian-founded election technology company headquartered in Denver, Colorado, "
            "and Toronto, Ontario. Founded in 2002 by John Poulos and James Hoover. Provides "
            "electronic voting hardware and software (ImageCast systems) used in approximately "
            "28 U.S. states and over 40 countries."
            "\n\n"
            "SECURITY RESEARCH: In the Curling v. Raffensperger case (N.D. Ga.), University of "
            "Michigan computer science professor J. Alex Halderman conducted court-ordered "
            "security testing of Dominion's ImageCast X ballot marking device. His sealed expert "
            "report (July 2021, partially unsealed June 2023) identified nine critical "
            "vulnerabilities including: the ability to install malicious software, alter QR codes "
            "on printed ballots, and manipulate vote records — all without detection. Halderman "
            "emphasized these were 'exploitable vulnerabilities' in the software, not evidence "
            "of actual exploitation in any election."
            "\n\n"
            "FOX NEWS DEFAMATION: Dominion sued Fox Corporation for $1.6 billion over Fox's "
            "broadcasting of false claims that Dominion machines had switched votes in the 2020 "
            "presidential election. Fox settled for $787.5 million in April 2023 — the largest "
            "known defamation settlement in U.S. history. Discovery in the case revealed that "
            "Fox hosts and executives privately acknowledged the claims were false while "
            "broadcasting them."
            "\n\n"
            "DISTINCTION: The existence of documented software vulnerabilities (Halderman) is "
            "separate from conspiracy theories about actual vote-switching in specific elections. "
            "The former is peer-reviewed computer science; the latter is unproven allegation. "
            "This database records the documented vulnerabilities, not the unproven claims."
        ),
        "aliases": "Dominion, DVS",
        "metadata": {"founded": 2002, "status": "active"},
    },
    {
        "name": "ES&S",
        "entity_type": "organization",
        "description": (
            "Election Systems & Software, LLC. The largest voting machine manufacturer in the "
            "United States, providing equipment used in approximately 4,500 jurisdictions across "
            "42 states. Headquartered in Omaha, Nebraska. Formed from the merger of American "
            "Information Systems (AIS) and Business Records Corporation (BRC)."
            "\n\n"
            "MARKET DOMINANCE: ES&S and its predecessor companies have manufactured or serviced "
            "voting equipment for more than half of all U.S. counties. The company operates with "
            "proprietary source code that is not subject to public inspection, citing trade "
            "secret protections. Independent security researchers have repeatedly identified "
            "vulnerabilities in ES&S equipment at DEFCON's Voting Village events."
            "\n\n"
            "HAGEL CONTROVERSY: Chuck Hagel served as chairman of AIS (later ES&S) before "
            "running for the U.S. Senate in Nebraska in 1996. He won a surprise upset victory "
            "in a race where votes were counted on machines manufactured by his former company. "
            "Hagel did not disclose his AIS/ES&S ownership stake during the campaign. Bev Harris "
            "documented these conflicts of interest in her Black Box Voting research."
            "\n\n"
            "PROPRIETARY CODE: ES&S, like Diebold/Premier and Dominion, has consistently fought "
            "legislative efforts to mandate open-source code, paper ballot backups, and "
            "risk-limiting audits. The company spent $1.9 million lobbying Congress between "
            "2019-2022 (OpenSecrets data). Critics argue that the combination of proprietary "
            "code, trade secret exemptions, and industry consolidation creates a system where "
            "the mechanics of vote counting are functionally unverifiable."
        ),
        "aliases": "Election Systems & Software, American Information Systems, AIS, Diebold/ES&S",
        "metadata": {"founded": 1979, "status": "active"},
    },
    {
        "name": "Internet Research Agency",
        "entity_type": "organization",
        "description": (
            "Russian company based in Saint Petersburg that conducted internet troll operations "
            "and social media interference campaigns. Founded in 2013 by Yevgeny Prigozhin, "
            "a businessman with close ties to Vladimir Putin (Prigozhin was later known as "
            "'Putin's chef' and the founder of the Wagner Group private military company)."
            "\n\n"
            "2016 U.S. ELECTION OPERATIONS: The Mueller Report (Vol. I) and the DOJ indictment "
            "(United States v. Internet Research Agency LLC, Feb 2018) documented that the IRA "
            "employed over 80 staff members on its 'American department' by 2016, operating on "
            "a monthly budget exceeding $1.25 million. IRA operatives created thousands of fake "
            "American personas on Facebook, Instagram, Twitter, and YouTube. They organized "
            "real-world rallies in the United States, purchased political advertisements, and "
            "operated social media accounts with hundreds of thousands of followers."
            "\n\n"
            "METHODOLOGY: The IRA used a two-pronged strategy: (1) amplify divisive content on "
            "both sides of American political debates (race, immigration, guns, religion) to "
            "deepen polarization, and (2) specifically support the Trump campaign and disparage "
            "Hillary Clinton. IRA operatives traveled to the United States on intelligence-"
            "gathering trips in 2014. Facebook later estimated that IRA content reached 126 "
            "million Americans."
            "\n\n"
            "LEGAL OUTCOME: The DOJ indicted 13 Russian nationals and 3 Russian entities "
            "(including the IRA and Concord Management) in February 2018. The case against "
            "Concord Management was later dropped in 2020 after the company exploited discovery "
            "procedures to access sensitive U.S. intelligence. Prigozhin was killed in a plane "
            "crash on August 23, 2023, following his failed Wagner Group mutiny."
        ),
        "aliases": "IRA, Glavset, Internet Research Agency LLC",
        "metadata": {"founded": 2013, "status": "active"},
    },
    {
        "name": "Black Box Voting",
        "entity_type": "organization",
        "description": (
            "American nonprofit election watchdog organization founded by Bev Harris in 2003. "
            "Based in Renton, Washington. The organization investigates electronic voting "
            "machine security, election administration practices, and corporate ownership of "
            "election infrastructure."
            "\n\n"
            "SIGNIFICANCE: Black Box Voting performed the earliest systematic investigation "
            "of electronic voting machine security in the United States. Harris's discovery of "
            "Diebold's unprotected FTP server containing proprietary voting software source "
            "code (2003) enabled the first independent security audits of U.S. voting machines. "
            "The organization's research was foundational for later academic work by Halderman, "
            "Appel, and others."
            "\n\n"
            "The name 'black box voting' refers to the fundamental problem: proprietary voting "
            "machines that count votes using code that no one outside the manufacturer can "
            "inspect, verify, or audit — making the democratic process dependent on trusting "
            "corporate vendors."
        ),
        "aliases": "BlackBoxVoting.org, BBV",
        "metadata": {"founded": 2003, "status": "active"},
    },
    # ---- Events (4) ----
    {
        "name": "Brooks Brothers Riot (2000)",
        "entity_type": "event",
        "description": (
            "On November 22, 2000, during the Florida presidential recount following the "
            "contested Bush-Gore election, a group of Republican operatives — many of them "
            "paid congressional staffers flown in from Washington — staged an aggressive "
            "protest outside the Miami-Dade County election board offices. The mob pounded "
            "on doors and windows, physically intimidated election workers, and disrupted the "
            "recount process. The Miami-Dade Canvassing Board voted to halt its recount, "
            "citing safety concerns and inability to meet the deadline."
            "\n\n"
            "PARTICIPANTS: Investigative reporting identified several participants as Republican "
            "congressional staff members, including aides to Tom DeLay (House Majority Whip), "
            "and operatives later given positions in the Bush administration. The 'Brooks "
            "Brothers' name referred to the incongruity of well-dressed Washington staffers "
            "posing as grassroots protesters."
            "\n\n"
            "IMPACT: The halted Miami-Dade recount was one of several factors that preserved "
            "George W. Bush's narrow 537-vote lead in Florida. The Supreme Court's subsequent "
            "Bush v. Gore decision (December 12, 2000) ended all recounts. Post-election "
            "media consortium analyses produced conflicting results depending on which ballots "
            "were counted and what standard was applied."
        ),
        "aliases": "Miami-Dade Recount Riot, Brooks Brothers Mob",
        "metadata": {"date": "2000-11-22"},
    },
    {
        "name": "Bush v. Gore (2000)",
        "entity_type": "event",
        "description": (
            "Supreme Court case (531 U.S. 98) decided on December 12, 2000, which effectively "
            "determined the outcome of the 2000 presidential election. In a 5-4 per curiam "
            "decision, the Court ruled that Florida's recount procedures violated the Equal "
            "Protection Clause because different counties used different standards for evaluating "
            "ballots. The Court then ruled 5-4 that no constitutionally valid recount could be "
            "completed before the December 12 'safe harbor' deadline — effectively ending the "
            "recount and awarding Florida's 25 electoral votes (and the presidency) to George "
            "W. Bush."
            "\n\n"
            "SIGNIFICANCE: The ruling was unprecedented — the Court explicitly stated that its "
            "Equal Protection analysis was 'limited to the present circumstances' and should "
            "not be cited as precedent. Justice Stevens's dissent warned that 'the identity of "
            "the loser is perfectly clear. It is the Nation's confidence in the judge as an "
            "impartial guardian of the rule of law.' The case remains one of the most "
            "controversial Supreme Court decisions in American history."
            "\n\n"
            "CONTEXT: Bush's final certified margin in Florida was 537 votes out of approximately "
            "6 million cast. Issues included the Palm Beach County 'butterfly ballot' (which "
            "likely cost Gore thousands of votes), 'hanging chads' on punch-card ballots, the "
            "disqualification of approximately 12,000 ballots in heavily Democratic precincts, "
            "and the role of Florida Secretary of State Katherine Harris (who co-chaired Bush's "
            "Florida campaign committee) in certifying the results."
        ),
        "aliases": "Bush v. Gore, 531 U.S. 98",
        "metadata": {"date": "2000-12-12"},
    },
    {
        "name": "Citizens United v. FEC (2010)",
        "entity_type": "event",
        "description": (
            "Supreme Court case (558 U.S. 310) decided on January 21, 2010, which struck down "
            "key provisions of the Bipartisan Campaign Reform Act (McCain-Feingold) and ruled "
            "that the First Amendment prohibits the government from restricting independent "
            "political expenditures by corporations, associations, and labor unions. The 5-4 "
            "decision, authored by Justice Kennedy, held that political speech does not lose "
            "constitutional protection 'simply because its source is a corporation.'"
            "\n\n"
            "IMPACT: The ruling enabled the creation of Super PACs — independent expenditure "
            "committees that can raise and spend unlimited amounts of money on political "
            "campaigns, so long as they do not 'coordinate' directly with candidates. Combined "
            "with the D.C. Circuit's SpeechNow.org v. FEC decision (March 2010), Citizens "
            "United opened the floodgates to unlimited dark money in American politics."
            "\n\n"
            "SCALE: Outside spending in federal elections exploded from $338 million in 2008 "
            "to $1.04 billion in 2012 to over $4.5 billion in 2020 (OpenSecrets data). Much of "
            "this spending is routed through 501(c)(4) 'social welfare' organizations that are "
            "not required to disclose their donors, creating untraceable 'dark money' pipelines."
            "\n\n"
            "STRUCTURAL EFFECT: Citizens United transformed the relationship between wealth and "
            "political power. Billionaire donors like Robert Mercer, Sheldon Adelson, the Koch "
            "brothers, George Soros, and Michael Bloomberg can now spend unlimited sums through "
            "Super PACs and nonprofits, effectively building parallel campaign infrastructures "
            "outside party control. This is the legal framework that enabled Cambridge "
            "Analytica's funding model."
        ),
        "aliases": "Citizens United ruling, Citizens United v. Federal Election Commission",
        "metadata": {"date": "2010-01-21"},
    },
    {
        "name": "2016 Russian Interference",
        "entity_type": "event",
        "description": (
            "The documented campaign by Russian government-linked entities to influence the "
            "2016 United States presidential election, as established by the Mueller Report "
            "(Vols. I-II), the Senate Intelligence Committee Report (Vols. 1-5), multiple DOJ "
            "indictments, and the U.S. Intelligence Community Assessment (ICA, January 2017)."
            "\n\n"
            "TWO TRACKS: The interference operated through two distinct channels: "
            "(1) The Internet Research Agency social media operation — creating fake American "
            "personas, organizing real-world rallies, purchasing political ads, and amplifying "
            "divisive content to reach an estimated 126 million Americans on Facebook alone. "
            "(2) GRU (Russian military intelligence) cyber operations — hacking the Democratic "
            "National Committee and John Podesta's emails, then releasing them through "
            "WikiLeaks, DCLeaks, and the 'Guccifer 2.0' persona."
            "\n\n"
            "DOCUMENTED FINDINGS: The Mueller Report established that Russian interference was "
            "'sweeping and systematic.' It did not establish that members of the Trump campaign "
            "conspired or coordinated with the Russian government, though it documented "
            "numerous contacts and a campaign that 'expected it would benefit electorally from "
            "information stolen and released through Russian efforts.' The Senate Intelligence "
            "Committee (Vol. 5) documented extensive contacts between campaign chairman Paul "
            "Manafort and Russian intelligence officer Konstantin Kilimnik."
            "\n\n"
            "INDICTMENTS: The Mueller investigation produced 37 indictments, including 12 GRU "
            "officers (Netyksho et al.), 13 IRA employees and 3 Russian entities, and several "
            "Trump campaign associates (Manafort, Gates, Flynn, Papadopoulos, Stone, Cohen) "
            "for various charges."
        ),
        "aliases": "Russian election interference, Russia-2016, Russiagate",
        "metadata": {"date": "2016-11-08"},
    },
    {
        "name": "Halderman Report (2021)",
        "entity_type": "event",
        "description": (
            "Court-ordered security analysis of Dominion Voting Systems' ImageCast X ballot "
            "marking device, conducted by University of Michigan computer science professor "
            "J. Alex Halderman as an expert witness in Curling v. Raffensperger (N.D. Ga.). "
            "The report was filed under seal in July 2021 and partially unsealed in June 2023."
            "\n\n"
            "FINDINGS: Halderman identified nine critical vulnerabilities in the Dominion "
            "ImageCast X, including: the ability to install malicious code that alters QR "
            "codes on printed ballots (which are what scanners actually read, not the "
            "human-readable text), the ability to modify the election database, and the "
            "ability to spread malware from the Election Management System (EMS) to all "
            "connected devices. All attacks could be executed without detection by standard "
            "election auditing procedures."
            "\n\n"
            "ACADEMIC CONTEXT: Halderman is one of the world's foremost election security "
            "researchers. His work builds on a two-decade body of peer-reviewed research "
            "demonstrating electronic voting machine vulnerabilities, including the 2006 "
            "Princeton/Appel/Feldman study of Diebold AccuVote-TS machines and annual DEFCON "
            "Voting Village findings. His testimony emphasized that documented vulnerabilities "
            "are not evidence of actual exploitation — they are evidence that the systems are "
            "exploitable."
            "\n\n"
            "SIGNIFICANCE: The report is the most rigorous court-admissible security analysis "
            "of a major U.S. voting system. Halderman recommended that Georgia either fix the "
            "vulnerabilities or switch to hand-marked paper ballots. The state did neither. "
            "The report matters because it demonstrates, under courtroom evidentiary standards, "
            "that the machines used to count American votes contain critical security flaws — "
            "regardless of whether those flaws have been exploited."
        ),
        "aliases": "Halderman expert report, Curling v. Raffensperger security analysis",
        "metadata": {"date": "2021-07-01"},
    },
    # ---- Legislation (1) ----
    {
        "name": "Help America Vote Act",
        "entity_type": "legislation",
        "description": (
            "Federal law (Pub.L. 107-252) signed by President George W. Bush on October 29, "
            "2002, in response to the voting controversies of the 2000 presidential election. "
            "HAVA created the Election Assistance Commission (EAC), established the first "
            "federal standards for voting systems, mandated provisional ballots, required "
            "statewide voter registration databases, and authorized $3.86 billion in federal "
            "funding for states to upgrade election infrastructure."
            "\n\n"
            "UNINTENDED CONSEQUENCE: HAVA's funding mandate accelerated the nationwide "
            "transition from paper ballots and mechanical lever machines to electronic voting "
            "systems — primarily Direct Recording Electronic (DRE) machines from Diebold, ES&S, "
            "and Sequoia. Critics argue that HAVA effectively subsidized the replacement of "
            "auditable paper systems with unauditable electronic black boxes."
            "\n\n"
            "THE VENDOR PIPELINE: The $3.86 billion in HAVA funds flowed primarily to three "
            "private companies (ES&S, Diebold/Premier, Sequoia) that had lobbied for the "
            "legislation. The Election Assistance Commission created under HAVA was given "
            "advisory (not regulatory) authority and was chronically understaffed and "
            "underfunded, leaving certification standards effectively voluntary."
        ),
        "aliases": "HAVA, Pub.L. 107-252",
        "metadata": {"date": "2002-10-29", "status": "enacted"},
    },
    # ---- Programs (1) ----
    {
        "name": "Project Alamo",
        "entity_type": "program",
        "description": (
            "The Trump 2016 campaign's digital operation, headquartered at an office in San "
            "Antonio, Texas, and staffed in part by Cambridge Analytica employees. Named after "
            "the Alamo mission in San Antonio. The operation combined Cambridge Analytica's "
            "psychographic profiling with Facebook's own advertising tools and the Republican "
            "National Committee's voter file."
            "\n\n"
            "OPERATION: Project Alamo ran the campaign's entire digital advertising operation "
            "on Facebook, including A/B testing of 40,000-50,000 ad variations per day. A "
            "leaked database analyzed by Channel 4 News (September 2020) revealed the operation "
            "maintained a database of 198 million American voters, categorized by race, "
            "demographics, and a 'deterrence' score — with 3.5 million Black Americans "
            "designated as targets for voter suppression messaging."
            "\n\n"
            "FACEBOOK EMBEDS: Facebook, Google, and Twitter all embedded staff directly in "
            "Project Alamo's San Antonio office to help optimize ad spending. Facebook's "
            "embedded team helped the Trump campaign use 'Custom Audiences' and 'Lookalike "
            "Audiences' tools to micro-target specific voter segments. Brad Parscale, the "
            "campaign's digital director, described Facebook as 'the single most important "
            "platform to help grow our fundraising base.'"
            "\n\n"
            "SCALE: Project Alamo spent an estimated $70 million on Facebook advertising "
            "alone during the 2016 campaign, compared to $20 million by the Clinton campaign. "
            "The operation is significant because it represents the convergence of military "
            "psyops methodology (via SCL/Cambridge Analytica), Silicon Valley data tools "
            "(Facebook embeds), and unlimited donor money (Mercer) in a single campaign."
        ),
        "aliases": "Trump digital operation, San Antonio operation",
        "metadata": {"year_start": 2016, "status": "concluded"},
    },
]


# ============================================================
# RELATIONSHIPS — 46 connections
# ============================================================

RELATIONSHIPS = [
    # ---- Cambridge Analytica / SCL Group internal structure ----
    {
        "source": "Cambridge Analytica",
        "target": "SCL Group",
        "type": "subsidiary_of",
        "tier": "documented",
        "desc": (
            "Cambridge Analytica was incorporated as a subsidiary of SCL Group in 2013. "
            "UK Companies House filings confirm the corporate relationship. SCL Group "
            "provided the military psyops methodology; Cambridge Analytica was the "
            "American-facing political division."
        ),
        "sources": [1081, 1082, 1103],
    },
    {
        "source": "Alexander Nix",
        "target": "Cambridge Analytica",
        "type": "member_of",
        "tier": "documented",
        "desc": (
            "Nix served as CEO of Cambridge Analytica from its founding in 2013 until his "
            "suspension and termination in March 2018. Also a director of SCL Group."
        ),
        "sources": [1081, 1096, 1103],
    },
    {
        "source": "Alexander Nix",
        "target": "SCL Group",
        "type": "member_of",
        "tier": "documented",
        "desc": (
            "Nix was a director of SCL Group and led its transition from military defence "
            "contracts to civilian political campaigns, ultimately creating Cambridge Analytica."
        ),
        "sources": [1081, 1103],
    },
    {
        "source": "Christopher Wylie",
        "target": "Cambridge Analytica",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Wylie worked at SCL Group from 2013 and helped design Cambridge Analytica's "
            "psychographic profiling methodology. Left in 2014, then went public as "
            "whistleblower in March 2018, providing internal documents and testimony to "
            "The Guardian, NYT, and UK Parliament."
        ),
        "sources": [1083, 1094, 1095],
    },
    {
        "source": "Christopher Wylie",
        "target": "SCL Group",
        "type": "employed_by",
        "tier": "documented",
        "desc": (
            "Wylie joined SCL Group in 2013 and was instrumental in creating the research "
            "program that became Cambridge Analytica. He designed the psychographic profiling "
            "methodology based on the OCEAN personality model."
        ),
        "sources": [1083, 1094],
    },
    {
        "source": "Robert Mercer",
        "target": "Cambridge Analytica",
        "type": "funded",
        "tier": "documented",
        "desc": (
            "Mercer invested approximately $15 million in Cambridge Analytica. His daughter "
            "Rebekah Mercer sat on the company's board. The Mercer family was the primary "
            "financial backer of Cambridge Analytica's operations."
        ),
        "sources": [1081, 1094, 1095, 1104],
    },
    {
        "source": "Robert Mercer",
        "target": "Donald Trump",
        "type": "funded",
        "tier": "documented",
        "desc": (
            "Mercer became a major Trump donor after Ted Cruz dropped out of the 2016 primary. "
            "His funding supported the Trump campaign through Super PACs, and he facilitated "
            "the integration of Cambridge Analytica and Steve Bannon into the campaign."
        ),
        "sources": [1095, 1104, 1106],
    },
    {
        "source": "Robert Mercer",
        "target": "Citizens United v. FEC (2010)",
        "type": "benefited_from",
        "tier": "documented",
        "desc": (
            "Citizens United enabled Mercer to spend unlimited amounts through Super PACs "
            "and nonprofits. His post-Citizens United spending funded Cambridge Analytica, "
            "Breitbart News, the Government Accountability Institute, and multiple Super PACs. "
            "OpenSecrets data shows Mercer family as top-tier post-Citizens United donors."
        ),
        "sources": [1088, 1097, 1104],
    },

    # ---- John Bolton / Cambridge Analytica ----
    {
        "source": "John Bolton",
        "target": "Cambridge Analytica",
        "type": "contracted",
        "tier": "documented",
        "desc": (
            "Bolton's Super PAC (The John Bolton Super PAC) paid Cambridge Analytica "
            "approximately $1.2 million for psychographic voter-targeting services. FEC "
            "filings document the payments. Bolton's PAC was one of CA's earliest U.S. "
            "political clients (2014)."
        ),
        "sources": [1081, 1109],
    },
    {
        "source": "Robert Mercer",
        "target": "John Bolton",
        "type": "funded",
        "tier": "documented",
        "desc": (
            "Mercer was a major donor to the John Bolton Super PAC, which in turn hired "
            "Cambridge Analytica (also Mercer-funded). This created a circular funding "
            "arrangement where Mercer's money flowed to Cambridge Analytica through "
            "multiple channels."
        ),
        "sources": [1104, 1109],
    },

    # ---- Project Alamo / Trump Digital Operation ----
    {
        "source": "Cambridge Analytica",
        "target": "Project Alamo",
        "type": "operated",
        "tier": "documented",
        "desc": (
            "Cambridge Analytica staff were embedded in Project Alamo's San Antonio office, "
            "providing psychographic profiling and voter targeting. Alexander Nix claimed on "
            "hidden camera that CA 'ran all of the campaign's digital campaign.'"
        ),
        "sources": [1096, 1106, 1107],
    },
    {
        "source": "Project Alamo",
        "target": "Donald Trump",
        "type": "supported",
        "tier": "documented",
        "desc": (
            "Project Alamo was the Trump 2016 campaign's entire digital advertising operation. "
            "Based in San Antonio, it ran 40,000-50,000 Facebook ad variations per day and "
            "maintained a database of 198 million voters."
        ),
        "sources": [1106, 1107],
    },
    {
        "source": "SCL Group",
        "target": "Project Alamo",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "Project Alamo's methodology derived from SCL Group's military 'Target Audience "
            "Analysis' framework, adapted for American civilian politics. The intellectual "
            "pipeline ran from NATO/MoD psyops contracts through SCL to Cambridge Analytica "
            "to the Trump campaign's digital operation."
        ),
        "sources": [1081, 1083, 1106],
    },

    # ---- Voting Machine Ecosystem ----
    {
        "source": "Bev Harris",
        "target": "Black Box Voting",
        "type": "founded",
        "tier": "documented",
        "desc": (
            "Harris founded Black Box Voting in 2003 after discovering Diebold's unprotected "
            "voting software source code on a public FTP server."
        ),
        "sources": [1093],
    },
    {
        "source": "Bev Harris",
        "target": "ES&S",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Harris's Black Box Voting research documented ES&S's revolving door with "
            "elected officials (Hagel), proprietary code exemptions under trade secret law, "
            "and resistance to independent security auditing."
        ),
        "sources": [1093, 1108],
    },
    {
        "source": "Black Box Voting",
        "target": "Dominion Voting Systems",
        "type": "investigated",
        "tier": "credible",
        "desc": (
            "Black Box Voting's research on proprietary voting machine code and vendor "
            "consolidation laid the groundwork for later scrutiny of Dominion and all major "
            "vendors. Harris's methodology of FOIA requests for internal logs became "
            "standard practice for election integrity researchers."
        ),
        "sources": [1093, 1092],
    },
    {
        "source": "Clint Curtis",
        "target": "ES&S",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Curtis's sworn testimony that he was asked to write vote-rigging software "
            "demonstrated the technical feasibility of manipulating DRE machines — the same "
            "class of machines manufactured by ES&S and Diebold. His testimony corroborated "
            "the category of vulnerability that Harris and Halderman independently documented."
        ),
        "sources": [1091, 1093, 1102],
    },
    {
        "source": "Help America Vote Act",
        "target": "ES&S",
        "type": "enabled",
        "tier": "documented",
        "desc": (
            "HAVA's $3.86 billion in federal funding for election equipment upgrades flowed "
            "primarily to ES&S, Diebold, and Sequoia — subsidizing the nationwide transition "
            "from paper to electronic voting machines."
        ),
        "sources": [1092, 1098, 1108],
    },
    {
        "source": "Help America Vote Act",
        "target": "Dominion Voting Systems",
        "type": "enabled",
        "tier": "documented",
        "desc": (
            "HAVA's equipment replacement mandates and funding created the market conditions "
            "for Dominion's growth. Dominion later acquired Sequoia Voting Systems (2010) "
            "and Premier Election Solutions/Diebold (select assets, 2010), further "
            "consolidating the industry."
        ),
        "sources": [1098, 1099],
    },
    {
        "source": "Bush v. Gore (2000)",
        "target": "Help America Vote Act",
        "type": "precipitated",
        "tier": "documented",
        "desc": (
            "The 2000 Florida recount debacle — punch-card ballots, hanging chads, butterfly "
            "ballots — was the direct impetus for HAVA. Congress passed the law to prevent a "
            "repeat of 2000, but the 'solution' (electronic machines) created new and arguably "
            "less auditable vulnerabilities."
        ),
        "sources": [1089, 1098],
    },

    # ---- 2000 Florida Election ----
    {
        "source": "Brooks Brothers Riot (2000)",
        "target": "Bush v. Gore (2000)",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The Brooks Brothers Riot halted the Miami-Dade recount on November 22, 2000, "
            "preserving Bush's narrow lead. The Supreme Court's Bush v. Gore decision three "
            "weeks later (December 12) ended all remaining recounts."
        ),
        "sources": [1089, 1100, 1101],
    },
    {
        "source": "Brooks Brothers Riot (2000)",
        "target": "George W. Bush",
        "type": "supported",
        "tier": "documented",
        "desc": (
            "Participants in the Brooks Brothers Riot were identified as Republican "
            "congressional staffers, including aides to Tom DeLay. Several participants "
            "later received positions in the Bush administration, suggesting organized "
            "coordination rather than spontaneous protest."
        ),
        "sources": [1100, 1101],
    },
    {
        "source": "Bush v. Gore (2000)",
        "target": "George W. Bush",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The 5-4 Supreme Court decision ended the Florida recount and effectively "
            "awarded the presidency to George W. Bush, who won Florida by 537 votes out "
            "of approximately 6 million cast."
        ),
        "sources": [1089, 1101],
    },

    # ---- Russian Interference ----
    {
        "source": "Internet Research Agency",
        "target": "2016 Russian Interference",
        "type": "operated",
        "tier": "documented",
        "desc": (
            "The IRA was the social media arm of Russia's 2016 election interference, "
            "operating over 80 staff on a $1.25M+ monthly budget. Indicted by DOJ in "
            "February 2018. Mueller Report documented sweeping operations reaching 126 "
            "million Americans on Facebook alone."
        ),
        "sources": [1084, 1085, 1086, 1110],
    },
    {
        "source": "Internet Research Agency",
        "target": "FSB",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "The IRA was founded by Yevgeny Prigozhin, who operated with Kremlin approval. "
            "While the IRA's direct chain of command ran through Prigozhin rather than the "
            "FSB, the Senate Intelligence Committee Report established that the operation "
            "was 'directed by the Kremlin' and coordinated with broader Russian state "
            "objectives."
        ),
        "sources": [1084, 1085],
    },
    {
        "source": "2016 Russian Interference",
        "target": "FBI",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "The FBI opened Operation Crossfire Hurricane in July 2016 to investigate "
            "Russian interference and possible coordination with the Trump campaign. "
            "This investigation was later taken over by Special Counsel Robert Mueller "
            "in May 2017."
        ),
        "sources": [1084, 1087],
    },
    {
        "source": "2016 Russian Interference",
        "target": "NSA",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "NSA contributed SIGINT analysis to the January 2017 Intelligence Community "
            "Assessment concluding that 'Russian President Vladimir Putin ordered an "
            "influence campaign in 2016 aimed at the US presidential election.'"
        ),
        "sources": [1084],
    },
    {
        "source": "2016 Russian Interference",
        "target": "Donald Trump",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Mueller Report documented that Russia's interference was 'sweeping and "
            "systematic' and that the Trump campaign 'expected it would benefit electorally "
            "from information stolen and released through Russian efforts.' The investigation "
            "did not establish conspiracy or coordination but documented extensive contacts."
        ),
        "sources": [1084, 1085],
    },

    # ---- Citizens United / Dark Money ----
    {
        "source": "Citizens United v. FEC (2010)",
        "target": "Cambridge Analytica",
        "type": "enabled",
        "tier": "inference",
        "desc": (
            "Citizens United created the legal framework (unlimited Super PAC spending) "
            "that enabled Robert Mercer to invest $15 million in Cambridge Analytica through "
            "political vehicles. Without the ruling, the funding model that created CA "
            "would not have been legal."
        ),
        "sources": [1088, 1097, 1104],
    },
    {
        "source": "Citizens United v. FEC (2010)",
        "target": "Project Alamo",
        "type": "enabled",
        "tier": "inference",
        "desc": (
            "Citizens United enabled the unlimited dark money flow through Super PACs that "
            "funded the ecosystem around Project Alamo — including Cambridge Analytica's "
            "$15 million Mercer investment, Bolton PAC spending, and the broader network "
            "of outside groups supporting the Trump digital operation."
        ),
        "sources": [1088, 1097, 1106],
    },

    # ---- Cross-references to EXISTING entities ----
    {
        "source": "SCL Group",
        "target": "GCHQ",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "SCL Group held defence contracts with the UK Ministry of Defence and "
            "conducted information operations aligned with British intelligence interests. "
            "Former MI5/MI6 personnel served as SCL advisors. The UK intelligence community's "
            "relationship with SCL predated Cambridge Analytica."
        ),
        "sources": [1081, 1103],
    },
    {
        "source": "Internet Research Agency",
        "target": "Twitter Files",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Twitter Files releases (2022-2023) revealed how Twitter handled IRA-linked "
            "accounts, including internal debates about labeling, removal timelines, and "
            "FBI communications about Russian bot identification. Twitter eventually removed "
            "over 3,800 IRA-linked accounts."
        ),
        "sources": [1085, 1110],
    },
    {
        "source": "Cambridge Analytica",
        "target": "Unit 8200",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "SCL Group/Cambridge Analytica operated in the same domain as Unit 8200-linked "
            "firms (NSO Group, Black Cube) — psychographic profiling and political influence "
            "operations. Whistleblower testimony referenced contacts between SCL personnel "
            "and Israeli intelligence-linked data firms, though direct operational ties remain "
            "unconfirmed."
        ),
        "sources": [1081, 1083],
    },
    {
        "source": "2016 Russian Interference",
        "target": "CIA",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "CIA Director John Brennan briefed the Gang of Eight in August 2016 on "
            "intelligence indicating Putin's personal involvement in election interference. "
            "CIA contributed analysis to the January 2017 ICA with 'high confidence.'"
        ),
        "sources": [1084],
    },
    {
        "source": "2016 Russian Interference",
        "target": "DOJ",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "DOJ appointed Special Counsel Robert Mueller in May 2017 and supported the "
            "investigation through its National Security Division. DOJ issued indictments "
            "against IRA employees, GRU officers, and Trump campaign associates."
        ),
        "sources": [1084, 1086, 1087],
    },
    {
        "source": "Dominion Voting Systems",
        "target": "Fox Corporation",
        "type": "sued",
        "tier": "documented",
        "desc": (
            "Dominion sued Fox Corporation for $1.6 billion in defamation over Fox's "
            "broadcasting of false claims about Dominion machines switching votes. Fox "
            "settled for $787.5 million in April 2023, the largest known defamation "
            "settlement in U.S. history."
        ),
        "sources": [1090],
    },

    # ---- Halderman / Academic Voting Research ----
    {
        "source": "Halderman Report (2021)",
        "target": "Dominion Voting Systems",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Halderman's court-ordered security analysis identified nine critical "
            "vulnerabilities in Dominion's ImageCast X ballot marking device, including "
            "the ability to install malicious code, alter QR codes on printed ballots, "
            "and spread malware across election infrastructure."
        ),
        "sources": [1090, 1091],
    },
    {
        "source": "Halderman Report (2021)",
        "target": "ES&S",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Halderman's findings on Dominion's ImageCast X are representative of a class "
            "of vulnerabilities common to all proprietary DRE/BMD systems, including ES&S "
            "equipment. DEFCON Voting Village research has demonstrated similar flaws across "
            "all major vendors."
        ),
        "sources": [1091, 1092],
    },
    {
        "source": "Dominion Voting Systems",
        "target": "ES&S",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Dominion and ES&S are the two largest U.S. voting machine vendors, collectively "
            "serving over 70% of U.S. jurisdictions. Both use proprietary code, resist "
            "open-source mandates, and lobby against risk-limiting audit requirements. "
            "Dominion acquired assets from Diebold/Premier (ES&S's predecessor entity) in 2010."
        ),
        "sources": [1091, 1092, 1108],
    },

    # ---- Clint Curtis / Florida Connection ----
    {
        "source": "Clint Curtis",
        "target": "Black Box Voting",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Curtis's testimony about vote-rigging software corroborated Bev Harris's "
            "research on electronic voting vulnerabilities from a different angle — Harris "
            "documented the technical flaws; Curtis testified to the political intent to "
            "exploit them."
        ),
        "sources": [1093, 1102],
    },

    # ---- Cross-cutting structural relationships ----
    {
        "source": "Cambridge Analytica",
        "target": "2016 Russian Interference",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "The Mueller investigation examined but did not establish direct coordination "
            "between Cambridge Analytica and Russian interference operations. However, both "
            "targeted the same swing-state voters using similar psychographic methods. The "
            "UK DCMS Committee found that Arron Banks (Leave.EU) had undisclosed contacts "
            "with Russian officials while also working with Cambridge Analytica."
        ),
        "sources": [1081, 1084],
    },
    {
        "source": "John Bolton",
        "target": "Donald Trump",
        "type": "advisor_to",
        "tier": "documented",
        "desc": (
            "Bolton served as National Security Advisor from April 2018 to September 2019. "
            "His earlier use of Cambridge Analytica (via his Super PAC) connects the Republican "
            "donor-data-campaign pipeline directly to the White House national security apparatus."
        ),
        "sources": [1109],
    },
    {
        "source": "Help America Vote Act",
        "target": "George W. Bush",
        "type": "signed_by",
        "tier": "documented",
        "desc": (
            "Bush signed HAVA on October 29, 2002 — a law created in direct response to the "
            "chaotic Florida recount that put him in office. The law's $3.86 billion subsidized "
            "electronic voting machines that introduced new, less auditable vulnerabilities."
        ),
        "sources": [1098],
    },
    {
        "source": "Alexander Nix",
        "target": "Robert Mercer",
        "type": "funded_by",
        "tier": "documented",
        "desc": (
            "Mercer's $15 million investment funded Nix's Cambridge Analytica operation. "
            "After CA's collapse, Nix founded Auspex International, continuing in the "
            "political data business. The Mercer-Nix relationship was the financial axis "
            "of the CA operation."
        ),
        "sources": [1081, 1094, 1104],
    },
    {
        "source": "ES&S",
        "target": "Help America Vote Act",
        "type": "benefited_from",
        "tier": "documented",
        "desc": (
            "ES&S was a primary beneficiary of HAVA's equipment replacement funding. "
            "The company lobbied for the legislation and then received billions in "
            "state and county contracts funded by HAVA appropriations."
        ),
        "sources": [1098, 1108],
    },
    {
        "source": "Black Box Voting",
        "target": "ES&S",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Black Box Voting's FOIA requests and investigative research documented "
            "ES&S's revolving door with elected officials, proprietary code exemptions, "
            "and security vulnerabilities in DRE machines."
        ),
        "sources": [1093],
    },
]


# ============================================================
# ENTITY_SOURCES — link entities to their primary sources
# ============================================================

ENTITY_SOURCES = {
    # People
    "Alexander Nix": [1081, 1082, 1083, 1094, 1096, 1103],
    "Christopher Wylie": [1081, 1083, 1094, 1095],
    "Clint Curtis": [1091, 1093, 1102],
    "Bev Harris": [1092, 1093, 1108],
    "Robert Mercer": [1081, 1094, 1095, 1097, 1104, 1109],
    "John Bolton": [1081, 1109],
    # Organizations
    "Cambridge Analytica": [1081, 1082, 1083, 1094, 1095, 1096, 1103],
    "SCL Group": [1081, 1083, 1094, 1103],
    "Dominion Voting Systems": [1090, 1091, 1092, 1099],
    "ES&S": [1091, 1092, 1093, 1098, 1108],
    "Internet Research Agency": [1084, 1085, 1086, 1110],
    "Black Box Voting": [1092, 1093],
    # Events
    "Brooks Brothers Riot (2000)": [1089, 1100, 1101],
    "Bush v. Gore (2000)": [1089, 1101],
    "Citizens United v. FEC (2010)": [1088, 1097, 1104, 1105],
    "2016 Russian Interference": [1084, 1085, 1086, 1087, 1110],
    "Halderman Report (2021)": [1090, 1091, 1092],
    # Legislation
    "Help America Vote Act": [1092, 1098, 1099],
    # Programs
    "Project Alamo": [1096, 1106, 1107],
}
