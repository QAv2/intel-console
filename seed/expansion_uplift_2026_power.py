"""
Power Architecture — August 2026 uplift expansion for Intel Console.

Fills the biggest structural gap in the console: the Russia-Ukraine War
(2022-present), its key principals and diplomatic events, and the Trump
second-administration power map (2025-2026). Also updates WEF succession,
Peter Mandelson's arrest, Bilderberg 2026, NATO summits, and the political
layer of the Iran conflict (connecting existing Operation Epic Fury /
Operation Midnight Hammer to political principals).

NEW ENTITIES (12):
  Russia-Ukraine War, Volodymyr Zelensky, Budapest Memorandum (1994),
  Anchorage Summit (2025), JD Vance, Marco Rubio, Pete Hegseth,
  Pam Bondi, Elon Musk, DOGE, Steve Witkoff, Howard Lutnick

ENTITY UPDATES (12):
  Donald Trump, Vladimir Putin, World Economic Forum, Klaus Schwab,
  Alois Zwinggi, Peter Mandelson, Ali Khamenei, Masoud Pezeshkian,
  Bilderberg Group, Davos Annual Meeting, NATO, Operation Epic Fury

EXISTING ENTITIES referenced by name (NOT duplicated):
  Donald Trump, Vladimir Putin, Henry Kissinger, NATO, FSB, DOJ,
  Peter Thiel, Operation Epic Fury, Operation Midnight Hammer,
  Metropolitan Police, World Economic Forum, Klaus Schwab,
  Alois Zwinggi, Peter Mandelson, Ali Khamenei, Masoud Pezeshkian,
  Bilderberg Group, Davos Annual Meeting, Borge Brende,
  Jeffrey Epstein

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1600-1699
# ============================================================

SOURCES = [
    # --- Russia-Ukraine War ---
    {
        "id": 1600,
        "title": "Russian invasion of Ukraine — Wikipedia (overview, timeline, casualties)",
        "url": "https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1601,
        "title": "Russia-Ukraine War Report Card, August 5, 2026 — Russia Matters (Harvard Belfer Center)",
        "url": "https://www.russiamatters.org/news/russia-ukraine-war-report-card/russia-ukraine-war-report-card-aug-5-2026",
        "source_type": "journalism",
        "author": "Russia Matters",
        "year": 2026,
    },
    {
        "id": 1602,
        "title": "Russia 'ready for new ideas' on Ukraine war that match Putin's goals — Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/8/21/russia-ready-for-new-ideas-on-ukraine-war-that-match-putins-goals",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    # --- Budapest Memorandum ---
    {
        "id": 1603,
        "title": "Budapest Memorandum on Security Assurances — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Budapest_Memorandum_on_Security_Assurances",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1604,
        "title": "The Budapest Memorandum (1994): After 30 Years of Non-Compliance — National Security Archive",
        "url": "https://nsarchive.gwu.edu/briefing-book/nato-75-russia-programs/2024-12-05/budapest-memorandum-1994-after-30-years-non",
        "source_type": "archive",
        "year": 2024,
    },
    # --- Anchorage Summit ---
    {
        "id": 1605,
        "title": "Trump-Putin meeting: Live updates from Alaska summit — CNN Politics",
        "url": "https://www.cnn.com/politics/live-news/trump-putin-meeting-news-08-15-25",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2025,
    },
    {
        "id": 1606,
        "title": "Trump-Putin meeting Alaska, Ukraine: Live updates — CBS News",
        "url": "https://www.cbsnews.com/live-updates/trump-putin-meeting-alaska-ukraine/",
        "source_type": "journalism",
        "author": "CBS News",
        "year": 2025,
    },
    {
        "id": 1607,
        "title": "No deal at Trump-Putin meeting: Key takeaways from Alaska summit — Al Jazeera",
        "url": "https://www.aljazeera.com/news/2025/8/16/no-deal-at-trump-putin-meeting-key-takeaways-from-alaska-summit",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2025,
    },
    # --- Zelensky / Peace talks ---
    {
        "id": 1608,
        "title": "Ukraine's Zelenskyy proposes peace talks in open letter to Putin — Bloomberg",
        "url": "https://www.bloomberg.com/news/articles/2026-06-04/ukraine-s-zelenskyy-proposes-peace-talks-in-open-letter-to-putin",
        "source_type": "journalism",
        "author": "Bloomberg",
        "year": 2026,
    },
    {
        "id": 1609,
        "title": "Zelensky says his open letter to Putin achieved its goal — Meduza",
        "url": "https://meduza.io/en/news/2026/06/09/zelensky-says-his-open-letter-to-putin-achieved-its-goal-revealing-to-ukraine-s-allies-that-moscow-rejects-peace",
        "source_type": "journalism",
        "author": "Meduza",
        "year": 2026,
    },
    {
        "id": 1610,
        "title": "2026 Russo-Ukrainian truce — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/2026_Russo-Ukrainian_truce",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1611,
        "title": "Volodymyr Zelensky — Encyclopaedia Britannica",
        "url": "https://www.britannica.com/biography/Volodymyr-Zelensky",
        "source_type": "other",
        "year": 2026,
    },
    # --- Witkoff ---
    {
        "id": 1612,
        "title": "US envoy Steve Witkoff calls Russia-Ukraine talks 'productive and constructive' — NBC News",
        "url": "https://www.nbcnews.com/politics/politics-news/us-envoy-steve-witkoff-calls-russia-ukraine-talks-productive-rcna250409",
        "source_type": "journalism",
        "author": "NBC News",
        "year": 2026,
    },
    {
        "id": 1613,
        "title": "Witkoff coached a Putin aide on how Russian leader should pitch Trump on Ukraine peace plan — PBS NewsHour",
        "url": "https://www.pbs.org/newshour/amp/world/steve-witkoff-coached-a-putin-aide-on-how-russian-leader-should-pitch-trump-on-ukraine-peace-plan-report-reveals",
        "source_type": "journalism",
        "author": "PBS NewsHour",
        "year": 2025,
    },
    # --- NATO summits ---
    {
        "id": 1614,
        "title": "The Hague Summit Declaration, June 2025 — NATO Official",
        "url": "https://www.nato.int/cps/en/natohq/235800.htm",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 1615,
        "title": "2026 NATO Summit in Ankara — NATO Official",
        "url": "https://www.nato.int/en/news-and-events/events/2026/07/overview---2026-nato-summit-in-ankara-",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 1616,
        "title": "Six Takeaways from the 2026 NATO Summit — Breaking Defense",
        "url": "https://breakingdefense.com/2026/07/six-take-aways-from-the-2026-nato-summit/",
        "source_type": "journalism",
        "author": "Breaking Defense",
        "year": 2026,
    },
    # --- Hegseth / DoW rename ---
    {
        "id": 1617,
        "title": "Trump Signs Order Rebranding DOD as 'Department of War' — Time",
        "url": "https://time.com/7314840/department-of-defense-name-change-department-of-war-pete-hegseth-trump/",
        "source_type": "journalism",
        "author": "Time",
        "year": 2025,
    },
    {
        "id": 1618,
        "title": "Executive Order Calls for the Return of the Department of War — ClearanceJobs",
        "url": "https://news.clearancejobs.com/2025/09/05/executive-order-calls-for-the-return-of-the-department-of-war-what-changes-in-a-dod-rebrand/",
        "source_type": "journalism",
        "author": "ClearanceJobs",
        "year": 2025,
    },
    # --- Rubio / Iran political layer ---
    {
        "id": 1619,
        "title": "Secretary of State Marco Rubio faces questions about Iran war on Capitol Hill — NPR",
        "url": "https://www.npr.org/2026/06/03/nx-s1-5844344/secretary-of-state-marco-rubio-faces-questions-about-iran-war-on-capitol-hill",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2026,
    },
    # --- Iran strikes June 2025 ---
    {
        "id": 1620,
        "title": "2025 United States strikes on Iranian nuclear sites — CRS Report IN12571",
        "url": "https://www.congress.gov/crs-product/IN12571",
        "source_type": "congressional",
        "year": 2025,
    },
    {
        "id": 1621,
        "title": "2025 United States strikes on Iranian nuclear sites — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/2025_United_States_strikes_on_Iranian_nuclear_sites",
        "source_type": "other",
        "year": 2025,
    },
    # --- Mandelson ---
    {
        "id": 1622,
        "title": "Peter Mandelson sacked as UK Ambassador to US over Epstein links — CNBC",
        "url": "https://www.cnbc.com/2025/09/11/peter-mandelson-sacked-uk-ambassador-epstein-files.html",
        "source_type": "journalism",
        "author": "CNBC",
        "year": 2025,
    },
    {
        "id": 1623,
        "title": "Peter Mandelson arrested by Met Police on suspicion of misconduct in public office — CNN",
        "url": "https://www.cnn.com/2026/02/23/uk/peter-mandelson-arrested-met-police-epstein-intl",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2026,
    },
    {
        "id": 1624,
        "title": "Peter Mandelson quits Labour Party — France24",
        "url": "https://www.france24.com/en/europe/20260201-peter-mandelson-quits-labour-party-epstein",
        "source_type": "journalism",
        "author": "France24",
        "year": 2026,
    },
    {
        "id": 1625,
        "title": "Peter Mandelson released under investigation, bail conditions removed — ITV News",
        "url": "https://www.itv.com/news/2026-03-06/peter-mandelson-released-under-investigation",
        "source_type": "journalism",
        "author": "ITV News",
        "year": 2026,
    },
    {
        "id": 1626,
        "title": "Starmer admits to Parliament he should not have appointed Mandelson — CNN",
        "url": "https://www.cnn.com/2026/04/20/uk/starmer-mandelson-appointment-parliament-intl",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2026,
    },
    # --- WEF / Schwab ---
    {
        "id": 1627,
        "title": "Davos founder Schwab cleared of misconduct by WEF probe — France24",
        "url": "https://www.france24.com/en/live-news/20250815-davos-founder-schwab-cleared-of-misconduct-by-wef-probe",
        "source_type": "journalism",
        "author": "France24",
        "year": 2025,
    },
    {
        "id": 1628,
        "title": "WEF confirms investigation into claims against founder Schwab — France24",
        "url": "https://www.france24.com/en/live-news/20250423-wef-confirms-investigation-into-claims-against-founder-schwab",
        "source_type": "journalism",
        "author": "France24",
        "year": 2025,
    },
    {
        "id": 1629,
        "title": "Klaus Schwab and wife Hilde: WEF questionable travel expenses investigation — Fortune",
        "url": "https://fortune.com/2025/07/23/klaus-schwab-wife-hilde-world-economic-forum-questionable-travel-expenses-investigation",
        "source_type": "journalism",
        "author": "Fortune",
        "year": 2025,
    },
    {
        "id": 1630,
        "title": "ECB head Christine Lagarde 'ready to serve' as WEF head — Euronews",
        "url": "https://www.euronews.com/my-europe/2026/08/23/ecb-head-christine-lagarde-ready-to-serve-wef-report-says",
        "source_type": "journalism",
        "author": "Euronews",
        "year": 2026,
    },
    {
        "id": 1631,
        "title": "ECB chief Christine Lagarde 'ready to serve' World Economic Forum — Semafor",
        "url": "https://www.semafor.com/article/08/24/2026/ecb-chief-christine-lagarde-ready-to-serve-world-economic-forum",
        "source_type": "journalism",
        "author": "Semafor",
        "year": 2026,
    },
    # --- Iran succession / ceasefire ---
    {
        "id": 1632,
        "title": "Israel launches attack on Iran's capital alongside US strikes — Spectrum News",
        "url": "https://spectrumlocalnews.com/us/snplus/international/2026/02/28/israel-launches-attack-on-iran-s-capital-with-u-s--help-as-tensions-high-over-nuclear-talks",
        "source_type": "journalism",
        "author": "Spectrum News",
        "year": 2026,
    },
    {
        "id": 1633,
        "title": "Khamenei's funeral meant to project strength, but Iran's new leader has yet to appear — Time",
        "url": "https://time.com/article/2026/07/05/khamenei-s-funeral-is-meant-to-project-strength-but-iran-s-new-leader-has-yet-to-appear/",
        "source_type": "journalism",
        "author": "Time",
        "year": 2026,
    },
    {
        "id": 1634,
        "title": "Why is Pezeshkian urging an end to Iran's 'no war, no peace' status? — Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/8/9/why-is-pezeshkian-urging-an-end-to-irans-no-war-no-peace-status",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    # --- Biographical / reference ---
    {
        "id": 1635,
        "title": "JD Vance — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/JD_Vance",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1636,
        "title": "Marco Rubio — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Marco_Rubio",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1637,
        "title": "Pete Hegseth — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Pete_Hegseth",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1638,
        "title": "Pam Bondi — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Pam_Bondi",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1639,
        "title": "Department of Government Efficiency — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Department_of_Government_Efficiency",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1640,
        "title": "Elon Musk — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Elon_Musk",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1641,
        "title": "Steve Witkoff — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Steve_Witkoff",
        "source_type": "other",
        "year": 2026,
    },
    # --- Iran retaliation ---
    {
        "id": 1642,
        "title": "2025 Iranian strikes on Al Udeid Air Base — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/2025_Iranian_strikes_on_Al_Udeid_Air_Base",
        "source_type": "other",
        "year": 2025,
    },
    # --- Hegseth confirmation ---
    {
        "id": 1643,
        "title": "Trump to Create Department of War, Hegseth Pushes 'Warrior Ethos': Live Updates — Newsweek",
        "url": "https://www.newsweek.com/trump-department-war-hegseth-defense-order-live-updates-2125101",
        "source_type": "journalism",
        "author": "Newsweek",
        "year": 2025,
    },
    # --- Bondi / Epstein files / firing ---
    {
        "id": 1644,
        "title": "Attorney General Pamela Bondi releases first phase of declassified Epstein files — DOJ",
        "url": "https://www.justice.gov/opa/pr/attorney-general-pamela-bondi-releases-first-phase-declassified-epstein-files",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 1645,
        "title": "Trump fires Pam Bondi as attorney general — CNBC",
        "url": "https://www.cnbc.com/2026/04/02/trump-pam-bondi-attorney-general-lee-zeldin.html",
        "source_type": "journalism",
        "author": "CNBC",
        "year": 2026,
    },
    {
        "id": 1646,
        "title": "Pam Bondi testifies on Epstein file release before Congress — NPR",
        "url": "https://www.npr.org/2026/05/29/nx-s1-5836563/pam-bondi-epstein-congress",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2026,
    },
    # --- Musk / DOGE departure ---
    {
        "id": 1647,
        "title": "Musk leaves DOGE: What comes next — NPR",
        "url": "https://www.npr.org/2025/05/30/nx-s1-5415641/musk-leaves-doge-what-comes-next",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2025,
    },
    {
        "id": 1648,
        "title": "Musk announces 'America Party' political party for 2026 midterms — NPR",
        "url": "https://www.npr.org/2025/07/06/g-s1-76292/musk-political-party-america",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2025,
    },
    # --- CZ pardon ---
    {
        "id": 1649,
        "title": "Trump pardons Binance founder Changpeng Zhao — CNN",
        "url": "https://www.cnn.com/2025/10/23/politics/binance-founder-trump-pardon",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2025,
    },
    # --- IEEPA tariffs ruling ---
    {
        "id": 1650,
        "title": "Supreme Court strikes down Trump IEEPA tariffs (Learning Resources v. Trump) — Tax Foundation",
        "url": "https://taxfoundation.org/blog/supreme-court-trump-tariffs-ruling/",
        "source_type": "journalism",
        "author": "Tax Foundation",
        "year": 2026,
    },
    # --- Lutnick / Epstein ---
    {
        "id": 1651,
        "title": "Howard Lutnick and Jeffrey Epstein: What we know about the Commerce Secretary's island visit — NBC News",
        "url": "https://www.nbcnews.com/politics/congress/howard-lutnick-jeffrey-epstein-island-rcna258333",
        "source_type": "journalism",
        "author": "NBC News",
        "year": 2026,
    },
    {
        "id": 1652,
        "title": "Howard Lutnick's Jeffrey Epstein ties: Commerce Secretary faces resignation calls — CNBC",
        "url": "https://www.cnbc.com/2026/05/14/howard-lutnick-jeffrey-epstein-commerce-trump.html",
        "source_type": "journalism",
        "author": "CNBC",
        "year": 2026,
    },
    # --- Jan 6 pardons ---
    {
        "id": 1653,
        "title": "Trump pardons January 6 defendants on first day in office — NPR",
        "url": "https://www.npr.org/2025/01/20/g-s1-36809/trump-pardons-january-6-riot",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2025,
    },
    # --- Gaza Board of Peace ---
    {
        "id": 1654,
        "title": "Guide to Trump's twenty-point Gaza peace deal — CFR",
        "url": "https://www.cfr.org/articles/guide-trumps-twenty-point-gaza-peace-deal",
        "source_type": "journalism",
        "author": "Council on Foreign Relations",
        "year": 2025,
    },
    # --- Howard Lutnick biography ---
    {
        "id": 1655,
        "title": "Howard Lutnick — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Howard_Lutnick",
        "source_type": "other",
        "year": 2026,
    },
]

# ============================================================
# ENTITIES (11 new)
# ============================================================

ENTITIES = [
    {
        "name": "Russia-Ukraine War",
        "entity_type": "event",
        "description": (
            "Armed conflict between Russia and Ukraine, the largest land war in Europe "
            "since 1945. Russia's full-scale invasion began February 24, 2022, following "
            "the annexation of Crimea in 2014 and proxy war in the Donbas. The invasion "
            "violated the Budapest Memorandum (1994) under which Ukraine surrendered the "
            "world's third-largest nuclear arsenal in exchange for sovereignty guarantees "
            "from Russia, the United States, and the United Kingdom. By February 2026, "
            "estimated casualties exceeded one million Russian military personnel (killed "
            "and wounded) and 250,000-300,000 Ukrainian. Multiple rounds of negotiations "
            "have taken place including US-Russia-Ukraine talks in Abu Dhabi (January-February "
            "2026), an Easter truce (April 11, 2026), and a Victory Day ceasefire (May 9-11, "
            "2026). Zelensky sent an open letter to Putin on June 4, 2026 proposing direct "
            "talks. The Trump-Putin Anchorage Summit (August 15, 2025) produced no agreement. "
            "As of August 2026, the war continues with no lasting ceasefire; Russia's "
            "territorial gains have slowed to 13 square miles in the four weeks prior to "
            "August 4, 2026."
        ),
        "aliases": "Russo-Ukrainian War, Ukraine War, Ukraine Conflict",
        "metadata": {
            "status": "active",
            "location": "Ukraine",
        },
    },
    {
        "name": "Volodymyr Zelensky",
        "entity_type": "person",
        "description": (
            "Volodymyr Oleksandrovych Zelensky (born January 25, 1978, Kryvyi Rih, Ukraine). "
            "Sixth President of Ukraine (2019-present). Former comedian, actor, and producer "
            "who starred in the television series 'Servant of the People' (2015-2019), "
            "playing a schoolteacher who accidentally becomes president. Won the 2019 "
            "presidential election in a landslide over incumbent Petro Poroshenko. Became "
            "the international face of Ukrainian resistance following Russia's full-scale "
            "invasion on February 24, 2022. Named Time Person of the Year 2022. Invoked "
            "the Budapest Memorandum's sovereignty guarantees. On June 4, 2026, published "
            "an open letter to Putin proposing direct peace talks and offering a full "
            "ceasefire during negotiations. Also sent a separate letter to Trump requesting "
            "missile defense capabilities. As of August 2026, continues to lead wartime "
            "Ukraine while navigating negotiations with both Trump and Putin."
        ),
        "aliases": "Zelenskyy, Volodymyr Zelenskyy, Zelensky",
        "metadata": {
            "nationality": "Ukrainian",
            "born": "1978-01-25",
            "role": "President of Ukraine (2019-present)",
            "status": "active",
        },
    },
    {
        "name": "Budapest Memorandum (1994)",
        "entity_type": "event",
        "description": (
            "Political agreement signed December 5, 1994, at the CSCE Budapest summit. "
            "The United States, the United Kingdom, and the Russian Federation provided "
            "security assurances to Ukraine in exchange for Ukraine's accession to the "
            "Treaty on the Non-Proliferation of Nuclear Weapons and its relinquishing of "
            "the world's third-largest nuclear arsenal (approximately 1,900 strategic "
            "warheads inherited from the Soviet Union). Parallel memoranda were signed "
            "with Belarus and Kazakhstan. The signatories pledged to respect Ukraine's "
            "sovereignty, territorial integrity, and existing borders, and to refrain "
            "from the threat or use of force. The memorandum is a political commitment, "
            "not a legally binding treaty. Russia violated its terms with the annexation "
            "of Crimea in 2014 and the full-scale invasion of Ukraine in 2022, rendering "
            "it the central broken promise of the post-Cold War security order."
        ),
        "aliases": "Budapest Memorandum",
        "metadata": {
            "location": "Budapest, Hungary",
        },
    },
    {
        "name": "Anchorage Summit (2025)",
        "entity_type": "event",
        "description": (
            "First in-person meeting between US President Donald Trump and Russian President "
            "Vladimir Putin since 2019, held August 15, 2025, at Joint Base Elmendorf-Richardson "
            "in Anchorage, Alaska. The approximately three-hour meeting (11:30 AM to 2:15 PM "
            "local time) included Secretary of State Marco Rubio and Special Envoy Steve "
            "Witkoff on the US side, and Foreign Minister Sergei Lavrov and presidential "
            "aide Yuri Ushakov on the Russian side. Zelensky was not present. No agreement "
            "was reached on ending the Russia-Ukraine war. Trump stated afterward: 'There's "
            "no deal until there's a deal.' The summit was part of Trump's broader diplomatic "
            "effort to broker a Russia-Ukraine settlement, which included multiple Witkoff "
            "missions to Moscow and Abu Dhabi talks in early 2026."
        ),
        "aliases": "Alaska Summit, Trump-Putin Anchorage Meeting",
        "metadata": {
            "location": "Joint Base Elmendorf-Richardson, Anchorage, Alaska",
        },
    },
    {
        "name": "JD Vance",
        "entity_type": "person",
        "description": (
            "James David Vance (born James Donald Bowman, August 2, 1984, Middletown, Ohio). "
            "50th Vice President of the United States (January 20, 2025-present). US Senator "
            "from Ohio (2023-2025). Former Marine who served in Iraq. Graduate of Ohio State "
            "University and Yale Law School. Author of the memoir 'Hillbilly Elegy' (2016). "
            "His 2022 Senate campaign was heavily backed by Peter Thiel (Palantir co-founder), "
            "who contributed $15 million. Originally a vocal critic of Trump who evolved into "
            "a close ally. Selected as Trump's running mate at the 2024 Republican National "
            "Convention. Cast the tie-breaking Senate vote to confirm Pete Hegseth as Secretary "
            "of Defense in January 2025. As Vice President, serves as President of the Senate "
            "and is positioned as Trump's political successor."
        ),
        "aliases": "James David Vance, J.D. Vance",
        "metadata": {
            "nationality": "American",
            "born": "1984-08-02",
            "role": "Vice President of the United States (2025-present)",
            "prior_role": "US Senator from Ohio (2023-2025)",
            "status": "active",
        },
    },
    {
        "name": "Marco Rubio",
        "entity_type": "person",
        "description": (
            "Marco Antonio Rubio (born May 28, 1971, Miami, Florida). 72nd United States "
            "Secretary of State (January 2025-present). US Senator from Florida (2011-2025). "
            "Son of Cuban immigrants. The first Cabinet member confirmed in Trump's second "
            "term. Also served as Acting National Security Advisor from May 1, 2025, holding "
            "dual foreign policy and national security portfolios. Attended the Trump-Putin "
            "Anchorage Summit (August 15, 2025) alongside Steve Witkoff. Testified before "
            "Congress in June 2026 regarding US objectives in the Iran conflict (Operation "
            "Epic Fury). Co-sponsor of the bipartisan UAP Disclosure Act with Senators "
            "Schumer, Gillibrand, and Rounds. Previously ran for president in 2016, losing "
            "to Trump in the Republican primary."
        ),
        "aliases": "Marco Antonio Rubio",
        "metadata": {
            "nationality": "American",
            "born": "1971-05-28",
            "role": "Secretary of State (2025-present), Acting NSA (May 2025-present)",
            "prior_role": "US Senator from Florida (2011-2025)",
            "status": "active",
        },
    },
    {
        "name": "Pete Hegseth",
        "entity_type": "person",
        "description": (
            "Peter Brian Hegseth (born June 6, 1980). Secretary of Defense (January "
            "2025-present), styled 'Secretary of War' since the September 5, 2025 executive order (announced August 25), following "
            "Trump's executive order directing use of the historical 'Department of War' "
            "title. Former Fox News weekend co-host. Army National Guard veteran who served "
            "in Guantanamo Bay (2004), Iraq (Samarra, 2005-2006), and Afghanistan (Kabul, "
            "2011-2012). Awarded two Bronze Stars. Narrowly confirmed by the Senate with "
            "Vice President JD Vance casting the tie-breaking vote. Oversaw the military "
            "execution of Operation Epic Fury (February-April 2026) against Iran. The "
            "Department of War executive order authorized secondary use of the historical "
            "title in official correspondence; a permanent statutory name change requires "
            "Congressional action."
        ),
        "aliases": "Peter Brian Hegseth",
        "metadata": {
            "nationality": "American",
            "born": "1980-06-06",
            "role": "Secretary of Defense / Secretary of War (2025-present)",
            "prior_role": "Fox News host",
            "status": "active",
        },
    },
    {
        "name": "Pam Bondi",
        "entity_type": "person",
        "description": (
            "Pamela Jo Bondi (born November 17, 1965, Tampa, Florida). 87th United States "
            "Attorney General (February-April 2026). Former Attorney General of Florida "
            "(2011-2019), the first woman elected to that office. Confirmed 54-46 on February "
            "4, 2025. In January 2026, released the first phase of declassified Epstein files "
            "(approximately three million pages) pursuant to the Epstein Files Transparency "
            "Act signed in November 2025. The release contained over 1,000 mentions of Donald "
            "Trump. Refused congressional questioning in February 2026; the House Oversight "
            "Committee subpoenaed her on March 4, 2026. Fired by Trump on April 2, 2026, "
            "reportedly over dissatisfaction with her handling of the Epstein files and other "
            "prosecutorial decisions. Testified before Congress on May 29, 2026 defending the "
            "DOJ's Epstein file release process."
        ),
        "aliases": "Pamela Jo Bondi",
        "metadata": {
            "nationality": "American",
            "born": "1965-11-17",
            "role": "Former United States Attorney General (Feb 2025-Apr 2026)",
            "prior_role": "Attorney General of Florida (2011-2019)",
            "status": "active",
        },
    },
    {
        "name": "Elon Musk",
        "entity_type": "person",
        "description": (
            "Elon Reeve Musk (born June 28, 1971, Pretoria, South Africa). Entrepreneur and "
            "business magnate. CEO of Tesla, SpaceX, and X (formerly Twitter, acquired October "
            "2022 for $44 billion). Spent $250+ million supporting Trump's 2024 presidential "
            "campaign. Appointed to lead the Department of Government Efficiency (DOGE) in "
            "January 2025. Led aggressive government cost-cutting initiatives, proposing up to "
            "$2 trillion in federal spending cuts and rapid federal workforce reductions. DOGE's "
            "actions generated extensive litigation, with multiple federal courts issuing "
            "injunctions. Departed DOGE on May 30, 2025, receiving a golden key from Trump in "
            "an Oval Office farewell. The split turned hostile in June 2025 when Musk publicly "
            "called a Republican spending bill a 'disgusting abomination,' triggering a social "
            "media feud with Trump. In July 2025, announced formation of the 'America Party' "
            "for the 2026 midterms. His role at DOGE marked an unprecedented overlap of private-"
            "sector power and executive branch authority, given his companies' extensive federal "
            "contracts (SpaceX with NASA and DOD, Tesla with DOE)."
        ),
        "aliases": "Elon Reeve Musk",
        "metadata": {
            "nationality": "South African-American",
            "born": "1971-06-28",
            "role": "CEO of Tesla/SpaceX/X; former DOGE head (Jan-May 2025)",
            "status": "active",
        },
    },
    {
        "name": "DOGE",
        "entity_type": "program",
        "description": (
            "Department of Government Efficiency (DOGE). Advisory body established by "
            "executive order (EO 14158) on January 20, 2025, Trump's first day in office, "
            "reorganizing the US Digital Service into the 'US DOGE Service.' Led by Elon "
            "Musk, initially alongside Vivek Ramaswamy (who departed in February 2025 to "
            "pursue Ohio's gubernatorial race). Tasked with identifying and eliminating "
            "government waste, fraud, and abuse, with Musk proposing up to $2 trillion in "
            "federal spending cuts. DOGE pursued aggressive federal workforce reductions "
            "and agency restructuring that generated extensive litigation, with multiple "
            "federal courts issuing injunctions. Musk departed DOGE on May 30, 2025; DOGE "
            "was subsequently dismantled following his exit and the Musk-Trump public split "
            "in June 2025. The initiative represented an unprecedented delegation of "
            "government restructuring authority to a private-sector figure."
        ),
        "aliases": "Department of Government Efficiency",
        "metadata": {
            "status": "dismantled",
        },
    },
    {
        "name": "Steve Witkoff",
        "entity_type": "person",
        "description": (
            "Steven C. Witkoff (born c. 1957). American real estate developer and Special "
            "Presidential Envoy for the Russia-Ukraine conflict. Founder of the Witkoff Group, "
            "a New York-based real estate investment firm. Personal friend of Donald Trump with "
            "no prior diplomatic experience. Appointed alongside Secretary of State Rubio to "
            "lead Russia-Ukraine peace negotiations. Attended the Trump-Putin Anchorage Summit "
            "(August 15, 2025). Visited Putin in St. Petersburg on April 11, 2025 (his third "
            "meeting with Putin since January 2025). Led talks with Russian envoy Kirill "
            "Dmitriev and Ukrainian officials throughout 2025-2026. A Bloomberg report revealed "
            "Witkoff coached a Putin aide on how to pitch the Russian leader's position to Trump, "
            "raising questions about neutrality in his mediating role."
        ),
        "aliases": "Steven Witkoff, Steven C. Witkoff",
        "metadata": {
            "nationality": "American",
            "born": "1957-03-15",
            "role": "Special Presidential Envoy, Russia-Ukraine (2025-present)",
            "status": "active",
        },
    },
    {
        "name": "Howard Lutnick",
        "entity_type": "person",
        "description": (
            "Howard Wayne Lutnick (born July 14, 1961, Jericho, New York). United States "
            "Secretary of Commerce (2025-present). Chairman and CEO of Cantor Fitzgerald, "
            "the financial services firm that lost 658 employees in the September 11, 2001 "
            "attacks. Co-chaired Trump's transition team. Confirmed along party lines "
            "(51-45). Documented Epstein connections: lived next door to Jeffrey Epstein in "
            "Manhattan for over a decade, visited Epstein's island in 2012 on what he "
            "described as a family vacation. Initially claimed he cut off contact with "
            "Epstein in 2005, but released Epstein files showed communications continuing "
            "to 2018. In May 2026, Democrats called for his resignation over the Epstein "
            "ties; Lutnick retained his position with Trump's backing."
        ),
        "aliases": "Howard Wayne Lutnick",
        "metadata": {
            "nationality": "American",
            "born": "1961-07-14",
            "role": "Secretary of Commerce (2025-present)",
            "prior_role": "CEO of Cantor Fitzgerald",
            "status": "active",
        },
    },
]

# ============================================================
# RELATIONSHIPS (31)
# ============================================================

RELATIONSHIPS = [
    # ---- Trump administration appointments ----
    {
        "source": "Donald Trump",
        "target": "JD Vance",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Selected JD Vance as running mate at the 2024 Republican National Convention. "
            "Vance inaugurated as 50th Vice President on January 20, 2025."
        ),
        "year_start": 2024,
        "year_end": 2025,
        "sources": [1635],
    },
    {
        "source": "Donald Trump",
        "target": "Marco Rubio",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Appointed Marco Rubio as 72nd Secretary of State. Rubio was the first Cabinet "
            "member confirmed in Trump's second term (January 2025). Also served as Acting "
            "National Security Advisor from May 1, 2025."
        ),
        "year_start": 2025,
        "sources": [1636, 1619],
    },
    {
        "source": "Donald Trump",
        "target": "Pete Hegseth",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Appointed Pete Hegseth as Secretary of Defense. Narrowly confirmed by the "
            "Senate with VP Vance casting the tie-breaking vote in January 2025. On August "
            "25, 2025, Trump signed an executive order directing use of the 'Department of "
            "War' secondary title."
        ),
        "year_start": 2025,
        "sources": [1637, 1617],
    },
    {
        "source": "Donald Trump",
        "target": "Pam Bondi",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Appointed Pam Bondi as 87th United States Attorney General in his second "
            "term (2025). Bondi previously served on Trump's first-term transition team."
        ),
        "year_start": 2025,
        "sources": [1638],
    },
    {
        "source": "Donald Trump",
        "target": "Elon Musk",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Appointed Elon Musk to lead the Department of Government Efficiency (DOGE) "
            "via executive order signed January 20, 2025. Musk had been Trump's most "
            "prominent financial backer in the 2024 campaign."
        ),
        "year_start": 2025,
        "sources": [1639, 1640],
    },
    {
        "source": "Donald Trump",
        "target": "Steve Witkoff",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Appointed personal friend Steve Witkoff as Special Presidential Envoy for "
            "Russia-Ukraine peace negotiations in early 2025. Witkoff had no prior "
            "diplomatic experience."
        ),
        "year_start": 2025,
        "sources": [1612, 1641],
    },
    # ---- Anchorage Summit attendees ----
    {
        "source": "Donald Trump",
        "target": "Anchorage Summit (2025)",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "Led the US delegation at the Anchorage Summit on August 15, 2025. Met with "
            "Putin for approximately three hours. Stated afterward: 'There's no deal until "
            "there's a deal.'"
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1605, 1606, 1607],
    },
    {
        "source": "Vladimir Putin",
        "target": "Anchorage Summit (2025)",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "Led the Russian delegation at the Anchorage Summit alongside Foreign Minister "
            "Lavrov and aide Ushakov. First in-person meeting with Trump since 2019."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1605, 1606, 1607],
    },
    {
        "source": "Marco Rubio",
        "target": "Anchorage Summit (2025)",
        "type": "attended",
        "tier": "documented",
        "desc": (
            "Attended the Trump-Putin Anchorage Summit on August 15, 2025 in his capacity "
            "as Secretary of State, alongside Special Envoy Witkoff."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1605, 1607],
    },
    {
        "source": "Steve Witkoff",
        "target": "Anchorage Summit (2025)",
        "type": "attended",
        "tier": "documented",
        "desc": (
            "Attended the Trump-Putin Anchorage Summit on August 15, 2025 as Special "
            "Presidential Envoy. Had previously met Putin in St. Petersburg on April 11, "
            "2025 (his third Putin meeting since January 2025)."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1605, 1607, 1613],
    },
    # ---- Russia-Ukraine War principals ----
    {
        "source": "Vladimir Putin",
        "target": "Russia-Ukraine War",
        "type": "ordered",
        "tier": "documented",
        "desc": (
            "Ordered the full-scale invasion of Ukraine on February 24, 2022. Continues "
            "to prosecute the war as of August 2026 despite estimated one million Russian "
            "military casualties (killed and wounded)."
        ),
        "year_start": 2022,
        "sources": [1600, 1601],
    },
    {
        "source": "Volodymyr Zelensky",
        "target": "Russia-Ukraine War",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "Wartime President of Ukraine leading national defense since Russia's full-scale "
            "invasion on February 24, 2022. International symbol of resistance. Pursuing "
            "diplomatic settlement including the June 4, 2026 open letter to Putin."
        ),
        "year_start": 2022,
        "sources": [1600, 1608, 1611],
    },
    {
        "source": "Donald Trump",
        "target": "Russia-Ukraine War",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "Pursuing diplomatic settlement of the war through the Anchorage Summit "
            "(August 2025), envoy Steve Witkoff's shuttle diplomacy, and Abu Dhabi "
            "talks (January-February 2026). No deal reached as of August 2026."
        ),
        "year_start": 2025,
        "sources": [1605, 1607, 1612],
    },
    {
        "source": "Marco Rubio",
        "target": "Russia-Ukraine War",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "In dual role as Secretary of State and Acting NSA, coordinated US diplomatic "
            "approach to the Russia-Ukraine conflict. Attended Anchorage Summit. Led "
            "interagency policy on Ukraine alongside Witkoff."
        ),
        "year_start": 2025,
        "sources": [1605, 1636],
    },
    {
        "source": "Steve Witkoff",
        "target": "Russia-Ukraine War",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "Special Presidential Envoy for Russia-Ukraine negotiations. Met with Putin "
            "multiple times (third visit by April 2025). Led talks with Russian envoy "
            "Kirill Dmitriev. Bloomberg reported he coached a Putin aide on how to pitch "
            "the Russian leader's position to Trump."
        ),
        "year_start": 2025,
        "sources": [1612, 1613],
    },
    {
        "source": "Steve Witkoff",
        "target": "Vladimir Putin",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Met Putin at least three times between January and April 2025 as special "
            "envoy, including an April 11, 2025 visit to St. Petersburg. Bloomberg "
            "reported Witkoff coached a Putin aide on messaging strategy."
        ),
        "year_start": 2025,
        "sources": [1613, 1612],
    },
    {
        "source": "Anchorage Summit (2025)",
        "target": "Russia-Ukraine War",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The summit was convened specifically to negotiate an end to the Russia-Ukraine "
            "war. No agreement was reached; the war continued through 2026."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1605, 1607],
    },
    # ---- Budapest Memorandum ----
    {
        "source": "Budapest Memorandum (1994)",
        "target": "Russia-Ukraine War",
        "type": "preceded",
        "tier": "documented",
        "desc": (
            "The Budapest Memorandum's security guarantees for Ukraine were violated by "
            "Russia's 2014 Crimea annexation and 2022 full-scale invasion. Ukraine "
            "surrendered its nuclear arsenal based on these now-broken assurances."
        ),
        "year_start": 1994,
        "sources": [1603, 1604],
    },
    {
        "source": "Vladimir Putin",
        "target": "Budapest Memorandum (1994)",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Russia under Putin violated the Budapest Memorandum's core provisions — "
            "sovereignty, territorial integrity, and non-use of force — with the 2014 "
            "Crimea annexation and 2022 invasion of Ukraine."
        ),
        "year_start": 2014,
        "sources": [1603, 1604],
    },
    # ---- Zelensky diplomatic edges ----
    {
        "source": "Volodymyr Zelensky",
        "target": "Donald Trump",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Wartime diplomatic relationship. Zelensky sent a separate letter to Trump "
            "in June 2026 requesting missile defense capabilities. Relations complicated "
            "by Trump's pursuit of a negotiated settlement that Ukraine fears could "
            "require territorial concessions."
        ),
        "year_start": 2025,
        "sources": [1608, 1609],
    },
    {
        "source": "Volodymyr Zelensky",
        "target": "Vladimir Putin",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Wartime adversaries. Zelensky published an open letter to Putin on June 4, "
            "2026 proposing direct face-to-face talks with a full ceasefire during "
            "negotiations. The Kremlin responded that Zelensky was welcome in Moscow "
            "'any time.' Zelensky said the letter achieved its goal of revealing Moscow's "
            "rejection of genuine peace."
        ),
        "year_start": 2022,
        "sources": [1608, 1609],
    },
    # ---- NATO / war ----
    {
        "source": "Russia-Ukraine War",
        "target": "NATO",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "NATO allies provide 99% of Ukraine's military aid per the 2025 Hague Summit "
            "declaration. The 2026 Ankara Summit committed 70 billion euros for Ukraine. "
            "Ukraine remains an aspirant partner, not a member."
        ),
        "year_start": 2022,
        "sources": [1614, 1615, 1616],
    },
    # ---- Iran political layer ----
    {
        "source": "Donald Trump",
        "target": "Operation Epic Fury",
        "type": "authorized",
        "tier": "documented",
        "desc": (
            "Authorized Operation Epic Fury, the combined US military operation against "
            "Iran launched February 28, 2026. No AUMF or formal declaration of war was "
            "passed by Congress, generating significant debate."
        ),
        "year_start": 2026,
        "year_end": 2026,
        "sources": [1632, 1619],
    },
    {
        "source": "Pete Hegseth",
        "target": "Operation Epic Fury",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "As Secretary of Defense (styled 'Secretary of War'), oversaw the military "
            "execution of Operation Epic Fury against Iran (February-April 2026)."
        ),
        "year_start": 2026,
        "year_end": 2026,
        "sources": [1617, 1632],
    },
    {
        "source": "Marco Rubio",
        "target": "Operation Epic Fury",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "In dual role as Secretary of State and Acting National Security Advisor, "
            "coordinated the political-diplomatic dimensions of the Iran campaign. "
            "Testified before Congress in June 2026 regarding US objectives."
        ),
        "year_start": 2026,
        "year_end": 2026,
        "sources": [1619],
    },
    # ---- DOGE ----
    {
        "source": "Elon Musk",
        "target": "DOGE",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Led DOGE from its creation on January 20, 2025 until his departure on May 30, "
            "2025. Proposed up to $2 trillion in federal spending cuts. Initially co-led "
            "with Vivek Ramaswamy, who departed in February 2025. DOGE was subsequently "
            "dismantled following Musk's exit."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1639, 1640, 1647],
    },
    {
        "source": "Elon Musk",
        "target": "Donald Trump",
        "type": "funded",
        "tier": "credible",
        "desc": (
            "Spent $250+ million supporting Trump's 2024 presidential campaign. Appointed "
            "to lead DOGE following inauguration. The alliance fractured in June 2025 when "
            "Musk publicly attacked a Republican spending bill; in July 2025, Musk announced "
            "formation of the rival 'America Party' for the 2026 midterms."
        ),
        "year_start": 2024,
        "year_end": 2025,
        "sources": [1640, 1647, 1648],
    },
    # ---- Pam Bondi / DOJ ----
    {
        "source": "Pam Bondi",
        "target": "DOJ",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Served as Attorney General heading the Department of Justice from February "
            "2025 until fired by Trump on April 2, 2026. Released the first phase of "
            "declassified Epstein files (approximately three million pages) in January "
            "2026. Fired reportedly over dissatisfaction with Epstein file handling."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1638, 1644, 1645],
    },
    {
        "source": "Pam Bondi",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As Attorney General, oversaw the release of the first phase of declassified "
            "Epstein files in January 2026 (approximately three million pages) pursuant "
            "to the Epstein Files Transparency Act. The release contained over 1,000 "
            "mentions of Donald Trump. Bondi was subpoenaed by House Oversight on March 4, "
            "2026, and testified before Congress on May 29, 2026."
        ),
        "year_start": 2026,
        "year_end": 2026,
        "sources": [1644, 1646],
    },
    # ---- JD Vance connections ----
    {
        "source": "JD Vance",
        "target": "Peter Thiel",
        "type": "ally_of",
        "tier": "documented",
        "desc": (
            "Thiel contributed $15 million to Vance's 2022 Ohio Senate campaign and "
            "served as a key political mentor. Vance previously worked at Thiel's Mithril "
            "Capital. The Thiel-Vance alliance represents the New Right's influence on "
            "the Trump coalition."
        ),
        "year_start": 2022,
        "sources": [1635],
    },
    {
        "source": "JD Vance",
        "target": "Pete Hegseth",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "VP Vance cast the tie-breaking Senate vote to confirm Hegseth as Secretary "
            "of Defense in January 2025, using his constitutional role as President of "
            "the Senate."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1637],
    },
    # ---- Mandelson / Met Police ----
    {
        "source": "Peter Mandelson",
        "target": "Metropolitan Police",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "Arrested by Metropolitan Police on February 23, 2026 on suspicion of "
            "misconduct in public office — specifically, allegations of passing "
            "market-sensitive information to Jeffrey Epstein while serving as Business "
            "Secretary. Released on bail the same day. Released under investigation on "
            "March 6, 2026 with bail conditions removed. As of August 2026, no charges "
            "filed."
        ),
        "year_start": 2026,
        "sources": [1623, 1625],
    },
    # ---- Howard Lutnick ----
    {
        "source": "Donald Trump",
        "target": "Howard Lutnick",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Appointed Howard Lutnick as Secretary of Commerce. Lutnick co-chaired "
            "Trump's transition team. Confirmed along party lines (51-45). Despite "
            "documented Epstein connections, Lutnick retained Trump's backing when "
            "Democrats called for his resignation in May 2026."
        ),
        "year_start": 2025,
        "sources": [1655, 1651],
    },
    {
        "source": "Howard Lutnick",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Lived next door to Jeffrey Epstein in Manhattan for over a decade. "
            "Visited Epstein's island in 2012, described as a family vacation. "
            "Initially claimed he cut off contact with Epstein in 2005, but released "
            "Epstein files showed communications continuing to 2018. Democrats demanded "
            "his resignation in May 2026 over these ties."
        ),
        "year_start": 2002,
        "year_end": 2018,
        "sources": [1651, 1652],
    },
]

# ============================================================
# ENTITY → SOURCE mappings (for every new entity)
# ============================================================

ENTITY_SOURCES = {
    "Russia-Ukraine War": [1600, 1601, 1602, 1608, 1610],
    "Volodymyr Zelensky": [1608, 1609, 1611],
    "Budapest Memorandum (1994)": [1603, 1604],
    "Anchorage Summit (2025)": [1605, 1606, 1607],
    "JD Vance": [1635],
    "Marco Rubio": [1636, 1619],
    "Pete Hegseth": [1617, 1637, 1643],
    "Pam Bondi": [1638, 1644, 1645, 1646],
    "Elon Musk": [1639, 1640, 1647, 1648],
    "DOGE": [1639, 1647],
    "Steve Witkoff": [1612, 1613, 1641],
    "Howard Lutnick": [1651, 1652, 1655],
}

# ============================================================
# ENTITY UPDATES (existing entities — exact DB names)
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "Donald Trump",
        "description_append": (
            "2025-2026 update: Inaugurated as 47th President on January 20, 2025. On his "
            "first day, issued pardons and commutations for approximately 1,500 January 6 "
            "defendants (including Enrique Tarrio and Stewart Rhodes) and established the "
            "Department of Government Efficiency (DOGE) under Elon Musk. Key appointments: "
            "Marco Rubio (Secretary of State, confirmed 99-0), Pete Hegseth (Secretary of "
            "Defense, VP tie-break), Pam Bondi (Attorney General, 54-46), Howard Lutnick "
            "(Commerce), Steve Witkoff (Ukraine envoy). Authorized strikes on Iran's nuclear "
            "facilities on June 21, 2025 (Operation Midnight Hammer). Held the Anchorage "
            "Summit with Putin on August 15, 2025 — no Ukraine deal. Signed executive order "
            "September 5, 2025 (announced August 25) restyling DoD as the 'Department of War' name. Pardoned Binance founder "
            "Changpeng Zhao on October 21, 2025. Announced 20-point Gaza peace plan with "
            "Netanyahu on September 29, 2025 ('Board of Peace'). Authorized Operation Epic "
            "Fury against Iran (February 28, 2026). On February 20, 2026, the Supreme Court "
            "struck down his IEEPA tariffs 6-3 (Learning Resources v. Trump). Fired Attorney "
            "General Bondi on April 2, 2026. Iran ceasefire reached April 8, 2026. As of "
            "August 2026, continues Russia-Ukraine negotiations through Witkoff."
        ),
        "metadata": {"role": "47th President of the United States (2025-present)"},
        "sources": [1605, 1617, 1620, 1632, 1639, 1649, 1650, 1653, 1654, 1645],
    },
    {
        "name": "Vladimir Putin",
        "description_append": (
            "2025-2026 update: Continues to prosecute the war against Ukraine despite "
            "mounting casualties estimated at one million Russian military killed and wounded "
            "by February 2026. Met with Trump at the Anchorage Summit on August 15, 2025 — "
            "no deal reached. Engaged in Abu Dhabi negotiations (January-February 2026) "
            "through intermediaries. Agreed to an Easter truce (April 11, 2026) and Victory "
            "Day ceasefire (May 9-11, 2026), both marked by violations. Dismissed Zelensky's "
            "June 4, 2026 open letter, with the Kremlin stating Zelensky could come to Moscow "
            "'any time.' As of August 2026, Russia's territorial gains have slowed "
            "significantly — only 13 square miles gained in the four weeks prior to August 4, "
            "2026. On August 21, 2026, Russia said it was 'ready for new ideas' on Ukraine, "
            "provided they aligned with Putin's stated positions."
        ),
        "sources": [1601, 1602, 1605, 1607, 1608, 1609],
    },
    {
        "name": "World Economic Forum",
        "description_append": (
            "2025-2026 update: In April 2025, the WEF board confirmed an investigation into "
            "whistleblower complaints against founder Klaus Schwab, alleging over $1 million "
            "in questionable expenses and mixing of personal and Forum resources. The probe "
            "cleared Schwab in August 2025. Davos 2026 (January 19-23) convened for the first "
            "time without Schwab under the theme 'A Spirit of Dialogue,' drawing approximately "
            "3,000 attendees including 65 heads of state and 830 CEOs. Following Brende's "
            "February 26, 2026 resignation, Alois Zwinggi continues as interim president/CEO. "
            "As of August 2026, no permanent successor has been named, though reports indicate "
            "ECB President Christine Lagarde has expressed readiness to serve as WEF head, "
            "possibly from 2027."
        ),
        "sources": [1627, 1628, 1629, 1630, 1631],
    },
    {
        "name": "Klaus Schwab",
        "description_append": (
            "2025-2026 update: In April 2025, faced a formal WEF board investigation "
            "following whistleblower complaints alleging more than $1 million in questionable "
            "expenses and mixing of personal resources with Forum funds. Stepped down as "
            "board chair during the investigation. The probe cleared Schwab and his wife "
            "Hilde of misconduct in August 2025. Schwab reportedly filed criminal complaints "
            "against the whistleblowers. The January 2026 Davos meeting was the first in WEF "
            "history held without Schwab's direct leadership."
        ),
        "sources": [1627, 1628, 1629],
    },
    {
        "name": "Alois Zwinggi",
        "description_append": (
            "2025-2026 update: Continues to serve as interim President and CEO of WEF as of "
            "August 2026, over six months after Brende's resignation. No permanent successor "
            "has been named. Reports in August 2026 indicate ECB President Christine Lagarde "
            "may be positioned to succeed him, possibly from 2027."
        ),
        "sources": [1630, 1631],
    },
    {
        "name": "Peter Mandelson",
        "description_append": (
            "2025-2026 update: On September 11, 2025, sacked as UK Ambassador to the United "
            "States after Epstein files revealed a deeper relationship with Jeffrey Epstein "
            "than previously disclosed. On February 1, 2026, resigned from the Labour Party. "
            "In February 2026, also resigned from the House of Lords (retaining his title as "
            "Baron Mandelson). On February 23, 2026, arrested by Metropolitan Police on "
            "suspicion of misconduct in public office — specifically, allegations of passing "
            "market-sensitive information to Epstein while serving as Business Secretary. "
            "Released on bail the same day. On March 6, 2026, released under investigation "
            "with bail conditions removed and passport returned. On April 20, 2026, Prime "
            "Minister Starmer admitted to Parliament that he should not have appointed "
            "Mandelson as ambassador. As of August 2026, remains released under investigation "
            "with no charges filed."
        ),
        "metadata": {"status": "released under investigation"},
        "sources": [1622, 1623, 1624, 1625, 1626],
    },
    {
        "name": "Ali Khamenei",
        "description_append": (
            "2025-2026 update: Following Khamenei's death in the February 28, 2026 strikes, "
            "his son Mojtaba Khamenei was selected as the third Supreme Leader of Iran on "
            "March 8, 2026, by the Assembly of Experts. Operation Epic Fury was authorized "
            "by President Trump; the military operation was overseen by Secretary of Defense "
            "Hegseth."
        ),
        "sources": [1632, 1633],
    },
    {
        "name": "Masoud Pezeshkian",
        "description_append": (
            "2025-2026 update: Survived the Operation Epic Fury strikes of February 28, "
            "2026. Vice President Mohammad Reza Aref briefly assumed executive functions "
            "during wartime uncertainty. Pezeshkian continues as President as of August "
            "2026. In August 2026, publicly called for an end to Iran's 'no war, no peace' "
            "status following the April 8, 2026 ceasefire with the United States."
        ),
        "sources": [1634],
    },
    {
        "name": "Bilderberg Group",
        "description_append": (
            "2025-2026 update: The 2026 Bilderberg Meeting was held April 9-12, 2026, at "
            "the Salamander Resort and Spa in Washington, D.C. 128 participants from 23 "
            "countries attended. Notable participants included King Willem-Alexander of the "
            "Netherlands, NATO Secretary General Mark Rutte, UK Foreign Secretary David "
            "Lammy, Google DeepMind CEO Demis Hassabis, former Google CEO Eric Schmidt, and "
            "Pfizer CEO Albert Bourla. The published agenda included AI governance, the "
            "Russia-Ukraine war, the Middle East, and Arctic security."
        ),
        "sources": [1615],
    },
    {
        "name": "Davos Annual Meeting",
        "description_append": (
            "2025-2026 update: The January 2026 meeting (January 19-23) convened under the "
            "theme 'A Spirit of Dialogue,' drawing approximately 3,000 attendees including "
            "65 heads of state and 830 CEOs. It was the first Davos held without founder "
            "Klaus Schwab's direct involvement. Speakers included President Trump, Canadian "
            "PM Mark Carney, and European Commission President Ursula von der Leyen."
        ),
        "sources": [1630],
    },
    {
        "name": "NATO",
        "description_append": (
            "2025-2026 update: The June 24-25, 2025 Hague Summit established a 5% GDP "
            "defense spending target by 2035 (3.5% core defense plus 1.5% resilience and "
            "infrastructure). Reaffirmed support for Ukraine, noting that 99% of Ukraine's "
            "military aid comes from NATO allies. Mark Rutte serves as Secretary General. "
            "The July 7-8, 2026 Ankara Summit produced the Ankara Declaration committing to "
            "$50 billion in new equipment procurement and 70 billion euros for Ukraine in "
            "2026, alongside a 12-nation long-range weapons initiative led by the UK. No "
            "new members admitted; Bosnia-Herzegovina, Georgia, and Ukraine remain aspirant "
            "partners."
        ),
        "sources": [1614, 1615, 1616],
    },
    {
        "name": "Operation Epic Fury",
        "description_append": (
            "2025-2026 update: Authorized directly by President Trump. Secretary of State "
            "and Acting National Security Advisor Marco Rubio coordinated the political-"
            "diplomatic dimensions. Secretary of Defense Pete Hegseth (styled 'Secretary "
            "of War') oversaw the military execution. No Authorization for Use of Military "
            "Force (AUMF) or formal declaration of war against Iran was passed by Congress, "
            "generating significant debate. Rubio testified before Congress in June 2026 "
            "regarding US objectives. A ceasefire was reached on April 8, 2026, with renewed "
            "peace talks initiated in Pakistan. Mojtaba Khamenei succeeded his father as "
            "Supreme Leader on March 8, 2026."
        ),
        "sources": [1619, 1632, 1633],
    },
]

# ============================================================
# GEO_COORDS — for new entities only
# ============================================================

GEO_COORDS = {
    "Russia-Ukraine War": (48.3794, 31.1656, "credible", "Geographic center of Ukraine"),
    "Volodymyr Zelensky": (50.4501, 30.5234, "credible", "Kyiv, Ukraine — presidential office"),
    "Budapest Memorandum (1994)": (47.4979, 19.0402, "documented", "Budapest, Hungary — CSCE summit venue"),
    "Anchorage Summit (2025)": (61.2501, -149.7948, "documented", "JBER, Anchorage, Alaska"),
    "JD Vance": (38.8921, -77.0669, "credible", "Washington DC — VP residence"),
    "Marco Rubio": (38.8951, -77.0469, "credible", "Washington DC — State Department HQ"),
    "Pete Hegseth": (38.8719, -77.0563, "credible", "The Pentagon, Arlington, VA"),
    "Pam Bondi": (38.8937, -77.0260, "credible", "Washington DC — DOJ Main Building"),
    "Elon Musk": (38.8977, -77.0365, "inference", "Washington DC — DOGE operations"),
    "DOGE": (38.8977, -77.0365, "credible", "Washington DC — federal government"),
    "Steve Witkoff": (40.7128, -74.0060, "inference", "New York, NY — Witkoff Group HQ"),
    "Howard Lutnick": (40.7527, -73.9772, "credible", "New York, NY — Cantor Fitzgerald HQ"),
}

# ============================================================
# PHOTO_CANDIDATES — for new persons / orgs
# ============================================================

PHOTO_CANDIDATES = {
    "Volodymyr Zelensky": "https://upload.wikimedia.org/wikipedia/commons/4/42/Volodymyr_Zelensky_2019_presidential_portrait_%28cropped%29.jpg",
    "JD Vance": "https://upload.wikimedia.org/wikipedia/commons/1/11/J.D._Vance_official_Senate_portrait_%28118th_Congress%29.jpg",
    "Marco Rubio": "https://upload.wikimedia.org/wikipedia/commons/6/66/Marco_Rubio%2C_Official_Portrait%2C_112th_Congress_2.jpg",
    "Pete Hegseth": "https://upload.wikimedia.org/wikipedia/commons/6/64/Pete_Hegseth_official_photo.jpg",
    "Pam Bondi": "https://upload.wikimedia.org/wikipedia/commons/5/54/Pam_Bondi_official_photo.jpg",
    "Elon Musk": "https://upload.wikimedia.org/wikipedia/commons/3/34/Elon_Musk_Royal_Society_%28crop2%29.jpg",
    "Steve Witkoff": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Steve_Witkoff.jpg",
    "Howard Lutnick": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Howard_Lutnick.jpg",
}
