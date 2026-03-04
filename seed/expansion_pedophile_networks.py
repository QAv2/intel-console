"""
Pedophile Networks — Institutional Abuse, Cover-Ups, and Cross-Border Trafficking.

Expansion layer for Intel Console. Maps the documented history of organized
pedophile networks operating under institutional protection: the Belgian
Dutroux affair, the UK Westminster VIP abuse scandal, the Catholic Church's
systematic cover-up, and NXIVM's sex-trafficking conviction. These are not
conspiracy theories — they are court-proven cases, official government
inquiries, and Pulitzer Prize-winning investigative journalism.

The pattern across all four clusters is identical:
1. Abuse is systematic, not isolated — networks, not individuals
2. Institutions (police, prosecutors, intelligence, churches, governments)
   are informed and fail to act, or actively suppress investigations
3. Witnesses die, disappear, or are discredited
4. When exposure becomes unavoidable, the institutional response is to
   frame the problem as historical "failures" rather than ongoing protection

This expansion focuses on cases with COURT CONVICTIONS, OFFICIAL INQUIRIES,
or DOCUMENTED INSTITUTIONAL FINDINGS. Evidence tiers are applied strictly:
"documented" means court record, official inquiry finding, or government
report. "Credible" means quality investigative journalism or on-record
testimony. "Inference" is used only for pattern connections between clusters.
"Speculative" is applied to alleged cover-up motives where institutional
intent cannot be proven.

Entities (~20): People (Marc Dutroux, Keith Raniere, Peter Scully, Cardinal
Bernard Law, Leon Brittan, Cyril Smith, Peter Hayman, Peter Ball), organizations
(NXIVM, Dutroux Network, Boston Globe Spotlight Team), events (Dutroux Affair,
Westminster Dossier Disappearance, NXIVM Trial, Spotlight Investigation,
Australian Royal Commission, Independent Inquiry into Child Sexual Abuse UK),
operations (Operation Yewtree, Operation Midland).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Jeffrey Epstein [1], Ghislaine Maxwell [2], Virginia Giuffre [3],
  Les Wexner [4], Bill Clinton [32], Prince Andrew [33],
  Franklin Cover-Up [ritual_occult], Presidio Abuse Case [ritual_occult],
  The Finders [ritual_occult], Larry King [ritual_occult],
  Paul Bonacci [ritual_occult], John DeCamp [ritual_occult],
  Jimmy Savile [curated], CIA [85], FBI [87], MI5 [90], MI6 [91],
  DOJ [89], Metropolitan Police [curated], Catholic Church [curated],
  NYPD [curated]

Evidence tiers:
  documented = court conviction, official inquiry finding, government report
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1021-1050
# ============================================================

SOURCES = [
    # --- Dutroux Affair (Belgium) ---
    {
        "id": 1021,
        "title": "Belgian Parliamentary Commission of Inquiry — 'The Dutroux Affair' (April 1997, Verwilghen Commission report on police and judicial failures)",
        "url": "https://en.wikipedia.org/wiki/Dutroux_affair#Parliamentary_inquiry",
        "source_type": "government",
        "year": 1997,
    },
    {
        "id": 1022,
        "title": "Court of Assizes of Arlon — Marc Dutroux trial verdict (June 2004, convicted of kidnapping, rape, and murder of six girls; accomplices convicted)",
        "url": "https://en.wikipedia.org/wiki/Marc_Dutroux#Trial",
        "source_type": "court",
        "year": 2004,
    },
    {
        "id": 1023,
        "title": "The Guardian — 'Belgium confronts its heart of darkness' (coverage of Dutroux trial revelations, White March, and institutional failures, 2004)",
        "url": "https://www.theguardian.com/world/2004/mar/05/dutroux.marksweeney",
        "source_type": "journalism",
        "author": "Mark Sweeney",
        "year": 2004,
    },
    {
        "id": 1024,
        "title": "Olenka Frenkiel — BBC 'Correspondent' investigation: 'Belgium's X-Files' (documentary on witness deaths and institutional obstruction in Dutroux case, 2002)",
        "url": "https://en.wikipedia.org/wiki/Dutroux_affair#Witness_deaths",
        "source_type": "documentary",
        "author": "Olenka Frenkiel",
        "year": 2002,
    },
    # --- Westminster VIP Abuse / UK ---
    {
        "id": 1025,
        "title": "Independent Inquiry into Child Sexual Abuse (IICSA) — Final Report (October 2022, Prof. Alexis Jay, 7 years, 725 witnesses, 2 million pages of evidence)",
        "url": "https://www.iicsa.org.uk/reports-recommendations/publications/investigation/final-report",
        "source_type": "government",
        "year": 2022,
    },
    {
        "id": 1026,
        "title": "Wanless-Whittam Review — report on the Home Office's handling of the 'Dickens dossier' on alleged paedophile networks (2014, found 114 'relevant files' missing or destroyed)",
        "url": "https://en.wikipedia.org/wiki/Dickens_dossier",
        "source_type": "government",
        "year": 2014,
    },
    {
        "id": 1027,
        "title": "Simon Danczuk & Matthew Baker — 'Smile for the Camera: The Double Life of Cyril Smith' (documented Smith's serial abuse of boys in care homes; Smith knighted despite police awareness)",
        "url": "https://en.wikipedia.org/wiki/Cyril_Smith#Abuse_allegations",
        "source_type": "book",
        "author": "Simon Danczuk & Matthew Baker",
        "year": 2014,
    },
    {
        "id": 1028,
        "title": "Metropolitan Police — Operation Midland final report and IOPC review (investigation into VIP abuse allegations, 2014-2016; criticized for credulity toward 'Nick' / Carl Beech)",
        "url": "https://en.wikipedia.org/wiki/Operation_Midland",
        "source_type": "government",
        "year": 2016,
    },
    {
        "id": 1029,
        "title": "Don Hale — 'The Lost Boy: One Boy's Brutal Ordeal' (Derbyshire journalist's investigation into VIP abuse allegations; documents seizure of his files by Special Branch)",
        "url": "https://en.wikipedia.org/wiki/Don_Hale",
        "source_type": "book",
        "author": "Don Hale",
        "year": 2015,
    },
    # --- Operation Yewtree (Savile / UK) ---
    {
        "id": 1030,
        "title": "Dame Janet Smith Review — 'The Dame Janet Smith Review Report' (BBC investigation into Jimmy Savile, February 2016, found BBC 'missed opportunities' across decades)",
        "url": "https://en.wikipedia.org/wiki/Jimmy_Savile_sexual_abuse_scandal#Dame_Janet_Smith_Review",
        "source_type": "government",
        "year": 2016,
    },
    {
        "id": 1031,
        "title": "Metropolitan Police / NSPCC — 'Giving Victims a Voice' (Operation Yewtree joint report, Jan 2013; 450+ complaints against Savile spanning 1955-2009, across NHS hospitals, BBC, schools)",
        "url": "https://en.wikipedia.org/wiki/Operation_Yewtree",
        "source_type": "government",
        "year": 2013,
    },
    # --- Catholic Church Abuse ---
    {
        "id": 1032,
        "title": "Boston Globe Spotlight Team — 'Church allowed abuse by priest for years' (Jan 6, 2002, first in Pulitzer Prize-winning investigative series exposing Cardinal Law's cover-up)",
        "url": "https://www.bostonglobe.com/news/special-reports/2002/01/06/church-allowed-abuse-priest-for-years/cSHfGkTIrAT25qKGvBuDNM/story.html",
        "source_type": "journalism",
        "author": "Matt Carroll, Sacha Pfeiffer, Michael Rezendes, Walter Robinson",
        "year": 2002,
    },
    {
        "id": 1033,
        "title": "Pennsylvania Grand Jury Report — 40th Statewide Investigating Grand Jury Report 1 (August 2018, documented 1,000+ child victims and 300+ 'predator priests' across 6 dioceses over 70 years)",
        "url": "https://www.attorneygeneral.gov/report/",
        "source_type": "court",
        "year": 2018,
    },
    {
        "id": 1034,
        "title": "Royal Commission into Institutional Responses to Child Sexual Abuse — Final Report (December 2017, Australian government, 5 years, 8,000+ private sessions, 57,000+ calls)",
        "url": "https://www.childabuseroyalcommission.gov.au/final-report",
        "source_type": "government",
        "year": 2017,
    },
    {
        "id": 1035,
        "title": "John Jay College of Criminal Justice — 'The Nature and Scope of Sexual Abuse of Minors by Catholic Priests and Deacons in the United States 1950-2002' (USCCB-commissioned, 2004)",
        "url": "https://en.wikipedia.org/wiki/John_Jay_Report",
        "source_type": "academic",
        "year": 2004,
    },
    {
        "id": 1036,
        "title": "Archdiocese of Boston — settlement of 552 abuse claims for $85 million (September 2003, largest diocese settlement at the time)",
        "url": "https://en.wikipedia.org/wiki/Sexual_abuse_scandal_in_the_Catholic_Archdiocese_of_Boston",
        "source_type": "court",
        "year": 2003,
    },
    # --- NXIVM ---
    {
        "id": 1037,
        "title": "U.S. v. Keith Raniere — Eastern District of New York, Case No. 18-cr-204 (convicted June 2019 on all counts: sex trafficking, racketeering, forced labor; sentenced to 120 years)",
        "url": "https://en.wikipedia.org/wiki/Keith_Raniere#Trial_and_conviction",
        "source_type": "court",
        "year": 2019,
    },
    {
        "id": 1038,
        "title": "U.S. v. Clare Bronfman — guilty plea to harboring an illegal alien and fraudulent use of identification (September 2020, sentenced to 81 months; $6M restitution)",
        "url": "https://en.wikipedia.org/wiki/Clare_Bronfman#Criminal_proceedings",
        "source_type": "court",
        "year": 2020,
    },
    {
        "id": 1039,
        "title": "Sarah Edmondson — 'Scarred: The True Story of How I Escaped NXIVM, the Cult That Bound My Life' (first-person account of DOS branding and recruitment)",
        "url": "https://en.wikipedia.org/wiki/Sarah_Edmondson",
        "source_type": "book",
        "author": "Sarah Edmondson",
        "year": 2019,
    },
    {
        "id": 1040,
        "title": "HBO — 'The Vow' (documentary series, 2020-2022, NXIVM inner workings and DOS recruitment through former members' footage and testimony)",
        "url": "https://en.wikipedia.org/wiki/The_Vow_(TV_series)",
        "source_type": "documentary",
        "year": 2020,
    },
    # --- Peter Scully / Daisy's Destruction ---
    {
        "id": 1041,
        "title": "Regional Trial Court, Cagayan de Oro (Philippines) — Peter Scully convicted of human trafficking and rape (June 2018); life sentence. Separate murder charge pending for killing of 12-year-old.",
        "url": "https://en.wikipedia.org/wiki/Peter_Scully",
        "source_type": "court",
        "year": 2018,
    },
    {
        "id": 1042,
        "title": "60 Minutes Australia — 'The Monsters Among Us' (investigation into Peter Scully's dark web child exploitation network, 2015)",
        "url": "https://en.wikipedia.org/wiki/Peter_Scully#Media_coverage",
        "source_type": "documentary",
        "year": 2015,
    },
    # --- Peter Hayman / PIE ---
    {
        "id": 1043,
        "title": "House of Commons debate — Geoffrey Dickens names Sir Peter Hayman as member of Paedophile Information Exchange under parliamentary privilege (November 1981; Attorney General had blocked prosecution)",
        "url": "https://en.wikipedia.org/wiki/Peter_Hayman_(diplomat)",
        "source_type": "congressional",
        "year": 1981,
    },
    {
        "id": 1044,
        "title": "Tom Bower — 'Fayed: The Unauthorized Biography' and subsequent reporting on Paedophile Information Exchange links to Home Office, NCCL (now Liberty), and establishment protection of PIE members",
        "url": "https://en.wikipedia.org/wiki/Paedophile_Information_Exchange",
        "source_type": "journalism",
        "year": 2014,
    },
    # --- Peter Ball ---
    {
        "id": 1045,
        "title": "R v. Peter Ball — Crown Court conviction (October 2015, Bishop of Lewes/Gloucester, convicted of indecent assaults and misconduct in public office against 18 young men over 30 years; sentenced to 32 months)",
        "url": "https://en.wikipedia.org/wiki/Peter_Ball_(bishop)",
        "source_type": "court",
        "year": 2015,
    },
    {
        "id": 1046,
        "title": "IICSA — Anglican Church Investigation Report (October 2020, found Church of England prioritized reputation over victims; documented Prince Charles's correspondence with Ball after initial caution)",
        "url": "https://www.iicsa.org.uk/reports-recommendations/publications/investigation/anglican-church",
        "source_type": "government",
        "year": 2020,
    },
    # --- Cross-cutting / General ---
    {
        "id": 1047,
        "title": "Nick Davies — 'The school for scandal' (Guardian investigation into North Wales care homes abuse and the Waterhouse Inquiry's limitations, 2000)",
        "url": "https://www.theguardian.com/uk/2000/jul/12/childprotection.society",
        "source_type": "journalism",
        "author": "Nick Davies",
        "year": 2000,
    },
    {
        "id": 1048,
        "title": "Tim Tate — 'The Abuse of Trust' (investigation into institutional child abuse in the UK, connections between care homes, police, and political figures)",
        "url": "https://en.wikipedia.org/wiki/Tim_Tate",
        "source_type": "book",
        "author": "Tim Tate",
        "year": 1991,
    },
    {
        "id": 1049,
        "title": "Marcel Vervloesser — Belgian Senate testimony and subsequent conviction for child abuse (1999); former gendarme who claimed to have reported Dutroux network to superiors years before arrests",
        "url": "https://en.wikipedia.org/wiki/Dutroux_affair#Accomplices_and_alleged_network",
        "source_type": "court",
        "year": 1999,
    },
    {
        "id": 1050,
        "title": "Frank Bruni & Elinor Burkett — 'A Gospel of Shame: Children, Sexual Abuse, and the Catholic Church' (early comprehensive account of Catholic abuse pattern, pre-Spotlight)",
        "url": "https://en.wikipedia.org/wiki/Catholic_Church_sexual_abuse_cases",
        "source_type": "book",
        "author": "Frank Bruni & Elinor Burkett",
        "year": 1993,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- People ---
    {
        "name": "Marc Dutroux",
        "entity_type": "person",
        "description": "Belgian serial kidnapper, rapist, and murderer. Convicted in 2004 of abducting six girls (1995-1996), four of whom died — two starved to death in his basement dungeon while he was briefly jailed for car theft and police failed to search properly. Previously convicted of child rape in 1989 and released after only 3 years of a 13-year sentence. The parliamentary inquiry (Verwilghen Commission, 1997) documented catastrophic police and judicial failures: police heard children's voices during a search but did not investigate; informants warned about Dutroux repeatedly; evidence was ignored or lost. 300,000 Belgians marched in the 'White March' (October 1996) demanding institutional reform.",
        "aliases": "",
        "metadata": {"role": "convicted kidnapper/murderer", "birth_date": "1956-11-06"},
    },
    {
        "name": "Keith Raniere",
        "entity_type": "person",
        "description": "Founder of NXIVM, a self-improvement organization that operated as a coercive cult. Created the secret sub-group DOS ('Dominus Obsequious Sororium') — a master-slave pyramid where women were branded with his initials, starved to meet weight requirements, and coerced into sexual acts using 'collateral' (compromising photos/confessions held as blackmail). Convicted in June 2019 on all seven counts: sex trafficking, racketeering, forced labor conspiracy, wire fraud conspiracy, sex trafficking conspiracy, attempted sex trafficking, and racketeering conspiracy. Sentenced to 120 years in federal prison.",
        "aliases": "Vanguard",
        "metadata": {"role": "NXIVM founder / convicted sex trafficker", "birth_date": "1960-08-26"},
    },
    {
        "name": "Peter Scully",
        "entity_type": "person",
        "description": "Australian national convicted in the Philippines of human trafficking, rape, and the production of extreme child sexual abuse material distributed on the dark web. His 'Daisy's Destruction' video — depicting the torture and rape of an 18-month-old infant — became one of the most notorious dark web files. Convicted in June 2018 and sentenced to life imprisonment. A separate murder charge is pending for the killing of a 12-year-old girl whose remains were found beneath a house he rented. Operated a network paying impoverished Filipino families for access to children.",
        "aliases": "",
        "metadata": {"role": "convicted child sex trafficker", "birth_date": "1963-01-13"},
    },
    {
        "name": "Cardinal Bernard Law",
        "entity_type": "person",
        "description": "Archbishop of Boston (1984-2002). The Boston Globe Spotlight team's investigation (beginning January 2002) revealed that Law had systematically reassigned priests known to be sexually abusing children to new parishes rather than removing them or reporting to police. Internal church documents showed Law was informed of abuse by multiple priests — including serial abuser John Geoghan (130+ victims) — and transferred them to unsuspecting parishes. Resigned as Archbishop in December 2002. Was NOT criminally prosecuted. Instead, Pope John Paul II appointed him Archpriest of the Basilica di Santa Maria Maggiore in Rome — effectively granting him Vatican protection from U.S. legal jurisdiction. Died in 2017.",
        "aliases": "Bernard Francis Law",
        "metadata": {"role": "Archbishop of Boston / abuse cover-up", "birth_date": "1931-11-04", "death_date": "2017-12-20"},
    },
    {
        "name": "Leon Brittan",
        "entity_type": "person",
        "description": "UK Home Secretary (1983-1985). In 1983, MP Geoffrey Dickens handed Brittan a dossier alleging a VIP paedophile network in Westminster. The dossier was never seen again. The Wanless-Whittam Review (2014) found that 114 'relevant files' were missing or destroyed from the Home Office. Brittan stated he passed the dossier to his officials for 'appropriate action' — no action was taken. Brittan was also named in abuse allegations himself, though he died in 2015 before the IICSA inquiry examined the claims. Metropolitan Police investigated him under Operation Midland but made no charges. The question of whether the dossier was deliberately destroyed or merely lost remains unresolved.",
        "aliases": "Baron Brittan of Spennithorne",
        "metadata": {"role": "UK Home Secretary 1983-1985", "birth_date": "1939-09-25", "death_date": "2015-01-21"},
    },
    {
        "name": "Cyril Smith",
        "entity_type": "person",
        "description": "Liberal/Liberal Democrat MP for Rochdale (1972-1992). Knighted in 1988. After his death in 2010, Lancashire Police confirmed they had received multiple complaints of sexual abuse against boys in care homes dating back to the 1960s — files were sent to the Director of Public Prosecutions in 1970 but no prosecution resulted. Simon Danczuk MP documented Smith's abuse of boys at Cambridge House hostel and Knowl View school in Rochdale. MI5 was reportedly aware of the allegations and is alleged to have suppressed them. Smith's abuse was an 'open secret' in Westminster — he was protected by party machinery and the honours system throughout his career.",
        "aliases": "",
        "metadata": {"role": "MP for Rochdale / serial abuser", "birth_date": "1928-06-28", "death_date": "2010-09-03"},
    },
    {
        "name": "Peter Hayman",
        "entity_type": "person",
        "description": "British diplomat and High Commissioner to Canada (1970-1974). Identified as a member of the Paedophile Information Exchange (PIE). In 1978, Customs intercepted a package of child abuse material addressed to Hayman. The Attorney General blocked prosecution, and his identity was protected until MP Geoffrey Dickens named him under parliamentary privilege in November 1981. The decision not to prosecute a senior diplomat for offences that would have resulted in charges for any ordinary citizen exemplifies the pattern of establishment protection documented across multiple UK cases.",
        "aliases": "Sir Peter Hayman",
        "metadata": {"role": "diplomat / PIE member", "birth_date": "1914-06-14", "death_date": "1992-04-25"},
    },
    {
        "name": "Peter Ball",
        "entity_type": "person",
        "description": "Bishop of Lewes (1977-1992) and Bishop of Gloucester (1992-1993). Convicted in October 2015 of indecent assaults and misconduct in public office against 18 young men over a period spanning the 1970s-1990s. In 1992, he accepted a caution for an act of gross indecency with a 16-year-old — the Church of England allowed him to resign quietly and then reinstated him as Bishop of Gloucester. The IICSA Anglican Church investigation (2020) found that Prince Charles had corresponded with Ball after the 1993 caution expressing sympathy, and that the Church of England had prioritized its reputation over the protection of victims.",
        "aliases": "",
        "metadata": {"role": "Bishop / convicted sex offender", "birth_date": "1932-02-14", "death_date": "2019-06-21"},
    },
    # --- Organizations ---
    {
        "name": "NXIVM",
        "entity_type": "organization",
        "description": "Albany, New York-based organization founded by Keith Raniere (1998), ostensibly offering 'Executive Success Programs' in self-improvement. Operated as a multi-level marketing scheme and coercive cult. The secret sub-group DOS (est. ~2015) functioned as a sex-trafficking operation: women were recruited as 'slaves,' required to provide 'collateral' (nude photos, damaging confessions), branded with Raniere's initials using a cauterizing pen, and coerced into sexual acts. Clare Bronfman (Seagram heiress) was a key financier, pleading guilty to charges in 2020 and sentenced to 81 months. Allison Mack (actress) pleaded guilty to racketeering charges. The trial revealed Raniere had sexual relationships with underage girls.",
        "aliases": "Executive Success Programs, ESP",
        "metadata": {"type": "cult / sex trafficking organization", "founded": 1998},
    },
    {
        "name": "Dutroux Network",
        "entity_type": "organization",
        "description": "Criminal network surrounding Marc Dutroux in Belgium. Accomplices convicted at the 2004 Arlon trial include: Michel Lelièvre (kidnapping accomplice), Michel Nihoul (convicted of drug-related charges, acquitted of kidnapping but described by prosecutors as the link to an organized network), and Dutroux's ex-wife Michelle Martin (convicted of complicity — she let two girls starve while Dutroux was in jail). The Verwilghen Commission documented systemic failures suggesting the network extended beyond those convicted — 27 potential witnesses died during the investigation under circumstances described as suspicious. Whether a wider 'protection network' involving Belgian elites existed remains the central unresolved question.",
        "aliases": "",
        "metadata": {"type": "criminal network", "location": "Belgium"},
    },
    {
        "name": "Boston Globe Spotlight Team",
        "entity_type": "organization",
        "description": "Investigative journalism unit of the Boston Globe newspaper. Their January 2002 series on systemic child sexual abuse in the Catholic Archdiocese of Boston — led by editor Walter Robinson with reporters Matt Carroll, Sacha Pfeiffer, and Michael Rezendes — exposed Cardinal Bernard Law's decades-long practice of reassigning abusive priests rather than removing them. The investigation identified over 250 priests and brothers accused of abuse in the Boston archdiocese alone. Won the 2003 Pulitzer Prize for Public Service. The reporting triggered a global cascade: dioceses worldwide faced scrutiny, and the Catholic abuse scandal became recognized as a systemic, institutional pattern rather than isolated incidents.",
        "aliases": "Spotlight Team, Spotlight",
        "metadata": {"type": "investigative journalism unit", "founded": 1970},
    },
    # --- Events ---
    {
        "name": "Dutroux Affair",
        "entity_type": "event",
        "description": "Belgian political crisis triggered by the arrest of Marc Dutroux in August 1996 and the subsequent revelation of catastrophic police and judicial failures. The Verwilghen parliamentary commission (1997) documented: police had searched Dutroux's house and heard children screaming but did not investigate the basement; an informant had warned police about Dutroux before the kidnappings; the investigating judge was removed from the case under suspicious circumstances. Two girls (Julie Lejeune and Melissa Russo) starved to death in Dutroux's basement while he was briefly jailed. 300,000 Belgians marched in the 'White March' (October 20, 1996) — the largest demonstration in Belgian history. 27 witnesses connected to the case died during the investigation.",
        "aliases": "White March",
        "metadata": {"date_range": "1996-2004", "location": "Belgium"},
    },
    {
        "name": "Westminster Dossier Disappearance",
        "entity_type": "event",
        "description": "In 1983 and 1984, Conservative MP Geoffrey Dickens compiled and handed to Home Secretary Leon Brittan a dossier of evidence alleging a VIP paedophile network operating in and around Westminster. The dossier was never seen again. The Wanless-Whittam Review (2014), commissioned by the Home Office itself, found that 114 'relevant files' were missing or destroyed. The review could not determine whether the destruction was deliberate or the result of routine file management. The disappearance of the 'Dickens dossier' became a symbol of alleged establishment cover-up and was a key catalyst for the creation of the Independent Inquiry into Child Sexual Abuse (IICSA) in 2014.",
        "aliases": "Dickens Dossier, Geoffrey Dickens Dossier",
        "metadata": {"date_range": "1983-2014", "location": "London, UK"},
    },
    {
        "name": "NXIVM Trial",
        "entity_type": "event",
        "description": "Federal trial of Keith Raniere in the Eastern District of New York (May-June 2019). Raniere was convicted on all seven counts including sex trafficking, racketeering, and forced labor conspiracy. Evidence presented at trial included: testimony from DOS 'slaves' describing branding ceremonies, starvation diets, and sexual coercion; evidence of Raniere's sexual contact with underage girls; recordings and documents showing the organizational structure of the coercive hierarchy. Co-defendants who pleaded guilty included Allison Mack (racketeering), Clare Bronfman (harboring an illegal alien, fraud), and others. Raniere was sentenced to 120 years in October 2020.",
        "aliases": "U.S. v. Keith Raniere",
        "metadata": {"date_range": "2019-2020", "location": "Brooklyn, NY"},
    },
    {
        "name": "Spotlight Investigation",
        "entity_type": "event",
        "description": "The Boston Globe Spotlight Team's investigation into systemic child sexual abuse in the Catholic Archdiocese of Boston, published beginning January 6, 2002. Editor Walter Robinson and reporters Matt Carroll, Sacha Pfeiffer, and Michael Rezendes used court records, church directories, and victim testimony to document how Cardinal Bernard Law had reassigned priests known to be abusers — including John Geoghan (130+ victims) and Paul Shanley — to new parishes for decades. The investigation ultimately identified over 250 accused priests in the Boston archdiocese alone. Won the 2003 Pulitzer Prize for Public Service. Triggered a global reckoning with Catholic institutional abuse.",
        "aliases": "Boston Globe Investigation",
        "metadata": {"date_range": "2001-2003", "location": "Boston, MA"},
    },
    {
        "name": "Australian Royal Commission",
        "entity_type": "event",
        "description": "Royal Commission into Institutional Responses to Child Sexual Abuse (2013-2017). The most comprehensive government inquiry into institutional child abuse ever conducted. Over 5 years: 8,000+ private sessions with survivors, 57,000+ phone calls, 1,200+ referrals to police. Examined abuse in religious institutions (Catholic, Anglican, Salvation Army, Jehovah's Witnesses), government institutions, schools, and youth organizations. Found the Catholic Church accounted for the largest share of abuse — 7% of Catholic priests in Australia were accused. Final report issued 409 recommendations. Led to Australia's National Redress Scheme. Documented that institutional cover-up was not aberration but standard practice across religious denominations and government bodies.",
        "aliases": "Royal Commission into Institutional Responses to Child Sexual Abuse",
        "metadata": {"date_range": "2013-2017", "location": "Australia"},
    },
    {
        "name": "Independent Inquiry into Child Sexual Abuse",
        "entity_type": "event",
        "description": "UK statutory inquiry established in 2014 (commonly known as IICSA), chaired by Prof. Alexis Jay after three previous chairs resigned or were removed. Ran for 7 years, heard 725 witnesses, reviewed 2 million pages of evidence. Investigated abuse in churches (Anglican, Catholic), local authorities, residential schools, the internet, and Westminster. Key findings (final report October 2022): institutions across all sectors prioritized reputation over children; victims were disbelieved, ignored, or silenced; institutional cultures actively discouraged reporting. Recommended mandatory reporting, a Child Protection Authority, and a national redress scheme. The inquiry itself was politically contentious — critics said it was too broad to be effective; supporters said its breadth was necessary to reveal the systemic pattern.",
        "aliases": "IICSA",
        "metadata": {"date_range": "2014-2022", "location": "United Kingdom"},
    },
    {
        "name": "Operation Yewtree",
        "entity_type": "program",
        "description": "Metropolitan Police investigation established in October 2012 in the wake of the Jimmy Savile abuse revelations. Conducted under three strands: allegations directly involving Savile, allegations involving Savile and others, and allegations involving others. Led to multiple arrests and convictions of public figures including publicist Max Clifford (8 years, indecent assault), entertainer Rolf Harris (5 years 9 months, indecent assault), and radio DJ Dave Lee Travis (3 months suspended, indecent assault). The operation demonstrated that Savile's predation was not isolated but existed within a broader culture of celebrity impunity. Also revealed the failure of multiple institutions — BBC, NHS hospitals, schools — to act on complaints spanning decades.",
        "aliases": "",
        "metadata": {"date_range": "2012-present", "location": "United Kingdom"},
    },
    {
        "name": "Operation Midland",
        "entity_type": "program",
        "description": "Metropolitan Police investigation (2014-2016) into allegations of a VIP child abuse and murder ring. Based primarily on testimony from a single witness, 'Nick' (later identified as Carl Beech), who alleged that prominent figures including Leon Brittan, Lord Bramall, and Harvey Proctor were part of an abuse network. The investigation was heavily criticized: Beech's claims were described as 'credible and true' by a senior detective before investigation; search warrants were executed on the homes of elderly public figures on the basis of uncorroborated testimony. Operation Midland was closed in March 2016 with no charges. Beech was subsequently convicted of 12 counts of perverting the course of justice and one of fraud (2019), sentenced to 18 years. The operation's failure is used by critics to discredit broader VIP abuse allegations — though the documented cases of Cyril Smith, Peter Hayman, Peter Ball, and Jimmy Savile remain unaffected by Beech's fabrications.",
        "aliases": "",
        "metadata": {"date_range": "2014-2016", "location": "London, UK"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # === DUTROUX CLUSTER ===
    {
        "source": "Marc Dutroux",
        "target": "Dutroux Network",
        "type": "led",
        "tier": "documented",
        "desc": "Central figure in the criminal network. Convicted in 2004 of kidnapping, raping, and causing the deaths of six girls. Network included accomplices Lelièvre, Nihoul, and Martin.",
        "sources": [1022, 1023],
        "year_start": 1995,
        "year_end": 2004,
    },
    {
        "source": "Marc Dutroux",
        "target": "Dutroux Affair",
        "type": "caused",
        "tier": "documented",
        "desc": "Dutroux's arrest in August 1996 triggered the political crisis. His prior 1989 conviction and early release, combined with police failures during the 1995-96 kidnappings, exposed systemic institutional failure.",
        "sources": [1021, 1022, 1023],
        "year_start": 1996,
        "year_end": 2004,
    },
    {
        "source": "Dutroux Affair",
        "target": "Dutroux Network",
        "type": "exposed",
        "tier": "documented",
        "desc": "The parliamentary inquiry and trial exposed the network's operations, though the question of whether the network extended beyond those convicted remains contested. 27 witnesses died during the investigation.",
        "sources": [1021, 1024],
        "year_start": 1996,
        "year_end": 2004,
    },
    {
        "source": "Dutroux Affair",
        "target": "Franklin Cover-Up",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both cases share the same structural pattern: institutional child abuse networks, police and judicial failures that appear protective rather than negligent, witnesses dying or being discredited, and investigations that stopped short of the alleged wider network. Pattern parallel, no direct operational connection.",
        "sources": [1021, 1024],
        "year_start": None,
        "year_end": None,
    },
    # === WESTMINSTER VIP ABUSE CLUSTER ===
    {
        "source": "Leon Brittan",
        "target": "Westminster Dossier Disappearance",
        "type": "implicated_in",
        "tier": "documented",
        "desc": "As Home Secretary, Brittan received the Dickens dossier on alleged VIP paedophile networks in 1983. He stated he passed it to officials for 'appropriate action.' The dossier was never seen again. The Wanless-Whittam review found 114 relevant files missing or destroyed.",
        "sources": [1026, 1029],
        "year_start": 1983,
        "year_end": 1984,
    },
    {
        "source": "Cyril Smith",
        "target": "Westminster Dossier Disappearance",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Smith was one of the Westminster figures whose abuse was allegedly documented in the Dickens dossier. Lancashire Police had sent files on Smith's abuse to the DPP in 1970 — no prosecution resulted. Smith was knighted in 1988 despite police awareness of his offending.",
        "sources": [1027, 1026],
        "year_start": 1970,
        "year_end": 1988,
    },
    {
        "source": "Cyril Smith",
        "target": "MI5",
        "type": "connected_to",
        "tier": "credible",
        "desc": "MI5 was reportedly aware of Smith's abuse of boys in care homes and is alleged to have suppressed the information. Simon Danczuk MP documented the pattern of institutional protection. Smith's abuse was an 'open secret' in Westminster for decades.",
        "sources": [1027, 1048],
        "year_start": 1970,
        "year_end": 1992,
    },
    {
        "source": "Peter Hayman",
        "target": "Westminster Dossier Disappearance",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Hayman was a Paedophile Information Exchange member whose prosecution was blocked by the Attorney General (1978). Geoffrey Dickens named him under parliamentary privilege in 1981. Hayman exemplifies the VIP protection pattern that the Dickens dossier sought to expose.",
        "sources": [1043, 1044, 1026],
        "year_start": 1978,
        "year_end": 1984,
    },
    {
        "source": "Independent Inquiry into Child Sexual Abuse",
        "target": "Westminster Dossier Disappearance",
        "type": "investigated",
        "tier": "documented",
        "desc": "IICSA was established in 2014 partly in response to the Dickens dossier scandal. The inquiry examined institutional failures across Westminster, churches, councils, and the care system over its 7-year duration.",
        "sources": [1025, 1026],
        "year_start": 2014,
        "year_end": 2022,
    },
    {
        "source": "Independent Inquiry into Child Sexual Abuse",
        "target": "Peter Ball",
        "type": "investigated",
        "tier": "documented",
        "desc": "IICSA's Anglican Church investigation (2020) examined the Ball case in detail, finding that the Church of England prioritized reputation over victims and that senior figures — including Prince Charles — had corresponded with Ball sympathetically after his 1993 caution.",
        "sources": [1025, 1046],
        "year_start": 2014,
        "year_end": 2020,
    },
    {
        "source": "Peter Ball",
        "target": "Catholic Church",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Ball was Anglican, not Catholic, but his case demonstrates the identical institutional pattern: abuse over decades, institutional awareness, protection of the abuser, silencing of victims. The IICSA found this pattern was not denomination-specific but institutional.",
        "sources": [1045, 1046, 1025],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Peter Ball",
        "target": "Prince Andrew",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both cases involve senior establishment figures and the pattern of institutional protection. Ball received sympathetic correspondence from Prince Charles; Prince Andrew's Epstein connections involved similar establishment reluctance to investigate. Pattern parallel — no direct operational link.",
        "sources": [1046],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Operation Midland",
        "target": "Leon Brittan",
        "type": "investigated",
        "tier": "documented",
        "desc": "Operation Midland investigated abuse allegations against Brittan based on Carl Beech's testimony. Brittan's home was searched. No charges were brought. Beech was later convicted of fabricating his claims (2019). However, the separate question of the Dickens dossier's disappearance under Brittan's watch remains unresolved.",
        "sources": [1028],
        "year_start": 2014,
        "year_end": 2016,
    },
    {
        "source": "Operation Midland",
        "target": "Metropolitan Police",
        "type": "operated_by",
        "tier": "documented",
        "desc": "Operation Midland was a Metropolitan Police investigation. It was heavily criticized by the IOPC (Independent Office for Police Conduct) for failures in evidence assessment — particularly the premature declaration that Beech's claims were 'credible and true.'",
        "sources": [1028],
        "year_start": 2014,
        "year_end": 2016,
    },
    # === OPERATION YEWTREE / SAVILE ===
    {
        "source": "Operation Yewtree",
        "target": "Jimmy Savile",
        "type": "investigated",
        "tier": "documented",
        "desc": "Operation Yewtree was established in the wake of the Savile revelations. The 'Giving Victims a Voice' report documented 450+ complaints against Savile spanning 1955-2009 across BBC, NHS hospitals, schools, and other institutions.",
        "sources": [1031, 1030],
        "year_start": 2012,
        "year_end": 2013,
    },
    {
        "source": "Operation Yewtree",
        "target": "Metropolitan Police",
        "type": "operated_by",
        "tier": "documented",
        "desc": "Yewtree was a Metropolitan Police operation conducted jointly with the NSPCC. Led to multiple arrests and convictions of public figures beyond Savile himself, including Max Clifford, Rolf Harris, and Dave Lee Travis.",
        "sources": [1031],
        "year_start": 2012,
        "year_end": None,
    },
    {
        "source": "Jimmy Savile",
        "target": "MI5",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Savile had documented access to royalty, senior politicians, and military/intelligence circles. The Dame Janet Smith Review found the BBC 'missed opportunities' to stop him over decades. His protection by multiple institutions — BBC, NHS, police — raises questions about whether intelligence agencies were aware.",
        "sources": [1030, 1031, 1048],
        "year_start": 1960,
        "year_end": 2011,
    },
    {
        "source": "Jimmy Savile",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "inference",
        "desc": "No direct operational connection, but the structural parallel is precise: both were serial predators who cultivated relationships with royalty, politicians, and institutions; both were protected by institutional failures across decades; both cases revealed systemic rather than isolated abuse. Savile (UK) and Epstein (US) represent the same pattern in different jurisdictions.",
        "sources": [1030, 1031],
        "year_start": None,
        "year_end": None,
    },
    # === CATHOLIC CHURCH CLUSTER ===
    {
        "source": "Cardinal Bernard Law",
        "target": "Spotlight Investigation",
        "type": "exposed_by",
        "tier": "documented",
        "desc": "The Globe investigation exposed Law's systematic reassignment of abusive priests. Internal church documents obtained by the Spotlight team showed Law was informed of abuse by multiple priests and transferred them to unsuspecting parishes for decades.",
        "sources": [1032, 1036],
        "year_start": 2002,
        "year_end": 2002,
    },
    {
        "source": "Cardinal Bernard Law",
        "target": "Catholic Church",
        "type": "member_of",
        "tier": "documented",
        "desc": "Archbishop of Boston (1984-2002). Resigned under pressure after Spotlight revelations. Appointed by Pope John Paul II as Archpriest of Basilica di Santa Maria Maggiore in Rome — effectively given Vatican protection from U.S. legal jurisdiction rather than facing accountability.",
        "sources": [1032, 1035, 1036],
        "year_start": 1984,
        "year_end": 2017,
    },
    {
        "source": "Boston Globe Spotlight Team",
        "target": "Spotlight Investigation",
        "type": "conducted",
        "tier": "documented",
        "desc": "The Spotlight Team conducted the investigation, publishing the first article on January 6, 2002. Led by editor Walter Robinson with reporters Carroll, Pfeiffer, and Rezendes. Won 2003 Pulitzer Prize for Public Service.",
        "sources": [1032],
        "year_start": 2001,
        "year_end": 2003,
    },
    {
        "source": "Spotlight Investigation",
        "target": "Catholic Church",
        "type": "exposed",
        "tier": "documented",
        "desc": "The Spotlight investigation exposed that the Catholic Church's cover-up of clergy abuse was not isolated to individual 'bad priests' but was a systematic institutional practice — reassign, deny, silence victims. Triggered a global cascade of similar revelations.",
        "sources": [1032, 1035, 1050],
        "year_start": 2002,
        "year_end": 2003,
    },
    {
        "source": "Australian Royal Commission",
        "target": "Catholic Church",
        "type": "investigated",
        "tier": "documented",
        "desc": "The Royal Commission found the Catholic Church accounted for the largest share of institutional abuse in Australia — 7% of Catholic priests active between 1950 and 2010 were accused. Documented that institutional cover-up was standard practice, not aberration.",
        "sources": [1034],
        "year_start": 2013,
        "year_end": 2017,
    },
    {
        "source": "Spotlight Investigation",
        "target": "Australian Royal Commission",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The Spotlight investigation's global impact helped create the political conditions for the Australian Royal Commission (est. 2013). The Boston revelations demonstrated that the Catholic abuse pattern was institutional and global, not local.",
        "sources": [1032, 1034],
        "year_start": 2002,
        "year_end": 2013,
    },
    # === NXIVM CLUSTER ===
    {
        "source": "Keith Raniere",
        "target": "NXIVM",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded NXIVM (1998) and created the DOS sub-group (~2015). Maintained total control over the organization's hierarchy, curriculum, and the sexual exploitation system. Convicted on all counts in 2019.",
        "sources": [1037, 1039, 1040],
        "year_start": 1998,
        "year_end": 2018,
    },
    {
        "source": "Keith Raniere",
        "target": "NXIVM Trial",
        "type": "convicted_in",
        "tier": "documented",
        "desc": "Convicted June 2019 on all seven counts: sex trafficking, racketeering, forced labor conspiracy, wire fraud conspiracy, sex trafficking conspiracy, attempted sex trafficking, racketeering conspiracy. Sentenced to 120 years, October 2020.",
        "sources": [1037],
        "year_start": 2019,
        "year_end": 2020,
    },
    {
        "source": "NXIVM",
        "target": "NXIVM Trial",
        "type": "exposed_by",
        "tier": "documented",
        "desc": "The federal trial exposed NXIVM's full structure: the DOS branding ceremonies, collateral system, starvation requirements, and Raniere's sexual contact with underage girls. Multiple co-defendants pleaded guilty.",
        "sources": [1037, 1038, 1039],
        "year_start": 2018,
        "year_end": 2020,
    },
    {
        "source": "NXIVM",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both NXIVM and Epstein's operation involved: elite social circles, sexual exploitation presented within a framework of mentorship/philanthropy, compromising material used as leverage (collateral/recordings), and wealthy financiers enabling the operation. Pattern parallel — no proven direct connection, though both intersected with Bronfman family wealth.",
        "sources": [1037, 1038],
        "year_start": None,
        "year_end": None,
    },
    # === PETER SCULLY ===
    {
        "source": "Peter Scully",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "inference",
        "desc": "No direct connection. Scully's dark web exploitation network and Epstein's elite trafficking ring represent opposite ends of the same spectrum — Scully exploited impoverished children in the Philippines for online distribution; Epstein exploited vulnerable teenagers in elite social settings. Both demonstrate that child sexual exploitation operates as organized networks, not isolated incidents.",
        "sources": [1041, 1042],
        "year_start": None,
        "year_end": None,
    },
    # === CROSS-CUTTING CONNECTIONS ===
    {
        "source": "Dutroux Affair",
        "target": "Jimmy Savile",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both cases emerged from the same period and reveal the same institutional pattern: serial predators protected by establishment networks across decades. In Belgium, police heard children screaming and didn't investigate. In the UK, the BBC received complaints for 50 years and did nothing. Pattern parallel — no direct operational connection.",
        "sources": [1021, 1030],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Westminster Dossier Disappearance",
        "target": "FBI",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Pattern parallel to U.S. cases: the UK Home Office 'lost' 114 files on VIP abuse; the FBI's handling of the Franklin investigation focused on discrediting witnesses rather than pursuing allegations. Different jurisdictions, same institutional response — protect the institution, discredit the accusers.",
        "sources": [1026, 1029],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Independent Inquiry into Child Sexual Abuse",
        "target": "Australian Royal Commission",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The UK's IICSA (2014-2022) and Australia's Royal Commission (2013-2017) were parallel national-level inquiries into institutional child abuse. Both found the same systemic patterns: institutions prioritized reputation over children, abusers were protected, victims were silenced.",
        "sources": [1025, 1034],
        "year_start": 2013,
        "year_end": 2022,
    },
    {
        "source": "Operation Yewtree",
        "target": "Independent Inquiry into Child Sexual Abuse",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Operation Yewtree (2012) and the Savile revelations created the political momentum that led to the establishment of IICSA (2014). Yewtree demonstrated the scale of celebrity and institutional abuse; IICSA was created to examine the systemic failures that enabled it.",
        "sources": [1031, 1025],
        "year_start": 2012,
        "year_end": 2014,
    },
    {
        "source": "Cyril Smith",
        "target": "Jimmy Savile",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Both were knighted establishment figures whose serial abuse of children was an 'open secret' protected by institutional silence. Smith (political sphere, knighted 1988) and Savile (entertainment/charity sphere, knighted 1990) represent the same pattern of establishment protection across different sectors of British public life.",
        "sources": [1027, 1030, 1031],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Cardinal Bernard Law",
        "target": "DOJ",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Despite evidence of systematic cover-up affecting hundreds of children, Law was never criminally prosecuted. The DOJ did not pursue federal charges. Law resigned as Archbishop and was given a Vatican appointment, effectively removing him from U.S. jurisdiction.",
        "sources": [1032, 1036],
        "year_start": 2002,
        "year_end": 2004,
    },
    {
        "source": "Dutroux Affair",
        "target": "Presidio Abuse Case",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both cases involved institutional abuse where investigations were derailed: in Belgium, the investigating judge was removed; at the Presidio, charges against Aquino were dropped despite 60+ alleged victims. Different continents, same pattern — investigations approaching powerful figures are shut down.",
        "sources": [1021, 1024],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "NXIVM",
        "target": "Ghislaine Maxwell",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both Maxwell and NXIVM used the same operational model: a trusted female recruiter (Maxwell for Epstein, Allison Mack and others for Raniere) who provided a veneer of legitimacy and recruited victims. Both systems used compromising material as leverage. Pattern parallel — no direct operational link documented.",
        "sources": [1037, 1039],
        "year_start": None,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Marc Dutroux": [1021, 1022, 1023, 1024],
    "Keith Raniere": [1037, 1039, 1040],
    "Peter Scully": [1041, 1042],
    "Cardinal Bernard Law": [1032, 1035, 1036, 1050],
    "Leon Brittan": [1026, 1028, 1029],
    "Cyril Smith": [1027, 1048],
    "Peter Hayman": [1043, 1044],
    "Peter Ball": [1045, 1046],
    "NXIVM": [1037, 1038, 1039, 1040],
    "Dutroux Network": [1021, 1022, 1023, 1024, 1049],
    "Boston Globe Spotlight Team": [1032],
    "Dutroux Affair": [1021, 1022, 1023, 1024],
    "Westminster Dossier Disappearance": [1026, 1029, 1044],
    "NXIVM Trial": [1037, 1038],
    "Spotlight Investigation": [1032, 1036],
    "Australian Royal Commission": [1034],
    "Independent Inquiry into Child Sexual Abuse": [1025, 1046, 1047],
    "Operation Yewtree": [1030, 1031],
    "Operation Midland": [1028],
}
