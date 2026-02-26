"""
Bohemian Club / Bohemian Grove Cluster — Expansion layer for Intel Console.

Extracted from More Perfect Union investigation: "We Uncovered The Most Infamous
Secret Society: And The Truth Is Shocking" (Feb 2026), featuring leaked membership
lists from investigative reporter Daniel Boguslaw.

Maps the documented Bohemian Club–Heritage Foundation–Bechtel Corporation nexus:
elite policy planning at the Grove (Social Security cuts, capital gains cuts,
Project 2025), the Bechtel government-contractor revolving door, Heritage Foundation
dark money network, and bipartisan elite collusion across decades.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Jeffrey Epstein [1], Henry Kissinger [111], Donald Trump [33],
  Bill Clinton [32], Hillary Clinton [31], CIA [85], DOJ [89],
  FBI [87], NSA [86], DARPA [90], Mossad [88],
  William Barr [8], Iran-Contra [96], Prince Andrew [108],
  Tom Barrack [129]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 334+ (continuing from existing 333)
# ============================================================

SOURCES = [
    {
        "id": 334,
        "title": "More Perfect Union — 'We Uncovered The Most Infamous Secret Society: And The Truth Is Shocking' (Daniel Boguslaw investigation, leaked 2023 membership/attendance lists)",
        "url": "https://youtu.be/unSBLkk2FKc",
        "source_type": "journalism",
        "author": "More Perfect Union / Daniel Boguslaw",
        "year": 2026,
    },
    {
        "id": 335,
        "title": "Reagan Presidential Library — Edwin Harper memo to Alan Greenspan: 'the paper we discussed at the Bohemian Grove' re: Social Security Reform Proposals (1981)",
        "url": "https://www.reaganlibrary.gov/archives/digital-library",
        "source_type": "government",
        "author": "Edwin Harper",
        "year": 1981,
    },
    {
        "id": 336,
        "title": "G. William Domhoff — 'The Bohemian Grove and Other Retreats: A Study in Ruling-Class Cohesiveness' (Harper & Row, 1974)",
        "url": "https://whorulesamerica.ucsc.edu/power/bohemian_grove.html",
        "source_type": "book",
        "author": "G. William Domhoff",
        "year": 1974,
    },
    {
        "id": 337,
        "title": "Philip Weiss — 'Masters of the Universe Go to Camp: Inside the Bohemian Grove' (Spy Magazine, November 1989)",
        "url": "https://archive.org/details/spy-magazine-1989-11",
        "source_type": "journalism",
        "author": "Philip Weiss",
        "year": 1989,
    },
    {
        "id": 338,
        "title": "ProPublica — 'Clarence Thomas and the Billionaire: The Justice Failed to Disclose Harlan Crow's Generosity' (including Bohemian Grove trips)",
        "url": "https://www.propublica.org/article/clarence-thomas-scotus-undisclosed-luxury-travel-gifts-crow",
        "source_type": "journalism",
        "author": "Joshua Kaplan, Justin Elliott, Alex Mierjeski",
        "year": 2023,
    },
    {
        "id": 339,
        "title": "Heritage Foundation — Project 2025: Mandate for Leadership, The Conservative Promise",
        "url": "https://www.project2025.org/",
        "source_type": "book",
        "year": 2023,
    },
    {
        "id": 340,
        "title": "Peter Phillips — 'A Relative Advantage: Sociology of the San Francisco Bohemian Club' (PhD dissertation, UC Davis, 1994)",
        "url": "https://whorulesamerica.ucsc.edu/power/bohemian_grove.html",
        "source_type": "book",
        "author": "Peter Phillips",
        "year": 1994,
    },
    {
        "id": 341,
        "title": "Washington Post — 'Bechtel Wins Major Iraq Reconstruction Contract' (USAID $680M no-bid contract, 2003)",
        "url": "https://www.washingtonpost.com/archive/politics/2003/04/18/bechtel-wins-major-contract/",
        "source_type": "journalism",
        "year": 2003,
    },
    {
        "id": 342,
        "title": "FEC — David McCormick for Senate campaign finance records (2024 cycle, PA)",
        "url": "https://www.fec.gov/data/candidate/S4PA00286/",
        "source_type": "government",
        "year": 2024,
    },
    {
        "id": 343,
        "title": "OpenSecrets — Heritage Foundation organizational profile (funding, donors, Koch network connections)",
        "url": "https://www.opensecrets.org/orgs/heritage-foundation/summary?id=D000000540",
        "source_type": "journalism",
        "year": 2024,
    },
    {
        "id": 344,
        "title": "Nixon White House tapes — references to Bohemian Grove ('The most faggy goddamn thing you could ever imagine,' 1971 tape)",
        "url": "https://www.nixonlibrary.gov/white-house-tapes",
        "source_type": "government",
        "author": "Richard Nixon",
        "year": 1971,
    },
    {
        "id": 345,
        "title": "San Francisco Chronicle — 'Who Is Neighbors for a Better San Francisco? Inside the Dark Money Group Reshaping City Politics'",
        "url": "https://www.sfchronicle.com/sf/article/neighbors-better-san-francisco-16974580.php",
        "source_type": "journalism",
        "year": 2022,
    },
    {
        "id": 346,
        "title": "Senate Judiciary Committee — Supreme Court Ethics hearings (Thomas/Crow gift disclosures, undisclosed travel)",
        "url": "https://www.judiciary.senate.gov/supreme-court-ethics",
        "source_type": "congressional",
        "year": 2023,
    },
    {
        "id": 347,
        "title": "CorpWatch — 'Bechtel: Profiting from Destruction' (Iraq contracts, government revolving door documentation)",
        "url": "https://www.corpwatch.org/article/bechtel-profiting-destruction",
        "source_type": "journalism",
        "author": "Pratap Chatterjee",
        "year": 2004,
    },
    {
        "id": 348,
        "title": "Social Security Works — Alex Lawson confirmation: Social Security cuts planned at Bohemian Grove (email correspondence with More Perfect Union)",
        "url": "https://socialsecurityworks.org/",
        "source_type": "journalism",
        "author": "Alex Lawson",
        "year": 2026,
    },
]


# ============================================================
# ENTITIES — 24 new (19 people + 3 organizations + 2 events)
# ============================================================

ENTITIES = [
    # --- PEOPLE: Presidents ---
    {
        "name": "Ronald Reagan",
        "entity_type": "person",
        "description": "40th President of the United States (1981-89). Bohemian Club member — Social Security reform planned at the Grove per Reagan Library memo from Edwin Harper to Alan Greenspan. Implemented Heritage Foundation's first Mandate for Leadership. Capital gains tax cut persuaded at the Grove by investor Bill Draper. Beloved the Grove — sent letters about it from the White House.",
        "metadata": {},
    },
    {
        "name": "George H.W. Bush",
        "entity_type": "person",
        "description": "41st President (1989-93), former CIA Director (1976-77). Bohemian Club member. Appointed William Barr as Attorney General (1991). Father of George W. Bush. Key node connecting intelligence community to the Grove's political elite.",
        "metadata": {},
    },
    {
        "name": "George W. Bush",
        "entity_type": "person",
        "description": "43rd President (2001-09). Bohemian Club member. Drove Iraq invasion alongside fellow Club members Cheney, Rumsfeld, and Powell — Bechtel Corporation (led by fellow members) received hundreds of millions in reconstruction contracts.",
        "metadata": {},
    },
    # --- PEOPLE: Cabinet / Senior Government ---
    {
        "name": "Dick Cheney",
        "entity_type": "person",
        "description": "Vice President under George W. Bush (2001-09), Secretary of Defense under George H.W. Bush (1989-93). Bohemian Club member. Former CEO of Halliburton. Key architect of Iraq War alongside fellow Grove members.",
        "metadata": {},
    },
    {
        "name": "Donald Rumsfeld",
        "entity_type": "person",
        "description": "Secretary of Defense under George W. Bush (2001-06). Bohemian Club member. Co-architect of Iraq invasion with fellow Club members Bush, Cheney, and Powell.",
        "metadata": {},
    },
    {
        "name": "Colin Powell",
        "entity_type": "person",
        "description": "Secretary of State under George W. Bush (2001-05), Chairman of Joint Chiefs under George H.W. Bush (1989-93). Bohemian Club member — former Grove workers report he starred as the lead in the camp's production of Macbeth.",
        "metadata": {},
    },
    {
        "name": "Caspar Weinberger",
        "entity_type": "person",
        "description": "Secretary of Defense under Reagan (1981-87). Bohemian Club member. Former Vice President and General Counsel of Bechtel Corporation — the textbook case of the Bechtel-to-government revolving door. Indicted in Iran-Contra, pardoned by George H.W. Bush.",
        "metadata": {},
    },
    {
        "name": "George Shultz",
        "entity_type": "person",
        "description": "Secretary of State under Reagan (1982-89). Bohemian Club member. Former President of Bechtel Corporation — went from running America's largest private construction firm to running American foreign policy. Also served as Nixon's Treasury Secretary and Labor Secretary.",
        "metadata": {},
    },
    {
        "name": "Edwin Meese",
        "entity_type": "person",
        "description": "Attorney General under Reagan (1985-88). Bohemian Club member. Close Reagan advisor — part of the 'troika' with James Baker and Michael Deaver. Connected to Bechtel network through Grove membership.",
        "metadata": {},
    },
    {
        "name": "Alan Greenspan",
        "entity_type": "person",
        "description": "Chairman of the Federal Reserve (1987-2006), appointed by Reagan. Received the Social Security Reform Proposals memo from Edwin Harper referencing 'the paper we discussed at the Bohemian Grove' (1981 Reagan Library document). Chaired the Greenspan Commission that recommended the cuts Reagan signed into law in 1983.",
        "metadata": {},
    },
    # --- PEOPLE: Heritage / Dark Money ---
    {
        "name": "Edwin Fuelner",
        "entity_type": "person",
        "description": "Co-founder and longtime president of the Heritage Foundation. On the 2023 Bohemian Grove attendance list (age 82). Launched Project 2025 / Mandate for Leadership 7 at a Heritage event, explicitly referencing 'the first time it all happened' under Reagan. Heritage board member until his death in late 2025.",
        "metadata": {},
    },
    {
        "name": "Joseph Coors Sr",
        "entity_type": "person",
        "description": "Co-founder of the Heritage Foundation (1973) with Edwin Fuelner. Coors Brewing Company family — son of Adolph Coors, father of Pete Coors. Bohemian Club member. Used beer fortune to build the conservative policy infrastructure that produced Project 2025.",
        "metadata": {},
    },
    {
        "name": "Charles Koch",
        "entity_type": "person",
        "description": "CEO of Koch Industries, synonymous with anti-worker political spending and dark money networks. Bohemian Club member/attendee. Funder of Heritage Foundation and vast network of pro-corporate advocacy organizations.",
        "metadata": {},
    },
    # --- PEOPLE: Judicial ---
    {
        "name": "Harlan Crow",
        "entity_type": "person",
        "description": "Dallas real estate billionaire. Bohemian Club member (on 2023 list). Took Supreme Court Justice Clarence Thomas on undisclosed luxury trips including to Bohemian Grove — exposed by ProPublica in 2023. Connected to Club for Growth. Nephew of Paul Pelosi works for Crow.",
        "metadata": {},
    },
    {
        "name": "Clarence Thomas",
        "entity_type": "person",
        "description": "Supreme Court Justice (1991-present), appointed by George H.W. Bush. Attended Bohemian Grove as guest of Harlan Crow — among undisclosed luxury gifts exposed by ProPublica. Failed to disclose trips per judicial ethics requirements.",
        "metadata": {},
    },
    # --- PEOPLE: Current Power ---
    {
        "name": "David McCormick",
        "entity_type": "person",
        "description": "Hedge fund billionaire (Bridgewater Associates CEO), elected U.S. Senator from Pennsylvania (2024). On the 2023 Bohemian Grove attendance list — Mandalay camp alongside Michael Bloomberg and Henry Kissinger. 11 men from Mandalay camp donated to his Senate campaign. Appeared with Trump and Brendan Bechtel at PA AI data center announcement.",
        "metadata": {},
    },
    {
        "name": "Steven Bechtel Sr",
        "entity_type": "person",
        "description": "Patriarch of the Bechtel family and longtime head of Bechtel Corporation. Bohemian Club member — photographed at the Grove with Henry Kissinger, sent personal correspondence to him. Built the family dynasty that has profited from government contracts across multiple administrations.",
        "metadata": {},
    },
    {
        "name": "Brendan Bechtel",
        "entity_type": "person",
        "description": "Current CEO of Bechtel Corporation, latest heir to the Bechtel fortune. On 2023 Bohemian Grove attendance list. Appeared with Trump and David McCormick for PA AI data center deal. Bechtel positioned for billions in Trump-era construction: foreign deals brokered by Trump, Venezuelan pipeline interests, floated as beneficiary of Kushner/Trump Gaza rebuild plan.",
        "metadata": {},
    },
    {
        "name": "Michael Bloomberg",
        "entity_type": "person",
        "description": "Billionaire media mogul, former Mayor of New York City (2002-13), 2020 presidential candidate. On 2023 Bohemian Grove attendance list — Mandalay camp alongside David McCormick and Henry Kissinger (Kissinger's final Grove).",
        "metadata": {},
    },
    # --- ORGANIZATIONS ---
    {
        "name": "Bohemian Club",
        "entity_type": "organization",
        "description": "Invite-only, men-only social club in San Francisco, founded 1872. Hosts annual summer encampments at Bohemian Grove — 2,700-acre campground in Monte Rio, CA. Members include presidents, CEOs, bankers, Supreme Court justices, CIA directors. Leaked 2023 membership/attendance lists obtained by Daniel Boguslaw reveal ongoing elite policy coordination despite motto 'Weaving spiders come not here.' Social Security cuts, capital gains cuts, Project 2025 all traced to Grove discussions.",
        "metadata": {},
    },
    {
        "name": "Heritage Foundation",
        "entity_type": "organization",
        "description": "Conservative think tank co-founded in 1973 by Joseph Coors Sr and Edwin Fuelner. Produced 'Mandate for Leadership' policy books for Reagan (1981) and Trump (Project 2025, 2023). Immensely powerful during Reagan administration — policies still affecting Americans today. Funded by Koch network. Heritage board was ~25% Bohemian Club members when Project 2025 was written.",
        "metadata": {},
    },
    {
        "name": "Bechtel Corporation",
        "entity_type": "organization",
        "description": "One of the largest private corporations in the world — massive government construction contracts. Bechtel family has been involved in Bohemian Club for generations. Textbook revolving door: executives Caspar Weinberger (VP/GC → SecDef) and George Shultz (President → SecState) moved directly into Reagan cabinet. Won hundreds of millions in Iraq reconstruction contracts from Bush admin. Currently positioned for billions in Trump-era deals.",
        "metadata": {},
    },
    # --- EVENTS ---
    {
        "name": "Project 2025",
        "entity_type": "event",
        "description": "Heritage Foundation's 'Mandate for Leadership 7: The Conservative Promise' — a 900-page policy blueprint for the Trump administration, published 2023. Edwin Fuelner launched it at Heritage, explicitly connecting it to the original 1981 Mandate that shaped the Reagan administration. Heritage board ~25% Bohemian Club members during its drafting. Fuelner attended the 2023 Bohemian Grove encampment the same summer.",
        "metadata": {},
    },
    {
        "name": "Social Security Reform 1983",
        "entity_type": "event",
        "description": "Reagan Library documents reveal Social Security reform was planned at Bohemian Grove: Edwin Harper memo to Alan Greenspan references 'the paper we discussed at the Bohemian Grove' (1981). The Greenspan Commission recommended cuts that Reagan signed into law in 1983. These cuts are still affecting Americans today — confirmed by Alex Lawson of Social Security Works.",
        "metadata": {},
    },
]


# ============================================================
# RELATIONSHIPS — ~55 new connections
# ============================================================

RELATIONSHIPS = [
    # =========================================
    # GROUP 1: BOHEMIAN CLUB MEMBERSHIPS (21)
    # =========================================
    {
        "source": "Ronald Reagan",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "Bohemian Club member. Reagan Library contains letters about the Grove and a memo referencing Social Security reform 'discussed at the Bohemian Grove.'",
        "sources": [334, 335, 336, 344],
    },
    {
        "source": "George H.W. Bush",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "Bohemian Club member. Multiple presidential library references.",
        "sources": [334, 336, 337],
    },
    {
        "source": "George W. Bush",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "Bohemian Club member. Drove Iraq invasion alongside fellow members Cheney, Rumsfeld, and Powell.",
        "sources": [334, 337],
    },
    {
        "source": "Dick Cheney",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "Bohemian Club member. Multiple journalistic reports place him at the Grove.",
        "sources": [334, 337],
    },
    {
        "source": "Donald Rumsfeld",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "Bohemian Club member.",
        "sources": [334, 337],
    },
    {
        "source": "Colin Powell",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "Bohemian Club member. Former Grove workers report he starred as the lead in the camp production of Macbeth.",
        "sources": [334],
    },
    {
        "source": "Henry Kissinger",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "Longtime Bohemian Club member. Photographed at Grove with Steven Bechtel Sr. On 2023 Mandalay camp list — his final Grove before death in November 2023.",
        "sources": [334, 335, 336, 337],
    },
    {
        "source": "Alan Greenspan",
        "target": "Bohemian Club",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Reagan Library memo from Edwin Harper to Greenspan: 'You asked for the paper we discussed at the Bohemian Grove' — Social Security Reform Proposals (1981).",
        "sources": [334, 335],
    },
    {
        "source": "Caspar Weinberger",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "Bohemian Club member. Documented by Domhoff (1974) and Phillips (1994).",
        "sources": [336, 340],
    },
    {
        "source": "George Shultz",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "Bohemian Club member. Documented by Domhoff (1974) and Phillips (1994).",
        "sources": [336, 340],
    },
    {
        "source": "Edwin Meese",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "Bohemian Club member. Part of Reagan's inner circle ('troika' with Baker and Deaver).",
        "sources": [336, 340],
    },
    {
        "source": "Edwin Fuelner",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "On the 2023 Bohemian Grove attendance list obtained by Daniel Boguslaw. Would have been 82 years old.",
        "sources": [334],
    },
    {
        "source": "Joseph Coors Sr",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "Bohemian Club member. Coors beer empire family — generational membership (son Pete Coors also connected).",
        "sources": [336, 340],
    },
    {
        "source": "Charles Koch",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "Attends Bohemian Grove. 'Synonymous with anti-worker political spending' — More Perfect Union.",
        "sources": [334],
    },
    {
        "source": "Harlan Crow",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "On the 2023 Bohemian Grove attendance list. Took Supreme Court Justice Clarence Thomas to the Grove.",
        "sources": [334, 338],
    },
    {
        "source": "Clarence Thomas",
        "target": "Bohemian Club",
        "type": "attended_as_guest",
        "tier": "documented",
        "desc": "Attended Bohemian Grove as guest of Harlan Crow. Among undisclosed luxury gifts exposed by ProPublica (2023). Confirmed in Senate Judiciary Committee ethics hearings.",
        "sources": [338, 346],
    },
    {
        "source": "David McCormick",
        "target": "Bohemian Club",
        "type": "attended",
        "tier": "credible",
        "desc": "On the 2023 Bohemian Grove attendance list — Mandalay camp. 11 men from Mandalay camp donated to his Senate campaign.",
        "sources": [334, 342],
    },
    {
        "source": "Steven Bechtel Sr",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "Longtime Bohemian Club member. Photographed at camp with Henry Kissinger, sent personal correspondence.",
        "sources": [334, 335, 336],
    },
    {
        "source": "Brendan Bechtel",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "Latest Bechtel heir. On 2023 Bohemian Grove attendance list — generational family membership.",
        "sources": [334],
    },
    {
        "source": "Michael Bloomberg",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "credible",
        "desc": "On 2023 Bohemian Grove attendance list — Mandalay camp alongside David McCormick and Henry Kissinger.",
        "sources": [334],
    },
    {
        "source": "Donald Trump",
        "target": "Bohemian Club",
        "type": "rejected_by",
        "tier": "credible",
        "desc": "'Trump is not welcome at the Grove. He tried to join. He's not a member.' — Mary Moore, longtime Grove researcher. Despite rejection, Trump agenda tied to Club through Heritage Foundation and Project 2025.",
        "sources": [334],
    },

    # =========================================
    # GROUP 2: HERITAGE FOUNDATION (6)
    # =========================================
    {
        "source": "Joseph Coors Sr",
        "target": "Heritage Foundation",
        "type": "co_founded",
        "tier": "documented",
        "desc": "Co-founded the Heritage Foundation in 1973 with Edwin Fuelner and Paul Weyrich. Used Coors beer fortune to build conservative policy infrastructure.",
        "sources": [343],
    },
    {
        "source": "Edwin Fuelner",
        "target": "Heritage Foundation",
        "type": "co_founded",
        "tier": "documented",
        "desc": "Co-founded Heritage Foundation. Longtime president. Remained on the board until his death in late 2025. Launched Project 2025 at Heritage event.",
        "sources": [334, 343],
    },
    {
        "source": "Charles Koch",
        "target": "Heritage Foundation",
        "type": "funded",
        "tier": "documented",
        "desc": "Major funder of Heritage Foundation through Koch network. Part of the vast dark money lobbying network connected to the Bohemian Club.",
        "sources": [343],
    },
    {
        "source": "Heritage Foundation",
        "target": "Project 2025",
        "type": "published",
        "tier": "documented",
        "desc": "Heritage Foundation published Project 2025 / Mandate for Leadership 7 — a 900-page policy blueprint for the Trump administration. Heritage board ~25% Bohemian Club members during its drafting.",
        "sources": [334, 339],
    },
    {
        "source": "Ronald Reagan",
        "target": "Heritage Foundation",
        "type": "implemented_policy_of",
        "tier": "documented",
        "desc": "Reagan implemented Heritage Foundation's first Mandate for Leadership (1981). Edwin Fuelner explicitly referenced this when launching Project 2025: 'the first time it all happened.'",
        "sources": [334, 339, 343],
    },
    {
        "source": "Heritage Foundation",
        "target": "Donald Trump",
        "type": "policy_influence",
        "tier": "documented",
        "desc": "Project 2025 shaped Trump administration policy. Despite Trump not being a Grove member, Heritage (co-founded by Club members, board ~25% Club members) successfully embedded its policy agenda in his administration.",
        "sources": [334, 339],
    },

    # =========================================
    # GROUP 3: BECHTEL CORPORATION (4)
    # =========================================
    {
        "source": "Steven Bechtel Sr",
        "target": "Bechtel Corporation",
        "type": "led",
        "tier": "documented",
        "desc": "Patriarch and longtime head of Bechtel Corporation. Built the family dynasty into one of the largest private companies in the world.",
        "sources": [336, 341, 347],
    },
    {
        "source": "Brendan Bechtel",
        "target": "Bechtel Corporation",
        "type": "leads",
        "tier": "documented",
        "desc": "Current CEO and latest family heir. Poised for billions in Trump-era government construction contracts.",
        "sources": [334, 347],
    },
    {
        "source": "Caspar Weinberger",
        "target": "Bechtel Corporation",
        "type": "executive_at",
        "tier": "documented",
        "desc": "Vice President and General Counsel of Bechtel before becoming Reagan's Secretary of Defense. Textbook revolving door — from the construction firm to the Pentagon.",
        "sources": [336, 341, 347],
    },
    {
        "source": "George Shultz",
        "target": "Bechtel Corporation",
        "type": "executive_at",
        "tier": "documented",
        "desc": "President of Bechtel Corporation before becoming Reagan's Secretary of State. Went from running America's largest private construction firm to running American foreign policy.",
        "sources": [336, 341, 347],
    },

    # =========================================
    # GROUP 4: GOVERNMENT SERVICE (11)
    # =========================================
    {
        "source": "Caspar Weinberger",
        "target": "Ronald Reagan",
        "type": "served_under",
        "tier": "documented",
        "desc": "Secretary of Defense (1981-87). Bechtel VP → Pentagon. Indicted in Iran-Contra, pardoned by George H.W. Bush.",
        "sources": [336, 347],
    },
    {
        "source": "George Shultz",
        "target": "Ronald Reagan",
        "type": "served_under",
        "tier": "documented",
        "desc": "Secretary of State (1982-89). Bechtel President → State Department.",
        "sources": [336, 347],
    },
    {
        "source": "Edwin Meese",
        "target": "Ronald Reagan",
        "type": "served_under",
        "tier": "documented",
        "desc": "Attorney General (1985-88). Part of Reagan's inner circle 'troika.'",
        "sources": [336],
    },
    {
        "source": "Edwin Meese",
        "target": "DOJ",
        "type": "led",
        "tier": "documented",
        "desc": "Attorney General (1985-88). Bohemian Club member who led the Department of Justice.",
        "sources": [336],
    },
    {
        "source": "Alan Greenspan",
        "target": "Ronald Reagan",
        "type": "appointed_by",
        "tier": "documented",
        "desc": "Appointed Federal Reserve Chairman by Reagan in 1987. Previously received the Bohemian Grove Social Security Reform memo.",
        "sources": [335],
    },
    {
        "source": "Dick Cheney",
        "target": "George W. Bush",
        "type": "served_under",
        "tier": "documented",
        "desc": "Vice President (2001-09). Both Bohemian Club members. Co-architects of Iraq War.",
        "sources": [334],
    },
    {
        "source": "Donald Rumsfeld",
        "target": "George W. Bush",
        "type": "served_under",
        "tier": "documented",
        "desc": "Secretary of Defense (2001-06). Both Bohemian Club members. Co-architects of Iraq War.",
        "sources": [334],
    },
    {
        "source": "Colin Powell",
        "target": "George W. Bush",
        "type": "served_under",
        "tier": "documented",
        "desc": "Secretary of State (2001-05). Both Bohemian Club members. Previously Chairman of Joint Chiefs under George H.W. Bush.",
        "sources": [334],
    },
    {
        "source": "George H.W. Bush",
        "target": "CIA",
        "type": "directed",
        "tier": "documented",
        "desc": "Director of Central Intelligence (1976-77). CIA directors are among those 'already disclosed' as Grove attendees.",
        "sources": [334, 336],
    },
    {
        "source": "George H.W. Bush",
        "target": "William Barr",
        "type": "appointed",
        "tier": "documented",
        "desc": "Appointed William Barr as Attorney General (1991-93). Barr later returned as AG under Trump (2019-20).",
        "sources": [336],
    },
    {
        "source": "Caspar Weinberger",
        "target": "Iran-Contra",
        "type": "indicted_in",
        "tier": "documented",
        "desc": "Indicted on felony charges in Iran-Contra. Pardoned by George H.W. Bush on Christmas Eve 1992, before trial.",
        "sources": [336],
    },

    # =========================================
    # GROUP 5: CROSS-CONNECTIONS (9)
    # =========================================
    {
        "source": "Harlan Crow",
        "target": "Clarence Thomas",
        "type": "financial_gifts",
        "tier": "documented",
        "desc": "ProPublica exposed Crow's pattern of undisclosed luxury gifts to Thomas including private jet trips, yacht vacations, and trips to Bohemian Grove. Senate Judiciary Committee held ethics hearings.",
        "sources": [338, 346],
    },
    {
        "source": "Steven Bechtel Sr",
        "target": "Henry Kissinger",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Photographed together at Bohemian Grove. Personal correspondence between them (Bechtel sent Kissinger a memo — documented in presidential records).",
        "sources": [334, 335],
    },
    {
        "source": "Brendan Bechtel",
        "target": "Donald Trump",
        "type": "government_contracts",
        "tier": "credible",
        "desc": "Bechtel poised for billions in Trump-era construction: appeared together at PA AI data center announcement, foreign deals brokered by Trump admin, Venezuelan pipeline interests, floated as beneficiary of Kushner/Trump Gaza rebuild plan.",
        "sources": [334],
    },
    {
        "source": "David McCormick",
        "target": "Donald Trump",
        "type": "political_alliance",
        "tier": "documented",
        "desc": "Elected to Senate 2024. Part of Trump announcement for AI investment in PA data centers alongside Brendan Bechtel. 11 Mandalay camp members donated to his campaign.",
        "sources": [334, 342],
    },
    {
        "source": "David McCormick",
        "target": "Henry Kissinger",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Both in Mandalay camp at 2023 Bohemian Grove encampment (Kissinger's final Grove).",
        "sources": [334],
    },
    {
        "source": "David McCormick",
        "target": "Michael Bloomberg",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Both in Mandalay camp at 2023 Bohemian Grove encampment. Demonstrates bipartisan nature of Grove networks.",
        "sources": [334],
    },
    {
        "source": "Bechtel Corporation",
        "target": "CIA",
        "type": "government_contracts",
        "tier": "credible",
        "desc": "Bechtel has long-standing government construction relationships including with intelligence agencies. Multiple Bechtel executives moved between the company and senior government/defense positions.",
        "sources": [347],
    },
    {
        "source": "Bohemian Club",
        "target": "Bill Clinton",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Paul Pelosi (Nancy Pelosi's husband) is on the Grove membership list, as are 'several major centrist and Democratic Party donors' — demonstrating bipartisan elite membership beyond just Republicans.",
        "sources": [334],
    },
    {
        "source": "Brendan Bechtel",
        "target": "David McCormick",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Both appeared at Trump PA AI data center announcement. McCormick's Senate seat + Bechtel's construction capacity = documented convergence of Grove network power in current policy.",
        "sources": [334],
    },

    # =========================================
    # GROUP 6: POLICY PLANNED AT GROVE (4)
    # =========================================
    {
        "source": "Bohemian Club",
        "target": "Social Security Reform 1983",
        "type": "policy_planned_at",
        "tier": "documented",
        "desc": "Reagan Library memo from Edwin Harper to Alan Greenspan: 'You asked for the paper we discussed at the Bohemian Grove' — Social Security Reform Proposals (1981). Confirmed by Alex Lawson of Social Security Works: 'Your thesis is completely correct.'",
        "sources": [334, 335, 348],
    },
    {
        "source": "Ronald Reagan",
        "target": "Social Security Reform 1983",
        "type": "signed_into_law",
        "tier": "documented",
        "desc": "Reagan signed the Social Security Amendments of 1983 into law. Cuts planned at Bohemian Grove are 'still affecting us today.'",
        "sources": [334, 335],
    },
    {
        "source": "Alan Greenspan",
        "target": "Social Security Reform 1983",
        "type": "implemented",
        "tier": "documented",
        "desc": "Chaired the National Commission on Social Security Reform (Greenspan Commission) that recommended the cuts. Received the Grove discussion paper from Edwin Harper.",
        "sources": [335, 348],
    },
    {
        "source": "Bohemian Club",
        "target": "Project 2025",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Heritage Foundation board was ~25% Bohemian Club members when Project 2025 was being written. Edwin Fuelner attended the 2023 Grove encampment the same summer he launched Project 2025 at Heritage.",
        "sources": [334, 339],
    },
]


# ============================================================
# ENTITY-SOURCE LINKS — which sources document each entity
# ============================================================

ENTITY_SOURCES = {
    "Bohemian Club": [334, 336, 337, 340, 344],
    "Heritage Foundation": [334, 339, 343],
    "Bechtel Corporation": [334, 336, 341, 347],
    "Project 2025": [334, 339],
    "Social Security Reform 1983": [334, 335, 348],
    "Ronald Reagan": [334, 335, 336, 344],
    "George H.W. Bush": [334, 336, 337],
    "George W. Bush": [334, 337, 341],
    "Dick Cheney": [334, 337],
    "Donald Rumsfeld": [334, 337],
    "Colin Powell": [334],
    "Caspar Weinberger": [336, 340, 347],
    "George Shultz": [336, 340, 347],
    "Edwin Meese": [336, 340],
    "Alan Greenspan": [334, 335],
    "Edwin Fuelner": [334, 339, 343],
    "Joseph Coors Sr": [336, 340, 343],
    "Charles Koch": [334, 343],
    "Harlan Crow": [334, 338, 346],
    "Clarence Thomas": [338, 346],
    "David McCormick": [334, 342],
    "Steven Bechtel Sr": [334, 335, 336],
    "Brendan Bechtel": [334],
    "Michael Bloomberg": [334],
}
