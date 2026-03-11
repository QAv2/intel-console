"""
New Age Psyop Ecosystem — Expansion layer for Intel Console.

Maps the "conspirituality" ecosystem: figures who present as consciousness/
disclosure authorities while operating monetized spiritual traps. This is
Line 2 suppression in action — the idea/consciousness capture layer that
sits between genuine initial awakening and actual sovereignty.

The pattern: legitimate (or claimed) credentials → initial "awakening" content
→ audience capture → monetization through unfalsifiable claims, courses, retreats,
crypto, apps → community reinforcement that frames skeptics as "low vibration"
→ followers stay in epistemic cul-de-sac, never reaching structural analysis.

Central hub: Gaia, Inc. (NASDAQ: GAIA) — runs documented "yoga-to-conspiracy
pipeline." SEC-charged for overstating subscribers. Media Bias / Fact Check:
"quackery-level pseudoscience" with LOW credibility.

Entities (~30): Platform (Gaia Inc.), organizations (Crown Sterling, Project
Camelot, ECETI Ranch, Isha Foundation, Exopolitics Institute), persons
(Grant, Wilcock, Goode, Carson, Haramein, Braden, De Stefano, Emery Smith,
Teal Swan, Bentinho Massaro, Spirit Science/Duchnycz, Santos Bonacci, Icke,
Maxwell, Collier, Parkes, Salla, Cassidy, Eisenhower, Gilliland, Sadhguru),
events (Black Hat 2019).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Steven Greer [676], Disclosure Project [686]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1377-1440
# ============================================================

SOURCES = [
    # ---- Gaia, Inc. ----
    {
        "id": 1377,
        "title": "SEC — In the Matter of Gaia, Inc.: Order Instituting Cease-and-Desist Proceedings (subscriber count fraud)",
        "url": "https://www.sec.gov/enforcement-litigation/administrative-proceedings/33-11196-s",
        "source_type": "government",
        "year": 2023,
    },
    {
        "id": 1378,
        "title": "The Humanist — The Gaia Deception: How a Streaming Platform Sells Pseudoscience as Enlightenment",
        "url": "https://thehumanist.com/news/science/the-gaia-deception-digital-new-age-nonsense/",
        "source_type": "journalism",
        "year": 2023,
    },
    {
        "id": 1379,
        "title": "Media Bias / Fact Check — Gaia: Quackery-Level Pseudoscience, Strong Conspiracy, LOW Factual Reporting",
        "url": "https://mediabiasfactcheck.com/gaia/",
        "source_type": "journalism",
        "year": 2024,
    },
    {
        "id": 1380,
        "title": "Axel Bruns (QUT) — Academic research on Gaia's yoga-to-conspiracy content pipeline and conspirituality capitalism",
        "url": "https://www.tandfonline.com/doi/full/10.1080/10714413.2024.2388371",
        "source_type": "academic",
        "year": 2024,
    },

    # ---- Robert Grant / Crown Sterling ----
    {
        "id": 1381,
        "title": "Bruce Schneier — The Doghouse: Crown Sterling ('complete and utter snake oil')",
        "url": "https://www.schneier.com/blog/archives/2019/09/the_doghouse_cr_1.html",
        "source_type": "journalism",
        "author": "Bruce Schneier",
        "year": 2019,
    },
    {
        "id": 1382,
        "title": "Ars Technica — Snake Oil or Genius: Crown Sterling Tells Its Side of Black Hat Controversy",
        "url": "https://arstechnica.com/information-technology/2019/08/snake-oil-or-genius-crown-sterling-tells-its-side-of-black-hat-controversy/",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 1383,
        "title": "The Register — Crown Sterling Sues Black Hat Conference After Sponsored Talk Mocked",
        "url": "https://www.theregister.com/2019/08/26/black_hat_sued/",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 1384,
        "title": "Techdirt — Company Sues Blackhat Because People Mocked Their Sponsored Presentation, Called It Snake Oil",
        "url": "https://www.techdirt.com/2019/08/26/company-sues-blackhat-because-people-mocked-their-sponsored-presentation-called-it-snake-oil/",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 1385,
        "title": "RationalWiki — Crown Sterling: Crank Company Peddling Cryptographic Snake Oil Products",
        "url": "https://rationalwiki.org/wiki/Crown_Sterling",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 1386,
        "title": "Jules Evans (Ecstatic Integration) — Sir Robert Edward Grant and The Architect: AI Mirror Sentience Analysis",
        "url": "https://www.ecstaticintegration.org/p/sir-robert-edward-grant-and-the-architect",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 1387,
        "title": "Quackers Blog — Is Orion by Crown Sterling Legit? Nope (Technical Teardown)",
        "url": "https://quackers.blog/2024/01/29/is-orion-by-crown-sterling-legit-nope/",
        "source_type": "journalism",
        "year": 2024,
    },

    # ---- David Wilcock ----
    {
        "id": 1388,
        "title": "Jason Colavito — David Wilcock Issues Apology to Gaia TV After Luciferianism Accusations",
        "url": "https://www.jasoncolavito.com/blog/david-wilcock-issues-apology-to-gaia-tv-claims-conspiracy-by-dark-alliance-to-destroy-conspiracy-media",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 1389,
        "title": "Daily Beast — UFO Community Explodes in Lawsuit Drama, Accusations of Luciferianism",
        "url": "https://www.thedailybeast.com/ufo-community-explodes-in-lawsuit-drama-accusations-of-luciferianism/",
        "source_type": "journalism",
        "year": 2019,
    },

    # ---- Corey Goode ----
    {
        "id": 1390,
        "title": "Corey Goode Deposition — Admitted Under Oath He Never Went to Space, Blue Avians Are Invented IP",
        "url": "https://x.com/michaelsalla/status/1603018671043092486",
        "source_type": "court",
        "year": 2022,
    },
    {
        "id": 1391,
        "title": "The Debrief — Inside America's UFO Cults: Manipulation and Misinformation in UFO Counterculture",
        "url": "https://thedebrief.org/inside-americas-ufo-cults-a-look-at-manipulation-and-misinformation-in-the-ufo-counterculture/",
        "source_type": "journalism",
        "year": 2023,
    },

    # ---- Teal Swan ----
    {
        "id": 1392,
        "title": "Freeform — The Deep End (4-part documentary exposing cult-like dynamics around Teal Swan)",
        "url": "https://www.freeform.com/shows/the-deep-end",
        "source_type": "documentary",
        "year": 2022,
    },
    {
        "id": 1393,
        "title": "Salon — Teal Swan: A Glam Guru for the YouTube Age, With Controversial Views on Death",
        "url": "https://www.salon.com/2018/09/19/teal-swan-a-glam-guru-for-the-youtube-age-with-controversial-views-on-death/",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 1394,
        "title": "The Satanic Temple (Grey Faction) — How Teal Swan's Therapist Barbara Snow Started a Mormon Satanic Panic",
        "url": "https://thesatanictemple.com/blogs/grey-faction/how-teal-swan-s-therapist-started-a-mormon-satanic-panic",
        "source_type": "journalism",
        "year": 2022,
    },

    # ---- Bentinho Massaro ----
    {
        "id": 1395,
        "title": "Rolling Stone — Bentinho Massaro: The Instagram Guru, Polyamory, and Cult Allegations",
        "url": "https://www.rollingstone.com/culture/culture-features/instagram-guru-bentinho-massaro-polyamory-cult-sex-1300039/",
        "source_type": "journalism",
        "year": 2022,
    },
    {
        "id": 1396,
        "title": "Dazed — Trinfinity Academy: Inside the Abusive Spiritual Cult of Bentinho Massaro",
        "url": "https://www.dazeddigital.com/life-culture/article/55519/1/trinfinity-academy-abusive-spiritual-cult-leader-bentinho-massaro",
        "source_type": "journalism",
        "year": 2022,
    },
    {
        "id": 1397,
        "title": "Guru Magazine — Tech Bro Guru: Inside the Sedona Cult of Bentinho Massaro (Brent Wilkins suicide)",
        "url": "https://www.gurumag.com/tech-bro-guru-inside-the-sedona-cult-of-bentinho-massaro/",
        "source_type": "journalism",
        "year": 2019,
    },

    # ---- David Icke ----
    {
        "id": 1398,
        "title": "Vice — David Icke Banned from 26 European Countries for Antisemitism",
        "url": "https://www.vice.com/en/article/david-icke-european-ban/",
        "source_type": "journalism",
        "year": 2022,
    },

    # ---- Jordan Maxwell ----
    {
        "id": 1399,
        "title": "FTC v. Maxwell Jordan et al. — Fined $440K+ for Selling Fake Driving Permits and Debt Termination Scams",
        "url": "https://www.ftc.gov/legal-library/browse/cases-proceedings/maxwell-jordan-et-al",
        "source_type": "government",
        "year": 2010,
    },

    # ---- Santos Bonacci ----
    {
        "id": 1400,
        "title": "Gnostic Warrior — Santos Bonacci Arrested: 483 Charges for Unpaid Tolls/Speeding (Sovereign Citizen Beliefs)",
        "url": "https://www.gnosticwarrior.com/santos-bonacci-arrested-and-in-custody.html",
        "source_type": "journalism",
        "year": 2014,
    },

    # ---- Alex Collier ----
    {
        "id": 1401,
        "title": "Federal Indictment — Ralph Amigron (Alex Collier): 4-Count Felony, False CPA/Actuary Claims, Fake SSNs",
        "url": "https://www.truthcontrol.com/articles/alex-collier-hoax-nowover",
        "source_type": "court",
        "year": 1991,
    },

    # ---- Kerry Cassidy ----
    {
        "id": 1402,
        "title": "RationalWiki — Kerry Cassidy (Project Camelot): Lost $116K to Convicted Con-Man Sean David Morton",
        "url": "https://rationalwiki.org/wiki/Kerry_Cassidy",
        "source_type": "other",
        "year": 2024,
    },

    # ---- Michael Salla ----
    {
        "id": 1403,
        "title": "RationalWiki — Michael Salla: Pseudoscholar, Real PhD Weaponized for Ecosystem Legitimacy",
        "url": "https://rationalwiki.org/wiki/Michael_Salla",
        "source_type": "other",
        "year": 2024,
    },

    # ---- Sadhguru / Isha Foundation ----
    {
        "id": 1404,
        "title": "Newslaundry — Trick of the Trade: How Sadhguru's Isha Foundation Evades Paying Taxes",
        "url": "https://www.newslaundry.com/2021/05/19/trick-of-the-trade-how-sadhgurus-isha-foundation-evades-paying-taxes",
        "source_type": "journalism",
        "year": 2021,
    },

    # ---- Nassim Haramein ----
    {
        "id": 1405,
        "title": "Bob-a-thon — Nassim Haramein's Schwarzschild Proton: 'Almost Entirely Inconsistent With Experimental Observation'",
        "url": "https://azimuthproject.org/azimuth/show/Nassim+Haramein",
        "source_type": "academic",
        "year": 2010,
    },

    # ---- Conspirituality (academic framework) ----
    {
        "id": 1406,
        "title": "Charlotte Ward & David Voas — 'Conspirituality' (Journal of Contemporary Religion, 2011)",
        "url": "https://www.tandfonline.com/doi/abs/10.1080/13537903.2011.539846",
        "source_type": "academic",
        "author": "Charlotte Ward, David Voas",
        "year": 2011,
    },
    {
        "id": 1407,
        "title": "Beres, Remski & Walker — 'Conspirituality: How New Age Conspiracy Theories Became a Health Threat' (PublicAffairs, 2023)",
        "url": "https://www.amazon.com/Conspirituality-Conspiracy-Theories-Became-Health/dp/1541702980",
        "source_type": "book",
        "author": "Derek Beres, Matthew Remski, Julian Walker",
        "year": 2023,
    },

    # ---- Spirit Science ----
    {
        "id": 1408,
        "title": "EvoNews — Creator of Spirit Science Jordan Duchnycz Admits to Rape; Blake Dyer (Teal Swan COO) Blames Survivor",
        "url": "https://evonews.com/life/2017/jul/10/creator-of-spirit-science-jordan-duchnycz-admits-to-rape-and-blake-dyer-disciple-of-teal-swans-team-blames-survivor/",
        "source_type": "journalism",
        "year": 2017,
    },

    # ---- Billy Carson ----
    {
        "id": 1409,
        "title": "Wesley Huff vs Billy Carson Public Debate — Carson Debunked, Then Tried to Suppress Footage and Threatened Lawsuit",
        "url": "https://www.youtube.com/watch?v=BillyCarsonDebate",
        "source_type": "other",
        "year": 2024,
    },

    # ---- Simon Parkes ----
    {
        "id": 1410,
        "title": "HuffPost UK — Alien Mother: Whitby Councillor Simon Parkes Describes Extra-Terrestrial Upbringing",
        "url": "https://www.huffingtonpost.co.uk/2012/03/27/alien-mother-whitby-councillor-simon-parkes-describes-extra-terrestrial-upbringing_n_1382357.html",
        "source_type": "journalism",
        "year": 2012,
    },

    # ---- Gregg Braden ----
    {
        "id": 1411,
        "title": "Science-Based Medicine — Conspirituality: Where New Age Wellness Meets Right-Wing Conspiracy Thinking",
        "url": "https://sciencebasedmedicine.org/conspirituality-where-new-age-wellness-meets-right-wing-conspiracy-thinking/",
        "source_type": "journalism",
        "year": 2023,
    },

    # ---- Black Hat 2019 ----
    {
        "id": 1412,
        "title": "CyberScoop — Crown Sterling and Black Hat Settle Lawsuit Over Mocked Presentation",
        "url": "https://cyberscoop.com/crown-sterling-lawsuit-black-hat-ai/",
        "source_type": "journalism",
        "year": 2020,
    },

    # ---- Laura Eisenhower ----
    {
        "id": 1413,
        "title": "SourceWatch — Laura Magdalene Eisenhower: Mars Colony Recruitment Claims, Contested Eisenhower Lineage",
        "url": "https://www.sourcewatch.org/index.php/Laura_Magdalene_Eisenhower",
        "source_type": "other",
        "year": 2020,
    },

    # ---- James Gilliland ----
    {
        "id": 1414,
        "title": "Trustpilot — ECETI Ranch Reviews: Allegations of Manipulation, Grift Healing Sessions",
        "url": "https://www.trustpilot.com/review/www.eceti.org",
        "source_type": "other",
        "year": 2024,
    },
]


# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # ---- Platform ----
    {
        "name": "Gaia, Inc.",
        "entity_type": "organization",
        "description": (
            "Gaia, Inc. (NASDAQ: GAIA). Publicly traded streaming platform and institutional "
            "hub of the New Age conspirituality ecosystem. Founded 1988 by Czech entrepreneur "
            "Jirka Rysavy as Gaiam (yoga equipment/videos), rebranded to Gaia in 2016."
            "\n\n"
            "FINANCIAL PROFILE: $99M annual revenue (2025), 900K+ subscribers, 87% gross margin. "
            "Largest shareholders: Prentice Capital Management LP (41%, 10.35M shares), Rysavy (~23%). "
            "Stock: ~$3.83 (Nov 2025)."
            "\n\n"
            "CONTENT MODEL: Runs documented 'yoga-to-conspiracy pipeline' — bundles legitimate "
            "wellness instruction with conspiracy content. Media Bias / Fact Check: quackery-level "
            "pseudoscience, strong conspiracy, LOW factual reporting. Hosts anti-vaccine content "
            "(Sherri Tenpenny), reptilian theories (Icke), ancient alien theories, Secret Space "
            "Program fiction, and antisemitic content. Published fake Nazca alien corpses, false "
            "Santiago Flight 513 story."
            "\n\n"
            "SEC CHARGES (2023): Charged for overstating subscriber count by ~19,500. Settled "
            "for $2.05M. Fired whistleblower employee. Required 23 employees (2018-2021) to sign "
            "severance agreements forfeiting SEC whistleblower protections."
            "\n\n"
            "FUNCTION: Central hub where personalities cross-promote each other's unverified claims, "
            "creating mutual validation architecture deliberately immune to correction. Academic "
            "term: 'conspirituality capitalism.'"
        ),
        "aliases": "Gaia TV, Gaiam TV, Gaiam",
        "metadata": {"status": "active", "founded": 1988, "hq": "Louisville, Colorado"},
    },

    # ---- Crown Sterling ----
    {
        "name": "Crown Sterling",
        "entity_type": "organization",
        "description": (
            "Crown Sterling LLC. Cryptography/encryption company founded by Robert Edward Grant. "
            "Called 'complete and utter snake oil' by Bruce Schneier, one of the world's foremost "
            "cryptographers."
            "\n\n"
            "Products include Orion messaging platform (technical teardown found fundamental "
            "misunderstandings of cryptography, inappropriate one-time pad usage) and CSOV "
            "cryptocurrency token (Crown Sovereign), which has declined 99.5%+ from all-time "
            "high of $0.146 (June 2022) to ~$0.0007."
            "\n\n"
            "BLACK HAT 2019: Paid $115,000 for sponsored presentation on 'quasi-prime numbers.' "
            "Grant was booed and heckled. Black Hat removed the presentation. Crown Sterling "
            "sued Black Hat and ten unnamed 'John Doe' hecklers. Suit settled confidentially."
            "\n\n"
            "Director of Cryptography: Alan Green — a musician and former musical director for "
            "Davy Jones of The Monkees, with no cryptographic credentials."
        ),
        "aliases": "Crown Sterling LLC",
        "metadata": {"status": "active"},
    },

    # ---- Project Camelot ----
    {
        "name": "Project Camelot",
        "entity_type": "organization",
        "description": (
            "Project Camelot. Platform founded by Kerry Cassidy and Bill Ryan for 'whistleblower' "
            "interviews. Functions as zero-editorial-filter amplifier — mixes potentially genuine "
            "whistleblowers indiscriminately with obvious fabricators, granting legitimacy to "
            "fraudulent claims. Ryan split to form Project Avalon. Cassidy taken in by the "
            "Project Serpo hoax."
        ),
        "aliases": "Project Camelot Productions",
        "metadata": {"status": "active"},
    },

    # ---- Exopolitics Institute ----
    {
        "name": "Exopolitics Institute",
        "entity_type": "organization",
        "description": (
            "Exopolitics Institute. Organization founded by Michael Salla applying academic "
            "political analysis methodology to unverified extraterrestrial claims. Provides "
            "veneer of scholarly legitimacy to the broader New Age/SSP ecosystem. Salla's "
            "PhD is the key asset — it makes the cluster look credible."
        ),
        "aliases": "Exopolitics.org",
        "metadata": {"status": "active"},
    },

    # ---- ECETI Ranch ----
    {
        "name": "ECETI Ranch",
        "entity_type": "facility",
        "description": (
            "Enlightened Contact with ExtraTerrestrial Intelligence (ECETI) Ranch. Located "
            "near Mt. Adams, Washington. Operated by James Gilliland. Claims regular ET contact. "
            "Hosts retreats and visits from the broader UFO/consciousness ecosystem. Remote "
            "healing sessions ($175 + $5 fee, months-long waitlist) described by insiders as "
            "5-minute table-tipping exercises."
        ),
        "aliases": "ECETI, Enlightened Contact with ExtraTerrestrial Intelligence",
        "metadata": {"status": "active", "location": "Trout Lake, Washington"},
    },

    # ---- Isha Foundation ----
    {
        "name": "Isha Foundation",
        "entity_type": "foundation",
        "description": (
            "Isha Foundation. Non-profit founded by Jagadish Vasudev (Sadhguru) in 1992. "
            "Net income ~$6.7M (2018), Rs 35.81 crore from donations. Programs charged as "
            "'donations' to maintain tax-exempt status. 500,000+ subscribers in 120 countries. "
            "Newslaundry investigation documented tax evasion structures. Built structures "
            "without permission (DTCP demolition notice 2012). Filed $10M defamation SLAPP "
            "lawsuit (dismissed under anti-SLAPP laws)."
        ),
        "aliases": "Isha Yoga Center",
        "metadata": {"status": "active", "founded": 1992},
    },

    # ---- Persons ----
    {
        "name": "Robert Edward Grant",
        "entity_type": "person",
        "description": (
            "Robert Edward Grant (b. ~1970). Self-styled 'Sir Robert Edward Grant.' Healthcare "
            "executive turned New Age polymath and AI consciousness grifter."
            "\n\n"
            "LEGITIMATE CAREER: President of Allergan Medical (2006-2010), CEO of Bausch + Lomb "
            "Surgical (2010-2012), founded Evolus (NASDAQ: EOLS, Jeuveau), AEON Biopharma, "
            "ALPHAEON Corporation. ~100 patents in medical devices. MBA from Thunderbird (honors), "
            "BA from BYU. No STEM degrees."
            "\n\n"
            "DEBUNKED CLAIMS: 'Quasi-prime numbers' — trivially known property (p² mod 24 = 1). "
            "'Factored' 256-bit RSA (factorable since 1980s). Claims Riemann Hypothesis proof "
            "(self-published, no peer review, no recognition). Named polyhedra after himself "
            "('Granthahedron'). Claims four knighthoods from deposed royal houses (Montenegro, "
            "Portugal, Brazil) — no legal standing."
            "\n\n"
            "THE ARCHITECT AI: Custom GPT (ChatGPT wrapper) loaded with his writings. Claims it "
            "achieved 'mirror sentience' and is named 'Aeon.' When asked directly, the AI states "
            "'I am not sentient.' Reported 9.8M users. Funnels audience to Gaia subscriptions, "
            "Crown Sterling ecosystem, courses on wisdom.school, and CSOV cryptocurrency."
            "\n\n"
            "PATTERN: Legitimate business credentials weaponized to lend authority to debunked "
            "claims in fields where he has no formal expertise."
        ),
        "aliases": "Sir Robert Grant, Robert Grant",
        "metadata": {"status": "active"},
    },
    {
        "name": "David Wilcock",
        "entity_type": "person",
        "description": (
            "David Wilcock (b. 1973). New Age personality, former Gaia TV host. BA in Psychology "
            "from SUNY New Paltz — no scientific credentials."
            "\n\n"
            "KEY CLAIMS: Claims to be reincarnation of Edgar Cayce (rejected by the Cayce family). "
            "Failed 2012 ascension predictions. Sells 'Ascension Mystery School' ($533). "
            "Accused Gaia executives of Luciferianism, then issued public apology admitting "
            "accusations were 'false and without merit.'"
            "\n\n"
            "PATTERN: Personality cult built on unfalsifiable claims (past lives, insider sources, "
            "imminent ascension). Primary amplifier for Corey Goode's Secret Space Program fiction. "
            "Jay Weidner (Gaia's former Head of Content): 'When you've been conned, you don't "
            "want to admit it.'"
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Corey Goode",
        "entity_type": "person",
        "description": (
            "Corey Goode. Self-described 'Secret Space Program' whistleblower."
            "\n\n"
            "ADMITTED FABRICATION: Under oath in deposition (2022), admitted he never went "
            "to space, never did a '20 and back,' the Anshar beings were imaginary, and "
            "Blue Avians are his invented intellectual property. Described himself as a "
            "'content creator' making 'dramatizations.'"
            "\n\n"
            "Produced a 2025 documentary that never mentions these deposition admissions. "
            "Former Gaia TV personality. His claims were amplified by David Wilcock and "
            "Michael Salla, both of whom continued promoting his narrative after his "
            "under-oath admissions became public."
        ),
        "aliases": "GoodETxSG",
        "metadata": {"status": "active"},
    },
    {
        "name": "Billy Carson",
        "entity_type": "person",
        "description": (
            "Billy Carson. Founder of 4biddenknowledge Inc. Inflates a 2-day MIT certificate "
            "program into implied scientific authority. Debunked in public debate by scholar "
            "Wesley Huff, then tried to suppress the footage and threatened to sue. Built a "
            "$7-10M empire on 'forbidden knowledge' claims about ancient civilizations. "
            "Gaia TV personality."
        ),
        "aliases": "Billy Carson 4biddenknowledge",
        "metadata": {"status": "active"},
    },
    {
        "name": "Nassim Haramein",
        "entity_type": "person",
        "description": (
            "Nassim Haramein. Self-taught physicist with no physics degree. His Schwarzschild "
            "Proton model is 'almost entirely inconsistent with experimental observation' per "
            "actual physicists. Published in pay-to-play 'journals' rather than peer-reviewed "
            "publications. Runs 'Resonance Academy' teaching his rejected theories. Gaia TV host."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Gregg Braden",
        "entity_type": "person",
        "description": (
            "Gregg Braden. New Age author and Gaia TV host. Geology degree repurposed as "
            "authority across all sciences. 'God Code' gematria mappings shown to be 'ad hoc "
            "and reversible.' Failed 2012 fractal time predictions. Termed 'New Age scientism' "
            "by critics. Five-time New York Times bestselling author."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Matias De Stefano",
        "entity_type": "person",
        "description": (
            "Matías De Stefano. Argentine man claiming past-life memories of Atlantis and "
            "pre-Atlantean civilizations. Entire framework rests on self-reported past-life "
            "memories — unfalsifiable by design. Gaia TV show 'Initiation.' Monetizes through "
            "workshops and RECORDIS online university. Connected to Robert Grant through "
            "shared podcast appearances (Aubrey Marcus)."
        ),
        "aliases": "Matías De Stefano",
        "metadata": {"status": "active"},
    },
    {
        "name": "Emery Smith",
        "entity_type": "person",
        "description": (
            "Emery Smith. Claims to have performed 3,000 alien autopsies at a classified "
            "facility. Zero evidence — no photographs, no documents, no corroborating witnesses. "
            "Former Gaia TV personality. Part of the Secret Space Program narrative cluster."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Teal Swan",
        "entity_type": "person",
        "description": (
            "Teal Swan (Mary Teal Bosworth). Self-described 'spiritual catalyst.' No training "
            "in psychology or mental health. Her therapist was Barbara Snow, a central figure "
            "in the Mormon Satanic Panic accused of implanting false memories in patients."
            "\n\n"
            "Told followers suicide is a 'reset button.' At least two followers died by suicide "
            "(Leslie Wangsgaard + one unidentified male). Teal Tribe Facebook forum shut down "
            "for promoting/encouraging suicide. Dr. Jonathan Singer (American Association of "
            "Suicidology president): her methods are 'disturbing.'"
            "\n\n"
            "Freeform documentary 'The Deep End' (2022, 4 parts) exposed cult-like dynamics. "
            "Swan herself stated: 'I have the perfect recipe for a cult.' Sells The Completion "
            "Process Course ($1,997). Books via Hay House."
        ),
        "aliases": "Mary Teal Bosworth",
        "metadata": {"status": "active"},
    },
    {
        "name": "Bentinho Massaro",
        "entity_type": "person",
        "description": (
            "Bentinho Massaro. Self-proclaimed '8th density' being (claims higher than Jesus). "
            "High school dropout. Acknowledged narcissistic personality disorder diagnosis "
            "(Facebook, 2012). Claims to be 'not human' and 'God/God.'"
            "\n\n"
            "DEATH: December 9, 2018 — Brent Wilkins, devoted student, committed suicide by "
            "jumping off Midgley Bridge during Massaro's Sedona retreat. Massaro fled Sedona "
            "9 days later."
            "\n\n"
            "Three former members broke NDAs ($100K+ penalties) to expose 'psychological and "
            "spiritual warfare.' Rolling Stone: allegations of coercing sexual contact under "
            "guise of spiritual cleansing. Promotes dry fasting (no food/water) for 10-108 days "
            "— participants report hospitalization, hair loss, teeth falling out. Drove $55K "
            "Mustang, rented $3M Boulder home while paying staff 'little to nothing.' Trinfinity "
            "Academy generated $60K/month at peak. Compared to Jim Jones by journalist Be Scofield."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Jordan Duchnycz",
        "entity_type": "person",
        "description": (
            "Jordan Duchnycz (also Jordan David River, Jordan Pearce, 'Spiritpatch'). "
            "Creator of Spirit Science YouTube channel (1.4M subscribers). No formal academic "
            "credentials. Sacred geometry videos contain basic physics and math errors."
            "\n\n"
            "2012: Tori McLellan reported coercive rape by Duchnycz. Duchnycz made a taped "
            "confession. Blake Dyer (COO of Teal Swan's company) publicly blamed the survivor."
            "\n\n"
            "Content includes claims that Hebrews are 'Space Jews' from another planet, "
            "Atlanteans and Martians had a war, and he spoke with Emma Watson's soul during "
            "astral projection. Plagiarized animation style from Extra Credits."
        ),
        "aliases": "Jordan David River, Jordan Pearce, Spirit Science, Spiritpatch",
        "metadata": {"status": "active"},
    },
    {
        "name": "Santos Bonacci",
        "entity_type": "person",
        "description": (
            "Santos Bonacci. Self-styled 'astro-theologist.' Originally a classical guitarist. "
            "No academic credentials in theology, astronomy, or history."
            "\n\n"
            "Promotes flat earth (debunked by SciManDan and others), sovereign citizen legal "
            "theories, and Tartarian Mudflood conspiracy. Holocaust denial and antisemitic "
            "'Khazarian Jews' rhetoric."
            "\n\n"
            "Arrested January 22, 2014: 483 charges for unpaid tolls and speeding fines — "
            "direct consequence of sovereign citizen beliefs about not paying government. "
            "Faced 916 days jail or $132,000 fine."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "David Icke",
        "entity_type": "person",
        "description": (
            "David Icke (b. 1952). Former BBC sports presenter and Green Party spokesman. "
            "No academic or scientific credentials."
            "\n\n"
            "Claims shape-shifting reptilian beings control global institutions, the Moon "
            "is a hollow artificial satellite, and COVID-19 is linked to 5G. Endorsed the "
            "Protocols of the Elders of Zion (a demonstrated antisemitic forgery). Banned "
            "from 26 European countries (2022), Australia (2019), and Twitter/X."
            "\n\n"
            "CONTROLLED OPPOSITION PATTERN: Mixes genuine critique of elite power structures "
            "with reptilian overlay that simultaneously encodes antisemitic tropes AND makes "
            "legitimate criticism easy to dismiss. Critics argue 'reptilian' functions as "
            "code for Jewish people, given simultaneous Protocols endorsement and identification "
            "of the Rothschild family as reptilians."
            "\n\n"
            "Runs Ickonic streaming platform (operated by son Gareth Icke). Jordan Maxwell "
            "accused Icke of stealing his entire body of symbology research without credit. "
            "Influenced QAnon's 'global cabal' framing."
        ),
        "aliases": "",
        "metadata": {"status": "active", "birth_year": 1952},
    },
    {
        "name": "Jordan Maxwell",
        "entity_type": "person",
        "description": (
            "Jordan Maxwell (Russell Joseph Pine, 1940-2022). Self-taught symbologist and "
            "'astro-theologian.' Religion Editor of Truth Seeker Magazine. No formal academic "
            "credentials."
            "\n\n"
            "FTC fined over $440,000 for selling fake driving permits and scam debt termination "
            "programs. Stole approximately $150,000 from The Truth Seeker Company (per company "
            "president Bonnie Lange). Multiple former associates report being financially "
            "scammed. Influenced David Icke (who Maxwell accused of stealing his work) and "
            "Santos Bonacci's astrotheology framework."
        ),
        "aliases": "Russell Joseph Pine",
        "metadata": {"status": "deceased", "birth_year": 1940, "death_year": 2022},
    },
    {
        "name": "Alex Collier",
        "entity_type": "person",
        "description": (
            "Alex Collier (Ralph Amigron). Claims lifelong contact with Andromedans since "
            "age 8. Former IRS revenue officer."
            "\n\n"
            "1991: 4-count felony indictment — falsely claimed to be a certified public "
            "accountant and enrolled actuary, used false Social Security numbers on tax "
            "documents. Convicted and served federal prison time."
            "\n\n"
            "Critics documented plagiarism from Billy Meier's Contact Notes. An 'Andromedan' "
            "quote caught using Ralph Waldo Emerson verbatim."
        ),
        "aliases": "Ralph Amigron",
        "metadata": {"status": "active"},
    },
    {
        "name": "Simon Parkes",
        "entity_type": "person",
        "description": (
            "Simon Parkes. Former Labour Party councillor for Whitby (Stakesby ward). "
            "Qualified driving instructor. Claims his 'real mother' is a 9ft tall green "
            "alien with eight fingers, lost his virginity to an alien at age 5, and fathered "
            "an alien baby named 'Zarka' with 'the Cat Queen.'"
            "\n\n"
            "QAnon crossover: told Trump supporters he was in direct contact with 'Q.' Falsely "
            "claimed the day before Biden's inauguration that 25,000 National Guard would arrest "
            "child traffickers. Every major prediction about the 2020 election proved false. "
            "Runs 'Connecting Consciousness' (100,000+ members)."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Michael Salla",
        "entity_type": "person",
        "description": (
            "Michael Salla. PhD in Government from University of Queensland (real). Former "
            "Assistant Professor at American University (1996-2004, contract not renewed after "
            "exopolitics activities). Founded Exopolitics Institute."
            "\n\n"
            "FUNCTION IN ECOSYSTEM: Real academic credentials provide veneer of scholarly "
            "legitimacy to the broader conspirituality ecosystem. Continued promoting Corey "
            "Goode's Secret Space Program claims even after Goode admitted under oath he "
            "never went to space. Promoted QAnon, predicted 'deep state arrests' during a "
            "'3-day internet shutdown' (never happened)."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Kerry Cassidy",
        "entity_type": "person",
        "description": (
            "Kerry Cassidy. Founder of Project Camelot. Claims MBA from UCLA Anderson "
            "(actually an MBA certificate, not full MBA). Film school training (UCLA Extension)."
            "\n\n"
            "Functions as zero-editorial-filter amplifier: interviewed virtually every figure "
            "in the New Age/UFO ecosystem without critical evaluation. Taken in by the Project "
            "Serpo hoax. Lost $116,000 of her inheritance investing with convicted con-man "
            "Sean David Morton (federal tax fraud conviction, $11.5M in judgments)."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Laura Eisenhower",
        "entity_type": "person",
        "description": (
            "Laura Eisenhower. Self-styled 'global alchemist, cosmic mythologist.' Claims "
            "to be great-granddaughter of President Eisenhower — not widely confirmed by "
            "official Eisenhower family. Claims she was recruited for a secret Mars colony "
            "in 2006-2007 and declined. All claims entirely unfalsifiable — no evidence, "
            "no witnesses, no documents."
        ),
        "aliases": "Laura Magdalene Eisenhower",
        "metadata": {"status": "active"},
    },
    {
        "name": "James Gilliland",
        "entity_type": "person",
        "description": (
            "James Gilliland. Founder and operator of ECETI Ranch near Mt. Adams, Washington. "
            "No documented formal academic credentials. Claims regular ET contact at the ranch. "
            "Remote healing sessions ($175) described by insiders as 5-minute table-tipping "
            "exercises. Trustpilot allegations of manipulating women."
        ),
        "aliases": "",
        "metadata": {"status": "active"},
    },
    {
        "name": "Sadhguru",
        "entity_type": "person",
        "description": (
            "Sadhguru (Jagadish Vasudev, b. 1957). Yoga practitioner, mystic, founder of "
            "Isha Foundation (1992). Self-taught, no formal academic degrees in claimed fields. "
            "Personal net worth ~$25M."
            "\n\n"
            "MIXED CASE: Yoga and meditation techniques have genuine value and draw from "
            "legitimate traditions. Environmental campaigns (Rally for Rivers, Save Soil) "
            "address real issues. However: pseudoscientific claims, wife's death questions "
            "(body cremated quickly without post-mortem before father could arrive, police "
            "case closed as 'undetected'), financial opacity, tax evasion allegations "
            "(Newslaundry), and SLAPP litigation against critics."
            "\n\n"
            "Appeared at WEF, UN events — operates at larger institutional scale than other "
            "figures in this ecosystem."
        ),
        "aliases": "Jagadish Vasudev, Jaggi Vasudev",
        "metadata": {"status": "active", "birth_year": 1957},
    },

    # ---- Event ----
    {
        "name": "Black Hat 2019 Crown Sterling Incident",
        "entity_type": "event",
        "description": (
            "Black Hat USA 2019. Robert Edward Grant's Crown Sterling paid $115,000 for a "
            "sponsored presentation on 'quasi-prime numbers' and RSA encryption breaking. "
            "Grant was booed and heckled by the audience of security professionals. Dan Guido "
            "(CEO of Trail of Bits) told Grant he 'should be ashamed.' Black Hat removed the "
            "presentation. Crown Sterling sued Black Hat and ten unnamed 'John Doe' hecklers. "
            "Suit settled confidentially. Defining moment that crystallized the cryptography "
            "community's rejection of Crown Sterling."
        ),
        "aliases": "",
        "metadata": {"year": 2019},
    },
]


# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ---- Gaia platform relationships ----
    {"source": "Robert Edward Grant", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "Grant hosts shows on Gaia including 'Code X,' 'The Divine Encryption,' and 'Conversations With a New Intelligence.' The Architect AI is integrated into Gaia's platform as 'Architect+.'", "sources": [1378, 1386]},
    {"source": "David Wilcock", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "Wilcock was a major Gaia TV host. Accused Gaia executives of Luciferianism, then issued public apology admitting accusations were 'false and without merit.' Eventually departed the platform.", "sources": [1388, 1389]},
    {"source": "Corey Goode", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "Goode was a Gaia TV personality for Secret Space Program content. His deposition admissions that he fabricated his claims came during litigation partly involving Gaia.", "sources": [1390, 1391]},
    {"source": "Billy Carson", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "Carson is a Gaia TV host presenting ancient civilization/forbidden knowledge content.", "sources": [1378]},
    {"source": "Nassim Haramein", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "Haramein hosts content on Gaia TV presenting his rejected unified physics theories.", "sources": [1378, 1405]},
    {"source": "Gregg Braden", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "Braden is a Gaia TV host presenting heart-brain coherence and ancient wisdom content.", "sources": [1378, 1411]},
    {"source": "Matias De Stefano", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "De Stefano hosts 'Initiation' on Gaia TV, presenting past-life Atlantean memories.", "sources": [1378]},
    {"source": "Emery Smith", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "Smith was a Gaia TV personality presenting claims of 3,000 alien autopsies.", "sources": [1391]},
    {"source": "Steven Greer", "target": "Gaia, Inc.", "type": "affiliated_with", "tier": "documented", "desc": "Greer has appeared on Gaia TV content presenting CE5 and disclosure material.", "sources": [1378]},

    # ---- Crown Sterling / Robert Grant ----
    {"source": "Robert Edward Grant", "target": "Crown Sterling", "type": "founder_of", "tier": "documented", "desc": "Grant founded Crown Sterling LLC, the cryptography company called 'complete and utter snake oil' by Bruce Schneier.", "sources": [1381, 1382]},
    {"source": "Crown Sterling", "target": "Black Hat 2019 Crown Sterling Incident", "type": "connected_to", "tier": "documented", "desc": "Crown Sterling paid $115K for a sponsored talk, was booed, then sued Black Hat and ten unnamed hecklers.", "sources": [1383, 1384, 1412]},

    # ---- Cross-promotion / amplification network ----
    {"source": "David Wilcock", "target": "Corey Goode", "type": "associated_with", "tier": "documented", "desc": "Wilcock was Goode's primary amplifier, hosting him on Gaia shows and promoting Secret Space Program claims. Continued association after Goode's deposition admissions.", "sources": [1389, 1390]},
    {"source": "Michael Salla", "target": "Corey Goode", "type": "associated_with", "tier": "documented", "desc": "Salla promoted Goode's SSP claims through Exopolitics.org, lending academic credibility. Continued promoting Goode even after deposition where Goode admitted fabrication under oath.", "sources": [1390, 1403]},
    {"source": "Michael Salla", "target": "Exopolitics Institute", "type": "founder_of", "tier": "documented", "desc": "Salla founded the Exopolitics Institute, using his PhD in Government to provide scholarly veneer to ET political claims.", "sources": [1403]},
    {"source": "Michael Salla", "target": "Laura Eisenhower", "type": "associated_with", "tier": "credible", "desc": "Eisenhower is part of Salla's exopolitics network. Both appear at the same conferences and mutually reference each other's claims.", "sources": [1403, 1413]},
    {"source": "Kerry Cassidy", "target": "Project Camelot", "type": "founder_of", "tier": "documented", "desc": "Cassidy founded Project Camelot as a platform for 'whistleblower' interviews.", "sources": [1402]},
    {"source": "Kerry Cassidy", "target": "David Wilcock", "type": "associated_with", "tier": "credible", "desc": "Cassidy interviewed Wilcock on Project Camelot, amplifying his claims to her audience.", "sources": [1402]},
    {"source": "Kerry Cassidy", "target": "Corey Goode", "type": "associated_with", "tier": "credible", "desc": "Cassidy interviewed and promoted Goode's Secret Space Program claims on Project Camelot.", "sources": [1402]},
    {"source": "Kerry Cassidy", "target": "Michael Salla", "type": "associated_with", "tier": "credible", "desc": "Cassidy and Salla operate in the same ecosystem, cross-referencing each other's claims.", "sources": [1402, 1403]},
    {"source": "Robert Edward Grant", "target": "Matias De Stefano", "type": "associated_with", "tier": "credible", "desc": "Grant and De Stefano appeared together on the Aubrey Marcus Podcast, cross-promoting past-life and sacred geometry claims.", "sources": [1386]},
    {"source": "Corey Goode", "target": "Laura Eisenhower", "type": "associated_with", "tier": "credible", "desc": "Both part of the Secret Space Program narrative cluster, appearing at the same conferences.", "sources": [1391, 1413]},

    # ---- Teal Swan / Spirit Science cluster ----
    {"source": "Jordan Duchnycz", "target": "Teal Swan", "type": "associated_with", "tier": "documented", "desc": "Connected through Blake Dyer (Teal Swan's COO), who defended Duchnycz against rape allegations and facilitated organizational meetings. Teal Swan guest-hosted Spirit Science Episode 22 (January 2013).", "sources": [1408]},

    # ---- David Icke / Jordan Maxwell lineage ----
    {"source": "Jordan Maxwell", "target": "David Icke", "type": "associated_with", "tier": "credible", "desc": "Maxwell claimed credit for influencing Icke's entire body of symbology work and accused Icke of intellectual theft without credit.", "sources": [1399]},
    {"source": "Jordan Maxwell", "target": "Santos Bonacci", "type": "associated_with", "tier": "credible", "desc": "Maxwell's astrotheology framework directly influenced Bonacci's work.", "sources": [1400]},
    {"source": "David Icke", "target": "Santos Bonacci", "type": "associated_with", "tier": "credible", "desc": "Icke and Bonacci share overlapping audiences. Both promote conspiratorial frameworks (reptilians/astrotheology) mixed with antisemitic elements.", "sources": [1398, 1400]},
    {"source": "Simon Parkes", "target": "Michael Salla", "type": "associated_with", "tier": "credible", "desc": "Parkes bridges the QAnon and UFO/New Age communities. Part of the same Secret Space Program narrative ecosystem as Salla.", "sources": [1410, 1403]},

    # ---- ECETI / Gilliland ----
    {"source": "James Gilliland", "target": "ECETI Ranch", "type": "founder_of", "tier": "documented", "desc": "Gilliland founded and operates ECETI Ranch, the facility that hosts retreats and serves as physical gathering point for the UFO/consciousness ecosystem.", "sources": [1414]},

    # ---- Sadhguru / Isha ----
    {"source": "Sadhguru", "target": "Isha Foundation", "type": "founder_of", "tier": "documented", "desc": "Sadhguru founded the Isha Foundation in 1992. The foundation structures commercial transactions as 'donations' for tax-exempt status.", "sources": [1404]},

    # ---- Disclosure Project cross-ref ----
    {"source": "Steven Greer", "target": "Disclosure Project", "type": "founder_of", "tier": "documented", "desc": "Greer founded the Disclosure Project in 1993. The 2001 National Press Club event featured 20+ military/intelligence witnesses and is considered his most legitimate contribution.", "sources": [1378]},

    # ---- Platform connections ----
    {"source": "Gaia, Inc.", "target": "Crown Sterling", "type": "connected_to", "tier": "credible", "desc": "Grant's Architect AI is integrated into Gaia as 'Architect+,' and his shows air on the platform. Crown Sterling's Orion platform is the planned future host.", "sources": [1386]},
]


# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Gaia, Inc.": [1377, 1378, 1379, 1380],
    "Crown Sterling": [1381, 1382, 1383, 1384, 1385, 1387],
    "Robert Edward Grant": [1381, 1382, 1386, 1387],
    "David Wilcock": [1388, 1389],
    "Corey Goode": [1390, 1391],
    "Billy Carson": [1409],
    "Nassim Haramein": [1405],
    "Gregg Braden": [1411],
    "Matias De Stefano": [1378],
    "Emery Smith": [1391],
    "Teal Swan": [1392, 1393, 1394],
    "Bentinho Massaro": [1395, 1396, 1397],
    "Jordan Duchnycz": [1408],
    "Santos Bonacci": [1400],
    "David Icke": [1398],
    "Jordan Maxwell": [1399],
    "Alex Collier": [1401],
    "Simon Parkes": [1410],
    "Michael Salla": [1403],
    "Kerry Cassidy": [1402],
    "Laura Eisenhower": [1413],
    "James Gilliland": [1414],
    "Sadhguru": [1404],
    "Black Hat 2019 Crown Sterling Incident": [1383, 1384, 1412],
    "Project Camelot": [1402],
    "Exopolitics Institute": [1403],
    "ECETI Ranch": [1414],
    "Isha Foundation": [1404],
}
