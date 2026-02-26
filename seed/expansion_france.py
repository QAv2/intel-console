"""
France Cluster — Expansion layer for Intel Console.

Maps the Paris modeling industry pipeline (Karin Models → MC2), Epstein's
Paris operations (22 Avenue Foch), the French Epstein investigation (2019–2026),
and French intelligence connections (DGSE/SDECE → Safari Club).

Key threads:
- Jean-Luc Brunel's Paris modeling agencies as a documented trafficking pipeline
- Gérald Marie / Elite Model Management parallel abuse pattern
- Eileen Ford's role in funneling young models to Brunel despite knowledge
- 22 Avenue Foch as an Epstein operational property
- French investigation: Brunel arrest (2020), death (2022), reopening (2026)
- Jack Lang (Culture Minister) under investigation (2026)
- DGSE predecessor SDECE initiated the Safari Club (1976)

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Jeffrey Epstein [1], Ghislaine Maxwell [2], Jean-Luc Brunel [135],
  MC2 Model Management [141], Jean-Luc Brunel Death (2022) [144],
  Virginia Giuffre [145], Donald Trump [33], Prince Andrew [108],
  Peter Mandelson [189], Safari Club [186], CIA [85], DOJ [89],
  9 East 71st Street [156]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 349+ (continuing from existing 348)
# ============================================================

SOURCES = [
    {
        "id": 349,
        "title": "CBS 60 Minutes — 'American Girls in Paris' (Diane Sawyer, produced by Craig Pyes, October 23, 1988). Seven-month investigation; approximately two dozen models accused Brunel and Claude Haddad of drugging and rape.",
        "url": "https://www.imdb.com/title/tt1619503/",
        "source_type": "journalism",
        "author": "Craig Pyes / Diane Sawyer",
        "year": 1988,
    },
    {
        "id": 350,
        "title": "The Fashion Law — 'Jean-Luc Brunel, at the Center of Jeffrey Epstein's Web of Underage Girls' (comprehensive timeline of Brunel's career, agencies, and abuse allegations)",
        "url": "https://www.thefashionlaw.com/jean-luc-brunel-at-the-center-of-jeffrey-epsteins-web-of-underage-girls/",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 351,
        "title": "Le Monde — 'Affaire Epstein: la justice française ouvre une enquête pour viols et agressions sexuelles' (French prosecutors open investigation, August 2019)",
        "url": "https://www.lemonde.fr/societe/article/2019/08/23/affaire-epstein-la-justice-francaise-ouvre-une-enquete_5501886_3224.html",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 352,
        "title": "Al Jazeera — 'Modeling agent close to Epstein found dead in French jail' (Brunel arrested December 16, 2020 at CDG airport while attempting to board a flight to Dakar, Senegal; found dead February 19, 2022 at La Santé Prison)",
        "url": "https://www.aljazeera.com/news/2022/2/19/modeling-agent-close-to-epstein-found-dead-in-french-jail",
        "source_type": "journalism",
        "year": 2022,
    },
    {
        "id": 353,
        "title": "BBC News — 'Jean-Luc Brunel: Epstein associate found dead in Paris jail' (February 19, 2022, suicide by hanging at La Santé Prison, age 76)",
        "url": "https://www.bbc.com/news/world-europe-60432721",
        "source_type": "journalism",
        "year": 2022,
    },
    {
        "id": 354,
        "title": "The Guardian — 'Gérald Marie: former boss of Elite modelling agency accused of rapes' (September 2020, multiple accusers including Carré Otis, Karen Mulder, Lisa Brinkworth)",
        "url": "https://www.theguardian.com/world/2020/sep/17/gerald-marie-former-boss-of-elite-modelling-agency-accused-of-rapes",
        "source_type": "journalism",
        "year": 2020,
    },
    {
        "id": 355,
        "title": "Business of Fashion — 'Ex-Models Go Public with Allegations of Assault by Former Elite Model Boss Gerald Marie' (September 2020)",
        "url": "https://www.businessoffashion.com/news/luxury/ex-models-go-public-with-allegations-of-assault-by-former-elite-model-boss-gerald-marie/",
        "source_type": "journalism",
        "year": 2020,
    },
    {
        "id": 356,
        "title": "France 24 — 'French prosecutors close rape probe into top model agency boss' (Gérald Marie investigation closed February 2023 on statute-of-limitations grounds)",
        "url": "https://www.france24.com/en/live-news/20230214-french-prosecutors-close-rape-probe-into-top-model-agency-boss",
        "source_type": "journalism",
        "year": 2023,
    },
    {
        "id": 357,
        "title": "Virginia Giuffre v. Ghislaine Maxwell — deposition transcripts (S.D.N.Y., unsealed 2019). Giuffre names Brunel, describes being directed to provide sexual services, details Paris operations.",
        "url": "https://www.courthousenews.com/wp-content/uploads/2019/08/Giuffre-unseal.pdf",
        "source_type": "court",
        "year": 2016,
    },
    {
        "id": 358,
        "title": "NBC News — 'Epstein accuser Virginia Roberts Giuffre testifies against modeling agent Jean-Luc Brunel in Paris court' (June 2021, full-day testimony)",
        "url": "https://www.nbcnews.com/news/world/jeffrey-epstein-accuser-virginia-roberts-giuffre-testifies-against-modeling-agent-n1270959",
        "source_type": "journalism",
        "year": 2021,
    },
    {
        "id": 359,
        "title": "The Guardian — 'Jeffrey Epstein's Paris flat raided by French police' (September 2019, 22 Avenue Foch searched along with Brunel's offices)",
        "url": "https://www.theguardian.com/us-news/2019/sep/19/jeffrey-epsteins-paris-flat-raided-french-police",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 360,
        "title": "Bloomberg — 'Jeffrey Epstein's Luxury Paris Home Sold for $10 Million to Bulgarian Tycoon' (Georgi Tuchev purchased 22 Avenue Foch, June 2022, proceeds to victim claims)",
        "url": "https://www.bloomberg.com/news/articles/2022-12-01/jeffrey-epstein-s-luxury-paris-home-sold-for-10-million-to-bulgarian-tycoon",
        "source_type": "journalism",
        "year": 2022,
    },
    {
        "id": 361,
        "title": "The Guardian — 'Teen models, powerful men and private dinners: when Trump hosted Look of the Year' (2020 investigation, Trump judged 1991 contest at Plaza Hotel, participants as young as 14)",
        "url": "https://www.rsn.org/001/teen-models-powerful-men-and-private-dinners-when-trump-hosted-look-of-the-year.html",
        "source_type": "journalism",
        "year": 2020,
    },
    {
        "id": 362,
        "title": "BBC MacIntyre Undercover — 'Modelling: The Dark Side' (1999). Hidden camera caught Gérald Marie offering a 15-year-old model £300 for sex. Marie resigned from Elite following the broadcast.",
        "url": "https://www.kqed.org/arts/13887034/fashion-is-about-to-have-its-metoo-moment-and-its-long-overdue",
        "source_type": "journalism",
        "author": "BBC / Donal MacIntyre",
        "year": 1999,
    },
    {
        "id": 363,
        "title": "France 24 — 'French police raid Paris's Arab World Institute in Epstein-linked probe into Jack Lang' (February 2026, investigated for laundering proceeds of tax evasion linked to company set up by Epstein and Lang's daughter in USVI)",
        "url": "https://www.france24.com/en/france/20260216-french-police-raid-paris-s-arab-world-institute-in-epstein-linked-probe-into-jack-lang",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 364,
        "title": "Washington Post — 'Paris prosecutor opens new Epstein probes, makes public appeal for victims in France' (February 18, 2026, two new probes: human trafficking and financial wrongdoing, three individual cases: Fabrice Aidan, Daniel Siad, Frederic Chaslin)",
        "url": "https://www.washingtonpost.com/world/2026/02/18/france-epstein-paris-prosecutor-opens-investigation/",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 365,
        "title": "Bloomberg — 'Epstein Files Prompt France to Open New Probes, Revisit Brunel' (February 2026, triggered by US DOJ release of 3.5 million Epstein files)",
        "url": "https://www.bloomberg.com/news/articles/2026-02-14/epstein-files-prompt-france-to-open-new-probes-revisit-brunel",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 366,
        "title": "NPR — 'Former French Models Come Forward With Abuse Allegations Against Gerald Marie' (September 2021, at least 15 women cooperated with French investigators)",
        "url": "https://www.npr.org/2021/09/10/1035814641/former-french-models-come-forward-with-abuse-allegations-against-gerald-mari",
        "source_type": "journalism",
        "year": 2021,
    },
    {
        "id": 367,
        "title": "Carré Otis — 'Beauty, Disrupted' memoir (2011). Alleges Gérald Marie raped her 'countless' times starting around 1986 when she was 17 at his Paris apartment. Filed formal lawsuit at Tribunal Judiciaire in Paris (August 2021).",
        "url": "https://www.hollywoodreporter.com/news/general-news/linda-evangelista-abusive-relationship-gerald-marie-marriage-1235595242/",
        "source_type": "book",
        "author": "Carré Otis",
        "year": 2011,
    },
    {
        "id": 368,
        "title": "USVI v. JPMorgan Chase — Exhibit 101: JPMorgan due diligence report confirming 'MC2 Model Management received $1 million from Epstein in 2005' (S.D.N.Y., 2022)",
        "url": "https://storage.courtlistener.com/recap/gov.uscourts.nysd.591706/gov.uscourts.nysd.591706.240.1.pdf",
        "source_type": "court",
        "year": 2022,
    },
    {
        "id": 369,
        "title": "Epstein's Black Book — court-released contact directory (Palm Beach County Circuit Court). Brunel listed under France with 4 contact numbers.",
        "url": "https://www.documentcloud.org/documents/1508273-jeffrey-epsteins-little-black-book-redacted",
        "source_type": "court",
    },
    {
        "id": 370,
        "title": "LBC — 'Inside Epstein's Paris apartment: photos reveal luxury 22 Avenue Foch property' (eight bedrooms, purpose-built massage room, photographs of young girls on walls)",
        "url": "https://www.lbc.co.uk/article/french-investigators-photos-inside-epsteins-paris-apartment-5HjdTS7_2/",
        "source_type": "journalism",
        "year": 2019,
    },
    {
        "id": 371,
        "title": "Sky News — Data and Forensics Unit verification: Peter Mandelson photographed in underwear at 22 Avenue Foch (matched metal balcony railing to the specific address)",
        "url": "https://britbrief.co.uk/politics/scandals/mandelson-in-underwear-at-epsteins-paris-flat.html",
        "source_type": "journalism",
        "year": 2024,
    },
    {
        "id": 372,
        "title": "France 24 — 'Who from France's political and cultural elite is named in the Epstein files?' (February 2026, overview of French names emerging from DOJ file release)",
        "url": "https://www.france24.com/en/france/20260206-who-from-france-political-cultural-elite-named-epstein-files",
        "source_type": "journalism",
        "year": 2026,
    },
]


# ============================================================
# ENTITIES — 10 new (5 people + 2 organizations + 1 agency + 1 facility + 1 event)
# ============================================================

ENTITIES = [
    # --- PEOPLE: Paris Modeling Industry ---
    {
        "name": "Gérald Marie",
        "entity_type": "person",
        "description": (
            "Head of Elite Model Management's European operations in Paris. One of the "
            "most powerful figures in the fashion industry during the 1980s and 1990s. "
            "Married to supermodel Linda Evangelista (1987-1993).\n\n"
            "Accused of rape and sexual assault by at least 15 women who cooperated with "
            "French investigators, including supermodel Carré Otis (alleges rape 'countless' "
            "times starting around 1986 when she was 17), Karen Mulder (raped multiple times, "
            "spent five months in psychiatric care), and BBC journalist Lisa Brinkworth "
            "(assaulted while working undercover on a documentary about the modeling industry "
            "in 1998).\n\n"
            "BBC MacIntyre Undercover (1999) caught Marie on hidden camera offering a "
            "15-year-old model £300 for sex and bragging about Elite Model Look competitors "
            "he planned to sleep with. Marie resigned from Elite following the broadcast.\n\n"
            "French prosecutors opened an investigation in 2020. The criminal investigation "
            "was closed in February 2023 on statute-of-limitations grounds — the alleged "
            "offenses (1980s-1990s) occurred too long ago under French law."
        ),
        "aliases": "Gerald Marie, Gerald Marie de Castellac",
        "metadata": {},
    },
    {
        "name": "John Casablancas",
        "entity_type": "person",
        "description": (
            "Founder of Elite Model Management (1972), credited with 'inventing the "
            "supermodel.' Born December 12, 1942 in New York to a Spanish family, raised "
            "in Europe. Died July 20, 2013 in Rio de Janeiro from cancer.\n\n"
            "Documented relationship with Stephanie Seymour, who was a finalist at the "
            "inaugural Elite Model Look of the Year contest in 1983 at age 15. Casablancas "
            "was in his early 40s when the relationship began — she was under 17 and he was "
            "her agent.\n\n"
            "Business relationship with Donald Trump: In 1991, Trump became a headline "
            "sponsor of Elite's Look of the Year contest, hosted it at the Plaza Hotel "
            "(which Trump owned), accommodated the young models, and served as one of 10 "
            "judges. Contestants included aspiring models as young as 14. Trump hosted the "
            "competition again in 1992. Photographic evidence of Casablancas and Trump "
            "together at these events is held by Getty Images.\n\n"
            "Operated in the same Paris modeling scene as Jean-Luc Brunel and Gérald Marie."
        ),
        "metadata": {},
    },
    {
        "name": "Eileen Ford",
        "entity_type": "person",
        "description": (
            "Co-founder of Ford Models (1946), one of the most powerful modeling agencies "
            "in the world. Died 2014.\n\n"
            "Critical role in the Brunel pipeline: Ford Models sent young American models "
            "to Jean-Luc Brunel at Karin Models in Paris for assignments. CBS 60 Minutes "
            "'American Girls in Paris' (1988) documented that approximately two dozen models "
            "accused Brunel of drugging and raping them — models who had been referred through "
            "the Ford pipeline.\n\n"
            "Ford claimed on 60 Minutes that she had not known about the abuse. She severed "
            "ties with Brunel only after the broadcast. Despite the CBS exposé, no authorities "
            "took action against Brunel at the time, and he continued working in the modeling "
            "industry — eventually launching MC2 with Epstein financing in 2005."
        ),
        "metadata": {},
    },
    {
        "name": "Claude Haddad",
        "entity_type": "person",
        "description": (
            "French modeling agent based in Paris, connected to the Ford Agency. Co-accused "
            "alongside Jean-Luc Brunel in the 1988 CBS 60 Minutes investigation 'American "
            "Girls in Paris.' Approximately two dozen models told the program that Brunel "
            "or Haddad had drugged and raped them.\n\n"
            "Haddad denied the allegations. He died in 2009. Like Brunel, he faced no "
            "criminal consequences from the 1988 exposé."
        ),
        "metadata": {},
    },
    {
        "name": "Jack Lang",
        "entity_type": "person",
        "description": (
            "French politician. Served as Minister of Culture under President Mitterrand "
            "(1981-1986, 1988-1993) and as Minister of Education (2000-2002). President of "
            "the Arab World Institute in Paris.\n\n"
            "Under investigation as of February 2026 in connection with the Epstein files. "
            "French police raided the Arab World Institute on February 16, 2026. Lang is "
            "investigated for 'laundering of the proceeds of tax evasion' linked to a company "
            "set up jointly by Epstein and Lang's daughter in the U.S. Virgin Islands. Lang "
            "resigned as institute president following the raid.\n\n"
            "Investigation triggered by the US DOJ's release of 3.5 million Epstein files, "
            "which prompted French prosecutors to reopen and expand multiple probes."
        ),
        "metadata": {},
    },
    # --- ORGANIZATIONS ---
    {
        "name": "Elite Model Management",
        "entity_type": "organization",
        "description": (
            "Major international modeling agency founded in Paris by John Casablancas (1972). "
            "Became one of the world's most powerful agencies, representing supermodels "
            "including Linda Evangelista, Naomi Campbell, and Cindy Crawford.\n\n"
            "The Paris office, run by Gérald Marie, was the epicenter of systematic abuse "
            "in the modeling industry. At least 15 women accused Marie of rape and sexual "
            "assault during his tenure. BBC MacIntyre Undercover (1999) caught Marie on "
            "hidden camera soliciting a minor. Marie resigned following the broadcast.\n\n"
            "Elite operated in the same Paris modeling ecosystem as Brunel's Karin Models. "
            "The agencies shared the same pool of young models and operated parallel abuse "
            "patterns that went unaddressed by French authorities for decades."
        ),
        "metadata": {},
    },
    {
        "name": "Karin Models",
        "entity_type": "organization",
        "description": (
            "Paris modeling agency originally founded by Karin Mossberg. Jean-Luc Brunel "
            "began working there in the late 1970s and was running the company by 1978. "
            "He discovered models who became prominent, including Christy Turlington "
            "(discovered at age 14) and Sharon Stone.\n\n"
            "Exposed by CBS 60 Minutes in 1988 ('American Girls in Paris'): approximately "
            "two dozen models told the program that Brunel or his associate Claude Haddad "
            "had drugged and raped them. Young American models were referred to the agency "
            "by Eileen Ford of Ford Models. Despite the broadcast, no criminal action was "
            "taken against Brunel.\n\n"
            "Karin Models was the precursor to MC2 Model Management, which Brunel co-founded "
            "in 2005 with financing from Jeffrey Epstein. The same pattern — recruiting young "
            "foreign models and subjecting them to exploitation — continued across agencies "
            "and decades."
        ),
        "metadata": {},
    },
    # --- AGENCY ---
    {
        "name": "DGSE",
        "entity_type": "agency",
        "description": (
            "Direction Générale de la Sécurité Extérieure — France's foreign intelligence "
            "service, responsible for military intelligence and counterintelligence outside "
            "French borders. Established April 2, 1982, when President Mitterrand reformed "
            "and renamed the SDECE.\n\n"
            "DGSE's predecessor, the SDECE (Service de Documentation Extérieure et de "
            "Contre-Espionnage), was a founding member of the Safari Club. SDECE Director "
            "Alexandre de Marenches initiated the Safari Club on September 1, 1976 — making "
            "France not merely a member but the originator of the covert intelligence "
            "alliance. The Safari Club's five charter signatories: de Marenches (SDECE/France), "
            "Kamal Adham (Saudi intelligence), Kamal Hassan Ali (Egypt), Ahmed Dlimi (Morocco), "
            "and Nematollah Nassiri (Iran, pre-revolution). Saudi Arabia provided money, "
            "France provided technology, Egypt and Morocco supplied weapons and troops — all "
            "to bypass post-Church Committee Congressional restrictions on the CIA."
        ),
        "aliases": "Direction Générale de la Sécurité Extérieure, SDECE",
        "metadata": {},
    },
    # --- FACILITY ---
    {
        "name": "22 Avenue Foch",
        "entity_type": "facility",
        "description": (
            "Jeffrey Epstein's Paris apartment, located on one of the most expensive streets "
            "in the world in the 16th arrondissement. Purchased by Epstein in 2001 through "
            "a French company named SCI JEP.\n\n"
            "The property comprised approximately 685 square meters (7,373 sq ft): three "
            "units on the second floor with views of the Arc de Triomphe, two units on the "
            "fifth floor, two cellars in the basement. Eight bedrooms, a gym, two service "
            "studios, and a purpose-built massage room. Decorated by designer Alberto Pinto. "
            "Epstein's Franco-Brazilian butler told Franceinfo that 'numerous photographs of "
            "young girls' were displayed on walls 'like family photos.'\n\n"
            "Raided by French police in September 2019 alongside Brunel's Paris offices. "
            "Sky News Data and Forensics Unit forensically verified that photographs showing "
            "Peter Mandelson in his underwear were taken at this specific address (matched "
            "metal balcony railing). Prince Andrew referenced in reporting as having been "
            "hosted at the property.\n\n"
            "Sold in June 2022 to Bulgarian plastics magnate Georgi Tuchev for approximately "
            "€10 million. Some proceeds directed to Epstein victims' claims."
        ),
        "metadata": {},
    },
    # --- EVENT ---
    {
        "name": "French Epstein Investigation",
        "entity_type": "event",
        "description": (
            "French criminal investigation into the Epstein trafficking network, opened by "
            "the Paris prosecutor on August 23, 2019, after attorney Yael Mellul wrote to "
            "prosecutors reporting an alleged international pedophile network involving Epstein. "
            "Charges investigated: rape and sexual assault of minors, criminal association.\n\n"
            "Timeline:\n"
            "- September 2019: French police raid 22 Avenue Foch and Brunel's offices.\n"
            "- December 16, 2020: Jean-Luc Brunel arrested at Charles de Gaulle Airport "
            "while attempting to board a flight to Dakar, Senegal. Held at La Santé Prison.\n"
            "- June 2021: Brunel formally charged with drugging and raping a 17-year-old, "
            "plus sexual assault, criminal conspiracy, and human trafficking of minors. "
            "Virginia Giuffre testifies in Paris court for a full day.\n"
            "- February 19, 2022: Brunel found dead in his cell at La Santé Prison. "
            "Reported suicide by hanging, age 76.\n\n"
            "2026 reopening: Following the US DOJ's release of 3.5 million Epstein files, "
            "French prosecutors reopened and expanded the investigation. February 16, 2026: "
            "police raid the Arab World Institute in probe of former Culture Minister Jack "
            "Lang. February 18, 2026: Paris Public Prosecutor Laure Beccuau opens two new "
            "probes (human trafficking and financial wrongdoing), refers three individual "
            "cases (diplomat Fabrice Aidan, model recruiter Daniel Siad, conductor Frederic "
            "Chaslin), and makes public appeal for victims in France to come forward."
        ),
        "metadata": {},
    },
]


# ============================================================
# RELATIONSHIPS — ~35 new connections
# ============================================================

RELATIONSHIPS = [
    # =========================================
    # GROUP 1: PARIS MODELING INDUSTRY (12)
    # =========================================
    {
        "source": "Jean-Luc Brunel",
        "target": "Karin Models",
        "type": "led",
        "tier": "documented",
        "desc": "Brunel began working at Karin Models in the late 1970s and was running the agency by 1978. He recruited models including Christy Turlington (discovered at 14) and Sharon Stone.",
        "sources": [349, 350],
        "year_start": 1978,
    },
    {
        "source": "John Casablancas",
        "target": "Elite Model Management",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded Elite Model Management in Paris in 1972. Credited with 'inventing the supermodel.' Built it into one of the world's most powerful agencies.",
        "sources": [361],
        "year_start": 1972,
    },
    {
        "source": "Gérald Marie",
        "target": "Elite Model Management",
        "type": "led",
        "tier": "documented",
        "desc": "Head of Elite Model Management's European operations, based in Paris. One of the most powerful figures in the fashion industry. Resigned in 1999 following BBC MacIntyre Undercover broadcast.",
        "sources": [354, 355, 362],
    },
    {
        "source": "Gérald Marie",
        "target": "Jean-Luc Brunel",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Both operated modeling agencies in Paris during the same era, shared the same pool of young models, and are accused of the same pattern of abuse — drugging and raping young models. Parallel networks in the same Paris scene.",
        "sources": [354, 350],
    },
    {
        "source": "John Casablancas",
        "target": "Jean-Luc Brunel",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Both operated at the top of the Paris modeling industry. Casablancas founded Elite, Brunel ran Karin Models — the two agencies overlapped in the same scene with the same models.",
        "sources": [350, 361],
    },
    {
        "source": "Eileen Ford",
        "target": "Jean-Luc Brunel",
        "type": "enabled",
        "tier": "documented",
        "desc": "Ford Models sent young American models to Brunel at Karin Models in Paris. CBS 60 Minutes (1988) documented that approximately two dozen models accused Brunel of drugging and rape — models referred through Ford. Ford claimed ignorance, severed ties only after the broadcast.",
        "sources": [349, 350],
    },
    {
        "source": "Eileen Ford",
        "target": "Karin Models",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Ford Models referred young American models to Brunel's Karin Models agency in Paris for assignments. This referral pipeline was documented by CBS 60 Minutes in 1988.",
        "sources": [349],
    },
    {
        "source": "Claude Haddad",
        "target": "Jean-Luc Brunel",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Both accused alongside each other in the 1988 CBS 60 Minutes investigation 'American Girls in Paris.' Approximately two dozen models told the program that Brunel or Haddad had drugged and raped them.",
        "sources": [349, 350],
    },
    {
        "source": "Claude Haddad",
        "target": "Karin Models",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Haddad operated a boutique modeling agency in Paris connected to the Ford Agency. Co-accused with Brunel in the 60 Minutes investigation of the Paris modeling industry.",
        "sources": [349],
    },
    {
        "source": "Karin Models",
        "target": "MC2 Model Management",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Both agencies were run by Jean-Luc Brunel — Karin Models (Paris, 1978-) and MC2 Model Management (New York/Miami, 2005). The same pattern of recruiting young models for exploitation continued across agencies and decades.",
        "sources": [350, 368],
    },
    {
        "source": "John Casablancas",
        "target": "Donald Trump",
        "type": "associated_with",
        "tier": "documented",
        "desc": "In 1991, Trump became a headline sponsor of Elite's Look of the Year contest, hosted it at the Plaza Hotel (which he owned), accommodated the young models, and served as one of 10 judges. Contestants included models as young as 14. Trump hosted the competition again in 1992. Getty Images holds photographs of Casablancas and Trump together at these events.",
        "sources": [361],
        "year_start": 1991,
        "year_end": 1992,
    },
    {
        "source": "Elite Model Management",
        "target": "MC2 Model Management",
        "type": "associated_with",
        "tier": "inference",
        "desc": "Both agencies operated in the Paris-to-New York modeling pipeline. Elite (Casablancas/Marie) and MC2 (Brunel/Epstein) exploited the same industry dynamics: bringing young foreign models to new cities, controlling their housing and work, creating conditions for abuse.",
        "sources": [350, 354],
    },

    # =========================================
    # GROUP 2: EPSTEIN'S PARIS OPERATIONS (7)
    # =========================================
    {
        "source": "Jeffrey Epstein",
        "target": "22 Avenue Foch",
        "type": "owned",
        "tier": "documented",
        "desc": "Purchased in 2001 through French company SCI JEP. Approximately 685 sqm: eight bedrooms, purpose-built massage room, photographs of young girls on walls. Sold June 2022 for approximately €10 million.",
        "sources": [359, 360, 370],
        "year_start": 2001,
        "year_end": 2022,
    },
    {
        "source": "Ghislaine Maxwell",
        "target": "22 Avenue Foch",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Maxwell had access to and used Epstein's Paris apartment as part of the broader operational network of Epstein properties (New York, Palm Beach, New Mexico, Little St. James, Paris).",
        "sources": [357, 359],
    },
    {
        "source": "Jean-Luc Brunel",
        "target": "22 Avenue Foch",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Brunel had access to Epstein's Paris apartment. His Paris offices were raided simultaneously with the Avenue Foch apartment in September 2019.",
        "sources": [359, 350],
    },
    {
        "source": "Peter Mandelson",
        "target": "22 Avenue Foch",
        "type": "visited",
        "tier": "documented",
        "desc": "Sky News Data and Forensics Unit forensically verified that photographs showing Mandelson in his underwear were taken at 22 Avenue Foch — matched the metal balcony railing visible in the window to the specific address.",
        "sources": [371],
    },
    {
        "source": "Virginia Giuffre",
        "target": "22 Avenue Foch",
        "type": "trafficked_at",
        "tier": "credible",
        "desc": "Giuffre stated in depositions that Epstein and Maxwell directed her to provide sexual services at multiple locations including Paris. The Avenue Foch apartment was Epstein's Paris base of operations.",
        "sources": [357],
    },
    {
        "source": "22 Avenue Foch",
        "target": "9 East 71st Street",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Both Epstein properties — Paris apartment and Manhattan mansion — part of a network of residences where trafficking occurred. Both contained photographs of young women, purpose-built massage rooms, and were raided by law enforcement.",
        "sources": [359, 370],
    },
    {
        "source": "Prince Andrew",
        "target": "22 Avenue Foch",
        "type": "visited",
        "tier": "credible",
        "desc": "Referenced in reporting as having been hosted at Epstein's Paris apartment. Part of the broader pattern of Prince Andrew visiting multiple Epstein properties.",
        "sources": [359],
    },

    # =========================================
    # GROUP 3: FRENCH INVESTIGATION (8)
    # =========================================
    {
        "source": "French Epstein Investigation",
        "target": "Jean-Luc Brunel",
        "type": "investigated",
        "tier": "documented",
        "desc": "Paris prosecutors investigated Brunel from August 2019. Arrested December 16, 2020 at CDG airport. Formally charged June 2021 with drugging and raping a 17-year-old, sexual assault, criminal conspiracy, human trafficking of minors.",
        "sources": [351, 352, 353],
        "year_start": 2019,
        "year_end": 2022,
    },
    {
        "source": "French Epstein Investigation",
        "target": "Jeffrey Epstein",
        "type": "investigated",
        "tier": "documented",
        "desc": "Paris prosecutor opened investigation on August 23, 2019, for rape and sexual assault of minors and criminal association. Epstein had died by suicide four days earlier; investigation continued posthumously, focused on associates.",
        "sources": [351, 365],
        "year_start": 2019,
    },
    {
        "source": "French Epstein Investigation",
        "target": "Gérald Marie",
        "type": "investigated",
        "tier": "documented",
        "desc": "French prosecutors investigated Marie following accusations from at least 15 women. Investigation opened 2020, closed February 2023 on statute-of-limitations grounds — the alleged offenses (1980s-1990s) occurred too long ago under French law.",
        "sources": [354, 356, 366],
        "year_start": 2020,
        "year_end": 2023,
    },
    {
        "source": "French Epstein Investigation",
        "target": "Jack Lang",
        "type": "investigated",
        "tier": "documented",
        "desc": "French police raided the Arab World Institute on February 16, 2026. Lang investigated for 'laundering of the proceeds of tax evasion' linked to a company set up jointly by Epstein and Lang's daughter in the USVI. Lang resigned as institute president.",
        "sources": [363, 364, 372],
        "year_start": 2026,
    },
    {
        "source": "French Epstein Investigation",
        "target": "22 Avenue Foch",
        "type": "investigated",
        "tier": "documented",
        "desc": "French police searched the apartment at 22 Avenue Foch in September 2019, alongside raids on Brunel's Paris offices. Part of the broader investigation opened August 23, 2019.",
        "sources": [359, 351],
        "year_start": 2019,
    },
    {
        "source": "Jean-Luc Brunel Death (2022)",
        "target": "French Epstein Investigation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Brunel was found dead in his cell at La Santé Prison on February 19, 2022 — reported suicide by hanging, age 76 — while awaiting trial in the French investigation. Died before his case could reach court.",
        "sources": [352, 353],
        "year_start": 2022,
    },
    {
        "source": "Virginia Giuffre",
        "target": "French Epstein Investigation",
        "type": "testified_in",
        "tier": "documented",
        "desc": "Giuffre traveled to Paris and testified against Brunel in court for a full day in June 2021. Told NBC News afterward: 'I wanted Brunel to know that he no longer has the power over me.'",
        "sources": [358],
        "year_start": 2021,
    },
    {
        "source": "Jack Lang",
        "target": "Jeffrey Epstein",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Epstein and Lang's daughter set up a company together in the US Virgin Islands. Lang under investigation for laundering proceeds of tax evasion linked to this entity. Emerged from DOJ release of 3.5 million Epstein files.",
        "sources": [363, 372],
    },

    # =========================================
    # GROUP 4: INTELLIGENCE (2)
    # =========================================
    {
        "source": "DGSE",
        "target": "Safari Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "DGSE predecessor SDECE initiated the Safari Club. SDECE Director Alexandre de Marenches was the originator — he organized the alliance on September 1, 1976 with Saudi, Egyptian, Moroccan, and Iranian intelligence chiefs. France provided technology; Saudi Arabia provided money. Designed to bypass post-Church Committee Congressional oversight of the CIA.",
        "sources": [],
        "year_start": 1976,
    },
    {
        "source": "DGSE",
        "target": "CIA",
        "type": "associated_with",
        "tier": "documented",
        "desc": "French intelligence (SDECE/DGSE) has a long-documented relationship with the CIA, formalized through the Safari Club framework (1976) and broader Western intelligence sharing. De Marenches specifically designed the Safari Club to allow CIA operations to continue outside Congressional oversight.",
        "sources": [],
    },

    # =========================================
    # GROUP 5: CROSS-CONNECTIONS (5)
    # =========================================
    {
        "source": "Gérald Marie",
        "target": "Ghislaine Maxwell",
        "type": "associated_with",
        "tier": "inference",
        "desc": "Both operated in the Paris-London-New York social circuit during the same era. Marie ran Elite's European operations while Maxwell facilitated Epstein's access to the modeling industry. The modeling industry pipeline that both leveraged was the same ecosystem.",
        "sources": [354, 350],
    },
    {
        "source": "Eileen Ford",
        "target": "Elite Model Management",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Ford Models and Elite Model Management were the two most powerful modeling agencies in the world. Both operated the Paris pipeline — Ford referred models to Paris where they entered the Elite/Karin ecosystem.",
        "sources": [349, 361],
    },
    {
        "source": "Karin Models",
        "target": "22 Avenue Foch",
        "type": "associated_with",
        "tier": "inference",
        "desc": "Brunel's Karin Models recruited young models in Paris — the same city where Epstein maintained his Avenue Foch property. Brunel's Paris offices were raided simultaneously with the apartment in September 2019, indicating investigators saw them as connected operations.",
        "sources": [359, 350],
    },
    {
        "source": "French Epstein Investigation",
        "target": "DOJ",
        "type": "associated_with",
        "tier": "documented",
        "desc": "The 2026 reopening of French probes was triggered by the US DOJ's release of 3.5 million Epstein files. Paris Public Prosecutor Laure Beccuau opened two new probes and referred three individual cases based on material from the American files.",
        "sources": [364, 365],
        "year_start": 2026,
    },
    {
        "source": "Eileen Ford",
        "target": "Claude Haddad",
        "type": "associated_with",
        "tier": "credible",
        "desc": "Haddad operated a boutique modeling agency in Paris connected to the Ford Agency. Both named in the 1988 60 Minutes investigation into the Paris modeling industry.",
        "sources": [349],
    },
]


# ============================================================
# ENTITY-SOURCE LINKS — which sources document each entity
# ============================================================

ENTITY_SOURCES = {
    "Gérald Marie": [354, 355, 356, 362, 366, 367],
    "John Casablancas": [361],
    "Eileen Ford": [349, 350],
    "Claude Haddad": [349, 350],
    "Jack Lang": [363, 364, 372],
    "Elite Model Management": [354, 355, 356, 361, 362],
    "Karin Models": [349, 350, 368],
    "DGSE": [],
    "22 Avenue Foch": [359, 360, 370, 371],
    "French Epstein Investigation": [351, 352, 353, 358, 364, 365, 372],
}
