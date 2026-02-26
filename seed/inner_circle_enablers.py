"""
Inner Circle & Enablers — Victims, Witnesses, Assistants, and Facilities
Research layer for the Intel Console OSINT database.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES (IDs 116-140)
# ============================================================

NEW_SOURCES = [
    # Court / Legal
    {"id": 116, "title": "Giuffre v. Maxwell — Deposition Transcripts (SDNY, Unsealed 2019-2024)", "url": "https://www.courtlistener.com/docket/4355835/giuffre-v-maxwell/", "source_type": "court", "year": 2019},
    {"id": 117, "title": "United States v. Maxwell — Trial Record (S.D.N.Y. 20-cr-330)", "url": "https://www.justice.gov/usao-sdny/united-states-v-ghislaine-maxwell", "source_type": "court", "year": 2021},
    {"id": 118, "title": "In Re: Courtney Wild — 11th Circuit CVRA Decision (No. 19-13843)", "url": "https://media.ca11.uscourts.gov/opinions/pub/files/201913843.enb.pdf", "source_type": "court", "year": 2020},
    {"id": 119, "title": "Farmer v. Indyke et al. — S.D.N.Y. No. 1:19-cv-10474", "url": "https://www.justice.gov/multimedia/Court%20Records/Farmer%20v.%20Indyke/", "source_type": "court", "year": 2019},
    {"id": 120, "title": "DOJ Inspector General Report — BOP Custody of Epstein at MCC", "url": "https://oig.justice.gov/reports/investigation-and-review-federal-bureau-prisons-custody-care-and-supervision-jeffrey", "source_type": "government", "year": 2023},
    {"id": 121, "title": "Epstein NPA Full Text — DocumentCloud", "url": "https://reason.com/wp-content/uploads/2021/08/Non-Prosecution-Agreement-1433.pdf", "source_type": "court", "year": 2007},
    {"id": 122, "title": "DOJ Office of Professional Responsibility — Acosta NPA Review", "url": "https://www.justice.gov/opr/page/file/1336471/dl", "source_type": "government", "year": 2020},

    # Journalism
    {"id": 123, "title": "NBC News — Virginia Giuffre, Epstein Abuse Survivor, Dies by Suicide", "url": "https://www.nbcnews.com/news/us-news/virginia-giuffre-one-jeffrey-epsteins-prominent-abuse-survivors-dies-s-rcna203027", "source_type": "journalism", "year": 2025},
    {"id": 124, "title": "Daily Beast — Epstein's Alleged Accomplices: Where Are Kellen, Marcinkova, Ross & Groff?", "url": "https://www.thedailybeast.com/jeffrey-epsteins-alleged-accomplices-where-are-sarah-kellen-nadia-marcinkova-adriana-ross-and-lesley-groff/", "source_type": "journalism", "year": 2019},
    {"id": 125, "title": "NBC News — Palm Beach Police Chief Michael Reiter on 2005 Epstein Investigation", "url": "https://www.nbcnews.com/news/us-news/ex-florida-police-chief-epstein-case-worst-failure-criminal-justice-n1057226", "source_type": "journalism", "year": 2019},
    {"id": 126, "title": "CNN — Maxwell Guilty: Jury Finds Her Guilty on Five of Six Counts", "url": "https://www.cnn.com/2021/12/29/us/ghislaine-maxwell-trial-wednesday", "source_type": "journalism", "year": 2021},
    {"id": 127, "title": "Calcalist Tech — The Ties That Bind: Ehud Barak's Business Network (Carbyne/Junkermann)", "url": "https://www.calcalistech.com/ctech/articles/0,7340,L-3766639,00.html", "source_type": "journalism", "year": 2019},
    {"id": 128, "title": "Bloomberg — How Jeffrey Epstein Got Into Hedge Funds: The Dubins Helped", "url": "https://www.bloomberg.com/news/features/2026-02-13/how-jeffrey-epstein-got-into-hedge-funds-billionaire-dubins-helped", "source_type": "journalism", "year": 2026},
    {"id": 129, "title": "New Republic — Epstein Bragged He 'Gave' His Young Girlfriend to Trump", "url": "https://newrepublic.com/post/203132/epstein-bragged-email-gave-young-girlfriend-trump", "source_type": "journalism", "year": 2024},
    {"id": 130, "title": "CBS News — Epstein Worked at Towers Financial with Hoffenberg (Ponzi Scheme)", "url": "https://www.cbsnews.com/news/jeffrey-epstein-worked-at-towers-financial-with-stephen-hoffenberg-who-committed-ponzi-scheme-crimes/", "source_type": "journalism", "year": 2019},
    {"id": 131, "title": "NPR — Epstein's Former Mentor Hoffenberg Found Dead in Connecticut", "url": "https://www.npr.org/2022/08/26/1119746511/jeffrey-epstein-mentor-steven-hoffenberg-dead", "source_type": "journalism", "year": 2022},
    {"id": 132, "title": "Law & Crime — Dalton School's 'Epstein-Barr' Problem", "url": "https://lawandcrime.com/high-profile/the-epstein-barr-problem-of-new-york-citys-dalton-school/", "source_type": "journalism", "year": 2019},
    {"id": 133, "title": "CBS News — Zorro Ranch: Epstein's New Mexico Property", "url": "https://www.cbsnews.com/news/jeffrey-epstein-new-mexico-ranch-official-says-there-is-a-story-to-be-told-in-new-mexico/", "source_type": "journalism", "year": 2019},
    {"id": 134, "title": "Sunday Guardian — Who Is Lesley Groff? Mentioned 150,000+ Times in DOJ Files", "url": "https://sundayguardianlive.com/world/who-is-lesley-groff-executive-assistant-to-jeffrey-epstein-mentioned-over-150000-times-in-newly-unredacted-doj-files-170552/", "source_type": "journalism", "year": 2026},
    {"id": 135, "title": "Pravda EU — Nicole Junkermann Mentioned 3,000+ Times in Epstein Case", "url": "https://eu.news-pravda.com/world/2026/02/23/170698.html", "source_type": "journalism", "year": 2026},
    {"id": 136, "title": "ABC News — Epstein Survivor Courtney Wild Presses CVRA Case", "url": "https://abcnews.com/US/jeffrey-epstein-survivor-presses-case-hold-us-govt/story?id=68313706", "source_type": "journalism", "year": 2019},
    {"id": 137, "title": "Wikipedia — Herbert N. Straus House (9 East 71st Street)", "url": "https://en.wikipedia.org/wiki/Herbert_N._Straus_House", "source_type": "journalism", "year": 2024},
    {"id": 138, "title": "Law & Crime — Eva Andersson-Dubin Testifies at Maxwell Trial", "url": "https://lawandcrime.com/live-trials/ghislaine-maxwell/wife-of-hedge-fund-billionaire-and-ex-girlfriend-of-jeffrey-epstein-testifies-in-ghislaine-maxwell-trial/", "source_type": "journalism", "year": 2021},
    {"id": 139, "title": "Sunday Guardian — Who Are Maria and Annie Farmer, Sisters Who Warned FBI in 1996?", "url": "https://sundayguardianlive.com/news/epstein-files-who-are-maria-and-annie-farmer-the-sisters-who-survived-warned-the-fbi-in-1996-162412/", "source_type": "journalism", "year": 2026},

    # Books
    {"id": 140, "title": "Virginia Giuffre — Nobody's Girl (Memoir, Posthumous)", "url": "", "source_type": "book", "author": "Virginia Giuffre", "year": 2025},
]


# ============================================================
# ENTITY DESCRIPTIONS
# ============================================================

_DESC_GIUFFRE = (
    "Virginia Louise Giuffre, nee Roberts (1983-2025). The most prominent survivor "
    "and witness in the Jeffrey Epstein sex trafficking case. Her public testimony, "
    "civil lawsuits, and advocacy fundamentally shaped public knowledge of the Epstein "
    "operation."
    "\n\n"
    "BACKGROUND: Born August 9, 1983, in Sacramento, California. Suffered childhood "
    "sexual abuse beginning at age seven. Ran away from home as a teenager and was "
    "living in a troubled circumstances when she was recruited."
    "\n\n"
    "RECRUITMENT AT MAR-A-LAGO (2000): At age 16, while working as a spa attendant at "
    "Donald Trump's Mar-a-Lago resort in Palm Beach, Florida, Giuffre was approached "
    "by Ghislaine Maxwell and recruited into Jeffrey Epstein's sex trafficking operation "
    "under the guise of a massage therapy job. This recruitment at Mar-a-Lago places "
    "the operation's victim pipeline at the doorstep of a future US president's primary "
    "residence."
    "\n\n"
    "TRAFFICKING ALLEGATIONS: Giuffre testified in depositions and civil filings that "
    "she was trafficked to numerous powerful men, including Prince Andrew (Duke of York), "
    "Alan Dershowitz, former New Mexico Governor Bill Richardson, and others. She "
    "described being transported to Epstein's properties in Manhattan, Palm Beach, "
    "New Mexico (Zorro Ranch), the US Virgin Islands (Little Saint James), and abroad."
    "\n\n"
    "LEGAL ACTIONS: Filed landmark civil suits that cracked open the case. Her 2009 "
    "lawsuit as 'Jane Doe 102' against Epstein was settled for $500,000. In 2015, she "
    "intervened in the Dershowitz defamation case. Her 2021 civil suit against Prince "
    "Andrew was settled in February 2022 for a reported sum estimated between 3 million "
    "and 12 million pounds, with Andrew making a 'substantial donation' to Giuffre's "
    "victims' charity — with no admission of liability."
    "\n\n"
    "ADVOCACY: In 2015, Giuffre founded Victims Refuse Silence (later relaunched as "
    "SOAR — Speak Out, Act, Reclaim) to support abuse survivors. She was the first "
    "Epstein victim to waive anonymity and speak publicly (2011), providing critical "
    "information to law enforcement that contributed to Ghislaine Maxwell's 2021 "
    "conviction."
    "\n\n"
    "DEATH: Died by suicide on April 25, 2025, at age 41, at her farm in Neergabby, "
    "Western Australia. She had been in a custody battle and divorce proceedings and "
    "had been prevented from seeing her three children. Her posthumous memoir, "
    "'Nobody's Girl,' was published in October 2025. Other survivors credited Giuffre "
    "with giving them the courage to speak out."
)

_DESC_KELLEN = (
    "Sarah Kellen (b. circa 1979-1980). Epstein's primary day-to-day scheduler and "
    "operational coordinator, described by victims and investigators as the "
    "administrative infrastructure of Epstein's trafficking operation."
    "\n\n"
    "ROLE: Kellen managed Epstein's calendar and logistics across his Palm Beach, "
    "Manhattan, and other properties. According to Palm Beach police reports, civil "
    "lawsuits, and victim testimony, her duties included scheduling 'massages' that "
    "were sexual abuse sessions with underage girls, coordinating victim travel, and "
    "greeting young women at Epstein's properties. Virginia Giuffre and multiple other "
    "accusers named Kellen as directly facilitating abuse."
    "\n\n"
    "NPA CO-CONSPIRATOR: Named as one of four co-conspirators in the 2007 "
    "Non-Prosecution Agreement alongside Nadia Marcinkova, Lesley Groff, and Adriana "
    "Ross. All four received immunity from federal prosecution as part of Epstein's "
    "plea deal negotiated by US Attorney Alexander Acosta. During Ghislaine Maxwell's "
    "sentencing in 2022, Judge Alison Nathan described Kellen as 'a knowing participant "
    "in the criminal conspiracy' and 'a criminally responsible participant.'"
    "\n\n"
    "LEGAL STATUS: Despite extensive public allegations, Kellen has never been charged "
    "with a crime. Through her attorney, she has described herself as a victim of "
    "Epstein. Prosecutors declined to bring charges after Epstein's 2019 death."
    "\n\n"
    "PERSONAL LIFE: Married NASCAR driver Brian Vickers in 2013. They divorced in 2025 "
    "after approximately 10 years of marriage."
)

_DESC_MARCINKOVA = (
    "Nadia Marcinkova, now Nadia Marcinko (b. circa 1986, Kosice, Slovakia). Brought "
    "to the United States by Jeffrey Epstein as a teenager from Eastern Europe. Named "
    "co-conspirator in the 2007 NPA. Later became a licensed pilot and aviation "
    "entrepreneur."
    "\n\n"
    "ORIGIN AND TRAFFICKING: According to Palm Beach police reports and victim "
    "depositions, Epstein told associates he had 'purchased' Marcinkova from her "
    "family in the former Yugoslavia when she was approximately 15 years old. Epstein "
    "described her to at least one victim as his 'sex slave.' Her father, Peter "
    "Marcinko, is an architect from Presov, Slovakia. The circumstances of her arrival "
    "in the US represent one of the most disturbing documented aspects of Epstein's "
    "international trafficking operation."
    "\n\n"
    "ROLE IN OPERATION: Earliest reports from victims in the 2005-2006 Palm Beach "
    "police investigation described Marcinkova as actively involved in sexual abuse, "
    "with Epstein often instructing her to participate in acts with recruited victims. "
    "Her dual status — simultaneously a trafficking victim and an active participant — "
    "illustrates the coercion dynamics of the Epstein operation."
    "\n\n"
    "NPA IMMUNITY: Named alongside Sarah Kellen, Lesley Groff, and Adriana Ross as "
    "co-conspirators who received immunity in the 2007 Non-Prosecution Agreement. "
    "Never charged with any crime."
    "\n\n"
    "LATER LIFE: Changed her name to Nadia Marcinko by approximately 2011. Obtained "
    "a pilot's license in 2012 and became a commercial pilot and flight instructor. "
    "Founded Aviloop, an aviation website. Described in some reporting as having "
    "piloted Epstein's aircraft."
)

_DESC_GROFF = (
    "Lesley Groff. Executive assistant to Jeffrey Epstein for nearly 20 years "
    "(approximately 2001-2019). Named co-conspirator in both the 2007 NPA and 2019 FBI "
    "investigation documents. One of the most frequently mentioned names in the "
    "released DOJ Epstein files."
    "\n\n"
    "BACKGROUND: Resided in New Canaan, Connecticut. Joined Epstein's New York office "
    "after posting her resume online and interviewing with both Epstein and Ghislaine "
    "Maxwell. Epstein once described her as 'an extension of my brain.'"
    "\n\n"
    "ROLE: Managed Epstein's schedule, travel logistics, investment meetings, and "
    "correspondence for nearly two decades. Her name appears more than 130,000 times "
    "in released DOJ documents, coordinating everything from meetings with Yale "
    "University professors to investment opportunities to the daily operations of "
    "Epstein's household across multiple properties."
    "\n\n"
    "CO-CONSPIRATOR DESIGNATIONS: Named as a co-conspirator in the 2007 "
    "Non-Prosecution Agreement and received immunity. A 2019 FBI investigation "
    "document listed Groff alongside Ghislaine Maxwell, Jean-Luc Brunel, and Les "
    "Wexner as co-conspirators. According to her attorney, Groff was never notified "
    "of the co-conspirator designation."
    "\n\n"
    "LEGAL OUTCOME: Faced multiple civil lawsuits from Epstein's victims accusing her "
    "of facilitating his crimes. All complaints were eventually dropped. In 2021, "
    "prosecutors declined to charge Groff after she voluntarily spoke with them and "
    "'answered each and every question.' Through her attorney, she has denied any "
    "knowledge of or involvement in Epstein's sex trafficking network."
)

_DESC_JUNKERMANN = (
    "Nicole Junkermann (b. 1975, Dusseldorf, Germany). Entrepreneur, venture "
    "capitalist, and investor whose business activities intersect the Epstein network, "
    "Israeli intelligence-linked technology, and government health advisory roles."
    "\n\n"
    "INVESTMENT CAREER: Founder and chair of NJF Holdings (established 2012), a "
    "private investment group with venture capital, private equity, and real estate "
    "arms focused on health technology, deep tech, and human performance."
    "\n\n"
    "EPSTEIN CONNECTION: Junkermann's name appears in Epstein's flight logs as early "
    "as 2002, documenting approximately 13 flights on his private aircraft. Released "
    "Epstein files revealed intensive contact between Junkermann and Epstein involving "
    "thousands of emails encompassing both business and private matters from 2009 "
    "through 2019 — continuing well after his 2008 conviction. She is mentioned more "
    "than 3,000 times in the Epstein case files."
    "\n\n"
    "CARBYNE AND ISRAELI TECH: In 2016, both Epstein and Junkermann invested in "
    "Carbyne, the Israeli emergency call-handling technology company co-founded by "
    "former Israeli PM Ehud Barak. Epstein invested $1 million through his BVI-"
    "registered Southern Trust; Junkermann's Montilla International contributed "
    "$500,000. Junkermann joined Carbyne's board in 2017, serving alongside Barak "
    "and former Unit 8200 director Pinhas Buchris. Carbyne's board composition — "
    "connecting Epstein money, Israeli intelligence leadership, and surveillance "
    "technology — is structurally significant."
    "\n\n"
    "UK GOVERNMENT ADVISORY ROLE: Appointed to the HealthTech Advisory Board of the "
    "UK Department of Health and Social Care in November 2018 by Health Secretary Matt "
    "Hancock, advising on technology transformation of the NHS. This appointment "
    "placed a figure with documented Epstein financial connections in a health data "
    "advisory role."
    "\n\n"
    "LEGAL ACTIONS: Junkermann has pursued legal action against journalists and "
    "publications investigating her Epstein connections, including the removal of "
    "four Epstein-related articles from Substack in 2025."
)

_DESC_EVA_DUBIN = (
    "Eva Birgitta Andersson-Dubin (b. 1961, Uddevalla, Sweden). Physician, former "
    "model, Miss Sweden 1980, and longtime Epstein social circle member whose "
    "continued relationship with Epstein after his conviction raises significant "
    "questions."
    "\n\n"
    "BACKGROUND: Won the Miss Sweden pageant in 1980 and placed fourth runner-up in "
    "Miss Universe 1980. Studied medicine at the Karolinska Institutet in Stockholm, "
    "then transferred to UCLA School of Medicine, earning her MD in 1989. Completed "
    "residency in internal medicine at Lenox Hill Hospital in New York. Founded the "
    "Dubin Breast Center at the Tisch Cancer Institute at Mount Sinai Hospital."
    "\n\n"
    "EPSTEIN RELATIONSHIP: Dated Jeffrey Epstein from approximately 1981 to 1990 — "
    "one of his earliest known girlfriends. Despite ending the romantic relationship, "
    "the two remained close for decades. Epstein served as godfather to her children "
    "with Glenn Dubin."
    "\n\n"
    "MARRIAGE TO GLENN DUBIN: Married hedge fund billionaire Glenn Dubin in 1994. "
    "Glenn Dubin co-founded Highbridge Capital Management. Bloomberg reporting in "
    "2026 revealed that Eva Dubin's social introduction of Epstein to her husband and "
    "the hedge fund world was a critical pathway for Epstein's financial career."
    "\n\n"
    "POST-CONVICTION CONTACT: Among the earliest in Epstein's social circle to resume "
    "contact after his 2008 release from jail. In 2009, Andersson-Dubin wrote to "
    "Epstein's probation officer stating she was '100% comfortable with Jeffrey "
    "Epstein around my children.' Released Epstein files revealed that in 2010, she "
    "invited Epstein to visit when her 15-year-old daughter would have five friends "
    "over — an invitation that, given Epstein's documented predatory behavior toward "
    "teenage girls, raised alarming questions."
    "\n\n"
    "MAXWELL TRIAL TESTIMONY: Testified at Ghislaine Maxwell's 2021 trial regarding "
    "her longstanding relationship with Epstein and the Epstein-Dubin social dynamic."
)

_DESC_MIDELFART = (
    "Celina Midelfart (b. February 1973, Oslo, Norway). Norwegian cosmetics heiress "
    "and businesswoman. Granddaughter of the founder of the Midelfart cosmetics "
    "company. Connected to both Epstein and Trump through the 1990s New York social "
    "scene."
    "\n\n"
    "EPSTEIN CONNECTION: Multiple sources and Epstein's own emails describe Midelfart "
    "as one of Epstein's girlfriends in the mid-1990s. Flight logs document "
    "approximately 13 flights on Epstein's private aircraft. In a released email, "
    "Epstein linked to an article about Midelfart and described her as 'my 20-year-old "
    "girlfriend in 93, that after two years I gave to Donald' — claiming credit for "
    "introducing her to Trump."
    "\n\n"
    "TRUMP CONNECTION: Midelfart was photographed with Trump at social events in the "
    "late 1990s. According to widely reported accounts, Trump was on a date with "
    "Midelfart at the Kit Kat Club in New York when he first noticed Melania Knauss "
    "and obtained her phone number — the meeting that led to his eventual marriage."
    "\n\n"
    "DENIALS: Through her attorney, Midelfart has stated she had a business connection "
    "with Epstein, not a personal one. She said she rented an apartment in Trump Tower "
    "during her studies in New York (1996-1998), knew Trump as a friend, and "
    "accompanied him to work-related events, but they were never in a romantic "
    "relationship."
    "\n\n"
    "SIGNIFICANCE: Whether or not Epstein's claim to have 'given' Midelfart to Trump "
    "is accurate, the claim itself — made in Epstein's own communications — "
    "demonstrates the transactional way Epstein viewed relationships with young women "
    "and his desire to create social obligations with powerful men."
)

_DESC_MARIA_FARMER = (
    "Maria Kristine Farmer (b. November 28, 1969, Paducah, Kentucky). Visual artist "
    "and the first known person to file a criminal complaint against Jeffrey Epstein "
    "and Ghislaine Maxwell — in 1996, nine years before the Palm Beach investigation."
    "\n\n"
    "BACKGROUND: Trained as a figurative painter at the New York Academy of Art. "
    "Entered Epstein's orbit in 1995 as an art researcher hired to source works for "
    "his collection. At the time, she was in graduate school and selling artwork from "
    "her studio."
    "\n\n"
    "SEXUAL ASSAULT AT WEXNER ESTATE (1996): In May 1996, Farmer traveled to Les "
    "Wexner's property in Ohio as an artist-in-residence. The estate was guarded by "
    "Wexner's armed security and she was required to call Wexner's wife for permission "
    "to leave. Farmer stated in a sworn affidavit that Epstein and Maxwell came to the "
    "property and sexually assaulted her. This assault occurred at Wexner's personal "
    "estate — placing the Epstein operation's activities directly within Wexner's "
    "physical domain."
    "\n\n"
    "FBI REPORT — THE FIRST COMPLAINT (1996): On August 26, 1996, Farmer called the "
    "NYPD and FBI to report the assault. On September 3, 1996, she reported to the "
    "FBI that nude photographs of her younger sisters — then aged 12 and 16 — had been "
    "stolen from her storage, expressing concerns about child pornography. The DOJ "
    "file release in 2026 provided irrefutable proof of this 1996 FBI report, "
    "confirming Farmer filed one of the earliest complaints against Epstein."
    "\n\n"
    "SISTER ANNIE FARMER: Maria's younger sister Annie was 15 years old when she was "
    "sexually assaulted by Epstein and Maxwell in separate incidents in 1996, including "
    "at Epstein's Zorro Ranch in New Mexico. Annie later became a psychologist "
    "specializing in trauma recovery and testified at Ghislaine Maxwell's 2021 trial."
    "\n\n"
    "SIGNIFICANCE: Farmer's 1996 complaint demonstrates that law enforcement — both "
    "NYPD and FBI — had documented allegations against Epstein and Maxwell nine years "
    "before the Palm Beach investigation. The failure to act on these early reports is "
    "part of the documented pattern of institutional protection around Epstein."
)

_DESC_COURTNEY_WILD = (
    "Courtney Wild. Epstein victim and legal advocate who led the most significant "
    "challenge to the 2007 Non-Prosecution Agreement through the federal courts."
    "\n\n"
    "RECRUITMENT: Wild was 14 years old when she was first recruited to Epstein's Palm "
    "Beach mansion in 2001. A friend told her about 'a really cool guy on Palm Beach "
    "Island' from whom they could earn $200 for a massage. Wild had been a straight-A "
    "student, cheerleading captain, and first chair trumpet, but her parents' struggles "
    "with addiction and homelessness had destabilized her life."
    "\n\n"
    "GROOMING AND EXPLOITATION: Wild described being sexually abused by Epstein and "
    "then groomed into his recruitment pyramid — she was offered $200 'finder's fees' "
    "for bringing new girls to his mansion. She sometimes brought two or three girls "
    "in a single day. Epstein groomed her to be, in her words, his 'personal sex slave "
    "that brought him underage girls.'"
    "\n\n"
    "CRIME VICTIMS' RIGHTS ACT CHALLENGE: In 2014, Wild (as Jane Doe 1) filed a "
    "federal civil suit against the United States for violations of the Crime Victims' "
    "Rights Act, arguing that federal prosecutors violated victims' rights when they "
    "secretly negotiated the 2007 NPA with Epstein's attorneys without notifying or "
    "consulting victims as required by law."
    "\n\n"
    "LEGAL OUTCOME: A federal district court ruled that victims' rights were violated. "
    "However, in April 2020, the 11th Circuit narrowly reversed, ruling that because "
    "the government never formally filed charges, the CVRA was technically never "
    "triggered. In 2022, the US Supreme Court declined to hear Wild's appeal. The case "
    "inspired the proposed 'Courtney Wild Reinforcing Crime Victims' Rights Act' "
    "introduced in Congress."
    "\n\n"
    "SIGNIFICANCE: Wild fought for over 10 years through federal courts to hold the "
    "government accountable for the NPA. Her case exposed the legal mechanisms by which "
    "Acosta's office shielded Epstein and his co-conspirators from meaningful "
    "prosecution."
)


# ============================================================
# ENTITIES
# ============================================================

NEW_ENTITIES = [
    # ---- Victims / Witnesses ----
    {"name": "Virginia Giuffre", "entity_type": "person", "description": _DESC_GIUFFRE, "aliases": "Virginia Roberts, Jenna", "metadata": {"birth_date": "1983-08-09", "death_date": "2025-04-25", "nationality": "American-Australian", "status": "deceased"}},
    {"name": "Maria Farmer", "entity_type": "person", "description": _DESC_MARIA_FARMER, "aliases": "", "metadata": {"birth_date": "1969-11-28", "nationality": "American", "status": "alive"}},
    {"name": "Courtney Wild", "entity_type": "person", "description": _DESC_COURTNEY_WILD, "aliases": "Jane Doe 1", "metadata": {"nationality": "American", "status": "alive"}},

    # ---- Inner Circle / Enablers ----
    {"name": "Sarah Kellen", "entity_type": "person", "description": _DESC_KELLEN, "aliases": "Sarah Kellen Vickers, Sarah Kensington", "metadata": {"birth_year": 1980, "nationality": "American", "status": "alive"}},
    {"name": "Nadia Marcinkova", "entity_type": "person", "description": _DESC_MARCINKOVA, "aliases": "Nadia Marcinko, Nada Marcinkova", "metadata": {"birth_year": 1986, "nationality": "Slovak-American", "status": "alive"}},
    {"name": "Lesley Groff", "entity_type": "person", "description": _DESC_GROFF, "aliases": "Leslie Groff", "metadata": {"nationality": "American", "status": "alive"}},
    {"name": "Nicole Junkermann", "entity_type": "person", "description": _DESC_JUNKERMANN, "aliases": "", "metadata": {"birth_year": 1975, "nationality": "German", "status": "alive"}},
    {"name": "Eva Andersson-Dubin", "entity_type": "person", "description": _DESC_EVA_DUBIN, "aliases": "Eva Dubin, Eva Andersson", "metadata": {"birth_year": 1961, "nationality": "Swedish-American", "status": "alive"}},
    {"name": "Celina Midelfart", "entity_type": "person", "description": _DESC_MIDELFART, "aliases": "", "metadata": {"birth_year": 1973, "nationality": "Norwegian", "status": "alive"}},

    # ---- Organizations ----
    {"name": "Dalton School", "entity_type": "organization", "description": (
        "The Dalton School. Elite private school on Manhattan's Upper East Side. "
        "Founded in 1919. Significant in the Epstein network because headmaster Donald "
        "Barr — an OSS veteran and father of future Attorney General William Barr — hired "
        "20-year-old Jeffrey Epstein to teach calculus and physics there in 1973-1974, "
        "despite Epstein lacking a college degree or teaching credentials. Barr resigned "
        "as headmaster in February 1974, shortly after hiring Epstein. Epstein taught at "
        "Dalton for approximately two years before leaving for Bear Stearns. The hiring "
        "decision — an OSS-connected headmaster giving an unqualified 20-year-old access "
        "to elite prep school students — has been the subject of significant scrutiny "
        "in the context of Epstein's later pattern of targeting young people."
    ), "aliases": ""},
    {"name": "Towers Financial", "entity_type": "organization", "description": (
        "Towers Financial Corporation. Manhattan-based debt collection agency that "
        "operated a $475 million Ponzi scheme between 1988 and 1993 — the largest "
        "financial fraud in American history prior to Bernie Madoff. Founded and run by "
        "Steven Hoffenberg, who met Jeffrey Epstein in 1987 through British defense "
        "contractor Douglas Leese. Hoffenberg hired Epstein as a senior consultant, "
        "paying him $25,000 per month and providing a $2 million loan that was never "
        "repaid. In court documents, Hoffenberg described Epstein as intimately involved "
        "in the scheme and called him 'the architect of the scam.' Epstein left Towers "
        "Financial before its 1993 collapse and was never charged. Hoffenberg pleaded "
        "guilty in 1995 and served 18 years in prison. He was found dead in his "
        "Connecticut apartment in August 2022 at age 77. In 2016, Hoffenberg and some "
        "of his victims sued Epstein seeking restitution. Towers Financial represents "
        "the earliest documented evidence of Epstein's involvement in large-scale "
        "financial fraud."
    ), "aliases": "TFC"},

    # ---- Facilities ----
    {"name": "Zorro Ranch", "entity_type": "facility", "description": (
        "Zorro Ranch. A 10,000-acre private property located near Stanley, New Mexico, "
        "approximately 30 miles southeast of Santa Fe. Owned by Jeffrey Epstein from "
        "the early 1990s until his death in 2019. Approximately 1,200 acres were leased "
        "from the New Mexico State Land Commission."
        "\n\n"
        "Virginia Giuffre testified in her 2016 deposition that she was trafficked to "
        "powerful men at the ranch, specifically alleging that Ghislaine Maxwell "
        "instructed her to provide sexual services to former New Mexico Governor Bill "
        "Richardson there. Annie Farmer, then 15, was sexually assaulted by Epstein at "
        "the ranch in April 1996."
        "\n\n"
        "Epstein donated $50,000 to Governor Richardson's 2006 reelection campaign and "
        "$15,000 to the state Attorney General race. In 2019, the New Mexico State Land "
        "Office cancelled Epstein's grazing lease. As of 2026, New Mexico has approved "
        "a comprehensive probe of the ranch through an Epstein Truth Commission, and "
        "the DOJ is investigating claims of burials near the property."
    ), "aliases": "Epstein Ranch, Stanley Ranch"},
    {"name": "9 East 71st Street", "entity_type": "facility", "description": (
        "9 East 71st Street. The Herbert N. Straus House, a seven-story neo-French "
        "Renaissance mansion on Manhattan's Upper East Side. One of the largest private "
        "residences in New York City, valued at approximately $77 million."
        "\n\n"
        "OWNERSHIP HISTORY: Originally built in 1932. Occupied by the Birch Wathen "
        "School from 1962 to 1989. Purchased by Les Wexner for $13.2 million in 1989. "
        "Wexner renovated the property extensively. Jeffrey Epstein moved in by 1996. "
        "The property was ultimately transferred to Epstein through a series of "
        "transactions with nominal or zero consideration — deeds show $0 or '$10 and "
        "other valuable consideration.' The transfer of one of Manhattan's most "
        "valuable private homes for effectively nothing remains one of the most "
        "significant unexplained financial transactions in the Epstein-Wexner "
        "relationship."
        "\n\n"
        "AS EPSTEIN'S HEADQUARTERS: The mansion served as Epstein's primary residence "
        "and operational base. Visitors described surveillance cameras throughout, "
        "including in bathrooms and bedrooms. Multiple victims described being abused "
        "in the mansion. The property was listed for sale by Epstein's estate after "
        "his death."
    ), "aliases": "Epstein Manhattan Mansion, Straus House"},
    {"name": "MCC New York", "entity_type": "facility", "description": (
        "Metropolitan Correctional Center, New York. Federal detention facility in "
        "Lower Manhattan operated by the Bureau of Prisons. The facility where Jeffrey "
        "Epstein was found dead on August 10, 2019, while awaiting trial on sex "
        "trafficking charges."
        "\n\n"
        "EPSTEIN'S DEATH: Epstein was found unresponsive in his cell at approximately "
        "6:30 AM, hanging from a bedsheet tied to the upper bunk. The New York City "
        "medical examiner ruled the death a suicide by hanging. The DOJ Inspector "
        "General's report documented catastrophic security failures."
        "\n\n"
        "SECURITY FAILURES: Two correctional officers — Michael Thomas and Tova Noel — "
        "assigned to guard Epstein overnight failed to complete more than 75 mandatory "
        "checks. Both officers were found to have been sleeping and later falsified "
        "records to cover the lapse. Nearly all cameras in and around the Special "
        "Housing Unit where Epstein was held stopped recording in late July 2019, "
        "continuing through the date of his death. Five hours of footage from a camera "
        "outside Epstein's cell on the night of a previous incident (July 22-23) were "
        "'mistakenly not preserved.'"
        "\n\n"
        "2026 DEVELOPMENTS: Newly released DOJ documents and surveillance logs raised "
        "additional questions, with investigators noting an unidentified orange-colored "
        "figure moving toward Epstein's locked housing tier at approximately 10:39 PM "
        "on August 9, 2019. The facility was permanently closed in 2021 due to "
        "deplorable conditions."
    ), "aliases": "Metropolitan Correctional Center"},

    # ---- Events ----
    {"name": "Epstein Palm Beach Investigation (2005)", "entity_type": "event", "description": (
        "Palm Beach police investigation into Jeffrey Epstein, initiated in March 2005 "
        "when a mother reported that her 14-year-old daughter was being sexually abused "
        "by an adult male at a Palm Beach mansion."
        "\n\n"
        "Led by Police Chief Michael Reiter, detectives conducted interviews with more "
        "than 20 alleged victims and 17 witnesses over approximately one year. Victims "
        "led detectives to other victims in a cascading pattern, all telling 'basically "
        "the same story.' Reiter requested charges of at least four counts of unlawful "
        "sexual activity with a minor."
        "\n\n"
        "The case was referred to the FBI and US Attorney's office. An AUSA submitted "
        "a draft 60-count indictment. However, prosecutors told Reiter the witnesses "
        "were 'not credible' and became dismissive and uncooperative. The case was "
        "eventually resolved through the 2007 Non-Prosecution Agreement negotiated by "
        "US Attorney Alexander Acosta."
        "\n\n"
        "Reiter described the handling of the case as 'the worst failure of the criminal "
        "justice system' in modern times. The investigation also revealed that Epstein "
        "was likely tipped off during the probe, suggesting law enforcement leaks."
    ), "aliases": "Palm Beach Epstein Case"},
    {"name": "Maxwell Trial (2021)", "entity_type": "event", "description": (
        "United States v. Ghislaine Maxwell (S.D.N.Y. 20-cr-330). Federal sex "
        "trafficking trial held November-December 2021 in Manhattan."
        "\n\n"
        "Ghislaine Maxwell was charged with six counts including sex trafficking of a "
        "minor, enticement of a minor, and conspiracy. Over three weeks of testimony, "
        "four women described how Maxwell recruited them into Epstein's orbit, presenting "
        "herself as a friendly older woman, earning trust through gifts and shopping "
        "sprees, then facilitating sexual abuse by Epstein. Two witnesses testified they "
        "were 14 years old when Maxwell lured them into sexual acts with Epstein."
        "\n\n"
        "VERDICT: On December 29, 2021, after five days of deliberation, the jury "
        "convicted Maxwell on five of six counts: sex trafficking of a minor (max 40 "
        "years), transporting a minor for criminal sexual activity (10 years), and "
        "three conspiracy counts (15 years total). She was acquitted on one count of "
        "enticement."
        "\n\n"
        "SENTENCING: On June 28, 2022, Maxwell was sentenced to 20 years in federal "
        "prison by Judge Alison Nathan. Her conviction was upheld on appeal by the "
        "Second Circuit in September 2024. Maxwell is currently incarcerated."
        "\n\n"
        "SIGNIFICANCE: The Maxwell trial was the only federal criminal proceeding "
        "arising from the Epstein investigation to produce a conviction beyond Epstein's "
        "own 2008 plea. Despite evidence implicating numerous co-conspirators, no other "
        "individuals have been federally charged."
    ), "aliases": "United States v. Maxwell"},
]


# ============================================================
# RELATIONSHIPS
# ============================================================

NEW_RELATIONSHIPS = [
    # ---- Virginia Giuffre connections ----
    {"source": "Virginia Giuffre", "target": "Jeffrey Epstein", "type": "trafficked_by", "tier": "documented", "desc": "Recruited at age 16 at Mar-a-Lago by Ghislaine Maxwell in 2000. Trafficked to multiple properties and individuals. Filed civil suits. Settled with Epstein estate.", "sources": [116, 29, 140]},
    {"source": "Virginia Giuffre", "target": "Ghislaine Maxwell", "type": "trafficked_by", "tier": "documented", "desc": "Maxwell personally recruited Giuffre at Mar-a-Lago spa. Giuffre's testimony was central to Maxwell's 2021 conviction.", "sources": [116, 117, 140]},
    {"source": "Virginia Giuffre", "target": "Alan Dershowitz", "type": "connected_to", "tier": "credible", "desc": "Named Dershowitz as participant in trafficking. Both filed competing defamation claims. Giuffre's suit settled 2022.", "sources": [116, 29]},
    {"source": "Virginia Giuffre", "target": "Mar-a-Lago", "type": "connected_to", "tier": "documented", "desc": "Working as spa attendant at Mar-a-Lago when recruited by Maxwell at age 16 in 2000.", "sources": [116, 140]},
    {"source": "Virginia Giuffre", "target": "Little Saint James", "type": "connected_to", "tier": "documented", "desc": "Testified she was trafficked to Epstein's private island multiple times.", "sources": [116, 29]},
    {"source": "Virginia Giuffre", "target": "Zorro Ranch", "type": "connected_to", "tier": "documented", "desc": "Testified she was trafficked at the ranch and instructed to provide sexual services to visitors there.", "sources": [116, 29, 133]},
    {"source": "Virginia Giuffre", "target": "9 East 71st Street", "type": "connected_to", "tier": "documented", "desc": "Testified she was abused at Epstein's Manhattan mansion on multiple occasions.", "sources": [116, 29]},
    {"source": "Virginia Giuffre", "target": "Maxwell Trial (2021)", "type": "connected_to", "tier": "documented", "desc": "Giuffre's prior testimony and depositions were central to the prosecution's case, though she did not testify at trial.", "sources": [117, 126]},

    # ---- Sarah Kellen connections ----
    {"source": "Sarah Kellen", "target": "Jeffrey Epstein", "type": "employed_by", "tier": "documented", "desc": "Primary day-to-day scheduler across Palm Beach, Manhattan and other properties. Named co-conspirator in NPA.", "sources": [121, 124, 31]},
    {"source": "Sarah Kellen", "target": "Ghislaine Maxwell", "type": "co_conspirator_of", "tier": "documented", "desc": "Both named co-conspirators in NPA. Judge Nathan described Kellen as 'a knowing participant in the criminal conspiracy.'", "sources": [121, 117]},
    {"source": "Sarah Kellen", "target": "Epstein NPA (2007)", "type": "connected_to", "tier": "documented", "desc": "Named as co-conspirator in the Non-Prosecution Agreement. Received immunity from federal prosecution.", "sources": [121, 122]},

    # ---- Nadia Marcinkova connections ----
    {"source": "Nadia Marcinkova", "target": "Jeffrey Epstein", "type": "trafficked_by", "tier": "documented", "desc": "Brought to US by Epstein as teenager from Slovakia. Epstein described her as his 'sex slave' he 'purchased' from her family. Also named NPA co-conspirator.", "sources": [121, 124, 31]},
    {"source": "Nadia Marcinkova", "target": "Epstein NPA (2007)", "type": "connected_to", "tier": "documented", "desc": "Named as co-conspirator in the Non-Prosecution Agreement. Received immunity from federal prosecution.", "sources": [121, 122]},

    # ---- Lesley Groff connections ----
    {"source": "Lesley Groff", "target": "Jeffrey Epstein", "type": "employed_by", "tier": "documented", "desc": "Executive assistant for nearly 20 years (2001-2019). Described by Epstein as 'an extension of my brain.' Named co-conspirator in NPA and 2019 FBI document.", "sources": [121, 134, 124]},
    {"source": "Lesley Groff", "target": "Ghislaine Maxwell", "type": "co_conspirator_of", "tier": "documented", "desc": "Both listed as co-conspirators on 2019 FBI investigation document alongside Brunel and Wexner.", "sources": [134, 121]},
    {"source": "Lesley Groff", "target": "Epstein NPA (2007)", "type": "connected_to", "tier": "documented", "desc": "Named as co-conspirator in the Non-Prosecution Agreement. Received immunity from federal prosecution.", "sources": [121, 122]},

    # ---- Nicole Junkermann connections ----
    {"source": "Nicole Junkermann", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "documented", "desc": "Flight logs show 13 flights on Epstein's aircraft from 2002. Thousands of emails 2009-2019. Mentioned 3,000+ times in Epstein files.", "sources": [127, 135, 30]},
    {"source": "Nicole Junkermann", "target": "Carbyne", "type": "member_of", "tier": "documented", "desc": "Invested $500K via Montilla International in 2016. Joined Carbyne board in 2017 alongside Ehud Barak and ex-Unit 8200 director.", "sources": [127]},
    {"source": "Nicole Junkermann", "target": "Ehud Barak", "type": "associate_of", "tier": "documented", "desc": "Co-invested in Carbyne with Epstein. Served on Carbyne board alongside Barak.", "sources": [127]},

    # ---- Eva Andersson-Dubin connections ----
    {"source": "Eva Andersson-Dubin", "target": "Jeffrey Epstein", "type": "romantic_partner_of", "tier": "documented", "desc": "Dated Epstein 1981-1990. Remained close for decades. Epstein was godfather to her children. Invited him around teenage daughter post-conviction.", "sources": [128, 138, 117]},
    {"source": "Eva Andersson-Dubin", "target": "Ghislaine Maxwell", "type": "associate_of", "tier": "credible", "desc": "Part of overlapping social circle. Testified at Maxwell's 2021 trial about her relationship with Epstein.", "sources": [138, 117]},
    {"source": "Eva Andersson-Dubin", "target": "Maxwell Trial (2021)", "type": "connected_to", "tier": "documented", "desc": "Testified at Ghislaine Maxwell's trial regarding her longstanding relationship with Epstein.", "sources": [138]},

    # ---- Celina Midelfart connections ----
    {"source": "Celina Midelfart", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "credible", "desc": "Described by Epstein as his 'girlfriend in 93.' 13 flights on Epstein aircraft per flight logs. Midelfart disputes romantic relationship.", "sources": [129, 30]},
    {"source": "Celina Midelfart", "target": "Donald Trump", "type": "associate_of", "tier": "credible", "desc": "Photographed together at social events late 1990s. Epstein claimed he 'gave' Midelfart to Trump. Midelfart says friendship only.", "sources": [129]},
    {"source": "Jeffrey Epstein", "target": "Celina Midelfart", "type": "introduced_by", "tier": "credible", "desc": "Epstein claimed in email he introduced Midelfart to Trump: 'my 20-year-old girlfriend in 93 that after two years I gave to Donald.'", "sources": [129]},

    # ---- Maria Farmer connections ----
    {"source": "Maria Farmer", "target": "Jeffrey Epstein", "type": "trafficked_by", "tier": "documented", "desc": "Assaulted by Epstein and Maxwell at Wexner's Ohio estate in 1996. Filed first-ever criminal complaint against Epstein to NYPD and FBI in August 1996.", "sources": [119, 139, 116]},
    {"source": "Maria Farmer", "target": "Ghislaine Maxwell", "type": "trafficked_by", "tier": "documented", "desc": "Assaulted by both Epstein and Maxwell at Wexner's Ohio estate. Filed FBI report naming both.", "sources": [119, 139]},
    {"source": "Maria Farmer", "target": "Les Wexner", "type": "connected_to", "tier": "documented", "desc": "Assault occurred at Wexner's personal Ohio estate. Armed Wexner security controlled access. Farmer required permission from Wexner's wife to leave.", "sources": [119, 139]},
    {"source": "Maria Farmer", "target": "FBI", "type": "connected_to", "tier": "documented", "desc": "Filed criminal complaint with FBI on August 26, 1996. Reported stolen photos of minor sisters on September 3, 1996. 2026 DOJ release confirmed original 1996 FBI report.", "sources": [119, 139]},

    # ---- Courtney Wild connections ----
    {"source": "Courtney Wild", "target": "Jeffrey Epstein", "type": "trafficked_by", "tier": "documented", "desc": "Recruited at age 14 in 2001 to Epstein's Palm Beach mansion. Groomed into recruitment pyramid. Lead plaintiff in CVRA challenge to the NPA.", "sources": [118, 136, 31]},
    {"source": "Courtney Wild", "target": "Epstein NPA (2007)", "type": "connected_to", "tier": "documented", "desc": "As Jane Doe 1, filed 2014 federal suit challenging the NPA under Crime Victims' Rights Act. District court ruled victims' rights violated. 11th Circuit reversed. SCOTUS declined review.", "sources": [118, 136]},
    {"source": "Courtney Wild", "target": "Alexander Acosta", "type": "connected_to", "tier": "documented", "desc": "Wild's CVRA case directly challenged Acosta's handling of the NPA. District court found Acosta's office violated victims' rights.", "sources": [118, 122]},

    # ---- Facility connections ----
    {"source": "Donald Barr", "target": "Dalton School", "type": "director_of", "tier": "documented", "desc": "Headmaster 1964-1974. Hired 20-year-old Epstein to teach despite no degree. Resigned February 1974. OSS veteran.", "sources": [132, 11]},
    {"source": "Jeffrey Epstein", "target": "Dalton School", "type": "employed_by", "tier": "documented", "desc": "Taught calculus and physics 1973-1975 despite lacking a college degree. Hired by headmaster Donald Barr.", "sources": [132, 11]},
    {"source": "Jeffrey Epstein", "target": "Towers Financial", "type": "employed_by", "tier": "documented", "desc": "Worked with Steven Hoffenberg 1987-1993 in $475M Ponzi scheme. Hoffenberg called Epstein 'the architect of the scam.' Epstein never charged.", "sources": [130, 131]},
    {"source": "Jeffrey Epstein", "target": "Zorro Ranch", "type": "affiliated_with", "tier": "documented", "desc": "Owned the 10,000-acre New Mexico ranch from early 1990s until death. Site of documented abuse of Annie Farmer and others.", "sources": [133, 116]},
    {"source": "Jeffrey Epstein", "target": "9 East 71st Street", "type": "affiliated_with", "tier": "documented", "desc": "Primary residence and operational base. Transferred from Wexner for $0 or nominal consideration. Surveillance cameras throughout including bathrooms.", "sources": [137, 11]},
    {"source": "Les Wexner", "target": "9 East 71st Street", "type": "connected_to", "tier": "documented", "desc": "Purchased for $13.2M in 1989. Transferred to Epstein for nominal or zero consideration. One of the most significant unexplained transactions in the network.", "sources": [137, 11]},
    {"source": "Jeffrey Epstein", "target": "MCC New York", "type": "connected_to", "tier": "documented", "desc": "Held at MCC awaiting trial on sex trafficking charges. Found dead in cell August 10, 2019. Two cameras failed. Two guards sleeping.", "sources": [120]},
    {"source": "Epstein Death (2019)", "target": "MCC New York", "type": "connected_to", "tier": "documented", "desc": "Epstein found dead at MCC. DOJ IG report documented catastrophic security failures: camera malfunctions, sleeping guards, falsified records.", "sources": [120]},

    # ---- Event connections ----
    {"source": "Epstein Palm Beach Investigation (2005)", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Investigation by Palm Beach PD Chief Michael Reiter. 20+ victims interviewed. 60-count draft indictment prepared. Led to NPA instead of prosecution.", "sources": [125, 31]},
    {"source": "Epstein Palm Beach Investigation (2005)", "target": "Epstein NPA (2007)", "type": "connected_to", "tier": "documented", "desc": "Palm Beach investigation produced evidence for 60-count indictment. Instead, Acosta negotiated the NPA. Reiter called it 'worst failure of criminal justice system.'", "sources": [125, 122]},
    {"source": "Maxwell Trial (2021)", "target": "Ghislaine Maxwell", "type": "connected_to", "tier": "documented", "desc": "Convicted on 5 of 6 counts including sex trafficking of a minor. Sentenced to 20 years. Conviction upheld on appeal 2024.", "sources": [117, 126]},
    {"source": "Maxwell Trial (2021)", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "documented", "desc": "Trial established the scope of Epstein's trafficking operation through witness testimony. Only criminal proceeding to produce conviction beyond Epstein's own plea.", "sources": [117, 126]},

    # ---- Cross-connections between enablers ----
    {"source": "Sarah Kellen", "target": "Nadia Marcinkova", "type": "co_conspirator_of", "tier": "documented", "desc": "Both named as co-conspirators in 2007 NPA. Both received immunity. Both operated within Epstein's inner circle.", "sources": [121]},
    {"source": "Sarah Kellen", "target": "Lesley Groff", "type": "co_conspirator_of", "tier": "documented", "desc": "Both named as co-conspirators in 2007 NPA. Both received immunity. Kellen handled scheduling; Groff managed executive operations.", "sources": [121]},
    {"source": "Nadia Marcinkova", "target": "Lesley Groff", "type": "co_conspirator_of", "tier": "documented", "desc": "Both named as co-conspirators in 2007 NPA. Both received immunity from federal prosecution.", "sources": [121]},
]


# ============================================================
# ENTITY_SOURCES — direct entity-to-source citations
# ============================================================

NEW_ENTITY_SOURCES = [
    # Virginia Giuffre
    {"entity_name": "Virginia Giuffre", "source_id": 116},
    {"entity_name": "Virginia Giuffre", "source_id": 117},
    {"entity_name": "Virginia Giuffre", "source_id": 123},
    {"entity_name": "Virginia Giuffre", "source_id": 126},
    {"entity_name": "Virginia Giuffre", "source_id": 129},
    {"entity_name": "Virginia Giuffre", "source_id": 140},
    {"entity_name": "Virginia Giuffre", "source_id": 29},
    {"entity_name": "Virginia Giuffre", "source_id": 30},
    {"entity_name": "Virginia Giuffre", "source_id": 31},

    # Sarah Kellen
    {"entity_name": "Sarah Kellen", "source_id": 121},
    {"entity_name": "Sarah Kellen", "source_id": 122},
    {"entity_name": "Sarah Kellen", "source_id": 124},
    {"entity_name": "Sarah Kellen", "source_id": 31},

    # Nadia Marcinkova
    {"entity_name": "Nadia Marcinkova", "source_id": 121},
    {"entity_name": "Nadia Marcinkova", "source_id": 122},
    {"entity_name": "Nadia Marcinkova", "source_id": 124},
    {"entity_name": "Nadia Marcinkova", "source_id": 31},

    # Lesley Groff
    {"entity_name": "Lesley Groff", "source_id": 121},
    {"entity_name": "Lesley Groff", "source_id": 122},
    {"entity_name": "Lesley Groff", "source_id": 124},
    {"entity_name": "Lesley Groff", "source_id": 134},

    # Nicole Junkermann
    {"entity_name": "Nicole Junkermann", "source_id": 127},
    {"entity_name": "Nicole Junkermann", "source_id": 135},
    {"entity_name": "Nicole Junkermann", "source_id": 30},

    # Eva Andersson-Dubin
    {"entity_name": "Eva Andersson-Dubin", "source_id": 117},
    {"entity_name": "Eva Andersson-Dubin", "source_id": 128},
    {"entity_name": "Eva Andersson-Dubin", "source_id": 138},

    # Celina Midelfart
    {"entity_name": "Celina Midelfart", "source_id": 129},
    {"entity_name": "Celina Midelfart", "source_id": 30},

    # Maria Farmer
    {"entity_name": "Maria Farmer", "source_id": 119},
    {"entity_name": "Maria Farmer", "source_id": 139},
    {"entity_name": "Maria Farmer", "source_id": 116},

    # Courtney Wild
    {"entity_name": "Courtney Wild", "source_id": 118},
    {"entity_name": "Courtney Wild", "source_id": 122},
    {"entity_name": "Courtney Wild", "source_id": 136},
    {"entity_name": "Courtney Wild", "source_id": 31},

    # Dalton School
    {"entity_name": "Dalton School", "source_id": 132},
    {"entity_name": "Dalton School", "source_id": 11},

    # Towers Financial
    {"entity_name": "Towers Financial", "source_id": 130},
    {"entity_name": "Towers Financial", "source_id": 131},

    # Zorro Ranch
    {"entity_name": "Zorro Ranch", "source_id": 133},
    {"entity_name": "Zorro Ranch", "source_id": 116},
    {"entity_name": "Zorro Ranch", "source_id": 29},

    # 9 East 71st Street
    {"entity_name": "9 East 71st Street", "source_id": 137},
    {"entity_name": "9 East 71st Street", "source_id": 11},

    # MCC New York
    {"entity_name": "MCC New York", "source_id": 120},

    # Events
    {"entity_name": "Epstein Palm Beach Investigation (2005)", "source_id": 125},
    {"entity_name": "Epstein Palm Beach Investigation (2005)", "source_id": 31},
    {"entity_name": "Epstein Palm Beach Investigation (2005)", "source_id": 122},
    {"entity_name": "Maxwell Trial (2021)", "source_id": 117},
    {"entity_name": "Maxwell Trial (2021)", "source_id": 126},
]
