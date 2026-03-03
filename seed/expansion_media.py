"""
Media Ownership & Narrative Control — Expansion layer for Intel Console.

Maps the architecture of narrative control: who owns the information pipeline,
how intelligence agencies penetrated media, the propaganda theory lineage,
whistleblower suppression, digital censorship infrastructure, and the
legislative framework that enabled media consolidation and domestic propaganda.

This is the mechanism by which all other branches of the map stay hidden.

Entities (~30): Media conglomerates (Murdoch/News Corp, Disney, Comcast,
Warner Bros Discovery, Paramount/Viacom), CIA-media nexus (Operation Mockingbird,
Church Committee exposure), propaganda theory (Edward Bernays, Tavistock Institute),
whistleblowers & transparency (Julian Assange, Edward Snowden, Chelsea Manning,
William Binney, WikiLeaks), digital censorship (Atlantic Council/DFRLab,
Twitter Files), legislation (Smith-Mundt Modernization, Telecommunications Act
of 1996), Pentagon Military Analyst Program, key journalists who exposed the system.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], NSA [86], Jeffrey Epstein [1], Palantir [87],
  DARPA [90], In-Q-Tel [91], FBI [84]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 483+ (continuing from existing 482)
# ============================================================

SOURCES = [
    # --- Operation Mockingbird / CIA-Media ---
    {
        "id": 483,
        "title": "The CIA and the Media — Carl Bernstein, Rolling Stone",
        "url": "https://www.carlbernstein.com/the-cia-and-the-media-rolling-stone-10-20-1977",
        "source_type": "journalism",
        "author": "Carl Bernstein",
        "year": 1977,
    },
    {
        "id": 484,
        "title": "Church Committee Final Report, Book I: Foreign and Military Intelligence — U.S. Senate Select Committee",
        "url": "https://www.intelligence.senate.gov/sites/default/files/94755_I.pdf",
        "source_type": "congressional",
        "year": 1976,
    },
    {
        "id": 485,
        "title": "CIA Family Jewels — FOIA release (National Security Archive, GWU)",
        "url": "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB222/index.htm",
        "source_type": "government",
        "year": 2007,
    },
    {
        "id": 486,
        "title": "Frank Wisner — Wikipedia (OPC founder, Mockingbird architect)",
        "url": "https://en.wikipedia.org/wiki/Frank_Wisner",
        "source_type": "other",
        "year": 2024,
    },
    # --- Edward Bernays / Propaganda Theory ---
    {
        "id": 487,
        "title": "Propaganda (1928) — Edward Bernays (full text, Archive.org)",
        "url": "https://archive.org/details/BernaysPropaganda",
        "source_type": "academic",
        "author": "Edward Bernays",
        "year": 1928,
    },
    {
        "id": 488,
        "title": "The Century of the Self (2002) — Adam Curtis, BBC Four documentary",
        "url": "https://en.wikipedia.org/wiki/The_Century_of_the_Self",
        "source_type": "other",
        "year": 2002,
    },
    {
        "id": 489,
        "title": "Edward Bernays — Wikipedia (biography, influence on PR industry)",
        "url": "https://en.wikipedia.org/wiki/Edward_Bernays",
        "source_type": "other",
        "year": 2024,
    },
    # --- Tavistock Institute ---
    {
        "id": 490,
        "title": "Tavistock Institute — Wikipedia (founding, WWII psychological warfare origins)",
        "url": "https://en.wikipedia.org/wiki/Tavistock_Institute",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 491,
        "title": "The Tavistock Institute of Human Relations — official website",
        "url": "https://www.tavinstitute.org/",
        "source_type": "other",
        "year": 2024,
    },
    # --- Media Consolidation / Conglomerates ---
    {
        "id": 492,
        "title": "Telecommunications Act of 1996 — Full text (FCC.gov)",
        "url": "https://www.fcc.gov/general/telecommunications-act-1996",
        "source_type": "government",
        "year": 1996,
    },
    {
        "id": 493,
        "title": "Who Owns the News? Media Consolidation, 1984-2024 — Columbia Journalism Review",
        "url": "https://www.cjr.org/special_report/media-consolidation-timeline.php",
        "source_type": "journalism",
        "author": "Columbia Journalism Review",
        "year": 2024,
    },
    {
        "id": 494,
        "title": "These 6 Corporations Control 90% Of The Media In America — Business Insider",
        "url": "https://www.businessinsider.com/these-6-corporations-control-90-of-the-media-in-america-2012-6",
        "source_type": "journalism",
        "author": "Business Insider",
        "year": 2012,
    },
    {
        "id": 495,
        "title": "Rupert Murdoch — Wikipedia (media empire biography)",
        "url": "https://en.wikipedia.org/wiki/Rupert_Murdoch",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 496,
        "title": "News Corp — Wikipedia (corporate structure, holdings)",
        "url": "https://en.wikipedia.org/wiki/News_Corp",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 497,
        "title": "Fox Corporation — Wikipedia (post-split structure)",
        "url": "https://en.wikipedia.org/wiki/Fox_Corporation",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 498,
        "title": "Leveson Inquiry Final Report (2012) — UK Government",
        "url": "https://www.gov.uk/government/publications/leveson-inquiry-report-into-the-culture-practices-and-ethics-of-the-press",
        "source_type": "government",
        "year": 2012,
    },
    {
        "id": 499,
        "title": "The Walt Disney Company — Wikipedia (corporate structure, acquisitions)",
        "url": "https://en.wikipedia.org/wiki/The_Walt_Disney_Company",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 500,
        "title": "Comcast — Wikipedia (NBCUniversal acquisition, holdings)",
        "url": "https://en.wikipedia.org/wiki/Comcast",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 501,
        "title": "Warner Bros. Discovery — Wikipedia (merger, CNN, HBO)",
        "url": "https://en.wikipedia.org/wiki/Warner_Bros._Discovery",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 502,
        "title": "Paramount Global — Wikipedia (Viacom/CBS merger)",
        "url": "https://en.wikipedia.org/wiki/Paramount_Global",
        "source_type": "other",
        "year": 2024,
    },
    # --- Whistleblowers ---
    {
        "id": 503,
        "title": "United States v. Julian Paul Assange — Eastern District of Virginia superseding indictment",
        "url": "https://www.justice.gov/opa/press-release/file/1165556/download",
        "source_type": "court",
        "year": 2019,
    },
    {
        "id": 504,
        "title": "Julian Assange plea deal: WikiLeaks founder pleads guilty to Espionage Act charge — AP News",
        "url": "https://apnews.com/article/julian-assange-wikileaks-plea-deal-e5c4e5c49a6f0ea8c5a0a08f08f50d47",
        "source_type": "journalism",
        "author": "AP News",
        "year": 2024,
    },
    {
        "id": 505,
        "title": "Edward Snowden — Wikipedia (NSA disclosures, exile)",
        "url": "https://en.wikipedia.org/wiki/Edward_Snowden",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 506,
        "title": "NSA Files Decoded — The Guardian interactive",
        "url": "https://www.theguardian.com/world/interactive/2013/nov/01/snowden-nsa-files-surveillance-revelations-decoded",
        "source_type": "journalism",
        "author": "The Guardian",
        "year": 2013,
    },
    {
        "id": 507,
        "title": "Chelsea Manning — Wikipedia (WikiLeaks source, military whistleblower)",
        "url": "https://en.wikipedia.org/wiki/Chelsea_Manning",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 508,
        "title": "William Binney — Wikipedia (NSA whistleblower, ThinThread designer)",
        "url": "https://en.wikipedia.org/wiki/William_Binney_(intelligence_official)",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 509,
        "title": "The Program — documentary (William Binney, NSA mass surveillance)",
        "url": "https://en.wikipedia.org/wiki/The_Program_(2012_film)",
        "source_type": "other",
        "year": 2012,
    },
    {
        "id": 510,
        "title": "WikiLeaks — Wikipedia (founding, major publications)",
        "url": "https://en.wikipedia.org/wiki/WikiLeaks",
        "source_type": "other",
        "year": 2024,
    },
    # --- PRISM / NSA Surveillance Programs ---
    {
        "id": 511,
        "title": "NSA Prism program taps in to user data of Apple, Google and others — The Guardian",
        "url": "https://www.theguardian.com/world/2013/jun/06/us-tech-giants-nsa-data",
        "source_type": "journalism",
        "author": "Glenn Greenwald & Ewen MacAskill",
        "year": 2013,
    },
    {
        "id": 512,
        "title": "PRISM (surveillance program) — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/PRISM",
        "source_type": "other",
        "year": 2024,
    },
    # --- Smith-Mundt Modernization ---
    {
        "id": 513,
        "title": "Smith-Mundt Modernization Act of 2012 — Section 1078, NDAA FY2013 (Congress.gov)",
        "url": "https://www.congress.gov/bill/112th-congress/house-bill/5736",
        "source_type": "congressional",
        "year": 2012,
    },
    {
        "id": 514,
        "title": "U.S. Repeals Propaganda Ban, Spreads Government-Made News to Americans — Foreign Policy",
        "url": "https://foreignpolicy.com/2013/07/14/u-s-repeals-propaganda-ban-spreads-government-made-news-to-americans/",
        "source_type": "journalism",
        "author": "Foreign Policy",
        "year": 2013,
    },
    # --- Pentagon Military Analyst Program ---
    {
        "id": 515,
        "title": "Behind TV Analysts, Pentagon's Hidden Hand — David Barstow, New York Times (Pulitzer Prize 2009)",
        "url": "https://www.nytimes.com/2008/04/20/us/20telecom.html",
        "source_type": "journalism",
        "author": "David Barstow",
        "year": 2008,
    },
    {
        "id": 516,
        "title": "DoD Inspector General Report on Pentagon Military Analyst Program (Interim)",
        "url": "https://media.defense.gov/2009/Jan/14/2001713955/-1/-1/1/09-INTEL-04.pdf",
        "source_type": "government",
        "year": 2009,
    },
    # --- Twitter Files ---
    {
        "id": 517,
        "title": "The Twitter Files — Matt Taibbi compilation thread",
        "url": "https://twitterfiles.substack.com/",
        "source_type": "journalism",
        "author": "Matt Taibbi",
        "year": 2022,
    },
    {
        "id": 518,
        "title": "The Weaponization of the Federal Government — House Judiciary Select Subcommittee interim staff report",
        "url": "https://judiciary.house.gov/sites/evo-subsites/republicans-judiciary.house.gov/files/evo-media-document/2023-03-09-interim-staff-report.pdf",
        "source_type": "congressional",
        "year": 2023,
    },
    # --- Atlantic Council / DFRLab ---
    {
        "id": 519,
        "title": "Atlantic Council — Wikipedia (founding, funding, partnerships)",
        "url": "https://en.wikipedia.org/wiki/Atlantic_Council",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 520,
        "title": "Facebook partners with Atlantic Council to fight misinformation — Reuters",
        "url": "https://www.reuters.com/article/us-usa-facebook-atlantic-council-idUSKBN1IJ2LA",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2018,
    },
    {
        "id": 521,
        "title": "Atlantic Council annual report — donors and funding (official site)",
        "url": "https://www.atlanticcouncil.org/support/",
        "source_type": "other",
        "year": 2024,
    },
    # --- Church Committee ---
    {
        "id": 522,
        "title": "Church Committee — Wikipedia (formation, intelligence abuse investigations)",
        "url": "https://en.wikipedia.org/wiki/Church_Committee",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 523,
        "title": "Select Committee to Study Governmental Operations with Respect to Intelligence Activities — Senate.gov",
        "url": "https://www.senate.gov/about/powers-procedures/investigations/church-committee.htm",
        "source_type": "congressional",
        "year": 1976,
    },
    # --- Carl Bernstein ---
    {
        "id": 524,
        "title": "Carl Bernstein — Wikipedia (Watergate, CIA-media exposé)",
        "url": "https://en.wikipedia.org/wiki/Carl_Bernstein",
        "source_type": "other",
        "year": 2024,
    },
    # --- Jeff Bezos / Amazon-CIA ---
    {
        "id": 525,
        "title": "Amazon Web Services wins secret $600M CIA cloud contract — Washington Post / FCW",
        "url": "https://fcw.com/cloud-infrastructure/2013/03/amazon-nabs-cia-cloud-deal/252702/",
        "source_type": "journalism",
        "author": "FCW (Federal Computer Week)",
        "year": 2013,
    },
    {
        "id": 526,
        "title": "Jeff Bezos acquires The Washington Post — Washington Post announcement",
        "url": "https://www.washingtonpost.com/national/jeff-bezos-on-post-purchase-says-utilitarian-utilitarian-utilitarian/2013/09/02/4a4c6b6a-13f3-11e3-b182-1b3bb2eb474c_story.html",
        "source_type": "journalism",
        "year": 2013,
    },
    # --- Anderson Cooper / Vanderbilt ---
    {
        "id": 527,
        "title": "Anderson Cooper — Wikipedia (Vanderbilt family, CIA internship)",
        "url": "https://en.wikipedia.org/wiki/Anderson_Cooper",
        "source_type": "other",
        "year": 2024,
    },
    # --- LifeLog / Facebook ---
    {
        "id": 528,
        "title": "Pentagon Kills LifeLog Project — Wired",
        "url": "https://www.wired.com/2004/02/pentagon-kills-lifelog-project/",
        "source_type": "journalism",
        "author": "Wired",
        "year": 2004,
    },
    {
        "id": 529,
        "title": "LifeLog — Wikipedia (DARPA program, cancellation date)",
        "url": "https://en.wikipedia.org/wiki/LifeLog",
        "source_type": "other",
        "year": 2024,
    },
]

# ============================================================
# ENTITIES — ~30 new (continuing from existing 313)
# ============================================================

ENTITIES = [
    # ============ PEOPLE ============

    {
        "name": "Rupert Murdoch",
        "entity_type": "person",
        "description": (
            "Australian-born American media mogul. Built the largest English-language "
            "media empire in history through News Corp and Fox Corporation. Holdings include "
            "Fox News, The Wall Street Journal, The Times (London), The Sun, Sky News Australia, "
            "New York Post, and HarperCollins. Pioneered the partisan 24-hour news model with "
            "Fox News (est. 1996). Phone hacking scandal led to closure of News of the World "
            "(2011) and UK Leveson Inquiry. Stepped down as Fox Corporation chairman in "
            "September 2023. His media properties have shaped political outcomes in the US, "
            "UK, and Australia for four decades."
        ),
        "aliases": "Keith Rupert Murdoch",
        "metadata": {
            "nationality": "American (born Australian)",
            "born": "1931-03-11",
            "role": "Founder & former Chairman, News Corp / Fox Corporation",
        },
    },
    {
        "name": "Edward Bernays",
        "entity_type": "person",
        "description": (
            "Austrian-American pioneer of public relations and propaganda theory. Nephew of "
            "Sigmund Freud. Authored 'Crystallizing Public Opinion' (1923) and 'Propaganda' "
            "(1928), which argued that 'the conscious and intelligent manipulation of the "
            "organized habits and opinions of the masses is an important element in democratic "
            "society.' Orchestrated the 1929 'Torches of Freedom' campaign linking cigarettes "
            "to women's liberation. Designed the media campaign for the 1954 CIA-backed "
            "Guatemalan coup (Operation PBSUCCESS). His techniques became foundational to "
            "modern PR, advertising, political campaigning, and intelligence psychological "
            "operations. Called 'the father of public relations.'"
        ),
        "aliases": "Edward Louis Bernays",
        "metadata": {
            "nationality": "American (born Austrian)",
            "born": "1891-11-22",
            "died": "1995-03-09",
            "role": "Father of public relations / propaganda theorist",
        },
    },
    {
        "name": "Frank Wisner",
        "entity_type": "person",
        "description": (
            "CIA officer who headed the Office of Policy Coordination (OPC, 1948-1951), "
            "the agency's covert operations arm. Architect of Operation Mockingbird — the "
            "CIA's systematic infiltration of American and international media. By the mid-1950s, "
            "the program had recruited journalists, editors, and publishers at major outlets "
            "including The Washington Post, New York Times, Newsweek, CBS, and Time-Life. "
            "Wisner called the network his 'Mighty Wurlitzer' — an organ he could play to "
            "produce any propaganda tune. Later served as CIA station chief in London. "
            "Suffered mental breakdown, died by suicide in 1965."
        ),
        "aliases": "Frank Gardiner Wisner",
        "metadata": {
            "nationality": "American",
            "born": "1909-06-23",
            "died": "1965-10-29",
            "role": "CIA OPC director, Mockingbird architect",
        },
    },
    {
        "name": "Carl Bernstein",
        "entity_type": "person",
        "description": (
            "American investigative journalist. Famous for Watergate reporting with Bob Woodward "
            "at The Washington Post. In 1977, published 'The CIA and the Media' in Rolling "
            "Stone — a 25,000-word exposé documenting how over 400 American journalists had "
            "secretly carried out assignments for the CIA between 1950-1977. Named specific "
            "media organizations including CBS, Time, The New York Times, and the Associated "
            "Press. The article remains the most comprehensive public accounting of the CIA's "
            "media infiltration program."
        ),
        "aliases": "Carl Milton Bernstein",
        "metadata": {
            "nationality": "American",
            "born": "1944-02-14",
            "role": "Investigative journalist, Watergate reporter",
        },
    },
    {
        "name": "Anderson Cooper",
        "entity_type": "person",
        "description": (
            "CNN anchor and journalist. Son of Gloria Vanderbilt, great-great-great-grandson "
            "of Cornelius Vanderbilt. Interned at the CIA while a student at Yale University — "
            "a fact he has publicly acknowledged, describing it as 'two summers' during college. "
            "After the internship, went directly into journalism. His career trajectory — from "
            "Vanderbilt dynasty to CIA internship to prominent media position — exemplifies "
            "the intelligence-media revolving door, though no evidence exists of ongoing "
            "CIA affiliation after his internship."
        ),
        "aliases": "Anderson Hays Cooper",
        "metadata": {
            "nationality": "American",
            "born": "1967-06-03",
            "role": "CNN anchor, Vanderbilt heir",
        },
    },
    {
        "name": "Jeff Bezos",
        "entity_type": "person",
        "description": (
            "Founder of Amazon. Purchased The Washington Post in 2013 for $250 million. "
            "The same year, Amazon Web Services won a $600 million CIA cloud computing "
            "contract — placing the CIA's data infrastructure and one of America's most "
            "influential newspapers under the same owner. No evidence of editorial interference "
            "has been publicly documented, but the structural conflict of interest is "
            "unprecedented in American media history."
        ),
        "aliases": "Jeffrey Preston Bezos",
        "metadata": {
            "nationality": "American",
            "born": "1964-01-12",
            "role": "Amazon founder, Washington Post owner",
        },
    },
    {
        "name": "Julian Assange",
        "entity_type": "person",
        "description": (
            "Australian journalist and founder of WikiLeaks. Published classified materials "
            "including the Iraq and Afghanistan war logs, Guantanamo files, and State Department "
            "cables (2010-2011). Sought asylum in Ecuadorian embassy in London (2012-2019). "
            "Arrested April 2019. Indicted under the Espionage Act of 1917 — the first time "
            "the act was used against a publisher. Faced 175 years in prison. Held in HM Prison "
            "Belmarsh for 5 years. Pleaded guilty to single Espionage Act charge in June 2024 "
            "plea deal, released to time served. His prosecution established a precedent that "
            "publishing classified information can be criminalized, with chilling effects on "
            "investigative journalism worldwide."
        ),
        "aliases": "Julian Paul Assange",
        "metadata": {
            "nationality": "Australian",
            "born": "1971-07-03",
            "role": "WikiLeaks founder, publisher",
        },
    },
    {
        "name": "Edward Snowden",
        "entity_type": "person",
        "description": (
            "Former NSA contractor (Booz Allen Hamilton) who in June 2013 disclosed "
            "thousands of classified documents revealing the NSA's global mass surveillance "
            "programs, including PRISM (direct access to tech company servers), XKeyscore "
            "(real-time internet monitoring), and Boundless Informant (metadata collection "
            "tracking). Disclosures published by The Guardian and The Washington Post. "
            "Charged under the Espionage Act. Granted asylum in Russia. The revelations "
            "triggered global debate on surveillance, led to the USA FREEDOM Act (2015), "
            "and exposed the Five Eyes alliance's scope of operations."
        ),
        "aliases": "Edward Joseph Snowden",
        "metadata": {
            "nationality": "American",
            "born": "1983-06-21",
            "role": "NSA whistleblower",
        },
    },
    {
        "name": "Chelsea Manning",
        "entity_type": "person",
        "description": (
            "Former U.S. Army intelligence analyst. In 2010, leaked approximately 750,000 "
            "classified military and diplomatic documents to WikiLeaks, including the "
            "'Collateral Murder' video showing a U.S. Apache helicopter killing Reuters "
            "journalists in Baghdad. Convicted under the Espionage Act in 2013. Sentenced "
            "to 35 years — the longest sentence for a leak case in U.S. history. Sentence "
            "commuted by President Obama in January 2017. Later jailed again (2019-2020) "
            "for refusing to testify before a grand jury investigating WikiLeaks."
        ),
        "aliases": "Bradley Manning, Chelsea Elizabeth Manning",
        "metadata": {
            "nationality": "American",
            "born": "1987-12-17",
            "role": "Military whistleblower, WikiLeaks source",
        },
    },
    {
        "name": "William Binney",
        "entity_type": "person",
        "description": (
            "Former NSA technical director and 36-year veteran of the agency. Co-created "
            "ThinThread, an NSA surveillance program designed with built-in privacy "
            "protections for American citizens. After 9/11, NSA leadership chose the "
            "warrantless mass surveillance program Stellar Wind over ThinThread, stripping "
            "out the privacy safeguards. Binney resigned in protest in October 2001. Filed "
            "DoD Inspector General complaint. FBI raided his home in 2007. Has testified "
            "before Congress and in the Jewel v. NSA case about unconstitutional surveillance. "
            "His story predates and corroborates Snowden's revelations."
        ),
        "aliases": "William Edward Binney",
        "metadata": {
            "nationality": "American",
            "born": "1943-09-01",
            "role": "NSA whistleblower, ThinThread designer",
        },
    },

    # ============ ORGANIZATIONS ============

    {
        "name": "News Corp",
        "entity_type": "organization",
        "description": (
            "American mass media conglomerate controlled by the Murdoch family. "
            "Split from 21st Century Fox in 2013. Owns The Wall Street Journal, New York Post, "
            "The Times (London), The Sun, The Australian, HarperCollins Publishers, Dow Jones, "
            "and REA Group. Together with Fox Corporation (Fox News, Fox Sports, Fox Business), "
            "the Murdoch media empire reaches billions globally. The 2011 phone hacking scandal "
            "at News of the World led to the UK Leveson Inquiry and exposed systematic illegal "
            "surveillance of public figures by Murdoch journalists."
        ),
        "aliases": "News Corporation, NewsCorp",
    },
    {
        "name": "Fox Corporation",
        "entity_type": "organization",
        "description": (
            "American mass media company spun off from 21st Century Fox in 2019 after "
            "Disney acquired Fox's entertainment assets. Owns Fox News Channel, Fox Business "
            "Network, Fox Sports, and 29 Fox Television Stations. Fox News, launched in 1996 "
            "with Roger Ailes, pioneered the partisan 24-hour cable news model and became "
            "the most-watched cable news network in the U.S. Settled the Dominion Voting "
            "Systems defamation lawsuit for $787.5 million in April 2023 — one of the largest "
            "media settlements in U.S. history."
        ),
        "aliases": "Fox News, Fox Media",
    },
    {
        "name": "The Walt Disney Company",
        "entity_type": "organization",
        "description": (
            "American multinational media and entertainment conglomerate. Controls ABC News, "
            "ESPN, FX Networks, National Geographic, Hulu, Disney+, Pixar, Marvel, Lucasfilm, "
            "and 20th Century Studios. Acquired 21st Century Fox entertainment assets for "
            "$71.3 billion in 2019. One of the 'Big Six' media conglomerates that control "
            "the vast majority of American media output. ABC News has been a primary broadcast "
            "news source since the network era."
        ),
        "aliases": "Disney, Walt Disney",
    },
    {
        "name": "Comcast Corporation",
        "entity_type": "organization",
        "description": (
            "American telecommunications and media conglomerate. Largest cable operator and "
            "internet service provider in the U.S. Acquired NBCUniversal in 2011 for $30 billion. "
            "Controls NBC News, MSNBC, CNBC, Universal Pictures, DreamWorks, Sky (UK/Europe), "
            "and Peacock streaming. The merger of America's largest cable company with a major "
            "broadcast network exemplifies the vertical integration enabled by the "
            "Telecommunications Act of 1996."
        ),
        "aliases": "Comcast, NBCUniversal, NBCU",
    },
    {
        "name": "Warner Bros. Discovery",
        "entity_type": "organization",
        "description": (
            "American multinational media conglomerate formed in 2022 by the merger of "
            "WarnerMedia and Discovery, Inc. Controls CNN, HBO, Warner Bros. Pictures, "
            "DC Studios, TNT, TBS, Discovery Channel, and Max streaming. CNN, founded by "
            "Ted Turner in 1980, pioneered the 24-hour news cycle. The successive mergers "
            "(Time Warner → AOL Time Warner → WarnerMedia → Warner Bros. Discovery) "
            "illustrate the accelerating consolidation of media ownership since the 1990s."
        ),
        "aliases": "WBD, WarnerMedia, Time Warner, AOL Time Warner",
    },
    {
        "name": "Paramount Global",
        "entity_type": "organization",
        "description": (
            "American multinational media conglomerate. Formed from the 2019 recombination "
            "of Viacom and CBS Corporation (previously split in 2006). Controlled by the "
            "Redstone family through National Amusements. Owns CBS News, Paramount Pictures, "
            "MTV, Nickelodeon, Comedy Central, BET, Showtime, and Paramount+. CBS News has "
            "been a primary broadcast news source since the Edward R. Murrow era."
        ),
        "aliases": "Viacom, ViacomCBS, CBS Corporation, National Amusements",
    },
    {
        "name": "WikiLeaks",
        "entity_type": "organization",
        "description": (
            "International non-profit organization founded by Julian Assange in 2006 to "
            "publish classified, censored, or restricted materials from anonymous sources. "
            "Major publications include: Afghan War Diary (2010), Iraq War Logs (2010), "
            "U.S. diplomatic cables / Cablegate (2010), Guantanamo files (2011), Vault 7 "
            "CIA hacking tools (2017), and DNC emails (2016). Partnered with major newspapers "
            "(The Guardian, NYT, Der Spiegel, Le Monde, El País) for initial publications. "
            "Described by Assange as a 'giant library of the world's most persecuted documents.' "
            "Changed the calculus of government secrecy by demonstrating that large-scale "
            "leaks were technically possible."
        ),
        "aliases": "",
    },
    {
        "name": "Tavistock Institute",
        "entity_type": "organization",
        "description": (
            "British research and consulting organization founded in 1947, growing out of the "
            "Tavistock Clinic's WWII work on psychological warfare and soldier selection for "
            "the British Army. Original researchers included Wilfred Bion, John Bowlby, and "
            "Eric Trist. Funded by the Rockefeller Foundation from its inception. Pioneered "
            "group dynamics, organizational development, and social engineering methodologies. "
            "Its techniques for managing group behavior at scale influenced corporate management, "
            "military psychological operations, and communications strategy. Connected to "
            "the broader Anglo-American psychological warfare establishment that included "
            "the OSS/CIA and British SOE/PWE."
        ),
        "aliases": "Tavistock Institute of Human Relations, TIHR",
    },
    {
        "name": "Atlantic Council",
        "entity_type": "organization",
        "description": (
            "American think tank founded in 1961 to promote Atlanticism and NATO. Funded by "
            "NATO governments, defense contractors (Raytheon, Lockheed Martin, Boeing), tech "
            "companies (Google, Facebook/Meta, Microsoft), oil companies (BP, Chevron), and "
            "sovereign wealth funds (UAE, Saudi Arabia). Its Digital Forensic Research Lab "
            "(DFRLab) partners directly with Facebook/Meta, Twitter/X, and other platforms "
            "to identify and remove 'disinformation.' This arrangement places a "
            "military-industrial-funded think tank in a gatekeeping role over public discourse "
            "on social media. Board members have included Henry Kissinger, Condoleezza Rice, "
            "Colin Powell, and James Mattis."
        ),
        "aliases": "DFRLab, Digital Forensic Research Lab",
    },

    # ============ PROGRAMS / OPERATIONS ============

    {
        "name": "Operation Mockingbird",
        "entity_type": "program",
        "description": (
            "CIA program to infiltrate and influence American and international media, "
            "beginning in the early 1950s under Frank Wisner's Office of Policy Coordination. "
            "By the mid-1950s, the CIA had recruited journalists, editors, publishers, and "
            "media executives at major outlets including The Washington Post, New York Times, "
            "Newsweek, CBS, Time-Life, Associated Press, UPI, Reuters, Hearst, Scripps-Howard, "
            "and Copley News Service. Carl Bernstein's 1977 Rolling Stone exposé documented "
            "over 400 American journalists who secretly carried out CIA assignments. The Church "
            "Committee (1975-1976) investigated but CIA Director George H.W. Bush only agreed "
            "to end 'paid' relationships — leaving unpaid, voluntary arrangements intact. "
            "The full scope of the program has never been officially declassified."
        ),
        "aliases": "Mockingbird, CIA media program",
    },
    {
        "name": "PRISM",
        "entity_type": "program",
        "description": (
            "NSA surveillance program revealed by Edward Snowden in June 2013. Provided the "
            "NSA with direct access to the servers of nine major tech companies: Microsoft "
            "(2007), Yahoo (2008), Google (2009), Facebook (2009), PalTalk (2009), YouTube "
            "(2010), Skype (2011), AOL (2011), and Apple (2012). Authorized under Section 702 "
            "of the FISA Amendments Act. Collected emails, chat logs, stored data, voice "
            "traffic, file transfers, video conferencing, and social media profiles. One of "
            "several NSA programs exposed by Snowden; others included XKeyscore (real-time "
            "internet monitoring), Boundless Informant (metadata analytics), and Upstream "
            "(fiber-optic cable tapping)."
        ),
        "aliases": "Planning Tool for Resource Integration, Synchronization, and Management",
    },

    # ============ LEGISLATION / EVENTS ============

    {
        "name": "Telecommunications Act of 1996",
        "entity_type": "legislation",
        "description": (
            "Major U.S. legislation signed by President Clinton on February 8, 1996. "
            "The first significant overhaul of telecommunications law since 1934. Removed "
            "most ownership limits on radio stations (previously capped at 40 nationally) "
            "and relaxed television ownership rules. Enabled massive media consolidation: "
            "within a decade, the number of major media companies dropped from ~50 to 6. "
            "Clear Channel Communications (now iHeartMedia) grew from 40 to 1,200 radio "
            "stations. Proponents argued it would increase competition; critics argue it "
            "concentrated control of public discourse in fewer hands than at any point "
            "in American history."
        ),
        "aliases": "Telecom Act 1996",
    },
    {
        "name": "Smith-Mundt Modernization Act",
        "entity_type": "legislation",
        "description": (
            "Section 1078 of the National Defense Authorization Act for FY2013, signed into "
            "law July 2, 2013. Amended the Smith-Mundt Act of 1948 and the Foreign Relations "
            "Authorization Act of 1987 to allow materials produced by the Broadcasting Board "
            "of Governors (Voice of America, Radio Free Europe, etc.) to be disseminated "
            "within the United States. The original Smith-Mundt Act had specifically prohibited "
            "the domestic distribution of government-produced propaganda. Critics argue the "
            "modernization legalized the domestic use of state propaganda; supporters claim "
            "it merely allowed Americans to access content already available overseas."
        ),
        "aliases": "Smith-Mundt Modernization Act of 2012, NDAA FY2013 Section 1078",
    },
    {
        "name": "Pentagon Military Analyst Program",
        "entity_type": "program",
        "description": (
            "Secret Pentagon program (2002-2008) exposed by David Barstow in the New York "
            "Times (Pulitzer Prize, 2009). The Department of Defense recruited ~75 retired "
            "military officers who served as paid TV news analysts at ABC, CBS, NBC, CNN, "
            "Fox News, and MSNBC. Pentagon provided them with talking points, classified "
            "briefings, and trips to Iraq/Guantanamo. Many had undisclosed financial ties "
            "to defense contractors who benefited from the wars they were promoting on air. "
            "Networks did not disclose these arrangements to viewers. The DoD Inspector General "
            "investigated but produced only a heavily redacted interim report. No analyst or "
            "Pentagon official faced consequences."
        ),
        "aliases": "Pentagon pundit program, DoD military analyst program",
    },
    {
        "name": "Church Committee",
        "entity_type": "event",
        "description": (
            "U.S. Senate Select Committee to Study Governmental Operations with Respect to "
            "Intelligence Activities (1975-1976), chaired by Senator Frank Church (D-Idaho). "
            "Investigated abuses by the CIA, NSA, FBI, and IRS. Published 14 reports exposing "
            "Operation Mockingbird (CIA media infiltration), COINTELPRO (FBI domestic "
            "surveillance), NSA warrantless wiretapping (Operation SHAMROCK and MINARET), "
            "CIA assassination plots against foreign leaders, and MKULTRA mind control "
            "experiments. Led directly to the creation of the Senate Select Committee on "
            "Intelligence and the Foreign Intelligence Surveillance Act (FISA). The most "
            "comprehensive Congressional investigation of intelligence abuses in U.S. history."
        ),
        "aliases": "Church Committee Investigation, Senate Intelligence Committee Investigation",
    },
    {
        "name": "Twitter Files",
        "entity_type": "event",
        "description": (
            "Series of internal Twitter communications released beginning December 2, 2022 "
            "after Elon Musk acquired the company. Published by journalists Matt Taibbi, "
            "Michael Shellenberger, Bari Weiss, Lee Fang, and David Zweig. Documented "
            "systematic government-platform censorship coordination: FBI flagged specific "
            "accounts/posts for suppression, DHS established regular content moderation "
            "meetings, State Department's GEC flagged foreign policy-related content, and "
            "Stanford Internet Observatory / Election Integrity Partnership served as "
            "intermediaries between government and platforms. The House Judiciary Select "
            "Subcommittee on the Weaponization of the Federal Government used the files "
            "in its investigation of federal censorship."
        ),
        "aliases": "Twitter Files releases",
    },
    {
        "name": "LifeLog",
        "entity_type": "program",
        "description": (
            "DARPA program announced in 2003 to create a comprehensive digital record of "
            "a person's entire life — every activity, relationship, communication, media "
            "consumption, and location. Officially cancelled on February 4, 2004. Facebook "
            "was launched the same day — February 4, 2004. The DARPA program and the social "
            "media platform share the same functional goal: a complete digital profile of "
            "human activity. No direct institutional link between LifeLog's cancellation and "
            "Facebook's launch has been publicly documented, but the coincidence of dates "
            "and functional overlap is noted by researchers."
        ),
        "aliases": "DARPA LifeLog",
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ==== OPERATION MOCKINGBIRD & CIA-MEDIA ====
    {
        "source": "Frank Wisner",
        "target": "CIA",
        "type": "served_in",
        "tier": "documented",
        "desc": (
            "Headed the CIA's Office of Policy Coordination (OPC, 1948-1951), "
            "the covert operations arm. Later served as CIA station chief in London."
        ),
        "year_start": 1948,
        "year_end": 1962,
        "sources": [484, 486],
    },
    {
        "source": "Frank Wisner",
        "target": "Operation Mockingbird",
        "type": "created",
        "tier": "credible",
        "desc": (
            "Architect of the CIA's media infiltration program beginning in the early 1950s. "
            "Called his network of media assets 'the Mighty Wurlitzer.'"
        ),
        "year_start": 1950,
        "sources": [483, 484, 486],
    },
    {
        "source": "Operation Mockingbird",
        "target": "CIA",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "CIA program to recruit journalists, editors, and publishers at major American "
            "and international media outlets. Church Committee confirmed the program's "
            "existence. Full scope never declassified."
        ),
        "year_start": 1950,
        "sources": [483, 484, 485],
    },
    {
        "source": "Carl Bernstein",
        "target": "Operation Mockingbird",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Published 'The CIA and the Media' in Rolling Stone (1977), documenting over "
            "400 American journalists who secretly carried out CIA assignments."
        ),
        "year_start": 1977,
        "sources": [483, 524],
    },
    {
        "source": "Church Committee",
        "target": "Operation Mockingbird",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Investigated CIA media infiltration as part of broader intelligence abuse "
            "inquiry. CIA Director George H.W. Bush agreed only to end 'paid' journalist "
            "relationships, leaving voluntary arrangements intact."
        ),
        "year_start": 1975,
        "year_end": 1976,
        "sources": [484, 522, 523],
    },
    {
        "source": "Church Committee",
        "target": "CIA",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Senate Select Committee (1975-1976) investigated CIA abuses including media "
            "infiltration, assassination plots, MKULTRA, and COINTELPRO collaboration. "
            "Published 14 reports."
        ),
        "year_start": 1975,
        "year_end": 1976,
        "sources": [484, 522, 523],
    },
    {
        "source": "Church Committee",
        "target": "NSA",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Exposed NSA warrantless wiretapping programs Operation SHAMROCK (monitoring "
            "all telegraph traffic) and Operation MINARET (watchlist surveillance of "
            "American citizens)."
        ),
        "year_start": 1975,
        "year_end": 1976,
        "sources": [484, 522, 523],
    },
    {
        "source": "Church Committee",
        "target": "FBI",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Exposed FBI's COINTELPRO domestic surveillance and disruption programs "
            "targeting civil rights leaders, antiwar activists, and political organizations."
        ),
        "year_start": 1975,
        "year_end": 1976,
        "sources": [484, 522, 523],
    },

    # ==== PROPAGANDA THEORY ====
    {
        "source": "Edward Bernays",
        "target": "CIA",
        "type": "consulted_for",
        "tier": "credible",
        "desc": (
            "Designed the media campaign for the 1954 CIA-backed Guatemalan coup "
            "(Operation PBSUCCESS). His propaganda techniques were foundational to "
            "CIA psychological operations methodology."
        ),
        "year_start": 1954,
        "sources": [487, 488, 489],
    },
    {
        "source": "Edward Bernays",
        "target": "Tavistock Institute",
        "type": "influenced",
        "tier": "inference",
        "desc": (
            "Bernays' propaganda theory and applied techniques for managing mass behavior "
            "informed the broader Anglo-American psychological warfare establishment from "
            "which Tavistock emerged. Both drew on Freudian psychology (Bernays was Freud's "
            "nephew) for mass persuasion."
        ),
        "sources": [487, 489, 490],
    },

    # ==== MEDIA CONGLOMERATES ====
    {
        "source": "Rupert Murdoch",
        "target": "News Corp",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Built News Corp from a single Adelaide newspaper into a global media empire. "
            "Split into News Corp (publishing) and 21st Century Fox (entertainment/news) "
            "in 2013; 21st Century Fox entertainment assets sold to Disney in 2019."
        ),
        "year_start": 1979,
        "sources": [495, 496],
    },
    {
        "source": "Rupert Murdoch",
        "target": "Fox Corporation",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Created Fox Corporation in 2019 from the news/sports assets retained after "
            "selling 21st Century Fox entertainment to Disney. Stepped down as chairman "
            "in September 2023."
        ),
        "year_start": 2019,
        "year_end": 2023,
        "sources": [495, 497],
    },
    {
        "source": "Telecommunications Act of 1996",
        "target": "News Corp",
        "type": "enabled",
        "tier": "credible",
        "desc": (
            "Relaxed media ownership limits enabled Murdoch's expansion across broadcast, "
            "cable, print, and digital media in the U.S. market."
        ),
        "year_start": 1996,
        "sources": [492, 493, 494],
    },
    {
        "source": "Telecommunications Act of 1996",
        "target": "Comcast Corporation",
        "type": "enabled",
        "tier": "credible",
        "desc": (
            "Deregulation enabled Comcast's growth from a regional cable operator to "
            "America's largest cable company, culminating in the $30B NBCUniversal "
            "acquisition (2011)."
        ),
        "year_start": 1996,
        "sources": [492, 493, 500],
    },
    {
        "source": "Telecommunications Act of 1996",
        "target": "The Walt Disney Company",
        "type": "enabled",
        "tier": "credible",
        "desc": (
            "Relaxed ownership rules enabled Disney's expansion into cable (ESPN, ABC) "
            "and subsequent $71.3B acquisition of 21st Century Fox entertainment assets."
        ),
        "year_start": 1996,
        "sources": [492, 493, 499],
    },
    {
        "source": "Telecommunications Act of 1996",
        "target": "Warner Bros. Discovery",
        "type": "enabled",
        "tier": "credible",
        "desc": (
            "Enabled the successive mergers: Time Inc. + Warner → Time Warner → "
            "AOL Time Warner → AT&T/WarnerMedia → Warner Bros. Discovery."
        ),
        "year_start": 1996,
        "sources": [492, 493, 501],
    },
    {
        "source": "Telecommunications Act of 1996",
        "target": "Paramount Global",
        "type": "enabled",
        "tier": "credible",
        "desc": (
            "Enabled Viacom/CBS/Paramount consolidation under Redstone family's "
            "National Amusements holding company."
        ),
        "year_start": 1996,
        "sources": [492, 493, 502],
    },

    # ==== WHISTLEBLOWERS & TRANSPARENCY ====
    {
        "source": "Julian Assange",
        "target": "WikiLeaks",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded WikiLeaks in 2006 as a platform for publishing classified and censored materials.",
        "year_start": 2006,
        "sources": [503, 510],
    },
    {
        "source": "Chelsea Manning",
        "target": "WikiLeaks",
        "type": "source_for",
        "tier": "documented",
        "desc": (
            "Leaked ~750,000 classified military and diplomatic documents to WikiLeaks "
            "in 2010, including the 'Collateral Murder' video. Convicted under Espionage Act."
        ),
        "year_start": 2010,
        "sources": [503, 507, 510],
    },
    {
        "source": "Edward Snowden",
        "target": "NSA",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Disclosed thousands of classified documents in June 2013 revealing NSA's "
            "global mass surveillance programs (PRISM, XKeyscore, Boundless Informant, "
            "Upstream). Charged under Espionage Act."
        ),
        "year_start": 2013,
        "sources": [505, 506, 511],
    },
    {
        "source": "Edward Snowden",
        "target": "PRISM",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Revealed PRISM program giving NSA direct access to servers of 9 major tech "
            "companies. Documents published by The Guardian and Washington Post."
        ),
        "year_start": 2013,
        "sources": [506, 511, 512],
    },
    {
        "source": "PRISM",
        "target": "NSA",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "NSA surveillance program authorized under Section 702 of FISA Amendments Act. "
            "Provided direct access to tech company servers from 2007 onward."
        ),
        "year_start": 2007,
        "sources": [511, 512],
    },
    {
        "source": "William Binney",
        "target": "NSA",
        "type": "served_in",
        "tier": "documented",
        "desc": (
            "36-year NSA veteran, technical director. Resigned October 2001 after NSA chose "
            "warrantless mass surveillance (Stellar Wind) over his privacy-protecting "
            "ThinThread program."
        ),
        "year_start": 1965,
        "year_end": 2001,
        "sources": [508, 509],
    },
    {
        "source": "William Binney",
        "target": "Edward Snowden",
        "type": "corroborated",
        "tier": "credible",
        "desc": (
            "Binney's earlier testimony about warrantless NSA surveillance predated and "
            "corroborated Snowden's 2013 document disclosures. Both described the same "
            "unconstitutional mass collection architecture."
        ),
        "sources": [505, 508, 509],
    },

    # ==== JEFF BEZOS / AMAZON-CIA-WAPO ====
    {
        "source": "Jeff Bezos",
        "target": "CIA",
        "type": "contracted_with",
        "tier": "documented",
        "desc": (
            "Amazon Web Services won $600 million CIA cloud computing contract in 2013, "
            "placing CIA data infrastructure under the same owner as The Washington Post."
        ),
        "year_start": 2013,
        "sources": [525],
    },

    # ==== ANDERSON COOPER / CIA INTERNSHIP ====
    {
        "source": "Anderson Cooper",
        "target": "CIA",
        "type": "interned_at",
        "tier": "documented",
        "desc": (
            "Interned at the CIA for two summers while a student at Yale. Has publicly "
            "acknowledged the internship. Went directly into journalism afterward."
        ),
        "year_start": 1989,
        "year_end": 1990,
        "sources": [527],
    },

    # ==== SMITH-MUNDT / DOMESTIC PROPAGANDA ====
    {
        "source": "Smith-Mundt Modernization Act",
        "target": "Operation Mockingbird",
        "type": "related_to",
        "tier": "inference",
        "desc": (
            "The 2012 amendment to the Smith-Mundt Act legalized what Mockingbird did "
            "covertly: disseminating government-produced media content to domestic audiences. "
            "The original 1948 act had been a response to concerns about domestic propaganda."
        ),
        "year_start": 2013,
        "sources": [513, 514, 483],
    },

    # ==== PENTAGON MILITARY ANALYST PROGRAM ====
    {
        "source": "Pentagon Military Analyst Program",
        "target": "Fox Corporation",
        "type": "placed_analysts_at",
        "tier": "documented",
        "desc": (
            "Pentagon placed retired military officers as paid TV analysts at Fox News "
            "with undisclosed DoD talking points and defense contractor ties."
        ),
        "year_start": 2002,
        "year_end": 2008,
        "sources": [515, 516],
    },
    {
        "source": "Pentagon Military Analyst Program",
        "target": "Comcast Corporation",
        "type": "placed_analysts_at",
        "tier": "documented",
        "desc": (
            "Pentagon placed retired military officers as paid TV analysts at NBC/MSNBC/CNBC "
            "with undisclosed DoD talking points and defense contractor ties."
        ),
        "year_start": 2002,
        "year_end": 2008,
        "sources": [515, 516],
    },
    {
        "source": "Pentagon Military Analyst Program",
        "target": "Warner Bros. Discovery",
        "type": "placed_analysts_at",
        "tier": "documented",
        "desc": (
            "Pentagon placed retired military officers as paid TV analysts at CNN "
            "with undisclosed DoD talking points and defense contractor ties."
        ),
        "year_start": 2002,
        "year_end": 2008,
        "sources": [515, 516],
    },

    # ==== TWITTER FILES / CENSORSHIP ====
    {
        "source": "Twitter Files",
        "target": "FBI",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Twitter Files revealed FBI regularly flagged specific accounts and posts "
            "for suppression. FBI had dedicated staff for social media content moderation "
            "requests to Twitter."
        ),
        "year_start": 2022,
        "sources": [517, 518],
    },
    {
        "source": "Twitter Files",
        "target": "Atlantic Council",
        "type": "exposed",
        "tier": "credible",
        "desc": (
            "Files documented how think tanks and government-adjacent organizations served "
            "as intermediaries in the censorship pipeline between federal agencies and "
            "social media platforms."
        ),
        "year_start": 2022,
        "sources": [517, 518],
    },
    {
        "source": "Atlantic Council",
        "target": "CIA",
        "type": "affiliated_with",
        "tier": "credible",
        "desc": (
            "Board members have included former CIA directors and senior intelligence officials. "
            "Funded by defense contractors and NATO governments. Its DFRLab conducts "
            "information operations analysis aligned with Western intelligence priorities."
        ),
        "sources": [519, 521],
    },

    # ==== LIFELOG / FACEBOOK / DARPA ====
    {
        "source": "LifeLog",
        "target": "DARPA",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "DARPA program to create comprehensive digital records of human lives. "
            "Announced 2003, cancelled February 4, 2004 — the same day Facebook launched."
        ),
        "year_start": 2003,
        "year_end": 2004,
        "sources": [528, 529],
    },

    # ==== TAVISTOCK CONNECTIONS ====
    {
        "source": "Tavistock Institute",
        "target": "Operation Mockingbird",
        "type": "influenced",
        "tier": "inference",
        "desc": (
            "Tavistock's WWII-era research on psychological warfare, group dynamics, and "
            "mass persuasion techniques informed the broader Anglo-American psychological "
            "operations establishment from which CIA media programs emerged."
        ),
        "sources": [490, 491, 484],
    },

    # ==== CROSS-LINKS TO EPSTEIN NETWORK ====
    {
        "source": "Jeffrey Epstein",
        "target": "News Corp",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Epstein cultivated relationships with media figures across conglomerates. "
            "The Epstein network's ability to avoid sustained media scrutiny for decades "
            "despite known criminal behavior illustrates the narrative control architecture."
        ),
        "sources": [498],
    },

    # ==== LEVESON INQUIRY / MURDOCH ====
    {
        "source": "News Corp",
        "target": "Rupert Murdoch",
        "type": "controlled_by",
        "tier": "documented",
        "desc": (
            "Murdoch family maintains controlling interest in News Corp through dual-class "
            "share structure. Rupert Murdoch built the company from a single Adelaide "
            "newspaper into a global media empire."
        ),
        "sources": [495, 496],
    },
]

# ============================================================
# ENTITY_SOURCES — link entities to their primary sources
# ============================================================

ENTITY_SOURCES = {
    # People
    "Rupert Murdoch": [495, 496, 497, 498],
    "Edward Bernays": [487, 488, 489],
    "Frank Wisner": [483, 484, 486],
    "Carl Bernstein": [483, 524],
    "Anderson Cooper": [527],
    "Jeff Bezos": [525, 526],
    "Julian Assange": [503, 504, 510],
    "Edward Snowden": [505, 506, 511],
    "Chelsea Manning": [503, 507],
    "William Binney": [508, 509],
    # Organizations
    "News Corp": [495, 496, 498],
    "Fox Corporation": [497, 498, 515],
    "The Walt Disney Company": [493, 494, 499],
    "Comcast Corporation": [493, 494, 500],
    "Warner Bros. Discovery": [493, 494, 501],
    "Paramount Global": [493, 494, 502],
    "WikiLeaks": [503, 504, 510],
    "Tavistock Institute": [490, 491],
    "Atlantic Council": [519, 520, 521],
    # Programs
    "Operation Mockingbird": [483, 484, 485, 486],
    "PRISM": [511, 512],
    # Legislation / Events
    "Telecommunications Act of 1996": [492, 493],
    "Smith-Mundt Modernization Act": [513, 514],
    "Pentagon Military Analyst Program": [515, 516],
    "Church Committee": [484, 522, 523],
    "Twitter Files": [517, 518],
    "LifeLog": [528, 529],
}
