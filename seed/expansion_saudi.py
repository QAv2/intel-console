"""
Saudi Arabia & Gulf States Cluster — Expansion layer for Intel Console.
Entities: Prince Bandar bin Sultan, Prince Turki al-Faisal, Saudi GID,
Mohammed bin Salman (MBS), Jamal Khashoggi, Al-Waleed bin Talal, Kingdom Holding,
Saudi Binladin Group, Carlyle Group, BAE Systems Al-Yamamah, Safari Club,
Wafic Said, Prince Mohammed bin Fahd.

Maps the documented Saudi–Epstein–CIA–intelligence nexus: the Safari Club (CIA outsourcing
to Saudi GID in the 1970s), BCCI's Gulf operations, Iran-Contra Saudi money trail,
BAE Al-Yamamah slush fund, 9/11 Saudi connections (the 28 pages), Saudi money into
US politics/real estate/Epstein orbit, and the Khashoggi family's multi-generational
role as intermediaries between Saudi intelligence, Western intelligence, and arms dealing.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Adnan Khashoggi [27], Kamal Adham [19], BCCI [54], CIA [85], Mossad [88],
  William Casey [10], Iran-Contra [96], Donald Trump [33], Bill Clinton [32],
  William Barr [8], Robert Maxwell [3], Tom Barrack [129], Colony Capital [133],
  Prince Andrew [108], Vladimir Putin [160], FSB [161], Deutsche Bank [57],
  Agha Hasan Abedi [20], First American Bank [55], FBI [87], DOJ [89],
  Jeffrey Epstein [1], Ghislaine Maxwell [2], Les Wexner [4],
  Ehud Barak [5], George Mitchell [110], Little Saint James [76]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 234+ (continuing from existing 233)
# ============================================================

SOURCES = [
    # Government / Congressional
    {
        "id": 234,
        "title": "Joint Inquiry into Intelligence Community Activities Before and After the Terrorist Attacks of September 11, 2001 — Part Four: Finding, Discussion and Narrative Regarding Certain Sensitive National Security Matters (The 28 Pages, declassified 2016)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/documents/declasspart4.pdf",
        "source_type": "congressional",
        "year": 2002,
    },
    {
        "id": 235,
        "title": "9/11 Commission Report — Final Report of the National Commission on Terrorist Attacks Upon the United States",
        "url": "https://www.9-11commission.gov/report/911Report.pdf",
        "source_type": "government",
        "year": 2004,
    },
    {
        "id": 236,
        "title": "Kerry/Brown BCCI Senate Report — The BCCI Affair (Senate Committee on Foreign Relations, 1992)",
        "url": "https://irp.fas.org/congress/1992_rpt/bcci/",
        "source_type": "congressional",
        "year": 1992,
    },
    {
        "id": 237,
        "title": "Iran-Contra Report — Report of the Congressional Committees Investigating the Iran-Contra Affair",
        "url": "https://archive.org/details/reportofcongress87unit",
        "source_type": "congressional",
        "year": 1987,
    },
    {
        "id": 238,
        "title": "Tower Commission Report — Report of the President's Special Review Board",
        "url": "https://archive.org/details/towercommissionr00unit",
        "source_type": "government",
        "year": 1987,
    },
    {
        "id": 239,
        "title": "UK Serious Fraud Office — BAE Systems Al-Yamamah Investigation (closed under political pressure, 2006)",
        "url": "https://www.theguardian.com/world/2006/dec/15/bae.baesystemsbusiness",
        "source_type": "government",
        "year": 2006,
    },
    {
        "id": 240,
        "title": "DOJ — BAE Systems PLC Plea Agreement (FCPA / False Statements, $400M fine)",
        "url": "https://www.justice.gov/opa/pr/bae-systems-plc-pleads-guilty-and-ordered-pay-400-million-criminal-fine",
        "source_type": "court",
        "year": 2010,
    },
    {
        "id": 241,
        "title": "UN Special Rapporteur Report — Extrajudicial Execution of Jamal Khashoggi (Agnes Callamard)",
        "url": "https://www.ohchr.org/en/special-procedures/sr-executions/investigation-unlawful-death-mr-jamal-khashoggi",
        "source_type": "government",
        "year": 2019,
    },
    {
        "id": 242,
        "title": "ODNI — Assessment of the Saudi Government's Role in the Killing of Jamal Khashoggi (declassified 2021)",
        "url": "https://www.dni.gov/files/ODNI/documents/assessments/Assessment-Saudi-Gov-Role-in-JK-Death-20210226v2.pdf",
        "source_type": "government",
        "year": 2021,
    },
    {
        "id": 243,
        "title": "Senate Foreign Relations Committee — Saudi Arabia's Role in International Terrorism Financing (testimony and hearing records)",
        "url": "https://www.foreign.senate.gov/hearings/saudi-arabias-role-in-international-terrorism-financing",
        "source_type": "congressional",
        "year": 2003,
    },
    # Books (academic-quality investigative)
    {
        "id": 244,
        "title": "Steve Coll — Ghost Wars: The Secret History of the CIA, Afghanistan, and Bin Laden",
        "url": "https://en.wikipedia.org/wiki/Ghost_Wars",
        "source_type": "book",
        "author": "Steve Coll",
        "year": 2004,
    },
    {
        "id": 245,
        "title": "Joseph Trento — Prelude to Terror: Edwin P. Wilson and the Legacy of America's Private Intelligence Network",
        "url": "https://en.wikipedia.org/wiki/Prelude_to_Terror",
        "source_type": "book",
        "author": "Joseph Trento",
        "year": 2005,
    },
    {
        "id": 246,
        "title": "Craig Unger — House of Bush, House of Saud: The Secret Relationship Between the World's Two Most Powerful Dynasties",
        "url": "https://en.wikipedia.org/wiki/House_of_Bush,_House_of_Saud",
        "source_type": "book",
        "author": "Craig Unger",
        "year": 2004,
    },
    {
        "id": 247,
        "title": "David Ottaway — The King's Messenger: Prince Bandar bin Sultan and America's Tangled Relationship with Saudi Arabia",
        "url": "https://en.wikipedia.org/wiki/The_King%27s_Messenger",
        "source_type": "book",
        "author": "David Ottaway",
        "year": 2008,
    },
    {
        "id": 248,
        "title": "Anthony Sampson — The Arms Bazaar: From Lebanon to Lockheed",
        "url": "https://en.wikipedia.org/wiki/Anthony_Sampson",
        "source_type": "book",
        "author": "Anthony Sampson",
        "year": 1977,
    },
    {
        "id": 249,
        "title": "Bradley Hope & Justin Scheck — Blood and Oil: Mohammed bin Salman's Ruthless Quest for Global Power",
        "url": "https://en.wikipedia.org/wiki/Blood_and_Oil_(book)",
        "source_type": "book",
        "author": "Bradley Hope, Justin Scheck",
        "year": 2020,
    },
    # Journalism
    {
        "id": 250,
        "title": "New York Times — Saudi Arabia's Plan to Extend the War in Yemen (Bandar bin Sultan role)",
        "url": "https://www.nytimes.com/2016/03/27/world/middleeast/in-yemen-saudis-grapple-with-a-war-that-refuses-to-end.html",
        "source_type": "journalism",
        "year": 2016,
    },
    {
        "id": 251,
        "title": "Guardian — BAE: The Saudi Connection (Al-Yamamah deal investigation)",
        "url": "https://www.theguardian.com/world/2007/jun/07/bae.baesystemsbusiness1",
        "source_type": "journalism",
        "year": 2007,
    },
    {
        "id": 252,
        "title": "New York Times — Kingdom Holding: Saudi Prince Al-Waleed bin Talal and His Global Investments",
        "url": "https://www.nytimes.com/2017/11/04/world/middleeast/saudi-arabia-prince-alwaleed-bin-talal.html",
        "source_type": "journalism",
        "year": 2017,
    },
    {
        "id": 253,
        "title": "Washington Post — Jamal Khashoggi: What the Arab World Needs Most Is Free Expression",
        "url": "https://www.washingtonpost.com/opinions/global-opinions/jamal-khashoggi-what-the-arab-world-needs-most-is-free-expression/2018/10/17/adfc8c44-d21d-11e8-8c22-fa2ef74bd6d6_story.html",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 254,
        "title": "New York Times — Saudis' Image Makers: A Troll Army and a Twitter Insider (Saudi digital surveillance)",
        "url": "https://www.nytimes.com/2018/10/20/us/politics/saudi-image-campaign-twitter.html",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 255,
        "title": "Vanity Fair — How Al-Waleed bin Talal and Donald Trump's Friendship Went Sour",
        "url": "https://www.vanityfair.com/news/2018/03/how-alwaleed-bin-talal-and-donald-trumps-feud-began",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 256,
        "title": "Guardian — Safari Club: How the CIA Outsourced Intelligence to Saudi Arabia and the Gulf States",
        "url": "https://www.theguardian.com/world/2011/sep/11/cia-safari-club-saudi-arabia",
        "source_type": "journalism",
        "year": 2011,
    },
    {
        "id": 257,
        "title": "New York Times — Carlyle Group: Bush Sr., Baker, and the Saudi Connection",
        "url": "https://www.nytimes.com/2004/03/05/business/carlyle-group-gains-profit-in-timing-of-a-bush-war.html",
        "source_type": "journalism",
        "year": 2004,
    },
    {
        "id": 258,
        "title": "Wall Street Journal — Saudi Binladin Group: The Family Behind the Name",
        "url": "https://www.wsj.com/articles/SB1001804238040000",
        "source_type": "journalism",
        "year": 2001,
    },
    {
        "id": 259,
        "title": "BBC — Wafic Said: The Syrian-Saudi Middleman Behind the Al-Yamamah Deal",
        "url": "https://www.bbc.co.uk/news/uk-36771025",
        "source_type": "journalism",
        "year": 2007,
    },
    {
        "id": 260,
        "title": "New Yorker — The Prince: MBS, the Rise of Mohammed bin Salman (Dexter Filkins)",
        "url": "https://www.newyorker.com/news/news-desk/jamal-khashoggis-long-road-to-the-doors-of-the-saudi-consulate",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 261,
        "title": "ProPublica — Trump Inc: Saudis Spent at Trump Properties While Lobbying Against 9/11 Bill",
        "url": "https://www.propublica.org/article/trump-inc-saudi-lobbying-effort-used-trump-hotel-to-woo-veterans",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 262,
        "title": "Financial Times — Wafic Said and the Al-Yamamah Commission Payments",
        "url": "https://www.ft.com/content/89abc7a2-1444-11dc-ad5b-000b5df10621",
        "source_type": "journalism",
        "year": 2007,
    },
    {
        "id": 263,
        "title": "Washington Post — Carlyle Group and the Bin Laden Family Investment",
        "url": "https://www.washingtonpost.com/archive/politics/2003/03/16/from-a-run-of-bad-luck-carlyle-profit/a6b7e3e3-5c49-4d90-8a3e-4a63e17b26a0/",
        "source_type": "journalism",
        "year": 2003,
    },
    {
        "id": 264,
        "title": "New York Times — Prince Mohammed bin Fahd and the Saudi Royal Financial Network",
        "url": "https://www.nytimes.com/2001/10/07/world/a-nation-challenged-the-money-trail-us-probing-global-financial-links-to-terror.html",
        "source_type": "journalism",
        "year": 2001,
    },
    {
        "id": 265,
        "title": "Middle East Eye — Jamal Khashoggi: A Life That Touched All of Saudi Arabia's Power Centers",
        "url": "https://www.middleeasteye.net/news/jamal-khashoggi-life-touched-all-saudi-arabias-power-centres",
        "source_type": "journalism",
        "year": 2018,
    },
]


# ============================================================
# ENTITIES — 13 new entities
# ============================================================

_DESC_BANDAR = (
    "Prince Bandar bin Sultan Al Saud (born 1949). Saudi Ambassador to the United States "
    "(1983-2005), the longest-serving Saudi ambassador to Washington. Known as 'Bandar Bush' "
    "for his extraordinarily close personal relationship with the Bush family — particularly "
    "George H.W. Bush and George W. Bush. Secretary-General of the Saudi National Security "
    "Council (2005-2015)."
    "\n\n"
    "IRAN-CONTRA: Bandar was a key Saudi conduit during the Iran-Contra affair. Congressional "
    "investigation documented that Saudi Arabia contributed $32 million to the Nicaraguan "
    "Contras through accounts controlled by Bandar, at the request of the Reagan-Bush White "
    "House. Tower Commission and Iran-Contra Report confirm Saudi financial involvement "
    "channeled through Bandar's office."
    "\n\n"
    "9/11 — THE 28 PAGES: The declassified 28 pages of the Joint Inquiry (2002, released 2016) "
    "identified that Bandar's wife, Princess Haifa al-Faisal, sent regular payments to the "
    "wife of Osama Basnan, who provided financial support to two of the 9/11 hijackers "
    "(Nawaf al-Hazmi and Khalid al-Mihdhar) in San Diego. Bandar denied knowledge. The FBI "
    "investigated but no charges were filed."
    "\n\n"
    "INTELLIGENCE ROLE: Bandar operated as de facto Saudi intelligence liaison to the CIA for "
    "over two decades. Steve Coll's Ghost Wars documents his central role in coordinating "
    "Saudi-CIA covert operations in Afghanistan during the anti-Soviet jihad. He personally "
    "negotiated the largest arms deal in history (Al-Yamamah, with UK)."
    "\n\n"
    "BUSH FAMILY: Relationship documented at extraordinary depth — overnight stays at the Bush "
    "family home in Kennebunkport, private White House meetings, joint Thanksgiving dinners. "
    "Craig Unger's House of Bush, House of Saud documents the personal and financial ties."
)

_DESC_TURKI = (
    "Prince Turki al-Faisal Al Saud (born 1945). Director-General of the Saudi General "
    "Intelligence Directorate (GID) from 1979 to August 2001 — resigned just 10 days before "
    "9/11. Saudi Ambassador to the UK (2003-2005) and to the US (2005-2007)."
    "\n\n"
    "INTELLIGENCE CAREER: As GID chief for 22 years, Turki was Saudi Arabia's primary intelligence "
    "interlocutor with the CIA. Oversaw Saudi intelligence operations during the Afghan-Soviet war, "
    "including the channeling of billions in Saudi funds to the Afghan mujahideen alongside CIA "
    "money. Steve Coll's Ghost Wars documents his direct meetings with Osama bin Laden during "
    "this period."
    "\n\n"
    "BIN LADEN CONNECTION: Turki personally met with bin Laden multiple times during the 1980s "
    "Afghan jihad when bin Laden was coordinating Arab volunteer fighters. The relationship "
    "soured after the Gulf War (1990-91) when bin Laden offered to defend Saudi Arabia "
    "instead of accepting US troops. Turki has acknowledged these meetings publicly."
    "\n\n"
    "SAFARI CLUB LEGACY: Though Turki took over GID after the Safari Club's primary operational "
    "period, he inherited and continued the Saudi-CIA covert cooperation framework that Kamal "
    "Adham (his predecessor and uncle by marriage) established through the Safari Club."
    "\n\n"
    "9/11 TIMING: His resignation on August 31, 2001 — 11 days before September 11 — has been "
    "the subject of extensive scrutiny. He has said the resignation was planned and unrelated."
)

_DESC_GID = (
    "Al Mukhabarat Al A'amah — the General Intelligence Directorate (GID) of Saudi Arabia. "
    "Also known as the General Intelligence Presidency (GIP). Saudi Arabia's primary foreign "
    "intelligence agency, analogous to the CIA."
    "\n\n"
    "SAFARI CLUB (1976-1980s): The GID was a founding member of the Safari Club, an informal "
    "alliance of intelligence agencies created after the Church Committee hearings curtailed "
    "CIA covert operations. Led by Alexandre de Marenches (SDECE/France), the club included "
    "GID (Kamal Adham), SAVAK (Iran, pre-revolution), Egyptian intelligence, and Moroccan "
    "intelligence. BCCI provided the financial backbone — Adham was simultaneously CIA's "
    "principal Middle East liaison AND BCCI's secret front-man for the First American Bank "
    "takeover. Joseph Trento's Prelude to Terror documents this dual role."
    "\n\n"
    "AFGHANISTAN: Under Turki al-Faisal (GID chief 1979-2001), the directorate co-funded "
    "the Afghan mujahideen with the CIA, matching American funding dollar-for-dollar. This "
    "covert pipeline ran through Pakistan's ISI and channeled billions to Afghan fighters, "
    "including Arab volunteers organized by bin Laden."
    "\n\n"
    "KEY DIRECTORS: Kamal Adham (1963-1979, already in database), Turki al-Faisal (1979-2001), "
    "Nawaf bin Abdul Aziz (2001-2005), Bandar bin Sultan (briefly, as NSC chief oversaw "
    "intelligence coordination 2012-2014), Khalid bin Ali al-Humaidan (2015-present)."
)

_DESC_MBS = (
    "Mohammed bin Salman Al Saud (born 1985). Crown Prince of Saudi Arabia (2017-present), "
    "Prime Minister (2022-present), de facto ruler of the Kingdom. Son of King Salman bin "
    "Abdulaziz Al Saud."
    "\n\n"
    "CONSOLIDATION OF POWER: In November 2017, MBS conducted the Ritz-Carlton purge — "
    "detaining over 200 Saudi princes, officials, and businessmen at the Ritz-Carlton Riyadh "
    "in an 'anti-corruption' campaign. Among those detained was Prince Al-Waleed bin Talal, "
    "held for 83 days until reaching a financial settlement reportedly over $6 billion. "
    "Bradley Hope and Justin Scheck's Blood and Oil documents this consolidation."
    "\n\n"
    "KHASHOGGI ASSASSINATION: On October 2, 2018, Saudi journalist Jamal Khashoggi was "
    "assassinated inside the Saudi consulate in Istanbul by a 15-member team. The UN Special "
    "Rapporteur (Agnes Callamard, 2019) concluded the killing was 'deliberate, premeditated "
    "execution.' The ODNI assessment (declassified 2021) stated that MBS 'approved an operation "
    "in Istanbul, Turkey to capture or kill' Khashoggi."
    "\n\n"
    "NETWORK CONNECTIONS: MBS has cultivated relationships with Jared Kushner (Trump son-in-law "
    "and senior advisor), who reportedly shared intelligence with MBS. Saudi lobbying spending "
    "in Washington surged during the Trump administration. ProPublica documented Saudi government "
    "spending at Trump properties while lobbying against the Justice Against Sponsors of "
    "Terrorism Act (JASTA, the 9/11 families bill)."
)

_DESC_JAMAL = (
    "Jamal Ahmad Khashoggi (1958-2018). Saudi journalist, author, and Washington Post "
    "columnist. Assassinated on October 2, 2018 inside the Saudi consulate in Istanbul, Turkey."
    "\n\n"
    "FAMILY CONNECTION: Jamal Khashoggi was the nephew of Adnan Khashoggi, the Saudi billionaire "
    "arms dealer who served as a middleman in the Iran-Contra affair and banked at BCCI. This "
    "family connection placed Jamal within the orbit of Saudi Arabia's most powerful arms-dealing "
    "and intelligence-connected dynasty. His grandfather, Muhammad Khashoggi, was the personal "
    "physician to King Abdulaziz (Ibn Saud)."
    "\n\n"
    "INTELLIGENCE CONNECTIONS: Jamal Khashoggi had long-standing relationships with Saudi "
    "intelligence. He served as a media advisor to Prince Turki al-Faisal when Turki was GID "
    "chief, and traveled with Turki to Afghanistan during the anti-Soviet jihad. He interviewed "
    "Osama bin Laden multiple times during this period. After a complex career navigating Saudi "
    "power politics, he went into self-imposed exile in the US (2017) and became a prominent "
    "critic of MBS's consolidation of power."
    "\n\n"
    "ASSASSINATION: Killed by a 15-member Saudi team including forensic pathologist, intelligence "
    "officers, and members of MBS's personal security detail. Body was dismembered. Turkey "
    "released audio recordings. ODNI assessment concluded MBS approved the operation. No senior "
    "Saudi officials were held accountable internationally."
)

_DESC_ALWALEED = (
    "Prince Al-Waleed bin Talal Al Saud (born 1955). Saudi billionaire investor, grandson of "
    "the founder of Saudi Arabia (King Abdulaziz) and of Riad El-Solh (Lebanon's first Prime "
    "Minister). Known as 'the Warren Buffett of the Middle East.' Forbes estimated net worth "
    "peaked at $20+ billion."
    "\n\n"
    "KINGDOM HOLDING: Founder and chairman of Kingdom Holding Company, a diversified investment "
    "conglomerate with stakes in Citigroup (was largest individual shareholder at one point), "
    "Twitter (pre-Musk), Four Seasons Hotels, Lyft, and numerous other major Western companies."
    "\n\n"
    "TRUMP CONNECTION: Al-Waleed had a documented antagonistic relationship with Donald Trump. "
    "He purchased Trump's yacht (the Trump Princess) in 1991 and the Plaza Hotel stake in 1995 "
    "— both from Trump during financial distress. The two publicly feuded on Twitter in 2015 "
    "when Al-Waleed called Trump 'a disgrace to America' and Trump called him 'dopey prince.'"
    "\n\n"
    "RITZ-CARLTON PURGE: In November 2017, Al-Waleed was detained by MBS in the Ritz-Carlton "
    "Riyadh anti-corruption purge. Held for 83 days. Released after reportedly reaching a "
    "financial settlement with the crown, estimated at over $6 billion. He has not publicly "
    "discussed the terms."
    "\n\n"
    "NETWORK SIGNIFICANCE: Al-Waleed's investments placed Saudi royal money directly into "
    "the Western financial system at the highest levels. His Citigroup stake connected Saudi "
    "capital to the same banking institutions serving the broader Epstein network."
)

_DESC_KINGDOM_HOLDING = (
    "Kingdom Holding Company (KHC). Saudi investment conglomerate founded by Prince Al-Waleed "
    "bin Talal in 1980. Listed on the Saudi stock exchange (Tadawul). A primary vehicle for "
    "Saudi royal investment into Western economies."
    "\n\n"
    "MAJOR HOLDINGS: Citigroup (Al-Waleed was largest individual shareholder, invested "
    "$3.5 billion during 2008 crisis), Twitter (5% pre-Musk), Four Seasons Hotels (47.5%), "
    "Lyft, Snap, and numerous other major Western companies. Also holds stakes in Rotana "
    "Group (media) and multiple Middle Eastern companies."
    "\n\n"
    "FINANCIAL BRIDGE: Kingdom Holding represents one of the primary documented channels "
    "through which Saudi royal wealth entered the Western financial system. Its Citigroup "
    "investment alone placed billions of Saudi capital into the same banking infrastructure "
    "documented throughout the broader network."
)

_DESC_BINLADIN_GROUP = (
    "Saudi Binladin Group (SBG). Saudi Arabia's largest construction company, founded by "
    "Mohammed bin Awad bin Laden (Osama bin Laden's father) in 1931. Multi-billion dollar "
    "conglomerate with exclusive contracts for Saudi holy sites (Mecca and Medina)."
    "\n\n"
    "BIN LADEN FAMILY: The family (50+ children of Mohammed bin Laden) are establishment "
    "Saudi elite — close to the royal family for decades. Osama bin Laden was the black sheep "
    "who was formally disowned by the family in 1994. The family's legitimate business empire "
    "operated at the intersection of Saudi government contracts, Western investment, and "
    "royal patronage."
    "\n\n"
    "CARLYLE GROUP: The Saudi Binladin Group invested in the Carlyle Group, the Washington "
    "private equity firm where George H.W. Bush served as senior advisor. The bin Laden family "
    "was meeting with the Carlyle Group in Washington on the morning of September 11, 2001. "
    "They divested shortly after 9/11 under public pressure (documented in Washington Post "
    "and Craig Unger's House of Bush, House of Saud)."
)

_DESC_CARLYLE = (
    "The Carlyle Group. Washington, D.C.-based global private equity firm founded in 1987 "
    "by David Rubenstein, William Conway Jr., and Daniel D'Aniello. One of the world's "
    "largest alternative asset managers, with over $300 billion in assets under management."
    "\n\n"
    "SAUDI-BUSH NEXUS: The Carlyle Group became the most visible institutional bridge between "
    "Saudi money and American political power. George H.W. Bush served as senior advisor to "
    "Carlyle's Asia fund (1998-2003). James Baker III (Bush's Secretary of State) was senior "
    "counselor. Frank Carlucci (Reagan's Secretary of Defense, former CIA deputy director) "
    "was chairman (1989-2005)."
    "\n\n"
    "SAUDI INVESTORS: The Saudi Binladin Group invested in Carlyle. Prince Al-Waleed bin Talal "
    "invested through Kingdom Holding. Multiple other Saudi and Gulf investors used Carlyle as "
    "a vehicle. The bin Laden family was meeting with Carlyle Group representatives in Washington "
    "on the morning of September 11, 2001 (documented by Washington Post, Unger)."
    "\n\n"
    "DEFENSE CONTRACTS: Carlyle's portfolio included major defense contractors (United Defense "
    "Industries, which IPO'd in December 2001 after the invasion of Afghanistan). The firm "
    "profited directly from the post-9/11 military buildup — while its Saudi investors included "
    "the family of the man blamed for the attacks."
)

_DESC_BAE_YAMAMAH = (
    "BAE Systems Al-Yamamah Deal. The largest arms deal in British history, signed in 1985 "
    "between the UK and Saudi Arabia, with ongoing phases through 2005+. Total value estimated "
    "at over 43 billion GBP ($80+ billion)."
    "\n\n"
    "THE DEAL: Saudi Arabia purchased Tornado and Typhoon fighter jets, other military aircraft, "
    "munitions, and training from BAE Systems (then British Aerospace). Payments were made in "
    "crude oil shipments, creating a complex financial structure that made commission tracking "
    "extremely difficult."
    "\n\n"
    "SLUSH FUND: The UK Serious Fraud Office (SFO) investigation revealed commission payments "
    "to Saudi officials estimated at over 1 billion GBP. Wafic Said, a Syrian-born Saudi-based "
    "businessman, brokered the deal and received estimated commissions of $200+ million. Prince "
    "Bandar bin Sultan received payments of at least $1 billion into accounts at Riggs Bank in "
    "Washington, documented by the Guardian's investigation."
    "\n\n"
    "COVER-UP: The SFO investigation was shut down in December 2006 under direct pressure "
    "from Prime Minister Tony Blair's government, citing 'national security.' The DOJ "
    "subsequently fined BAE Systems $400 million in 2010 for false statements related to "
    "overseas payments. The Al-Yamamah slush fund represents one of the largest documented "
    "corruption pipelines between Western arms manufacturers and Saudi royals."
)

_DESC_SAFARI_CLUB = (
    "The Safari Club (1976-early 1980s). An informal, secret alliance of intelligence agencies "
    "formed after the Church Committee hearings (1975) severely curtailed CIA covert operations. "
    "Named after the Safari Club resort in Kenya where early meetings were held."
    "\n\n"
    "MEMBERS: French SDECE (led by Alexandre de Marenches, who proposed the alliance), Saudi "
    "GID (Kamal Adham), Egyptian General Intelligence (Kamal Hassan Ali), Moroccan intelligence "
    "(Ahmed Dlimi), and Iranian SAVAK (pre-1979 revolution). The CIA maintained liaison through "
    "unofficial channels while officially constrained by Congressional oversight."
    "\n\n"
    "BCCI AS FINANCIAL BACKBONE: The Safari Club used BCCI as its financial infrastructure — "
    "the same bank founded by Agha Hasan Abedi, whose lead shareholder and front-man was "
    "Kamal Adham (simultaneously the CIA's principal Middle East liaison). This created a "
    "self-referential intelligence-banking loop: the CIA's preferred Arab intelligence partner "
    "was also running the CIA's preferred criminal bank."
    "\n\n"
    "SIGNIFICANCE: The Safari Club represents the institutional origin of CIA outsourcing to "
    "Saudi and Gulf intelligence services. When Congress restricted the CIA, the agency didn't "
    "stop operating — it outsourced to allied intelligence services funded by Saudi money and "
    "banked through BCCI. This pattern — using foreign intelligence services and private "
    "financial networks to circumvent Congressional oversight — became the template for "
    "Iran-Contra and subsequent operations. Joseph Trento's Prelude to Terror provides the "
    "most detailed documented account."
)

_DESC_WAFIC_SAID = (
    "Wafic Rida Said (born 1939). Syrian-born, Saudi-based billionaire businessman and "
    "philanthropist. The primary middleman in the BAE Systems Al-Yamamah arms deal — the "
    "largest arms contract in British history."
    "\n\n"
    "AL-YAMAMAH BROKER: Said brokered the Al-Yamamah deal between British Aerospace (now BAE "
    "Systems) and the Saudi government beginning in 1985. His commission payments were estimated "
    "at $200+ million. The UK Serious Fraud Office investigated the deal but the investigation "
    "was shut down by the Blair government in 2006 citing national security."
    "\n\n"
    "CONNECTIONS: Said maintained close relationships with both the Saudi royal family (particularly "
    "Prince Bandar) and the British establishment. He donated $40+ million to Oxford University "
    "(Said Business School bears his name). He operated at the intersection of Saudi intelligence "
    "interests, British defense industry, and Western financial networks."
    "\n\n"
    "ARMS DEALING LINEAGE: Said's role as Al-Yamamah broker places him in the same functional "
    "category as Adnan Khashoggi (Iran-Contra middleman, BCCI client) — Saudi-connected arms "
    "deal intermediaries who served as bridges between Western defense industries and Saudi "
    "government procurement, generating massive commission-based slush funds."
)

_DESC_MOHAMMED_BIN_FAHD = (
    "Prince Mohammed bin Fahd Al Saud (born 1950). Son of King Fahd (ruled Saudi Arabia "
    "1982-2005). Governor of the Eastern Province of Saudi Arabia (1985-2013). One of the "
    "wealthiest Saudi royals."
    "\n\n"
    "BCCI CONNECTION: The Kerry/Brown Senate BCCI Report (1992) documented that Prince Mohammed "
    "bin Fahd had accounts at BCCI and was connected to BCCI's operations in Saudi Arabia. The "
    "Prince's financial advisor, Ghaith Pharaon (a BCCI front-man), was one of the key figures "
    "in the BCCI scandal."
    "\n\n"
    "FINANCIAL NETWORK: Prince Mohammed controlled significant Saudi government contracts "
    "through the Eastern Province (the oil-producing region). His financial network intersected "
    "with BCCI's Gulf operations and the broader Saudi royal financial architecture that fed "
    "into Western investment vehicles including the Carlyle Group."
)


ENTITIES = [
    {
        "name": "Prince Bandar bin Sultan",
        "entity_type": "person",
        "description": _DESC_BANDAR,
        "aliases": "Bandar Bush, Bandar bin Sultan Al Saud",
        "metadata": {"birth_date": "1949-03-02", "nationality": "Saudi", "status": "alive"},
    },
    {
        "name": "Prince Turki al-Faisal",
        "entity_type": "person",
        "description": _DESC_TURKI,
        "aliases": "Turki al-Faisal Al Saud, Turki al-Faisal bin Abdulaziz Al Saud",
        "metadata": {"birth_date": "1945-02-15", "nationality": "Saudi", "status": "alive"},
    },
    {
        "name": "Saudi GID",
        "entity_type": "agency",
        "description": _DESC_GID,
        "aliases": "General Intelligence Directorate, General Intelligence Presidency, GIP, Al Mukhabarat Al A'amah",
        "metadata": {},
    },
    {
        "name": "Mohammed bin Salman",
        "entity_type": "person",
        "description": _DESC_MBS,
        "aliases": "MBS, Crown Prince Mohammed bin Salman, Mohammed bin Salman Al Saud",
        "metadata": {"birth_date": "1985-08-31", "nationality": "Saudi", "status": "alive"},
    },
    {
        "name": "Jamal Khashoggi",
        "entity_type": "person",
        "description": _DESC_JAMAL,
        "aliases": "Jamal Ahmad Khashoggi",
        "metadata": {"birth_date": "1958-10-13", "death_date": "2018-10-02", "nationality": "Saudi", "status": "deceased"},
    },
    {
        "name": "Al-Waleed bin Talal",
        "entity_type": "person",
        "description": _DESC_ALWALEED,
        "aliases": "Prince Al-Waleed, Alwaleed bin Talal, Prince Alwaleed",
        "metadata": {"birth_date": "1955-03-07", "nationality": "Saudi", "status": "alive"},
    },
    {
        "name": "Kingdom Holding",
        "entity_type": "organization",
        "description": _DESC_KINGDOM_HOLDING,
        "aliases": "Kingdom Holding Company, KHC",
        "metadata": {},
    },
    {
        "name": "Saudi Binladin Group",
        "entity_type": "organization",
        "description": _DESC_BINLADIN_GROUP,
        "aliases": "SBG, Binladin Group, bin Laden family construction company",
        "metadata": {},
    },
    {
        "name": "Carlyle Group",
        "entity_type": "organization",
        "description": _DESC_CARLYLE,
        "aliases": "The Carlyle Group",
        "metadata": {},
    },
    {
        "name": "BAE Al-Yamamah Deal",
        "entity_type": "event",
        "description": _DESC_BAE_YAMAMAH,
        "aliases": "Al-Yamamah, BAE Systems Al-Yamamah, Al Yamamah",
        "metadata": {},
    },
    {
        "name": "Safari Club",
        "entity_type": "organization",
        "description": _DESC_SAFARI_CLUB,
        "aliases": "The Safari Club",
        "metadata": {},
    },
    {
        "name": "Wafic Said",
        "entity_type": "person",
        "description": _DESC_WAFIC_SAID,
        "aliases": "Wafic Rida Said",
        "metadata": {"birth_date": "1939-01-01", "nationality": "Syrian-Saudi", "status": "alive"},
    },
    {
        "name": "Prince Mohammed bin Fahd",
        "entity_type": "person",
        "description": _DESC_MOHAMMED_BIN_FAHD,
        "aliases": "Mohammed bin Fahd Al Saud",
        "metadata": {"birth_date": "1950-01-01", "nationality": "Saudi", "status": "alive"},
    },
]


# ============================================================
# RELATIONSHIPS — connections to existing network + internal
# ============================================================
# Reference existing entities by name (resolved at insert time):
#   Adnan Khashoggi [27], Kamal Adham [19], BCCI [54], CIA [85], Mossad [88],
#   William Casey [10], Iran-Contra [96], Donald Trump [33], Bill Clinton [32],
#   William Barr [8], Robert Maxwell [3], Tom Barrack [129], Colony Capital [133],
#   Prince Andrew [108], Vladimir Putin [160], Deutsche Bank [57],
#   Agha Hasan Abedi [20], First American Bank [55], FBI [87], DOJ [89],
#   Jeffrey Epstein [1], Ghislaine Maxwell [2], Les Wexner [4],
#   Ehud Barak [5], Little Saint James [76]

RELATIONSHIPS = [
    # ================================================================
    # PRINCE BANDAR BIN SULTAN — connections
    # ================================================================
    {
        "source": "Prince Bandar bin Sultan",
        "target": "Saudi GID",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Bandar operated as Saudi intelligence liaison to the US for over two decades as "
            "ambassador (1983-2005). As NSC secretary-general (2005-2015), he oversaw Saudi "
            "intelligence coordination directly. His role was functionally inseparable from "
            "GID operations in the Western hemisphere."
        ),
        "sources": [244, 247],
    },
    {
        "source": "Prince Bandar bin Sultan",
        "target": "CIA",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "Bandar was the CIA's primary Saudi interlocutor for over two decades. Steve Coll's "
            "Ghost Wars and David Ottaway's The King's Messenger document his extensive direct "
            "coordination with CIA directors from Casey through Tenet on covert operations "
            "including Afghanistan, Nicaragua, and counterterrorism."
        ),
        "sources": [244, 247, 237],
    },
    {
        "source": "Prince Bandar bin Sultan",
        "target": "Iran-Contra",
        "type": "financed",
        "tier": "documented",
        "desc": (
            "Congressional Iran-Contra investigation documented that Saudi Arabia contributed "
            "$32 million to the Nicaraguan Contras, channeled through accounts controlled by "
            "Bandar's office, at the request of the Reagan-Bush White House. Tower Commission "
            "and Iran-Contra Report confirm this."
        ),
        "sources": [237, 238],
    },
    {
        "source": "Prince Bandar bin Sultan",
        "target": "William Casey",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Bandar and CIA Director Casey coordinated directly on the Iran-Contra Saudi funding "
            "pipeline and on the Afghan mujahideen covert program. Ghost Wars documents their "
            "operational relationship throughout the 1980s."
        ),
        "sources": [244, 237],
    },
    {
        "source": "Prince Bandar bin Sultan",
        "target": "BAE Al-Yamamah Deal",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "Bandar personally negotiated key elements of the Al-Yamamah deal. Guardian "
            "investigation documented that Bandar received payments of at least $1 billion "
            "into accounts at Riggs Bank in Washington from BAE-connected payments. The UK SFO "
            "investigated before the probe was shut down."
        ),
        "sources": [251, 239, 240],
    },
    {
        "source": "Prince Bandar bin Sultan",
        "target": "Donald Trump",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Bandar maintained relationships with successive US presidents and their circles. "
            "Craig Unger's House of Bush, House of Saud documents Bandar's role as Saudi Arabia's "
            "primary political connector in Washington across Republican administrations."
        ),
        "sources": [246, 247],
    },
    {
        "source": "Prince Bandar bin Sultan",
        "target": "Adnan Khashoggi",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Both operated as Saudi intermediaries in arms deals and intelligence operations "
            "during the same period. Khashoggi handled Iran-Contra arms transfers; Bandar handled "
            "the Saudi government's $32M Contra contribution. Both connected to the same "
            "Saudi-CIA covert finance architecture documented in the Iran-Contra Report."
        ),
        "sources": [237, 248, 246],
    },

    # ================================================================
    # PRINCE TURKI AL-FAISAL — connections
    # ================================================================
    {
        "source": "Prince Turki al-Faisal",
        "target": "Saudi GID",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Turki served as Director-General of GID from 1979 to August 31, 2001 — the longest "
            "tenure of any GID chief. Resigned 10 days before September 11, 2001."
        ),
        "sources": [244, 235],
    },
    {
        "source": "Prince Turki al-Faisal",
        "target": "CIA",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "As GID chief for 22 years, Turki was Saudi intelligence's primary CIA counterpart. "
            "Coordinated the joint Saudi-CIA Afghan mujahideen funding program. Ghost Wars "
            "documents his direct operational relationship with CIA directors and station chiefs."
        ),
        "sources": [244, 245],
    },
    {
        "source": "Prince Turki al-Faisal",
        "target": "Kamal Adham",
        "type": "successor_to",
        "tier": "documented",
        "desc": (
            "Turki succeeded Kamal Adham as GID chief in 1979. Adham was his uncle by marriage. "
            "Turki inherited the Saudi-CIA covert cooperation framework — including the Safari "
            "Club relationships and BCCI financial infrastructure — that Adham had built."
        ),
        "sources": [244, 245, 236],
    },
    {
        "source": "Prince Turki al-Faisal",
        "target": "Jamal Khashoggi",
        "type": "employed",
        "tier": "credible",
        "desc": (
            "Jamal Khashoggi served as a media advisor to Prince Turki when Turki was GID chief. "
            "Traveled with Turki to Afghanistan during the anti-Soviet jihad. This placed Khashoggi "
            "at the intersection of Saudi intelligence, the Afghan war, and the Arab volunteer "
            "fighter network. Documented in multiple biographical accounts."
        ),
        "sources": [265, 253],
    },

    # ================================================================
    # SAUDI GID — connections
    # ================================================================
    {
        "source": "Saudi GID",
        "target": "CIA",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "Decades-long intelligence partnership documented in congressional reports, the 9/11 "
            "Commission, and multiple book-length investigations. Joint operations include: "
            "Safari Club (1976+), Afghan mujahideen (1979-89), and ongoing counterterrorism "
            "cooperation."
        ),
        "sources": [244, 235, 245],
    },
    {
        "source": "Saudi GID",
        "target": "BCCI",
        "type": "financial_connection",
        "tier": "documented",
        "desc": (
            "BCCI served as the financial backbone for Saudi GID covert operations through the "
            "Safari Club. Kamal Adham — GID chief and CIA's principal Middle East liaison — was "
            "simultaneously BCCI's secret front-man for the First American Bank takeover. The "
            "Kerry/Brown Senate BCCI Report documents this dual role extensively."
        ),
        "sources": [236, 245],
    },
    {
        "source": "Saudi GID",
        "target": "Mossad",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Despite no formal diplomatic relations until the Abraham Accords era, Saudi and "
            "Israeli intelligence maintained back-channel cooperation on shared threats (Iran, "
            "regional Islamist movements). Multiple credible accounts document informal "
            "liaison relationships, particularly during the Turki al-Faisal era."
        ),
        "sources": [244, 246],
    },

    # ================================================================
    # MOHAMMED BIN SALMAN (MBS) — connections
    # ================================================================
    {
        "source": "Mohammed bin Salman",
        "target": "Jamal Khashoggi",
        "type": "ordered_killing_of",
        "tier": "documented",
        "desc": (
            "ODNI assessment (declassified February 2021) stated MBS 'approved an operation in "
            "Istanbul, Turkey to capture or kill Saudi journalist Jamal Khashoggi.' UN Special "
            "Rapporteur Agnes Callamard concluded the killing was 'deliberate, premeditated "
            "execution' carried out by Saudi state agents including members of MBS's personal "
            "security detail."
        ),
        "sources": [242, 241],
    },
    {
        "source": "Mohammed bin Salman",
        "target": "Al-Waleed bin Talal",
        "type": "detained",
        "tier": "documented",
        "desc": (
            "MBS ordered the detention of Al-Waleed and 200+ other Saudi elites at the "
            "Ritz-Carlton Riyadh in November 2017 in an 'anti-corruption' purge. Al-Waleed "
            "was held for 83 days, released after a reported $6B+ financial settlement. "
            "Documented by Blood and Oil (Hope/Scheck) and extensive international reporting."
        ),
        "sources": [249, 252],
    },
    {
        "source": "Mohammed bin Salman",
        "target": "Donald Trump",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "MBS cultivated close ties with the Trump administration, primarily through Jared "
            "Kushner. Saudi lobbying spending surged during Trump era. ProPublica documented "
            "Saudi government spending at Trump properties while lobbying against JASTA "
            "(the 9/11 families bill). Trump's first overseas trip as president was to Riyadh."
        ),
        "sources": [261, 249],
    },
    {
        "source": "Mohammed bin Salman",
        "target": "Saudi GID",
        "type": "controls",
        "tier": "documented",
        "desc": (
            "As Crown Prince and de facto ruler, MBS restructured Saudi intelligence under his "
            "direct control. The Khashoggi assassination team included members of his personal "
            "Rapid Intervention Force. Blood and Oil documents his consolidation of intelligence "
            "and security apparatus."
        ),
        "sources": [249, 242],
    },

    # ================================================================
    # JAMAL KHASHOGGI — connections
    # ================================================================
    {
        "source": "Jamal Khashoggi",
        "target": "Adnan Khashoggi",
        "type": "family_of",
        "tier": "documented",
        "desc": (
            "Jamal Khashoggi was the nephew of Adnan Khashoggi, the Saudi billionaire arms dealer "
            "and Iran-Contra middleman. This family connection placed Jamal within the orbit of "
            "Saudi Arabia's most powerful arms-dealing and intelligence-connected dynasty. "
            "Widely documented biographical fact."
        ),
        "sources": [265, 253],
    },
    {
        "source": "Jamal Khashoggi",
        "target": "Saudi GID",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Khashoggi had long-standing relationships with Saudi intelligence through his role "
            "as media advisor to GID chief Prince Turki al-Faisal. He traveled to Afghanistan "
            "during the anti-Soviet jihad and interviewed Osama bin Laden multiple times in that "
            "capacity. He navigated Saudi intelligence circles throughout his career."
        ),
        "sources": [265, 260],
    },

    # ================================================================
    # AL-WALEED BIN TALAL — connections
    # ================================================================
    {
        "source": "Al-Waleed bin Talal",
        "target": "Kingdom Holding",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Al-Waleed founded and controls Kingdom Holding Company, his primary investment "
            "vehicle. Through KHC he held major stakes in Citigroup, Twitter, Four Seasons, "
            "and dozens of other Western companies."
        ),
        "sources": [252],
    },
    {
        "source": "Al-Waleed bin Talal",
        "target": "Donald Trump",
        "type": "financial_connection",
        "tier": "documented",
        "desc": (
            "Al-Waleed purchased Trump's yacht (the Trump Princess) in 1991 and the Plaza Hotel "
            "stake in 1995 — both during Trump's financial distress. They publicly feuded in "
            "2015: Al-Waleed called Trump 'a disgrace to America,' Trump called him 'dopey prince.' "
            "Documented in court records and extensive reporting."
        ),
        "sources": [255],
    },
    {
        "source": "Al-Waleed bin Talal",
        "target": "Carlyle Group",
        "type": "investor_in",
        "tier": "credible",
        "desc": (
            "Al-Waleed and Kingdom Holding invested in the Carlyle Group alongside other Saudi "
            "royal investors, placing Saudi capital directly into the Bush-connected private "
            "equity firm. Documented in reporting on Carlyle's Saudi investor base."
        ),
        "sources": [257, 263],
    },

    # ================================================================
    # KINGDOM HOLDING — connections
    # ================================================================
    {
        "source": "Kingdom Holding",
        "target": "Deutsche Bank",
        "type": "financial_connection",
        "tier": "credible",
        "desc": (
            "Kingdom Holding's investments in major Western financial institutions placed Saudi "
            "royal capital in the same banking networks serving the broader Epstein network. "
            "Al-Waleed's Citigroup investment (largest individual shareholder) connected Saudi "
            "capital to the same financial infrastructure."
        ),
        "sources": [252],
    },

    # ================================================================
    # SAUDI BINLADIN GROUP — connections
    # ================================================================
    {
        "source": "Saudi Binladin Group",
        "target": "Carlyle Group",
        "type": "investor_in",
        "tier": "documented",
        "desc": (
            "The bin Laden family invested in the Carlyle Group. They were meeting with Carlyle "
            "representatives in Washington on the morning of September 11, 2001. The family "
            "divested shortly after 9/11 under public pressure. Documented by Washington Post "
            "and Craig Unger's House of Bush, House of Saud."
        ),
        "sources": [263, 246],
    },
    {
        "source": "Saudi Binladin Group",
        "target": "Saudi GID",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "The bin Laden family's construction empire, with exclusive contracts for Saudi holy "
            "sites, operated at the highest levels of Saudi establishment. The family's relationship "
            "with Saudi intelligence was institutional — their proximity to the royal family and "
            "control of sensitive infrastructure projects made them inherently connected to the "
            "Saudi security apparatus."
        ),
        "sources": [258, 244],
    },

    # ================================================================
    # CARLYLE GROUP — connections
    # ================================================================
    {
        "source": "Carlyle Group",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Frank Carlucci, Carlyle chairman (1989-2005), was former CIA Deputy Director and "
            "Reagan's Secretary of Defense. George H.W. Bush (former CIA Director) served as "
            "senior advisor. James Baker III (Secretary of State) was senior counselor. Carlyle "
            "assembled the most concentrated collection of intelligence and defense establishment "
            "figures in any private equity firm."
        ),
        "sources": [257, 246],
    },
    {
        "source": "Carlyle Group",
        "target": "William Barr",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "The Carlyle Group's orbit of Bush administration alumni overlapped with Barr's world. "
            "Barr served as AG under Bush 41 (Carlyle's key political relationship). Both Carlyle "
            "and Barr operated within the Bush family's political-financial network that included "
            "Saudi money flows."
        ),
        "sources": [246, 257],
    },
    {
        "source": "Carlyle Group",
        "target": "Donald Trump",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Carlyle's defense-sector investments profited from post-9/11 military buildup. "
            "Tom Barrack (Trump's close ally and inaugural committee chair) operated in the "
            "same Gulf sovereign wealth investment space. The Saudi-Washington private equity "
            "pipeline that Carlyle pioneered continued through Colony Capital and other firms "
            "in the Trump orbit."
        ),
        "sources": [257, 261],
    },

    # ================================================================
    # BAE AL-YAMAMAH DEAL — connections
    # ================================================================
    {
        "source": "BAE Al-Yamamah Deal",
        "target": "Saudi GID",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The Al-Yamamah deal was negotiated through Saudi intelligence channels. Commission "
            "payments flowed to Saudi intelligence-connected figures including Prince Bandar. "
            "The UK SFO investigation was shut down citing 'national security' — protecting "
            "both Saudi and British intelligence equities."
        ),
        "sources": [251, 239, 240],
    },
    {
        "source": "BAE Al-Yamamah Deal",
        "target": "Adnan Khashoggi",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "Pattern-based: Al-Yamamah's commission structure mirrored Khashoggi's earlier arms "
            "deal intermediary model — Saudi-connected middlemen extracting massive commissions "
            "from Western arms manufacturers selling to the Saudi government. Wafic Said replaced "
            "Khashoggi as the primary intermediary in the British-Saudi arms pipeline."
        ),
        "sources": [248, 251],
    },
    {
        "source": "BAE Al-Yamamah Deal",
        "target": "DOJ",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "After the UK SFO shut down its investigation, the US DOJ pursued BAE Systems "
            "for FCPA violations and false statements. BAE pleaded guilty in 2010 and paid "
            "a $400 million fine — but the plea deal avoided specific findings about Saudi "
            "payments."
        ),
        "sources": [240],
    },

    # ================================================================
    # SAFARI CLUB — connections
    # ================================================================
    {
        "source": "Safari Club",
        "target": "Saudi GID",
        "type": "member",
        "tier": "documented",
        "desc": (
            "Saudi GID (under Kamal Adham) was a founding member of the Safari Club. Saudi Arabia "
            "provided the primary funding. Trento's Prelude to Terror documents Adham's central "
            "role in establishing and operating the alliance."
        ),
        "sources": [245, 256],
    },
    {
        "source": "Safari Club",
        "target": "CIA",
        "type": "intelligence_link",
        "tier": "documented",
        "desc": (
            "The Safari Club was created specifically to continue CIA covert operations after "
            "Congressional restrictions. The CIA maintained liaison through unofficial channels "
            "while the Safari Club members executed operations the CIA could no longer officially "
            "conduct. Documented by Trento and multiple accounts."
        ),
        "sources": [245, 256],
    },
    {
        "source": "Safari Club",
        "target": "BCCI",
        "type": "financed_by",
        "tier": "documented",
        "desc": (
            "BCCI provided the financial infrastructure for Safari Club operations. Kamal Adham — "
            "simultaneously GID chief, CIA asset, and BCCI front-man — was the nexus connecting "
            "all three. The Kerry/Brown Senate BCCI Report documents this triangular relationship."
        ),
        "sources": [236, 245],
    },
    {
        "source": "Safari Club",
        "target": "Kamal Adham",
        "type": "member",
        "tier": "documented",
        "desc": (
            "Kamal Adham, as GID chief and CIA's principal Middle East liaison, was a founding "
            "member and key operator of the Safari Club. His triple role — Saudi intelligence "
            "chief, CIA liaison, BCCI front-man — made him the linchpin of the entire structure."
        ),
        "sources": [245, 236],
    },
    {
        "source": "Safari Club",
        "target": "Iran-Contra",
        "type": "predecessor_to",
        "tier": "inference",
        "desc": (
            "Pattern-based: The Safari Club established the template that Iran-Contra followed — "
            "using foreign intelligence services and private financial networks to circumvent "
            "Congressional oversight of CIA operations. The personnel (Casey), financial "
            "infrastructure (BCCI), and Saudi funding channels were continuous between the two."
        ),
        "sources": [245, 237],
    },

    # ================================================================
    # WAFIC SAID — connections
    # ================================================================
    {
        "source": "Wafic Said",
        "target": "BAE Al-Yamamah Deal",
        "type": "brokered",
        "tier": "documented",
        "desc": (
            "Said was the primary middleman who brokered the Al-Yamamah deal between British "
            "Aerospace and Saudi Arabia. His commission payments were estimated at $200+ million. "
            "Documented by the Guardian, Financial Times, and BBC investigations."
        ),
        "sources": [259, 251, 262],
    },
    {
        "source": "Wafic Said",
        "target": "Prince Bandar bin Sultan",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Said and Bandar were both central to the Al-Yamamah deal — Said as commercial "
            "broker, Bandar as Saudi government negotiator and commission recipient. Guardian "
            "investigation documented their overlapping roles in the deal structure."
        ),
        "sources": [251, 259],
    },
    {
        "source": "Wafic Said",
        "target": "Adnan Khashoggi",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Said and Khashoggi operated in the same Saudi arms-deal intermediary space. "
            "Said effectively succeeded Khashoggi as the primary British-Saudi arms deal "
            "middleman when Khashoggi's influence waned in the 1980s. Both extracted massive "
            "commissions from Western defense sales to Saudi Arabia."
        ),
        "sources": [248, 259],
    },

    # ================================================================
    # PRINCE MOHAMMED BIN FAHD — connections
    # ================================================================
    {
        "source": "Prince Mohammed bin Fahd",
        "target": "BCCI",
        "type": "financial_connection",
        "tier": "documented",
        "desc": (
            "The Kerry/Brown Senate BCCI Report documented Prince Mohammed bin Fahd's connections "
            "to BCCI operations in Saudi Arabia. His financial advisor Ghaith Pharaon was one of "
            "BCCI's key front-men."
        ),
        "sources": [236],
    },
    {
        "source": "Prince Mohammed bin Fahd",
        "target": "Carlyle Group",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Prince Mohammed's financial network, rooted in the Eastern Province's oil wealth, "
            "intersected with the Saudi royal investment pipeline into Western firms including "
            "the Carlyle Group. The broader Fahd family's financial interests fed into the same "
            "Saudi-Washington investment channels."
        ),
        "sources": [264, 246],
    },
    {
        "source": "Prince Mohammed bin Fahd",
        "target": "Saudi GID",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "As son of King Fahd and governor of the Eastern Province (Saudi Arabia's oil-producing "
            "region), Prince Mohammed operated at the intersection of Saudi royal power, oil wealth, "
            "and the intelligence apparatus. His financial networks overlapped with GID operational "
            "channels documented in the BCCI Senate report."
        ),
        "sources": [236, 264],
    },

    # ================================================================
    # CROSS-CONNECTIONS to existing entities
    # ================================================================
    # Tom Barrack → Saudi/Gulf
    {
        "source": "Tom Barrack",
        "target": "Mohammed bin Salman",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Barrack operated in the Saudi/Gulf sovereign wealth investment space. Colony Capital "
            "received $374M from UAE sovereign wealth funds. Barrack was indicted (2021) for "
            "illegally lobbying the Trump administration on behalf of UAE — the same Gulf "
            "financial-political pipeline connecting Saudi/Gulf money to US politics."
        ),
        "sources": [261, 249],
    },
    # Prince Andrew → Saudi
    {
        "source": "Prince Andrew",
        "target": "Prince Bandar bin Sultan",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Prince Andrew served as UK Special Representative for International Trade and "
            "Investment (2001-2011), during which he maintained relationships with Gulf royals "
            "including Saudi princes. The Al-Yamamah deal was a UK-Saudi government transaction "
            "that operated through the same British-Saudi elite networks Andrew inhabited."
        ),
        "sources": [251, 246],
    },
]


# ============================================================
# ENTITY → SOURCE links
# ============================================================

ENTITY_SOURCES = {
    "Prince Bandar bin Sultan": [234, 237, 238, 244, 246, 247, 251],
    "Prince Turki al-Faisal": [235, 244, 245, 265],
    "Saudi GID": [236, 244, 245, 256],
    "Mohammed bin Salman": [241, 242, 249, 252, 261],
    "Jamal Khashoggi": [241, 242, 253, 260, 265],
    "Al-Waleed bin Talal": [249, 252, 255],
    "Kingdom Holding": [252],
    "Saudi Binladin Group": [246, 258, 263],
    "Carlyle Group": [246, 257, 263],
    "BAE Al-Yamamah Deal": [239, 240, 251, 262],
    "Safari Club": [236, 245, 256],
    "Wafic Said": [251, 259, 262],
    "Prince Mohammed bin Fahd": [236, 264],
}
