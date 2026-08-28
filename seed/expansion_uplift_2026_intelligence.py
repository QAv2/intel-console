"""
Intelligence & Covert — August 2026 uplift expansion for Intel Console.

Brings the intelligence branch (153 entities) up to date through August 2026.
Covers: Trump-era intelligence leadership appointments (Ratcliffe CIA, Patel FBI,
Gabbard DNI, Metreweli MI6); Signalgate (March 2025); Operation Grim Beeper
(Sept 2024 Hezbollah pager attack); Operation Southern Spear and the capture
of Nicolás Maduro (Jan 2026); Salt Typhoon telecom breach; Nord Stream sabotage
prosecution; Mossad/Unit 8200 roles in the 2025–2026 Iran wars; NSO Group
WhatsApp verdict and acquisition; Epstein–intelligence revelations from
DOJ/FBI releases; FISA Section 702 lapse; Assange plea deal; Snowden status.

EXISTING ENTITIES referenced by exact DB name:
  CIA, FBI, NSA, DOJ, DEA, Mossad, MI6, MI5, FSB, CENTCOM,
  Unit 8200, NSO Group, Hezbollah, MSS, Donald Trump, Vladimir Putin,
  Jeffrey Epstein, James Clapper, Julian Assange, Edward Snowden,
  Operation Epic Fury, Operation Roaring Lion, Operation Midnight Hammer,
  FISA Amendments Act, NATO

ENTITIES created by OTHER agents (referenced, not duplicated):
  Pete Hegseth, Marco Rubio, Elon Musk, JD Vance, Pam Bondi,
  Tulsi Gabbard — OVERRIDDEN: created here per task instructions
  John Ratcliffe, Kash Patel — OVERRIDDEN: created here
  Benjamin Netanyahu (Topol agent)
  Russia–Ukraine War, Volodymyr Zelensky (power agent)
  Epstein Files Transparency Act, Todd Blanche (exploitation agent)

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1700–1799
# ============================================================

SOURCES = [
    # --- Intelligence leadership ---
    {
        "id": 1700,
        "title": "John Ratcliffe Sworn In as CIA Director — CIA.gov",
        "url": "https://www.cia.gov/stories/story/john-ratcliffe-sworn-in-as-cia-director",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 1701,
        "title": "New FBI Director Takes Oath of Office — FBI.gov",
        "url": "https://www.fbi.gov/news/stories/new-fbi-director-takes-oath-of-office",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 1702,
        "title": "DNI Gabbard Sworn In as 8th Director of National Intelligence — DNI.gov",
        "url": "https://www.dni.gov/index.php/newsroom/press-releases/press-releases-2025/4050-pr-01-25",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 1703,
        "title": "Senate confirms Tulsi Gabbard as Director of National Intelligence — Washington Post",
        "url": "https://www.washingtonpost.com/national-security/2025/02/12/tulsi-gabbard-senate-confirmation/",
        "source_type": "journalism",
        "author": "Washington Post",
        "year": 2025,
    },
    {
        "id": 1704,
        "title": "Britain's MI6 appoints Blaise Metreweli as first female chief — Euronews",
        "url": "https://euronews.com/2025/06/16/britains-mi6-appoints-blaise-metreweli-as-its-first-female-chief-in-116-year-history",
        "source_type": "journalism",
        "author": "Euronews",
        "year": 2025,
    },
    {
        "id": 1705,
        "title": "NSA Director Fired: Tim Haugh removed — Washington Post",
        "url": "https://www.washingtonpost.com/national-security/2025/04/03/nsa-director-fired-tim-haugh/",
        "source_type": "journalism",
        "author": "Washington Post",
        "year": 2025,
    },
    {
        "id": 1706,
        "title": "Senate confirms new leader of CyberCom and NSA — Federal News Network",
        "url": "https://federalnewsnetwork.com/federal-newscast/2026/03/senate-confirms-new-leader-of-cybercom-and-nsa/",
        "source_type": "journalism",
        "author": "Federal News Network",
        "year": 2026,
    },
    {
        "id": 1707,
        "title": "Mossad Chief Barnea to Step Down — Times of Israel",
        "url": "https://www.timesofisrael.com/report-mossad-chief-barnea-to-step-down-next-june-pm-begins-search-for-successor/",
        "source_type": "journalism",
        "author": "Times of Israel",
        "year": 2026,
    },
    {
        "id": 1708,
        "title": "Roman Gofman approved as next Mossad director — JNS",
        "url": "https://www.jns.org/news/israel-news/roman-gofman-approved-as-next-mossad-director",
        "source_type": "journalism",
        "author": "JNS",
        "year": 2026,
    },
    # --- Signalgate ---
    {
        "id": 1709,
        "title": "Judge orders preservation of Signal messages from Houthi strike chat — NPR",
        "url": "https://www.npr.org/2025/03/28/g-s1-56821/signal-houthi-strike-chat-judge",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2025,
    },
    {
        "id": 1710,
        "title": "Pentagon IG finds Hegseth violated military regulations in Signalgate — NBC News",
        "url": "https://www.nbcnews.com/politics/politics-news/pentagons-signalgate-review-finds-pete-hegseth-violated-military-regul-rcna247023",
        "source_type": "journalism",
        "author": "NBC News",
        "year": 2025,
    },
    {
        "id": 1711,
        "title": "Waltz ousted as National Security Adviser after Signalgate — CNN",
        "url": "https://www.cnn.com/2025/05/01/politics/mike-waltz-national-security-adviser-depart",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2025,
    },
    {
        "id": 1712,
        "title": "Signalgate Inspector General report contradicts Hegseth's claims — Washington Post",
        "url": "https://www.washingtonpost.com/national-security/2025/12/04/signal-pete-hegseth-inspector-general/",
        "source_type": "journalism",
        "author": "Washington Post",
        "year": 2025,
    },
    # --- Operation Grim Beeper ---
    {
        "id": 1713,
        "title": "Walkie-talkies explode in Lebanon day after pager attack — CNN",
        "url": "https://www.cnn.com/world/live-news/lebanon-pagers-explode-hezbollah-israel-09-18-24-intl-hnk/index.html",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2024,
    },
    {
        "id": 1714,
        "title": "Gold Apollo pager supply chain and BAC Consulting — CNN",
        "url": "https://www.cnn.com/2024/09/18/business/gold-apollo-taiwan-lebanon-exploding-pagers-hnk-intl/index.html",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2024,
    },
    {
        "id": 1715,
        "title": "Israel BAC Consulting supply chain details — Newsweek",
        "url": "https://www.newsweek.com/israel-bac-exploding-pagers-hezbollah-1955525",
        "source_type": "journalism",
        "author": "Newsweek",
        "year": 2024,
    },
    # --- Operation Southern Spear / Venezuela ---
    {
        "id": 1716,
        "title": "The US Military Campaign Targeting Venezuela — Council on Foreign Relations",
        "url": "https://www.cfr.org/articles/operation-southern-spear-us-military-campaign-targeting-venezuela",
        "source_type": "academic",
        "author": "Council on Foreign Relations",
        "year": 2026,
    },
    {
        "id": 1717,
        "title": "Operation Southern Spear — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Operation_Southern_Spear",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1718,
        "title": "Timeline of US strikes against alleged drug boats — InSight Crime",
        "url": "https://insightcrime.org/news/timeline-us-strikes-against-alleged-drug-boats/",
        "source_type": "journalism",
        "author": "InSight Crime",
        "year": 2026,
    },
    {
        "id": 1719,
        "title": "How the US captured Maduro — NBC News",
        "url": "https://www.nbcnews.com/politics/donald-trump/us-venezuela-strike-nicolas-maduro-captured-how-timeline-trump-rcna252041",
        "source_type": "journalism",
        "author": "NBC News",
        "year": 2026,
    },
    {
        "id": 1720,
        "title": "Manhattan US Attorney announces narco-terrorism charges against Nicolás Maduro — DOJ",
        "url": "https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-narco-terrorism-charges-against-nicolas-maduro-current",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 1721,
        "title": "Delta Force carried out Venezuela raid — Task and Purpose",
        "url": "https://taskandpurpose.com/news/venezuela-maduro-delta-force-absolute-resolve/",
        "source_type": "journalism",
        "author": "Task and Purpose",
        "year": 2026,
    },
    {
        "id": 1722,
        "title": "US spy agencies contributed to operation that captured Maduro — Defense One",
        "url": "https://www.defenseone.com/threats/2026/01/us-spy-agencies-contributed-operation-captured-maduro/410437/",
        "source_type": "journalism",
        "author": "Defense One",
        "year": 2026,
    },
    # --- Salt Typhoon ---
    {
        "id": 1723,
        "title": "Salt Typhoon Telecom Breach — CRS Report for Congress",
        "url": "https://www.congress.gov/crs-product/IF12798",
        "source_type": "congressional",
        "year": 2025,
    },
    {
        "id": 1724,
        "title": "China's Salt Typhoon hackers continue to breach telecom firms — TechCrunch",
        "url": "https://techcrunch.com/2025/02/13/chinas-salt-typhoon-hackers-continue-to-breach-telecom-firms-despite-us-sanctions",
        "source_type": "journalism",
        "author": "TechCrunch",
        "year": 2025,
    },
    {
        "id": 1725,
        "title": "FBI labels suspected China hack of law enforcement data 'major cyber incident' — NBC News",
        "url": "https://www.nbcnews.com/news/us-news/fbi-labels-suspected-china-hack-law-enforcement-data-major-cyber-incid-rcna266495",
        "source_type": "journalism",
        "author": "NBC News",
        "year": 2025,
    },
    # --- Nord Stream sabotage ---
    {
        "id": 1726,
        "title": "German prosecutors charge Ukrainian suspect over Nord Stream explosions — Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/7/2/german-prosecutors-charge-ukrainian-suspect-over-nord-stream-explosions",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    {
        "id": 1727,
        "title": "Italy to extradite Ukrainian Nord Stream sabotage suspect to Germany — Al Jazeera",
        "url": "https://www.aljazeera.com/news/2025/11/20/italy-to-extradite-ukrainian-nord-stream-sabotage-suspect-to-germany",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2025,
    },
    {
        "id": 1728,
        "title": "Second Nord Stream suspect arrested in Croatia — CBC News",
        "url": "https://www.cbc.ca/news/world/nord-stream-pipeline-damage-arrest-9.7312068",
        "source_type": "journalism",
        "author": "CBC News",
        "year": 2026,
    },
    # --- Epstein–intelligence layer ---
    {
        "id": 1729,
        "title": "DOJ says no evidence Jeffrey Epstein had a 'client list' or blackmailed associates — NPR",
        "url": "https://www.npr.org/2025/07/07/g-s1-76367/doj-jeffrey-epstein-memo",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2025,
    },
    {
        "id": 1730,
        "title": "Jeffrey Epstein died by suicide and there's no 'client list' — CNN",
        "url": "https://www.cnn.com/2025/07/07/politics/jeffrey-epstein-suicide-client-list-justice",
        "source_type": "journalism",
        "author": "CNN",
        "year": 2025,
    },
    {
        "id": 1731,
        "title": "Department of Justice Publishes 3.5 Million Pages in Compliance with the Epstein Files Transparency Act — DOJ",
        "url": "https://www.justice.gov/opa/pr/department-justice-publishes-35-million-responsive-pages-compliance-epstein-files",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 1732,
        "title": "Epstein was target of 5-year-plus DEA probe: Docs — KFOR/CBS",
        "url": "https://kfor.com/news/epstein-was-target-of-5-year-plus-dea-probe-docs/",
        "source_type": "journalism",
        "author": "KFOR News",
        "year": 2026,
    },
    {
        "id": 1733,
        "title": "Epstein Files: What the DEA investigation revealed — New Republic",
        "url": "https://newrepublic.com/post/206960/jeffrey-epstein-files-drug-enforcement-administration-dea-investigation",
        "source_type": "journalism",
        "author": "New Republic",
        "year": 2026,
    },
    {
        "id": 1734,
        "title": "Wyden presses DEA for answers about Epstein investigation — Senate Finance Committee",
        "url": "https://www.finance.senate.gov/ranking-members-news/wyden-questions-dea-over-mystery-epstein-investigation",
        "source_type": "congressional",
        "year": 2026,
    },
    # --- NSO Group / surveillance ---
    {
        "id": 1735,
        "title": "Jury orders NSO Group to pay over $167M to WhatsApp — CyberScoop",
        "url": "https://cyberscoop.com/nso-group-owes-whatsapp-over-spyware-infections-jury/",
        "source_type": "journalism",
        "author": "CyberScoop",
        "year": 2025,
    },
    {
        "id": 1736,
        "title": "NSO ordered to stop hacking WhatsApp, damages cut to $4 million — SecurityWeek",
        "url": "https://www.securityweek.com/nso-ordered-to-stop-hacking-whatsapp-but-damages-cut-to-4-million/",
        "source_type": "journalism",
        "author": "SecurityWeek",
        "year": 2025,
    },
    {
        "id": 1737,
        "title": "Spyware maker NSO Group confirms acquisition by US investors — TechCrunch",
        "url": "https://techcrunch.com/2025/10/10/spyware-maker-nso-group-confirms-acquisition-by-us-investors/",
        "source_type": "journalism",
        "author": "TechCrunch",
        "year": 2025,
    },
    # --- FISA / Assange / Snowden ---
    {
        "id": 1738,
        "title": "FISA Section 702 Reauthorized for Two Years — Lawfare",
        "url": "https://www.lawfaremedia.org/article/fisa-section-702-reauthorized-for-two-years",
        "source_type": "academic",
        "author": "Lawfare",
        "year": 2024,
    },
    {
        "id": 1739,
        "title": "FISA 702 surveillance expires — NPR",
        "url": "https://www.npr.org/2026/06/12/nx-s1-5856291/fisa-702-surveillance-expiration-bill-pulte",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2026,
    },
    {
        "id": 1740,
        "title": "WikiLeaks founder Julian Assange pleads guilty and is sentenced — DOJ",
        "url": "https://www.justice.gov/archives/opa/pr/wikileaks-founder-pleads-guilty-and-sentenced-conspiring-obtain-and-disclose-classified",
        "source_type": "government",
        "year": 2024,
    },
    {
        "id": 1741,
        "title": "Julian Assange breaks silence at Council of Europe hearing — RSF",
        "url": "https://rsf.org/en/julian-assange-breaks-silence-landmark-council-europe-hearing",
        "source_type": "journalism",
        "author": "Reporters Without Borders",
        "year": 2024,
    },
    # --- Israel–Iran intelligence layer ---
    {
        "id": 1742,
        "title": "Operation Rising Lion to Midnight Hammer: US and Israel gambling with Iran's nuclear ambitions — Fair Observer",
        "url": "https://www.fairobserver.com/world-news/operation-rising-lion-to-midnight-hammer-why-the-us-and-israel-are-gambling-with-irans-nuclear-ambitions/",
        "source_type": "journalism",
        "author": "Fair Observer",
        "year": 2025,
    },
    {
        "id": 1743,
        "title": "5 times Unit 8200 waged digital war on Iran — WION",
        "url": "https://www.wionews.com/world/5-times-israel-s-unit-8200-waged-digital-war-on-iran-1750497054192",
        "source_type": "journalism",
        "author": "WION",
        "year": 2025,
    },
    {
        "id": 1744,
        "title": "Operations Epic Fury and Roaring Lion update — JINSA",
        "url": "https://jinsa.org/wp-content/uploads/2026/03/Operations-Epic-Fury-and-Roaring-Lion-03-01-26.pdf",
        "source_type": "academic",
        "author": "JINSA",
        "year": 2026,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Intelligence leadership ---
    {
        "name": "Office of the Director of National Intelligence",
        "entity_type": "agency",
        "description": (
            "United States federal agency established by the Intelligence Reform and "
            "Terrorism Prevention Act of 2004 in response to 9/11 Commission recommendations. "
            "The ODNI is headed by the Director of National Intelligence (DNI), who serves as "
            "the principal intelligence adviser to the President and oversees the entire "
            "U.S. Intelligence Community, comprising 18 member organizations including the CIA, "
            "NSA, FBI intelligence division, DIA, NRO, and NGA. The DNI coordinates budgets, "
            "collection priorities, and analysis across agencies. Senate-confirmed directors: "
            "John Negroponte (2005-2007), Mike McConnell (2007-2009), Dennis Blair (2009-2010), "
            "James Clapper (2010-2017), Dan Coats (2017-2019), John Ratcliffe (acting, 2020), "
            "Avril Haines (2021-2025), and Tulsi Gabbard (2025-present, confirmed Feb 12, 2025, "
            "the first female combat veteran to hold the post)."
        ),
        "aliases": "ODNI, DNI, Director of National Intelligence",
        "metadata": {
            "location": "Liberty Crossing, McLean, Virginia",
        },
    },
    {
        "name": "Tulsi Gabbard",
        "entity_type": "person",
        "description": (
            "Former U.S. Representative from Hawaii (2013-2021), Iraq War combat veteran, "
            "and 2020 Democratic presidential candidate who switched party affiliation to "
            "Republican in 2022. Confirmed as the 8th Director of National Intelligence on "
            "February 12, 2025, by a 52-48 Senate vote, becoming the first female combat "
            "veteran in the role. Oversees the 18-agency U.S. Intelligence Community. "
            "Her confirmation was contentious due to past statements sympathetic to Edward "
            "Snowden and meetings with Syrian President Bashar al-Assad. Participant in the "
            "March 2025 Signalgate group chat that leaked classified Houthi strike plans."
        ),
        "aliases": "Tulsi",
        "metadata": {
            "nationality": "American",
            "born": "1981-04-12",
            "role": "Director of National Intelligence (2025-present)",
            "prior_role": "U.S. Representative (HI-2), 2013-2021",
        },
    },
    {
        "name": "John Ratcliffe",
        "entity_type": "person",
        "description": (
            "Former U.S. Representative from Texas (2015-2020) and the 6th Director of "
            "National Intelligence (2020-2021) under President Trump's first term. Confirmed "
            "as the 9th Director of the Central Intelligence Agency on January 23, 2025, by a "
            "74-25 Senate vote, with twenty Democrats joining Republicans. Sworn in the same "
            "day by Vice President JD Vance at the White House. Participant in the March 2025 "
            "Signalgate group chat that exposed classified Houthi strike plans when a journalist "
            "was accidentally added."
        ),
        "aliases": "John Lee Ratcliffe",
        "metadata": {
            "nationality": "American",
            "born": "1965-10-20",
            "role": "CIA Director (2025-present)",
            "prior_role": "Director of National Intelligence, 2020-2021",
        },
    },
    {
        "name": "Kash Patel",
        "entity_type": "person",
        "description": (
            "American attorney and former government official. Served as Senior Director for "
            "Counterterrorism at the NSC and Chief of Staff to the Acting Secretary of Defense "
            "during Trump's first term. Confirmed as the 9th Director of the Federal Bureau of "
            "Investigation on February 20, 2025, by a 51-49 party-line Senate vote, sworn in "
            "February 21 by Attorney General Pamela Bondi. His appointment followed Trump's "
            "dismissal of Christopher Wray. In July 2025, Senator Dick Durbin wrote to Patel "
            "questioning the FBI's two-page memo concluding there was no Epstein 'client list,' "
            "noting the finding contradicted prior assurances from AG Bondi that 'everything' "
            "would be brought to light."
        ),
        "aliases": "Kashyap Pramod Patel",
        "metadata": {
            "nationality": "American",
            "born": "1980-02-25",
            "role": "FBI Director (2025-present)",
            "prior_role": "Chief of Staff to Acting SecDef, 2020-2021",
        },
    },
    {
        "name": "Blaise Metreweli",
        "entity_type": "person",
        "description": (
            "British intelligence officer who became the 18th Chief of the Secret Intelligence "
            "Service (MI6) on October 1, 2025, succeeding Sir Richard Moore. The first woman "
            "to hold the position of 'C' in MI6's 116-year history. Announced by PM Keir "
            "Starmer on June 16, 2025. Joined MI6 in 1999 and spent much of her early career "
            "in the Middle East during the Afghanistan and Iraq wars. Previously served as Head "
            "of Hostile States Counterintelligence at MI5 and Director General of Technology "
            "and Innovation (known as 'Q') at MI6. Studied anthropology at Pembroke College, "
            "Cambridge. Awarded CMG in 2024."
        ),
        "aliases": "C, Blaise Florence Metreweli",
        "metadata": {
            "nationality": "British",
            "born": "1977-07-30",
            "role": "Chief of MI6 (2025-present)",
            "prior_role": "MI6 Director General of Technology and Innovation",
        },
    },
    # --- Venezuela ---
    {
        "name": "Nicolás Maduro",
        "entity_type": "person",
        "description": (
            "President of Venezuela from 2013 until his capture by U.S. special forces on "
            "January 3, 2026. Succeeded Hugo Chavez after winning a disputed 2013 election. "
            "His government oversaw Venezuela's economic collapse, hyperinflation, and the "
            "displacement of over seven million Venezuelans. First indicted in the U.S. "
            "Southern District of New York in March 2020 on narco-terrorism charges alleging "
            "he led the Cartel de los Soles, a military-run drug trafficking network. "
            "Captured in a predawn Delta Force raid in Caracas (Operation Absolute Resolve) "
            "on January 3, 2026, along with his wife Cilia Flores. Transferred to USS Iwo "
            "Jima, then flown to New York. Arraigned in Manhattan federal court on January 5, "
            "2026, pleading not guilty to narco-terrorism conspiracy and cocaine importation "
            "charges. The superseding indictment named 14 co-defendants. The most significant "
            "U.S. direct action in Latin America since the 1989 invasion of Panama."
        ),
        "aliases": "Nicolás Maduro Moros, Nicolas Maduro",
        "metadata": {
            "nationality": "Venezuelan",
            "born": "1962-11-23",
            "role": "Former President of Venezuela (2013-2026)",
            "status": "indicted",
        },
    },
    {
        "name": "SOUTHCOM",
        "entity_type": "agency",
        "description": (
            "United States Southern Command. Unified combatant command responsible for U.S. "
            "military operations in Central America, South America, and the Caribbean, "
            "headquartered at Doral, Florida. In 2025-2026, SOUTHCOM led Operation Southern "
            "Spear, the largest U.S. military campaign in the Western Hemisphere since the "
            "Cold War, deploying approximately 15,000 personnel, the USS Gerald R. Ford "
            "carrier strike group, B-52 bombers, and MQ-9 Reaper drones. Created Joint Task "
            "Force Southern Spear in October 2025 (HQ at Naval Station Mayport, FL). "
            "Coordinated the January 3, 2026 capture of Nicolás Maduro (Operation Absolute "
            "Resolve). Between August 2025 and March 2026, operations cost at least $4.7 "
            "billion. In August 2026, JTF Southern Spear was replaced by Joint Task Force "
            "Western Hemisphere under the Americas Counter-Cartel Coalition."
        ),
        "aliases": "United States Southern Command, USSOUTHCOM",
        "metadata": {
            "location": "Doral, Florida",
        },
    },
    {
        "name": "Operation Southern Spear",
        "entity_type": "event",
        "description": (
            "U.S. military counter-narco-terrorism campaign in the Caribbean and South America, "
            "formally announced by Defense Secretary Pete Hegseth on November 13, 2025, though "
            "boat strikes began September 1, 2025. The largest U.S. military presence in the "
            "Caribbean since the Cold War. Led by SOUTHCOM and the newly created Joint Task "
            "Force Southern Spear. Encompassed naval strikes on alleged drug-trafficking "
            "vessels (227 killed in vessel strikes by August 2026), an oil blockade of "
            "Venezuela, and the January 3, 2026 capture of President Nicolás Maduro in "
            "Operation Absolute Resolve (a Delta Force raid in Caracas). Over 150 aircraft "
            "deployed including F-22 Raptors, F-35s, and F/A-18 Super Hornets. CIA operatives "
            "provided ground intelligence tracking Maduro's location. Cost: at least $4.7 "
            "billion (Aug 2025-Mar 2026). Replaced August 2026 by JTF Western Hemisphere."
        ),
        "aliases": "Southern Spear, Operation Absolute Resolve",
    },
    # --- Signalgate ---
    {
        "name": "Signalgate",
        "entity_type": "event",
        "description": (
            "National security breach in March 2025 when National Security Advisor Mike Waltz "
            "accidentally added The Atlantic editor-in-chief Jeffrey Goldberg to a Signal "
            "group chat ('Houthi PC small group') used by senior Trump administration officials "
            "to discuss classified military operations against Houthi rebels in Yemen. On "
            "March 15, Defense Secretary Pete Hegseth posted specific operational details "
            "including F-18 launch times, Tomahawk missile targeting, and attack sequencing "
            "two to four hours before execution. The source material was classified "
            "SECRET/NOFORN. Participants included VP JD Vance, CIA Director John Ratcliffe, "
            "DNI Tulsi Gabbard, Secretary of State Marco Rubio, and Treasury Secretary "
            "Scott Bessent. Goldberg published the first account March 24, 2025. Waltz was "
            "removed as NSA on May 1, 2025. The Pentagon IG report (December 2025) found "
            "Hegseth violated Department of Defense policy and created 'a risk to operational "
            "security' that could 'harm DoD personnel and mission objectives.'"
        ),
        "aliases": "Signal Chat Leak, Houthi PC Small Group, United States Government Group Chat Leak",
    },
    # --- Pager attack ---
    {
        "name": "Operation Grim Beeper",
        "entity_type": "event",
        "description": (
            "Covert supply-chain sabotage operation attributed to Israel's Mossad that "
            "detonated thousands of electronic devices used by Hezbollah operatives in Lebanon "
            "on September 17-18, 2024. On the first day, thousands of Gold Apollo AR-924 "
            "pagers exploded simultaneously; on the second, hundreds of Icom walkie-talkies "
            "detonated. The devices had been manufactured by BAC Consulting KFT, a "
            "Budapest-based front company operating under a licensing agreement with Taiwan's "
            "Gold Apollo, with approximately 3 grams of PETN explosive implanted in each "
            "battery. Casualties: 42 killed (including 12 civilians and 2 children) and "
            "3,500-4,000 wounded. Described as Hezbollah's worst security breach since "
            "October 2023. Israeli PM Benjamin Netanyahu acknowledged the operation in "
            "November 2024. Approximately 1,500 Hezbollah fighters were taken out of action."
        ),
        "aliases": "Lebanon Pager Attack, 2024 Lebanon Pager Explosions",
    },
    # --- Salt Typhoon ---
    {
        "name": "Salt Typhoon Telecom Breach",
        "entity_type": "event",
        "description": (
            "Chinese state-sponsored cyber espionage campaign attributed to China's Ministry "
            "of State Security (MSS), first reported in October 2024. Salt Typhoon infiltrated "
            "at least nine major U.S. telecommunications providers including AT&T, Verizon, and "
            "T-Mobile by exploiting government-mandated CALEA wiretap infrastructure. The "
            "hackers exfiltrated metadata from over one million users, an almost complete list "
            "of phone numbers under U.S. law enforcement wiretap orders, and 18 months of FBI "
            "wiretap data. Targets included 2024 presidential campaign staffers from both "
            "parties. Described by officials as the worst telecom hack in American history. "
            "U.S. Treasury sanctioned Sichuan Juxinhe Network Technology Co. for direct "
            "involvement. The U.S. launched a $3 billion program to remove Chinese-linked "
            "hardware from global networks. As of August 2026, the FBI stated threats remain "
            "'still very much ongoing.'"
        ),
        "aliases": "Salt Typhoon, GhostEmperor",
    },
    # --- Nord Stream ---
    {
        "name": "Nord Stream Sabotage Investigation",
        "entity_type": "event",
        "description": (
            "German federal criminal investigation into the September 26, 2022 underwater "
            "explosions that destroyed three of four Nord Stream 1 and Nord Stream 2 gas "
            "pipeline lines in the Baltic Sea near Denmark's Bornholm Island. German "
            "prosecutors allege the sabotage was a Ukrainian covert operation. Two Ukrainian "
            "suspects identified: Serhii Kuznetsov, a former Ukrainian military officer "
            "alleged to have led a seven-person team aboard the sailing yacht 'Andromeda,' "
            "was arrested in Italy in August 2025, extradited to Germany in November 2025, "
            "and formally charged in July 2026 with attacking civilian energy infrastructure "
            "and war crimes. Trial set for October 26, 2026 in Hamburg. A second suspect, "
            "Volodymyr Zhuravlev (a professional diver), was arrested in Croatia in August "
            "2026 while working on a Hollywood film about the sabotage. Ukraine denies state "
            "involvement."
        ),
        "aliases": "Nord Stream Prosecution, Nord Stream Pipeline Sabotage",
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ========== LEADERSHIP APPOINTMENTS ==========
    {
        "source": "Tulsi Gabbard",
        "target": "Office of the Director of National Intelligence",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as 8th Director of National Intelligence on February 12, 2025 "
            "(Senate vote 52-48). First female combat veteran in the role. Oversees the "
            "18-agency U.S. Intelligence Community."
        ),
        "year_start": 2025,
        "sources": [1702, 1703],
    },
    {
        "source": "John Ratcliffe",
        "target": "CIA",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as 9th Director of the CIA on January 23, 2025 (Senate vote 74-25). "
            "Sworn in the same day by Vice President JD Vance. Previously served as 6th "
            "Director of National Intelligence (2020-2021)."
        ),
        "year_start": 2025,
        "sources": [1700],
    },
    {
        "source": "Kash Patel",
        "target": "FBI",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as 9th FBI Director on February 20, 2025 (Senate vote 51-49), "
            "sworn in February 21 by AG Pamela Bondi. Replaced Christopher Wray, who "
            "was dismissed by President Trump."
        ),
        "year_start": 2025,
        "sources": [1701],
    },
    {
        "source": "Tulsi Gabbard",
        "target": "Donald Trump",
        "type": "appointed_by",
        "tier": "documented",
        "desc": (
            "Nominated by President Trump for DNI. Confirmed February 12, 2025. "
            "Her nomination was part of Trump's overhaul of the intelligence community."
        ),
        "year_start": 2025,
        "sources": [1702, 1703],
    },
    {
        "source": "John Ratcliffe",
        "target": "Donald Trump",
        "type": "appointed_by",
        "tier": "documented",
        "desc": (
            "Nominated by President Trump for CIA Director, confirmed January 23, 2025. "
            "Second intelligence community appointment by Trump (previously DNI in 2020)."
        ),
        "year_start": 2025,
        "sources": [1700],
    },
    {
        "source": "Kash Patel",
        "target": "Donald Trump",
        "type": "appointed_by",
        "tier": "documented",
        "desc": (
            "Nominated by President Trump for FBI Director, confirmed February 20, 2025. "
            "Previously served Trump as NSC Senior Director for Counterterrorism."
        ),
        "year_start": 2025,
        "sources": [1701],
    },
    {
        "source": "Blaise Metreweli",
        "target": "MI6",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Appointed 18th Chief of MI6 ('C') on October 1, 2025, succeeding Sir Richard "
            "Moore. First woman to lead MI6 in its 116-year history. Announced by PM Starmer "
            "on June 16, 2025."
        ),
        "year_start": 2025,
        "sources": [1704],
    },
    {
        "source": "James Clapper",
        "target": "Office of the Director of National Intelligence",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "4th Director of National Intelligence from August 2010 to January 2017. "
            "Infamously told Congress the NSA does not 'wittingly' collect data on Americans "
            "— proven false by Snowden revelations."
        ),
        "year_start": 2010,
        "year_end": 2017,
        "sources": [1702],
    },
    # ========== SIGNALGATE ==========
    {
        "source": "Tulsi Gabbard",
        "target": "Signalgate",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "Participant in the March 2025 Signal group chat ('Houthi PC small group') "
            "that leaked classified military strike plans when a journalist was accidentally "
            "added by NSA Mike Waltz."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1709, 1710],
    },
    {
        "source": "John Ratcliffe",
        "target": "Signalgate",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "CIA Director Ratcliffe was a member of the Houthi PC small group Signal chat "
            "that exposed classified strike plans in March 2025."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1709, 1710],
    },
    # NOTE: Pete Hegseth involved_in Signalgate and Marco Rubio involved_in
    # Signalgate edges deferred — those entities are created by the power agent.
    # Add after power module lands:
    #   Pete Hegseth -> Signalgate (involved_in, documented, [1709, 1710, 1712])
    #   Marco Rubio -> Signalgate (involved_in, documented, [1709, 1711])
    # ========== OPERATION GRIM BEEPER ==========
    {
        "source": "Mossad",
        "target": "Operation Grim Beeper",
        "type": "led",
        "tier": "credible",
        "desc": (
            "Widely attributed to Mossad by multiple intelligence sources and confirmed by "
            "Israeli PM Netanyahu in November 2024. Mossad manufactured AR-924 pagers "
            "integrated with PETN explosives through the Budapest-based front company BAC "
            "Consulting KFT, a supply-chain operation spanning multiple countries."
        ),
        "year_start": 2024,
        "year_end": 2024,
        "sources": [1713, 1714, 1715],
    },
    {
        "source": "Operation Grim Beeper",
        "target": "Hezbollah",
        "type": "targeted",
        "tier": "documented",
        "desc": (
            "Hezbollah was the target of the September 17-18, 2024 pager and walkie-talkie "
            "detonations. 42 killed, 3,500-4,000 wounded. Approximately 1,500 Hezbollah "
            "fighters taken out of action. Described as Hezbollah's worst security breach "
            "since October 2023."
        ),
        "year_start": 2024,
        "year_end": 2024,
        "sources": [1713, 1715],
    },
    # NOTE: Benjamin Netanyahu authorized Operation Grim Beeper edge deferred —
    # Netanyahu is created by the Topol agent. Add after that module lands:
    #   Benjamin Netanyahu -> Operation Grim Beeper (authorized, credible, [1713])
    # ========== OPERATION SOUTHERN SPEAR / VENEZUELA ==========
    {
        "source": "SOUTHCOM",
        "target": "Operation Southern Spear",
        "type": "led",
        "tier": "documented",
        "desc": (
            "SOUTHCOM led Operation Southern Spear, creating Joint Task Force Southern Spear "
            "in October 2025 (HQ Naval Station Mayport, FL). Deployed ~15,000 personnel, "
            "the Gerald R. Ford carrier strike group, and 150+ aircraft."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1716, 1717],
    },
    {
        "source": "CIA",
        "target": "Operation Southern Spear",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "CIA operatives were on the ground in Caracas before the January 3, 2026 raid, "
            "tracking Maduro's movements, habits, and sleep locations. A CIA source within "
            "the Venezuelan government assisted with location tracking. In late December 2025, "
            "the CIA conducted a drone strike on a Venezuelan dock described as a drug-loading "
            "facility."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1722],
    },
    {
        "source": "DEA",
        "target": "Operation Southern Spear",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "The narco-terrorism charges that formed the legal basis for the operation "
            "originated from a DEA-led investigation. DEA agents accompanied Maduro to "
            "New York after capture and assisted in his custody and processing."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1720, 1719],
    },
    {
        "source": "Nicolás Maduro",
        "target": "Operation Southern Spear",
        "type": "target_of",
        "tier": "documented",
        "desc": (
            "Captured by Delta Force in a predawn raid in Caracas on January 3, 2026 "
            "(Operation Absolute Resolve, a component of Operation Southern Spear). "
            "Transferred to USS Iwo Jima, arraigned in Manhattan federal court January 5, "
            "2026 on narco-terrorism conspiracy and cocaine importation charges."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1719, 1720, 1721],
    },
    {
        "source": "Nicolás Maduro",
        "target": "DOJ",
        "type": "indicted_in",
        "tier": "documented",
        "desc": (
            "First indicted in the U.S. Southern District of New York in March 2020 on "
            "narco-terrorism charges. Superseding indictment unsealed January 2026 after "
            "capture, naming 14 co-defendants including his wife Cilia Flores. Arraigned "
            "January 5, 2026, pleading not guilty."
        ),
        "year_start": 2020,
        "sources": [1720],
    },
    {
        "source": "Nicolás Maduro",
        "target": "DEA",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "Subject of DEA investigation that led to the March 2020 narco-terrorism "
            "indictment. The U.S. government identified Maduro as head of the Cartel "
            "de los Soles, a military-run drug trafficking network within Venezuela's "
            "armed forces."
        ),
        "year_start": 2020,
        "sources": [1720, 1719],
    },
    # ========== SALT TYPHOON ==========
    {
        "source": "MSS",
        "target": "Salt Typhoon Telecom Breach",
        "type": "directed",
        "tier": "credible",
        "desc": (
            "Salt Typhoon is attributed to China's Ministry of State Security by U.S. "
            "government agencies. Attack sophistication, target selection, and tools are "
            "consistent with known MSS operations. U.S. Treasury sanctioned Sichuan Juxinhe "
            "Network Technology Co. for direct involvement."
        ),
        "year_start": 2024,
        "year_end": 2026,
        "sources": [1723, 1724],
    },
    {
        "source": "Salt Typhoon Telecom Breach",
        "target": "FBI",
        "type": "targeted",
        "tier": "documented",
        "desc": (
            "Hackers exfiltrated 18 months of FBI wiretap data by exploiting "
            "government-mandated CALEA wiretap infrastructure at compromised telecoms. "
            "Accessed an almost complete list of phone numbers under U.S. law enforcement "
            "wiretap orders. FBI labeled it a 'major cyber incident.'"
        ),
        "year_start": 2024,
        "year_end": 2025,
        "sources": [1723, 1725],
    },
    {
        "source": "Salt Typhoon Telecom Breach",
        "target": "NSA",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "The breach compromised CALEA lawful intercept infrastructure that underpins "
            "U.S. signals intelligence collection capabilities. The scale of the breach — "
            "nine telecoms, metadata on over a million users — exposed vulnerabilities in "
            "the surveillance architecture the NSA relies upon."
        ),
        "year_start": 2024,
        "year_end": 2025,
        "sources": [1723, 1724],
    },
    # ========== NORD STREAM SABOTAGE ==========
    # NOTE: Nord Stream Sabotage Investigation resulted_from Russia–Ukraine War
    # edge deferred — that entity is created by the power agent. Add after:
    #   Nord Stream Sabotage Investigation -> Russia–Ukraine War (resulted_from,
    #   documented, [1726, 1727])
    {
        "source": "Vladimir Putin",
        "target": "Nord Stream Sabotage Investigation",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Russia is the primary affected party in the Nord Stream sabotage — the "
            "pipelines carried Russian natural gas to Europe. Putin repeatedly demanded "
            "international investigation. The destruction eliminated a major Russian "
            "economic and geopolitical lever over European energy markets."
        ),
        "year_start": 2022,
        "sources": [1726],
    },
    {
        "source": "FSB",
        "target": "Nord Stream Sabotage Investigation",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Russia's FSB opened its own criminal investigation into the pipeline sabotage. "
            "The German prosecution of Ukrainian suspects implicates a wartime covert action "
            "against critical infrastructure partly owned by Russian state-backed entities."
        ),
        "year_start": 2022,
        "sources": [1726, 1728],
    },
    # ========== MOSSAD / UNIT 8200 IRAN WAR CONNECTIONS ==========
    {
        "source": "Mossad",
        "target": "Operation Midnight Hammer",
        "type": "involved_in",
        "tier": "credible",
        "desc": (
            "Mossad deployed over 1,000 agents operating covertly inside Iranian territory "
            "during the June 2025 Israeli strikes (Operation Rising Lion), providing "
            "intelligence maps of air defense networks and commander locations that directly "
            "supported the subsequent U.S. B-2 strikes on nuclear facilities (Operation "
            "Midnight Hammer, June 22, 2025)."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1742],
    },
    {
        "source": "Mossad",
        "target": "Operation Roaring Lion",
        "type": "involved_in",
        "tier": "credible",
        "desc": (
            "Mossad provided intelligence support for the February 28, 2026 Israeli strikes "
            "(Operation Roaring Lion), conducted in coordination with U.S. Operation Epic "
            "Fury. Pre-war Mossad sabotage included the destruction of a mobile radar station "
            "in Isfahan on January 10, 2026, via a targeted drone strike launched from within "
            "city limits — consistent with ground agent operations."
        ),
        "year_start": 2026,
        "year_end": 2026,
        "sources": [1744],
    },
    {
        "source": "Unit 8200",
        "target": "Operation Midnight Hammer",
        "type": "involved_in",
        "tier": "credible",
        "desc": (
            "Unit 8200 launched cyberattacks and electronic warfare operations during the "
            "June 2025 strikes — jamming Iranian communications and radar, inserting fake IP "
            "addresses into Iran's telecom network (reportedly redirecting 73% of traffic), "
            "and paralyzing IRGC radar at critical moments. Iran retaliated by striking "
            "Unit 8200's base on June 17, 2025."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1743],
    },
    {
        "source": "Unit 8200",
        "target": "Operation Epic Fury",
        "type": "involved_in",
        "tier": "credible",
        "desc": (
            "Unit 8200 conducted 'Reflector' cyberattacks and targeted DDoS operations "
            "against Iranian jamming centers during Operation Epic Fury (February 2026). "
            "Coordinated U.S.-Israeli cyber operations disrupted Iranian command, control, "
            "and sensor networks ahead of airstrikes."
        ),
        "year_start": 2026,
        "year_end": 2026,
        "sources": [1744, 1743],
    },
    # ========== EPSTEIN INTELLIGENCE LAYER ==========
    {
        "source": "DEA",
        "target": "Jeffrey Epstein",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "A 69-page DEA memorandum (2015) revealed in the Epstein Files Transparency Act "
            "releases disclosed that Epstein was part of 'Operation Chain Reaction,' a "
            "five-year-plus investigation examining wire transfers of 15 individuals for "
            "suspicious money transfers possibly linked to illegal narcotics. Previously "
            "undisclosed. Senator Wyden pressed the DEA for details in February 2026."
        ),
        "year_start": 2010,
        "year_end": 2015,
        "sources": [1732, 1733, 1734],
    },
    # ========== STRUCTURAL / COORDINATION EDGES ==========
    {
        "source": "Office of the Director of National Intelligence",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The ODNI oversees the U.S. Intelligence Community. The CIA is one of 18 member "
            "agencies. The DNI coordinates budgets, collection priorities, and analysis "
            "across all IC agencies."
        ),
        "sources": [1702],
    },
    {
        "source": "SOUTHCOM",
        "target": "DEA",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "SOUTHCOM and DEA coordinate counter-narcotics operations throughout the Western "
            "Hemisphere. In Operation Southern Spear (2025-2026), DEA-originated indictments "
            "provided the legal basis for SOUTHCOM's military campaign against Venezuelan "
            "targets."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1716, 1720],
    },
    {
        "source": "SOUTHCOM",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "CIA and SOUTHCOM coordinated during Operation Southern Spear. CIA operatives "
            "provided ground intelligence for the Maduro capture, and the CIA conducted at "
            "least one drone strike on Venezuelan territory in December 2025."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1722],
    },
]

# ============================================================
# ENTITY → SOURCE mappings
# ============================================================

ENTITY_SOURCES = {
    "Office of the Director of National Intelligence": [1702, 1703],
    "Tulsi Gabbard": [1702, 1703, 1709, 1710],
    "John Ratcliffe": [1700, 1709, 1710],
    "Kash Patel": [1701, 1729],
    "Blaise Metreweli": [1704],
    "Nicolás Maduro": [1719, 1720, 1721],
    "SOUTHCOM": [1716, 1717],
    "Operation Southern Spear": [1716, 1717, 1718, 1719, 1720, 1721, 1722],
    "Signalgate": [1709, 1710, 1711, 1712],
    "Operation Grim Beeper": [1713, 1714, 1715],
    "Salt Typhoon Telecom Breach": [1723, 1724, 1725],
    "Nord Stream Sabotage Investigation": [1726, 1727, 1728],
}

# ============================================================
# ENTITY UPDATES — modifies EXISTING entities
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "CIA",
        "description_append": (
            "2025-2026 update: John Ratcliffe confirmed as 9th CIA Director on January 23, "
            "2025 (Senate vote 74-25). Under Ratcliffe, CIA operatives provided ground "
            "intelligence for Operation Southern Spear, tracking Venezuelan President "
            "Maduro's location ahead of his January 3, 2026 capture. The CIA conducted at "
            "least one drone strike on Venezuelan territory in December 2025. Ratcliffe was "
            "a participant in the March 2025 Signalgate group chat that exposed classified "
            "Houthi strike plans."
        ),
        "sources": [1700, 1722],
    },
    {
        "name": "FBI",
        "description_append": (
            "2025-2026 update: Kash Patel confirmed as 9th FBI Director on February 20, "
            "2025 (51-49 party-line vote), replacing Christopher Wray. In July 2025, the "
            "FBI co-authored a two-page memo with DOJ concluding there was no Epstein 'client "
            "list' and no evidence of blackmail — a finding that contradicted AG Bondi's prior "
            "assurances. The FBI suffered a major counterintelligence blow when China's Salt "
            "Typhoon operation exfiltrated 18 months of FBI wiretap data from compromised "
            "telecom CALEA infrastructure."
        ),
        "sources": [1701, 1729, 1725],
    },
    {
        "name": "NSA",
        "description_append": (
            "2025-2026 update: NSA Director Gen. Timothy Haugh was fired by President Trump "
            "on April 3, 2025, along with civilian deputy Wendy Noble. Lt. Gen. William "
            "Hartman served as acting USCYBERCOM commander, and Sheila Thomas as acting NSA "
            "deputy director. Gen. Joshua Rudd confirmed by the Senate in March 2026 (vote "
            "71-29) as permanent NSA Director and Commander of U.S. Cyber Command, maintaining "
            "the dual-hat arrangement. The Salt Typhoon breach exposed critical vulnerabilities "
            "in the CALEA wiretap infrastructure that underpins U.S. signals intelligence "
            "collection."
        ),
        "sources": [1705, 1706, 1723],
    },
    {
        "name": "Mossad",
        "description_append": (
            "2025-2026 update: Director David Barnea stepped down in June 2026 after five "
            "years. Maj.-Gen. Roman Gofman (Netanyahu's former military secretary) appointed "
            "as successor effective July 2, 2026, in a controversial selection. In September "
            "2024, Mossad orchestrated Operation Grim Beeper — a supply-chain sabotage "
            "operation that detonated thousands of pagers and walkie-talkies used by Hezbollah "
            "in Lebanon, killing 42 and wounding 3,500-4,000. During the June 2025 war, "
            "Mossad deployed over 1,000 agents inside Iran for intelligence support of "
            "Operations Rising Lion and Midnight Hammer. Continued intelligence operations "
            "supported Operation Roaring Lion in February 2026."
        ),
        "sources": [1707, 1708, 1713, 1742],
    },
    {
        "name": "MI6",
        "description_append": (
            "2025-2026 update: Blaise Metreweli became the 18th Chief of MI6 ('C') on "
            "October 1, 2025, succeeding Sir Richard Moore. The first woman to lead MI6 "
            "in its 116-year history. Metreweli joined MI6 in 1999, spent her early career "
            "in the Middle East, and previously served as Director General of Technology "
            "and Innovation ('Q')."
        ),
        "sources": [1704],
    },
    {
        "name": "Hezbollah",
        "description_append": (
            "2025-2026 update: Suffered its worst security breach since October 2023 when "
            "thousands of pagers and walkie-talkies used by operatives detonated on September "
            "17-18, 2024 (Operation Grim Beeper). 42 killed, 3,500-4,000 wounded, "
            "approximately 1,500 fighters taken out of action. The devices had been "
            "manufactured through a Mossad front company (BAC Consulting KFT, Budapest) "
            "with PETN explosive implanted in the batteries."
        ),
        "sources": [1713, 1714, 1715],
    },
    {
        "name": "NSO Group",
        "description_append": (
            "2025-2026 update: In May 2025, a jury ordered NSO Group to pay $167 million "
            "in punitive damages (plus $444K compensatory) to WhatsApp/Meta for using "
            "Pegasus to hack approximately 1,400 users. In October 2025, the judge reduced "
            "punitive damages to $4 million but granted a permanent injunction barring NSO "
            "from hacking WhatsApp, effective January 28, 2026. On October 10, 2025, NSO "
            "confirmed acquisition by a U.S. investor consortium led by Hollywood producer "
            "Robert Simonds, valued at tens of millions. Co-founder Omri Lavie stepped down. "
            "In June 2026, WhatsApp detected a fresh Pegasus campaign launched within days "
            "of the injunction and filed a federal contempt motion."
        ),
        "sources": [1735, 1736, 1737],
    },
    {
        "name": "Julian Assange",
        "description_append": (
            "2025-2026 update: On June 24, 2024, Assange left Belmarsh Prison after 1,901 "
            "days of detention. He flew to Saipan (U.S. territory) where he pleaded guilty "
            "to a single felony count under the Espionage Act — conspiring to obtain and "
            "disclose classified national defense information. Sentenced to 62 months (time "
            "served) and walked free. Arrived in Canberra, Australia on June 26, 2024 as a "
            "free man. On October 1, 2024, made his first public appearance at the Council "
            "of Europe's Parliamentary Assembly in Strasbourg, testifying: 'I am not free "
            "today because the system worked. I am free today after years of incarceration "
            "because I pled guilty to journalism.' Living in Australia as of 2026."
        ),
        "metadata": {"status": "active"},
        "sources": [1740, 1741],
    },
    {
        "name": "Edward Snowden",
        "description_append": (
            "2025-2026 update: Received Russian citizenship in September 2022 by presidential "
            "decree (had previously obtained permanent residency in 2020). Remains in Russia "
            "as of August 2026 and is still charged with multiple felonies in the U.S. under "
            "the Espionage Act. Has been largely absent from public life in 2025-2026. During "
            "DNI confirmation hearings, Tulsi Gabbard published an op-ed arguing 'traitor' "
            "was too harsh a word for Snowden, addressing concerns about her prior sympathetic "
            "statements. No pardon or change in legal status."
        ),
        "sources": [1703],
    },
    {
        "name": "Unit 8200",
        "description_append": (
            "2025-2026 update: Played a central cyberwarfare role in the 2025-2026 Iran wars. "
            "During the June 2025 strikes (Operation Rising Lion / Midnight Hammer), Unit "
            "8200 launched cyberattacks jamming Iranian communications and radar, inserted "
            "fake IP addresses into Iran's telecom network (reportedly redirecting 73% of "
            "traffic), and intercepted IRGC command communications. Iran retaliated by "
            "striking Unit 8200's base on June 17, 2025. During Operation Epic Fury / "
            "Roaring Lion (February 2026), Unit 8200 conducted 'Reflector' cyberattacks "
            "and targeted DDoS operations against Iranian jamming centers."
        ),
        "sources": [1743, 1744],
    },
    {
        "name": "DOJ",
        "description_append": (
            "2025-2026 update: In July 2025, DOJ and FBI released a two-page unsigned memo "
            "concluding there was no Epstein 'client list' and no evidence of blackmail, "
            "finding Epstein died by suicide. This contradicted AG Bondi's prior assurances. "
            "The Epstein Files Transparency Act (signed November 19, 2025) required DOJ to "
            "publish all unclassified Epstein-related records. By January 2026, DOJ had "
            "released over 3.5 million pages from five primary source collections. The "
            "releases revealed a previously undisclosed DEA investigation of Epstein "
            "(Operation Chain Reaction). DOJ also oversaw the prosecution of Nicolás Maduro "
            "following his January 2026 capture."
        ),
        "sources": [1729, 1731, 1720],
    },
    {
        "name": "DEA",
        "description_append": (
            "2025-2026 update: Epstein Files Transparency Act releases in 2026 disclosed "
            "a previously unknown DEA investigation of Jeffrey Epstein — 'Operation Chain "
            "Reaction,' a five-year-plus probe targeting Epstein and 14 others for suspicious "
            "wire transfers (4,725 transfers totaling $1.5 billion) possibly linked to illegal "
            "narcotics. A heavily redacted 69-page 2015 DEA memorandum was among the released "
            "documents. Senator Wyden pressed the DEA for answers in February 2026. The DEA "
            "also played a central role in the Maduro prosecution, with DEA-originated "
            "indictments providing the legal basis for Operation Southern Spear."
        ),
        "sources": [1732, 1733, 1734, 1720],
    },
    {
        "name": "FISA Amendments Act",
        "description_append": (
            "2025-2026 update: Section 702 was reauthorized on April 20, 2024, via the "
            "Reforming Intelligence and Securing America Act (RISAA) for two years — the "
            "shortest extension in the program's history. RISAA included a first-ever Fourth "
            "Amendment warrant requirement for FBI queries seeking U.S. persons' communications "
            "and prohibited FBI 'about' queries. When the two-year extension expired, Congress "
            "passed a 45-day clean extension in April 2026, pushing the deadline to June 12, "
            "2026. On June 11, 2026, the House voted 218-198 against reauthorization. Section "
            "702 lapsed at midnight June 12, 2026 — the first time the authority has expired "
            "since its 2008 enactment. Existing FISA Court certifications remain in force "
            "until March 2027, so collection continues under those authorizations."
        ),
        "sources": [1738, 1739],
    },
]

# ============================================================
# GEO_COORDS — for NEW entities only
# ============================================================

GEO_COORDS = {
    "Office of the Director of National Intelligence": (38.8602, -77.0595, "documented", "Liberty Crossing, McLean, Virginia"),
    "Tulsi Gabbard": (38.8977, -77.0365, "inference", "Washington, D.C."),
    "John Ratcliffe": (38.9531, -77.1465, "credible", "CIA HQ, Langley, Virginia"),
    "Kash Patel": (38.8977, -77.0365, "inference", "Washington, D.C."),
    "Blaise Metreweli": (51.4873, -0.1244, "credible", "SIS Building, Vauxhall Cross, London"),
    "Nicolás Maduro": (10.4806, -66.9036, "credible", "Caracas, Venezuela"),
    "SOUTHCOM": (25.8249, -80.3427, "documented", "Doral, Florida"),
    "Operation Southern Spear": (12.0, -68.0, "credible", "Caribbean Sea"),
    "Signalgate": (38.8977, -77.0365, "credible", "Washington, D.C."),
    "Operation Grim Beeper": (33.8938, 35.5018, "credible", "Beirut, Lebanon"),
    "Salt Typhoon Telecom Breach": (38.8977, -77.0365, "inference", "U.S. telecommunications infrastructure"),
    "Nord Stream Sabotage Investigation": (53.5511, 9.9937, "documented", "Hamburg, Germany (trial venue)"),
}

# ============================================================
# PHOTO_CANDIDATES — for NEW persons/orgs
# ============================================================

PHOTO_CANDIDATES = {
    "Tulsi Gabbard": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Director_Tulsi_Gabbard_Official_Portrait.jpg",
    "John Ratcliffe": "https://upload.wikimedia.org/wikipedia/commons/c/c0/John_Ratcliffe_official_photo.jpg",
    "Kash Patel": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Kash_Patel%2C_official_FBI_portrait_%28cropped_2%29.jpg",
    "Nicolás Maduro": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Nicol%C3%A1s_Maduro_in_2023_%28cropped%29.jpg",
    "SOUTHCOM": "https://upload.wikimedia.org/wikipedia/commons/0/05/Seal_of_the_United_States_Southern_Command.svg",
}
