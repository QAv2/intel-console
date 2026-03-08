"""
Hollywood Predator Network & Adjacent Cases — Expansion layer for Intel Console.
Entities: Entertainment industry figures with documented sexual predation patterns,
trafficking convictions, or direct appearance in Epstein files — plus adjacent
cases (John of God) connected through documented endorsement chains.

This expansion maps the broader entertainment-predator ecosystem that operated
alongside and overlapping with the Epstein network: convicted traffickers (R. Kelly,
Diddy, John of God), accused predators with documented evidence (Russell Simmons),
enablers through platform (Oprah/John of God), and figures named in Epstein files
(DiCaprio via ex-girlfriend Riabenkova's emails to Epstein).

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# HOLLYWOOD PREDATOR NETWORK & ADJACENT CASES
# Sources 1329-1370, Entities, Relationships, Entity-Sources
# ============================================================

SOURCES = [
    # ---- Leonardo DiCaprio / Riabenkova / Epstein files ----
    {"id": 1329, "title": "Hollywood Reporter — Inside Jeffrey Epstein's Hollywood: The Stars, Moguls, Directors, Producers and Fixers in His Orbit", "url": "https://www.hollywoodreporter.com/news/general-news/jeffrey-epstein-hollywood-orbit-1236508954/", "source_type": "journalism", "year": 2026},
    {"id": 1330, "title": "Yahoo News UK — Why Leonardo DiCaprio's Name Appears in the Epstein Files Several Times", "url": "https://uk.news.yahoo.com/why-leonardo-dicaprios-name-appears-095900309.html", "source_type": "journalism", "year": 2026},
    {"id": 1331, "title": "Sunday Guardian — Do Epstein Files Link Leonardo DiCaprio to Crimes? Here's What the Records Actually Show", "url": "https://sundayguardianlive.com/world/fact-check-do-epstein-files-link-leonardo-dicaprio-to-crimes-or-conspiracy-claims-heres-what-the-records-actually-show-171519/", "source_type": "journalism", "year": 2026},
    {"id": 1332, "title": "FandomWire — Truth Behind Leonardo DiCaprio's Relationship With Alesia Riabenkova and Her Emails to Epstein", "url": "https://fandomwire.com/truth-behind-leonardo-dicaprio-relationship-with-alesia-riabenkova-and-her-emails-to-epstein/", "source_type": "journalism", "year": 2026},
    {"id": 1333, "title": "DOJ Epstein Library — Dataset 11 (Riabenkova email correspondence)", "url": "https://www.justice.gov/epstein", "source_type": "government", "year": 2026},

    # ---- Oprah Winfrey / John of God ----
    {"id": 1334, "title": "Washington Post — Celebrity Brazilian Healer 'John of God,' Once Featured by Oprah, Surrenders on Sexual Abuse Charges", "url": "https://www.washingtonpost.com/nation/2018/12/17/celebrity-brazilian-healer-john-god-once-featured-by-oprah-surrenders-sexual-abuse-charges/", "source_type": "journalism", "year": 2018},
    {"id": 1335, "title": "BuzzFeed News — John Of God Was Once Hyped By Oprah. Now He's Accused Of Abusing Hundreds Of Women", "url": "https://www.buzzfeednews.com/article/hayesbrown/john-god-joao-deus-brazil-healer-allegations-sexual-abuse", "source_type": "journalism", "year": 2018},
    {"id": 1336, "title": "CNN — Brazilian Healer João Teixeira de Faria Accused of Sexually Abusing More Than 300 Women", "url": "https://www.cnn.com/2018/12/17/americas/brazilian-healer-sexual-abuse-accusations", "source_type": "journalism", "year": 2018},
    {"id": 1337, "title": "Fox News — Brazilian Spiritual Healer, Spotlighted by Oprah, to Stand Trial on Rape, Sex Abuse Charges", "url": "https://www.foxnews.com/world/brazilian-spiritual-healer-spotlighted-by-oprah-to-stand-trial-on-rape-sex-abuse-charges", "source_type": "journalism", "year": 2019},
    {"id": 1338, "title": "OpIndia — 'John of God' Now Faces 370 Years in Jail: How This 'Faith Healer' Exploited and Raped Hundreds of Believers", "url": "https://www.opindia.com/2023/07/john-of-god-celebrity-faith-healer-promoted-by-oprah-370-year-prison-sentence-after-600-accusations-of-sexual-exploitation/", "source_type": "journalism", "year": 2023},
    {"id": 1339, "title": "Gateway Hispanic — Brazilian Healer John of God Sentenced to 118 Years for Sexual Rapes", "url": "https://gatewayhispanic.com/2026/03/brazilian-healer-john-god-promoted-oprah-winfrey-as/", "source_type": "journalism", "year": 2026},
    {"id": 1340, "title": "ABC News — Brazilian Spiritual Healer 'John of God' Indicted for Rape, Accused of Sexually Abusing Nearly 600 Women", "url": "https://abcnews.com/International/brazilian-spiritual-healer-john-god-indicted-rape-accused/story?id=60019325", "source_type": "journalism", "year": 2019},

    # ---- Sean "Diddy" Combs ----
    {"id": 1341, "title": "DOJ SDNY — Sean Combs Charged in Manhattan Federal Court With Sex Trafficking and Other Federal Offenses", "url": "https://www.justice.gov/usao-sdny/pr/sean-combs-charged-manhattan-federal-court-sex-trafficking-and-other-federal-offenses", "source_type": "government", "year": 2024},
    {"id": 1342, "title": "DOJ SDNY — United States v. Sean Combs Indictment (Full Text)", "url": "https://www.justice.gov/usao-sdny/media/1368556/dl", "source_type": "court", "year": 2024},
    {"id": 1343, "title": "CNN — Takeaways From the Racketeering Conspiracy and Sex Trafficking Indictment Against Sean 'Diddy' Combs", "url": "https://www.cnn.com/2024/09/17/us/takeaways-indictment-sean-diddy-combs", "source_type": "journalism", "year": 2024},
    {"id": 1344, "title": "CBS News — Sean 'Diddy' Combs Acquitted of Sex Trafficking and Racketeering, Convicted on Prostitution-Related Counts", "url": "https://www.cbsnews.com/news/sean-diddy-combs-trial-verdict-jury/", "source_type": "journalism", "year": 2025},
    {"id": 1345, "title": "NPR — Sean 'Diddy' Combs Indicted on Additional Sex Trafficking Charges", "url": "https://www.npr.org/2025/04/04/g-s1-58294/sean-diddy-combs-new-trafficking-charges", "source_type": "journalism", "year": 2025},
    {"id": 1346, "title": "Hollywood Reporter — The Creepy Parallels Between the Epstein and Diddy Cases", "url": "https://www.hollywoodreporter.com/news/general-news/sean-diddy-combs-jeffrey-epstein-conspiracy-theories-1236309805/", "source_type": "journalism", "year": 2024},
    {"id": 1347, "title": "Washington Post — Sean 'Diddy' Combs Indictment, Charges on Sex Trafficking, Racketeering Broken Down", "url": "https://www.washingtonpost.com/style/2024/09/17/diddy-indictment-charges-sex-trafficking-racketeering-takeaways/", "source_type": "journalism", "year": 2024},

    # ---- Russell Simmons ----
    {"id": 1348, "title": "Rolling Stone — Russell Simmons Owed Millions to His Accusers. Have They Finally Found Justice?", "url": "https://www.rollingstone.com/music/music-features/russell-simmons-sexual-misconduct-assault-lawsuit-1235448701/", "source_type": "journalism", "year": 2024},
    {"id": 1349, "title": "Billboard — A Timeline of Russell Simmons' Sexual Misconduct Allegations", "url": "https://www.billboard.com/lists/russell-simmons-sexual-misconduct-allegations-timeline/", "source_type": "journalism", "year": 2018},
    {"id": 1350, "title": "Variety — Brett Ratner and Russell Simmons Accused of Working Together to Carry Out Sexual Misconduct", "url": "https://variety.com/2017/biz/news/brett-ratner-russell-simmons-teaming-up-sexual-misconduct-1202618675/", "source_type": "journalism", "year": 2017},
    {"id": 1351, "title": "Consequence of Sound — Russell Simmons, Accused of Sexual Assault, Jets Off to Extradition-Free Bali", "url": "https://consequence.net/2018/07/russell-simmons-bali/", "source_type": "journalism", "year": 2018},
    {"id": 1352, "title": "Black Enterprise — Russell Simmons Accused of Using Indonesian Retirement to Dodge Sexual Assault Lawsuit", "url": "https://www.blackenterprise.com/russell-simmons-indonesian-retirement-sexual-assault-lawsuit/", "source_type": "journalism", "year": 2024},

    # ---- R. Kelly ----
    {"id": 1353, "title": "DOJ — R. Kelly Sentenced to 30 Years in Prison for Sex Trafficking (SDNY)", "url": "", "source_type": "court", "year": 2022},
    {"id": 1354, "title": "CNN — R. Kelly Sentenced to 30 Years in Prison for Federal Racketeering and Sex Trafficking Charges", "url": "https://www.cnn.com/2022/06/29/us/r-kelly-sentencing-racketeering-sex-trafficking", "source_type": "journalism", "year": 2022},
    {"id": 1355, "title": "PBS — Federal Appeals Court Upholds R. Kelly's Convictions and 30-Year Prison Sentence", "url": "https://www.pbs.org/newshour/nation/federal-appeals-court-upholds-singer-r-kellys-convictions-and-30-year-prison-sentence", "source_type": "journalism", "year": 2025},
    {"id": 1356, "title": "NPR — R. Kelly Is Sentenced to 30 Years in Prison for Sex Crimes and Racketeering", "url": "https://www.npr.org/2022/06/29/1105551227/r-kelly-sentence-30-years", "source_type": "journalism", "year": 2022},
    {"id": 1357, "title": "Washington Post — R. Kelly Sentenced to 30 Years for Sex Trafficking, Racketeering Convictions", "url": "https://www.washingtonpost.com/arts-entertainment/2022/06/29/r-kelly-sentenced-sex-trafficking-racketeering/", "source_type": "journalism", "year": 2022},
    {"id": 1358, "title": "ICE — Chicago Recording Artist 'R. Kelly' Indicted and Arrested on Federal Child Pornography, Obstruction Charges", "url": "https://www.ice.gov/news/releases/chicago-recording-artist-r-kelly-indicted-and-arrested-federal-child-pornography", "source_type": "government", "year": 2019},

    # ---- John of God (court records) ----
    {"id": 1359, "title": "Goiás State Court — João Teixeira de Faria Sentencing (cumulative 489+ years for rape and sexual abuse)", "url": "", "source_type": "court", "year": 2023},
    {"id": 1360, "title": "IJNET — Q&A with Brazilian Journalist Whose Investigation Put an End to John of God's Sex Crimes", "url": "https://ijnet.org/en/story/qa-brazilian-journalist-whose-investigation-put-end-john-god%E2%80%99s-sex-crimes", "source_type": "journalism", "year": 2019},

    # ---- Cross-reference: Diddy in Epstein files ----
    {"id": 1361, "title": "Shockya — The Epstein Web That Connects Jay-Z, Diddy, Alex Spiro, and a Dead Russian Senator", "url": "https://www.shockya.com/news/2026/03/03/the-epstein-web-that-connects-jay-z-diddy-alex-spiro-and-a-dead-russian-senator-umar-dzhabrailov/", "source_type": "journalism", "year": 2026},

    # ---- Brett Ratner in Epstein files (cross-ref for Simmons) ----
    {"id": 1362, "title": "Variety — Brett Ratner Denies 'Personal Relationship' With Jeffrey Epstein", "url": "https://variety.com/2026/politics/global/brett-jeffrey-epstein-files-horrible-denies-1236650608/", "source_type": "journalism", "year": 2026},
    {"id": 1363, "title": "Daily Beast — Melania Doc Director Found in Creepy Epstein Files Photos", "url": "https://www.thedailybeast.com/melania-doc-director-found-in-creepy-epstein-files-photos/", "source_type": "journalism", "year": 2026},
]

ENTITIES = [
    # ---- Leonardo DiCaprio ----
    {"name": "Leonardo DiCaprio", "entity_type": "person", "description": (
        "Leonardo Wilhelm DiCaprio (b. 1974). Academy Award-winning actor whose name appears "
        "multiple times in DOJ-released Epstein files, though not in flight logs or direct "
        "correspondence with Epstein."
        "\n\n"
        "CAREER: Born in Los Angeles. Breakthrough in What's Eating Gilbert Grape (1993), "
        "global stardom via Titanic (1997). Academy Award for The Revenant (2015). Founded "
        "the Leonardo DiCaprio Foundation (environmental advocacy) in 1998. One of the "
        "highest-grossing actors of all time."
        "\n\n"
        "EPSTEIN FILE MENTIONS: DiCaprio's name appears in DOJ-released Epstein documents in "
        "two contexts. First, a 2016 email exchange involving Deepak Chopra's account discussed "
        "arranging a dinner: 'do you think leo dicaprio would want to have dinner with woody' "
        "(referring to Woody Allen, Epstein's close friend). No confirmation that the dinner "
        "occurred. Second, a June 2009 email from former UK minister Peter Mandelson asked "
        "Epstein whether international companies might secure DiCaprio's endorsement. Neither "
        "email was written by or to DiCaprio."
        "\n\n"
        "RIABENKOVA CONNECTION: Alesia Riabenkova, a Latvian-born model who briefly dated "
        "DiCaprio in 2013, appears in DOJ Dataset 11 exchanging emails with Epstein. The "
        "emails allegedly include affectionate language, references to 'Leo,' and offers to "
        "'find a little girl' while describing Eastern Europe as a better location for finding "
        "young women. These emails are attributed to Riabenkova's account and do not implicate "
        "DiCaprio directly, but establish that a woman in his social orbit was in direct contact "
        "with Epstein's procurement language."
        "\n\n"
        "IMPORTANT LIMITATIONS: Court testimony and flight logs do not list DiCaprio as a "
        "passenger or close associate of Epstein. No verified evidence shows DiCaprio ever met "
        "Epstein, socialized with him, or knew about his criminal activities. Multiple fact-checks "
        "confirm that extreme viral claims about DiCaprio derived from the files are fabrications "
        "(e.g., 'cannibal diet' claim originated from The People's Voice, a known disinformation site)."
    ), "aliases": "Leo DiCaprio", "metadata": {"birth_year": 1974, "nationality": "American", "status": "alive"}},

    # ---- Oprah Winfrey ----
    {"name": "Oprah Winfrey", "entity_type": "person", "description": (
        "Oprah Gail Winfrey (b. 1954). Media mogul, television host, and philanthropist whose "
        "platform amplified João Teixeira de Faria ('John of God') to a global audience before "
        "his arrest and conviction for the serial rape and sexual abuse of over 600 women and girls."
        "\n\n"
        "CAREER: Born in Kosciusko, Mississippi. Hosted The Oprah Winfrey Show (1986-2011), "
        "the highest-rated daytime talk show in American history. Founded Harpo Productions "
        "and OWN (Oprah Winfrey Network). Named the richest African American of the 20th century "
        "by Forbes. Net worth estimated at $2.5 billion."
        "\n\n"
        "JOHN OF GOD ENDORSEMENT: In 2010, Winfrey devoted a full episode of her show to "
        "João Teixeira de Faria, presenting him as a miraculous faith healer and broadcasting "
        "his 'Casa de Dom Inácio de Loyola' clinic in Abadiânia, Brazil to millions of viewers "
        "worldwide. In 2012, Winfrey traveled to Brazil to record an episode of Oprah's Next "
        "Chapter at Faria's clinic, further amplifying his reputation. These endorsements "
        "extended Faria's reach internationally, drawing thousands of additional visitors — "
        "including vulnerable women seeking healing — to his compound."
        "\n\n"
        "FARIA'S CRIMES: In December 2018, following investigative journalism by Globo TV, "
        "over 600 women accused Faria of sexual abuse, rape, and exploitation of vulnerable "
        "people seeking spiritual healing. He was arrested and has accumulated sentences "
        "exceeding 489 years in prison. Allegations also surfaced of a baby trafficking "
        "operation. The scale of his predation — spanning decades, enabled by celebrity "
        "endorsement and institutional protection — parallels the Epstein pattern of using "
        "legitimate social cover to access victims."
        "\n\n"
        "RESPONSE: After allegations became public, Winfrey deleted the episodes from her "
        "platforms and released a statement expressing hope that justice would be served. "
        "Winfrey has not been accused of knowledge of or complicity in Faria's crimes."
    ), "aliases": "", "metadata": {"birth_year": 1954, "nationality": "American", "status": "alive"}},

    # ---- João Teixeira de Faria (John of God) ----
    {"name": "João Teixeira de Faria", "entity_type": "person", "description": (
        "João Teixeira de Faria (b. 1942), known as 'John of God' (João de Deus). Brazilian "
        "self-proclaimed faith healer convicted of the serial rape and sexual abuse of over "
        "600 women and girls over decades, while operating under the guise of spiritual healing."
        "\n\n"
        "OPERATIONS: Opened Casa de Dom Inácio de Loyola in Abadiânia, Goiás, Brazil in the "
        "late 1970s, claiming to perform 'spiritual surgeries' and channel healing entities. "
        "The clinic drew an estimated 10,000+ visitors per week at its peak, including "
        "international celebrities, politicians, and desperate patients. Faria exploited the "
        "power dynamic inherent in spiritual authority — victims who came seeking healing were "
        "sexually abused under the guise of 'treatment' in private rooms."
        "\n\n"
        "CELEBRITY ENDORSEMENT: Featured on The Oprah Winfrey Show (2010) and Oprah's Next "
        "Chapter (2012), which exponentially expanded his international reach. Also endorsed "
        "by various New Age figures and wellness influencers."
        "\n\n"
        "ARREST AND CONVICTION: In December 2018, following Globo TV investigative reporting, "
        "over 600 women came forward with accusations of sexual abuse, rape, and exploitation. "
        "Faria surrendered to police on December 16, 2018. He has been convicted in multiple "
        "trials with cumulative sentences exceeding 489 years in prison (including an additional "
        "99-year sentence in 2023 and 118 years in a subsequent ruling). Currently serving "
        "sentences under house arrest pending appeals."
        "\n\n"
        "BABY TRAFFICKING: Brazilian activist Sabrina Bittencourt alleged Faria ran a baby "
        "trafficking operation where children were 'farmed' in Brazil and sold to childless "
        "couples internationally. Bittencourt died in February 2019, reportedly by suicide, "
        "shortly after making these allegations public."
        "\n\n"
        "PATTERN SIGNIFICANCE: Faria's case demonstrates the faith healer / spiritual authority "
        "variant of the predator-enablement pattern: legitimate social cover (healing ministry), "
        "celebrity endorsement (Oprah), institutional protection (local political connections), "
        "and exploitation of the vulnerable (sick people seeking cures). The whistleblower's "
        "death echoes the pattern of witnesses dying before testimony."
    ), "aliases": "John of God, João de Deus", "metadata": {"birth_year": 1942, "nationality": "Brazilian", "status": "incarcerated"}},

    # ---- Sean "Diddy" Combs ----
    {"name": "Sean Combs", "entity_type": "person", "description": (
        "Sean John Combs (b. 1969), known as Puff Daddy, P. Diddy, and Diddy. Music mogul, "
        "record producer, and founder of Bad Boy Entertainment, indicted on federal racketeering "
        "and sex trafficking charges in 2024 — the most high-profile entertainment industry "
        "trafficking prosecution since Epstein."
        "\n\n"
        "CAREER: Born in Harlem, New York. Founded Bad Boy Records in 1993. Launched the "
        "careers of The Notorious B.I.G., Mary J. Blige, and others. Built a business empire "
        "spanning music (Bad Boy), fashion (Sean John), spirits (Cîroc vodka), and media "
        "(Revolt TV). Forbes estimated peak net worth at $1 billion."
        "\n\n"
        "FEDERAL INDICTMENT (2024): On September 16, 2024, a federal grand jury in the "
        "Southern District of New York indicted Combs on three counts: racketeering conspiracy, "
        "sex trafficking by force/fraud/coercion, and transportation to engage in prostitution. "
        "The indictment described a 'Combs Enterprise' — a criminal organization using his "
        "business entities (Bad Boy Entertainment, Combs Enterprises, etc.) and employees "
        "(security, household staff, personal assistants) to facilitate sex trafficking, forced "
        "labor, kidnapping, arson, bribery, and obstruction of justice spanning decades."
        "\n\n"
        "'FREAK OFFS': The indictment described elaborate multi-day sexual events Combs called "
        "'Freak Offs,' involving coerced victims and male commercial sex workers at luxury "
        "properties. Staff arranged travel, booked hotel rooms, stocked them with drugs/baby "
        "oil/lubricant, cleaned afterward, and provided cash to pay sex workers. Hidden cameras "
        "allegedly captured activity — echoing the Epstein pattern of surveillance-based kompromat."
        "\n\n"
        "TRIAL OUTCOME (2025): On July 2, 2025, a jury found Combs not guilty of racketeering "
        "conspiracy and sex trafficking, but guilty on two counts of transportation for purposes "
        "of prostitution. On October 3, 2025, sentenced to 4 years and 2 months in prison, "
        "a $500,000 fine, and 5 years of supervised release."
        "\n\n"
        "EPSTEIN PARALLELS: Multiple journalists and legal analysts have noted structural "
        "parallels between the Combs and Epstein operations: use of legitimate business as "
        "cover, staff-facilitated procurement, surveillance/recording of sexual activity, "
        "coercion through power imbalance, and obstruction of investigations. Combs' name "
        "appeared in Epstein-related FBI files, and indirect connections exist through shared "
        "social networks (e.g., Russian businessman Umar Dzhabrailov, who was friends with "
        "both Combs and Ghislaine Maxwell). No direct Combs-Epstein collaboration has been "
        "documented."
    ), "aliases": "Diddy, Puff Daddy, P. Diddy, Sean John Combs", "metadata": {"birth_year": 1969, "nationality": "American", "status": "incarcerated"}},

    # ---- Russell Simmons ----
    {"name": "Russell Simmons", "entity_type": "person", "description": (
        "Russell Wendell Simmons (b. 1957). Co-founder of Def Jam Recordings and hip-hop "
        "mogul accused of sexual assault or misconduct by over 20 women, who relocated to "
        "Bali, Indonesia — a country with no US extradition treaty — in 2018."
        "\n\n"
        "CAREER: Born in Queens, New York. Co-founded Def Jam Recordings with Rick Rubin in "
        "1984, launching the careers of LL Cool J, Beastie Boys, Public Enemy, and Jay-Z. "
        "Founded Phat Farm clothing, Rush Communications, and the Russell Simmons Music Group. "
        "One of the architects of hip-hop's commercial mainstream crossover. Forbes estimated "
        "peak net worth at $340 million."
        "\n\n"
        "SEXUAL ASSAULT ACCUSATIONS: In November 2017, model Keri Claussen accused Simmons "
        "of sexual assault in the Los Angeles Times. Screenwriter Jenny Lumet alleged assault "
        "in The Hollywood Reporter. Three women, including music executive Drew Dixon, accused "
        "Simmons of rape in a December 2017 New York Times investigation. Ultimately, over 20 "
        "women accused Simmons of sexual assault or harassment spanning decades. Simmons has "
        "denied all allegations but agreed to pay $11 million in settlements."
        "\n\n"
        "BRETT RATNER CO-ACCUSATION: A woman alleged that Simmons coerced her into performing "
        "oral sex on him while director Brett Ratner watched, in an incident she said occurred "
        "in 1991 when she was 17 years old. A second woman, Tanya Reid, alleged a similar "
        "pattern involving both Simmons and Ratner at a Miami hotel in 1994. Ratner separately "
        "appears in DOJ-released Epstein files — photographed on a sofa with Epstein and two "
        "young women, and referenced in a Peggy Siegal email to Epstein."
        "\n\n"
        "BALI EXILE: Since 2018, Simmons has lived primarily in Bali, Indonesia. Critics note "
        "Indonesia has no extradition treaty with the United States, complicating legal pursuit. "
        "Simmons has denied that his relocation is related to the allegations, describing it "
        "as a 'spiritual journey.' He has been served with legal papers at his Bali resort."
        "\n\n"
        "NETWORK SIGNIFICANCE: While no direct Epstein connection is documented, Simmons' "
        "co-accused Brett Ratner appears in Epstein files, and both operated in overlapping "
        "entertainment industry power circles where sexual predation was protected by industry "
        "gatekeepers. The flight-to-no-extradition pattern (Simmons→Bali, Brunel→attempted "
        "Senegal, Roman Polanski→France) recurs across accused entertainment industry predators."
    ), "aliases": "Russell Wendell Simmons", "metadata": {"birth_year": 1957, "nationality": "American", "status": "alive"}},

    # ---- R. Kelly ----
    {"name": "R. Kelly", "entity_type": "person", "description": (
        "Robert Sylvester Kelly (b. 1967). Grammy Award-winning R&B singer convicted of "
        "federal racketeering and sex trafficking, sentenced to 30 years in prison — one of "
        "the most prominent entertainment industry trafficking convictions and a case study "
        "in decades-long institutional protection of a known predator."
        "\n\n"
        "CAREER: Born in Chicago. Became one of the best-selling R&B artists of all time "
        "with hits including 'I Believe I Can Fly,' 'Ignition (Remix),' and the 'Trapped in "
        "the Closet' series. Produced Aaliyah's debut album Age Ain't Nothing but a Number "
        "(1994). Won three Grammy Awards."
        "\n\n"
        "PATTERN OF PREDATION: Kelly exploited his fame to systematically target, isolate, "
        "and abuse young women and girls over 25+ years. The pattern included: recruiting "
        "young fans at concerts and malls, isolating victims in properties he controlled, "
        "imposing strict behavioral rules (eating, sleeping, bathroom permissions), confiscating "
        "phones, recording sexual activity, and using recordings as control leverage. Multiple "
        "victims were underage."
        "\n\n"
        "AALIYAH MARRIAGE: In 1994, Kelly illegally married 15-year-old singer Aaliyah using "
        "a fraudulent ID listing her age as 18. Kelly was 27. The marriage was annulled. Kelly "
        "was convicted of bribery in connection with obtaining the fake ID — a public official "
        "was involved in procuring it."
        "\n\n"
        "DECADES OF INSTITUTIONAL PROTECTION: Despite a 2002 indictment on 21 counts of child "
        "pornography (acquitted 2008), ongoing allegations, journalist Jim DeRogatis' sustained "
        "reporting beginning in 2000, a widely circulated sex tape involving an underage girl, "
        "and the 2017 BuzzFeed investigation revealing a 'sex cult' — Kelly continued to "
        "release music, tour, and maintain recording contracts. Jive Records/RCA Records kept "
        "him signed through decades of allegations. The music industry's protection of Kelly "
        "mirrors the entertainment industry's broader pattern of shielding profitable predators."
        "\n\n"
        "CONVICTIONS: In September 2021, convicted by federal jury (SDNY) on nine counts "
        "including racketeering and eight violations of the Mann Act (sex trafficking). "
        "Sentenced to 30 years in prison in June 2022. In February 2023, convicted in a "
        "separate federal trial in Chicago on child pornography and enticement charges, "
        "receiving an additional 20 years (to run partially concurrent). Appeal upheld in "
        "February 2025 by the Second Circuit."
        "\n\n"
        "PATTERN SIGNIFICANCE: The Kelly case demonstrates how entertainment industry power "
        "structures protect predators for decades when they remain commercially valuable — "
        "the same institutional dynamic that enabled Epstein, Weinstein, and others. The "
        "'Surviving R. Kelly' documentary (2019) that finally catalyzed prosecution parallels "
        "investigative journalism's role in exposing the Epstein and Weinstein networks."
    ), "aliases": "Robert Sylvester Kelly, Robert Kelly", "metadata": {"birth_year": 1967, "nationality": "American", "status": "incarcerated"}},
]

RELATIONSHIPS = [
    # ---- Leonardo DiCaprio ----
    {"source": "Leonardo DiCaprio", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "inference", "desc": (
        "DiCaprio's name appears in DOJ-released Epstein files in two contexts: (1) a 2016 email from Deepak Chopra's "
        "account asking Epstein if 'leo dicaprio would want to have dinner with woody [Allen],' and (2) a 2009 email "
        "from Peter Mandelson asking about DiCaprio endorsements. Neither email was written by or to DiCaprio. No flight "
        "logs, direct correspondence, or confirmed meetings. His ex-girlfriend Alesia Riabenkova (dated 2013) appears "
        "in Dataset 11 exchanging emails with Epstein with procurement language. DiCaprio is not directly implicated."
    ), "sources": [1329, 1330, 1331, 1332, 1333]},
    {"source": "Leonardo DiCaprio", "target": "Woody Allen", "type": "connected_to", "tier": "inference", "desc": (
        "Epstein asked Chopra in 2016 whether DiCaprio would want to have dinner with Allen. No confirmation the dinner "
        "occurred. The email establishes that Epstein saw DiCaprio as someone in his social orbit worth cultivating."
    ), "sources": [1330, 1331]},

    # ---- Oprah Winfrey ----
    {"source": "Oprah Winfrey", "target": "João Teixeira de Faria", "type": "patron_of", "tier": "documented", "desc": (
        "Winfrey devoted a full Oprah Winfrey Show episode to Faria in 2010 and traveled to Brazil to film Oprah's Next "
        "Chapter at his clinic in 2012. These endorsements amplified Faria's reach internationally, drawing thousands of "
        "additional visitors — including vulnerable women — to his compound. After his arrest in December 2018, Winfrey "
        "deleted the episodes and released a statement."
    ), "sources": [1334, 1335, 1337, 1339]},

    # ---- João Teixeira de Faria (John of God) ----
    {"source": "João Teixeira de Faria", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "inference", "desc": (
        "No direct connection documented between Faria and Epstein. Both operated parallel predator systems using "
        "legitimate social cover (faith healing / financial management), celebrity endorsement, and institutional "
        "protection. Both exploited vulnerable populations and accumulated hundreds of victims over decades. Pattern "
        "parallel, not operational connection."
    ), "sources": [1338, 1340]},

    # ---- Sean Combs ----
    {"source": "Sean Combs", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "inference", "desc": (
        "Combs named in Epstein-related FBI files. Indirect connections through shared social networks — Russian "
        "businessman Umar Dzhabrailov was friends with both Combs and Ghislaine Maxwell. Structural parallels between "
        "operations (staff-facilitated procurement, surveillance/recording, coercion through power). No direct "
        "Combs-Epstein collaboration documented."
    ), "sources": [1346, 1361]},
    {"source": "Sean Combs", "target": "Harvey Weinstein", "type": "connected_to", "tier": "credible", "desc": (
        "Both operated in overlapping New York entertainment circles. Both indicted for sex trafficking-related offenses "
        "in the SDNY. Both used staff infrastructure to facilitate sexual coercion. The Combs indictment described the "
        "same district (SDNY) and similar legal framework (RICO + trafficking) as Weinstein and Epstein prosecutions."
    ), "sources": [1343, 1346]},

    # ---- Russell Simmons ----
    {"source": "Russell Simmons", "target": "Harvey Weinstein", "type": "connected_to", "tier": "credible", "desc": (
        "Both major entertainment industry figures accused of serial sexual assault during the same #MeToo era. Both "
        "used industry power to coerce and suppress allegations. Both operated in overlapping New York entertainment "
        "and media circles."
    ), "sources": [1348, 1349]},
    {"source": "Russell Simmons", "target": "Sean Combs", "type": "connected_to", "tier": "credible", "desc": (
        "Both hip-hop industry moguls accused of sexual predation. Simmons co-founded Def Jam and launched Jay-Z's "
        "career; Combs founded Bad Boy. Both were part of the same late-1990s/2000s hip-hop industry power structure "
        "and New York social scene."
    ), "sources": [1348, 1349]},

    # ---- R. Kelly ----
    {"source": "R. Kelly", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "inference", "desc": (
        "No direct connection. Both convicted sex traffickers who exploited fame and power to target young women "
        "and girls over decades. Both benefited from institutional protection (recording industry / financial industry). "
        "Both used surveillance and control systems. Both prosecuted under federal RICO and trafficking statutes in "
        "the same era. Pattern parallel, not operational connection."
    ), "sources": [1354, 1356]},
    {"source": "R. Kelly", "target": "Sean Combs", "type": "connected_to", "tier": "credible", "desc": (
        "Both music industry figures convicted of federal sex-related offenses. Kelly's racketeering conviction "
        "(2021) preceded Combs' indictment (2024). Both cases involved staff-facilitated procurement, isolation "
        "of victims, and decades of institutional protection by the recording industry."
    ), "sources": [1354, 1344]},
]

ENTITY_SOURCES = {
    "Leonardo DiCaprio": [1329, 1330, 1331, 1332, 1333],
    "Oprah Winfrey": [1334, 1335, 1336, 1337, 1338, 1339, 1340],
    "João Teixeira de Faria": [1334, 1335, 1336, 1337, 1338, 1339, 1340, 1359, 1360],
    "Sean Combs": [1341, 1342, 1343, 1344, 1345, 1346, 1347, 1361],
    "Russell Simmons": [1348, 1349, 1350, 1351, 1352, 1362, 1363],
    "R. Kelly": [1353, 1354, 1355, 1356, 1357, 1358],
}
