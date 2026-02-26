"""
Hand-curated core entities and relationships for the Intel Console.
All data from public, documented sources already cited in disclosure-data.json.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — every relationship links back to at least one
# ============================================================

SOURCES = [
    # Congressional
    {"id": 1, "title": "Kerry/Brown BCCI Senate Report (1992)", "url": "https://irp.fas.org/congress/1992_rpt/bcci/", "source_type": "congressional", "year": 1992},
    {"id": 2, "title": "Church Committee Final Report (Senate Report 94-755)", "url": "https://www.intelligence.senate.gov/resources/intelligence-related-commissions", "source_type": "congressional", "year": 1976},
    {"id": 3, "title": "MKULTRA Senate Hearing (95th Congress)", "url": "https://www.intelligence.senate.gov/sites/default/files/hearings/95mkultra.pdf", "source_type": "congressional", "year": 1977},
    # Court / Settlement
    {"id": 4, "title": "JPMorgan Epstein Settlement — SDNY", "url": "", "source_type": "court", "year": 2023},
    {"id": 5, "title": "Deutsche Bank NYDFS Settlement", "url": "", "source_type": "court", "year": 2020},
    {"id": 6, "title": "Epstein Non-Prosecution Agreement (NPA)", "url": "", "source_type": "court", "year": 2007},
    {"id": 7, "title": "INSLAW Bankruptcy Proceedings", "url": "", "source_type": "court", "year": 1987},
    # Government / FOIA
    {"id": 8, "title": "CIA Inspector General Report Vol. II (1998)", "url": "", "source_type": "foia", "year": 1998},
    {"id": 9, "title": "FBI CHS Memo on Epstein (Oct 2020)", "url": "", "source_type": "foia", "year": 2020},
    {"id": 10, "title": "National Security Act of 1947", "url": "", "source_type": "government", "year": 1947},
    # Journalism / Books
    {"id": 11, "title": "Webb — One Nation Under Blackmail Vol 1 & 2 (2022)", "url": "", "source_type": "book", "author": "Whitney Webb", "year": 2022},
    {"id": 12, "title": "Washington Times — Craig Spence Investigation (1989)", "url": "", "source_type": "journalism", "year": 1989},
    {"id": 13, "title": "Cockburn/St. Clair — Whiteout: The CIA, Drugs, and the Press", "url": "", "source_type": "book", "year": 1998},
    {"id": 14, "title": "Columbus Dispatch — SAT/Southern Air Transport Investigation", "url": "", "source_type": "journalism", "year": 1998},
    {"id": 15, "title": "Haaretz — Marc Rich/Mossad Relationship", "url": "", "source_type": "journalism", "year": 2013},
    {"id": 16, "title": "UK Sandstorm Report — Bear Stearns/BCCI (2011)", "url": "https://www.telegraph.co.uk/finance/newsbysector/banksandfinance/8416922/Bear-Stearns-link-to-BCCI-revealed.html", "source_type": "court", "year": 2011},
    {"id": 17, "title": "Seattle Times — Stephens/Clinton Campaign Finance", "url": "", "source_type": "journalism", "year": 1992},
    {"id": 18, "title": "Omaha World Herald — Franklin Investigation", "url": "", "source_type": "journalism", "year": 1990},
    {"id": 19, "title": "Hartford Courant — AmeriCares/Contra Funding", "url": "", "source_type": "journalism", "year": 1988},
    {"id": 20, "title": "Newsweek — Robert Keith Gray CIA Connections", "url": "", "source_type": "journalism", "year": 1982},
    {"id": 21, "title": "Senate Judiciary Committee — INSLAW/PROMIS Investigation", "url": "", "source_type": "congressional", "year": 1992},
    {"id": 22, "title": "In-Q-Tel Public Filings and Press Releases", "url": "", "source_type": "government", "year": 1999},
    {"id": 23, "title": "Palantir Technologies SEC Filings", "url": "", "source_type": "government", "year": 2020},
    {"id": 24, "title": "DARPA TIA Program Documentation", "url": "", "source_type": "government", "year": 2002},
    {"id": 25, "title": "Inslaw Document to Ken Starr — National Archives", "url": "", "source_type": "government", "year": 1995},

    # ---- New sources (26-40) ----
    {"id": 26, "title": "New York Magazine — Jeffrey Epstein: International Moneyman of Mystery", "url": "https://nymag.com/nymetro/news/people/n_7912/", "source_type": "journalism", "author": "Landon Thomas Jr.", "year": 2002},
    {"id": 27, "title": "NJ Casino Control Commission Records — Trump License Hearings", "url": "", "source_type": "government", "year": 1982},
    {"id": 28, "title": "Daily Beast — Accused Sex Trafficker Had 'Belonged to Intelligence'", "url": "https://www.thedailybeast.com/jeffrey-epsteins-sick-story-played-out-for-years-in-plain-sight", "source_type": "journalism", "author": "Vicky Ward", "year": 2019},
    {"id": 29, "title": "Virginia Giuffre Depositions (Maxwell Civil Case, Unsealed)", "url": "", "source_type": "court", "year": 2016},
    {"id": 30, "title": "Epstein Flight Logs (Court Records, Unsealed 2024)", "url": "", "source_type": "court", "year": 2024},
    {"id": 31, "title": "Julie K. Brown — Perversion of Justice (Miami Herald Investigation)", "url": "https://www.miamiherald.com/topics/jeffrey-epstein", "source_type": "journalism", "author": "Julie K. Brown", "year": 2018},
    {"id": 32, "title": "Julie K. Brown — Perversion of Justice (Book)", "url": "", "source_type": "book", "author": "Julie K. Brown", "year": 2021},
    {"id": 33, "title": "Wexner House Oversight Committee Deposition (Feb 18, 2026)", "url": "", "source_type": "congressional", "year": 2026},
    {"id": 34, "title": "Vicky Ward — The Talented Mr. Epstein (Vanity Fair)", "url": "", "source_type": "journalism", "author": "Vicky Ward", "year": 2003},
    {"id": 35, "title": "Bradley Edwards — Relentless Pursuit: My Fight for the Victims of Jeffrey Epstein", "url": "", "source_type": "book", "author": "Bradley Edwards", "year": 2020},
    {"id": 36, "title": "Epstein Victim Impact Statements (SDNY, 2019-2020)", "url": "", "source_type": "court", "year": 2020},
    {"id": 37, "title": "Wayne Barrett — Trump: The Deals and the Downfall", "url": "", "source_type": "book", "author": "Wayne Barrett", "year": 1992},
    {"id": 38, "title": "David Cay Johnston — The Making of Donald Trump", "url": "", "source_type": "book", "author": "David Cay Johnston", "year": 2016},
    {"id": 39, "title": "Conchita Sarnoff — TrafficKing: The Jeffrey Epstein Case", "url": "", "source_type": "book", "author": "Conchita Sarnoff", "year": 2020},
    {"id": 40, "title": "Bayrock/Sater Litigation Records (Kriss v. Bayrock et al.)", "url": "", "source_type": "court", "year": 2010},

    # ---- Organized crime sources (41-55) ----
    {"id": 41, "title": "Mafia Commission Trial Records — US v. Salerno et al. (SDNY)", "url": "", "source_type": "court", "year": 1986},
    {"id": 42, "title": "Fortune — The Mafia's Bite of the Big Apple (1988)", "url": "https://money.cnn.com/magazines/fortune/fortune_archive/1988/06/06/70628/index.htm", "source_type": "journalism", "year": 1988},
    {"id": 43, "title": "NJ State Commission of Investigation — Organized Crime-Affiliated Sub-Contractors Report", "url": "https://nj.gov/sci/investigative-reports/organized-crime-affiliated-sub-contractors-on-casino-and-publicly-funded-construction-projects.shtml", "source_type": "government", "year": 1986},
    {"id": 44, "title": "Philadelphia Magazine — John-John Veasey's Life After the Philly Mob", "url": "https://www.phillymag.com/news/2010/10/29/john-john-veasey-s-life-after-the-philly-mob/", "source_type": "journalism", "year": 2010},
    {"id": 45, "title": "Philadelphia Inquirer — What to Know About John Veasey (Netflix Mob War)", "url": "https://www.inquirer.com/history/john-veasey-philadelphia-mob-netflix-20251022.html", "source_type": "journalism", "year": 2025},
    {"id": 46, "title": "CBS News 60 Minutes — Hit Man: Has a Mobster Found Redemption?", "url": "https://www.cbsnews.com/news/hit-man-has-a-mobster-found-redemption/", "source_type": "journalism", "year": 2010},
    {"id": 47, "title": "MintPress News — Hidden in Plain Sight (Cohn-Epstein Blackmail Origins)", "url": "https://www.mintpressnews.com/shocking-origins-jeffrey-epstein-blackmail-roy-cohn/260621/", "source_type": "journalism", "author": "Whitney Webb", "year": 2019},
    {"id": 48, "title": "Chicago Tribune — Trump Swam in Mob-Infested Waters", "url": "https://www.chicagotribune.com/2015/10/18/trump-swam-in-mob-infested-waters-in-early-years-as-an-nyc-developer/", "source_type": "journalism", "year": 2015},
    {"id": 49, "title": "Press of Atlantic City — Scarfo Left Mark on A.C. Casino Foundations", "url": "https://pressofatlanticcity.com/news/scarfo-left-mark-on-a-c-casino-foundations/article_0de0d140-0165-530d-bf36-154af1804766.html", "source_type": "journalism", "year": 2017},
    {"id": 50, "title": "Operation Underworld — Navy/ONI Historical Records", "url": "", "source_type": "government", "year": 1942},
    {"id": 51, "title": "Anthony Summers — Official and Confidential: The Secret Life of J. Edgar Hoover", "url": "", "source_type": "book", "author": "Anthony Summers", "year": 1993},
    {"id": 52, "title": "Crime and Cocktails — Blood in the Concrete: Fat Tony's Empire", "url": "https://crimeandcocktails.net/blood-in-the-concrete-fat-tony-salernos-empire/", "source_type": "journalism", "year": 2023},
    {"id": 53, "title": "TrumpFile.org — Trump Plaza Opens Thanks to Philadelphia Mob", "url": "https://trumpfile.org/trump-plaza-opens-in-atlantic-city/", "source_type": "journalism", "year": 2020},
    {"id": 54, "title": "Unlimited Hangout — Government by Blackmail (Epstein/Cohn/Reagan Era)", "url": "https://unlimitedhangout.com/2019/07/serie-investigativa/government-by-blackmail-jeffrey-epstein-trumps-mentor-and-the-dark-secrets-of-the-reagan-era/", "source_type": "journalism", "author": "Whitney Webb", "year": 2019},
    {"id": 55, "title": "Mob Museum — Notable Names and Historical Exhibits", "url": "https://themobmuseum.org/", "source_type": "journalism", "year": 2024},
]


# ============================================================
# EXPANDED DESCRIPTIONS — long-form dossiers for key entities
# ============================================================

_DESC_EPSTEIN = (
    "Jeffrey Edward Epstein (1953-2019). Financier, convicted sex offender, "
    "and intelligence asset whose network connected Wall Street, government, and "
    "intelligence services across multiple countries."
    "\n\n"
    "EARLY CAREER: Hired in 1974 to teach calculus and physics at the Dalton School "
    "in Manhattan by headmaster Donald Barr (OSS veteran, father of future AG William "
    "Barr) despite lacking a college degree. Joined Bear Stearns in 1976, recruited by "
    "CEO Ace Greenberg, rising to limited partner before departing in 1981 under unclear "
    "circumstances."
    "\n\n"
    "FINANCIAL ENIGMA: Established J. Epstein & Co. with Les Wexner as his only publicly "
    "confirmed client. Granted unprecedented power of attorney over Wexner's finances and "
    "a $46M Manhattan mansion (9 East 71st St, transferred for $0 in 1998). His claimed "
    "billionaire status was never independently verified — no former clients besides "
    "Wexner have been publicly identified."
    "\n\n"
    "INTELLIGENCE CONNECTIONS: FBI Confidential Human Source memo (Oct 2020, FOIA) "
    "identifies Epstein as a 'co-opted Mossad agent.' Former Israeli PM Ehud Barak "
    "visited Epstein residences (photographed entering NYC building), received $2M from "
    "Wexner Foundation, and co-founded Carbyne (Israeli emergency tech, Epstein investor) "
    "with mass surveillance applications. Robert Maxwell (Ghislaine's father, documented "
    "Mossad asset) distributed backdoored PROMIS software — Epstein inherited this "
    "intelligence network connection through Ghislaine."
    "\n\n"
    "2007 NON-PROSECUTION AGREEMENT: Palm Beach police investigation led to federal "
    "charges, but US Attorney Alexander Acosta granted an unprecedented NPA shielding "
    "unnamed co-conspirators. Victims were not notified as required by law. Acosta later "
    "told the Trump transition team he was told to back off because Epstein 'belonged to "
    "intelligence' (Daily Beast, 2019)."
    "\n\n"
    "FINANCIAL NETWORK: JPMorgan processed 4,725 suspicious Epstein-linked wires totaling "
    "$1.1B, filing SARs years late ($290M settlement, 2023). Deutsche Bank maintained "
    "Butterfly Trust accounts after JPMorgan dropped him ($75M NYDFS settlement, 2020). "
    "Leon Black paid $158M in Apollo advisory fees. Epstein attended Mega Group meetings "
    "(Wexner/Bronfman billionaire donor group)."
    "\n\n"
    "2019 ARREST AND DEATH: Re-arrested by SDNY July 6, 2019 on federal sex trafficking "
    "charges. Found dead in MCC cell August 10, 2019. Ruled suicide by hanging. Both "
    "surveillance cameras outside his cell simultaneously malfunctioned. Both assigned "
    "guards were sleeping and later falsified records. Dr. Michael Baden noted hyoid bone "
    "fracture pattern more consistent with homicidal strangulation than hanging. AG "
    "William Barr (whose father hired Epstein at Dalton) oversaw the investigation."
    "\n\n"
    "PROPERTY EMPIRE: Residences in Manhattan, Palm Beach, Paris, New Mexico (Zorro "
    "Ranch), and US Virgin Islands (Little Saint James, Great Saint James). Flight logs "
    "document hundreds of prominent visitors."
)

_DESC_WEXNER = (
    "Leslie Herbert Wexner (b. 1937). Founder of L Brands (The Limited, Victoria's "
    "Secret, Bath & Body Works, Abercrombie & Fitch). Richest man in Ohio. Mega Group "
    "co-founder. Central figure in the Epstein network through an unprecedented financial "
    "relationship."
    "\n\n"
    "EPSTEIN RELATIONSHIP: Granted Jeffrey Epstein full power of attorney over his "
    "finances — an arrangement virtually unheard of between a billionaire and a financial "
    "advisor. Transferred the largest private residence in Manhattan (9 East 71st St, "
    "valued at $46M) to Epstein for a reported $0 in 1998. The nature of Epstein's "
    "financial services to Wexner has never been adequately explained. Wexner claimed in "
    "2019 that Epstein had 'misappropriated vast sums of money' but no legal action was "
    "ever filed."
    "\n\n"
    "MEGA GROUP: Co-founded with Charles Bronfman in 1991 — a secretive annual gathering "
    "of approximately 20 of the wealthiest pro-Israel donors in North America. Epstein "
    "attended Mega Group meetings despite not qualifying for membership by wealth. The "
    "group's activities and membership are deliberately opaque."
    "\n\n"
    "VICTORIA'S SECRET PIPELINE: Multiple witnesses and victims described Epstein using "
    "Victoria's Secret modeling recruitment as a lure. Epstein carried business cards "
    "identifying himself as a VS talent scout. Wexner's knowledge of this misuse has not "
    "been conclusively established."
    "\n\n"
    "INTELLIGENCE AND MILITARY CONNECTIONS: Southern Air Transport — a documented CIA "
    "front airline used in Iran-Contra — shipped goods for The Limited. Ohio created "
    "taxpayer incentives for SAT at Wexner's behest. The Wexner Foundation paid former "
    "Israeli PM Ehud Barak $2M for vague 'research,' channeling money to Israeli military "
    "intelligence leadership."
    "\n\n"
    "CO-CONSPIRATOR DESIGNATION: Named as a co-conspirator on a 2019 FBI document "
    "related to the Epstein investigation. The scope and specifics remain partially sealed."
    "\n\n"
    "2026 HOUSE OVERSIGHT DEPOSITION: Testified before the House Oversight Committee on "
    "February 18, 2026. During the deposition, attorney Michael Levy was caught on a hot "
    "microphone threatening Wexner for answering committee questions, suggesting ongoing "
    "efforts to limit testimony about the Epstein network."
)

_DESC_BARR = (
    "William Pelham Barr (b. 1950). US Attorney General under George H.W. Bush "
    "(1991-1993) and Donald Trump (2019-2020). Connected to multiple cover-ups spanning "
    "three decades."
    "\n\n"
    "FAMILY CONNECTION TO EPSTEIN: Father Donald Barr was headmaster at the Dalton School "
    "when he hired 20-year-old Jeffrey Epstein to teach calculus and physics in 1974, "
    "despite Epstein lacking a college degree or teaching credentials. Donald Barr was an "
    "OSS (Office of Strategic Services) veteran — the WWII predecessor to the CIA. He "
    "authored a 1973 science fiction novel, 'Space Relations,' depicting a planet where "
    "oligarchs practice sexual slavery."
    "\n\n"
    "FIRST TERM AS AG (BUSH 41): Oversaw the BCCI cover-up, ensuring the largest criminal "
    "banking scandal in history resulted in minimal accountability for CIA-connected "
    "figures. Recommended pardons for Iran-Contra figures, effectively ending "
    "investigations that could have exposed CIA drug trafficking and illegal arms deals. "
    "Per Terry Reed's testimony, Barr served as CIA Director Casey's emissary to Governor "
    "Bill Clinton regarding money laundering operations through Arkansas."
    "\n\n"
    "SECOND TERM AS AG (TRUMP): Appointed by Donald Trump in 2019 — the same year Epstein "
    "was re-arrested. As Attorney General during Epstein's death at MCC on August 10, "
    "2019, Barr oversaw the investigation. Declared the death a suicide despite multiple "
    "anomalies: simultaneous camera failures, sleeping guards who falsified records, and "
    "a hyoid bone fracture pattern disputed by forensic pathologists. The investigation "
    "into Epstein's co-conspirators produced no significant indictments beyond Ghislaine "
    "Maxwell."
    "\n\n"
    "PATTERN: Barr's career spans both major cover-up eras — the BCCI/Iran-Contra period "
    "(1991-1993) and the Epstein death investigation (2019). In both cases, he held the "
    "office with authority to either expose or bury intelligence community connections to "
    "criminal networks. In both cases, investigations were curtailed."
)

_DESC_MAXWELL = (
    "Ghislaine Noelle Marion Maxwell (b. 1961). Convicted sex trafficker, socialite, "
    "and intelligence network connector. Daughter of Robert Maxwell, documented Mossad "
    "asset."
    "\n\n"
    "FAMILY BACKGROUND: Father Robert Maxwell (born Jan Ludvik Hoch) was a British media "
    "mogul and documented Israeli intelligence asset who distributed backdoored PROMIS "
    "software to governments worldwide on behalf of Mossad. Robert Maxwell died under "
    "mysterious circumstances on November 5, 1991, found floating near his yacht, the "
    "Lady Ghislaine (named after his daughter). He received an Israeli state funeral "
    "attended by six serving and former heads of Israeli intelligence. His death occurred "
    "months after the BCCI shutdown and Danny Casolaro's death — three Octopus-connected "
    "events within five months."
    "\n\n"
    "EPSTEIN OPERATION: Moved to New York after her father's death and became Jeffrey "
    "Epstein's primary companion and accomplice. Federal prosecutors established that "
    "Maxwell recruited, groomed, and trafficked underage girls for Epstein from at least "
    "1994 to 2004. She used her social connections and aristocratic credibility to "
    "normalize access to victims and provide cover for the operation."
    "\n\n"
    "TERRAMAR PROJECT: Founded the TerraMar Project, an ocean conservation nonprofit, in "
    "2012. The organization closed the day after Epstein's July 2019 arrest, raising "
    "questions about its true purpose. TerraMar had applied for diplomatic status at the "
    "United Nations."
    "\n\n"
    "ARREST AND CONVICTION: After Epstein's death, Maxwell became the FBI's most wanted "
    "target in the case. Arrested July 2, 2020 at a New Hampshire property. Convicted in "
    "December 2021 on five of six counts including sex trafficking of a minor. Sentenced "
    "to 20 years in federal prison in June 2022. Currently incarcerated."
    "\n\n"
    "INTELLIGENCE NEXUS: Maxwell served as the bridge between her father's Mossad "
    "intelligence network and Epstein's operation. Through Robert Maxwell, the family "
    "had deep connections to Israeli intelligence leadership. Multiple researchers have "
    "documented this as a continuation of the Maxwell family's intelligence role."
)

_DESC_COHN = (
    "Roy Marcus Cohn (1927-1986). Attorney, political fixer, and sexual blackmail "
    "operator who served as a nexus between organized crime, intelligence agencies, and "
    "political power for three decades."
    "\n\n"
    "MCCARTHY ERA: Chief counsel to Senator Joseph McCarthy's investigations. Prosecuted "
    "Julius and Ethel Rosenberg (executed 1953). Used his anti-communist credentials to "
    "build a network spanning law, politics, organized crime, and intelligence."
    "\n\n"
    "ORGANIZED CRIME: Attorney for Fat Tony Salerno (Genovese family boss) and Paul "
    "Castellano (Gambino family boss). Through these clients, Cohn connected Donald Trump "
    "to the construction industry's mob-controlled concrete supply. S&A Concrete — a "
    "joint Genovese-Gambino venture run by Salerno and Castellano — provided concrete for "
    "Trump Tower. NJ Casino Control Commission records document Trump's organized crime "
    "associations through Cohn."
    "\n\n"
    "TRUMP MENTORSHIP (1973-1986): Became Donald Trump's attorney and mentor in 1973, "
    "when Trump retained Cohn to fight federal housing discrimination charges. For 13 "
    "years, Cohn served as Trump's fixer, teaching him tactics of aggressive denial, "
    "counterattack, and media manipulation. Cohn connected Trump to New York's political "
    "and social elite, mob figures, and intelligence-adjacent networks."
    "\n\n"
    "SEXUAL BLACKMAIL OPERATIONS: Ran sexual blackmail operations in coordination with "
    "J. Edgar Hoover and CIA Director William Casey, with whom he had daily phone calls. "
    "Cohn's blackmail network operated through parties at his townhouse and at Studio 54, "
    "where compromising situations were arranged and documented. This continued the "
    "Hoover-Lansky tradition of sexual compromise as a control mechanism."
    "\n\n"
    "INTELLIGENCE CONNECTIONS: Maintained daily phone contact with CIA Director William "
    "Casey. This direct line between a mob-connected political fixer and the CIA Director "
    "illustrates the integration of organized crime, intelligence, and political power "
    "that characterizes this network."
    "\n\n"
    "DEATH: Disbarred in 1986 for ethical violations. Died of AIDS complications in "
    "August 1986 while publicly denying his diagnosis and his homosexuality."
)

_DESC_THIEL = (
    "Peter Andreas Thiel (b. 1967). Venture capitalist, technology entrepreneur, and "
    "political operative who bridges Silicon Valley, the intelligence community, and "
    "conservative politics."
    "\n\n"
    "PAYPAL: Co-founded PayPal in 1998, creating one of the first major digital payment "
    "platforms. The 'PayPal Mafia' — Thiel, Elon Musk, Reid Hoffman, and others — went "
    "on to shape Silicon Valley's trajectory."
    "\n\n"
    "PALANTIR TECHNOLOGIES: Co-founded Palantir in 2003 with Alex Karp and others. The "
    "company received early seed funding from In-Q-Tel, the CIA's venture capital arm. "
    "Palantir became a primary data analytics contractor for the CIA, NSA, FBI, and "
    "military. Researchers have documented Palantir as the private-sector successor to "
    "DARPA's Total Information Awareness program, which Congress defunded in 2003 after "
    "public outcry over mass surveillance. The capabilities Congress rejected were rebuilt "
    "in the private sector with intelligence community backing."
    "\n\n"
    "FACEBOOK INVESTMENT: Made a $500,000 angel investment in Facebook in 2004, becoming "
    "the company's first outside investor and joining its board. DARPA's LifeLog program "
    "— designed to build a database of a person's entire existence — was cancelled "
    "February 4, 2004, the same day Facebook launched. Thiel's simultaneous involvement "
    "with CIA-funded Palantir and the world's largest personal data collection platform "
    "is structurally significant."
    "\n\n"
    "SURVEILLANCE INFRASTRUCTURE: Through Palantir, Thiel built the analytical layer of "
    "the modern surveillance state. Palantir's software integrates data from multiple "
    "intelligence sources, enabling pattern analysis across communications, financial "
    "records, travel data, and social networks at scale."
    "\n\n"
    "POLITICAL INFLUENCE: Bilderberg Group steering committee member. Major Republican "
    "donor. Backed Trump's 2016 campaign. Funded the Hogan v. Gawker lawsuit that "
    "destroyed Gawker Media — demonstrating willingness to use financial power to "
    "eliminate critical press."
)

_DESC_GOTTI = (
    "John Joseph Gotti Jr. (1940-2002). 'The Teflon Don' and 'The Dapper Don.' "
    "Boss of the Gambino crime family from 1985 until his conviction in 1992."
    "\n\n"
    "RISE TO POWER: On December 16, 1985, Gotti orchestrated the assassination of "
    "Gambino boss Paul Castellano outside Sparks Steak House in midtown Manhattan — "
    "one of the most brazen mob hits in history. Castellano and underboss Thomas "
    "Bilotti were shot by gunmen in trench coats while Gotti watched from a car "
    "across the street. Gotti became boss without Commission approval, violating "
    "the Mafia's fundamental governance structure."
    "\n\n"
    "THE TEFLON DON: Acquitted three times on federal racketeering charges between "
    "1986 and 1990, earning the nickname 'Teflon Don' because charges seemed to "
    "slide off. His acquittals were later attributed to jury tampering and witness "
    "intimidation. He cultivated a celebrity persona — Armani suits, media "
    "appearances, lavish Fourth of July block parties in Ozone Park, Queens."
    "\n\n"
    "ROY COHN CONNECTION: Roy Cohn represented Gotti, adding him to a client list "
    "that already included Fat Tony Salerno (Genovese boss) and Castellano himself "
    "(the man Gotti would later murder). Through Cohn, the same attorney connected "
    "the bosses of two rival families AND Donald Trump."
    "\n\n"
    "TRUMP CASINO CONNECTION: Robert LiButti, a Gambino associate caught on FBI "
    "wiretap calling Gotti 'my boss,' lost $12 million gambling at Trump casinos. "
    "Trump Plaza was fined $450,000 for funneling $1.6M in luxury cars to LiButti "
    "and $200,000 for removing Black and female dealers at LiButti's demand."
    "\n\n"
    "PHILADELPHIA CONNECTION: John Stanfa, the Gambino-connected boss of the "
    "Philadelphia crime family, had brothers who were made Gambino members under "
    "Gotti's regime. When Stanfa was installed in Philadelphia, it was with Gambino "
    "backing."
    "\n\n"
    "DOWNFALL: Underboss Sammy 'The Bull' Gravano turned government witness in 1991, "
    "providing devastating testimony. Gotti was convicted June 23, 1992 on 13 "
    "counts including five murders and sentenced to life without parole. He died "
    "of throat cancer in USP Marion on June 10, 2002. His conviction marked the "
    "symbolic end of the Italian-American Mafia's golden age."
)

_DESC_LANSKY = (
    "Meyer Suchowljansky (1902-1983). 'The Mob's Accountant.' Architect of the "
    "National Crime Syndicate and the most important bridge node between organized "
    "crime and the intelligence apparatus."
    "\n\n"
    "NATIONAL CRIME SYNDICATE: With Lucky Luciano, Lansky created the organizational "
    "model for American organized crime — a national corporation transcending ethnic "
    "lines. The Commission (1931) governed the Five Families. Murder, Inc. served as "
    "the enforcement arm. Lansky served as the financial brain for all of it."
    "\n\n"
    "OPERATION UNDERWORLD (1942-1945): Served as intermediary when the Office of "
    "Naval Intelligence recruited the mob to secure New York's waterfront during WWII. "
    "Lansky connected ONI to Lucky Luciano in prison, who ordered his entire network "
    "to prevent sabotage and strikes. Not a single incident occurred for the rest of "
    "the war. The mob also provided intelligence for the Sicily invasion. This "
    "established the structural relationship between organized crime and the national "
    "security state that has never been fully severed."
    "\n\n"
    "HOOVER BLACKMAIL: Obtained compromising photographs of FBI Director J. Edgar "
    "Hoover, per multiple witnesses including Susan Rosenstiel (testimony under oath "
    "to NY State Crime Committee) and two former OSS officials. For three decades, "
    "Hoover refused to acknowledge organized crime existed — 400 FBI agents assigned "
    "to communists, 4 to organized crime. Whether blackmail was the cause, the effect "
    "was identical: Lansky operated with de facto FBI protection."
    "\n\n"
    "ISRAEL AND INTELLIGENCE: Arranged arms smuggling for the Haganah (pre-IDF) in "
    "1945-48, using Albert Anastasia's control of the longshoremen to load weapons "
    "onto ships. Worked directly with Rafi Eitan (legendary Israeli intelligence "
    "operative who captured Eichmann and later ran Jonathan Pollard). Through Tibor "
    "Rosenbaum's Banque de Credit International in Geneva, Lansky laundered criminal "
    "proceeds through the same institution that handled 90% of Israeli Defense "
    "Ministry arms purchases."
    "\n\n"
    "CUBA AND LAS VEGAS: Partnered with Fulgencio Batista to build Havana's casino "
    "empire. Organized the 1946 Havana Conference at the Hotel Nacional — the "
    "national syndicate's postwar summit, attended by Luciano, Costello, Genovese, "
    "Bonanno, and others. When Castro's revolution destroyed Cuban operations, Lansky "
    "pivoted to Las Vegas, which he had been developing since assigning Bugsy Siegel "
    "to build the Flamingo Hotel in 1946."
    "\n\n"
    "OFFSHORE BANKING: Pioneered the use of Swiss banks (from 1932), Bahamas shell "
    "companies, and Caribbean tax havens for money laundering — creating the "
    "infrastructure later adopted by intelligence agencies for covert finance. This "
    "architecture survived Lansky and was used by successor networks."
    "\n\n"
    "LEGACY: Died January 15, 1983, officially leaving $57,000. FBI estimated $300M "
    "hidden worldwide. The money was never found. But the infrastructure — offshore "
    "routes, intelligence relationships, blackmail methodology, Israeli connections "
    "— was institutional, not personal. It persisted through Rafi Eitan to Robert "
    "Maxwell to Ghislaine Maxwell to Jeffrey Epstein."
)

_DESC_BRUNO = (
    "Angelo Bruno (1910-1980). 'The Docile Don' and 'The Gentle Don.' Boss of the "
    "Philadelphia crime family from 1959 until his assassination in 1980. Commission "
    "member and Meyer Lansky partner."
    "\n\n"
    "TERRITORY: Controlled organized crime operations throughout the greater "
    "Philadelphia metropolitan area and South Jersey from his rowhouse at 934 Snyder "
    "Avenue in South Philadelphia's Lower Moyamensing neighborhood. His influence "
    "extended through the Italian Market on 9th Street, Passyunk Avenue, and the "
    "entire South Philadelphia Italian-American community."
    "\n\n"
    "PHILOSOPHY: Bruno treated violence as a business decision with a cost-benefit "
    "analysis. He preferred bribery over bullets, paying off politicians, police, "
    "and judges. He banned family involvement in narcotics, fearing the long "
    "sentences and law enforcement attention. Over 21 years, he successfully avoided "
    "the scrutiny that plagued other families. This philosophy ultimately killed him "
    "— subordinates wanting drug money conspired against him."
    "\n\n"
    "LANSKY PARTNERSHIP: Partnered with Meyer Lansky on casino operations including "
    "the Colony Sports Club in London. The Bruno-Lansky relationship was a gambling "
    "partnership connecting Philadelphia's territorial control to Lansky's global "
    "financial network."
    "\n\n"
    "COMMISSION SEAT: First Philadelphia boss to hold an influential seat on the "
    "Commission, secured through his close friendship with Carlo Gambino. This gave "
    "Philadelphia unprecedented standing in the national syndicate."
    "\n\n"
    "ASSASSINATION: On March 21, 1980, a shotgun blast killed Bruno as he sat in "
    "his car outside 934 Snyder Avenue. His own consigliere, Antonio 'Tony Bananas' "
    "Caponigro, ordered the hit. Caponigro had been lied to by Genovese boss Frank "
    "'Funzi' Tieri, who said the Commission approved — it had not. Caponigro was "
    "found tortured and dead in a Bronx car trunk weeks later. Bruno's murder "
    "triggered a succession war that claimed 20+ lives."
)

_DESC_VEASEY = (
    "John 'John-John' Veasey (b. 1967). Philadelphia mob enforcer turned FBI "
    "informant whose testimony brought down boss John Stanfa."
    "\n\n"
    "BACKGROUND: Born in South Philadelphia to Walter Veasey (violent alcoholic, "
    "found dead in a hotel 1970) and Sophia Maria Cuticchia (Sicilian native, died "
    "of heart attack when John was 16). Youngest of five children. Grew up in the "
    "heart of Philadelphia crime family territory during the Bruno and Scarfo eras."
    "\n\n"
    "MOB CAREER: Became an enforcer and triggerman for boss John Stanfa during the "
    "Stanfa-Merlino war (1992-1994). Admitted to participating in multiple murders "
    "including Michael 'Mikey Chang' Ciancaglini and Frank Baldino Sr."
    "\n\n"
    "ASSASSINATION ATTEMPT: On January 14, 1994, Stanfa associates Frank Martines "
    "and Vincent 'Al Pajamas' Pagano attempted to kill Veasey in an apartment above "
    "a meat store. He was shot four times — three times in the head with a small-"
    "caliber pistol, once in the chest — and stabbed seven times. Doctors said years "
    "of being hit with metal pipes and baseball bats had built up protective calcium "
    "deposits on his skull, which deflected the bullets. Despite his injuries, Veasey "
    "wrestled a knife from an attacker, stabbed him in the face, and escaped."
    "\n\n"
    "FBI INFORMANT: His brother Billy recommended he cooperate with the FBI. Veasey's "
    "testimony was devastating — the judge was amused, the jury loved him. He helped "
    "convict Stanfa and seven associates, earning Stanfa five consecutive life "
    "sentences. Hours before Veasey took the stand, his brother Billy was shot and "
    "killed on the 1700 block of Oregon Avenue in South Philadelphia."
    "\n\n"
    "AFTERMATH: Entered witness protection. His story was featured on CBS 60 Minutes "
    "and Netflix's Mob War (2025). Lives under an assumed name."
)

_DESC_TRUMP = (
    "Donald John Trump (b. 1946). 45th and 47th President of the United States. Real "
    "estate developer and media figure whose career intersects organized crime, "
    "intelligence operations, and the Epstein network through decades of documented "
    "connections."
    "\n\n"
    "ROY COHN MENTORSHIP (1973-1986): Retained attorney Roy Cohn in 1973 to fight "
    "federal housing discrimination charges. For 13 years, Cohn served as Trump's fixer, "
    "connecting him to organized crime figures, intelligence operatives, and political "
    "power brokers. Through Cohn, Trump gained access to Fat Tony Salerno (Genovese "
    "family boss) and Paul Castellano (Gambino family boss), whose S&A Concrete supplied "
    "Trump Tower construction. NJ Casino Control Commission records document these "
    "organized crime associations."
    "\n\n"
    "RESORTS INTERNATIONAL (1987): Purchased Resorts International, a casino company "
    "with documented intelligence community connections. Resorts operated through Intertel "
    "(International Intelligence Inc.), a private intelligence firm staffed by former FBI "
    "and CIA personnel. The company had historical ties to Meyer Lansky's gambling "
    "operations. Later reorganized as Trump Taj Mahal."
    "\n\n"
    "EPSTEIN RELATIONSHIP (~1987-2004): Social relationship documented through quotes, "
    "photographs, party footage, and flight logs. In a 2002 New York Magazine profile, "
    "Trump stated: 'I've known Jeff for 15 years. Terrific guy. He's a lot of fun to be "
    "with. It is even said that he likes beautiful women as much as I do, and many of "
    "them are on the younger side.' Trump claims to have banned Epstein from Mar-a-Lago, "
    "though the timing is disputed. Epstein's Palm Beach residence was approximately one "
    "mile from Mar-a-Lago."
    "\n\n"
    "KEY APPOINTMENTS: Appointed Alexander Acosta — the US Attorney who gave Epstein the "
    "2007 NPA — as Secretary of Labor (2017-2019). Appointed William Barr — whose father "
    "hired Epstein at Dalton — as Attorney General (2019-2020). Barr was AG when Epstein "
    "died in federal custody."
    "\n\n"
    "DEUTSCHE BANK: After every major US bank refused to lend to Trump following multiple "
    "bankruptcies, Deutsche Bank provided over $340M in loans. Deutsche Bank was later "
    "fined for Russian mirror trading (money laundering) and for maintaining Epstein's "
    "Butterfly Trust accounts."
    "\n\n"
    "FELIX SATER AND BAYROCK GROUP: Partnered with Felix Sater through Bayrock Group on "
    "Trump SoHo and other projects. Sater, a convicted felon with documented ties to "
    "Russian organized crime, was also an FBI informant. His business card read 'Senior "
    "Advisor to Donald Trump.' Bayrock connected Trump to Russian and Central Asian money "
    "flows documented in multiple lawsuits."
)


# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # ---- People (expanded dossiers) ----
    {"name": "Jeffrey Epstein", "entity_type": "person", "description": _DESC_EPSTEIN, "aliases": "", "metadata": {"photo_url": "/static/photos/epstein.jpg", "birth_date": "1953-01-20", "death_date": "2019-08-10", "nationality": "American", "status": "deceased"}},
    {"name": "Ghislaine Maxwell", "entity_type": "person", "description": _DESC_MAXWELL, "aliases": "", "metadata": {"photo_url": "/static/photos/maxwell.jpg", "birth_date": "1961-12-25", "nationality": "British-American", "status": "incarcerated"}},
    {"name": "Robert Maxwell", "entity_type": "person", "description": "Media mogul, Mossad asset. Sold PROMIS software backdoored by Israeli intelligence to governments worldwide. Died 1991.", "aliases": "Jan Ludvik Hoch", "metadata": {"photo_url": "/static/photos/robert_maxwell.jpg", "birth_date": "1923-06-10", "death_date": "1991-11-05", "nationality": "British", "status": "deceased"}},
    {"name": "Les Wexner", "entity_type": "person", "description": _DESC_WEXNER, "aliases": "Leslie Wexner", "metadata": {"photo_url": "/static/photos/wexner.jpg", "birth_date": "1937-09-08", "nationality": "American", "status": "alive"}},
    {"name": "Ehud Barak", "entity_type": "person", "description": "Former Israeli PM and IDF Chief of Staff. Visited Epstein's residences. Wexner Foundation paid $2M for vague 'research.' Carbyne co-founder.", "aliases": "", "metadata": {"photo_url": "/static/photos/barak.jpg", "birth_date": "1942-02-12", "nationality": "Israeli", "status": "alive"}},
    {"name": "Peter Thiel", "entity_type": "person", "description": _DESC_THIEL, "aliases": "", "metadata": {"photo_url": "/static/photos/thiel.jpg", "birth_date": "1967-10-11", "nationality": "American", "status": "alive"}},
    {"name": "Alex Karp", "entity_type": "person", "description": "Palantir CEO. PhD from Frankfurt School lineage. Runs Palantir's intelligence community relationships.", "aliases": "", "metadata": {"photo_url": "/static/photos/karp.jpg", "birth_date": "1967-10-02", "nationality": "American", "status": "alive"}},
    {"name": "William Barr", "entity_type": "person", "description": _DESC_BARR, "aliases": "Bill Barr", "metadata": {"photo_url": "/static/photos/barr.jpg", "birth_date": "1950-05-23", "nationality": "American", "status": "alive"}},
    {"name": "Donald Barr", "entity_type": "person", "description": "Headmaster at Dalton School who hired Epstein to teach (1974). OSS veteran. Father of William Barr. Authored 'Space Relations' (1973), a sci-fi novel depicting oligarchs practicing sexual slavery in space.", "aliases": "", "metadata": {"photo_url": "/static/photos/donald_barr.jpg", "birth_date": "1921-08-08", "death_date": "2004-02-05", "nationality": "American", "status": "deceased"}},
    {"name": "William Casey", "entity_type": "person", "description": "CIA Director 1981-87. Iran-Contra architect. Daily calls with Roy Cohn. BCCI meetings alleged. Mena/Arkansas operations.", "aliases": "Bill Casey", "metadata": {"photo_url": "/static/photos/casey.jpg", "birth_date": "1913-03-13", "death_date": "1987-05-06", "nationality": "American", "status": "deceased"}},
    {"name": "Roy Cohn", "entity_type": "person", "description": _DESC_COHN, "aliases": "", "metadata": {"photo_url": "/static/photos/cohn.jpg", "birth_date": "1927-02-20", "death_date": "1986-08-02", "nationality": "American", "status": "deceased"}},
    {"name": "Robert Keith Gray", "entity_type": "person", "description": "Hill & Knowlton CEO. CIA blackmail specialist per DeCamp. George Town Club president. Reagan deputy comms under Casey.", "aliases": "", "metadata": {"photo_url": "/static/photos/robert_keith_gray.jpg"}},
    {"name": "Craig Spence", "entity_type": "person", "description": "DC lobbyist who ran bugged apartments. Entered Bush White House with minors. Predicted CIA would kill him. Found dead, ruled suicide.", "aliases": ""},
    {"name": "Edwin Wilson", "entity_type": "person", "description": "CIA/Naval Intelligence officer. Ran sexual blackmail operations targeting Congress in 1970s with Terpil.", "aliases": ""},
    {"name": "Frank Terpil", "entity_type": "person", "description": "CIA officer, Wilson's partner. Described Wilson's congressional blackmail operation in detail to journalist Hougan.", "aliases": ""},
    {"name": "J. Edgar Hoover", "entity_type": "person", "description": "FBI Director 1924-1972. Compromised by Lansky photographs. Refused to investigate organized crime for decades.", "aliases": "", "metadata": {"photo_url": "/static/photos/hoover.jpg", "birth_date": "1895-01-01", "death_date": "1972-05-02", "nationality": "American", "status": "deceased"}},
    {"name": "James Angleton", "entity_type": "person", "description": "CIA counterintelligence chief. Held Hoover compromise material. Managed CIA-Mossad relationship.", "aliases": "", "metadata": {"photo_url": "/static/photos/angleton.jpg", "birth_date": "1917-12-09", "death_date": "1987-05-12", "nationality": "American", "status": "deceased"}},
    {"name": "Meyer Lansky", "entity_type": "person", "description": _DESC_LANSKY, "aliases": "", "metadata": {"photo_url": "/static/photos/lansky.jpg", "birth_date": "1902-07-04", "death_date": "1983-01-15", "nationality": "American", "status": "deceased"}},
    {"name": "Kamal Adham", "entity_type": "person", "description": "CIA's principal Middle East liaison (mid-1960s-1979). Secret lead front-man for BCCI takeover of First American Bank.", "aliases": "", "metadata": {"photo_url": "/static/photos/adham.jpg", "nationality": "Saudi", "status": "deceased"}},
    {"name": "Agha Hasan Abedi", "entity_type": "person", "description": "BCCI founder. Secret meetings with Casey alleged. Built the criminal banking empire used by CIA.", "aliases": ""},
    {"name": "Clark Clifford", "entity_type": "person", "description": "Washington power broker. Front-man for BCCI's acquisition of First American Bank. Indicted 1992.", "aliases": "", "metadata": {"photo_url": "/static/photos/clifford.jpg", "birth_date": "1906-12-25", "death_date": "1998-10-10", "nationality": "American", "status": "deceased"}},
    {"name": "Marc Rich", "entity_type": "person", "description": "Commodities trader, Mossad's primary oil source for 20 years. Founded Glencore. Pardoned by Clinton.", "aliases": "", "metadata": {"photo_url": "/static/photos/marc_rich.jpg", "birth_date": "1934-12-18", "death_date": "2013-06-26", "nationality": "American-Israeli-Spanish", "status": "deceased"}},
    {"name": "Jackson Stephens", "entity_type": "person", "description": "Arkansas oligarch. Bankrolled Clinton's rise. Worthen Bank provided $3.5M campaign credit. Rose Law Firm client.", "aliases": ""},
    {"name": "Barry Seal", "entity_type": "person", "description": "CIA drug pilot operating out of Mena Airport. Used Southern Air Transport aircraft. Assassinated 1986.", "aliases": "Adler Berriman Seal", "metadata": {"photo_url": "/static/photos/barry_seal.jpg", "birth_date": "1939-07-16", "death_date": "1986-02-19", "nationality": "American", "status": "deceased"}},
    {"name": "Bill Hamilton", "entity_type": "person", "description": "INSLAW founder. Developed PROMIS software, which DOJ stole and distributed to intelligence agencies worldwide.", "aliases": "William Hamilton"},
    {"name": "Danny Casolaro", "entity_type": "person", "description": "Journalist investigating INSLAW/PROMIS and 'The Octopus.' Found dead in hotel bathtub 1991, ruled suicide. Arms slashed 10+ times.", "aliases": "", "metadata": {"photo_url": "/static/photos/casolaro.jpg", "birth_date": "1947-06-16", "death_date": "1991-08-10", "nationality": "American", "status": "deceased"}},
    {"name": "Adnan Khashoggi", "entity_type": "person", "description": "Saudi arms dealer. Iran-Contra middleman. BCCI Monte Carlo client. Connected to Epstein network.", "aliases": "", "metadata": {"photo_url": "/static/photos/khashoggi.jpg", "birth_date": "1935-07-25", "death_date": "2017-06-06", "nationality": "Saudi", "status": "deceased"}},
    {"name": "Richard Helms", "entity_type": "person", "description": "CIA Director. Ordered MKULTRA files destroyed 1973. Drafted legal language protecting BCCI front-men despite later denials.", "aliases": "", "metadata": {"photo_url": "/static/photos/helms.jpg", "birth_date": "1913-03-30", "death_date": "2002-10-22", "nationality": "American", "status": "deceased"}},
    {"name": "John Poindexter", "entity_type": "person", "description": "National Security Advisor under Reagan. Later directed DARPA's Total Information Awareness program.", "aliases": "", "metadata": {"photo_url": "/static/photos/poindexter.jpg", "nationality": "American", "status": "alive"}},
    {"name": "Leon Black", "entity_type": "person", "description": "Apollo Global Management co-founder. Paid Epstein $158M in fees. Resigned from Apollo chairmanship.", "aliases": "", "metadata": {"birth_date": "1951-07-31", "nationality": "American", "status": "alive"}},
    {"name": "Hillary Clinton", "entity_type": "person", "description": "Rose Law Firm partner. Firm represented both Systematics and assisted BCCI's US entry.", "aliases": "", "metadata": {"photo_url": "/static/photos/hillary_clinton.jpg", "birth_date": "1947-10-26", "nationality": "American", "status": "alive"}},
    {"name": "Bill Clinton", "entity_type": "person", "description": "Arkansas Governor, later President. Sent AR National Guard to Honduras. Pardoned Marc Rich. Epstein flight logs document 26+ flights on Epstein's aircraft.", "aliases": "William Clinton", "metadata": {"photo_url": "/static/photos/clinton.jpg", "birth_date": "1946-08-19", "nationality": "American", "status": "alive"}},

    # ---- New people ----
    {"name": "Donald Trump", "entity_type": "person", "description": _DESC_TRUMP, "aliases": "", "metadata": {"photo_url": "/static/photos/trump.jpg", "birth_date": "1946-06-14", "nationality": "American", "status": "alive"}},
    {"name": "Fat Tony Salerno", "entity_type": "person", "description": (
        "Anthony 'Fat Tony' Salerno (1911-1992). Boss of the Genovese crime family, one "
        "of the most powerful organized crime figures in New York. Roy Cohn served as "
        "Salerno's attorney, connecting him to Donald Trump and the political establishment. "
        "Salerno and Paul Castellano (Gambino family) jointly controlled S&A Concrete, "
        "which held a monopoly on concrete deliveries for large construction projects in "
        "Manhattan. S&A Concrete provided concrete for Trump Tower's construction. "
        "Convicted in the 1986 Mafia Commission Trial and sentenced to 100 years. "
        "Died in federal prison in 1992."
    ), "aliases": "Anthony Salerno", "metadata": {"photo_url": "/static/photos/salerno.jpg", "birth_date": "1911-08-15", "death_date": "1992-07-27", "nationality": "American", "status": "deceased"}},
    {"name": "Paul Castellano", "entity_type": "person", "description": (
        "Paul Castellano (1915-1985). Boss of the Gambino crime family. Jointly controlled "
        "S&A Concrete with Fat Tony Salerno (Genovese family), providing concrete for "
        "major Manhattan construction projects including Trump Tower. Roy Cohn represented "
        "both Castellano and Salerno. Assassinated outside Sparks Steak House in Manhattan "
        "on December 16, 1985, in a hit ordered by John Gotti, who succeeded him as "
        "Gambino boss."
    ), "aliases": "Big Paul", "metadata": {"photo_url": "/static/photos/castellano.jpg", "birth_date": "1915-06-26", "death_date": "1985-12-16", "nationality": "American", "status": "deceased"}},
    {"name": "Felix Sater", "entity_type": "person", "description": (
        "Felix Henry Sater (b. 1966). Russian-American businessman, convicted felon, and "
        "FBI informant. Managing director of Bayrock Group, which partnered with Trump on "
        "Trump SoHo and other projects. Born in Moscow, emigrated to the US as a child. "
        "Convicted in 1998 in connection with a $40 million stock fraud scheme tied to the "
        "Russian mafia, later became a cooperating witness for the FBI and CIA on national "
        "security matters. His business card at Bayrock read 'Senior Advisor to Donald "
        "Trump.' Despite his criminal record and organized crime ties, Sater maintained "
        "access to Trump Organization offices in Trump Tower. Documented in multiple "
        "lawsuits, congressional testimony, and investigative journalism as a key conduit "
        "between Trump business operations and Russian-connected money flows."
    ), "aliases": "Felix Satter", "metadata": {"birth_date": "1966-03-02", "nationality": "American", "status": "alive"}},
    {"name": "Alexander Acosta", "entity_type": "person", "description": (
        "Robert Alexander Acosta (b. 1969). US Attorney for the Southern District of "
        "Florida (2005-2009). US Secretary of Labor (2017-2019)."
        "\n\n"
        "As US Attorney, Acosta negotiated the 2007 Non-Prosecution Agreement with "
        "Jeffrey Epstein — an unprecedented deal that allowed Epstein to plead guilty to "
        "state solicitation charges, serve 13 months in county jail with work release "
        "privileges, and register as a sex offender, while shielding unnamed "
        "co-conspirators from federal prosecution. Victims were not notified as required "
        "by the Crime Victims' Rights Act (later ruled a violation by Judge Kenneth Marra "
        "in 2019)."
        "\n\n"
        "According to the Daily Beast (2019), Acosta told the Trump transition team during "
        "his vetting for Labor Secretary that he had been told to back off the Epstein "
        "case because Epstein 'belonged to intelligence.' Despite this disclosure, Trump "
        "appointed Acosta as Secretary of Labor in 2017."
        "\n\n"
        "Resigned from the Labor Secretary position in July 2019, days after renewed "
        "scrutiny of the NPA following Epstein's re-arrest by SDNY."
    ), "aliases": "", "metadata": {"photo_url": "/static/photos/acosta.jpg", "birth_date": "1969-01-16", "nationality": "American", "status": "alive"}},
    {"name": "Alan Dershowitz", "entity_type": "person", "description": (
        "Alan Morton Dershowitz (b. 1938). Harvard Law School professor emeritus. "
        "Constitutional lawyer. Defense attorney for Jeffrey Epstein during the 2007 NPA "
        "negotiations."
        "\n\n"
        "Served as Epstein's defense counsel during negotiations that produced the "
        "unprecedented Non-Prosecution Agreement. Named by Virginia Roberts Giuffre as a "
        "participant in Epstein's sex trafficking operation. Dershowitz and Giuffre filed "
        "competing defamation claims; Giuffre's suit was settled in 2022 (terms "
        "undisclosed). Dershowitz initially denied ever meeting Giuffre, later acknowledged "
        "meeting her but denied any sexual contact."
        "\n\n"
        "Documented as a frequent guest at Epstein properties, appearing in flight logs "
        "and witness testimony. Published academic arguments advocating for lowering the "
        "statutory age of consent. Connected to both Trump and Epstein legal circles — "
        "served on Trump's first impeachment defense team in 2020."
        "\n\n"
        "Flight logs and witness depositions place Dershowitz at Epstein's residences in "
        "Manhattan, Palm Beach, New Mexico, and the US Virgin Islands on multiple "
        "occasions."
    ), "aliases": "", "metadata": {"photo_url": "/static/photos/dershowitz.jpg", "birth_date": "1938-09-01", "nationality": "American", "status": "alive"}},

    # ---- Organized crime figures ----
    {"name": "John Gotti", "entity_type": "person", "description": _DESC_GOTTI, "aliases": "The Teflon Don, The Dapper Don", "metadata": {"photo_url": "/static/photos/gotti.jpg", "birth_date": "1940-10-27", "death_date": "2002-06-10", "nationality": "American", "status": "deceased"}},
    {"name": "Angelo Bruno", "entity_type": "person", "description": _DESC_BRUNO, "aliases": "The Docile Don, The Gentle Don", "metadata": {"birth_date": "1910-05-21", "death_date": "1980-03-21", "nationality": "American", "status": "deceased"}},
    {"name": "Nicky Scarfo", "entity_type": "person", "description": (
        "Nicodemo Domenico Scarfo Sr. (1929-2017). 'Little Nicky.' Boss of the Philadelphia "
        "crime family from 1981 to 1991, succeeding Angelo Bruno after the bloody succession "
        "war. Unlike Bruno's restraint, Scarfo ruled through terror — responsibility for over "
        "30 murders during his reign. Controlled Atlantic City construction through Scarf Inc. "
        "Kenneth Shapiro served as his financial advisor and front man for casino-area land "
        "deals, including properties sold to Donald Trump for casino development. Salvatore "
        "Testa, 'The Crown Prince,' also sold land to Trump's casino operations before Scarfo "
        "had him murdered. Convicted of first-degree murder, racketeering, and extortion in "
        "1988. Died in federal prison in 2017."
    ), "aliases": "Little Nicky, Nicodemo Scarfo", "metadata": {"photo_url": "/static/photos/scarfo.jpg", "birth_date": "1929-03-08", "death_date": "2017-01-13", "nationality": "American", "status": "deceased"}},
    {"name": "John Stanfa", "entity_type": "person", "description": (
        "Giovanni Stanfa (b. 1940). Boss of the Philadelphia crime family from 1991 to 1994, "
        "installed with Gambino family backing after the Scarfo era. Born in Caccamo, Sicily. "
        "Was the driver for Angelo Bruno on the night of his 1980 assassination — a bullet "
        "grazed Stanfa's shoulder, but he was later cleared. Led a bloody war against the "
        "young faction led by Joey Merlino and Michael Ciancaglini. Convicted of racketeering "
        "and three murders in 1995 based largely on testimony from his own enforcer, "
        "John-John Veasey. Sentenced to five consecutive life terms."
    ), "aliases": "Giovanni Stanfa", "metadata": {"birth_date": "1940-09-07", "nationality": "American-Italian", "status": "incarcerated"}},
    {"name": "Joey Merlino", "entity_type": "person", "description": (
        "Joseph Salvatore Merlino (b. 1962). 'Skinny Joey.' Boss of the Philadelphia crime "
        "family from 1999, succeeding the Stanfa era after winning the bloody Stanfa-Merlino "
        "war. Son of Salvatore 'Chuckie' Merlino, underboss under Scarfo. Led the young "
        "faction against Stanfa with Michael Ciancaglini. Survived being shot in 1993. "
        "Convicted of racketeering in 2001, sentenced to 14 years. Acquitted of murder charges "
        "in 2018 after a second trial. Considered the last traditional boss of the Philadelphia "
        "family."
    ), "aliases": "Skinny Joey", "metadata": {"photo_url": "/static/photos/merlino.jpg", "birth_date": "1962-03-16", "nationality": "American", "status": "alive"}},
    {"name": "John-John Veasey", "entity_type": "person", "description": _DESC_VEASEY, "aliases": "John Veasey", "metadata": {"birth_date": "1967-01-01", "nationality": "American", "status": "alive"}},
    {"name": "Lucky Luciano", "entity_type": "person", "description": (
        "Charles 'Lucky' Luciano (1897-1962). Founder of the modern American Mafia. With "
        "Meyer Lansky, created the National Crime Syndicate — organizing Italian and Jewish "
        "criminal enterprises into a corporate structure. Established The Commission in 1931 "
        "to govern the Five Families. Created Murder, Incorporated as the national enforcement "
        "arm. Imprisoned in 1936. Released in 1946 through Operation Underworld — ONI recruited "
        "the mob through Lansky to secure NYC waterfront and provide intelligence for the Sicily "
        "invasion. Deported to Italy. Organized the 1946 Havana Conference at the Hotel "
        "Nacional. Died in Naples, 1962."
    ), "aliases": "Charles Luciano, Salvatore Lucania", "metadata": {"photo_url": "/static/photos/luciano.jpg", "birth_date": "1897-11-24", "death_date": "1962-01-26", "nationality": "American-Italian", "status": "deceased"}},
    {"name": "Bugsy Siegel", "entity_type": "person", "description": (
        "Benjamin 'Bugsy' Siegel (1906-1947). Murder Incorporated co-founder and the man who "
        "built Las Vegas. Childhood friend and lifelong partner of Meyer Lansky. Sent west by "
        "the syndicate to establish operations in California and Las Vegas. Built the Flamingo "
        "Hotel (1946), transforming Las Vegas from a desert outpost into the mob's legitimate "
        "front. Cost overruns and skimming led the Commission to approve his murder. Shot "
        "through the window of his Beverly Hills home on June 20, 1947. Frankie Carbo was "
        "one of several suspected triggermen. Within 20 minutes of the shooting, Lansky "
        "associates walked into the Flamingo and took control."
    ), "aliases": "Benjamin Siegel", "metadata": {"photo_url": "/static/photos/siegel.jpg", "birth_date": "1906-02-28", "death_date": "1947-06-20", "nationality": "American", "status": "deceased"}},
    {"name": "Sammy Gravano", "entity_type": "person", "description": (
        "Salvatore 'Sammy the Bull' Gravano (b. 1945). Gambino family underboss under John "
        "Gotti. The highest-ranking member of the American Mafia to turn government witness. "
        "Admitted to involvement in 19 murders. His 1991 decision to cooperate with the FBI "
        "provided devastating testimony that convicted Gotti on June 23, 1992. Entered "
        "witness protection but was expelled after being caught running an ecstasy ring in "
        "Arizona. His testimony marked the symbolic end of the Mafia's ability to maintain "
        "omerta. Lives in Arizona under his own name after serving his drug sentence."
    ), "aliases": "Sammy the Bull", "metadata": {"photo_url": "/static/photos/gravano.jpg", "birth_date": "1945-03-12", "nationality": "American", "status": "alive"}},
    {"name": "Frankie Carbo", "entity_type": "person", "description": (
        "Paolo Giovanni 'Frankie' Carbo (1904-1976). Murder Incorporated triggerman turned "
        "boxing czar. Connected to the Lucchese crime family. Suspected in the killing of "
        "Bugsy Siegel (1947). With partner Blinky Palermo, controlled professional boxing in "
        "America for decades — fixing fights, managing champions, and extorting promoters. "
        "Their control of boxing represents the Philadelphia-New York organized crime "
        "partnership in action. Convicted of conspiracy and extortion in 1961. Died in "
        "federal prison."
    ), "aliases": "Paolo Giovanni Carbo, Mr. Gray", "metadata": {"birth_date": "1904-08-10", "death_date": "1976-11-09", "nationality": "American", "status": "deceased"}},
    {"name": "Blinky Palermo", "entity_type": "person", "description": (
        "Frank 'Blinky' Palermo (1905-1996). Philadelphia mob figure and boxing racket "
        "operator. Partner of Frankie Carbo in controlling professional boxing. Managed "
        "heavyweight champion Sonny Liston and numerous other fighters. Their joint control "
        "of boxing demonstrates the Philadelphia-New York organized crime partnership. "
        "Connected to the Philadelphia crime family. Convicted alongside Carbo for conspiracy "
        "and extortion in boxing."
    ), "aliases": "Frank Palermo", "metadata": {"birth_date": "1905-03-19", "death_date": "1996-02-09", "nationality": "American", "status": "deceased"}},
    {"name": "Kenneth Shapiro", "entity_type": "person", "description": (
        "Kenneth Shapiro. Atlantic City businessman and financial advisor to Nicky Scarfo. "
        "Served as the mob's point man for casino-area land deals in Atlantic City. Facilitated "
        "property transactions with Trump's casino operations. His role demonstrates the direct "
        "financial pipeline between the Philadelphia crime family and the Atlantic City casino "
        "industry documented by the NJ State Commission of Investigation."
    ), "aliases": "", "metadata": {"nationality": "American", "status": "alive"}},
    {"name": "Salvatore Testa", "entity_type": "person", "description": (
        "Salvatore Testa (1956-1984). 'The Crown Prince of the Mob.' Son of Philip 'Chicken "
        "Man' Testa, who briefly succeeded Angelo Bruno as Philadelphia boss before being "
        "killed by a nail bomb in 1981. Salvatore was a feared enforcer under Nicky Scarfo. "
        "Sold land used for Donald Trump's Atlantic City casino development. Murdered on "
        "Scarfo's orders in 1984 at age 28 — Scarfo feared Testa's growing power and "
        "popularity."
    ), "aliases": "The Crown Prince", "metadata": {"birth_date": "1956-04-11", "death_date": "1984-09-14", "nationality": "American", "status": "deceased"}},
    {"name": "Robert LiButti", "entity_type": "person", "description": (
        "Robert LiButti. High-rolling gambler and Gambino crime family associate. FBI wiretap "
        "recordings captured LiButti referring to John Gotti as 'my boss.' Lost $12 million "
        "gambling at Trump casinos. Trump Plaza was fined $450,000 by the NJ Casino Control "
        "Commission for funneling $1.65 million in luxury cars and gifts to LiButti, and "
        "$200,000 for removing Black and female dealers from his table at his demand — "
        "a documented pattern of Trump casino management accommodating mob-connected gamblers."
    ), "aliases": "", "metadata": {"nationality": "American", "status": "deceased"}},
    {"name": "Rafi Eitan", "entity_type": "person", "description": (
        "Rafael 'Rafi' Eitan (1926-2019). Legendary Israeli intelligence operative. Led the "
        "team that captured Adolf Eichmann in Buenos Aires (1960). Ran Jonathan Pollard as a "
        "spy inside the US Navy (1984-85). Worked directly with Meyer Lansky on arms smuggling "
        "for the Haganah (pre-IDF) using waterfront access provided by Albert Anastasia's "
        "longshoremen. Connected to Robert Maxwell's PROMIS distribution network. Served as a "
        "bridge between Lansky's organized crime-intelligence nexus and Israeli intelligence "
        "operations — the same structural pipeline that later connected through Maxwell to "
        "Epstein. Served in the Israeli Knesset 2006-2009. Died March 2019."
    ), "aliases": "Rafael Eitan", "metadata": {"photo_url": "/static/photos/rafi_eitan.jpg", "birth_date": "1926-11-23", "death_date": "2019-03-23", "nationality": "Israeli", "status": "deceased"}},

    # ---- Organizations ----
    {"name": "BCCI", "entity_type": "organization", "description": "Bank of Credit and Commerce International. CIA's criminal banking arm. Secretly owned First American Bank. Shut down 1991.", "aliases": "Bank of Credit and Commerce International"},
    {"name": "First American Bank", "entity_type": "organization", "description": "Largest DC bank holding company. Secretly owned by BCCI via CIA asset front-men. Fed never told despite CIA knowledge.", "aliases": "First American Bankshares"},
    {"name": "JPMorgan Chase", "entity_type": "organization", "description": "Processed 4,725 suspicious Epstein-related wires totaling $1.1B. Settled $290M in 2023.", "aliases": "JPMorgan"},
    {"name": "Deutsche Bank", "entity_type": "organization", "description": "Maintained Epstein accounts via Butterfly Trust structure. Settled $75M with NYDFS in 2020. Provided $340M+ in loans to Trump after all other US banks refused. Fined for Russian mirror trading/money laundering scheme.", "aliases": ""},
    {"name": "Bear Stearns", "entity_type": "organization", "description": "Epstein's former employer. Served as broker to BCCI — hidden until 2011 UK Sandstorm Report.", "aliases": ""},
    {"name": "Palantir Technologies", "entity_type": "organization", "description": "Data analytics firm co-founded by Peter Thiel. Major CIA/NSA/military contractor. Successor to TIA capabilities.", "aliases": "Palantir"},
    {"name": "In-Q-Tel", "entity_type": "organization", "description": "CIA venture capital arm. Founded 1999. Funded companies that became core surveillance infrastructure.", "aliases": "IQT"},
    {"name": "Hill & Knowlton", "entity_type": "organization", "description": "PR firm led by Robert Keith Gray. Used as cover for CIA influence operations.", "aliases": "H&K"},
    {"name": "Rose Law Firm", "entity_type": "organization", "description": "Arkansas law firm (Hillary Clinton partner). Represented Systematics AND assisted BCCI's US entry.", "aliases": ""},
    {"name": "Systematics", "entity_type": "organization", "description": "Stephens-owned tech firm. Alleged primary vehicle for NSA to implant bugged PROMIS software in banks worldwide.", "aliases": "Alltel Information Services"},
    {"name": "Southern Air Transport", "entity_type": "organization", "description": "CIA front airline. Iran-Contra arms/drugs flights. Ohio taxpayer subsidies at Wexner's behest. Bankruptcy same day as CIA IG report.", "aliases": "SAT"},
    {"name": "The Limited", "entity_type": "organization", "description": "Les Wexner's retail empire. Used SAT for shipping. Victoria's Secret, Bath & Body Works.", "aliases": "L Brands"},
    {"name": "Mega Group", "entity_type": "organization", "description": "Secretive group of billionaire pro-Israel donors. Co-founded by Wexner and Charles Bronfman. Epstein attended meetings.", "aliases": ""},
    {"name": "Carbyne", "entity_type": "organization", "description": "Israeli emergency call-handling tech company. Co-founded by Ehud Barak. Epstein invested. Potential mass surveillance vector.", "aliases": "Carbyne911"},
    {"name": "Wexner Foundation", "entity_type": "foundation", "description": "Les Wexner's philanthropic vehicle. Paid Ehud Barak $2M for vague 'research.'", "aliases": ""},
    {"name": "Apollo Global Management", "entity_type": "organization", "description": "Private equity firm co-founded by Leon Black. Paid Epstein $158M in advisory fees.", "aliases": "Apollo"},
    {"name": "CAPCOM", "entity_type": "organization", "description": "BCCI commodities affiliate. Billions in anonymous trading with ties to telecom executives and intelligence figures.", "aliases": ""},
    {"name": "Glencore", "entity_type": "organization", "description": "Commodities giant founded by Marc Rich. Partially owned by Nathaniel Rothschild.", "aliases": ""},
    {"name": "George Town Club", "entity_type": "facility", "description": "Washington DC private club. Korean intelligence front per WaPo. Robert Keith Gray was president. Blackmail venue.", "aliases": ""},

    # ---- New organizations/facilities ----
    {"name": "Bayrock Group", "entity_type": "organization", "description": (
        "Bayrock Group LLC. Real estate development company headquartered in Trump Tower. "
        "Founded by Tevfik Arif, a former Soviet-era government official from Kazakhstan. "
        "Felix Sater served as managing director. Partnered with the Trump Organization on "
        "Trump SoHo and multiple other projects. Connected to Russian and Central Asian "
        "capital flows documented in litigation (Kriss v. Bayrock) and investigative "
        "reporting. Financing sources and business relationships have been the subject of "
        "congressional inquiry and multiple lawsuits alleging money laundering."
    ), "aliases": ""},
    {"name": "Resorts International", "entity_type": "organization", "description": (
        "Resorts International. Casino and resort company with documented intelligence "
        "community connections. Founded by James Crosby, who established Intertel "
        "(International Intelligence Inc.) as its security arm — staffed by former FBI, "
        "CIA, and NSA personnel. Historical connections to Meyer Lansky's gambling "
        "operations in the Bahamas. Purchased by Donald Trump in 1987, later reorganized "
        "as Trump Taj Mahal. The CIA/Intertel connection made Resorts one of the "
        "documented intersections between intelligence operations and the casino industry."
    ), "aliases": ""},
    {"name": "Mar-a-Lago", "entity_type": "facility", "description": (
        "Mar-a-Lago. Private estate and club in Palm Beach, Florida, owned by Donald "
        "Trump since 1985. Site of Trump's claimed ban of Jeffrey Epstein (timing "
        "disputed). Epstein's Palm Beach mansion was approximately one mile away. "
        "According to court documents and witness testimony, Mar-a-Lago was part of the "
        "Palm Beach social circuit where Trump and Epstein interacted in the late 1990s "
        "and early 2000s."
    ), "aliases": "", "metadata": {"photo_url": "/static/photos/mar_a_lago.jpg"}},
    {"name": "Little Saint James", "entity_type": "facility", "description": (
        "Little Saint James. Private island in the US Virgin Islands owned by Jeffrey "
        "Epstein from 1998 until his death. Also known as 'Pedophile Island' or 'Epstein "
        "Island.' Site of a mysterious temple-like structure, staff quarters, and "
        "underground facilities documented in aerial photographs and drone footage. "
        "Flight logs and witness testimony document visits by numerous prominent figures. "
        "FBI raided the island in August 2019 following Epstein's arrest. The island and "
        "neighboring Great Saint James were listed for sale by Epstein's estate."
    ), "aliases": "Epstein Island, Pedophile Island", "metadata": {"photo_url": "/static/photos/little_saint_james.jpg"}},

    # ---- Crime organizations ----
    {"name": "The Commission", "entity_type": "organization", "description": (
        "The Commission. Governing body of the American Mafia, established by Lucky Luciano "
        "in 1931 to prevent inter-family warfare. Comprised bosses of the Five Families "
        "(Gambino, Genovese, Lucchese, Bonanno, Colombo) plus the Chicago Outfit and Buffalo "
        "family. The Commission approved major operations, settled disputes, and authorized "
        "assassinations. Broken by the 1986 Commission Trial (US v. Salerno et al.), which "
        "convicted the bosses of the Genovese, Lucchese, and Colombo families."
    ), "aliases": "Mafia Commission"},
    {"name": "Gambino Crime Family", "entity_type": "organization", "description": (
        "One of the Five Families of New York. Led by Paul Castellano (until 1985 assassination), "
        "then John Gotti (1985-1992). Co-controlled S&A Concrete with the Genovese family, "
        "providing concrete for major Manhattan construction including Trump Tower. Roy Cohn "
        "represented both Castellano and Gotti. Extended influence into Philadelphia through "
        "John Stanfa."
    ), "aliases": "Gambino Family"},
    {"name": "Genovese Crime Family", "entity_type": "organization", "description": (
        "One of the Five Families of New York. Led by Fat Tony Salerno (front boss, convicted "
        "1986). Co-controlled S&A Concrete with the Gambino family. The most powerful family "
        "in the Mafia — managed to keep its true leadership structure hidden for decades. "
        "Roy Cohn represented boss Salerno."
    ), "aliases": "Genovese Family"},
    {"name": "Lucchese Crime Family", "entity_type": "organization", "description": (
        "One of the Five Families of New York. Connected to Frankie Carbo (Murder Inc triggerman "
        "turned boxing czar). Extended operations across construction, garment industry, and "
        "labor unions in New York. The 'Carbone' name associated with Lucchese operations."
    ), "aliases": "Lucchese Family"},
    {"name": "Philadelphia Crime Family", "entity_type": "organization", "description": (
        "Also known as the Bruno-Scarfo family. Controlled organized crime in the greater "
        "Philadelphia area and South Jersey. Successive bosses: Angelo Bruno (1959-1980), "
        "Phil Testa (1980-1981), Nicky Scarfo (1981-1991), John Stanfa (1991-1994), "
        "Ralph Natale (1994-1999), Joey Merlino (1999-present). The bloodiest succession in "
        "Mafia history — Bruno's assassination triggered a war claiming 20+ lives. Critical "
        "to Atlantic City casino development and Trump's entry into the casino business."
    ), "aliases": "Bruno-Scarfo Family, Philly Mob"},
    {"name": "Murder Incorporated", "entity_type": "organization", "description": (
        "Enforcement arm of the National Crime Syndicate, established by Lucky Luciano and "
        "Meyer Lansky in the early 1930s. Operated as a professional assassination service "
        "for the Commission. Based in Brooklyn under Albert Anastasia and Louis Buchalter. "
        "Responsible for an estimated 400-1,000 contract killings. Members included Frankie "
        "Carbo and Bugsy Siegel. Disbanded after informant Abe Reles's suspicious death (fell "
        "from a guarded hotel window in 1941)."
    ), "aliases": "Murder Inc, The Combination"},
    {"name": "Scarf Inc", "entity_type": "organization", "description": (
        "Nicky Scarfo's construction company in Atlantic City. Controlled concrete and "
        "construction work for casino development during the 1980s Atlantic City boom. "
        "The NJ State Commission of Investigation documented organized crime influence over "
        "casino construction sub-contractors, with Scarfo's operations controlling the "
        "foundations that casinos — including Trump's — were built upon."
    ), "aliases": "Scarfo Construction"},
    {"name": "S&A Concrete", "entity_type": "organization", "description": (
        "S&A Concrete. Joint Genovese-Gambino crime family concrete company controlled by "
        "Fat Tony Salerno and Paul Castellano. Held a monopoly on concrete deliveries for "
        "any Manhattan construction project over $2 million during the 1980s — the 'Concrete "
        "Club.' Provided concrete for Trump Tower, Trump Plaza, and other major developments. "
        "Roy Cohn represented both family bosses. The concrete racket was a documented "
        "intersection of organized crime and the New York real estate industry."
    ), "aliases": "Concrete Club"},

    # ---- Agencies ----
    {"name": "CIA", "entity_type": "agency", "description": "Central Intelligence Agency. Created by National Security Act 1947. MKULTRA, BCCI banking, Iran-Contra, sexual blackmail operations documented.", "aliases": "Central Intelligence Agency"},
    {"name": "NSA", "entity_type": "agency", "description": "National Security Agency. PROMIS/Systematics connection. Watch list included Church Committee members.", "aliases": "National Security Agency"},
    {"name": "FBI", "entity_type": "agency", "description": "Federal Bureau of Investigation. COINTELPRO. Hoover compromised by Lansky. CHS memo on Epstein.", "aliases": "Federal Bureau of Investigation"},
    {"name": "Mossad", "entity_type": "agency", "description": "Israeli intelligence service. Robert Maxwell asset. Epstein identified as co-opted agent. PROMIS distribution.", "aliases": "Institute for Intelligence and Special Operations"},
    {"name": "DOJ", "entity_type": "agency", "description": "Department of Justice. Stole PROMIS from INSLAW. Epstein NPA. BCCI non-notification from CIA.", "aliases": "Department of Justice"},
    {"name": "DARPA", "entity_type": "agency", "description": "Defense Advanced Research Projects Agency. Ran Total Information Awareness program. LifeLog program.", "aliases": "Defense Advanced Research Projects Agency"},

    # ---- Programs ----
    {"name": "PROMIS", "entity_type": "program", "description": "Prosecutor's Management Information System. Stolen from INSLAW by DOJ. Backdoored by Israeli intelligence. Sold worldwide via Robert Maxwell.", "aliases": "Prosecutor's Management Information System"},
    {"name": "Main Core", "entity_type": "program", "description": "Domestic surveillance database. Alleged successor to PROMIS for tracking Americans. Continuity of government program.", "aliases": ""},
    {"name": "Total Information Awareness", "entity_type": "program", "description": "DARPA mass surveillance program directed by John Poindexter (2002). Congress defunded 2003. Capabilities migrated to NSA.", "aliases": "TIA"},
    {"name": "MKULTRA", "entity_type": "program", "description": "CIA mind control program. Operation Midnight Climax used sexual blackmail. DCI Helms ordered files destroyed 1973.", "aliases": "MK-ULTRA"},
    {"name": "COINTELPRO", "entity_type": "program", "description": "FBI domestic counterintelligence program. 2,370 approved actions (1956-71). Sexual disruption as explicit technique.", "aliases": "Counter Intelligence Program"},
    {"name": "Iran-Contra", "entity_type": "program", "description": "Covert arms-for-hostages and drug trafficking operation. Casey architect. BCCI banking. Mena Airport. SAT flights.", "aliases": ""},
    {"name": "Operation Midnight Climax", "entity_type": "program", "description": "CIA operation: safe houses where targets given LSD, filmed during sexual acts through two-way mirrors. TSD operated.", "aliases": ""},
    {"name": "LifeLog", "entity_type": "program", "description": "DARPA program to build a database of a person's entire existence. Cancelled Feb 4, 2004 — same day Facebook launched.", "aliases": ""},

    # ---- Events ----
    {"name": "BCCI Shutdown (1991)", "entity_type": "event", "description": "Bank of England shut down BCCI July 5, 1991. Largest bank fraud in history at the time.", "aliases": ""},
    {"name": "Epstein NPA (2007)", "entity_type": "event", "description": "Non-Prosecution Agreement. Acosta reportedly told Epstein 'belonged to intelligence.' Victims not notified.", "aliases": ""},
    {"name": "Epstein Arrest (2019)", "entity_type": "event", "description": "SDNY arrested Epstein July 6, 2019 on sex trafficking charges.", "aliases": ""},
    {"name": "Epstein Death (2019)", "entity_type": "event", "description": "Epstein found dead in MCC cell Aug 10, 2019. Ruled suicide. Cameras malfunctioned. Guards sleeping.", "aliases": ""},
    {"name": "Danny Casolaro Death (1991)", "entity_type": "event", "description": "Journalist found dead in Martinsburg WV hotel, Aug 10, 1991. Ruled suicide. Arms slashed 10+ times. Notes missing.", "aliases": ""},
    {"name": "Robert Maxwell Death (1991)", "entity_type": "event", "description": "Found dead off his yacht Nov 5, 1991. Israeli state funeral. BCCI connection. PROMIS distribution halted.", "aliases": ""},
    {"name": "Wexner House Oversight Deposition (2026)", "entity_type": "event", "description": (
        "House Oversight Committee deposition of Les Wexner regarding the Jeffrey Epstein "
        "network, conducted February 18, 2026. Attorney Michael Levy caught on hot "
        "microphone threatening Wexner for answering committee questions. Wexner identified "
        "as co-conspirator on 2019 FBI document. Part of the House Oversight Committee's "
        "broader investigation into the Epstein network and intelligence connections."
    ), "aliases": ""},

    # ---- Organized crime events ----
    {"name": "Commission Trial (1986)", "entity_type": "event", "description": (
        "US v. Salerno et al. The Mafia Commission Trial (1985-1986). Federal RICO prosecution "
        "of the bosses of three of the Five Families: Fat Tony Salerno (Genovese), Tony Ducks "
        "Corallo (Lucchese), and Carmine Persico (Colombo). All convicted. Salerno received "
        "100 years. The trial broke the Commission's power as a governing body and demonstrated "
        "that RICO could dismantle organized crime leadership."
    ), "aliases": "US v. Salerno"},
    {"name": "Castellano Assassination (1985)", "entity_type": "event", "description": (
        "Assassination of Gambino boss Paul Castellano. On December 16, 1985, Castellano and "
        "underboss Thomas Bilotti were shot by gunmen in trench coats outside Sparks Steak "
        "House in midtown Manhattan. John Gotti orchestrated the hit and watched from a car "
        "across the street. Gotti became boss without Commission approval — violating the "
        "Mafia's fundamental governance structure. The most brazen mob hit in modern history."
    ), "aliases": "Sparks Steak House Hit"},
]


# ============================================================
# RELATIONSHIPS — every one has evidence tier + source IDs
# ============================================================

RELATIONSHIPS = [
    # ---- PROMIS → Main Core → TIA → Palantir pipeline ----
    {"source": "Bill Hamilton", "target": "PROMIS", "type": "founder_of", "tier": "documented", "desc": "Created PROMIS at INSLAW", "sources": [21]},
    {"source": "DOJ", "target": "PROMIS", "type": "asset_of", "tier": "documented", "desc": "DOJ stole PROMIS from INSLAW through rigged bankruptcy proceedings", "sources": [21, 7]},
    {"source": "Robert Maxwell", "target": "PROMIS", "type": "asset_of", "tier": "credible", "desc": "Distributed backdoored PROMIS to governments worldwide on behalf of Israeli intelligence", "sources": [11, 21]},
    {"source": "Mossad", "target": "PROMIS", "type": "asset_of", "tier": "credible", "desc": "Backdoored PROMIS software with surveillance capabilities before distribution", "sources": [21, 25]},
    {"source": "Systematics", "target": "PROMIS", "type": "asset_of", "tier": "credible", "desc": "Primary vehicle for NSA to implant bugged PROMIS in world's major banks", "sources": [25]},
    {"source": "NSA", "target": "Systematics", "type": "affiliated_with", "tier": "credible", "desc": "NSA used Systematics to implant surveillance software in banks per 1995 Inslaw document", "sources": [25]},
    {"source": "Jackson Stephens", "target": "Systematics", "type": "director_of", "tier": "documented", "desc": "Stephens Inc owned Systematics", "sources": [17]},
    {"source": "Rose Law Firm", "target": "Systematics", "type": "affiliated_with", "tier": "documented", "desc": "Represented Systematics as legal counsel", "sources": [11]},
    {"source": "PROMIS", "target": "Main Core", "type": "evolved_into", "tier": "credible", "desc": "PROMIS capabilities evolved into domestic surveillance database", "sources": [11]},
    {"source": "Main Core", "target": "Total Information Awareness", "type": "evolved_into", "tier": "inference", "desc": "Domestic tracking concept formalized into DARPA program", "sources": [11, 24]},
    {"source": "John Poindexter", "target": "Total Information Awareness", "type": "director_of", "tier": "documented", "desc": "Directed TIA program at DARPA (2002-2003)", "sources": [24]},
    {"source": "DARPA", "target": "Total Information Awareness", "type": "affiliated_with", "tier": "documented", "desc": "DARPA ran TIA before Congress defunded it", "sources": [24]},
    {"source": "Total Information Awareness", "target": "Palantir Technologies", "type": "evolved_into", "tier": "credible", "desc": "TIA capabilities migrated to private sector via Palantir after Congress defunded", "sources": [11, 23]},
    {"source": "Peter Thiel", "target": "Palantir Technologies", "type": "founder_of", "tier": "documented", "desc": "Co-founded Palantir in 2003", "sources": [23]},
    {"source": "Alex Karp", "target": "Palantir Technologies", "type": "director_of", "tier": "documented", "desc": "CEO of Palantir Technologies", "sources": [23]},
    {"source": "In-Q-Tel", "target": "Palantir Technologies", "type": "invested_in", "tier": "documented", "desc": "CIA venture arm invested in Palantir's early rounds", "sources": [22, 23]},
    {"source": "CIA", "target": "In-Q-Tel", "type": "founder_of", "tier": "documented", "desc": "CIA created In-Q-Tel as its venture capital arm in 1999", "sources": [22]},
    {"source": "DARPA", "target": "LifeLog", "type": "affiliated_with", "tier": "documented", "desc": "DARPA ran LifeLog program — cancelled same day Facebook launched", "sources": [24]},

    # ---- BCCI nexus ----
    {"source": "Agha Hasan Abedi", "target": "BCCI", "type": "founder_of", "tier": "documented", "desc": "Founded BCCI in 1972", "sources": [1]},
    {"source": "Kamal Adham", "target": "BCCI", "type": "front_for", "tier": "documented", "desc": "CIA's principal Middle East liaison was secret lead front-man for BCCI's takeover of First American", "sources": [1]},
    {"source": "Kamal Adham", "target": "CIA", "type": "asset_of", "tier": "documented", "desc": "CIA's principal Middle East liaison mid-1960s through 1979", "sources": [1]},
    {"source": "BCCI", "target": "First American Bank", "type": "front_for", "tier": "documented", "desc": "Secretly owned First American through CIA asset front-men", "sources": [1]},
    {"source": "Clark Clifford", "target": "First American Bank", "type": "front_for", "tier": "documented", "desc": "Served as front-man for BCCI's acquisition of First American. Indicted 1992.", "sources": [1]},
    {"source": "Rose Law Firm", "target": "BCCI", "type": "affiliated_with", "tier": "documented", "desc": "Assisted BCCI's acquisition of First American Bank", "sources": [11, 1]},
    {"source": "William Casey", "target": "Agha Hasan Abedi", "type": "connected_to", "tier": "credible", "desc": "Alleged secret meetings at Madison Hotel for 3 years per NBC and credible BCCI official", "sources": [1]},
    {"source": "Richard Helms", "target": "BCCI", "type": "covered_for", "tier": "documented", "desc": "Drafted legal language protecting BCCI front-man Irvani despite later denials — his own telex proves it", "sources": [1]},
    {"source": "CAPCOM", "target": "BCCI", "type": "affiliated_with", "tier": "documented", "desc": "BCCI commodities affiliate handling billions in anonymous trading", "sources": [1]},
    {"source": "Bear Stearns", "target": "BCCI", "type": "affiliated_with", "tier": "documented", "desc": "Served as broker to BCCI — hidden until 2011 UK Sandstorm Report", "sources": [16]},
    {"source": "BCCI Shutdown (1991)", "target": "BCCI", "type": "connected_to", "tier": "documented", "desc": "Bank of England shut down BCCI July 5, 1991", "sources": [1]},

    # ---- Iran-Contra ----
    {"source": "William Casey", "target": "Iran-Contra", "type": "director_of", "tier": "documented", "desc": "Architect of Iran-Contra covert operations as CIA Director", "sources": [8, 13]},
    {"source": "Southern Air Transport", "target": "Iran-Contra", "type": "participated_in", "tier": "documented", "desc": "CIA front airline used for arms/drugs flights", "sources": [14, 8]},
    {"source": "Barry Seal", "target": "Southern Air Transport", "type": "affiliated_with", "tier": "documented", "desc": "CIA drug pilot using SAT aircraft out of Mena Airport", "sources": [13]},
    {"source": "Adnan Khashoggi", "target": "Iran-Contra", "type": "participated_in", "tier": "documented", "desc": "Iran-Contra middleman, banked at BCCI Monte Carlo", "sources": [1]},
    {"source": "Adnan Khashoggi", "target": "BCCI", "type": "affiliated_with", "tier": "documented", "desc": "Banked at BCCI Monte Carlo; told manager he was 'working for US government and CIA'", "sources": [1]},
    {"source": "Les Wexner", "target": "Southern Air Transport", "type": "affiliated_with", "tier": "documented", "desc": "Ohio created taxpayer incentives for SAT at Wexner's behest for The Limited shipping", "sources": [14]},
    {"source": "Southern Air Transport", "target": "The Limited", "type": "affiliated_with", "tier": "documented", "desc": "CIA front airline provided shipping for Wexner's retail empire", "sources": [14]},

    # ---- Epstein network ----
    {"source": "Jeffrey Epstein", "target": "Mossad", "type": "asset_of", "tier": "credible", "desc": "FBI CHS memo (Oct 2020) identifies Epstein as 'co-opted Mossad agent' trained under Barak", "sources": [9]},
    {"source": "Ghislaine Maxwell", "target": "Jeffrey Epstein", "type": "affiliated_with", "tier": "documented", "desc": "Primary accomplice in sex trafficking operation. Convicted 2021.", "sources": [4]},
    {"source": "Robert Maxwell", "target": "Ghislaine Maxwell", "type": "connected_to", "tier": "documented", "desc": "Father-daughter. Robert was documented Mossad asset.", "sources": [11]},
    {"source": "Robert Maxwell", "target": "Mossad", "type": "asset_of", "tier": "credible", "desc": "Mossad asset who distributed backdoored PROMIS software worldwide", "sources": [11, 21]},
    {"source": "Les Wexner", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Granted Epstein power of attorney, $46M mansion, financial management role", "sources": [4, 11]},
    {"source": "Ehud Barak", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Visited Epstein's residences. Photographed entering Epstein's NYC building.", "sources": [11]},
    {"source": "Wexner Foundation", "target": "Ehud Barak", "type": "funded", "tier": "documented", "desc": "Paid Barak $2M for vague 'research' — Mega Group money flowing to Israeli military intelligence", "sources": [11]},
    {"source": "Les Wexner", "target": "Wexner Foundation", "type": "founder_of", "tier": "documented", "desc": "Created as philanthropic vehicle", "sources": [11]},
    {"source": "Les Wexner", "target": "Mega Group", "type": "founder_of", "tier": "documented", "desc": "Co-founded with Charles Bronfman", "sources": [11]},
    {"source": "Jeffrey Epstein", "target": "Mega Group", "type": "participated_in", "tier": "credible", "desc": "Attended Mega Group meetings", "sources": [11]},
    {"source": "Ehud Barak", "target": "Carbyne", "type": "founder_of", "tier": "documented", "desc": "Co-founded Carbyne emergency call-handling technology company", "sources": [11]},
    {"source": "Jeffrey Epstein", "target": "Carbyne", "type": "invested_in", "tier": "documented", "desc": "Invested in Carbyne — potential mass surveillance vector", "sources": [11]},
    {"source": "Jeffrey Epstein", "target": "Bear Stearns", "type": "employed_by", "tier": "documented", "desc": "Worked at Bear Stearns in 1970s-80s", "sources": [11]},
    {"source": "JPMorgan Chase", "target": "Jeffrey Epstein", "type": "affiliated_with", "tier": "documented", "desc": "Processed 4,725 suspicious wires totaling $1.1B. SARs filed years late.", "sources": [4]},
    {"source": "Deutsche Bank", "target": "Jeffrey Epstein", "type": "affiliated_with", "tier": "documented", "desc": "Maintained accounts via Butterfly Trust structure after JPMorgan dropped him", "sources": [5]},
    {"source": "Leon Black", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Paid Epstein $158M in advisory fees through Apollo Global", "sources": [4]},
    {"source": "Leon Black", "target": "Apollo Global Management", "type": "founder_of", "tier": "documented", "desc": "Co-founded Apollo Global Management", "sources": [23]},
    {"source": "Epstein NPA (2007)", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Non-Prosecution Agreement — Acosta told Epstein 'belonged to intelligence'", "sources": [6]},
    {"source": "Epstein Arrest (2019)", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "SDNY arrested Epstein July 6, 2019", "sources": [4]},
    {"source": "Epstein Death (2019)", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Found dead in MCC cell. Cameras malfunctioned. Guards sleeping.", "sources": [11]},
    {"source": "William Barr", "target": "Epstein Death (2019)", "type": "covered_for", "tier": "inference", "desc": "As AG, oversaw investigation into Epstein's death. Declared suicide despite evidence anomalies.", "sources": [11]},
    {"source": "Donald Barr", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Hired Epstein to teach at Dalton School 1974 despite no degree", "sources": [11]},

    # ---- Sexual blackmail lineage ----
    {"source": "Meyer Lansky", "target": "J. Edgar Hoover", "type": "handler_of", "tier": "credible", "desc": "Obtained compromising photos of Hoover. FBI refused to investigate organized crime for decades.", "sources": [11, 2]},
    {"source": "James Angleton", "target": "J. Edgar Hoover", "type": "connected_to", "tier": "credible", "desc": "Held copies of Hoover compromise material. Managed CIA-Mossad relationship.", "sources": [11]},
    {"source": "CIA", "target": "Operation Midnight Climax", "type": "affiliated_with", "tier": "documented", "desc": "CIA-funded safe houses where targets drugged with LSD and filmed during sexual acts", "sources": [2, 3]},
    {"source": "Operation Midnight Climax", "target": "MKULTRA", "type": "affiliated_with", "tier": "documented", "desc": "Sub-project of MKULTRA mind control program", "sources": [2, 3]},
    {"source": "Richard Helms", "target": "MKULTRA", "type": "covered_for", "tier": "documented", "desc": "As DCI, ordered MKULTRA files destroyed in 1973", "sources": [2, 3]},
    {"source": "Edwin Wilson", "target": "CIA", "type": "employed_by", "tier": "documented", "desc": "CIA/Naval Intelligence officer running congressional blackmail", "sources": [11]},
    {"source": "Frank Terpil", "target": "Edwin Wilson", "type": "affiliated_with", "tier": "documented", "desc": "CIA partner who described Wilson's blackmail operation in detail", "sources": [11]},
    {"source": "Robert Keith Gray", "target": "George Town Club", "type": "director_of", "tier": "documented", "desc": "President of the George Town Club — Korean intelligence front per WaPo", "sources": [20]},
    {"source": "Robert Keith Gray", "target": "Hill & Knowlton", "type": "director_of", "tier": "documented", "desc": "CEO of Hill & Knowlton", "sources": [20]},
    {"source": "Robert Keith Gray", "target": "CIA", "type": "asset_of", "tier": "credible", "desc": "CIA blackmail specialist per DeCamp. Reagan deputy comms under Casey.", "sources": [11, 20]},
    {"source": "Craig Spence", "target": "CIA", "type": "asset_of", "tier": "credible", "desc": "Ran bugged DC apartments. Boasted of CIA work. Predicted agency would kill him.", "sources": [12]},
    {"source": "Roy Cohn", "target": "William Casey", "type": "connected_to", "tier": "credible", "desc": "Daily phone calls between Cohn and CIA Director Casey", "sources": [11]},
    {"source": "FBI", "target": "COINTELPRO", "type": "affiliated_with", "tier": "documented", "desc": "FBI domestic counterintelligence: 2,370 approved actions. Sexual disruption explicit technique.", "sources": [2]},
    {"source": "Roy Cohn", "target": "J. Edgar Hoover", "type": "affiliated_with", "tier": "credible", "desc": "Coordinated sexual blackmail operations with Hoover. Both used compromising material as control mechanism.", "sources": [11]},

    # ---- Stephens/Arkansas/Clinton ----
    {"source": "Jackson Stephens", "target": "Bill Clinton", "type": "funded", "tier": "documented", "desc": "Bankrolled Clinton's rise. Worthen Bank provided $3.5M campaign credit.", "sources": [17]},
    {"source": "Hillary Clinton", "target": "Rose Law Firm", "type": "employed_by", "tier": "documented", "desc": "Partner at Rose Law Firm", "sources": [11]},
    {"source": "Bill Clinton", "target": "Marc Rich", "type": "connected_to", "tier": "documented", "desc": "Pardoned Marc Rich on last day in office", "sources": [15]},
    {"source": "Marc Rich", "target": "Mossad", "type": "asset_of", "tier": "credible", "desc": "Main source of Israel's oil for 20 years. Offices served Mossad agents per Haaretz.", "sources": [15]},
    {"source": "Marc Rich", "target": "Glencore", "type": "founder_of", "tier": "documented", "desc": "Founded the commodities giant", "sources": [15]},
    {"source": "Barry Seal", "target": "CIA", "type": "asset_of", "tier": "documented", "desc": "CIA drug pilot operating from Mena Airport", "sources": [13, 8]},
    {"source": "William Barr", "target": "William Casey", "type": "affiliated_with", "tier": "credible", "desc": "Barr served as Casey's emissary to Clinton regarding money laundering per Reed", "sources": [11]},
    {"source": "Bill Clinton", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Epstein flight logs document 26+ flights on Epstein's aircraft. Visited Epstein's island.", "sources": [30]},

    # ---- Danny Casolaro / INSLAW ----
    {"source": "Danny Casolaro", "target": "PROMIS", "type": "investigated", "tier": "documented", "desc": "Was investigating INSLAW/PROMIS theft and the network he called 'The Octopus'", "sources": [21]},
    {"source": "Danny Casolaro Death (1991)", "target": "Danny Casolaro", "type": "connected_to", "tier": "documented", "desc": "Found dead Aug 10, 1991. Notes missing. Ruled suicide.", "sources": [21]},
    {"source": "Robert Maxwell Death (1991)", "target": "Robert Maxwell", "type": "connected_to", "tier": "documented", "desc": "Found dead off yacht Nov 5, 1991. Israeli state funeral.", "sources": [11]},
    {"source": "BCCI Shutdown (1991)", "target": "Danny Casolaro Death (1991)", "type": "connected_to", "tier": "inference", "desc": "BCCI shutdown (Jul), Casolaro death (Aug), Maxwell death (Nov) — three Octopus-connected events in 5 months", "sources": [11]},

    # ---- Donald Trump network ----
    {"source": "Roy Cohn", "target": "Donald Trump", "type": "mentor_of", "tier": "documented", "desc": "Mentor and fixer 1973-1986. Connected Trump to organized crime, intelligence, and political power. Federal housing discrimination defense through death.", "sources": [11, 37, 38]},
    {"source": "Donald Trump", "target": "Jeffrey Epstein", "type": "associated_with", "tier": "documented", "desc": "Social relationship ~1987-2004. Trump quote (2002): 'terrific guy...likes beautiful women on the younger side.' Photos, party footage, flight logs.", "sources": [26, 30]},
    {"source": "Donald Trump", "target": "William Barr", "type": "appointed", "tier": "documented", "desc": "Appointed Barr as AG in 2019. Barr's father hired Epstein at Dalton. Barr was AG when Epstein died in custody.", "sources": [11]},
    {"source": "Donald Trump", "target": "Alexander Acosta", "type": "appointed", "tier": "documented", "desc": "Appointed Acosta (who gave Epstein the NPA) as Secretary of Labor 2017. Acosta told transition team Epstein 'belonged to intelligence.'", "sources": [28]},
    {"source": "Deutsche Bank", "target": "Donald Trump", "type": "funded", "tier": "documented", "desc": "Provided $340M+ in loans after all other US banks refused. DB later fined for Russian mirror trades and Epstein accounts.", "sources": [5, 11]},
    {"source": "Donald Trump", "target": "Resorts International", "type": "acquired", "tier": "documented", "desc": "Purchased Resorts International in 1987. Casino company with CIA/Intertel intelligence connections and Lansky history.", "sources": [37, 38]},
    {"source": "Donald Trump", "target": "Ghislaine Maxwell", "type": "associated_with", "tier": "credible", "desc": "Photographed together at social events. Maxwell attended Trump events. Social overlap through Epstein.", "sources": [26, 30]},
    {"source": "Donald Trump", "target": "Mar-a-Lago", "type": "affiliated_with", "tier": "documented", "desc": "Owned since 1985. Palm Beach estate approximately one mile from Epstein's residence.", "sources": [37]},
    {"source": "Donald Trump", "target": "Fat Tony Salerno", "type": "connected_to", "tier": "documented", "desc": "Connected via Roy Cohn. Salerno's S&A Concrete provided concrete for Trump Tower construction.", "sources": [27, 37]},
    {"source": "Donald Trump", "target": "Paul Castellano", "type": "connected_to", "tier": "documented", "desc": "Connected via Roy Cohn. Castellano's S&A Concrete (joint Gambino-Genovese venture) built Trump Tower.", "sources": [27, 37]},
    {"source": "Felix Sater", "target": "Donald Trump", "type": "affiliated_with", "tier": "documented", "desc": "Bayrock Group partner. Sater's business card read 'Senior Advisor to Donald Trump.' Office in Trump Tower.", "sources": [40]},
    {"source": "Resorts International", "target": "CIA", "type": "affiliated_with", "tier": "credible", "desc": "Intertel security arm staffed by former FBI/CIA/NSA personnel. Historical Lansky connections.", "sources": [37, 11]},

    # ---- Acosta / Dershowitz / NPA connections ----
    {"source": "Alexander Acosta", "target": "Epstein NPA (2007)", "type": "connected_to", "tier": "documented", "desc": "As US Attorney, negotiated the NPA. Later said he was told Epstein 'belonged to intelligence.'", "sources": [6, 28]},
    {"source": "Alexander Acosta", "target": "DOJ", "type": "employed_by", "tier": "documented", "desc": "US Attorney, Southern District of Florida (2005-2009)", "sources": [28]},
    {"source": "Alan Dershowitz", "target": "Jeffrey Epstein", "type": "legal_counsel", "tier": "documented", "desc": "Defense attorney for Epstein during NPA negotiations. Named by Giuffre as participant. Flight logs.", "sources": [6, 29, 30]},
    {"source": "Alan Dershowitz", "target": "Epstein NPA (2007)", "type": "connected_to", "tier": "documented", "desc": "Epstein's defense counsel who negotiated the unprecedented NPA.", "sources": [6]},
    {"source": "Alan Dershowitz", "target": "Donald Trump", "type": "affiliated_with", "tier": "documented", "desc": "Served on Trump's first impeachment defense team (2020). Connected through Epstein legal circles.", "sources": [11]},

    # ---- Sater / Bayrock ----
    {"source": "Felix Sater", "target": "Bayrock Group", "type": "director_of", "tier": "documented", "desc": "Managing director of Bayrock Group, headquartered in Trump Tower.", "sources": [40]},
    {"source": "Bayrock Group", "target": "Donald Trump", "type": "affiliated_with", "tier": "documented", "desc": "Partnered with Trump Organization on Trump SoHo and other projects. Russian/Central Asian capital flows.", "sources": [40]},

    # ---- Other new connections ----
    {"source": "Roy Cohn", "target": "Fat Tony Salerno", "type": "legal_counsel", "tier": "documented", "desc": "Attorney for Salerno. Connected Genovese family boss to political establishment.", "sources": [11, 27]},
    {"source": "Roy Cohn", "target": "Paul Castellano", "type": "legal_counsel", "tier": "documented", "desc": "Attorney for Castellano. Represented both major NYC mob bosses simultaneously.", "sources": [11, 27]},
    {"source": "Les Wexner", "target": "The Limited", "type": "founder_of", "tier": "documented", "desc": "Founded The Limited (L Brands) retail empire — Victoria's Secret, Bath & Body Works, Abercrombie & Fitch.", "sources": [11]},
    {"source": "Wexner House Oversight Deposition (2026)", "target": "Les Wexner", "type": "connected_to", "tier": "documented", "desc": "Feb 18, 2026 deposition. Attorney Levy caught on hot mic threatening Wexner for answering questions.", "sources": [33]},
    {"source": "FBI", "target": "Les Wexner", "type": "investigated", "tier": "documented", "desc": "Named as co-conspirator on 2019 FBI document related to Epstein investigation.", "sources": [9]},
    {"source": "Jeffrey Epstein", "target": "Mar-a-Lago", "type": "connected_to", "tier": "documented", "desc": "Attended events at Mar-a-Lago. Epstein's Palm Beach residence ~1 mile away. Trump claims ban (timing disputed).", "sources": [26, 30]},
    {"source": "Jeffrey Epstein", "target": "Little Saint James", "type": "affiliated_with", "tier": "documented", "desc": "Owned from 1998 until death. Site of trafficking operations. FBI raided Aug 2019. Temple structure, underground facilities.", "sources": [11, 31]},
    {"source": "Bill Clinton", "target": "Little Saint James", "type": "connected_to", "tier": "documented", "desc": "Flight logs and witness testimony document visits to Epstein's island.", "sources": [30]},

    # ---- Organized crime structure ----
    {"source": "Lucky Luciano", "target": "The Commission", "type": "founder_of", "tier": "documented", "desc": "Established The Commission in 1931 to govern the Five Families and prevent inter-family warfare.", "sources": [55]},
    {"source": "Lucky Luciano", "target": "Meyer Lansky", "type": "affiliated_with", "tier": "documented", "desc": "Lifelong partners. Created the National Crime Syndicate together — organized crime as a national corporation.", "sources": [55, 50]},
    {"source": "Lucky Luciano", "target": "Murder Incorporated", "type": "founder_of", "tier": "documented", "desc": "Established Murder Inc as the Commission's enforcement arm with Lansky.", "sources": [55]},
    {"source": "Bugsy Siegel", "target": "Meyer Lansky", "type": "affiliated_with", "tier": "documented", "desc": "Childhood friends on the Lower East Side. Lifelong criminal partnership. Lansky sent Siegel to build Vegas.", "sources": [55]},
    {"source": "Bugsy Siegel", "target": "Murder Incorporated", "type": "affiliated_with", "tier": "documented", "desc": "Murder Inc member and triggerman before being sent west to build Las Vegas.", "sources": [55]},
    {"source": "Frankie Carbo", "target": "Murder Incorporated", "type": "affiliated_with", "tier": "documented", "desc": "Murder Inc triggerman. Suspected in the killing of Bugsy Siegel (1947).", "sources": [55]},
    {"source": "Frankie Carbo", "target": "Bugsy Siegel", "type": "connected_to", "tier": "credible", "desc": "Suspected triggerman in Siegel's assassination (June 20, 1947, Beverly Hills).", "sources": [55]},
    {"source": "Frankie Carbo", "target": "Lucchese Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Connected to the Lucchese family. Boxing racket operations.", "sources": [55]},
    {"source": "Frankie Carbo", "target": "Blinky Palermo", "type": "affiliated_with", "tier": "documented", "desc": "Partners in controlling professional boxing — fixing fights, managing champions, extorting promoters.", "sources": [55]},
    {"source": "Blinky Palermo", "target": "Philadelphia Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Philadelphia mob figure. Boxing racket operator demonstrating Philly-NYC partnership.", "sources": [55]},
    {"source": "Meyer Lansky", "target": "The Commission", "type": "affiliated_with", "tier": "documented", "desc": "Financial brain of the National Crime Syndicate. Served the Commission but never a formal member (Jewish, not Sicilian).", "sources": [55, 50]},
    {"source": "Meyer Lansky", "target": "Murder Incorporated", "type": "affiliated_with", "tier": "documented", "desc": "Co-created Murder Inc as the enforcement arm of the National Crime Syndicate.", "sources": [55]},
    {"source": "Meyer Lansky", "target": "Resorts International", "type": "connected_to", "tier": "credible", "desc": "Historical connections between Lansky's gambling operations and Resorts International's Bahamas origins.", "sources": [11, 37]},

    # ---- Five Families structure ----
    {"source": "The Commission", "target": "Gambino Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Gambino family held a permanent Commission seat.", "sources": [41]},
    {"source": "The Commission", "target": "Genovese Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Genovese family held a permanent Commission seat.", "sources": [41]},
    {"source": "The Commission", "target": "Lucchese Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Lucchese family held a permanent Commission seat.", "sources": [41]},
    {"source": "Fat Tony Salerno", "target": "Genovese Crime Family", "type": "boss_of", "tier": "documented", "desc": "Front boss of the Genovese family. Convicted in 1986 Commission Trial.", "sources": [41, 52]},
    {"source": "Paul Castellano", "target": "Gambino Crime Family", "type": "boss_of", "tier": "documented", "desc": "Boss of the Gambino family until assassination in 1985.", "sources": [41]},
    {"source": "John Gotti", "target": "Gambino Crime Family", "type": "boss_of", "tier": "documented", "desc": "Boss from 1985 (Castellano assassination) until conviction in 1992.", "sources": [41, 55]},

    # ---- S&A Concrete / Construction racket ----
    {"source": "Fat Tony Salerno", "target": "S&A Concrete", "type": "director_of", "tier": "documented", "desc": "Co-controlled S&A Concrete with Castellano. Genovese side of the Concrete Club.", "sources": [42, 52]},
    {"source": "Paul Castellano", "target": "S&A Concrete", "type": "director_of", "tier": "documented", "desc": "Co-controlled S&A Concrete with Salerno. Gambino side of the Concrete Club.", "sources": [42]},
    {"source": "S&A Concrete", "target": "Donald Trump", "type": "connected_to", "tier": "documented", "desc": "Provided concrete for Trump Tower construction. $2M+ contract during Concrete Club monopoly era.", "sources": [42, 48]},

    # ---- Gotti network ----
    {"source": "John Gotti", "target": "Castellano Assassination (1985)", "type": "connected_to", "tier": "documented", "desc": "Orchestrated the assassination. Watched from a car across the street. Became boss without Commission approval.", "sources": [55]},
    {"source": "Castellano Assassination (1985)", "target": "Paul Castellano", "type": "connected_to", "tier": "documented", "desc": "Shot outside Sparks Steak House, December 16, 1985.", "sources": [55]},
    {"source": "Roy Cohn", "target": "John Gotti", "type": "legal_counsel", "tier": "credible", "desc": "Cohn represented Gotti, adding him to a client list that already included Salerno and Castellano.", "sources": [47, 54]},
    {"source": "Robert LiButti", "target": "John Gotti", "type": "affiliated_with", "tier": "documented", "desc": "FBI wiretap: LiButti called Gotti 'my boss.' Gambino associate.", "sources": [27, 48]},
    {"source": "Robert LiButti", "target": "Donald Trump", "type": "connected_to", "tier": "documented", "desc": "Lost $12M at Trump casinos. Trump Plaza fined $450K for $1.65M in gifts, $200K for removing Black/female dealers.", "sources": [27, 48]},
    {"source": "Sammy Gravano", "target": "John Gotti", "type": "affiliated_with", "tier": "documented", "desc": "Underboss who turned government witness. Testimony convicted Gotti on 13 counts including 5 murders.", "sources": [55]},
    {"source": "Sammy Gravano", "target": "Gambino Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Gambino family underboss. Admitted to 19 murders. Highest-ranking Mafia member to cooperate with FBI.", "sources": [55]},
    {"source": "Sammy Gravano", "target": "FBI", "type": "asset_of", "tier": "documented", "desc": "Government witness from 1991. Testimony devastated the Gambino family.", "sources": [55]},

    # ---- Commission Trial ----
    {"source": "Commission Trial (1986)", "target": "Fat Tony Salerno", "type": "connected_to", "tier": "documented", "desc": "Convicted at Commission Trial, sentenced to 100 years.", "sources": [41]},
    {"source": "Commission Trial (1986)", "target": "The Commission", "type": "connected_to", "tier": "documented", "desc": "RICO prosecution that broke the Commission's power as governing body.", "sources": [41]},

    # ---- Philadelphia crime family succession ----
    {"source": "Angelo Bruno", "target": "Philadelphia Crime Family", "type": "boss_of", "tier": "documented", "desc": "Boss 1959-1980. The Docile Don. First Philly boss with major Commission influence.", "sources": [55, 49]},
    {"source": "Angelo Bruno", "target": "Meyer Lansky", "type": "affiliated_with", "tier": "documented", "desc": "Gambling partnership including Colony Sports Club in London. Bruno-Lansky axis connected Philly to global finance.", "sources": [11, 55]},
    {"source": "Angelo Bruno", "target": "The Commission", "type": "affiliated_with", "tier": "documented", "desc": "First Philadelphia boss to hold an influential Commission seat, through friendship with Carlo Gambino.", "sources": [55]},
    {"source": "Nicky Scarfo", "target": "Philadelphia Crime Family", "type": "boss_of", "tier": "documented", "desc": "Boss 1981-1991. Ruled through terror. Controlled Atlantic City construction.", "sources": [49, 43]},
    {"source": "Nicky Scarfo", "target": "Angelo Bruno", "type": "connected_to", "tier": "documented", "desc": "Succeeded Bruno after the bloody succession war. Opposite philosophy — terror vs diplomacy.", "sources": [49]},
    {"source": "Nicky Scarfo", "target": "Scarf Inc", "type": "director_of", "tier": "documented", "desc": "Controlled Atlantic City construction through Scarf Inc.", "sources": [43, 49]},
    {"source": "Scarf Inc", "target": "Donald Trump", "type": "connected_to", "tier": "documented", "desc": "Scarfo's construction operations controlled the foundations Trump's Atlantic City casinos were built on.", "sources": [43, 53]},
    {"source": "Kenneth Shapiro", "target": "Nicky Scarfo", "type": "affiliated_with", "tier": "documented", "desc": "Financial advisor and front man for casino-area land deals. Mob's money man in Atlantic City.", "sources": [43, 49]},
    {"source": "Kenneth Shapiro", "target": "Donald Trump", "type": "connected_to", "tier": "documented", "desc": "Facilitated property transactions for Trump's casino operations in Atlantic City.", "sources": [43, 53]},
    {"source": "Salvatore Testa", "target": "Nicky Scarfo", "type": "affiliated_with", "tier": "documented", "desc": "Feared enforcer under Scarfo. Murdered on Scarfo's orders in 1984 — Scarfo feared his growing power.", "sources": [49]},
    {"source": "Salvatore Testa", "target": "Donald Trump", "type": "connected_to", "tier": "documented", "desc": "Sold land used for Trump's Atlantic City casino development before his murder.", "sources": [53]},
    {"source": "Salvatore Testa", "target": "Philadelphia Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Son of boss Phil Testa. 'Crown Prince of the Mob.' Feared enforcer.", "sources": [49]},
    {"source": "John Stanfa", "target": "Philadelphia Crime Family", "type": "boss_of", "tier": "documented", "desc": "Boss 1991-1994. Installed with Gambino backing. Driver for Bruno on night of assassination.", "sources": [44, 45]},
    {"source": "John Stanfa", "target": "Gambino Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Installed as Philadelphia boss with Gambino family backing. Brothers were made Gambino members under Gotti.", "sources": [44]},
    {"source": "John Stanfa", "target": "Angelo Bruno", "type": "connected_to", "tier": "documented", "desc": "Was Bruno's driver on the night of the 1980 assassination. A bullet grazed Stanfa's shoulder.", "sources": [44, 45]},
    {"source": "John-John Veasey", "target": "John Stanfa", "type": "affiliated_with", "tier": "documented", "desc": "Enforcer and triggerman for Stanfa. Stanfa later ordered Veasey killed — survived 4 gunshots and 7 stab wounds.", "sources": [44, 45, 46]},
    {"source": "John-John Veasey", "target": "Philadelphia Crime Family", "type": "affiliated_with", "tier": "documented", "desc": "Grew up in South Philadelphia crime family territory. Became enforcer during Stanfa era.", "sources": [44, 45]},
    {"source": "John-John Veasey", "target": "FBI", "type": "asset_of", "tier": "documented", "desc": "Turned FBI informant after surviving assassination attempt. Testimony convicted Stanfa and 7 associates.", "sources": [44, 45, 46]},
    {"source": "Joey Merlino", "target": "Philadelphia Crime Family", "type": "boss_of", "tier": "documented", "desc": "Boss from 1999. Won the Stanfa-Merlino war. Last traditional boss of the Philadelphia family.", "sources": [44, 45]},
    {"source": "Joey Merlino", "target": "John Stanfa", "type": "connected_to", "tier": "documented", "desc": "Led the young faction against Stanfa in the bloody 1992-1994 war. Survived being shot in 1993.", "sources": [44, 45]},
    {"source": "John Gotti", "target": "John Stanfa", "type": "connected_to", "tier": "credible", "desc": "Stanfa installed as Philly boss with Gambino backing during Gotti's reign.", "sources": [44]},

    # ---- Rafi Eitan / Intelligence bridge ----
    {"source": "Rafi Eitan", "target": "Meyer Lansky", "type": "affiliated_with", "tier": "credible", "desc": "Worked directly with Lansky on Haganah arms smuggling (1945-48). Israeli intelligence-organized crime bridge.", "sources": [11, 50]},
    {"source": "Rafi Eitan", "target": "Mossad", "type": "employed_by", "tier": "documented", "desc": "Legendary Israeli intelligence operative. Led team that captured Eichmann. Ran Pollard spy case.", "sources": [11]},
    {"source": "Rafi Eitan", "target": "Robert Maxwell", "type": "connected_to", "tier": "credible", "desc": "Connected through PROMIS distribution network and Israeli intelligence operations.", "sources": [11]},
    {"source": "Rafi Eitan", "target": "PROMIS", "type": "connected_to", "tier": "credible", "desc": "Israeli intelligence connection to PROMIS software distribution through Maxwell network.", "sources": [11, 21]},
]


# ============================================================
# ENTITY_SOURCES — direct entity-to-source citations
# (populated into entity_sources junction table)
# ============================================================

ENTITY_SOURCES = {
    "Jeffrey Epstein": [4, 5, 6, 9, 11, 26, 28, 29, 30, 31, 34, 35, 36, 39],
    "Ghislaine Maxwell": [11, 29, 30, 35, 36],
    "Les Wexner": [11, 14, 33],
    "William Barr": [1, 8, 11],
    "Roy Cohn": [11, 27, 37, 38],
    "Peter Thiel": [22, 23, 24],
    "Donald Trump": [11, 26, 27, 28, 37, 38, 40],
    "Alexander Acosta": [6, 28, 31],
    "Alan Dershowitz": [6, 29, 30, 35],
    "Donald Barr": [11],
    "Bill Clinton": [11, 30],
    "Robert Maxwell": [11, 21],
    "Leon Black": [4],
    "Ehud Barak": [9, 11],
    "Fat Tony Salerno": [27, 37],
    "Paul Castellano": [27, 37],
    "Felix Sater": [40],
    "John Gotti": [41, 47, 48, 54, 55],
    "Angelo Bruno": [49, 55],
    "Nicky Scarfo": [43, 49, 53],
    "John Stanfa": [44, 45, 46],
    "Joey Merlino": [44, 45],
    "John-John Veasey": [44, 45, 46],
    "Lucky Luciano": [50, 55],
    "Bugsy Siegel": [55],
    "Sammy Gravano": [55],
    "Frankie Carbo": [55],
    "Blinky Palermo": [55],
    "Kenneth Shapiro": [43, 49, 53],
    "Salvatore Testa": [49, 53],
    "Robert LiButti": [27, 48],
    "Rafi Eitan": [11, 50],
    "Meyer Lansky": [11, 50, 51, 55],
    "The Commission": [41, 55],
    "Gambino Crime Family": [41, 55],
    "Genovese Crime Family": [41, 52],
    "Lucchese Crime Family": [55],
    "Philadelphia Crime Family": [43, 44, 45, 49],
    "Murder Incorporated": [55],
    "Scarf Inc": [43, 49],
    "S&A Concrete": [42, 48, 52],
}
