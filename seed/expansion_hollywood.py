"""
Hollywood, Media & Modeling Cluster — Expansion layer for Intel Console.
Entities: Entertainment industry figures, modeling agencies, and media companies
connected to the Epstein network.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# HOLLYWOOD, MEDIA & MODELING CLUSTER
# Sources 96-115, Entities, Relationships, Entity-Sources
# ============================================================

SOURCES = [
    # Journalism
    {"id": 96, "title": "Ronan Farrow — Catch and Kill: Lies, Spies, and a Conspiracy to Protect Predators", "url": "", "source_type": "book", "author": "Ronan Farrow", "year": 2019},
    {"id": 97, "title": "New Yorker — Harvey Weinstein's Army of Spies (Ronan Farrow)", "url": "https://www.newyorker.com/news/news-desk/harvey-weinsteins-army-of-spies", "source_type": "journalism", "author": "Ronan Farrow", "year": 2017},
    {"id": 98, "title": "New Yorker — Les Moonves and CBS Face Allegations of Sexual Misconduct (Ronan Farrow)", "url": "https://www.newyorker.com/magazine/2018/08/06/les-moonves-and-cbs-face-allegations-of-sexual-misconduct", "source_type": "journalism", "author": "Ronan Farrow", "year": 2018},
    {"id": 99, "title": "Daily Beast — Jeffrey Epstein's Hollywood Pipeline Ran Straight to Harvey Weinstein", "url": "https://www.thedailybeast.com/jeffrey-epsteins-hollywood-pipeline-ran-straight-to-harvey-weinstein/", "source_type": "journalism", "year": 2019},
    {"id": 100, "title": "NPR — ABC News Defends Epstein Coverage After Leaked Amy Robach Video", "url": "https://www.npr.org/2019/11/05/776482189/abc-news-defends-its-epstein-coverage-after-leaked-video-of-anchor", "source_type": "journalism", "year": 2019},
    {"id": 101, "title": "Times of Israel — Ehud Barak Referred Weinstein to Ex-Mossad Agents", "url": "https://www.timesofisrael.com/ehud-barak-referred-weinstein-to-ex-mossad-agents-he-hired-to-quash-allegations/", "source_type": "journalism", "year": 2017},
    {"id": 102, "title": "Washington Post — Jean-Luc Brunel Found Hanged in Paris Prison", "url": "https://www.washingtonpost.com/nation/2022/02/19/jean-luc-brunel-hanged-epstein/", "source_type": "journalism", "year": 2022},
    {"id": 103, "title": "Newsweek — Kevin Spacey Admits to Flying with Jeffrey Epstein and Bill Clinton", "url": "https://www.newsweek.com/kevin-spacey-admits-flying-jeffery-epstien-bill-clinton-1911631", "source_type": "journalism", "year": 2024},
    {"id": 104, "title": "Hollywood Reporter — Behind Steve Bing's Sudden, Tragic End", "url": "https://www.hollywoodreporter.com/news/general-news/behind-steve-bing-s-sudden-tragic-end-1300992/", "source_type": "journalism", "year": 2020},
    {"id": 105, "title": "Daily Beast — Inside Woody Allen's Close Friendship with Jeffrey Epstein", "url": "https://www.thedailybeast.com/inside-woody-allens-close-friendship-with-jeffrey-epstein/", "source_type": "journalism", "year": 2026},
    {"id": 106, "title": "Black Enterprise — Supermodel Naomi Campbell Stayed in Epstein's Orbit", "url": "https://www.blackenterprise.com/naomi-cambell-jeffrey-epstein-deny/", "source_type": "journalism", "year": 2024},
    {"id": 107, "title": "PBS — CBS CEO Les Moonves Accused of Sexual Misconduct Amid 'Culture of Impunity'", "url": "https://www.pbs.org/newshour/show/cbs-ceo-les-moonves-accused-of-sexual-misconduct-amid-culture-of-impunity", "source_type": "journalism", "year": 2018},
    {"id": 108, "title": "Harvey Weinstein Sexual Abuse Cases — NY Criminal Court Records", "url": "", "source_type": "court", "year": 2020},
    {"id": 109, "title": "CBS/Moonves $30.5M Settlement — NY Attorney General", "url": "", "source_type": "court", "year": 2022},
    {"id": 110, "title": "Virginia Giuffre Affidavit — Brunel Trafficking Allegations", "url": "", "source_type": "court", "year": 2015},
    {"id": 111, "title": "USVI v. JPMorgan Chase — Exhibit 101 (Epstein-Brunel Funding)", "url": "https://www.justice.gov/multimedia/Court%20Records/Government%20of%20the%20United%20States%20Virgin%20Islands%20v.%20JPMorgan%20Chase%20Bank,%20N.A.,%20No.%20122-cv-10904%20(S.D.N.Y.%202022)/240-01.pdf", "source_type": "court", "year": 2022},
    {"id": 112, "title": "Epstein Files — Congressional Release (House Oversight, 2026)", "url": "", "source_type": "congressional", "year": 2026},
    {"id": 113, "title": "Hollywood Reporter — Jeffrey Epstein's Hollywood: Mapping His Industry Connections", "url": "https://www.hollywoodreporter.com/news/general-news/jeffrey-epstein-hollywood-orbit-1236508954/", "source_type": "journalism", "year": 2026},
    {"id": 114, "title": "19th News — Epstein Tracked #MeToo Fallout and Advised Accused Men", "url": "https://19thnews.org/2026/02/jeffrey-epstein-files-tracked-metoo-fallout/", "source_type": "journalism", "year": 2026},
    {"id": 115, "title": "Rolling Stone — Aspiring Victoria's Secret Model Accuses Jeffrey Epstein of Sexual Assault", "url": "https://www.rollingstone.com/culture/culture-news/jeffrey-epstein-alicia-arden-victorias-secret-leslie-wexner-864095/", "source_type": "journalism", "year": 2019},
]

ENTITIES = [
    # ---- People ----
    {"name": "Harvey Weinstein", "entity_type": "person", "description": (
        "Harvey Weinstein (b. 1952). Co-founder of Miramax Films and The Weinstein Company. "
        "Convicted sex offender whose decades-long pattern of sexual assault, coercion, and "
        "surveillance-based intimidation parallels the Epstein operation's blackmail methodology."
        "\n\n"
        "CAREER: Co-founded Miramax Films with brother Bob Weinstein in 1979, named after their "
        "parents Miriam and Max. Built it into a dominant force in independent film, producing "
        "Pulp Fiction, Shakespeare in Love, and The English Patient. Left Miramax in 2005 to "
        "found The Weinstein Company."
        "\n\n"
        "SEXUAL PREDATION: Over 80 women accused Weinstein of sexual misconduct ranging from "
        "harassment to rape, spanning decades of his career. He exploited his position as "
        "Hollywood's most powerful producer — the promise of career advancement and the threat "
        "of career destruction were his primary coercion tools. Convicted in February 2020 in "
        "Manhattan on criminal sexual assault and third-degree rape (sentenced to 23 years). "
        "Convicted again in December 2022 in Los Angeles on rape and forced oral copulation "
        "(sentenced to 16 years). The New York conviction was overturned in April 2024 on "
        "procedural grounds; a 2025 retrial resulted in a partial guilty verdict."
        "\n\n"
        "BLACK CUBE / INTELLIGENCE METHODS: Hired Black Cube — a private intelligence firm "
        "staffed by former Mossad and Aman (Israeli military intelligence) operatives — to "
        "surveil, infiltrate, and discredit his accusers and journalists investigating him. "
        "Black Cube operatives used fabricated identities to approach accusers and reporters "
        "at The New Yorker, The New York Times, and New York magazine, compiling psychological "
        "profiles focusing on personal and sexual histories. Former Israeli PM Ehud Barak "
        "personally referred Weinstein to Black Cube — the same Barak who co-founded Carbyne "
        "with Epstein investment and received $2M from the Wexner Foundation."
        "\n\n"
        "EPSTEIN OVERLAP: Weinstein and Epstein socialized in the same New York circles. They "
        "shared a regular table at a Hamptons restaurant. Both were part of a group of investors "
        "who attempted to buy New York Magazine in 2003. Ghislaine Maxwell attended Weinstein "
        "film premieres and parties. Epstein introduced women to Weinstein for auditions. In "
        "October 2017, Epstein emailed attorney Brad Karp asking 'how bad does the Harvey "
        "Weinstein story get?' — monitoring the fallout that would eventually reach his own "
        "network. The Weinstein-Epstein connection demonstrates how entertainment industry "
        "power structures and intelligence-linked blackmail operations operated in parallel "
        "within the same social ecosystem."
    ), "aliases": "", "metadata": {"birth_year": 1952, "nationality": "American", "status": "incarcerated"}},

    {"name": "Jean-Luc Brunel", "entity_type": "person", "description": (
        "Jean-Luc Brunel (1946-2022). French model scout, agency founder, and accused sex "
        "trafficker. Epstein's primary modeling industry pipeline who funneled young women "
        "into the trafficking network through the legitimate facade of fashion recruitment."
        "\n\n"
        "MODELING CAREER: Born in Neuilly-sur-Seine, France. Began working as a scout for "
        "Karin Models in Paris in the late 1970s, eventually running the agency. Launched "
        "careers of Milla Jovovich, Christy Turlington, Sharon Stone, and Monica Bellucci. "
        "His industry credentials provided the perfect cover for identifying and accessing "
        "vulnerable young women."
        "\n\n"
        "MC2 MODEL MANAGEMENT: In 2005, Brunel transformed the Karin Models US division into "
        "MC2 Model Management, with offices in New York and Miami. Epstein wired up to $1 million "
        "to fund the launch. The name 'MC2' was an inside reference — E=MC2, with 'E' standing "
        "for Epstein. The agency operated a work visa pipeline, securing employment visas for "
        "young foreign women from Eastern Europe and Latin America, creating a paper trail of "
        "legitimate modeling work while the agency functioned as an Epstein feeder."
        "\n\n"
        "TRAFFICKING ALLEGATIONS: Virginia Giuffre alleged in a 2015 court affidavit that "
        "Epstein bragged about having 'slept with over 1,000 of Brunel's girls.' Giuffre "
        "described a system where young models recruited through legitimate-seeming agencies "
        "were funneled to Epstein. Brunel was accused of trafficking girls as young as 12."
        "\n\n"
        "ARREST AND DEATH: On December 16, 2020, Brunel was intercepted by police at Charles "
        "de Gaulle airport attempting to board a flight to Dakar, Senegal. Charged with rape "
        "of a minor, sexual assault, criminal conspiracy, and human trafficking. On February "
        "19, 2022, Brunel was found hanged with bedsheets in his cell at La Sante Prison in "
        "Paris at approximately 1:30 AM. He was not on suicide watch. The pattern echoes "
        "Epstein's death — a key witness with knowledge of the network's clients found dead "
        "in custody before trial. In 2016, Brunel had reportedly been in discussions with "
        "federal prosecutors about potentially cooperating, requesting $3 million, before "
        "backing off the deal."
    ), "aliases": "", "metadata": {"birth_year": 1946, "death_year": 2022, "nationality": "French", "status": "deceased"}},

    {"name": "Kevin Spacey", "entity_type": "person", "description": (
        "Kevin Spacey Fowler (b. 1959). Academy Award-winning actor whose career collapsed "
        "amid sexual assault allegations, with documented connections to both Jeffrey Epstein "
        "and Bill Clinton through shared travel on Epstein's private aircraft."
        "\n\n"
        "CAREER: Born in South Orange, New Jersey. Trained at Juilliard. Won Academy Awards "
        "for The Usual Suspects (1995, Supporting) and American Beauty (1999, Lead). Starred "
        "as Frank Underwood in Netflix's House of Cards (2013-2017). Served as artistic "
        "director of the Old Vic theatre in London (2004-2015)."
        "\n\n"
        "EPSTEIN FLIGHT LOGS: Named in Epstein's flight logs for a September 2002 trip to "
        "Africa aboard Epstein's Boeing 727 (the 'Lolita Express'). The eight-day trip included "
        "Bill Clinton, Chris Tucker, and other Clinton Foundation associates, ostensibly to "
        "visit HIV/AIDS project sites. In a 2024 interview, Spacey admitted to the flight and "
        "stated: 'I didn't want to be around this guy because I felt he put the president at "
        "risk on that trip to South Africa because there were these young girls.' This admission "
        "confirms both the flight and the presence of young women, while attempting to distance "
        "himself from Epstein."
        "\n\n"
        "SEXUAL ASSAULT ALLEGATIONS: In October 2017, actor Anthony Rapp alleged that Spacey "
        "made a sexual advance toward him in 1986, when Rapp was 14. Spacey responded by "
        "coming out as gay while deflecting the allegation. Over 30 additional accusers came "
        "forward, including crew members from House of Cards. Charged with felony sexual "
        "assault in Massachusetts (dropped 2019). Charged with 12 counts of sexual assault "
        "in the UK — acquitted on all charges in July 2023. Found not liable in Anthony "
        "Rapp's civil suit. Multiple civil cases remain pending."
        "\n\n"
        "NETWORK SIGNIFICANCE: Spacey's presence on the Epstein flight with Clinton illustrates "
        "how entertainment industry figures were integrated into the Epstein social network "
        "through high-profile humanitarian cover events."
    ), "aliases": "Kevin Spacey Fowler", "metadata": {"birth_year": 1959, "nationality": "American", "status": "alive"}},

    {"name": "Woody Allen", "entity_type": "person", "description": (
        "Woody Allen (b. 1935). Director, writer, and actor whose close personal friendship "
        "with Jeffrey Epstein is extensively documented in Epstein's emails and photographs, "
        "including Epstein arranging a White House visit for Allen and his wife."
        "\n\n"
        "CAREER: Born Allan Stewart Konigsberg in Brooklyn, New York. One of the most prolific "
        "filmmakers in American cinema with over 50 directed films including Annie Hall (1977), "
        "Manhattan (1979), and Midnight in Paris (2011). Four-time Academy Award winner."
        "\n\n"
        "EPSTEIN FRIENDSHIP: Allen and Epstein were longstanding friends and neighbors on "
        "Manhattan's Upper East Side who dined together regularly. Photographs show Allen and "
        "his wife Soon-Yi Previn leaving Epstein's East 71st Street townhouse in September 2013 "
        "— five years after Epstein's 2008 guilty plea to child prostitution charges. Epstein "
        "files released by the DOJ in 2026 show extensive email communication between the two, "
        "revealing that they offered each other emotional support during periods when both were "
        "being publicly criticized for sexual misconduct allegations."
        "\n\n"
        "WHITE HOUSE VISIT: In May 2015, Epstein emailed former Obama White House counsel "
        "Kathy Ruemmler: 'Could you show Soon Yi the White House. I assume Woody would be too "
        "politically sensitive?' Ruemmler responded that she could show both of them. White "
        "House records confirm Allen, Previn, and Ruemmler visited on December 27, 2015 (Obama "
        "was in Hawaii). This demonstrates Epstein's continued ability to leverage political "
        "access even after his 2008 conviction."
        "\n\n"
        "OWN ABUSE ALLEGATIONS: Separately accused of sexual abuse by adoptive daughter Dylan "
        "Farrow (allegation first made in 1992). Allen was never charged. He married Soon-Yi "
        "Previn, the adopted daughter of his former partner Mia Farrow, in 1997. Allen has "
        "denied all allegations. His social proximity to Epstein, combined with his own "
        "allegations, illustrates the network's pattern of mutual support among accused figures."
    ), "aliases": "Allan Stewart Konigsberg", "metadata": {"birth_year": 1935, "nationality": "American", "status": "alive"}},

    {"name": "Naomi Campbell", "entity_type": "person", "description": (
        "Naomi Elaine Campbell (b. 1970). British supermodel whose extensive, documented "
        "contacts with Jeffrey Epstein and Ghislaine Maxwell span over a decade, including "
        "flight logs, emails, and social events — with her name appearing over 300 times in "
        "the released Epstein files."
        "\n\n"
        "CAREER: Born in Streatham, London. Began modeling at age 15. Became one of the six "
        "original supermodels of the late 1980s/early 1990s alongside Cindy Crawford, Linda "
        "Evangelista, Christy Turlington, Claudia Schiffer, and Kate Moss. Her career spans "
        "four decades of fashion, music, and entertainment."
        "\n\n"
        "EPSTEIN CONNECTIONS: Campbell appears in the Lolita Express flight logs four times. "
        "She was listed in Epstein's personal contacts ('black book') with five separate phone "
        "numbers. Emails show she asked to borrow Epstein's jet, attended multiple Epstein "
        "parties, and traveled with him. She reportedly visited Little Saint James island. "
        "Introduced to Epstein by her former fiance Flavio Briatore."
        "\n\n"
        "MAXWELL RELATIONSHIP: Maintained a friendship with Ghislaine Maxwell independent of "
        "Epstein. Epstein files reveal Maxwell offered Campbell 'two playmates' in an email. "
        "Campbell attended a dinner at Epstein's New York home four months after his 2008 "
        "conviction — a dinner also attended by Prince Andrew. This continued social contact "
        "after Epstein's conviction is documented in emails and scheduling records."
        "\n\n"
        "POST-CONVICTION CONTACT: Campbell continued inviting Epstein to parties and events "
        "after his 2008 sex crime conviction, demonstrating how Epstein maintained social "
        "access to the entertainment elite despite his criminal record. Campbell's lawyer has "
        "stated she had no knowledge of Epstein's criminal conduct prior to his 2019 arrest."
        "\n\n"
        "Campbell has not been accused of involvement in Epstein's criminal activities."
    ), "aliases": "", "metadata": {"birth_year": 1970, "nationality": "British", "status": "alive"}},

    {"name": "Ari Emanuel", "entity_type": "person", "description": (
        "Ariel Zev Emanuel (b. 1961). CEO of Endeavor (parent of WME talent agency), CEO and "
        "executive chairman of TKO Group Holdings (UFC/WWE). One of the most powerful figures "
        "in Hollywood whose position at the apex of the entertainment industry intersects "
        "with the broader power network through family and business connections."
        "\n\n"
        "FAMILY: Son of Benjamin Emanuel, a pediatrician who was active in the Irgun in "
        "Mandatory Palestine. Brother of Rahm Emanuel (White House Chief of Staff under Obama, "
        "Mayor of Chicago, US Ambassador to Japan) and Ezekiel Emanuel (oncologist and "
        "bioethicist). The Emanuel family bridges entertainment, politics, and healthcare "
        "policy at the highest levels."
        "\n\n"
        "CAREER: Founded Endeavor Talent Agency and orchestrated its 2009 merger with the "
        "William Morris Agency to create WME — the most powerful talent agency in Hollywood. "
        "Took Endeavor public in 2021. Represents over 1,000 A-list clients. Described by the "
        "New York Times as 'the pre-eminent power player in Hollywood.' Net worth estimated "
        "at over $1 billion."
        "\n\n"
        "NETWORK SIGNIFICANCE: Emanuel's position makes him a gatekeeper of the entertainment "
        "industry. He was reportedly involved in efforts to manage the fallout from the "
        "Weinstein scandal through talent agency channels. His rival Casey Wasserman — the "
        "LA 2028 Olympics chief — appeared in the Epstein files with flight logs and suggestive "
        "emails with Ghislaine Maxwell, and has accused Emanuel of fueling outrage over those "
        "revelations. Emanuel is interested in acquiring parts of Wasserman's agency as it "
        "is forced to sell. The Weinstein-era Hollywood power dynamics reveal how talent agency "
        "executives function as nodes connecting entertainment, politics, and media control."
    ), "aliases": "Ariel Emanuel", "metadata": {"birth_year": 1961, "nationality": "American", "status": "alive"}},

    {"name": "Les Moonves", "entity_type": "person", "description": (
        "Leslie Roy Moonves (b. 1949). Former Chairman and CEO of CBS Corporation whose "
        "sexual misconduct closely parallels Weinstein's and Epstein's patterns, combined "
        "with documented use of law enforcement to suppress allegations — illustrating how "
        "media gatekeepers participate in the same systems of coercion they are positioned "
        "to expose."
        "\n\n"
        "CBS CAREER: Born in Brooklyn, New York. Rose through the entertainment industry from "
        "acting to executive positions at Lorimar Television and Warner Bros. Television "
        "(where he greenlighted Friends and ER). Joined CBS in 1995 as president of CBS "
        "Entertainment, eventually becoming Chairman and CEO of CBS Corporation in 2006."
        "\n\n"
        "SEXUAL MISCONDUCT: Ronan Farrow's reporting in The New Yorker (2018) led to "
        "allegations from 12 women spanning decades — ranging from forced oral sex to "
        "forcible touching and career retaliation. Lawyers investigating CBS found credible "
        "evidence that Moonves received oral sex from at least four employees under "
        "'transactional and improper' circumstances. Moonves was 'evasive and untruthful,' "
        "deleted hundreds of texts, and gave investigators his son's iPad instead of his own."
        "\n\n"
        "LAPD CONSPIRACY: An LAPD captain met personally with Moonves and fed him confidential "
        "information about active investigations into his sexual assault allegations. CBS and "
        "Moonves were ordered to pay $30.5 million to the NY Attorney General for insider "
        "trading and concealing sexual assault allegations from investors."
        "\n\n"
        "EPSTEIN CONNECTION: Moonves appears in Epstein's records sharing two flights on "
        "Epstein's aircraft. Epstein monitored the #MeToo fallout affecting Moonves in 2017 "
        "emails, tracking which powerful men were being accused and advising some behind the "
        "scenes. Moonves was among the names Epstein discussed in email correspondence with "
        "publicist Peggy Siegal."
        "\n\n"
        "MEDIA SUPPRESSION: CBS's corporate culture under Moonves exemplified how media "
        "organizations could function as protective shields for powerful predators. Ronan "
        "Farrow's reporting revealed a 'culture of impunity' at the network. ABC News anchor "
        "Amy Robach was separately caught on a hot mic in 2019 stating that ABC had killed "
        "her Epstein story three years earlier under pressure from Buckingham Palace — "
        "demonstrating the broader pattern of network-level story suppression protecting the "
        "Epstein network."
    ), "aliases": "Leslie Moonves", "metadata": {"birth_year": 1949, "nationality": "American", "status": "alive"}},

    # ---- Organizations ----
    {"name": "MC2 Model Management", "entity_type": "organization", "description": (
        "MC2 Model Management. Modeling agency founded in 2005 by Jean-Luc Brunel with up to "
        "$1 million in funding from Jeffrey Epstein. The name was an inside reference to "
        "Einstein's E=MC2 equation, with 'E' standing for Epstein. Operated offices in New "
        "York City and Miami. Served as a legitimate commercial front that simultaneously "
        "functioned as a trafficking pipeline — securing work visas for young foreign women "
        "from Eastern Europe and Latin America, creating paper trails of legitimate modeling "
        "employment while providing Epstein access to vulnerable young models. Virginia "
        "Giuffre's 2014 court filing alleged the agency was a cover for sex trafficking. "
        "Brunel quietly sold off MC2's assets after Epstein's 2019 arrest."
    ), "aliases": "MC2 Models"},

    {"name": "Black Cube", "entity_type": "organization", "description": (
        "Black Cube (BC Strategy Ltd). Private intelligence firm founded in 2010 by former "
        "Israeli intelligence officers Dan Zorella and Avi Yanus. Based in London, Tel Aviv, "
        "and Madrid. Staffed by former members of Mossad and Aman (Israeli military "
        "intelligence). Board included former Mossad director Meir Dagan (honorary president, "
        "deceased) and former Mossad director Efraim Halevy. Clients include wealthy "
        "individuals, oligarchs, and global corporations. Most notoriously hired by Harvey "
        "Weinstein — on referral from former Israeli PM Ehud Barak — to surveil, infiltrate, "
        "and discredit sexual assault accusers and investigative journalists. Operatives used "
        "fabricated identities to approach targets at The New Yorker, New York Times, and New "
        "York magazine, compiling psychological profiles focusing on personal and sexual "
        "histories. The Barak-Weinstein-Black Cube triangle connects directly to the Epstein "
        "network: Barak co-founded Carbyne with Epstein investment, received Wexner Foundation "
        "money, and was photographed entering Epstein's Manhattan residence. Black Cube "
        "represents the privatization of Israeli intelligence capabilities for the protection "
        "of predators within the same network."
    ), "aliases": "BC Strategy Ltd"},

    {"name": "Victoria's Secret", "entity_type": "organization", "description": (
        "Victoria's Secret. Lingerie brand owned by Les Wexner's L Brands (The Limited). "
        "Epstein exploited his relationship with Wexner to pose as a Victoria's Secret "
        "talent recruiter, using business cards identifying himself as a VS scout. Multiple "
        "victims reported being lured by promises of modeling work for the brand. Actress "
        "Alicia Arden filed a 1997 police report stating Epstein misrepresented himself as "
        "a VS recruiter before an alleged assault. Model Elisabetta Tai reported being given "
        "Epstein's address by her booker in 2004, told he was 'one of the most important "
        "people in modeling.' In 1993, a female L Brands executive informed Wexner that "
        "Epstein was posing as a VS recruiter — Wexner's attorney said he 'confronted Epstein' "
        "but did not sever the financial relationship until 2007. Maria Farmer reported an "
        "assault by Epstein and Maxwell at Wexner's Ohio property in 1996. The Victoria's "
        "Secret pipeline demonstrates how Epstein weaponized a legitimate corporate brand "
        "as recruitment infrastructure for trafficking."
    ), "aliases": "VS"},

    # ---- Events ----
    {"name": "Jean-Luc Brunel Death (2022)", "entity_type": "event", "description": (
        "On February 19, 2022, Jean-Luc Brunel was found hanged with bedsheets in his cell "
        "at La Sante Prison in Paris at approximately 1:30 AM. He was being held on charges "
        "of rape of a minor, sexual assault, criminal conspiracy, and human trafficking — all "
        "involving minors. He was not on suicide watch. Prison guards conducted five overnight "
        "checks, and corridor video confirmed no checks were missed. An investigation into "
        "the cause of death was opened, 'as is systematically done in these cases.' Brunel "
        "had been arrested on December 16, 2020 at Charles de Gaulle airport while attempting "
        "to flee to Senegal. The death of a second key Epstein network figure in custody — "
        "under strikingly similar circumstances to Epstein's own death (hanging, pre-trial, "
        "key witness) — raised questions about whether individuals with knowledge of the "
        "network's clients were being silenced. In 2016, Brunel had reportedly been in "
        "discussions about cooperating with US prosecutors."
    ), "aliases": "Brunel Death"},
]

RELATIONSHIPS = [
    # ---- Harvey Weinstein ----
    {"source": "Harvey Weinstein", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "credible", "desc": "Socialized in overlapping New York circles. Shared a regular table at a Hamptons restaurant. Part of investor group attempting to buy New York Magazine (2003). Epstein monitored Weinstein's #MeToo fallout in emails.", "sources": [99, 114]},
    {"source": "Harvey Weinstein", "target": "Black Cube", "type": "employed_by", "tier": "documented", "desc": "Hired Black Cube in 2016 to surveil and discredit sexual assault accusers and journalists. Operatives used fabricated identities to infiltrate newsrooms.", "sources": [96, 97]},
    {"source": "Harvey Weinstein", "target": "Ehud Barak", "type": "connected_to", "tier": "credible", "desc": "Barak personally referred Weinstein to Black Cube. Both attended a Hillary Clinton fundraiser with Black Cube co-founder Dan Zorella.", "sources": [101]},
    {"source": "Harvey Weinstein", "target": "Ghislaine Maxwell", "type": "associate_of", "tier": "credible", "desc": "Maxwell attended Weinstein film premieres and parties. Maria Farmer recalled Maxwell speaking of a film executive named 'Harvey.'", "sources": [99]},

    # ---- Jean-Luc Brunel ----
    {"source": "Jean-Luc Brunel", "target": "Jeffrey Epstein", "type": "co_conspirator_of", "tier": "documented", "desc": "Epstein funded MC2 Model Management (up to $1M). Brunel supplied young models to Epstein. Giuffre affidavit: Epstein bragged about sleeping with 'over 1,000 of Brunel's girls.'", "sources": [110, 111, 102]},
    {"source": "Jean-Luc Brunel", "target": "MC2 Model Management", "type": "member_of", "tier": "documented", "desc": "Founded MC2 in 2005 with Epstein financing. Operated offices in New York and Miami as modeling front and trafficking pipeline.", "sources": [111]},
    {"source": "Jean-Luc Brunel", "target": "Ghislaine Maxwell", "type": "co_conspirator_of", "tier": "credible", "desc": "Both part of Epstein's inner circle of procurers. Brunel supplied models from the fashion industry while Maxwell recruited from social circles.", "sources": [110, 29]},
    {"source": "Jean-Luc Brunel", "target": "Jean-Luc Brunel Death (2022)", "type": "connected_to", "tier": "documented", "desc": "Found hanged in La Sante Prison on February 19, 2022 while awaiting trial on trafficking charges.", "sources": [102]},

    # ---- Kevin Spacey ----
    {"source": "Kevin Spacey", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Named in Epstein flight logs. Flew on Epstein's Boeing 727 to Africa in September 2002. Spacey admitted to the flight in 2024, acknowledging 'young girls' were present.", "sources": [30, 103]},
    {"source": "Kevin Spacey", "target": "Bill Clinton", "type": "associate_of", "tier": "documented", "desc": "Traveled together on Epstein's plane to Africa in 2002 for Clinton Foundation HIV/AIDS project sites. Spacey stated Clinton invited him on the trip.", "sources": [30, 103]},

    # ---- Woody Allen ----
    {"source": "Woody Allen", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "documented", "desc": "Longstanding friends and Upper East Side neighbors. Dined regularly. Photographed leaving Epstein's townhouse in 2013 (post-conviction). Epstein arranged White House visit for Allen in 2015.", "sources": [105, 112]},

    # ---- Steve Bing ----
    {"source": "Steve Bing", "target": "Bill Clinton", "type": "patron_of", "tier": "documented", "desc": "Donated $10M+ to Clinton Foundation. Funded Clinton's North Korea rescue mission plane (2009). Left trust with Clinton Foundation as sole beneficiary.", "sources": [104]},
    {"source": "Steve Bing", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "credible", "desc": "Part of same 'hard-partying' Clinton social circle that included Epstein. Briefly socialized with Epstein. Moved in overlapping New York and political donor networks.", "sources": [104, 113]},

    # ---- Naomi Campbell ----
    {"source": "Naomi Campbell", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "documented", "desc": "Named 300+ times in Epstein files. Flight logs (4 flights), black book (5 phone numbers), emails requesting use of Epstein's jet. Attended Epstein parties post-2008 conviction.", "sources": [30, 106, 112]},
    {"source": "Naomi Campbell", "target": "Ghislaine Maxwell", "type": "associate_of", "tier": "documented", "desc": "Maintained independent friendship with Maxwell. Maxwell offered Campbell 'two playmates' in documented email. Attended dinner at Epstein's home with Prince Andrew after 2008 conviction.", "sources": [106, 112]},

    # ---- Ari Emanuel ----
    {"source": "Ari Emanuel", "target": "Harvey Weinstein", "type": "connected_to", "tier": "credible", "desc": "As head of the most powerful talent agency, Emanuel operated in the same Hollywood power ecosystem as Weinstein. Engaged in public disputes over handling of Weinstein-related claims through talent agencies.", "sources": [113]},

    # ---- Les Moonves ----
    {"source": "Les Moonves", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Shared two flights on Epstein's aircraft per flight log records. Epstein monitored Moonves in 2017 #MeToo tracking emails.", "sources": [30, 114]},

    # ---- MC2 / Epstein funding ----
    {"source": "Jeffrey Epstein", "target": "MC2 Model Management", "type": "financed_by", "tier": "documented", "desc": "Epstein wired up to $1 million to fund MC2's 2005 launch. The agency name (E=MC2) was an inside joke referencing Epstein.", "sources": [111]},

    # ---- Black Cube / Intelligence network ----
    {"source": "Black Cube", "target": "Mossad", "type": "connected_to", "tier": "credible", "desc": "Founded by former Mossad/Aman officers. Board included two former Mossad directors (Meir Dagan, Efraim Halevy). Recruits from Israeli intelligence because operatives 'know how to look for weak points.'", "sources": [97, 101]},
    {"source": "Ehud Barak", "target": "Black Cube", "type": "connected_to", "tier": "documented", "desc": "Referred Weinstein to Black Cube. Admitted putting the producer in touch with the agency. Connecting Epstein's intelligence network to Weinstein's counter-investigation apparatus.", "sources": [101]},

    # ---- Victoria's Secret pipeline ----
    {"source": "Victoria's Secret", "target": "Les Wexner", "type": "connected_to", "tier": "documented", "desc": "Owned by Wexner's L Brands. Epstein exploited Wexner's ownership to pose as VS talent recruiter.", "sources": [115, 39]},
    {"source": "Jeffrey Epstein", "target": "Victoria's Secret", "type": "connected_to", "tier": "documented", "desc": "Used VS brand as recruitment lure. Carried business cards identifying himself as VS scout. Multiple victims reported being approached via fake VS modeling opportunities.", "sources": [115, 39]},

    # ---- Brunel Death event ----
    {"source": "Jean-Luc Brunel Death (2022)", "target": "Epstein Death (2019)", "type": "connected_to", "tier": "inference", "desc": "Second key Epstein network witness found hanged in custody before trial. Same method (hanging), same context (pre-trial, facing trafficking charges), same outcome (network secrets die with witness).", "sources": [102]},

    # ---- Cross-cluster connections ----
    {"source": "Harvey Weinstein", "target": "Bill Clinton", "type": "connected_to", "tier": "credible", "desc": "Both attended the same social and political events. Weinstein was a major Democratic donor. Moved in overlapping political-entertainment circles.", "sources": [99]},
    {"source": "Steve Bing", "target": "Ghislaine Maxwell", "type": "connected_to", "tier": "inference", "desc": "Moved in overlapping Clinton-Epstein social circles. Both part of the same New York political donor and entertainment network.", "sources": [104]},
    {"source": "Les Moonves", "target": "Harvey Weinstein", "type": "connected_to", "tier": "credible", "desc": "Both subjects of Ronan Farrow's reporting on sexual predation in entertainment. Both used power positions to coerce and suppress allegations. Epstein tracked both in #MeToo monitoring emails.", "sources": [96, 114]},
]

ENTITY_SOURCES = {
    "Harvey Weinstein": [96, 97, 99, 101, 108, 113, 114],
    "Jean-Luc Brunel": [29, 102, 110, 111, 112],
    "Kevin Spacey": [30, 103, 112],
    "Woody Allen": [105, 112],
    "Naomi Campbell": [30, 106, 112],
    "Ari Emanuel": [113],
    "Les Moonves": [30, 98, 107, 109, 114],
    "MC2 Model Management": [110, 111],
    "Black Cube": [96, 97, 101],
    "Victoria's Secret": [39, 115],
    "Jean-Luc Brunel Death (2022)": [102],
}
