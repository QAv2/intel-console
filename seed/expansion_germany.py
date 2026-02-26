"""
Germany Cluster — Expansion layer for Intel Console.

Deep dive into Deutsche Bank's role as Epstein's banker (2013-2018), the
compliance failures documented in the DFS consent order, the personnel who
enabled and those who tried to stop it, and the broader pattern of Deutsche
Bank scandals ($10B Russian mirror trading, $2.5B Trump loans).

Also maps BND (German intelligence, created by CIA via Gehlen Organization),
and Philippa Sigl-Glockner (Scholz aide named in 2026 Epstein files, described
as former German intelligence).

Key threads:
- Deutsche Bank onboarded Epstein AFTER JPMorgan dropped him, despite knowing
  his criminal history (17 out-of-court sex abuse settlements documented in memo)
- Same private wealth division handled Epstein AND Trump/Kushner accounts
- Tammy McFadden flagged Epstein transactions, claims retaliation firing
- Thomas Bowers approved both Epstein accounts and Trump loans, died Nov 2019
- Val Broeksmit leaked thousands of DB documents to FBI, found dead Apr 2022
- DFS $150M consent order (2020) + $75M civil settlement (2023)
- $10B Russian mirror trading through DB Moscow/London/NY (2011-2015)
- BND created by CIA through Gehlen Organization (1956), Mossad cooperation (1957+)

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Jeffrey Epstein [1], Deutsche Bank [57], Donald Trump [33],
  CIA [85], FBI [87], Mossad [88], DOJ [89], NSA [86],
  JPMorgan Chase [56], Nicole Junkermann [151]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 373+ (continuing from existing 372)
# ============================================================

SOURCES = [
    {
        "id": 373,
        "title": "NY Department of Financial Services — Consent Order: Deutsche Bank AG, $150 million penalty for significant compliance failures in connection with Jeffrey Epstein, Danske Bank Estonia, and FBME Bank (July 7, 2020)",
        "url": "https://www.dfs.ny.gov/system/files/documents/2020/07/ea20200706_deutsche_bank_consent_order.pdf",
        "source_type": "government",
        "year": 2020,
    },
    {
        "id": 374,
        "title": "NY DFS Press Release — 'DFS Fines Deutsche Bank $150 Million for Compliance Failures Including Jeffrey Epstein and Danske Bank Estonia' (July 7, 2020, documents DB maintained 40+ Epstein accounts)",
        "url": "https://www.dfs.ny.gov/reports_and_publications/press_releases/pr202007071",
        "source_type": "government",
        "year": 2020,
    },
    {
        "id": 375,
        "title": "NPR — 'Deutsche Bank settles lawsuit with Epstein accusers for $75 million' (May 18, 2023, victims to receive $75K-$5M per claim, DB did not admit wrongdoing)",
        "url": "https://www.npr.org/2023/05/18/1176974676/deutsche-bank-settles-lawsuit-with-epstein-accusers-for-75-million",
        "source_type": "journalism",
        "year": 2023,
    },
    {
        "id": 376,
        "title": "CNBC — Deutsche Bank CEO Christian Sewing: 'It was a critical mistake... Mr. Epstein should have never been onboarded, should have never been our client' (July 7, 2020)",
        "url": "https://www.cnbc.com/2020/07/07/jeffrey-epstein-penalty-deutsche-bank-ceo-christian-sewing-says-firm-learned-our-lesson.html",
        "source_type": "journalism",
        "year": 2020,
    },
    {
        "id": 377,
        "title": "The Lever — 'The Compliance Officer Who Flagged Epstein — and Lost Her Job' (Tammy McFadden flagged transactions to young women, French art gallery; entire Jacksonville team wanted to terminate Epstein; she was moved and laid off)",
        "url": "https://www.levernews.com/the-compliance-officer-who-flagged-epstein-and-lost-her-job/",
        "source_type": "journalism",
        "year": 2020,
    },
    {
        "id": 378,
        "title": "Fortune — 'Deutsche Bank and Jeffrey Epstein: Ghost of the Relationship' (Charles Packard approved Epstein relationship, Paul Morris pitched him as $2-4M/year client)",
        "url": "https://fortune.com/2025/10/08/deutsche-bank-and-jeffrey-epstein-ghost/",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 379,
        "title": "Law & Crime — 'Former Deutsche Bank executive who oversaw Trump's loans dies by suicide' (Thomas Bowers, November 19, 2019, Malibu, found hanging, age 55)",
        "url": "https://lawandcrime.com/high-profile/former-deutsche-bank-executive-who-oversaw-trumps-loans-dies-by-suicide/",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 380,
        "title": "The Hill — 'Informant in federal probe into Trump-Deutsche Bank relationship found dead' (Val Broeksmit, April 25, 2022, Los Angeles, found at Woodrow Wilson High School, ruled accidental)",
        "url": "https://thehill.com/homenews/3470023-informant-in-federal-probe-into-trump-deutsche-bank-relationship-found-dead/",
        "source_type": "journalism",
        "year": 2022,
    },
    {
        "id": 381,
        "title": "Newsweek — 'Deutsche Bank article found among Trump's classified documents at Mar-a-Lago' (December 2023, questions about why such material was retained)",
        "url": "https://www.newsweek.com/donald-trump-mar-lago-deutsche-bank-whistleblower-florida-palm-beach-aileen-cannon-1917559",
        "source_type": "journalism",
        "year": 2023,
    },
    {
        "id": 382,
        "title": "NY DFS — Consent Order: Deutsche Bank AG, $425 million penalty for Russian mirror trading scheme that laundered $10 billion through Moscow, London, and New York offices (2011-2015). FCA added £163 million. Total ~$630 million. (January 30, 2017)",
        "url": "https://www.dfs.ny.gov/reports_and_publications/press_releases/pr1701301",
        "source_type": "government",
        "year": 2017,
    },
    {
        "id": 383,
        "title": "CNN Money — 'Deutsche Bank fined $630 million for Russian money laundering' (January 31, 2017, clients bought stocks in Moscow in rubles, sold identical stocks through London in dollars)",
        "url": "https://money.cnn.com/2017/01/31/investing/deutsche-bank-us-fine-russia-money-laundering/index.html",
        "source_type": "journalism",
        "year": 2017,
    },
    {
        "id": 384,
        "title": "CNBC — 'Ex-Deutsche banker William Broeksmit left notes before killing himself' (January 26, 2014, found hanging at Kensington home, London. Head of risk and capital optimization. Left several notes.)",
        "url": "https://www.cnbc.com/2014/03/25/ex-deutsche-banker-left-notes-before-killing-himself-london-inquest.html",
        "source_type": "journalism",
        "year": 2014,
    },
    {
        "id": 385,
        "title": "ProPublica — 'Trump, Inc.' investigation: Deutsche Bank and Trump relationship (DB loaned ~$2.5 billion over two decades, Trump was 'completely frozen out of the financial system')",
        "url": "https://www.propublica.org/article/trump-inc-podcast-deutsche-bank-donald-trump",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 386,
        "title": "CNBC — 'Deutsche Bank reportedly loaned $2 billion to Donald Trump over two decades' (March 2019, started lending late 1990s when Trump couldn't get loans elsewhere)",
        "url": "https://www.cnbc.com/2019/03/19/deutsche-bank-loaned-2-billion-to-donald-trump-over-two-decades-nyt.html",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 387,
        "title": "Anadolu Agency — 'Former German Chancellor Scholz's ex-secretary named in Epstein documents' (Philippa Sigl-Glockner, private secretary May 2019-Nov 2020, passed information about African telecommunications to Epstein, described as former German intelligence)",
        "url": "https://www.aa.com.tr/en/europe/former-german-chancellor-scholz-s-ex-secretary-named-in-epstein-documents/3836728",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 388,
        "title": "WION — 'Epstein files: Philippa Sigl-Glöckner, Olaf Scholz, DOJ release' (described in redacted message as having 'completed master's in computer science, joined super-elite German intelligence service, assigned to ministry of finance to track money flows')",
        "url": "https://www.wionews.com/world/epstein-files-philippa-sigl-gloeckner-olaf-scholz-doj-release-1771763806746",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 389,
        "title": "CIA FOIA / National Archives — 'Forging an Intelligence Partnership: CIA and the Origins of the BND, 1945-49' (declassified two-volume CIA history of Gehlen Organization → BND creation)",
        "url": "https://www.archives.gov/iwg/declassified-records/rg-263-cia-records/rg-263-report.html",
        "source_type": "foia",
        "year": 1999,
    },
    {
        "id": 390,
        "title": "Oxford Academic — 'West German-Israeli Intelligence and Military Cooperation, 1957-1982' (BND-Mossad contacts from 1957, formalized cooperation through Cold War era)",
        "url": "https://academic.oup.com/book/1547/chapter/141013021",
        "source_type": "academic",
        "year": 2017,
    },
    {
        "id": 391,
        "title": "Bloomberg — 'Trump Family Banker Forced to Leave Deutsche Bank Over Deal' (Rosemary Vrablic resigned December 2020, purchased $1.5M apartment from Kushner entity while he was her client)",
        "url": "https://www.bloomberg.com/news/articles/2021-02-03/trump-family-banker-forced-to-leave-deutsche-bank-over-deal",
        "source_type": "journalism",
        "year": 2021,
    },
    {
        "id": 392,
        "title": "NPR — 'Epstein fallout spreads across Europe' (February 2026, European investigations triggered by DOJ file release, Norwegian diplomat Mona Juul resigned)",
        "url": "https://www.npr.org/2026/02/14/nx-s1-5714609/epstein-europe-fallout",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 393,
        "title": "Anadolu Agency — 'German opposition demands government probe into Epstein files' (Green Party deputy Konstantin von Notz demands evaluation, SPD Sebastian Fiedler cites intelligence concerns)",
        "url": "https://www.aa.com.tr/en/europe/german-opposition-demands-government-probe-into-epstein-files/3826096",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 394,
        "title": "USVI v. JPMorgan Chase — JPMorgan due diligence report: MC2 Model Management received $1 million from Epstein in 2005 (Exhibit 101, S.D.N.Y., 2022). JPMorgan dropped Epstein 2013; Deutsche Bank onboarded him same year.",
        "url": "https://storage.courtlistener.com/recap/gov.uscourts.nysd.591706/gov.uscourts.nysd.591706.240.1.pdf",
        "source_type": "court",
        "year": 2022,
    },
    {
        "id": 395,
        "title": "Jacobin — 'FBI, Epstein, Kushner, Whistleblower Silenced' (Tammy McFadden reported to FBI about Epstein transactions, flagged 102 politically exposed persons whose review was 'deferred indefinitely')",
        "url": "https://jacobin.com/2026/02/fbi-epstein-kuchner-whistleblower-silenced",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 396,
        "title": "Daily Beast — 'Deutsche Bank Late Executive's Whistleblower Son Gave Trump-Russia Documents to FBI, Congress' (Val Broeksmit discovered thousands of confidential DB documents in father's email, handed to FBI and Congress)",
        "url": "https://www.thedailybeast.com/deutsche-bank-late-executives-whistleblower-son-gave-trump-russia-documents-to-fbi-congress-report-says/",
        "source_type": "journalism",
        "year": 2022,
    },
]


# ============================================================
# ENTITIES — 9 new (6 people + 1 agency + 2 events)
# ============================================================

ENTITIES = [
    # --- PEOPLE: Deutsche Bank Personnel ---
    {
        "name": "Thomas Bowers",
        "entity_type": "person",
        "description": (
            "Head of Deutsche Bank's American wealth-management division. Critical node "
            "connecting Deutsche Bank to both Jeffrey Epstein and Donald Trump — signed off "
            "on high-risk accounts and loans for both.\n\n"
            "When Bowers left Citibank for Deutsche Bank, Epstein reportedly followed. He "
            "approved new high-risk loans and credit lines. He also oversaw the private "
            "wealth division that loaned Trump approximately $2.5 billion over two decades "
            "when Trump was 'completely frozen out of the financial system' — no other major "
            "bank would lend to him.\n\n"
            "Died November 19, 2019 — found hanging at his beachfront home in Malibu, "
            "California. LA County medical examiner ruled suicide. He was 55. Federal "
            "investigators were reportedly seeking to interview him at the time of his death "
            "about documents related to Deutsche Bank."
        ),
        "metadata": {},
    },
    {
        "name": "Rosemary Vrablic",
        "entity_type": "person",
        "description": (
            "Managing Director and Senior Private Banker at Deutsche Bank's U.S. Private "
            "Wealth Management division. She was Donald Trump's personal banker at Deutsche "
            "Bank — worked in the same wealth management division that handled both "
            "Trump/Kushner and Epstein accounts.\n\n"
            "Resigned from Deutsche Bank in December 2020 amid an internal investigation. "
            "Revealed in February 2021 that DB forced her out over a conflict of interest: "
            "she purchased a $1.5 million apartment in 2013 from Bergel 715 Associates, an "
            "entity in which Jared Kushner held an ownership stake, while Kushner was her "
            "client. She also formed an 'unapproved outside entity' to hold the investment."
        ),
        "metadata": {},
    },
    {
        "name": "Tammy McFadden",
        "entity_type": "person",
        "description": (
            "Anti-money laundering compliance officer at Deutsche Bank, based in Jacksonville, "
            "Florida. The whistleblower who tried to stop Deutsche Bank's Epstein relationship.\n\n"
            "In 2015, McFadden raised concerns about Epstein's transactions — telling "
            "investigators it appeared Epstein was sending wires to young women and to a "
            "French art gallery owner. Her entire Jacksonville compliance team wanted to "
            "terminate the Epstein relationship. She also flagged 102 'politically exposed "
            "persons' designated as high-risk individuals whose review had been 'deferred "
            "indefinitely.'\n\n"
            "McFadden claims she was moved to an adjacent team shortly after raising concerns, "
            "then laid off in 2018 — characterizing it as retaliation. She reported her "
            "experience to the FBI."
        ),
        "metadata": {},
    },
    {
        "name": "William Broeksmit",
        "entity_type": "person",
        "description": (
            "Senior Deutsche Bank executive — head of risk and capital optimization. American "
            "national who joined DB from Merrill Lynch in the 1990s alongside future co-CEO "
            "Anshu Jain.\n\n"
            "In 2012, BaFin (German financial regulator) blocked his appointment to the "
            "management board as head of risk management. He retired from DB in February 2013 "
            "and was reported to be 'very anxious' about authorities investigating areas "
            "where he had worked.\n\n"
            "Died January 26, 2014 — found hanging at his Kensington home in London. London "
            "inquest ruled suicide. He was 58. Left several notes for family and friends.\n\n"
            "After his death, his adopted son Val Broeksmit discovered thousands of "
            "confidential Deutsche Bank documents in his email account — board meeting minutes, "
            "spreadsheets, financial plans — which became the basis for federal investigations "
            "into Deutsche Bank's ties to Trump and Russia."
        ),
        "metadata": {},
    },
    {
        "name": "Val Broeksmit",
        "entity_type": "person",
        "description": (
            "Deutsche Bank whistleblower and FBI informant. Adopted son of senior DB "
            "executive William Broeksmit.\n\n"
            "After his father's suicide in January 2014, discovered thousands of confidential "
            "Deutsche Bank documents in his father's email — board meeting minutes, "
            "spreadsheets, financial plans from DB Trust Company Americas. In 2019, introduced "
            "to Rep. Adam Schiff (House Intelligence Committee) by musician Moby. Subpoenaed "
            "by Congress. Became a cooperating FBI witness — the FBI gave him a 'special "
            "advisory title' and assisted his girlfriend in obtaining a U.S. visa.\n\n"
            "Handed over hundreds of documents to the FBI related to Deutsche Bank's ties to "
            "Trump, Russia, and other illegal activity.\n\n"
            "Died April 25, 2022 — found dead on the campus of Woodrow Wilson High School in "
            "El Sereno, Los Angeles. Appeared to have fallen from a tree, suffering "
            "blunt-force trauma, broken ribs, and spinal fracture. LAPD stated no foul play "
            "suspected. LA County coroner ruled the death accidental. He was 46.\n\n"
            "Newsweek reported (December 2023) that a Deutsche Bank article was found among "
            "Trump's classified documents at Mar-a-Lago."
        ),
        "metadata": {},
    },
    {
        "name": "Philippa Sigl-Glöckner",
        "entity_type": "person",
        "description": (
            "German economist and founder of think tank 'Dezernat Zukunft.' Served as "
            "private secretary to Chancellor Olaf Scholz from May 2019 to November 2020, "
            "during his tenure as Finance Minister.\n\n"
            "Named in the 2026 DOJ Epstein files release. Documents show she passed "
            "information about African telecommunications to Epstein. A redacted message in "
            "the files describes her background: 'completed her master's degree in computer "
            "science, joined the super-elite German intelligence service, and was assigned "
            "to the ministry of finance to track money flows.'\n\n"
            "German opposition politicians have demanded a government probe. Green Party "
            "deputy leader Konstantin von Notz demanded systematic evaluation of the files. "
            "SPD domestic policy spokesman Sebastian Fiedler cited concern about 'possible "
            "European intelligence dimensions.'"
        ),
        "aliases": "Philippa Sigl-Glockner",
        "metadata": {},
    },
    # --- AGENCY ---
    {
        "name": "BND",
        "entity_type": "agency",
        "description": (
            "Bundesnachrichtendienst — Germany's foreign intelligence service. Literally "
            "created by the CIA.\n\n"
            "History: The Gehlen Organization was established June 1946 by U.S. occupation "
            "authorities, headed by Reinhard Gehlen — former Wehrmacht Major General and head "
            "of Nazi military intelligence on the Eastern Front (Fremde Heere Ost). CIA "
            "assumed formal responsibility in July 1949, supplying funding, cars, and "
            "airplanes. On April 1, 1956, the Gehlen Organization was formally transferred "
            "to the Federal Republic of Germany under Chancellor Adenauer, becoming the BND.\n\n"
            "1998: U.S. Congress passed the Nazi War Crimes Disclosure Act, declassifying "
            "thousands of CIA documents about the Gehlen/BND relationship. The CIA's own "
            "two-volume history 'Forging an Intelligence Partnership: CIA and the Origins of "
            "the BND, 1945-49' was released.\n\n"
            "BND-Mossad cooperation documented from 1957, beginning after the Suez War. "
            "Mossad used BND cooperation during Operation Wrath of God (post-Munich 1972). "
            "Germany has been a key mediator in Israel-Hezbollah prisoner exchanges since "
            "the 1990s. Recent 'Cyber Dome' initiative expands BND-Mossad cooperation."
        ),
        "aliases": "Bundesnachrichtendienst, Gehlen Organization",
        "metadata": {},
    },
    # --- EVENTS ---
    {
        "name": "DFS Deutsche Bank Consent Order (2020)",
        "entity_type": "event",
        "description": (
            "New York Department of Financial Services consent order against Deutsche Bank, "
            "issued July 7, 2020. Penalty: $150 million. First regulatory enforcement action "
            "against a financial institution for its Epstein dealings.\n\n"
            "Key findings from the consent order:\n"
            "- Deutsche Bank onboarded Epstein in August 2013 (after JPMorgan dropped him), "
            "maintaining over 40 accounts until December 2018.\n"
            "- Before onboarding, a junior relationship coordinator prepared a memo detailing "
            "Epstein's '17 out-of-court civil sex abuse settlements,' his plea deal, and "
            "prison sentence. Superiors decided to proceed anyway.\n"
            "- Paul Morris (relationship manager from JPMorgan) pitched Epstein as a "
            "$2-4M/year revenue client. Charles Packard (head of wealth management) approved.\n"
            "- Epstein's attorney withdrew more than $800,000 in cash, repeatedly asking how "
            "to avoid triggering reporting requirements, then structuring withdrawals below "
            "$10,000 across multiple days.\n"
            "- At least 18 wires of $10,000+ to named co-conspirators.\n"
            "- Payments to young women, Russian models, women with Eastern European surnames, "
            "hotel/rent expenses, school tuition.\n"
            "- Settlement payments exceeding $7 million and legal expenses over $6 million.\n"
            "- Reputational Risk Committee conditions were 'not transmitted' to the account team.\n\n"
            "In May 2023, Deutsche Bank separately agreed to pay $75 million to settle a "
            "civil lawsuit by Epstein victims (victims to receive $75K-$5M per claim). DB "
            "did not admit wrongdoing. Total Epstein-related penalties: $225 million."
        ),
        "metadata": {},
    },
    {
        "name": "Deutsche Bank Russian Mirror Trading",
        "entity_type": "event",
        "description": (
            "Deutsche Bank fined approximately $630 million for a 'mirror trading' scheme "
            "that laundered an estimated $10 billion out of Russia through DB's Moscow, "
            "London, and New York offices between 2011 and 2015.\n\n"
            "The scheme: clients bought stocks in Moscow in rubles; related parties then sold "
            "identical stocks through Deutsche Bank's London branch in dollars. DFS fined DB "
            "$425 million (January 30, 2017); UK FCA added £163 million (~$204 million).\n\n"
            "The DFS consent order found DB's AML/compliance units were 'ineffective and "
            "understaffed.' The Moscow branch's head of compliance was an attorney with no "
            "compliance background who simultaneously served as head of legal and AML officer.\n\n"
            "This occurred during the same era that Deutsche Bank onboarded Epstein (2013), "
            "continued lending to Trump (~$2.5 billion cumulative), and manipulated LIBOR "
            "($2.5 billion in fines, 2015). The same institution with the same compliance "
            "failures across multiple dimensions."
        ),
        "metadata": {},
    },
]


# ============================================================
# RELATIONSHIPS — ~18 new connections
# ============================================================

RELATIONSHIPS = [
    # =========================================
    # GROUP 1: DEUTSCHE BANK PERSONNEL (9)
    # =========================================
    {
        "source": "Thomas Bowers",
        "target": "Deutsche Bank",
        "type": "executive_at",
        "tier": "documented",
        "desc": "Head of Deutsche Bank's American wealth-management division. Oversaw the private wealth unit that managed both Epstein and Trump accounts.",
        "sources": [379, 385],
    },
    {
        "source": "Thomas Bowers",
        "target": "Jeffrey Epstein",
        "type": "facilitated",
        "tier": "credible",
        "desc": "Oversaw the wealth-management division that approved and maintained Epstein's 40+ accounts at Deutsche Bank. When Bowers left Citibank for DB, Epstein reportedly followed. Died November 2019 — federal investigators were seeking to interview him.",
        "sources": [379, 373],
        "year_start": 2013,
        "year_end": 2019,
    },
    {
        "source": "Thomas Bowers",
        "target": "Donald Trump",
        "type": "facilitated",
        "tier": "documented",
        "desc": "Signed off on high-risk loans to Trump through Deutsche Bank's private wealth division. DB loaned Trump approximately $2.5 billion over two decades when he was 'completely frozen out of the financial system.'",
        "sources": [379, 385, 386],
    },
    {
        "source": "Rosemary Vrablic",
        "target": "Deutsche Bank",
        "type": "executive_at",
        "tier": "documented",
        "desc": "Managing Director and Senior Private Banker in DB's U.S. Private Wealth Management division. Forced to resign December 2020 over conflict-of-interest: purchased apartment from Kushner entity while Kushner was her client.",
        "sources": [391],
    },
    {
        "source": "Rosemary Vrablic",
        "target": "Donald Trump",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Trump's personal banker at Deutsche Bank. Worked in the same private wealth division that handled both Trump/Kushner and Epstein accounts. Forced out over purchasing $1.5M apartment from Jared Kushner entity while he was her client.",
        "sources": [391, 385],
    },
    {
        "source": "Tammy McFadden",
        "target": "Deutsche Bank",
        "type": "worked_for",
        "tier": "documented",
        "desc": "AML compliance officer at Deutsche Bank's Jacksonville, FL office. Flagged Epstein transactions in 2015 — wires to young women, French art gallery. Her entire team wanted to terminate the Epstein relationship. Claims she was moved off the team and laid off in 2018 as retaliation.",
        "sources": [377, 395],
        "year_start": 2015,
        "year_end": 2018,
    },
    {
        "source": "William Broeksmit",
        "target": "Deutsche Bank",
        "type": "executive_at",
        "tier": "documented",
        "desc": "Head of risk and capital optimization. Joined from Merrill Lynch in the 1990s. BaFin blocked his appointment to management board in 2012. Retired February 2013. Found dead January 26, 2014 — suicide by hanging at his Kensington home, London. Left several notes.",
        "sources": [384],
    },
    {
        "source": "Val Broeksmit",
        "target": "William Broeksmit",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Adopted son. After William's death in January 2014, Val discovered thousands of confidential Deutsche Bank documents in his father's email — board minutes, spreadsheets, financial plans that became the basis for federal investigations.",
        "sources": [380, 384, 396],
        "year_start": 2014,
    },
    {
        "source": "Val Broeksmit",
        "target": "Deutsche Bank",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Leaked thousands of confidential Deutsche Bank documents to the FBI and Congress — board meeting minutes, financial plans from DB Trust Company Americas. Subpoenaed by House Intelligence Committee. Became cooperating FBI witness. Found dead April 25, 2022.",
        "sources": [380, 396, 381],
        "year_start": 2019,
        "year_end": 2022,
    },

    # =========================================
    # GROUP 2: WHISTLEBLOWER → AGENCIES (2)
    # =========================================
    {
        "source": "Tammy McFadden",
        "target": "FBI",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Reported Deutsche Bank's Epstein compliance failures to the FBI after being laid off, characterizing her termination as retaliation for flagging suspicious transactions.",
        "sources": [377, 395],
    },
    {
        "source": "Val Broeksmit",
        "target": "FBI",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Cooperating FBI witness. Handed over hundreds of Deutsche Bank documents related to Trump, Russia, and other illegal activity. FBI gave him a 'special advisory title' and assisted his girlfriend in obtaining a U.S. visa.",
        "sources": [380, 396],
        "year_start": 2019,
        "year_end": 2022,
    },

    # =========================================
    # GROUP 3: DEUTSCHE BANK ACCOUNTABILITY (3)
    # =========================================
    {
        "source": "DFS Deutsche Bank Consent Order (2020)",
        "target": "Deutsche Bank",
        "type": "investigated",
        "tier": "documented",
        "desc": "NY DFS fined Deutsche Bank $150 million for compliance failures including the Epstein relationship. First regulatory enforcement action against a financial institution for Epstein dealings. Found DB maintained 40+ Epstein accounts despite knowing his criminal history.",
        "sources": [373, 374],
        "year_start": 2020,
    },
    {
        "source": "DFS Deutsche Bank Consent Order (2020)",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The consent order documented DB's Epstein relationship in detail: the memo listing 17 sex abuse settlements that was ignored, $800K in structured cash withdrawals, 18+ wires to co-conspirators, payments to young women and Russian models, $7M in settlements and $6M in legal fees flowing through accounts.",
        "sources": [373, 374],
    },
    {
        "source": "Deutsche Bank Russian Mirror Trading",
        "target": "Deutsche Bank",
        "type": "investigated",
        "tier": "documented",
        "desc": "$630 million in combined DFS + FCA fines for a mirror trading scheme that laundered approximately $10 billion out of Russia through DB's Moscow, London, and New York offices (2011-2015). Same institution, same compliance failures, same era as the Epstein relationship.",
        "sources": [382, 383],
        "year_start": 2017,
    },

    # =========================================
    # GROUP 4: INTELLIGENCE (3)
    # =========================================
    {
        "source": "BND",
        "target": "CIA",
        "type": "associated_with",
        "tier": "documented",
        "desc": "The BND was literally created by the CIA. The Gehlen Organization (1946, headed by former Nazi military intelligence chief Reinhard Gehlen) was CIA-funded and CIA-directed until April 1, 1956, when it was formally transferred to West Germany and became the BND. Declassified under the 1998 Nazi War Crimes Disclosure Act.",
        "sources": [389],
        "year_start": 1956,
    },
    {
        "source": "BND",
        "target": "Mossad",
        "type": "associated_with",
        "tier": "documented",
        "desc": "BND-Mossad intelligence cooperation documented from 1957, beginning after the Suez War. Formalized through Cold War era. Mossad used BND cooperation during Operation Wrath of God (post-Munich 1972). Recent 'Cyber Dome' initiative expands cooperation.",
        "sources": [390],
        "year_start": 1957,
    },
    {
        "source": "Philippa Sigl-Glöckner",
        "target": "BND",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Described in a redacted Epstein file as having 'joined the super-elite German intelligence service.' Whether this refers to the BND specifically or another German intelligence body is not confirmed, but the BND is Germany's foreign intelligence service and the most likely candidate given her described role 'tracking money flows.'",
        "sources": [387, 388],
    },

    # =========================================
    # GROUP 5: CROSS-CONNECTIONS (3)
    # =========================================
    {
        "source": "Philippa Sigl-Glöckner",
        "target": "Jeffrey Epstein",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Named in the January 2026 DOJ Epstein files release. Documents show she passed information about African telecommunications to Epstein. German opposition demands government investigation into what German intelligence knew about Epstein's networks.",
        "sources": [387, 388, 393],
    },
    {
        "source": "Deutsche Bank",
        "target": "JPMorgan Chase",
        "type": "associated_with",
        "tier": "documented",
        "desc": "JPMorgan dropped Epstein as a client in 2013. Deutsche Bank onboarded him the same year — relationship manager Paul Morris had just moved from JPMorgan to DB and brought Epstein with him. Both banks eventually paid massive penalties (JPMorgan: $290M to victims; DB: $225M combined).",
        "sources": [373, 394],
        "year_start": 2013,
    },
    {
        "source": "Deutsche Bank",
        "target": "Donald Trump",
        "type": "financed",
        "tier": "documented",
        "desc": "Loaned Trump approximately $2.5 billion over two decades, starting in the late 1990s when he was 'completely frozen out of the financial system.' Trump defaulted on a $640M loan; DB's commercial unit refused further lending, but the private wealth unit then loaned him $48M. By the time DB cut ties (January 2021, after January 6th), Trump still owed approximately $340 million.",
        "sources": [385, 386],
        "year_start": 1998,
        "year_end": 2021,
    },
]


# ============================================================
# ENTITY-SOURCE LINKS — which sources document each entity
# ============================================================

ENTITY_SOURCES = {
    "Thomas Bowers": [379, 373, 385],
    "Rosemary Vrablic": [391, 385],
    "Tammy McFadden": [377, 395, 373],
    "William Broeksmit": [384, 396],
    "Val Broeksmit": [380, 381, 396],
    "Philippa Sigl-Glöckner": [387, 388, 393],
    "BND": [389, 390],
    "DFS Deutsche Bank Consent Order (2020)": [373, 374, 375, 376],
    "Deutsche Bank Russian Mirror Trading": [382, 383],
}
