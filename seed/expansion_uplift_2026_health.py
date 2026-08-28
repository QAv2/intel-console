"""
Health & Bio — August 2026 uplift expansion for Intel Console.

Brings the health branch up to date through August 2026. Two main layers:
1. 2025-2026 developments: RFK Jr. as HHS Secretary (confirmed Feb 13 2025),
   his appointees (Bhattacharya at NIH, Makary at FDA, Prasad at CBER),
   ACIP dismissals, CDC Director firing, measles outbreaks, US WHO withdrawal,
   Fauci preemptive pardon, EcoHealth debarment confirmation, Purdue settlement.
2. Historical wiring: connecting the newly-routed suppressed-medicine entities
   (Flexner→Carnegie→AMA, Fishbein→Hoxsey, Keys/Yudkin/Sugar Research Foundation,
   Gerson→AMA, Reich→FDA, Fritz ter Meer→IG Farben→Bayer, Hofmann→Sandoz→MKULTRA).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  FDA [478], CDC [479], NIH [480], WHO [481], USAMRIID [188], DTRA [189],
  Pfizer [486], Purdue Pharma [485], EcoHealth Alliance [484],
  Gain-of-Function Research [490], Monsanto [487], Bayer [421], Syngenta [420],
  Anthony Fauci [470], Peter Daszak [472], Bill Gates [471],
  Arthur Sackler [474], Richard Sackler [834],
  Abraham Flexner [827], Morris Fishbein [828], Ancel Keys [829],
  John Yudkin [830], Max Gerson [831], Harry Hoxsey [832],
  Wilhelm Reich [833], Cristin Kearns [835], AMA [903],
  Fritz ter Meer [871], Sandoz Labs [895],
  MKULTRA [94], CIA [85], Donald Trump [33], Robert F. Kennedy [552],
  Rockefeller Foundation [708], Andrew Carnegie [324],
  Roundup Cancer Litigation [428], Monsanto Papers [427],
  Royal Raymond Rife [477], Bill & Melinda Gates Foundation [482], GAVI [483]

ENTITIES FROM OTHER MODULES (referenced, not created here):
  Tulsi Gabbard, Elon Musk, Kash Patel [power/intelligence modules]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 2300–2399
# ============================================================

SOURCES = [
    # ---- RFK Jr. / HHS 2025-2026 ----
    {
        "id": 2300,
        "title": "Robert F. Kennedy Jr. — Wikipedia (career, HHS tenure, ACIP, measles, MAHA)",
        "url": "https://en.wikipedia.org/wiki/Robert_F._Kennedy_Jr.",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2301,
        "title": "Senate confirms RFK Jr. as HHS Secretary in 52-48 vote — AP News",
        "url": "https://apnews.com/article/rfk-kennedy-hhs-secretary-confirmation-senate",
        "source_type": "journalism",
        "author": "AP News",
        "year": 2025,
    },
    {
        "id": 2302,
        "title": "2025 United States measles outbreak — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/2025_United_States_measles_outbreak",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2303,
        "title": "United States Department of Health and Human Services — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/United_States_Department_of_Health_and_Human_Services",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2304,
        "title": "MAHA Commission report contains fictional citations — Washington Post",
        "url": "https://www.washingtonpost.com/health/2025/05/maha-commission-report-citations/",
        "source_type": "journalism",
        "author": "Washington Post",
        "year": 2025,
    },
    # ---- HHS appointees ----
    {
        "id": 2305,
        "title": "Jay Bhattacharya — Wikipedia (Stanford, Great Barrington Declaration, NIH Director)",
        "url": "https://en.wikipedia.org/wiki/Jay_Bhattacharya",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2306,
        "title": "Marty Makary — Wikipedia (Johns Hopkins, FDA Commissioner, resignation)",
        "url": "https://en.wikipedia.org/wiki/Marty_Makary",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2307,
        "title": "Vinay Prasad — Wikipedia (UCSF, CBER Director, COVID vaccine restrictions)",
        "url": "https://en.wikipedia.org/wiki/Vinay_Prasad",
        "source_type": "other",
        "year": 2026,
    },
    # ---- GoF / EcoHealth / Fauci ----
    {
        "id": 2308,
        "title": "Biden issues preemptive pardons for Fauci, Milley, Jan. 6 committee — Reuters",
        "url": "https://www.reuters.com/world/us/biden-issues-preemptive-pardons-2025-01-20/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2309,
        "title": "Wenstrup applauds EcoHealth Alliance debarment — House Oversight Committee",
        "url": "https://oversight.house.gov/release/wenstrup-applauds-ecohealth-alliance-debarment/",
        "source_type": "congressional",
        "year": 2024,
    },
    {
        "id": 2310,
        "title": "Executive Order: Withdrawal from the World Health Organization — White House",
        "url": "https://www.whitehouse.gov/presidential-actions/withdrawal-from-the-world-health-organization/",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 2311,
        "title": "House Select Subcommittee on the Coronavirus Pandemic — Final Report (Dec 2 2024)",
        "url": "https://oversight.house.gov/wp-content/uploads/2024/12/12.2.24-SSC-Final-Report_Complete.pdf",
        "source_type": "congressional",
        "year": 2024,
    },
    # ---- Purdue / Bayer / FDA actions ----
    {
        "id": 2312,
        "title": "Purdue Pharma reaches revised $6.5 billion Sackler settlement — Reuters",
        "url": "https://www.reuters.com/legal/purdue-pharma-reaches-revised-settlement-2024/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2024,
    },
    {
        "id": 2313,
        "title": "Supreme Court to hear Bayer Roundup preemption case — Reuters",
        "url": "https://www.reuters.com/legal/supreme-court-bayer-roundup-preemption/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2314,
        "title": "FDA revokes authorization for Red No. 3 in food and ingested drugs — FDA.gov",
        "url": "https://www.fda.gov/food/food-additives-petitions/red-no-3",
        "source_type": "government",
        "year": 2025,
    },
    # ---- Flexner Report / Carnegie / Rockefeller ----
    {
        "id": 2315,
        "title": "Flexner Report — Wikipedia (1910, Carnegie Foundation, medical school closures)",
        "url": "https://en.wikipedia.org/wiki/Flexner_Report",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 2316,
        "title": "Abraham Flexner — Medical Education in the United States and Canada (1910)",
        "url": "https://archive.org/details/medicaleducation00markup",
        "source_type": "book",
        "author": "Abraham Flexner",
        "year": 1910,
    },
    {
        "id": 2317,
        "title": "E. Richard Brown — Rockefeller Medicine Men: Medicine and Capitalism in America (1979)",
        "url": "https://archive.org/details/rockefellermedicine",
        "source_type": "book",
        "author": "E. Richard Brown",
        "year": 1979,
    },
    # ---- Fishbein / Hoxsey ----
    {
        "id": 2318,
        "title": "Harry Hoxsey — Wikipedia (alternative cancer treatment, Fishbein feud, FDA closure)",
        "url": "https://en.wikipedia.org/wiki/Harry_Hoxsey",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 2319,
        "title": "Kenny Ausubel — When Healing Becomes a Crime: The Amazing Story of the Hoxsey Cancer Clinics (2000)",
        "url": "https://archive.org/details/whenhealingbecom0000ausu",
        "source_type": "book",
        "author": "Kenny Ausubel",
        "year": 2000,
    },
    {
        "id": 2320,
        "title": "Hoxsey v. Fishbein — U.S. District Court, Northern District of Texas (1949 libel verdict)",
        "url": "https://en.wikipedia.org/wiki/Harry_Hoxsey#Legal_battles",
        "source_type": "court",
        "year": 1949,
    },
    # ---- Sugar / Keys / Yudkin / Kearns ----
    {
        "id": 2321,
        "title": "Cristin E. Kearns, Laura A. Schmidt, Stanton A. Glantz — Sugar Industry and Coronary Heart Disease Research: A Historical Analysis — JAMA Internal Medicine (2016)",
        "url": "https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2548255",
        "source_type": "academic",
        "author": "Cristin E. Kearns, Laura A. Schmidt, Stanton A. Glantz",
        "year": 2016,
    },
    {
        "id": 2322,
        "title": "John Yudkin — Pure, White and Deadly: How Sugar Is Killing Us (1972)",
        "url": "https://archive.org/details/purewhitedeadlyh0000yudk",
        "source_type": "book",
        "author": "John Yudkin",
        "year": 1972,
    },
    {
        "id": 2323,
        "title": "Sugar Association — Wikipedia (history as Sugar Research Foundation, industry lobbying)",
        "url": "https://en.wikipedia.org/wiki/Sugar_Association",
        "source_type": "other",
        "year": 2024,
    },
    # ---- Gerson / Senate ----
    {
        "id": 2324,
        "title": "Max Gerson — Wikipedia (Gerson therapy, 1946 Senate testimony, AMA opposition)",
        "url": "https://en.wikipedia.org/wiki/Max_Gerson",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 2325,
        "title": "S.J. Haught — Censured for Curing Cancer: The American Experience of Dr. Max Gerson (1991)",
        "url": "https://archive.org/details/censuredcuringcancer",
        "source_type": "book",
        "author": "S.J. Haught",
        "year": 1991,
    },
    # ---- Reich / FDA ----
    {
        "id": 2326,
        "title": "Wilhelm Reich — Wikipedia (orgone, FDA injunction 1954, book burning, death 1957)",
        "url": "https://en.wikipedia.org/wiki/Wilhelm_Reich",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 2327,
        "title": "United States v. Wilhelm Reich — Federal court injunction ordering destruction of orgone accumulators (1954)",
        "url": "https://en.wikipedia.org/wiki/Wilhelm_Reich#FDA_investigation_and_trial",
        "source_type": "court",
        "year": 1954,
    },
    # ---- IG Farben / Fritz ter Meer ----
    {
        "id": 2328,
        "title": "IG Farben — Wikipedia (formation, Nazi collaboration, Nuremberg trial, dissolution)",
        "url": "https://en.wikipedia.org/wiki/IG_Farben",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 2329,
        "title": "IG Farben Trial — Nuremberg Military Tribunals, Case VI (1947-1948)",
        "url": "https://en.wikipedia.org/wiki/IG_Farben_trial",
        "source_type": "court",
        "year": 1948,
    },
    {
        "id": 2330,
        "title": "Fritz ter Meer — Wikipedia (IG Farben, Nuremberg conviction, Bayer chairmanship)",
        "url": "https://en.wikipedia.org/wiki/Fritz_ter_Meer",
        "source_type": "other",
        "year": 2024,
    },
    # ---- Albert Hofmann / Sandoz / LSD ----
    {
        "id": 2331,
        "title": "Albert Hofmann — Wikipedia (LSD synthesis, Sandoz, Bicycle Day)",
        "url": "https://en.wikipedia.org/wiki/Albert_Hofmann",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 2332,
        "title": "Albert Hofmann — LSD: My Problem Child (1980)",
        "url": "https://archive.org/details/lsdmyproblemchild",
        "source_type": "book",
        "author": "Albert Hofmann",
        "year": 1980,
    },
    {
        "id": 2333,
        "title": "Martin A. Lee & Bruce Shlain — Acid Dreams: The Complete Social History of LSD (1985)",
        "url": "https://archive.org/details/aciddreamssocial00leex",
        "source_type": "book",
        "author": "Martin A. Lee & Bruce Shlain",
        "year": 1985,
    },
    # ---- Additional 2025-2026 ----
    {
        "id": 2334,
        "title": "Kennedy fires all 17 members of CDC vaccine advisory committee — NPR",
        "url": "https://www.npr.org/2025/06/kennedy-fires-acip-vaccine-committee",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2025,
    },
    {
        "id": 2335,
        "title": "CDC Director Susan Monarez ousted as Kennedy reshapes health agencies — STAT News",
        "url": "https://www.statnews.com/2025/08/cdc-director-monarez-ousted/",
        "source_type": "journalism",
        "author": "STAT News",
        "year": 2025,
    },
    {
        "id": 2336,
        "title": "FDA Commissioner Makary resigns over e-cigarette ban reversal — New York Times",
        "url": "https://www.nytimes.com/2026/05/13/health/makary-fda-resignation.html",
        "source_type": "journalism",
        "author": "New York Times",
        "year": 2026,
    },
    {
        "id": 2337,
        "title": "Georgia, North Dakota pass pesticide failure-to-warn shield laws — Reuters Legal",
        "url": "https://www.reuters.com/legal/state-pesticide-shield-laws-roundup/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2338,
        "title": "Harrington v. Purdue Pharma — Supreme Court ruling striking Sackler immunity (2024)",
        "url": "https://www.supremecourt.gov/opinions/23pdf/23-124_p86b.pdf",
        "source_type": "court",
        "year": 2024,
    },
]

# ============================================================
# ENTITIES — 10 new
# ============================================================

ENTITIES = [
    # ---- 2025-2026 principals ----
    {
        "name": "Robert F. Kennedy Jr.",
        "entity_type": "person",
        "description": (
            "American environmental lawyer, anti-vaccine activist, and politician. Son of "
            "Senator Robert F. Kennedy and nephew of President John F. Kennedy. Founded "
            "Children's Health Defense, a prominent anti-vaccine organization. Author of "
            "'The Real Anthony Fauci' (2021). Ran for the 2024 Democratic presidential "
            "nomination, then as an independent, before suspending his campaign and endorsing "
            "Donald Trump. Confirmed as Secretary of Health and Human Services on February 13, "
            "2025, by a 52-48 Senate vote (Mitch McConnell the sole Republican opposing). "
            "As HHS Secretary, dismissed all 17 Advisory Committee on Immunization Practices "
            "(ACIP) members in June 2025 and appointed replacements whose decisions a "
            "Massachusetts court reversed in March 2026. Ousted CDC Director Susan Monarez "
            "in August 2025, triggering senior official resignations. Oversaw the MAHA "
            "(Make America Healthy Again) Commission report (May 2025), which was found to "
            "contain fictional citations. During the 2025 measles outbreak (2,255 cases across "
            "44 states, three deaths in Texas), characterized vaccination as a 'personal choice' "
            "and promoted vitamin A supplements. Remains HHS Secretary as of August 2026."
        ),
        "aliases": "RFK Jr., Bobby Kennedy Jr., Robert Francis Kennedy Jr.",
        "metadata": {
            "nationality": "American",
            "born": "1954-01-17",
            "role": "HHS Secretary (2025-present)",
            "prior_role": "Environmental lawyer, Children's Health Defense founder",
        },
    },
    {
        "name": "HHS",
        "entity_type": "agency",
        "description": (
            "United States Department of Health and Human Services, the federal executive "
            "department responsible for protecting the health of all Americans and providing "
            "essential human services. Oversees the FDA, CDC, NIH, CMS, and BARDA, among "
            "other agencies. With a budget exceeding $1.7 trillion (primarily through Medicare "
            "and Medicaid), HHS is the largest department in the federal government by spending. "
            "In February 2025, Robert F. Kennedy Jr. was confirmed as HHS Secretary (52-48), "
            "bringing his vaccine-skeptic advocacy and Make America Healthy Again agenda to "
            "the department. Under Kennedy, HHS dismissed all 17 ACIP members (June 2025), "
            "ousted CDC Director Susan Monarez (August 2025), oversaw workforce reductions "
            "of approximately 20,000 positions (announced March 2025), and revised CDC "
            "guidance on vaccines and autism (November 2025). The department's leadership "
            "appointments — Jay Bhattacharya at NIH, Marty Makary at FDA, Vinay Prasad at "
            "CBER — represented a sharp departure from public health establishment consensus."
        ),
        "aliases": "Department of Health and Human Services, DHHS",
    },
    {
        "name": "Jay Bhattacharya",
        "entity_type": "person",
        "description": (
            "American physician, economist, and professor of health policy at Stanford "
            "University (born 1968). Co-author of the Great Barrington Declaration (October "
            "2020), which advocated focused protection of vulnerable populations while "
            "allowing COVID-19 to spread among lower-risk groups — a position that placed "
            "him in direct opposition to mainstream public health authorities. NIH leadership "
            "internally flagged his work; the Twitter Files revealed government pressure to "
            "suppress the Declaration. Confirmed as NIH Director by the Senate on March 25, "
            "2025 (53-47), assuming office April 1, 2025. Eliminated foreign researcher "
            "subcontracting at NIH (May 2025) and championed a gender dysphoria report. "
            "Appointed Acting CDC Director on February 18, 2026, while retaining the NIH "
            "directorship, consolidating control over both the nation's primary biomedical "
            "research institution and its leading public health agency."
        ),
        "aliases": "Jayanta Bhattacharya",
        "metadata": {
            "nationality": "American",
            "born": "1968",
            "role": "NIH Director (2025-present), Acting CDC Director (2026-present)",
            "prior_role": "Stanford professor, Great Barrington Declaration co-author",
        },
    },
    {
        "name": "Marty Makary",
        "entity_type": "person",
        "description": (
            "American surgeon, health policy researcher, and professor at Johns Hopkins "
            "University School of Medicine (born 1970). Author of books criticizing healthcare "
            "system transparency, including 'The Price We Pay' (2019). Became a prominent "
            "media voice during COVID-19, advocating for natural immunity recognition and "
            "criticizing extended school closures. Confirmed as FDA Commissioner by the Senate "
            "on March 25, 2025 (56-44), taking office April 1, 2025. Initiated food-dye "
            "phase-out programs and school meal improvement pilots. Resigned May 13, 2026, "
            "in protest over the Trump administration's decision to lift the e-cigarette "
            "ban — a rare instance of a Trump health appointee departing over a public health "
            "policy disagreement."
        ),
        "aliases": "Martin A. Makary",
        "metadata": {
            "nationality": "American",
            "born": "1970",
            "role": "FDA Commissioner (April 2025 - May 2026)",
            "prior_role": "Johns Hopkins surgeon and professor",
        },
    },
    {
        "name": "Vinay Prasad",
        "entity_type": "person",
        "description": (
            "American hematologist-oncologist and professor at the University of California, "
            "San Francisco (born 1983). Prolific critic of FDA regulatory practices and "
            "pharmaceutical industry influence on clinical trials. Appointed Director of "
            "the FDA's Center for Biologics Evaluation and Research (CBER) on May 6, 2025. "
            "Restricted COVID-19 vaccine eligibility to adults over 65 or high-risk "
            "individuals (May 2025). Issued a controversial November 2025 memo claiming "
            "ten children had died from COVID vaccination, which twelve former FDA "
            "commissioners publicly condemned. Rejected a Moderna mRNA influenza vaccine "
            "for review (February 2026). Briefly resigned in August 2025 after attacks "
            "from Laura Loomer but returned within two weeks. Departed CBER on April 30, "
            "2026. His tenure was the most turbulent in CBER's history."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "American",
            "born": "1983",
            "role": "CBER Director (May 2025 - April 2026)",
            "prior_role": "UCSF hematologist-oncologist and professor",
        },
    },
    # ---- Historical entities (newly wired) ----
    {
        "name": "IG Farben",
        "entity_type": "organization",
        "description": (
            "Interessen-Gemeinschaft Farbenindustrie AG, the massive German chemical and "
            "pharmaceutical conglomerate formed in 1925 through the merger of Bayer, BASF, "
            "Hoechst, and other companies. Became the largest corporation in Europe and the "
            "single largest corporate donor to the Nazi Party. Produced Zyklon B through "
            "subsidiary Degesch, the gas used in the Holocaust. Used slave labor from "
            "concentration camps, including a dedicated facility at Auschwitz III-Monowitz. "
            "At the IG Farben Trial (1947-1948, Nuremberg Military Tribunal Case VI), 24 "
            "executives were indicted; 13 convicted, including Fritz ter Meer (seven-year "
            "sentence, released 1950). Ordered dissolved by the Allies. Its constituent "
            "companies — Bayer, BASF, and Hoechst (later Aventis/Sanofi) — were re-established "
            "as independent entities and became some of the world's largest pharmaceutical "
            "and chemical corporations. Ter Meer became chairman of Bayer's supervisory board "
            "in 1956, six years after his release from Landsberg prison."
        ),
        "aliases": "I.G. Farbenindustrie AG, I.G. Farben",
    },
    {
        "name": "Albert Hofmann",
        "entity_type": "person",
        "description": (
            "Swiss chemist (1906-2008) who first synthesized lysergic acid diethylamide (LSD) "
            "at Sandoz Laboratories in Basel in 1938 and discovered its psychoactive properties "
            "on April 19, 1943 — a date known as 'Bicycle Day' after he rode home while "
            "experiencing the first intentional LSD trip. Sandoz marketed LSD as the "
            "psychiatric drug Delysid beginning in 1947. In the 1950s and 1960s, the CIA "
            "procured LSD from Sandoz for use in MKULTRA experiments on unwitting subjects, "
            "a weaponization Hofmann called deeply troubling. He also isolated psilocybin "
            "from Mexican mushrooms in 1958. Hofmann's discovery became one of the most "
            "consequential in 20th-century pharmacology, bridging legitimate psychiatric "
            "research, counterculture, and covert intelligence operations."
        ),
        "aliases": "Albert Hoffman",
        "metadata": {
            "nationality": "Swiss",
            "born": "1906-01-11",
            "died": "2008-04-29",
            "status": "deceased",
            "role": "Chemist, LSD synthesizer",
        },
    },
    {
        "name": "Sugar Research Foundation",
        "entity_type": "organization",
        "description": (
            "Industry trade group established in 1943 by major American sugar companies to "
            "promote sugar consumption and counter emerging research linking sugar to chronic "
            "disease. In 1967, the SRF paid Harvard researchers Mark Hegsted and Robert "
            "McGandy $6,500 (approximately $50,000 in 2016 dollars) to publish a literature "
            "review in the New England Journal of Medicine that minimized sugar's role in "
            "coronary heart disease while shifting blame to dietary fat — amplifying Ancel "
            "Keys's lipid hypothesis and undermining John Yudkin's sugar-centered research. "
            "This funding and its influence were concealed for nearly fifty years until "
            "dentist-turned-researcher Cristin Kearns uncovered the internal industry "
            "documents and published her findings in JAMA Internal Medicine in 2016. The "
            "SRF later became the Sugar Association. The episode is one of the clearest "
            "documented cases of industry-funded science shaping national dietary guidelines "
            "for decades."
        ),
        "aliases": "SRF, Sugar Association (successor)",
    },
    {
        "name": "Flexner Report",
        "entity_type": "publication",
        "description": (
            "Report on medical education in the United States and Canada, published in 1910 "
            "by educator Abraham Flexner under the auspices of the Carnegie Foundation for "
            "the Advancement of Teaching. Evaluated 155 medical schools and recommended "
            "closing those that did not meet its standards of laboratory-based scientific "
            "medicine. Implementation, funded largely by the Rockefeller Foundation's General "
            "Education Board, led to the closure of nearly half of all American medical "
            "schools by 1935 — including most schools serving Black students and women, "
            "and virtually all schools teaching homeopathic, eclectic, and naturopathic "
            "medicine. The report consolidated medical education under the AMA's Council "
            "on Medical Education and established the pharmaceutical-oriented model of "
            "medicine that remains dominant. While credited with raising standards, critics "
            "argue it systematically eliminated competing medical traditions and concentrated "
            "control of American healthcare under institutions aligned with Rockefeller and "
            "Carnegie interests."
        ),
        "aliases": "Flexner Report on Medical Education, Medical Education in the United States and Canada",
    },
    {
        "name": "2025 United States Measles Outbreak",
        "entity_type": "event",
        "description": (
            "Series of measles outbreaks across the United States beginning in early 2025, "
            "with the epicenter in west Texas. By August 2025, the outbreak had grown to "
            "2,255 confirmed cases across 44 states with nearly 50 separate clusters — the "
            "largest U.S. measles outbreak since 1994. In Texas alone, 762 cases were reported "
            "with 99 hospitalizations and three deaths, all among unvaccinated individuals. "
            "The outbreak occurred against the backdrop of declining childhood vaccination "
            "rates and new HHS leadership under Robert F. Kennedy Jr., who characterized "
            "vaccination as a 'personal choice' and promoted vitamin A and cod liver oil "
            "as alternatives on February 26. CDC communications director Kevin Griffis "
            "resigned in March 2025 over disagreements with the administration's messaging. "
            "Mexico experienced a concurrent outbreak of 3,872 cases with 13 deaths."
        ),
        "aliases": "2025 measles outbreak, Texas measles outbreak 2025",
    },
]

# ============================================================
# RELATIONSHIPS — 38 edges
# ============================================================

RELATIONSHIPS = [
    # ==== HISTORICAL WIRING: Flexner Report / AMA / Carnegie / Rockefeller ====
    {
        "source": "Abraham Flexner",
        "target": "Flexner Report",
        "type": "authored",
        "tier": "documented",
        "desc": (
            "Abraham Flexner wrote the Flexner Report (1910), a comprehensive evaluation "
            "of 155 medical schools in the United States and Canada, commissioned by the "
            "Carnegie Foundation for the Advancement of Teaching."
        ),
        "year_start": 1910,
        "year_end": 1910,
        "sources": [2315, 2316],
    },
    {
        "source": "Andrew Carnegie",
        "target": "Flexner Report",
        "type": "funded",
        "tier": "documented",
        "desc": (
            "The Carnegie Foundation for the Advancement of Teaching, endowed by Andrew "
            "Carnegie, commissioned and published the Flexner Report (1910). Carnegie's "
            "institutional support gave the report enormous authority."
        ),
        "year_start": 1910,
        "sources": [2315, 2316],
    },
    {
        "source": "Rockefeller Foundation",
        "target": "Flexner Report",
        "type": "funded",
        "tier": "documented",
        "desc": (
            "The Rockefeller Foundation's General Education Board provided the funding to "
            "implement the Flexner Report's recommendations, spending hundreds of millions "
            "of dollars reshaping American medical education around pharmaceutical-oriented, "
            "laboratory-based medicine. Flexner later joined the GEB."
        ),
        "year_start": 1910,
        "year_end": 1935,
        "sources": [2315, 2317],
    },
    {
        "source": "Flexner Report",
        "target": "American Medical Association",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The Flexner Report consolidated the AMA's control over medical education. "
            "Schools that did not meet AMA-aligned standards lost accreditation and closed. "
            "By 1935, nearly half of American medical schools had shut down, including "
            "virtually all schools teaching homeopathic, eclectic, and naturopathic medicine."
        ),
        "year_start": 1910,
        "year_end": 1935,
        "sources": [2315, 2316, 2317],
    },
    # ==== HISTORICAL WIRING: Fishbein / Hoxsey / AMA / FDA ====
    {
        "source": "Morris Fishbein",
        "target": "Harry Hoxsey",
        "type": "suppressed",
        "tier": "documented",
        "desc": (
            "Morris Fishbein, as JAMA editor and de facto AMA spokesman, waged a decades-long "
            "campaign against Harry Hoxsey's cancer clinics. Fishbein publicly labeled Hoxsey "
            "a quack. In 1947, Hoxsey sued Fishbein for libel; at the 1949 federal trial in "
            "Dallas, the jury found in Hoxsey's favor, declaring Fishbein's statements libelous "
            "and ruling that the AMA had 'fixed its gruesome grip on healthcare.' Fishbein was "
            "forced out as JAMA editor in 1950."
        ),
        "year_start": 1936,
        "year_end": 1950,
        "sources": [2318, 2319, 2320],
    },
    {
        "source": "Harry Hoxsey",
        "target": "American Medical Association",
        "type": "target_of",
        "tier": "documented",
        "desc": (
            "The AMA conducted a sustained campaign against Hoxsey's cancer treatment clinics "
            "from the 1930s through the 1950s. The AMA's campaign was led by JAMA editor "
            "Morris Fishbein. Hoxsey won the 1949 libel trial but the institutional campaign "
            "continued through FDA channels."
        ),
        "year_start": 1936,
        "year_end": 1960,
        "sources": [2318, 2319, 2320],
    },
    {
        "source": "Harry Hoxsey",
        "target": "FDA",
        "type": "suppressed_by",
        "tier": "documented",
        "desc": (
            "The FDA shut down all of Hoxsey's cancer treatment clinics across the United "
            "States by 1960. FDA enforcement actions came after the AMA's direct campaign "
            "(which Hoxsey defeated in court) had failed. Hoxsey moved his remaining clinic "
            "to Tijuana, Mexico, where it continued to operate."
        ),
        "year_start": 1956,
        "year_end": 1960,
        "sources": [2318, 2319],
    },
    {
        "source": "Morris Fishbein",
        "target": "Max Gerson",
        "type": "suppressed",
        "tier": "credible",
        "desc": (
            "Morris Fishbein and the AMA under his leadership actively opposed Max Gerson's "
            "nutritional cancer therapy. Despite Gerson's 1946 Senate testimony before the "
            "Pepper-Neely subcommittee, the AMA campaigned against his methods and discouraged "
            "publication of his research."
        ),
        "year_start": 1946,
        "year_end": 1959,
        "sources": [2324, 2325],
    },
    {
        "source": "Max Gerson",
        "target": "American Medical Association",
        "type": "suppressed_by",
        "tier": "credible",
        "desc": (
            "The AMA opposed Gerson's nutritional cancer therapy after his testimony before "
            "the Senate's Pepper-Neely subcommittee (July 1-3, 1946), where he presented "
            "recovered cancer patients. A bill to fund research into his methods failed after "
            "opposition. Gerson died in 1959, his work marginalized by the medical establishment."
        ),
        "year_start": 1946,
        "year_end": 1959,
        "sources": [2324, 2325],
    },
    # ==== HISTORICAL WIRING: Sugar / Keys / Yudkin / Kearns ====
    {
        "source": "Sugar Research Foundation",
        "target": "John Yudkin",
        "type": "suppressed",
        "tier": "documented",
        "desc": (
            "The Sugar Research Foundation funded research and advocacy that discredited "
            "John Yudkin's sugar-as-heart-disease hypothesis. SRF-funded Harvard researchers "
            "published a 1967 NEJM review that shifted blame to dietary fat, helping bury "
            "Yudkin's work for decades. Documented by Kearns et al. (JAMA Internal Medicine, 2016)."
        ),
        "year_start": 1965,
        "year_end": 1972,
        "sources": [2321, 2322],
    },
    {
        "source": "Sugar Research Foundation",
        "target": "Ancel Keys",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The SRF's 1967 campaign to shift blame from sugar to dietary fat aligned with "
            "and amplified Ancel Keys's lipid hypothesis. SRF paid Harvard scientists to "
            "publish a review in the NEJM supporting Keys's position. While Keys was not "
            "directly paid by the SRF, the industry's efforts reinforced his paradigm and "
            "marginalized his critic John Yudkin."
        ),
        "year_start": 1967,
        "sources": [2321, 2323],
    },
    {
        "source": "Cristin Kearns",
        "target": "Sugar Research Foundation",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Cristin Kearns uncovered internal Sugar Research Foundation documents showing "
            "the SRF paid Harvard scientists $6,500 in 1967 to publish a literature review "
            "minimizing sugar's role in heart disease. Her findings, published in JAMA "
            "Internal Medicine in 2016, exposed nearly fifty years of concealed industry "
            "influence on dietary science and public health policy."
        ),
        "year_start": 2016,
        "sources": [2321],
    },
    # ==== HISTORICAL WIRING: Reich / FDA ====
    {
        "source": "FDA",
        "target": "Wilhelm Reich",
        "type": "suppressed",
        "tier": "documented",
        "desc": (
            "The FDA obtained an injunction against Wilhelm Reich in 1954, ordering "
            "destruction of all orgone accumulators and the banning of literature promoting "
            "them. When Reich violated the injunction, he was arrested. In 1956, the FDA "
            "oversaw the burning of several tons of his publications — one of the most "
            "notable instances of book burning in U.S. history. Reich died in Lewisburg "
            "federal penitentiary on November 3, 1957."
        ),
        "year_start": 1954,
        "year_end": 1957,
        "sources": [2326, 2327],
    },
    # ==== HISTORICAL WIRING: IG Farben / Bayer / Fritz ter Meer ====
    {
        "source": "Fritz ter Meer",
        "target": "IG Farben",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Fritz ter Meer served on the IG Farben managing board (Vorstand) and oversaw "
            "plant construction, including the Auschwitz III-Monowitz facility using slave "
            "labor. Convicted at the IG Farben Trial (Nuremberg Case VI, 1948) and sentenced "
            "to seven years. Released in 1950."
        ),
        "year_start": 1926,
        "year_end": 1945,
        "sources": [2328, 2329, 2330],
    },
    {
        "source": "Bayer",
        "target": "IG Farben",
        "type": "subsidiary_of",
        "tier": "documented",
        "desc": (
            "Bayer was a constituent company of the IG Farben conglomerate from 1925 to 1952. "
            "After IG Farben's dissolution by the Allies, Bayer was re-established as an "
            "independent company in 1951. Fritz ter Meer, convicted at Nuremberg for IG Farben "
            "crimes, became chairman of Bayer's supervisory board in 1956."
        ),
        "year_start": 1925,
        "year_end": 1952,
        "sources": [2328, 2330],
    },
    # ==== HISTORICAL WIRING: Hofmann / Sandoz / MKULTRA ====
    {
        "source": "Albert Hofmann",
        "target": "Sandoz Labs",
        "type": "employed_by",
        "tier": "documented",
        "desc": (
            "Albert Hofmann worked as a research chemist at Sandoz Laboratories in Basel, "
            "Switzerland, where he first synthesized LSD-25 in 1938 and discovered its "
            "psychoactive properties in 1943. Sandoz marketed LSD as Delysid for psychiatric "
            "research beginning in 1947."
        ),
        "year_start": 1929,
        "year_end": 1971,
        "sources": [2331, 2332],
    },
    {
        "source": "Sandoz Labs",
        "target": "MKULTRA",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Sandoz Laboratories was the CIA's primary supplier of LSD for the MKULTRA "
            "program. The CIA procured large quantities of LSD from Sandoz in the 1950s "
            "and 1960s for experiments on unwitting subjects. When Sandoz could not meet "
            "demand, the CIA funded domestic production through Eli Lilly."
        ),
        "year_start": 1953,
        "year_end": 1966,
        "sources": [2331, 2333],
    },
    {
        "source": "Sandoz Labs",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Sandoz supplied LSD to the CIA for covert programs including MKULTRA. CIA "
            "operative George White purchased bulk quantities from Sandoz for Operation "
            "Midnight Climax and other sub-projects. Church Committee records document "
            "the procurement chain."
        ),
        "year_start": 1953,
        "year_end": 1966,
        "sources": [2333, 2331],
    },
    # ==== 2025-2026: RFK Jr. / HHS / APPOINTMENTS ====
    {
        "source": "Robert F. Kennedy Jr.",
        "target": "HHS",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as Secretary of Health and Human Services on February 13, 2025, "
            "by a 52-48 Senate vote. As HHS Secretary, oversees the FDA, CDC, NIH, CMS, "
            "and BARDA. Remains in office as of August 2026."
        ),
        "year_start": 2025,
        "sources": [2300, 2301],
    },
    {
        "source": "Robert F. Kennedy Jr.",
        "target": "Donald Trump",
        "type": "appointed_by",
        "tier": "documented",
        "desc": (
            "Nominated by President Donald Trump as HHS Secretary after Kennedy suspended "
            "his independent presidential campaign and endorsed Trump. Kennedy's MAHA "
            "(Make America Healthy Again) platform aligned with Trump's anti-establishment "
            "agenda. Confirmed February 13, 2025."
        ),
        "year_start": 2024,
        "sources": [2300, 2301],
    },
    {
        "source": "Robert F. Kennedy Jr.",
        "target": "Robert F. Kennedy",
        "type": "family_of",
        "tier": "documented",
        "desc": (
            "Son of Senator Robert F. Kennedy, who was assassinated in 1968 during his "
            "presidential campaign. Nephew of President John F. Kennedy. The Kennedy "
            "political dynasty spans three generations."
        ),
        "sources": [2300],
    },
    {
        "source": "Jay Bhattacharya",
        "target": "NIH",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as NIH Director by the Senate on March 25, 2025 (53-47), assuming "
            "office April 1, 2025. Eliminated foreign researcher subcontracting (May 2025). "
            "The first openly vaccine-skepticism-sympathetic NIH Director in the agency's history."
        ),
        "year_start": 2025,
        "sources": [2305],
    },
    {
        "source": "Jay Bhattacharya",
        "target": "CDC",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Appointed Acting CDC Director on February 18, 2026, while retaining the NIH "
            "directorship. Dual appointment consolidated control over both the nation's "
            "primary biomedical research institution and its leading public health agency."
        ),
        "year_start": 2026,
        "sources": [2305],
    },
    {
        "source": "Jay Bhattacharya",
        "target": "Donald Trump",
        "type": "appointed_by",
        "tier": "documented",
        "desc": (
            "Nominated by President Trump as NIH Director. Bhattacharya's co-authorship "
            "of the Great Barrington Declaration and criticism of lockdown policies aligned "
            "with Trump's COVID-era positions. Confirmed March 25, 2025."
        ),
        "year_start": 2025,
        "sources": [2305],
    },
    {
        "source": "Marty Makary",
        "target": "FDA",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as FDA Commissioner on March 25, 2025 (56-44), taking office "
            "April 1, 2025. Initiated food-dye phase-out and school meal improvement "
            "programs. Resigned May 13, 2026, over the administration's reversal of "
            "the e-cigarette ban."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [2306, 2336],
    },
    {
        "source": "Marty Makary",
        "target": "Donald Trump",
        "type": "appointed_by",
        "tier": "documented",
        "desc": (
            "Nominated by President Trump as FDA Commissioner. Makary's criticism of "
            "COVID-era public health measures and advocacy for FDA reform aligned with "
            "the administration's agenda. His resignation in May 2026 was a rare public "
            "break with Trump over health policy."
        ),
        "year_start": 2025,
        "sources": [2306],
    },
    {
        "source": "Vinay Prasad",
        "target": "FDA",
        "type": "employed_by",
        "tier": "documented",
        "desc": (
            "Served as Director of the FDA's Center for Biologics Evaluation and Research "
            "(CBER) from May 6, 2025 to April 30, 2026. Restricted COVID vaccine eligibility "
            "to 65+/high-risk; rejected Moderna mRNA flu vaccine review (Feb 2026). His "
            "November 2025 memo claiming ten children died from COVID vaccination was "
            "condemned by twelve former FDA commissioners."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [2307],
    },
    # ==== 2025-2026: HHS organizational structure ====
    {
        "source": "HHS",
        "target": "CDC",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The CDC is a federal agency within HHS. Under HHS Secretary Kennedy, CDC "
            "Director Monarez was ousted (August 2025), senior officials resigned, and "
            "Jay Bhattacharya was appointed Acting Director (February 2026)."
        ),
        "sources": [2300, 2303],
    },
    {
        "source": "HHS",
        "target": "FDA",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The FDA is a federal agency within HHS. Under HHS Secretary Kennedy, Marty "
            "Makary served as Commissioner (April 2025 - May 2026) and Vinay Prasad "
            "directed CBER (May 2025 - April 2026)."
        ),
        "sources": [2300, 2303],
    },
    {
        "source": "HHS",
        "target": "NIH",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The NIH is a federal agency within HHS. Under HHS Secretary Kennedy, "
            "Jay Bhattacharya was confirmed as NIH Director (April 2025), the first "
            "director sympathetic to vaccine skepticism."
        ),
        "sources": [2300, 2303],
    },
    # ==== 2025-2026: Measles outbreak / public health impact ====
    {
        "source": "2025 United States Measles Outbreak",
        "target": "CDC",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The CDC tracked and responded to the 2025 measles outbreak — 2,255 cases "
            "across 44 states, the largest since 1994. CDC communications director Kevin "
            "Griffis resigned in March 2025 over disagreements with the administration's "
            "messaging on the outbreak."
        ),
        "year_start": 2025,
        "sources": [2302],
    },
    {
        "source": "2025 United States Measles Outbreak",
        "target": "Robert F. Kennedy Jr.",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The measles outbreak unfolded under HHS Secretary Kennedy's leadership. "
            "Kennedy characterized vaccination as a 'personal choice' on February 26 and "
            "promoted vitamin A and cod liver oil as alternatives to vaccination, drawing "
            "criticism from the medical establishment."
        ),
        "year_start": 2025,
        "sources": [2300, 2302],
    },
    # ==== 2025-2026: WHO withdrawal ====
    {
        "source": "Robert F. Kennedy Jr.",
        "target": "WHO",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As HHS Secretary, Kennedy oversaw the U.S. withdrawal from the WHO initiated "
            "by Trump's executive order on January 20, 2025. WHO bylaws require a 12-month "
            "notice period, making the effective withdrawal date approximately January 2026. "
            "Kennedy had been a longtime WHO critic."
        ),
        "year_start": 2025,
        "sources": [2300, 2310],
    },
    # ==== 2025-2026: GoF / EcoHealth ====
    {
        "source": "Robert F. Kennedy Jr.",
        "target": "EcoHealth Alliance",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As HHS Secretary, Kennedy oversaw the department that confirmed the standing "
            "debarment of EcoHealth Alliance from federal funding. EcoHealth had been "
            "debarred in May 2024; the Trump administration upheld the action."
        ),
        "year_start": 2025,
        "sources": [2300, 2309],
    },
    {
        "source": "Robert F. Kennedy Jr.",
        "target": "Anthony Fauci",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Kennedy was a prominent critic of Fauci, authoring 'The Real Anthony Fauci' "
            "(2021). As HHS Secretary, Kennedy led the department Fauci formerly served in "
            "for 38 years. Biden preemptively pardoned Fauci on January 20, 2025 — his "
            "last day in office — reportedly in part due to Kennedy's stated intentions "
            "regarding Fauci's role in gain-of-function research funding."
        ),
        "year_start": 2021,
        "sources": [2300, 2308],
    },
    {
        "source": "Vinay Prasad",
        "target": "Marty Makary",
        "type": "subordinate_of",
        "tier": "documented",
        "desc": (
            "Prasad served as CBER Director under FDA Commissioner Makary. Makary's FDA "
            "leadership oversaw Prasad's appointment and his controversial actions, including "
            "restricting COVID vaccine eligibility and rejecting the Moderna mRNA flu vaccine."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [2306, 2307],
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Robert F. Kennedy Jr.": [2300, 2301, 2302, 2304],
    "HHS": [2300, 2303],
    "Jay Bhattacharya": [2305],
    "Marty Makary": [2306, 2336],
    "Vinay Prasad": [2307],
    "IG Farben": [2328, 2329, 2330],
    "Albert Hofmann": [2331, 2332, 2333],
    "Sugar Research Foundation": [2321, 2322, 2323],
    "Flexner Report": [2315, 2316, 2317],
    "2025 United States Measles Outbreak": [2302],
}

# ============================================================
# ENTITY_UPDATES — 15 existing entities updated
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "Anthony Fauci",
        "description_append": (
            "2025-2026 update: On January 20, 2025 — his last day in office — President "
            "Biden issued a preemptive pardon for Fauci, alongside Gen. Mark Milley and "
            "members of the January 6 Committee, covering potential but unspecified federal "
            "charges. The pardon came as Robert F. Kennedy Jr., a prominent Fauci critic and "
            "author of 'The Real Anthony Fauci,' assumed the HHS Secretary role. The House "
            "Select Subcommittee on the Coronavirus Pandemic published its final report on "
            "December 2, 2024, concluding the pandemic 'most likely' originated from a "
            "lab-related incident and documenting that Fauci's senior advisor had deleted emails."
        ),
        "sources": [2308, 2311, 2300],
    },
    {
        "name": "Peter Daszak",
        "description_append": (
            "2025 update: EcoHealth Alliance's debarment from federal funding, finalized in "
            "May 2024, was confirmed as standing under the incoming Trump administration in "
            "January 2025. Daszak remained EcoHealth president as of late 2024 but the "
            "organization's federal funding pipeline — the mechanism through which NIH money "
            "reached the Wuhan Institute of Virology — was permanently severed."
        ),
        "sources": [2309],
    },
    {
        "name": "EcoHealth Alliance",
        "description_append": (
            "2025 update: EcoHealth Alliance's debarment from federal funding, enacted in "
            "May 2024 following the House Select Subcommittee investigation, was upheld by "
            "the incoming Trump administration. The organization can no longer receive U.S. "
            "government grants, permanently closing the channel through which NIH funds "
            "reached the Wuhan Institute of Virology."
        ),
        "sources": [2309, 2311],
    },
    {
        "name": "WHO",
        "description_append": (
            "2025-2026 update: President Trump signed an executive order on January 20, 2025, "
            "initiating U.S. withdrawal from the WHO — the second such withdrawal (Trump "
            "previously began the process in 2020, reversed by Biden). WHO bylaws require "
            "a 12-month notice period, placing the effective withdrawal date at approximately "
            "January 2026. The World Health Assembly adopted a pandemic agreement in its "
            "May/June 2025 session. Argentina under President Milei also announced intent "
            "to withdraw from the WHO in early 2025."
        ),
        "sources": [2310],
    },
    {
        "name": "CDC",
        "description_append": (
            "2025-2026 update: CDC Director Susan Monarez was ousted in August 2025 under "
            "HHS Secretary Robert F. Kennedy Jr. Multiple senior officials resigned, including "
            "Demetre Daskalakis (NCIRD director) and Debra Houry (chief medical officer). "
            "CDC communications director Kevin Griffis resigned in March 2025 over the "
            "administration's messaging on the measles outbreak. Jay Bhattacharya, already "
            "serving as NIH Director, was appointed Acting CDC Director on February 18, 2026. "
            "The CDC's 'Autism and Vaccines' webpage was revised in November 2025 to abandon "
            "prior scientific consensus language."
        ),
        "sources": [2300, 2305, 2335],
    },
    {
        "name": "FDA",
        "description_append": (
            "2025-2026 update: Marty Makary confirmed as FDA Commissioner (March 25, 2025; "
            "resigned May 13, 2026 over e-cigarette ban reversal). Vinay Prasad served as "
            "CBER Director (May 2025 - April 2026), restricting COVID vaccines to 65+/high-risk "
            "and rejecting Moderna's mRNA flu vaccine. FDA revoked authorization for Red No. 3 "
            "(FD&C Red No. 3/erythrosine) in food and ingested drugs effective January 15, 2025, "
            "with compliance deadlines extending into 2027."
        ),
        "sources": [2306, 2307, 2314, 2336],
    },
    {
        "name": "NIH",
        "description_append": (
            "2025-2026 update: Jay Bhattacharya, co-author of the Great Barrington "
            "Declaration, confirmed as NIH Director on March 25, 2025 (53-47). Key actions "
            "included eliminating foreign researcher subcontracting (May 2025). Bhattacharya "
            "was also appointed Acting CDC Director in February 2026, consolidating control "
            "over both agencies."
        ),
        "sources": [2305],
    },
    {
        "name": "Purdue Pharma",
        "description_append": (
            "2024-2025 update: After the Supreme Court struck down the original ~$6 billion "
            "Sackler settlement in Harrington v. Purdue Pharma (June 2024) — ruling that "
            "bankruptcy courts cannot grant non-debtor releases shielding the Sackler family "
            "from civil liability — a revised settlement was reached increasing the Sackler "
            "family's contribution to approximately $6.5 billion."
        ),
        "sources": [2312, 2338],
    },
    {
        "name": "Gain-of-Function Research",
        "description_append": (
            "2024-2025 update: The House Select Subcommittee on the Coronavirus Pandemic's "
            "final report (December 2, 2024) concluded the pandemic 'most likely' originated "
            "from a lab-related incident at the Wuhan Institute of Virology and documented "
            "that NIH-funded research through EcoHealth Alliance met the definition of "
            "gain-of-function research. EcoHealth's debarment from federal funding was "
            "upheld by the incoming Trump administration."
        ),
        "sources": [2311, 2309],
    },
    {
        "name": "Bayer",
        "description_append": (
            "2025-2026 update: The Supreme Court granted certiorari in a Roundup preemption "
            "case to decide whether federal pesticide labeling under FIFRA preempts state "
            "failure-to-warn claims. Georgia and North Dakota passed state-level pesticide "
            "failure-to-warn shield laws in 2025, potentially limiting future Roundup "
            "litigation in those states."
        ),
        "sources": [2313, 2337],
    },
    {
        "name": "Richard Sackler",
        "description_append": (
            "2024-2025 update: After the Supreme Court struck down the original Purdue "
            "bankruptcy deal's blanket immunity provision in Harrington v. Purdue Pharma "
            "(June 2024), a revised settlement was reached with the Sackler family's "
            "contribution increased to approximately $6.5 billion. The ruling established "
            "that non-debtor third-party releases cannot be granted without creditors' "
            "consent in bankruptcy proceedings."
        ),
        "sources": [2312, 2338],
    },
    {
        "name": "Roundup Cancer Litigation",
        "description_append": (
            "2025-2026 update: The Supreme Court granted certiorari in a Roundup preemption "
            "case to determine whether FIFRA's federal labeling requirements preempt state "
            "failure-to-warn tort claims — a ruling that could effectively end future "
            "Roundup cancer lawsuits. Georgia and North Dakota enacted state-level pesticide "
            "shield laws in 2025 protecting manufacturers from failure-to-warn claims when "
            "their labels comply with EPA standards."
        ),
        "sources": [2313, 2337],
    },
    {
        "name": "Morris Fishbein",
        "description_append": (
            "Historical supplement: In 1947, Harry Hoxsey sued Fishbein for libel in federal "
            "court in Dallas, Texas. At trial in 1949, the jury found in Hoxsey's favor, "
            "declaring Fishbein's published statements libelous. The verdict damaged Fishbein's "
            "credibility, and he was forced out as JAMA editor in 1950 after a quarter-century "
            "in the role."
        ),
        "sources": [2318, 2319, 2320],
    },
    {
        "name": "Harry Hoxsey",
        "description_append": (
            "Historical supplement: Hoxsey won the 1949 federal libel trial against Morris "
            "Fishbein in Dallas, where the jury ruled Fishbein's attacks were libelous. Despite "
            "this courtroom victory, the FDA subsequently shut down all seventeen Hoxsey cancer "
            "clinics across the United States by 1960. Hoxsey relocated his clinic to Tijuana, "
            "Mexico, where the Bio-Medical Center continues to operate."
        ),
        "sources": [2318, 2319, 2320],
    },
    {
        "name": "Wilhelm Reich",
        "description_append": (
            "Historical supplement: The FDA's 1954 injunction ordered the destruction of all "
            "orgone accumulators and the banning of literature mentioning orgone energy. When "
            "an associate shipped accumulators across state lines in violation of the injunction, "
            "Reich was charged with contempt. In 1956, the FDA oversaw the burning of several "
            "tons of Reich's publications in a New York City incinerator — one of the most "
            "notable instances of book burning in American history. Reich died of heart failure "
            "in Lewisburg federal penitentiary on November 3, 1957, days before his parole "
            "hearing."
        ),
        "sources": [2326, 2327],
    },
]

# ============================================================
# GEO_COORDS — for every new entity
# ============================================================

GEO_COORDS = {
    "Robert F. Kennedy Jr.": (38.8862, -77.0199, "credible", "HHS headquarters, Washington DC"),
    "HHS": (38.8862, -77.0199, "documented", "Hubert H. Humphrey Building, 200 Independence Ave SW, Washington DC"),
    "Jay Bhattacharya": (38.9959, -77.0969, "credible", "NIH campus, Bethesda MD"),
    "Marty Makary": (39.0303, -76.9760, "credible", "FDA White Oak campus, Silver Spring MD"),
    "Vinay Prasad": (39.0303, -76.9760, "credible", "FDA/CBER, Silver Spring MD"),
    "IG Farben": (50.1275, 8.6697, "documented", "IG Farben Building (now Goethe University), Frankfurt am Main"),
    "Albert Hofmann": (47.5596, 7.5886, "credible", "Basel, Switzerland — Sandoz Laboratories"),
    "Sugar Research Foundation": (38.9072, -77.0369, "credible", "Washington DC"),
    "Flexner Report": (40.7549, -73.9840, "credible", "New York City — Carnegie Foundation headquarters"),
    "2025 United States Measles Outbreak": (32.14, -102.63, "credible", "Gaines County, Texas — outbreak epicenter"),
}

# ============================================================
# PHOTO_CANDIDATES — for new persons / orgs
# ============================================================

PHOTO_CANDIDATES = {
    "Robert F. Kennedy Jr.": "https://upload.wikimedia.org/wikipedia/commons/7/70/Robert_F._Kennedy_Jr._official_portrait.jpg",
    "Jay Bhattacharya": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Jay_Bhattacharya_in_2024_%28cropped%29.jpg",
    "Marty Makary": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Marty_Makary_official_FDA_portrait.jpg",
    "Albert Hofmann": "https://upload.wikimedia.org/wikipedia/commons/0/05/Albert_Hofmann_Oct_1993.jpg",
    "IG Farben": "https://upload.wikimedia.org/wikipedia/commons/8/89/Frankfurt_IG-Farben-Haus_A.jpg",
}
