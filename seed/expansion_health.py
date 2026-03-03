"""
Big Pharma & Health Governance — Expansion layer for Intel Console.

Maps the architecture of health-sector control: regulatory capture (FDA/CDC/NIH
revolving door), pharmaceutical industry power, global health governance (WHO,
GAVI, Gates Foundation), the opioid crisis as case study in corporate capture,
gain-of-function research controversy, documented human experimentation programs,
suppressed healing modalities, and the food system control layer (Monsanto/Bayer).

This branch represents the most publicly visible control mechanism post-COVID
and one of the clearest examples of institutional capture across multiple sectors.

Entities (~30): Regulatory agencies (FDA, CDC, NIH, WHO), pharma companies
(Pfizer, Purdue Pharma, Monsanto/Bayer), key figures (Anthony Fauci, Bill Gates,
Peter Daszak, Ralph Baric, Arthur Sackler, Sidney Gottlieb, Donald Ewen Cameron),
organizations (Gates Foundation, GAVI, EcoHealth Alliance), experiments
(Tuskegee, Guatemala), gain-of-function research framework.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], FBI [84], MKULTRA [94], Church Committee [338],
  Jeffrey Epstein [1], Richard Helms [28]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 530+ (continuing from existing 529)
# ============================================================

SOURCES = [
    # --- FDA / Regulatory Capture ---
    {
        "id": 530,
        "title": "FDA — Wikipedia (history, structure, regulatory authority)",
        "url": "https://en.wikipedia.org/wiki/Food_and_Drug_Administration",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 531,
        "title": "A Prescription for Revolving-Door Problems at the FDA — Project on Government Oversight (POGO)",
        "url": "https://www.pogo.org/analysis/a-prescription-for-revolving-door-problems-at-the-fda",
        "source_type": "journalism",
        "author": "Project on Government Oversight",
        "year": 2016,
    },
    {
        "id": 532,
        "title": "FDA User Fee Acts and the PDUFA Process — Congressional Research Service",
        "url": "https://crsreports.congress.gov/product/pdf/R/R47101",
        "source_type": "congressional",
        "year": 2022,
    },
    # --- CDC ---
    {
        "id": 533,
        "title": "CDC — Wikipedia (history, mission, controversies)",
        "url": "https://en.wikipedia.org/wiki/Centers_for_Disease_Control_and_Prevention",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 534,
        "title": "CDC Scientists File Ethics Complaint Over Agency's Integrity — Public Employees for Environmental Responsibility",
        "url": "https://peer.org/cdc-scientists-file-ethics-complaint-over-agencys-integrity/",
        "source_type": "other",
        "author": "PEER",
        "year": 2016,
    },
    # --- NIH / Fauci ---
    {
        "id": 535,
        "title": "NIH — Wikipedia (structure, funding, research mission)",
        "url": "https://en.wikipedia.org/wiki/National_Institutes_of_Health",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 536,
        "title": "Anthony Fauci — Wikipedia (NIAID tenure, career, COVID response)",
        "url": "https://en.wikipedia.org/wiki/Anthony_Fauci",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 537,
        "title": "NIH admits to funding gain-of-function research in Wuhan — The Intercept",
        "url": "https://theintercept.com/2021/09/06/new-details-emerge-about-coronavirus-research-at-chinese-lab/",
        "source_type": "journalism",
        "author": "Sharon Lerner & Mara Hvistendahl",
        "year": 2021,
    },
    {
        "id": 538,
        "title": "Fauci testifies before House COVID Select Subcommittee — C-SPAN / Congress.gov",
        "url": "https://www.congress.gov/event/118th-congress/house-event/117369",
        "source_type": "congressional",
        "year": 2024,
    },
    # --- WHO ---
    {
        "id": 539,
        "title": "World Health Organization — Wikipedia (structure, governance, funding)",
        "url": "https://en.wikipedia.org/wiki/World_Health_Organization",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 540,
        "title": "WHO Programme Budget — Assessed and voluntary contributions by donor",
        "url": "https://open.who.int/who-programme-budget/",
        "source_type": "government",
        "year": 2024,
    },
    # --- Bill Gates / Gates Foundation ---
    {
        "id": 541,
        "title": "Bill Gates — Wikipedia (Microsoft, philanthropy, global health)",
        "url": "https://en.wikipedia.org/wiki/Bill_Gates",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 542,
        "title": "Bill & Melinda Gates Foundation — Wikipedia (endowment, global health programs)",
        "url": "https://en.wikipedia.org/wiki/Bill_%26_Melinda_Gates_Foundation",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 543,
        "title": "How Bill Gates and partners used their clout to control the global Covid response — Politico",
        "url": "https://www.politico.com/news/2022/09/14/global-covid-pandemic-response-bill-gates-partners-00053969",
        "source_type": "journalism",
        "author": "Politico",
        "year": 2022,
    },
    {
        "id": 544,
        "title": "The Bill Gates Problem: Reckoning with the Myth of the Good Billionaire — Tim Schwab (Columbia Journalism Review)",
        "url": "https://www.cjr.org/criticism/gates-foundation-journalism-funding.php",
        "source_type": "journalism",
        "author": "Tim Schwab",
        "year": 2020,
    },
    # --- GAVI ---
    {
        "id": 545,
        "title": "GAVI, the Vaccine Alliance — Wikipedia (founding, structure, donors)",
        "url": "https://en.wikipedia.org/wiki/GAVI",
        "source_type": "other",
        "year": 2024,
    },
    # --- EcoHealth Alliance / Gain-of-Function ---
    {
        "id": 546,
        "title": "EcoHealth Alliance — Wikipedia (founding, WIV collaboration, controversy)",
        "url": "https://en.wikipedia.org/wiki/EcoHealth_Alliance",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 547,
        "title": "Peter Daszak — Wikipedia (EcoHealth president, WIV collaboration)",
        "url": "https://en.wikipedia.org/wiki/Peter_Daszak",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 548,
        "title": "NIH Grant R01 AI110964 to EcoHealth Alliance — NIH Reporter",
        "url": "https://reporter.nih.gov/search/xQW6UJmWfUuVm6mhJkafgQ/project-details/9819304",
        "source_type": "government",
        "year": 2014,
    },
    {
        "id": 549,
        "title": "Ralph Baric — Wikipedia (coronavirus research, gain-of-function)",
        "url": "https://en.wikipedia.org/wiki/Ralph_S._Baric",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 550,
        "title": "A SARS-like cluster of circulating bat coronaviruses shows potential for human emergence — Menachery, Yount, Debbink, ... Baric (2015)",
        "url": "https://www.nature.com/articles/nm.3985",
        "source_type": "academic",
        "author": "Vineet Menachery, Ralph Baric et al.",
        "year": 2015,
    },
    {
        "id": 551,
        "title": "House Select Subcommittee on the Coronavirus Pandemic Final Report",
        "url": "https://oversight.house.gov/wp-content/uploads/2024/12/12.2.24-SSC-Final-Report_Complete.pdf",
        "source_type": "congressional",
        "year": 2024,
    },
    # --- Sackler Family / Purdue Pharma / Opioid Crisis ---
    {
        "id": 552,
        "title": "Arthur M. Sackler — Wikipedia (pharma advertising pioneer)",
        "url": "https://en.wikipedia.org/wiki/Arthur_M._Sackler",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 553,
        "title": "Purdue Pharma — Wikipedia (OxyContin, lawsuits, bankruptcy)",
        "url": "https://en.wikipedia.org/wiki/Purdue_Pharma",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 554,
        "title": "In re Purdue Pharma L.P. — Supreme Court ruling on Sackler immunity (Harrington v. Purdue Pharma)",
        "url": "https://www.supremecourt.gov/opinions/23pdf/23-124_p86b.pdf",
        "source_type": "court",
        "year": 2024,
    },
    {
        "id": 555,
        "title": "The Family That Built an Empire of Pain — Patrick Radden Keefe, New Yorker",
        "url": "https://www.newyorker.com/magazine/2017/10/30/the-family-that-built-an-empire-of-pain",
        "source_type": "journalism",
        "author": "Patrick Radden Keefe",
        "year": 2017,
    },
    {
        "id": 556,
        "title": "Purdue Pharma pleads guilty to federal criminal charges — DOJ Press Release",
        "url": "https://www.justice.gov/opa/pr/purdue-pharma-lp-admits-guilt-federal-opioid-charges",
        "source_type": "government",
        "year": 2020,
    },
    # --- Pfizer ---
    {
        "id": 557,
        "title": "Pfizer — Wikipedia (corporate history, products, settlements)",
        "url": "https://en.wikipedia.org/wiki/Pfizer",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 558,
        "title": "Justice Department Announces Largest Health Care Fraud Settlement in Its History — DOJ ($2.3B Pfizer settlement)",
        "url": "https://www.justice.gov/opa/pr/justice-department-announces-largest-health-care-fraud-settlement-its-history",
        "source_type": "government",
        "year": 2009,
    },
    # --- Monsanto / Bayer ---
    {
        "id": 559,
        "title": "Monsanto — Wikipedia (history, Roundup, GMOs, Bayer acquisition)",
        "url": "https://en.wikipedia.org/wiki/Monsanto",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 560,
        "title": "The Monsanto Papers — Le Monde / U.S. Right to Know (Roundup cancer litigation)",
        "url": "https://usrtk.org/pesticides/monsanto-papers/",
        "source_type": "journalism",
        "author": "U.S. Right to Know",
        "year": 2017,
    },
    {
        "id": 561,
        "title": "Bayer to pay $10.9B to settle Roundup cancer claims — Reuters",
        "url": "https://www.reuters.com/article/us-bayer-litigation-settlement-idUSKBN23V2FP",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2020,
    },
    # --- Sidney Gottlieb / MKULTRA ---
    {
        "id": 562,
        "title": "Sidney Gottlieb — Wikipedia (MKULTRA director, Technical Services Staff)",
        "url": "https://en.wikipedia.org/wiki/Sidney_Gottlieb",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 563,
        "title": "Project MKUltra, the CIA's Program of Research in Behavioral Modification — Senate Select Committee on Intelligence (1977)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/hearings/95mkultra.pdf",
        "source_type": "congressional",
        "year": 1977,
    },
    # --- Donald Ewen Cameron ---
    {
        "id": 564,
        "title": "Donald Ewen Cameron — Wikipedia (MKULTRA Subproject 68, McGill experiments)",
        "url": "https://en.wikipedia.org/wiki/Donald_Ewen_Cameron",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 565,
        "title": "In the Sleep Room: The Story of the CIA Brainwashing Experiments — Anne Collins (book / CBC documentary)",
        "url": "https://en.wikipedia.org/wiki/In_the_Sleep_Room",
        "source_type": "other",
        "author": "Anne Collins",
        "year": 1988,
    },
    {
        "id": 566,
        "title": "Canada settles with MKULTRA brainwashing victims at McGill — CBC News",
        "url": "https://www.cbc.ca/news/canada/montreal/canada-settles-with-mkultra-brainwashing-victims-at-mcgill-1.6785665",
        "source_type": "journalism",
        "author": "CBC News",
        "year": 2023,
    },
    # --- Tuskegee Syphilis Study ---
    {
        "id": 567,
        "title": "U.S. Public Health Service Syphilis Study at Tuskegee — CDC official page",
        "url": "https://www.cdc.gov/tuskegee/index.html",
        "source_type": "government",
        "year": 2024,
    },
    {
        "id": 568,
        "title": "Tuskegee Syphilis Study — Wikipedia (1932-1972, 40-year study)",
        "url": "https://en.wikipedia.org/wiki/Tuskegee_Syphilis_Study",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 569,
        "title": "Final Report of the Tuskegee Syphilis Study Legacy Committee — University of Virginia bioethics",
        "url": "https://bioethics.virginia.edu/tuskegee-syphilis-study",
        "source_type": "academic",
        "year": 1996,
    },
    # --- Guatemala Syphilis Experiments ---
    {
        "id": 570,
        "title": "U.S. apologizes for Guatemala syphilis experiments — NPR",
        "url": "https://www.npr.org/sections/health-shots/2010/10/01/130266949/u-s-apologizes-for-guatemala-syphilis-experiments",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2010,
    },
    {
        "id": 571,
        "title": "Ethically Impossible: STD Research in Guatemala 1946-1948 — Presidential Commission for Bioethics",
        "url": "https://bioethics.gov/sites/default/files/Ethically-Impossible_PCSBI.pdf",
        "source_type": "government",
        "year": 2011,
    },
    # --- Royal Raymond Rife ---
    {
        "id": 572,
        "title": "Royal Raymond Rife — Wikipedia (microscope, frequency therapy controversy)",
        "url": "https://en.wikipedia.org/wiki/Royal_Raymond_Rife",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 573,
        "title": "The Rife Machine — Smithsonian National Museum of American History",
        "url": "https://americanhistory.si.edu/collections/search/object/nmah_1307856",
        "source_type": "other",
        "year": 2024,
    },
    # --- PDUFA / Industry Funding of FDA ---
    {
        "id": 574,
        "title": "Prescription Drug User Fee Act (PDUFA) — FDA.gov",
        "url": "https://www.fda.gov/industry/prescription-drug-user-fee-amendments/pdufa-legislation-and-background",
        "source_type": "government",
        "year": 2022,
    },
    # --- Epstein-MIT/academic ---
    {
        "id": 575,
        "title": "MIT Media Lab and Jeffrey Epstein — MIT investigation report",
        "url": "https://www.mit.edu/item/mit-releases-results-of-fact-finding-on-jeffrey-epstein/",
        "source_type": "other",
        "year": 2020,
    },
]

# ============================================================
# ENTITIES — ~30 new
# ============================================================

ENTITIES = [
    # ============ PEOPLE ============

    {
        "name": "Anthony Fauci",
        "entity_type": "person",
        "description": (
            "American immunologist who served as Director of the National Institute of "
            "Allergy and Infectious Diseases (NIAID) from 1984 to 2022 — a 38-year tenure "
            "spanning seven presidents. Became the public face of the U.S. COVID-19 response. "
            "Testified before the House Select Subcommittee on the Coronavirus Pandemic (2024) "
            "regarding NIH funding of gain-of-function research through EcoHealth Alliance "
            "grants to the Wuhan Institute of Virology. The longest-serving head of any NIH "
            "institute, overseeing $6.1 billion in annual research funding. His dual role as "
            "chief scientist and chief policy spokesperson during COVID raised questions about "
            "the conflation of scientific authority with political power."
        ),
        "aliases": "Dr. Fauci, Anthony Stephen Fauci",
        "metadata": {
            "nationality": "American",
            "born": "1940-12-24",
            "role": "NIAID Director 1984-2022",
        },
    },
    {
        "name": "Bill Gates",
        "entity_type": "person",
        "description": (
            "Co-founder of Microsoft. Through the Bill & Melinda Gates Foundation (est. 2000), "
            "became the single largest private funder of global health initiatives. The "
            "Foundation has spent over $50 billion on global health, agriculture, and education. "
            "Gates Foundation is the second-largest contributor to WHO (after Germany), giving "
            "it extraordinary influence over global health policy. Co-founded GAVI, the Vaccine "
            "Alliance. The Foundation's investments in pharmaceutical companies that benefit "
            "from the health policies it advocates have been documented by investigative "
            "journalists. Met with Jeffrey Epstein multiple times beginning in 2011 — after "
            "Epstein's 2008 conviction — which Gates initially denied, then acknowledged."
        ),
        "aliases": "William Henry Gates III",
        "metadata": {
            "nationality": "American",
            "born": "1955-10-28",
            "role": "Microsoft co-founder, Gates Foundation co-chair",
        },
    },
    {
        "name": "Peter Daszak",
        "entity_type": "person",
        "description": (
            "British-American zoologist and president of EcoHealth Alliance. Directed NIH-funded "
            "research on bat coronaviruses at the Wuhan Institute of Virology through NIAID "
            "grant R01 AI110964. Organized the February 2020 Lancet letter (signed by 27 "
            "scientists) dismissing the lab-leak hypothesis as 'conspiracy theory' — without "
            "disclosing his conflict of interest as WIV's primary U.S. research partner. "
            "Served on the WHO-convened team investigating COVID-19 origins (2021) despite "
            "the same conflict. Grant suspended by NIH in 2020; EcoHealth Alliance debarred "
            "from federal funding in 2024 following congressional investigation."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "British-American",
            "born": "1966",
            "role": "EcoHealth Alliance president",
        },
    },
    {
        "name": "Ralph Baric",
        "entity_type": "person",
        "description": (
            "American virologist and epidemiologist at the University of North Carolina "
            "at Chapel Hill. Pioneered reverse genetics techniques for coronaviruses, enabling "
            "construction of chimeric viruses from synthetic genomes. Co-authored the 2015 "
            "Nature Medicine paper creating a chimeric bat coronavirus that could infect "
            "human airway cells — research flagged by the NIH moratorium on gain-of-function "
            "research but allowed to proceed under exception. Trained researchers at the "
            "Wuhan Institute of Virology. His lab's capabilities are central to the "
            "gain-of-function debate."
        ),
        "aliases": "Ralph S. Baric",
        "metadata": {
            "nationality": "American",
            "role": "UNC virologist, coronavirus gain-of-function researcher",
        },
    },
    {
        "name": "Arthur Sackler",
        "entity_type": "person",
        "description": (
            "American psychiatrist, businessman, and philanthropist. Pioneered modern "
            "pharmaceutical advertising in the 1950s-60s through his agency Medical Advertising "
            "Hall of Fame. His marketing of Valium for Roche made it the first $100 million "
            "drug. Died in 1987, before his brothers' company Purdue Pharma introduced "
            "OxyContin (1996), but his innovations in pharma marketing created the playbook "
            "that Purdue used: direct-to-physician promotion, minimizing addiction risks, "
            "and manufacturing demand through aggressive sales tactics. The Sackler name has "
            "been removed from institutions worldwide (Met Museum, Louvre, Tate, etc.) due "
            "to the family's role in the opioid crisis."
        ),
        "aliases": "Arthur Mitchell Sackler",
        "metadata": {
            "nationality": "American",
            "born": "1913-08-22",
            "died": "1987-05-26",
            "role": "Pharma advertising pioneer, Sackler family patriarch",
        },
    },
    {
        "name": "Sidney Gottlieb",
        "entity_type": "person",
        "description": (
            "American chemist who directed the CIA's MKULTRA program (1953-1973) as head of "
            "the Technical Services Staff. Oversaw 149 sub-projects involving LSD experiments "
            "on unwitting subjects, sensory deprivation, electroshock, hypnosis, and other "
            "mind control techniques. Tested LSD on CIA employees, military personnel, "
            "prisoners, and mental patients — often without consent. At least one death "
            "(Frank Olson, 1953) is attributed to his experiments. Destroyed most MKULTRA "
            "records in 1973 before Church Committee investigation. Testified before the "
            "Senate in 1977, invoking the Fifth Amendment. Known as the CIA's 'Black Sorcerer' "
            "and 'Dirty Trickster.'"
        ),
        "aliases": "Joseph Scheider (birth name)",
        "metadata": {
            "nationality": "American",
            "born": "1918-08-03",
            "died": "1999-03-07",
            "role": "CIA MKULTRA director, Technical Services Staff chief",
        },
    },
    {
        "name": "Donald Ewen Cameron",
        "entity_type": "person",
        "description": (
            "Scottish-born American psychiatrist. President of the American Psychiatric "
            "Association (1952-1953), Canadian Psychiatric Association, and World Psychiatric "
            "Association. Directed MKULTRA Subproject 68 at McGill University's Allan Memorial "
            "Institute in Montreal (1957-1964). Conducted 'psychic driving' experiments on "
            "patients: drug-induced comas lasting weeks, electroshock treatments at 30-40 times "
            "normal intensity, forced listening to looped messages for days. Patients suffered "
            "permanent memory loss, regression, and incontinence. Funded by the CIA through "
            "front organizations. Canada settled with victims in 2023. His experiments remain "
            "among the most documented cases of government-funded medical torture."
        ),
        "aliases": "D. Ewen Cameron",
        "metadata": {
            "nationality": "American (born Scottish)",
            "born": "1901-12-24",
            "died": "1967-09-08",
            "role": "MKULTRA Subproject 68 director, McGill Allan Memorial Institute",
        },
    },
    {
        "name": "Royal Raymond Rife",
        "entity_type": "person",
        "description": (
            "American inventor who in the 1930s developed a high-magnification optical "
            "microscope (the 'Universal Microscope') and claimed to observe live viruses, "
            "developing a theory of destroying pathogens using specific electromagnetic "
            "frequencies ('Mortal Oscillatory Rate'). His work attracted support from "
            "established medical figures including Dr. Milbank Johnson (USC) who conducted "
            "clinical trials in 1934. Equipment was reportedly confiscated and laboratories "
            "damaged. His supporters allege systematic suppression by the AMA under Morris "
            "Fishbein. The scientific establishment classifies his frequency therapy claims "
            "as unproven. His story has become a prominent case study in the suppressed "
            "healing modalities discourse."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "American",
            "born": "1888-05-16",
            "died": "1971-08-05",
            "role": "Inventor, frequency therapy pioneer (controversial)",
        },
    },

    # ============ ORGANIZATIONS ============

    {
        "name": "FDA",
        "entity_type": "agency",
        "description": (
            "U.S. Food and Drug Administration, federal agency within HHS responsible for "
            "regulating food, drugs, biologics, medical devices, and tobacco. Approves all "
            "pharmaceuticals for the U.S. market. Since the Prescription Drug User Fee Act "
            "(PDUFA, 1992), the FDA's drug review division has been predominantly funded by "
            "fees paid by pharmaceutical companies — the entities it regulates. As of 2022, "
            "industry user fees account for ~65% of the FDA's human drug review budget. "
            "A 2016 study by POGO found that 27 out of 55 FDA medical reviewers moved to "
            "industry positions at companies they had previously regulated. This revolving "
            "door is the structural mechanism of regulatory capture."
        ),
        "aliases": "Food and Drug Administration",
    },
    {
        "name": "CDC",
        "entity_type": "agency",
        "description": (
            "U.S. Centers for Disease Control and Prevention, the national public health "
            "agency headquartered in Atlanta, Georgia. Issues vaccination schedules, disease "
            "surveillance, and public health guidance. The CDC Foundation (est. 1995) accepts "
            "donations from pharmaceutical companies, creating structural conflicts. In 2016, "
            "a group of senior CDC scientists (the 'Spider' group — Scientists Preserving "
            "Integrity, Diligence, and Ethics in Research) filed an internal complaint alleging "
            "the agency's integrity was being undermined by outside influence. During COVID-19, "
            "CDC guidance on masking, testing, and vaccines faced criticism for inconsistency "
            "and perceived political influence."
        ),
        "aliases": "Centers for Disease Control and Prevention, Centers for Disease Control",
    },
    {
        "name": "NIH",
        "entity_type": "agency",
        "description": (
            "U.S. National Institutes of Health, the primary federal agency for biomedical "
            "research. Comprises 27 institutes and centers, including NIAID (directed by "
            "Anthony Fauci, 1984-2022). Distributes approximately $45 billion annually in "
            "research grants — making it the single largest funder of biomedical research "
            "in the world. This funding power gives NIH enormous influence over which "
            "research questions are pursued and which researchers advance. NIH-funded "
            "gain-of-function research through EcoHealth Alliance grants to the Wuhan "
            "Institute of Virology became a central controversy in the COVID-19 origins "
            "debate."
        ),
        "aliases": "National Institutes of Health, NIAID",
    },
    {
        "name": "WHO",
        "entity_type": "organization",
        "description": (
            "World Health Organization, the United Nations' specialized health agency "
            "headquartered in Geneva. 194 member states. Sets global health standards, "
            "coordinates pandemic response, and issues treatment guidelines adopted by "
            "nations worldwide. Funding has shifted from assessed contributions (guaranteed, "
            "unrestricted) to voluntary contributions (often earmarked by donors for specific "
            "programs). The Gates Foundation is the second-largest contributor after Germany, "
            "giving a private foundation outsized influence over global health priorities. "
            "Criticized for slow response to the 2014 Ebola outbreak, initially dismissing "
            "SARS-CoV-2 human-to-human transmission, and relying on Chinese government data "
            "in the early COVID-19 investigation."
        ),
        "aliases": "World Health Organization",
    },
    {
        "name": "Bill & Melinda Gates Foundation",
        "entity_type": "foundation",
        "description": (
            "Largest private foundation in the world with an endowment exceeding $67 billion. "
            "The dominant private funder of global health programs. Second-largest contributor "
            "to the WHO. Co-founded and funds GAVI. Funds research at universities, health "
            "ministries, and NGOs across 130+ countries. Its grant-making concentrates power "
            "over global health priorities in a single unelected institution. The Foundation "
            "holds investments in pharmaceutical companies (Pfizer, BioNTech, Merck) that "
            "benefit from the vaccine and health programs it funds — a structural conflict "
            "documented by investigative journalists at Columbia Journalism Review and "
            "The Nation."
        ),
        "aliases": "Gates Foundation, BMGF",
    },
    {
        "name": "GAVI",
        "entity_type": "organization",
        "description": (
            "Global Alliance for Vaccines and Immunisation (rebranded Gavi, the Vaccine "
            "Alliance). Public-private partnership founded in 2000 at the World Economic "
            "Forum with a $750 million grant from the Gates Foundation. Partners include WHO, "
            "UNICEF, World Bank, and pharmaceutical industry. Has vaccinated over 1 billion "
            "children in developing countries. Critics note that GAVI's structure gives "
            "pharmaceutical companies and the Gates Foundation direct influence over vaccine "
            "procurement and distribution policy for the developing world."
        ),
        "aliases": "Gavi, the Vaccine Alliance, Global Alliance for Vaccines and Immunisation",
    },
    {
        "name": "EcoHealth Alliance",
        "entity_type": "organization",
        "description": (
            "U.S.-based nonprofit research organization focused on emerging infectious "
            "diseases. Under President Peter Daszak, served as the intermediary for NIH/NIAID "
            "funding (Grant R01 AI110964) to the Wuhan Institute of Virology for bat "
            "coronavirus research. The grant funded collection of bat coronaviruses from "
            "caves in Yunnan Province and research on their potential to infect humans. "
            "Congress determined that EcoHealth failed to comply with NIH grant conditions "
            "and failed to file required progress reports. Debarred from federal funding "
            "in May 2024 following House Select Subcommittee investigation."
        ),
        "aliases": "EHA",
    },
    {
        "name": "Purdue Pharma",
        "entity_type": "organization",
        "description": (
            "American pharmaceutical company owned by the Sackler family. Developed and "
            "marketed OxyContin (extended-release oxycodone) beginning in 1996. The company's "
            "aggressive marketing strategy — including claims that OxyContin had low addiction "
            "risk ('less than one percent') — is credited with igniting the U.S. opioid "
            "epidemic, which has killed over 500,000 Americans since 1999. Pleaded guilty to "
            "federal criminal charges in 2007 and again in 2020 (misbranding, conspiracy to "
            "defraud the U.S.). Filed for bankruptcy in 2019. The Supreme Court ruled in 2024 "
            "that the Sackler family's $6 billion settlement could not include blanket immunity "
            "from future lawsuits (Harrington v. Purdue Pharma)."
        ),
        "aliases": "Purdue Pharmaceuticals",
    },
    {
        "name": "Pfizer",
        "entity_type": "organization",
        "description": (
            "American multinational pharmaceutical company, one of the world's largest by "
            "revenue. In 2009, paid $2.3 billion in the largest health care fraud settlement "
            "in DOJ history for illegal promotion of Bextra and other drugs. Produced the "
            "first authorized mRNA COVID-19 vaccine (with BioNTech) under Emergency Use "
            "Authorization in December 2020. COVID vaccine revenue exceeded $37 billion in "
            "2022 alone. The company's history of regulatory violations — including the 2009 "
            "settlement, a 1996 controversial meningitis drug trial in Nigeria (Trovan), and "
            "multiple off-label marketing fines — exists in tension with its role as a trusted "
            "public health partner during the pandemic."
        ),
        "aliases": "Pfizer Inc.",
    },
    {
        "name": "Monsanto",
        "entity_type": "organization",
        "description": (
            "American agrochemical and agricultural biotechnology corporation. Producer of "
            "Roundup (glyphosate) herbicide and genetically modified seeds. Controlled ~80% "
            "of the U.S. corn and ~90% of the soybean seed market through patents and licensing. "
            "Internal documents revealed by litigation (the 'Monsanto Papers') showed the "
            "company knew of cancer risks from glyphosate, ghostwrote scientific studies, and "
            "attempted to discredit IARC's 2015 classification of glyphosate as 'probably "
            "carcinogenic.' Acquired by Bayer AG in 2018 for $63 billion. Bayer subsequently "
            "agreed to pay $10.9 billion to settle ~100,000 Roundup cancer lawsuits. The "
            "Monsanto name was retired after acquisition."
        ),
        "aliases": "Monsanto Company, Bayer Crop Science (post-2018)",
    },

    # ============ PROGRAMS / EXPERIMENTS ============

    {
        "name": "Tuskegee Syphilis Study",
        "entity_type": "program",
        "description": (
            "U.S. Public Health Service study conducted from 1932 to 1972 in Tuskegee, "
            "Alabama. 399 Black men with syphilis were told they were receiving free treatment "
            "for 'bad blood' but were deliberately left untreated to study the disease's "
            "progression — even after penicillin became the standard cure in 1947. 128 men "
            "died of syphilis or its complications; 40 wives were infected; 19 children were "
            "born with congenital syphilis. Exposed by AP reporter Jean Heller in 1972. Led "
            "to the National Research Act (1974) and the Belmont Report establishing ethical "
            "principles for human subjects research. President Clinton issued a formal apology "
            "in 1997. Remains a foundational reason for medical distrust in Black communities."
        ),
        "aliases": "Tuskegee Study of Untreated Syphilis in the Negro Male, USPHS Syphilis Study",
    },
    {
        "name": "Guatemala Syphilis Experiments",
        "entity_type": "program",
        "description": (
            "U.S.-funded experiments (1946-1948) in which U.S. Public Health Service "
            "researchers deliberately infected Guatemalan prisoners, soldiers, sex workers, "
            "and psychiatric patients with syphilis, gonorrhea, and chancroid — without consent "
            "— to test the effectiveness of penicillin. Led by Dr. John Charles Cutler, who "
            "later participated in the Tuskegee Study. At least 83 deaths. Discovered by "
            "Wellesley historian Susan Reverby in 2010. President Obama personally called "
            "Guatemalan President Colom to apologize. The Presidential Commission for the "
            "Study of Bioethical Issues published 'Ethically Impossible' (2011) documenting "
            "the experiments."
        ),
        "aliases": "U.S.-Guatemala STD experiments",
    },
    {
        "name": "Gain-of-Function Research",
        "entity_type": "program",
        "description": (
            "Research methodology that deliberately enhances the transmissibility, virulence, "
            "or host range of pathogens. The U.S. government imposed a moratorium on federally "
            "funded gain-of-function research on influenza, MERS, and SARS viruses in October "
            "2014, lifted in December 2017 with the P3CO (Potential Pandemic Pathogen Care and "
            "Oversight) framework. During the moratorium, EcoHealth Alliance's bat coronavirus "
            "research at the Wuhan Institute of Virology continued under an exception. Whether "
            "NIH-funded research at WIV constituted gain-of-function became a central "
            "controversy in the COVID-19 origins debate. The House Select Subcommittee's 2024 "
            "final report concluded the pandemic 'most likely' originated from a lab-related "
            "incident."
        ),
        "aliases": "GOF research, enhanced potential pandemic pathogen research, ePPP",
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ==== REGULATORY ARCHITECTURE ====
    {
        "source": "Anthony Fauci",
        "target": "NIH",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Director of NIAID (an NIH institute) from 1984 to 2022 — 38 years spanning "
            "seven presidents. Oversaw $6.1 billion in annual research funding."
        ),
        "year_start": 1984,
        "year_end": 2022,
        "sources": [535, 536],
    },
    {
        "source": "NIH",
        "target": "EcoHealth Alliance",
        "type": "funded",
        "tier": "documented",
        "desc": (
            "NIAID Grant R01 AI110964 funded EcoHealth Alliance's bat coronavirus research "
            "at the Wuhan Institute of Virology. Grant suspended 2020, EcoHealth debarred 2024."
        ),
        "year_start": 2014,
        "year_end": 2020,
        "sources": [537, 548, 551],
    },
    {
        "source": "Peter Daszak",
        "target": "EcoHealth Alliance",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "President of EcoHealth Alliance. Directed the organization's WIV collaboration "
            "and NIH-funded bat coronavirus research."
        ),
        "sources": [546, 547],
    },
    {
        "source": "EcoHealth Alliance",
        "target": "Gain-of-Function Research",
        "type": "conducted",
        "tier": "credible",
        "desc": (
            "Channeled NIH funds to WIV for bat coronavirus research that congressional "
            "investigation determined met the definition of gain-of-function research. "
            "EcoHealth failed to comply with grant conditions and reporting requirements."
        ),
        "year_start": 2014,
        "sources": [537, 548, 550, 551],
    },
    {
        "source": "Ralph Baric",
        "target": "Gain-of-Function Research",
        "type": "pioneered",
        "tier": "documented",
        "desc": (
            "Pioneered reverse genetics for coronaviruses. 2015 Nature Medicine paper created "
            "chimeric bat coronavirus capable of infecting human airway cells. Trained WIV "
            "researchers in these techniques."
        ),
        "year_start": 2015,
        "sources": [549, 550],
    },
    {
        "source": "Anthony Fauci",
        "target": "Gain-of-Function Research",
        "type": "oversaw_funding",
        "tier": "credible",
        "desc": (
            "As NIAID director, oversaw the institute that funded gain-of-function research "
            "through EcoHealth Alliance. Testified before Congress (2024) regarding NIH's "
            "role. The Intercept obtained documents showing NIAID was aware of the research."
        ),
        "year_start": 2014,
        "sources": [537, 538, 551],
    },
    {
        "source": "FDA",
        "target": "Pfizer",
        "type": "regulates",
        "tier": "documented",
        "desc": (
            "FDA regulates Pfizer's drug approvals. Since PDUFA (1992), ~65% of FDA's drug "
            "review budget comes from industry user fees — the companies it regulates. "
            "27 of 55 FDA medical reviewers have moved to industry positions (POGO, 2016)."
        ),
        "sources": [530, 531, 532, 557, 574],
    },
    {
        "source": "FDA",
        "target": "Purdue Pharma",
        "type": "regulates",
        "tier": "documented",
        "desc": (
            "FDA approved OxyContin in 1995. The original FDA reviewer who approved the label "
            "claiming low addiction risk later joined Purdue Pharma. The approval and "
            "subsequent failure to intervene as the opioid crisis grew is a textbook case "
            "of regulatory capture."
        ),
        "year_start": 1995,
        "sources": [530, 531, 553, 555],
    },

    # ==== GATES / GLOBAL HEALTH GOVERNANCE ====
    {
        "source": "Bill Gates",
        "target": "Bill & Melinda Gates Foundation",
        "type": "co-founded",
        "tier": "documented",
        "desc": (
            "Co-founded the Foundation in 2000 with then-wife Melinda. Endowment exceeds "
            "$67 billion — the world's largest private foundation."
        ),
        "year_start": 2000,
        "sources": [541, 542],
    },
    {
        "source": "Bill & Melinda Gates Foundation",
        "target": "WHO",
        "type": "funds",
        "tier": "documented",
        "desc": (
            "Second-largest WHO contributor after Germany. Voluntary, often earmarked "
            "contributions give the Foundation outsized influence over WHO program priorities. "
            "This places a private foundation in a governance role over global public health."
        ),
        "sources": [540, 542, 543],
    },
    {
        "source": "Bill & Melinda Gates Foundation",
        "target": "GAVI",
        "type": "co-founded",
        "tier": "documented",
        "desc": (
            "Gates Foundation provided GAVI's founding $750 million grant at the 2000 World "
            "Economic Forum. Remains the dominant private funder of the vaccine alliance."
        ),
        "year_start": 2000,
        "sources": [542, 545],
    },
    {
        "source": "Bill & Melinda Gates Foundation",
        "target": "Pfizer",
        "type": "invested_in",
        "tier": "credible",
        "desc": (
            "Gates Foundation trust holds investments in pharmaceutical companies including "
            "Pfizer and BioNTech that benefit from the vaccine programs the Foundation funds. "
            "Documented by Columbia Journalism Review."
        ),
        "sources": [542, 544],
    },
    {
        "source": "Bill Gates",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Gates met with Epstein multiple times beginning in 2011 — after Epstein's 2008 "
            "sex trafficking conviction. Initially denied the meetings, later acknowledged them. "
            "Gates said he met Epstein for philanthropic discussions."
        ),
        "year_start": 2011,
        "sources": [541],
    },
    {
        "source": "GAVI",
        "target": "WHO",
        "type": "partnered_with",
        "tier": "documented",
        "desc": (
            "GAVI partners with WHO on vaccine procurement, distribution, and immunization "
            "programs in developing countries. WHO provides technical guidance; GAVI provides "
            "funding and procurement."
        ),
        "year_start": 2000,
        "sources": [539, 545],
    },

    # ==== SACKLER / OPIOID CRISIS ====
    {
        "source": "Arthur Sackler",
        "target": "Purdue Pharma",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Arthur Sackler pioneered the pharma advertising playbook that Purdue later used "
            "for OxyContin. His brothers (Mortimer and Raymond) and their heirs owned and "
            "controlled Purdue Pharma. Arthur died in 1987, before OxyContin's 1996 launch."
        ),
        "sources": [552, 553, 555],
    },
    {
        "source": "Purdue Pharma",
        "target": "FDA",
        "type": "influenced",
        "tier": "credible",
        "desc": (
            "Purdue's OxyContin label claiming 'less than 1%' addiction risk was approved by "
            "an FDA reviewer who subsequently took a position at Purdue. Company pleaded "
            "guilty to criminal charges in 2007 and 2020 for misbranding and fraud."
        ),
        "year_start": 1995,
        "sources": [553, 555, 556],
    },

    # ==== PFIZER ====
    {
        "source": "Pfizer",
        "target": "FDA",
        "type": "pays_user_fees",
        "tier": "documented",
        "desc": (
            "Pfizer pays PDUFA user fees that fund ~65% of FDA's drug review budget. "
            "In 2009, paid $2.3 billion — the largest health care fraud settlement in DOJ "
            "history — for illegal off-label promotion."
        ),
        "sources": [557, 558, 574],
    },

    # ==== MONSANTO / FOOD SYSTEM ====
    {
        "source": "Monsanto",
        "target": "FDA",
        "type": "regulated_by",
        "tier": "documented",
        "desc": (
            "FDA regulates Monsanto's GMO products and pesticide residue limits. Internal "
            "Monsanto documents ('Monsanto Papers') revealed company efforts to influence "
            "regulatory decisions and ghostwrite studies submitted to regulators."
        ),
        "sources": [559, 560],
    },

    # ==== MKULTRA SUBPROJECTS ====
    {
        "source": "Sidney Gottlieb",
        "target": "MKULTRA",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Directed MKULTRA from 1953-1973 as head of CIA's Technical Services Staff. "
            "Oversaw 149 sub-projects. Destroyed most records in 1973 before Congressional "
            "investigation."
        ),
        "year_start": 1953,
        "year_end": 1973,
        "sources": [562, 563],
    },
    {
        "source": "Sidney Gottlieb",
        "target": "CIA",
        "type": "served_in",
        "tier": "documented",
        "desc": (
            "CIA chemist, head of Technical Services Staff. Directed MKULTRA program and "
            "other CIA chemical/biological weapons programs."
        ),
        "year_start": 1951,
        "year_end": 1973,
        "sources": [562, 563],
    },
    {
        "source": "Donald Ewen Cameron",
        "target": "MKULTRA",
        "type": "conducted_experiments",
        "tier": "documented",
        "desc": (
            "Directed MKULTRA Subproject 68 at McGill's Allan Memorial Institute (1957-1964). "
            "Conducted psychic driving, drug-induced comas, and extreme electroshock on "
            "patients. Funded by CIA through front organizations. Canada settled with "
            "victims in 2023."
        ),
        "year_start": 1957,
        "year_end": 1964,
        "sources": [563, 564, 565, 566],
    },
    {
        "source": "Church Committee",
        "target": "MKULTRA",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Church Committee and subsequent Senate Select Committee on Intelligence hearings "
            "(1977) investigated MKULTRA. Gottlieb had destroyed most records in 1973, but "
            "a cache of financial documents survived and revealed the program's scope."
        ),
        "year_start": 1975,
        "year_end": 1977,
        "sources": [563],
    },

    # ==== HUMAN EXPERIMENTS ====
    {
        "source": "Tuskegee Syphilis Study",
        "target": "CDC",
        "type": "operated_by",
        "tier": "documented",
        "desc": (
            "Run by the U.S. Public Health Service (later absorbed into CDC). 399 Black men "
            "deliberately left untreated for syphilis from 1932 to 1972 — even after "
            "penicillin became available in 1947."
        ),
        "year_start": 1932,
        "year_end": 1972,
        "sources": [567, 568, 569],
    },
    {
        "source": "Guatemala Syphilis Experiments",
        "target": "NIH",
        "type": "funded_by",
        "tier": "documented",
        "desc": (
            "Funded by the U.S. Public Health Service and NIH. Researchers deliberately "
            "infected prisoners, soldiers, and psychiatric patients with STDs (1946-1948). "
            "At least 83 deaths. Obama apologized in 2010."
        ),
        "year_start": 1946,
        "year_end": 1948,
        "sources": [570, 571],
    },
    {
        "source": "Guatemala Syphilis Experiments",
        "target": "Tuskegee Syphilis Study",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Dr. John Charles Cutler led the Guatemala experiments and subsequently "
            "participated in the Tuskegee Study. Same institutional actors, same disregard "
            "for consent and human rights."
        ),
        "year_start": 1946,
        "sources": [568, 570, 571],
    },

    # ==== CROSS-LINKS TO EXISTING ENTITIES ====
    {
        "source": "Richard Helms",
        "target": "Sidney Gottlieb",
        "type": "supervised",
        "tier": "documented",
        "desc": (
            "As CIA Deputy Director for Plans and later CIA Director, Helms oversaw "
            "Gottlieb's MKULTRA program. Helms ordered the destruction of MKULTRA records "
            "in 1973 before leaving office."
        ),
        "year_start": 1953,
        "year_end": 1973,
        "sources": [562, 563],
    },
    {
        "source": "Jeffrey Epstein",
        "target": "NIH",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Epstein funded academic research at MIT Media Lab, Harvard, and other institutions "
            "that intersect with NIH-funded research networks. His financial relationships "
            "with prominent scientists illustrate how private funding can create conflicts "
            "within publicly funded research institutions."
        ),
        "sources": [575],
    },

    # ==== SUPPRESSED HEALING ====
    {
        "source": "Royal Raymond Rife",
        "target": "FDA",
        "type": "suppressed_by",
        "tier": "inference",
        "desc": (
            "Rife's frequency therapy devices were reportedly confiscated and his research "
            "suppressed by the medical establishment in the late 1930s-1940s. The AMA under "
            "Morris Fishbein is alleged to have coordinated the suppression. Scientific "
            "establishment classifies his claims as unproven; supporters allege systematic "
            "elimination of evidence."
        ),
        "year_start": 1939,
        "sources": [572, 573],
    },
]

# ============================================================
# ENTITY_SOURCES — link entities to their primary sources
# ============================================================

ENTITY_SOURCES = {
    # People
    "Anthony Fauci": [536, 537, 538, 551],
    "Bill Gates": [541, 542, 543, 544],
    "Peter Daszak": [546, 547, 548, 551],
    "Ralph Baric": [549, 550],
    "Arthur Sackler": [552, 553, 555],
    "Sidney Gottlieb": [562, 563],
    "Donald Ewen Cameron": [564, 565, 566],
    "Royal Raymond Rife": [572, 573],
    # Organizations / Agencies
    "FDA": [530, 531, 532, 574],
    "CDC": [533, 534, 567],
    "NIH": [535, 537, 548],
    "WHO": [539, 540],
    "Bill & Melinda Gates Foundation": [542, 543, 544],
    "GAVI": [545],
    "EcoHealth Alliance": [546, 547, 548, 551],
    "Purdue Pharma": [553, 554, 555, 556],
    "Pfizer": [557, 558],
    "Monsanto": [559, 560, 561],
    # Programs / Experiments / Events
    "Tuskegee Syphilis Study": [567, 568, 569],
    "Guatemala Syphilis Experiments": [570, 571],
    "Gain-of-Function Research": [537, 549, 550, 551],
}
