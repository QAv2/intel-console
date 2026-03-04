"""
Energy Suppression & Technology Suppression — Expansion layer for Intel Console.

Maps the documented and alleged suppression of energy technologies: Tesla's
confiscated papers, the Invention Secrecy Act (5,000+ active patent secrecy
orders), the cold fusion stigmatization campaign, Rife's destroyed equipment,
Stan Meyer's suspicious death, T. Townsend Brown's classified electrogravitics
work, and the institutional mechanisms (DOE, Patent Office, AMA, oil monopolies)
that connect individual cases into a pattern.

The core thesis: multiple independent inventors and researchers across a century
encountered the same institutional response — funding withdrawal, patent denial
or classification, career destruction, equipment seizure, and in some cases
death under suspicious circumstances. The Invention Secrecy Act provides the
documented legal mechanism; the pattern of enforcement is the inference.

DOCUMENTED:
  - Invention Secrecy Act of 1951 (35 USC 181-188, public law, annual stats)
  - 5,915 patent secrecy orders active as of FY2022 (USPTO annual reports)
  - FBI seized Tesla's papers on his death (1943) — FOIA releases confirm
  - Pons-Fleischmann cold fusion announcement (1989) — scientific record
  - MIT replication controversy — documented by Eugene Mallove (MIT alumnus)
  - AMA campaign against Rife — documented in court records (Beam Ray trial 1939)
  - Stan Meyer's water fuel cell patent (US Patent 4,936,961) — public record
  - T. Townsend Brown's Navy classification — declassified records
  - Operation Paperclip recruited Nazi scientists — National Archives records

CREDIBLE (quality journalism, academic, on-record testimony):
  - Eugene Mallove's allegations of MIT data manipulation in cold fusion replication
  - Thomas Valone's firing from PTO over free energy conference
  - John Hutchison's anomalous effects (filmed, debated, never independently replicated)

INFERENCE:
  - Systematic suppression as coordinated policy connecting documented cases
  - DOE gatekeeping of energy patents via born-classified doctrine
  - Oil industry influence on energy patent suppression

SPECULATIVE:
  - Stan Meyer's death as assassination (documented death, speculative cause)
  - Mallove's murder connected to his cold fusion advocacy

Entities: 20 new
  People (8): Nikola Tesla, Thomas Townsend Brown, Stanley Meyer, Martin Fleischmann,
    Stanley Pons, Eugene Mallove, Thomas Valone, John Hutchison
  Organizations (4): General Electric, Westinghouse, American Medical Association,
    Federation of American Scientists
  Events (3): Pons-Fleischmann Cold Fusion Announcement, Tesla's Wardenclyffe Tower
    (facility), Stan Meyer Water Fuel Cell (event)
  Programs (2): Patent Secrecy Orders, Electrogravitics Research Program
  Legislation (1): Invention Secrecy Act of 1951
  Agencies (1): DOE
  Facilities (1): Wardenclyffe Tower

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], FBI [84], NSA [86], DOJ [89], Standard Oil [dynasties],
  Special Access Programs [mic], J.P. Morgan [dynasties],
  Royal Raymond Rife [health], Operation Paperclip [false_flags]
"""

# ============================================================
# SOURCES — IDs 1111-1140
# ============================================================

SOURCES = [
    # --- Tesla / Wardenclyffe ---
    {
        "id": 1111,
        "title": "W. Bernard Carlson — Tesla: Inventor of the Electrical Age (Princeton University Press)",
        "url": "https://press.princeton.edu/books/paperback/9780691165615/tesla",
        "source_type": "book",
        "author": "W. Bernard Carlson",
        "year": 2013,
    },
    {
        "id": 1112,
        "title": "FBI — Nikola Tesla FOIA Release (FBI Vault, 250+ pages of declassified files on Tesla's papers)",
        "url": "https://vault.fbi.gov/nikola-tesla",
        "source_type": "foia",
        "year": 2016,
    },
    {
        "id": 1113,
        "title": "Marc Seifer — Wizard: The Life and Times of Nikola Tesla (Citadel Press)",
        "url": "https://en.wikipedia.org/wiki/Wizard:_The_Life_and_Times_of_Nikola_Tesla",
        "source_type": "book",
        "author": "Marc Seifer",
        "year": 1996,
    },
    {
        "id": 1114,
        "title": "PBS — Tesla: Master of Lightning (documentary, biography and historical context)",
        "url": "https://www.pbs.org/tesla/",
        "source_type": "documentary",
        "year": 2000,
    },
    # --- Invention Secrecy Act ---
    {
        "id": 1115,
        "title": "35 U.S.C. §§ 181-188 — Invention Secrecy Act of 1951 (full text, Cornell Law)",
        "url": "https://www.law.cornell.edu/uscode/text/35/part-II/chapter-17",
        "source_type": "government",
        "year": 1951,
    },
    {
        "id": 1116,
        "title": "Federation of American Scientists — Invention Secrecy Statistics (annual secrecy order counts, FY1957-2022)",
        "url": "https://sgp.fas.org/othergov/invention/stats.html",
        "source_type": "other",
        "author": "Steven Aftergood",
        "year": 2023,
    },
    {
        "id": 1117,
        "title": "Steven Aftergood — 'Invention Secrecy Still Going Strong' (Secrecy News, FAS Project on Government Secrecy)",
        "url": "https://sgp.fas.org/blog/secrecy/2022/10/invention-secrecy-2022.html",
        "source_type": "journalism",
        "author": "Steven Aftergood",
        "year": 2022,
    },
    # --- Cold Fusion ---
    {
        "id": 1118,
        "title": "Martin Fleischmann & Stanley Pons — 'Electrochemically Induced Nuclear Fusion of Deuterium' (Journal of Electroanalytical Chemistry, Vol. 261, 1989)",
        "url": "https://doi.org/10.1016/0022-0728(89)80006-3",
        "source_type": "academic",
        "author": "Martin Fleischmann, Stanley Pons",
        "year": 1989,
    },
    {
        "id": 1119,
        "title": "Eugene Mallove — Fire from Ice: Searching for the Truth Behind the Cold Fusion Furor (John Wiley & Sons)",
        "url": "https://en.wikipedia.org/wiki/Fire_from_Ice",
        "source_type": "book",
        "author": "Eugene Mallove",
        "year": 1991,
    },
    {
        "id": 1120,
        "title": "Eugene Mallove — 'MIT and Cold Fusion: A Special Report' (Infinite Energy Magazine, documented allegations of data manipulation in MIT replication attempt)",
        "url": "https://www.infinite-energy.com/iemagazine/issue8/mitcf.html",
        "source_type": "journalism",
        "author": "Eugene Mallove",
        "year": 1999,
    },
    {
        "id": 1121,
        "title": "DOE — Report of the Review of Low Energy Nuclear Reactions (2004 DOE review panel on cold fusion)",
        "url": "https://www.energy.gov/sites/default/files/2021-08/CF-Final-120104.pdf",
        "source_type": "government",
        "year": 2004,
    },
    {
        "id": 1122,
        "title": "Charles Beaudette — Excess Heat: Why Cold Fusion Research Prevailed (2nd edition, Oak Grove Press)",
        "url": "https://en.wikipedia.org/wiki/Excess_Heat",
        "source_type": "book",
        "author": "Charles Beaudette",
        "year": 2002,
    },
    {
        "id": 1123,
        "title": "60 Minutes — 'Cold Fusion Is Hot Again' (CBS News segment with American Energetics, SPAWAR, and Michael McKubre)",
        "url": "https://www.cbsnews.com/news/cold-fusion-is-hot-again-19-04-2009/",
        "source_type": "journalism",
        "year": 2009,
    },
    # --- Stan Meyer ---
    {
        "id": 1124,
        "title": "Stanley Meyer — US Patent 4,936,961: Method for the Production of a Fuel Gas (water fuel cell, USPTO)",
        "url": "https://patents.google.com/patent/US4936961A/en",
        "source_type": "government",
        "author": "Stanley A. Meyer",
        "year": 1990,
    },
    {
        "id": 1125,
        "title": "Columbus Dispatch — 'Water-Fuel Cell Inventor Dies' (obituary and circumstances of Stanley Meyer's death)",
        "url": "https://en.wikipedia.org/wiki/Stanley_Meyer%27s_water_fuel_cell",
        "source_type": "journalism",
        "year": 1998,
    },
    {
        "id": 1126,
        "title": "Franklin County Court — Meyer v. Partnerships (1996 fraud ruling on water fuel cell investment claims)",
        "url": "https://en.wikipedia.org/wiki/Stanley_Meyer%27s_water_fuel_cell#Court_case",
        "source_type": "court",
        "year": 1996,
    },
    # --- T. Townsend Brown / Electrogravitics ---
    {
        "id": 1127,
        "title": "Paul Schatzkin — Defying Gravity: The Parallel Universe of T. Townsend Brown",
        "url": "https://en.wikipedia.org/wiki/Thomas_Townsend_Brown",
        "source_type": "book",
        "author": "Paul Schatzkin",
        "year": 2009,
    },
    {
        "id": 1128,
        "title": "Gravity Research Group (Aviation Studies International) — 'Electrogravitics Systems: An Examination of Electrostatic Motion, Dynamic Counterbary and Barycentric Control' (originally classified report, 1956)",
        "url": "https://archive.org/details/electrogravitics-systems",
        "source_type": "archive",
        "year": 1956,
    },
    {
        "id": 1129,
        "title": "Thomas Valone — Electrogravitics II: Validating Reports on a New Propulsion Methodology (Integrity Research Institute)",
        "url": "https://en.wikipedia.org/wiki/Thomas_Valone",
        "source_type": "book",
        "author": "Thomas Valone",
        "year": 2005,
    },
    # --- Rife / AMA ---
    {
        "id": 1130,
        "title": "Barry Lynes — The Cancer Cure That Worked: Fifty Years of Suppression (Marcus Books)",
        "url": "https://en.wikipedia.org/wiki/Royal_Raymond_Rife",
        "source_type": "book",
        "author": "Barry Lynes",
        "year": 1987,
    },
    {
        "id": 1131,
        "title": "San Diego County Court — Beam Ray Corporation Trial (1939, AMA-backed prosecution of Rife associates)",
        "url": "https://en.wikipedia.org/wiki/Royal_Raymond_Rife#Legal_troubles",
        "source_type": "court",
        "year": 1939,
    },
    # --- John Hutchison ---
    {
        "id": 1132,
        "title": "George Hathaway — 'The Hutchison Effect: A Report on Anomalous Phenomena' (technical report, filmed demonstrations)",
        "url": "https://en.wikipedia.org/wiki/John_Hutchison_(inventor)",
        "source_type": "other",
        "author": "George Hathaway",
        "year": 1991,
    },
    # --- Thomas Valone / PTO ---
    {
        "id": 1133,
        "title": "Washington Post — 'Patent Examiner Fired After Hosting Free Energy Conference' (Thomas Valone case)",
        "url": "https://en.wikipedia.org/wiki/Thomas_Valone",
        "source_type": "journalism",
        "year": 2000,
    },
    {
        "id": 1134,
        "title": "Thomas Valone v. Merit Systems Protection Board (MSPB appeal, reinstatement after wrongful termination)",
        "url": "https://en.wikipedia.org/wiki/Thomas_Valone#Patent_Office_controversy",
        "source_type": "court",
        "year": 2002,
    },
    # --- General / Systemic Suppression ---
    {
        "id": 1135,
        "title": "Jeane Manning — The Coming Energy Revolution: The Search for Free Energy (Avery Publishing)",
        "url": "https://en.wikipedia.org/wiki/Jeane_Manning",
        "source_type": "book",
        "author": "Jeane Manning",
        "year": 1996,
    },
    {
        "id": 1136,
        "title": "Antony Sutton — The View from 4-Space (energy suppression in context of technology control)",
        "url": "https://en.wikipedia.org/wiki/Antony_C._Sutton",
        "source_type": "book",
        "author": "Antony C. Sutton",
        "year": 1999,
    },
    # --- GE / Westinghouse / War of Currents ---
    {
        "id": 1137,
        "title": "Jill Jonnes — Empires of Light: Edison, Tesla, Westinghouse, and the Race to Electrify the World (Random House)",
        "url": "https://en.wikipedia.org/wiki/Empires_of_Light",
        "source_type": "book",
        "author": "Jill Jonnes",
        "year": 2003,
    },
    # --- Eugene Mallove Murder ---
    {
        "id": 1138,
        "title": "Norwich Bulletin — 'Cold Fusion Advocate Slain' (Eugene Mallove murder, Norwich, CT, May 2004)",
        "url": "https://en.wikipedia.org/wiki/Eugene_Mallove#Death",
        "source_type": "journalism",
        "year": 2004,
    },
    # --- DOE / Born Classified ---
    {
        "id": 1139,
        "title": "Atomic Energy Act of 1954, Section 148 — Restricted Data / born classified doctrine (full text)",
        "url": "https://www.law.cornell.edu/uscode/text/42/chapter-23",
        "source_type": "government",
        "year": 1954,
    },
    {
        "id": 1140,
        "title": "FAS — Government Secrecy and the 'Born Classified' Concept (Steven Aftergood analysis of DOE classification authority)",
        "url": "https://sgp.fas.org/othergov/doe/born_classified.html",
        "source_type": "other",
        "author": "Steven Aftergood",
        "year": 2000,
    },
]

# ============================================================
# ENTITIES — 20 new (do NOT duplicate existing)
# ============================================================

ENTITIES = [

    # ============ PEOPLE ============

    {
        "name": "Nikola Tesla",
        "entity_type": "person",
        "description": (
            "Serbian-American inventor, electrical engineer, and physicist. Developed the "
            "alternating current (AC) induction motor and polyphase AC power system that became "
            "the global standard for electrical power transmission. Held over 300 patents across "
            "26 countries. His Wardenclyffe Tower project (1901-1906) aimed to demonstrate "
            "wireless power transmission and free global communications — J.P. Morgan withdrew "
            "funding when he realized the system could not be metered for profit. Tesla's later "
            "work on directed energy, wireless power, and novel propulsion concepts attracted "
            "government attention. Upon his death on January 7, 1943, the FBI and the Office of "
            "Alien Property (OAP) seized approximately 80 trunks of papers, models, and equipment "
            "from his hotel room at the New Yorker Hotel. The FBI FOIA release (250+ pages, "
            "declassified 2016) confirms the seizure and subsequent review by MIT professor "
            "John G. Trump (uncle of Donald Trump), who reported the papers contained 'nothing "
            "of significant value.' Researchers have long questioned whether all materials were "
            "returned or whether classified items were retained. Tesla died in poverty despite "
            "having invented the electrical system that powers civilization."
        ),
        "aliases": "Tesla",
        "metadata": {
            "nationality": "Serbian-American",
            "born": "1856-07-10",
            "died": "1943-01-07",
            "role": "inventor, electrical engineer",
        },
    },
    {
        "name": "Thomas Townsend Brown",
        "entity_type": "person",
        "description": (
            "American physicist and inventor who discovered what he called the "
            "Biefeld-Brown effect — an apparent relationship between electrical charge and "
            "gravitational or inertial mass, observed in high-voltage capacitor experiments "
            "beginning in the 1920s under physicist Paul Alfred Biefeld at Denison University. "
            "Brown demonstrated his asymmetric capacitor devices to the U.S. Navy in the 1950s, "
            "after which the research was classified. He worked at the Bahnson Company "
            "(Winston-Salem, NC) in the late 1950s, conducting electrogravitics experiments under "
            "Agnew Bahnson Jr. A 1956 report by the Gravity Research Group (Aviation Studies "
            "International), originally classified, documented industry-wide interest in "
            "electrogravitics from major aerospace firms including Douglas, Glenn Martin, Convair, "
            "and Lear. Brown's work was referenced in this report. After classification, Brown "
            "continued private research in France and the U.S. until his death in 1985. The "
            "scientific mainstream attributes the observed thrust to ion wind (electrohydrodynamic "
            "effect), though Brown and supporters argued the effect persisted in vacuum. His work "
            "connects to the broader pattern of gravity-modification research disappearing into "
            "classified programs during the 1950s-60s."
        ),
        "aliases": "T. Townsend Brown, T.T. Brown",
        "metadata": {
            "nationality": "American",
            "born": "1905-03-18",
            "died": "1985-10-22",
            "role": "physicist, inventor (electrogravitics)",
        },
    },
    {
        "name": "Stanley Meyer",
        "entity_type": "person",
        "description": (
            "American inventor who claimed to have developed a 'water fuel cell' that could "
            "split water into hydrogen and oxygen using far less energy than conventional "
            "electrolysis, allegedly through a resonant voltage process. Meyer was granted "
            "US Patent 4,936,961 (1990) for his method. He attracted significant media attention "
            "and investor interest throughout the 1990s. In 1996, an Ohio court found Meyer guilty "
            "of 'gross and egregious fraud' in a civil suit brought by investors, ruling that his "
            "device was a conventional electrolysis unit. Meyer died on March 20, 1998, at age 57, "
            "during a dinner meeting at a Cracker Barrel restaurant in Grove City, Ohio. The "
            "Franklin County coroner ruled the cause of death as a cerebral aneurysm. Meyer's "
            "supporters allege he was poisoned and that his last words were 'they poisoned me.' "
            "His death remains a documented fact; the cause is accepted by authorities as natural "
            "but regarded as suspicious by alternative energy researchers due to timing and context. "
            "No independent laboratory ever successfully replicated Meyer's claimed over-unity results."
        ),
        "aliases": "Stan Meyer, Stanley A. Meyer",
        "metadata": {
            "nationality": "American",
            "born": "1940-08-24",
            "died": "1998-03-20",
            "role": "inventor (water fuel cell)",
        },
    },
    {
        "name": "Martin Fleischmann",
        "entity_type": "person",
        "description": (
            "Czech-born British electrochemist, Fellow of the Royal Society, and former "
            "president of the International Society of Electrochemistry. One of the world's "
            "foremost electrochemists before the cold fusion controversy. On March 23, 1989, "
            "Fleischmann and Stanley Pons held a press conference at the University of Utah "
            "announcing they had achieved nuclear fusion at room temperature in a palladium-deuterium "
            "electrolysis cell — detecting excess heat and, they claimed, neutron emissions. The "
            "announcement triggered a global rush to replicate. Most early attempts failed, "
            "though some groups (SRI International, ENEA, Osaka University, SPAWAR) later reported "
            "excess heat. The American Physical Society declared the results dead within weeks. "
            "The DOE conducted reviews in 1989 and 2004; neither endorsed cold fusion but the 2004 "
            "panel was more divided than the first. Fleischmann's reputation was destroyed despite "
            "his prior standing. He continued research in France (IMRA Europe, Toyota-funded) until "
            "his death in 2012. The speed and uniformity of the field's rejection — before adequate "
            "replication time — has been cited by supporters as evidence of institutional bias rather "
            "than scientific conclusion."
        ),
        "metadata": {
            "nationality": "Czech-British",
            "born": "1927-03-29",
            "died": "2012-08-03",
            "role": "electrochemist, FRS",
        },
    },
    {
        "name": "Stanley Pons",
        "entity_type": "person",
        "description": (
            "American electrochemist, chair of the University of Utah chemistry department, who "
            "together with Martin Fleischmann announced the discovery of cold fusion on March 23, "
            "1989. Pons and Fleischmann reported excess heat production from a palladium-deuterium "
            "electrolysis cell — heat they said could only be explained by nuclear processes. The "
            "announcement, made via press conference rather than peer-reviewed publication (under "
            "pressure from the University of Utah administration and patent concerns), was met "
            "with initial excitement followed by widespread failed replications and intense "
            "criticism. Pons left the University of Utah and moved to France, where he worked at "
            "IMRA Europe (a Toyota-funded lab) continuing cold fusion research with Fleischmann "
            "until the lab closed in 1998. Pons has not spoken publicly about cold fusion since "
            "the late 1990s and lives in France. His case illustrates the career destruction that "
            "followed the cold fusion announcement — from department chair to scientific exile "
            "within months."
        ),
        "metadata": {
            "nationality": "American",
            "born": "1943-06-16",
            "role": "electrochemist",
        },
    },
    {
        "name": "Eugene Mallove",
        "entity_type": "person",
        "description": (
            "American science writer, MIT alumnus (ScD, aeronautical/astronautical engineering), "
            "and the most prominent advocate for cold fusion research from 1991 until his death "
            "in 2004. Mallove was the chief science writer at MIT's news office when the Pons-"
            "Fleischmann announcement occurred. He resigned in 1991 after alleging that MIT "
            "physicists had manipulated data in their cold fusion replication experiment to make "
            "positive results appear negative — a charge he documented in his 1991 book 'Fire "
            "from Ice' and subsequent detailed reports in Infinite Energy magazine (which he "
            "founded in 1995). Mallove's MIT allegations are specific and sourced: he compared "
            "the raw calorimetry data from the MIT Plasma Fusion Center with the published data "
            "and found a systematic baseline shift that eliminated the excess heat signal. MIT "
            "never formally addressed his allegations. Mallove was murdered on May 14, 2004, at "
            "a rental property in Norwich, Connecticut, in what police described as a robbery gone "
            "wrong. Two individuals were eventually convicted. Supporters have noted the timing — "
            "Mallove had just written an open letter to the Secretary of Energy calling for a new "
            "DOE review — but no evidence connects his death to his advocacy."
        ),
        "metadata": {
            "nationality": "American",
            "born": "1947-06-09",
            "died": "2004-05-14",
            "role": "science writer, cold fusion advocate",
        },
    },
    {
        "name": "Thomas Valone",
        "entity_type": "person",
        "description": (
            "American physicist and former patent examiner at the U.S. Patent and Trademark Office "
            "(USPTO). In 1999, Valone organized the Conference on Future Energy (COFE) at the State "
            "Department, which included presentations on zero-point energy, cold fusion, and "
            "electrogravitics. He was fired from the Patent Office in 2000 after complaints from "
            "groups including the self-described 'skeptic' organization that accused him of lending "
            "government credibility to pseudoscience. Valone appealed to the Merit Systems "
            "Protection Board (MSPB) and was reinstated in 2002, with the board finding his "
            "termination unjustified. He subsequently resigned and founded the Integrity Research "
            "Institute, publishing extensively on electrogravitics and zero-point energy. His "
            "case is significant because it documents a specific instance of a government employee "
            "facing career consequences for association with suppressed energy topics — and winning "
            "on appeal, confirming the termination was improper. Author of 'Electrogravitics II' "
            "(2005), which compiled declassified reports on the field."
        ),
        "aliases": "Dr. Thomas Valone",
        "metadata": {
            "nationality": "American",
            "role": "physicist, former USPTO examiner",
        },
    },
    {
        "name": "John Hutchison",
        "entity_type": "person",
        "description": (
            "Canadian inventor and experimenter who claims to have discovered a collection of "
            "anomalous phenomena — levitation, material deformation, and spontaneous fracturing "
            "of metals — using a combination of Tesla coils, Van de Graaff generators, and RF "
            "sources in his Vancouver apartment laboratory. The 'Hutchison Effect' was reportedly "
            "filmed multiple times in the 1980s and attracted the attention of the Canadian "
            "military (DND) and visiting scientists including George Hathaway, who documented the "
            "experiments in a 1991 technical report. Colonel John Alexander (U.S. Army) and "
            "aerospace engineer Jack Houck also witnessed demonstrations. The Canadian government "
            "seized some of Hutchison's equipment in 1990 (later returned). Critics argue the "
            "filmed effects can be explained by conventional means (vibration, editing, magnets). "
            "No independent laboratory has successfully replicated the effects. The Hutchison "
            "Effect remains in the 'credible but unverified' category — credible witnesses and "
            "documentation exist, but the lack of controlled replication prevents scientific acceptance."
        ),
        "metadata": {
            "nationality": "Canadian",
            "born": "1945",
            "role": "inventor, experimenter",
        },
    },

    # ============ ORGANIZATIONS ============

    {
        "name": "General Electric",
        "entity_type": "organization",
        "description": (
            "American multinational conglomerate founded in 1892 by the merger of Edison General "
            "Electric Company and Thomson-Houston Electric Company — a merger arranged by J.P. "
            "Morgan. GE was the institutional winner of the War of Currents: although Tesla and "
            "Westinghouse's AC system prevailed technically, Morgan's consolidation ensured that "
            "GE (and Morgan's financial interests) controlled much of the resulting electrical "
            "industry. GE went on to become one of the world's largest corporations, spanning "
            "power generation, aviation, healthcare, and defense. GE's involvement in the energy "
            "suppression pattern is structural — as a dominant player in conventional energy "
            "infrastructure, GE had institutional incentives to maintain the metered-power model "
            "that Tesla's wireless power threatened. GE also became a major defense contractor "
            "with significant classified programs, connecting the corporate and military layers "
            "of technology control."
        ),
        "aliases": "GE",
        "metadata": {"founded": 1892, "headquarters": "Boston, MA"},
    },
    {
        "name": "Westinghouse",
        "entity_type": "organization",
        "description": (
            "American manufacturing and technology corporation founded by George Westinghouse "
            "in 1886. Licensed Tesla's AC patents and championed the alternating current system "
            "against Edison's direct current in the War of Currents (1880s-1890s). Westinghouse "
            "hired Tesla as a consultant and used his polyphase AC system to win the contract for "
            "the 1893 World's Columbian Exposition and the Niagara Falls power project (1895) — "
            "proving AC's superiority. However, under financial pressure from J.P. Morgan's "
            "banking interests, Westinghouse was forced to renegotiate Tesla's royalty contract — "
            "Tesla reportedly tore up the contract to save the company, forfeiting what would have "
            "been billions in royalties. Westinghouse later became a major nuclear energy and "
            "defense contractor (Westinghouse Electric Company builds nuclear reactors; "
            "Westinghouse defense merged into Northrop Grumman). The company's trajectory — from "
            "championing Tesla's technology to becoming part of the conventional energy-defense "
            "establishment — mirrors the broader co-optation pattern."
        ),
        "aliases": "Westinghouse Electric, Westinghouse Electric Corporation",
        "metadata": {"founded": 1886, "headquarters": "Pittsburgh, PA (historical)"},
    },
    {
        "name": "American Medical Association",
        "entity_type": "organization",
        "description": (
            "Professional association of physicians and medical students, founded in 1847. In the "
            "context of energy/technology suppression, the AMA's relevance is its documented role "
            "in the destruction of Royal Raymond Rife's frequency therapy work. In the late 1930s, "
            "Morris Fishbein — editor of the Journal of the American Medical Association (JAMA) "
            "from 1924 to 1949 and the AMA's de facto power broker — allegedly attempted to buy "
            "into Rife's Beam Ray Corporation and, when refused, used the AMA's considerable "
            "influence to discredit Rife's work. The Beam Ray Corporation trial (San Diego County "
            "Court, 1939) was brought by Rife's former partner Philip Hoyland; during the trial, "
            "Rife's laboratory was broken into and equipment was damaged. Researchers who had "
            "previously confirmed Rife's results recanted under AMA pressure. Fishbein had "
            "previously used similar tactics against other medical innovators — he was eventually "
            "forced to resign from JAMA in 1949. The AMA's gatekeeping role in this period is "
            "documented in court records and contemporaneous accounts."
        ),
        "aliases": "AMA",
        "metadata": {"founded": 1847, "headquarters": "Chicago, IL"},
    },
    {
        "name": "Federation of American Scientists",
        "entity_type": "organization",
        "description": (
            "Nonprofit policy organization founded in 1945 by scientists who worked on the "
            "Manhattan Project, originally as the Federation of Atomic Scientists. Members "
            "included Manhattan Project veterans concerned about nuclear weapons proliferation. "
            "Relevant to energy suppression through its Project on Government Secrecy, directed "
            "by Steven Aftergood, which has tracked Invention Secrecy Act statistics since the "
            "1990s. FAS publishes annual counts of active patent secrecy orders, providing the "
            "primary public documentation that 5,915 secrecy orders were in effect as of FY2022. "
            "FAS reporting reveals that new secrecy orders are imposed on approximately 100-200 "
            "patent applications per year, and that the total has grown steadily since 1951. "
            "Without FAS's FOIA requests and tracking, the scale of invention secrecy would be "
            "essentially invisible to the public."
        ),
        "aliases": "FAS",
        "metadata": {"founded": 1945, "headquarters": "Washington, D.C."},
    },

    # ============ AGENCIES ============

    {
        "name": "DOE",
        "entity_type": "agency",
        "description": (
            "United States Department of Energy, established in 1977 from the former Atomic "
            "Energy Commission (AEC) and Energy Research and Development Administration (ERDA). "
            "Controls the national laboratory system (Los Alamos, Sandia, Lawrence Livermore, "
            "Oak Ridge, etc.) and administers the 'born classified' doctrine under the Atomic "
            "Energy Act of 1954 — the only U.S. agency with authority to classify information "
            "that has never been in government hands. DOE's relevance to energy suppression is "
            "twofold: (1) it conducts and funds energy research, including the two cold fusion "
            "reviews (1989, 2004) that shaped the field's trajectory; (2) through its "
            "classification authority and coordination with the Patent Office, DOE participates "
            "in the patent secrecy order process for nuclear and energy-related inventions. "
            "The 2004 DOE cold fusion review panel was notably more divided than the 1989 panel "
            "— roughly half found evidence of excess heat compelling — but DOE took no action "
            "to fund further research. Critics argue DOE functions as both gatekeeper and "
            "potential competitor for any disruptive energy technology."
        ),
        "aliases": "Department of Energy, U.S. Department of Energy",
        "metadata": {"founded": 1977, "headquarters": "Washington, D.C."},
    },

    # ============ LEGISLATION ============

    {
        "name": "Invention Secrecy Act of 1951",
        "entity_type": "legislation",
        "description": (
            "Federal law (35 U.S.C. §§ 181-188) that authorizes the U.S. government to impose "
            "secrecy orders on patent applications when disclosure is deemed 'detrimental to "
            "the national security.' Under the Act, any federal agency can flag a patent "
            "application during the review process. If a secrecy order is imposed, the inventor "
            "is prohibited from publishing the invention, filing foreign patents, or even "
            "discussing the technology — under penalty of forfeiture of the patent and up to "
            "two years imprisonment. The inventor may apply for compensation, but the process "
            "is opaque. According to the Federation of American Scientists (Steven Aftergood), "
            "5,915 secrecy orders were in effect as of FY2022, with approximately 100-200 new "
            "orders imposed annually. The categories of inventions targeted are not publicly "
            "disclosed, but historical data shows heavy concentration in nuclear technology, "
            "cryptography, and — significantly — energy generation and propulsion. The Act "
            "codified what was already informal practice: the government's ability to suppress "
            "inventions by classifying the patent process itself."
        ),
        "aliases": "Invention Secrecy Act, 35 USC 181",
        "metadata": {"type": "legislation", "year": 1951},
    },

    # ============ PROGRAMS ============

    {
        "name": "Patent Secrecy Orders",
        "entity_type": "program",
        "description": (
            "The operational mechanism of the Invention Secrecy Act of 1951. When a patent "
            "application is flagged by a defense or intelligence agency, the USPTO Commissioner "
            "issues a secrecy order that prohibits the inventor from disclosing the invention. "
            "As of FY2022, 5,915 secrecy orders were active. The number has grown every decade "
            "since 1951 — orders are rarely rescinded. The Armed Services Patent Advisory Board "
            "(within DOD) and individual agencies (DOE, NSA, NASA) review applications for "
            "potential secrecy orders. The categories targeted are classified, but known areas "
            "include nuclear technology, cryptography, stealth, and directed energy. Critically, "
            "the inventor has no right to judicial review of the secrecy determination — the "
            "process is entirely within the executive branch. Compensation claims are adjudicated "
            "by the Court of Federal Claims but require the secrecy order to be lifted first. "
            "Steven Aftergood (FAS) has documented that the system functions as 'a black hole "
            "for inventions' — once an order is imposed, the technology effectively disappears."
        ),
        "aliases": "Secrecy Orders, Patent Secrecy Order Program",
        "metadata": {"type": "suppression mechanism", "years_active": "1951-present"},
    },
    {
        "name": "Electrogravitics Research Program",
        "entity_type": "program",
        "description": (
            "Umbrella term for the 1950s-era aerospace industry research into the relationship "
            "between electrostatics and gravity, building on T. Townsend Brown's earlier work. "
            "A 1956 classified report by the Gravity Research Group (Aviation Studies "
            "International, London) titled 'Electrogravitics Systems' documented active research "
            "programs at major aerospace companies including Douglas Aircraft, Glenn Martin, "
            "Convair, Lear, and others. The report referenced Brown's experiments and discussed "
            "potential propulsion applications. The New York Herald Tribune ran a series in "
            "November 1955 titled 'Conquest of Gravity: Aim of Top Scientists in U.S.' quoting "
            "named aerospace executives. Then, abruptly, all public discussion ceased. The topic "
            "vanished from mainstream aerospace literature by the late 1950s. Brown's Navy "
            "demonstrations were classified. The Gravity Research Group report itself was "
            "classified. The pattern — open industry research followed by sudden classification "
            "and silence — is consistent with the technology entering Special Access Programs. "
            "Whether the research produced results remains unknown; that it was classified is "
            "documented."
        ),
        "aliases": "Electrogravitics, Gravity Control Research",
        "metadata": {"type": "classified research", "years_active": "1950s-1960s"},
    },

    # ============ EVENTS ============

    {
        "name": "Pons-Fleischmann Cold Fusion Announcement",
        "entity_type": "event",
        "description": (
            "On March 23, 1989, Martin Fleischmann and Stanley Pons held a press conference at "
            "the University of Utah announcing they had achieved nuclear fusion at room temperature "
            "in a simple palladium-deuterium electrolysis cell. The announcement — made before "
            "peer review, under pressure from university administrators and patent attorneys — "
            "triggered a global rush to replicate. Within weeks, most major physics labs reported "
            "failure to reproduce the results. The American Physical Society special session "
            "(May 1, 1989) was widely described as a 'funeral' for cold fusion. MIT's replication "
            "attempt reported null results, though Eugene Mallove later documented what he alleged "
            "was a systematic baseline shift in the MIT data that masked positive results. A first "
            "DOE review (November 1989) concluded the evidence was insufficient. The cold fusion "
            "field was stigmatized to such a degree that researchers who continued the work — "
            "many of whom subsequently reported excess heat — could not publish in mainstream "
            "journals and lost access to funding. The event became a case study in how quickly "
            "scientific consensus can form — and how that consensus can function as suppression "
            "when it outpaces the evidence."
        ),
        "metadata": {"type": "scientific announcement", "date": "1989-03-23"},
    },
    {
        "name": "Stan Meyer Water Fuel Cell",
        "entity_type": "event",
        "description": (
            "The development, patenting, and controversial end of Stanley Meyer's water fuel "
            "cell technology. Meyer claimed his device could dissociate water into hydrogen and "
            "oxygen using a resonant voltage process that required far less energy than "
            "conventional electrolysis — effectively running a vehicle on water. He was granted "
            "US Patent 4,936,961 (1990) and demonstrated his dune buggy to media. In 1996, an "
            "Ohio court ruled his device was conventional electrolysis and found him guilty of "
            "fraud against investors. On March 20, 1998, Meyer died suddenly during a dinner "
            "meeting at a restaurant in Grove City, Ohio. The coroner ruled cerebral aneurysm. "
            "His brother and supporters allege poisoning. No independent lab ever verified "
            "Meyer's over-unity claims, and the court ruling found fraud — but his death at "
            "57 during a business meeting remains a focal point for alternative energy "
            "researchers who see the pattern: inventor makes energy breakthrough claims, faces "
            "legal attack, dies under unusual circumstances. The documented facts (patent, court "
            "ruling, death) are clear; the interpretation remains contested."
        ),
        "metadata": {"type": "suppression case", "years_active": "1990-1998"},
    },

    # ============ FACILITIES ============

    {
        "name": "Wardenclyffe Tower",
        "entity_type": "facility",
        "description": (
            "Tesla's experimental wireless transmission station at Shoreham, Long Island, New "
            "York. Construction began in 1901 with funding from J.P. Morgan ($150,000 — "
            "approximately $5.3 million in 2024 dollars). The tower was designed to demonstrate "
            "wireless power transmission and global communications. The 187-foot wooden tower "
            "was topped by a 68-foot copper dome (the transmitter) and sat above a 120-foot "
            "shaft with iron pipes driven 300 feet into the earth (the ground connection). "
            "Tesla intended Wardenclyffe to be the first node in a global wireless power network. "
            "When Morgan learned that Tesla's real goal was free wireless power — which could not "
            "be metered or sold per unit — he withdrew funding. Tesla's famous line: Morgan asked "
            "'Where do we put the meter?' The tower was never completed to Tesla's specification. "
            "Unable to find replacement funding, Tesla lost the property in 1915. The tower was "
            "demolished in 1917 to pay debts (the steel was scrapped for wartime use). The site "
            "was designated a historical landmark in 2018. Wardenclyffe is the most concrete "
            "example in the energy suppression narrative: a working free-energy transmission "
            "system defunded specifically because it threatened the metered-power business model."
        ),
        "aliases": "Tesla Tower, Tesla Science Center at Wardenclyffe, Wardenclyffe",
        "metadata": {
            "location": "Shoreham, Long Island, NY",
            "built": 1901,
            "demolished": 1917,
        },
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [

    # ==== TESLA / WARDENCLYFFE / MORGAN / FBI ====
    {
        "source": "Nikola Tesla",
        "target": "Wardenclyffe Tower",
        "type": "created",
        "tier": "documented",
        "desc": (
            "Designed and built Wardenclyffe Tower (1901-1906) as a wireless power transmission "
            "station. Intended as first node in a global free-energy network. Never completed to "
            "full specification due to funding withdrawal."
        ),
        "year_start": 1901,
        "year_end": 1906,
        "sources": [1111, 1113, 1114],
    },
    {
        "source": "J.P. Morgan",
        "target": "Wardenclyffe Tower",
        "type": "funded",
        "tier": "documented",
        "desc": (
            "Provided $150,000 in initial funding for Wardenclyffe. Withdrew further support when "
            "he understood Tesla intended free wireless power — which could not be metered for profit. "
            "Morgan's withdrawal killed the project."
        ),
        "year_start": 1901,
        "year_end": 1904,
        "sources": [1111, 1113],
    },
    {
        "source": "J.P. Morgan",
        "target": "Nikola Tesla",
        "type": "suppressed",
        "tier": "credible",
        "desc": (
            "Morgan's funding withdrawal from Wardenclyffe and subsequent financial pressure "
            "effectively ended Tesla's wireless power research. Tesla could not find replacement "
            "investors — Morgan's influence in banking ensured no one else would fund the project."
        ),
        "year_start": 1904,
        "sources": [1111, 1113, 1137],
    },
    {
        "source": "FBI",
        "target": "Nikola Tesla",
        "type": "seized_papers",
        "tier": "documented",
        "desc": (
            "FBI and Office of Alien Property seized approximately 80 trunks of Tesla's papers, "
            "models, and equipment from his hotel room on his death (January 7, 1943). FOIA release "
            "(250+ pages) confirms seizure and review by John G. Trump (MIT). Papers declared of "
            "'no significant value' — a finding disputed by researchers."
        ),
        "year_start": 1943,
        "sources": [1112, 1113],
    },
    {
        "source": "Nikola Tesla",
        "target": "Westinghouse",
        "type": "licensed_to",
        "tier": "documented",
        "desc": (
            "Tesla licensed his AC polyphase patents to Westinghouse, enabling the company to "
            "champion alternating current. Under financial pressure from Morgan interests, Tesla "
            "reportedly tore up his royalty contract to save Westinghouse — forfeiting billions."
        ),
        "year_start": 1888,
        "sources": [1111, 1137],
    },
    {
        "source": "General Electric",
        "target": "Nikola Tesla",
        "type": "competed_with",
        "tier": "documented",
        "desc": (
            "GE (founded by Morgan from Edison's companies) opposed Tesla's AC system during the "
            "War of Currents. After AC won, Morgan consolidated the industry through GE, ensuring "
            "his financial interests controlled the electrical infrastructure Tesla's technology built."
        ),
        "year_start": 1892,
        "sources": [1137, 1111],
    },
    {
        "source": "J.P. Morgan",
        "target": "General Electric",
        "type": "founded",
        "tier": "documented",
        "desc": (
            "Morgan arranged the 1892 merger of Edison General Electric and Thomson-Houston to "
            "create General Electric. GE became Morgan's vehicle for controlling the electrical "
            "industry regardless of which current system prevailed."
        ),
        "year_start": 1892,
        "sources": [1137],
    },

    # ==== INVENTION SECRECY ACT / PATENT SECRECY ====
    {
        "source": "Invention Secrecy Act of 1951",
        "target": "Patent Secrecy Orders",
        "type": "authorized",
        "tier": "documented",
        "desc": (
            "The Act (35 USC 181-188) is the legal foundation for patent secrecy orders. "
            "Authorizes any federal agency to flag patent applications for classification. "
            "5,915 active orders as of FY2022."
        ),
        "year_start": 1951,
        "sources": [1115, 1116],
    },
    {
        "source": "Patent Secrecy Orders",
        "target": "DOE",
        "type": "administered_by",
        "tier": "documented",
        "desc": (
            "DOE reviews patent applications for potential secrecy orders in energy-related "
            "domains. DOE's 'born classified' authority under the Atomic Energy Act extends "
            "classification power beyond the patent system into fundamental research."
        ),
        "year_start": 1951,
        "sources": [1115, 1139, 1140],
    },
    {
        "source": "Patent Secrecy Orders",
        "target": "NSA",
        "type": "administered_by",
        "tier": "documented",
        "desc": (
            "NSA reviews patent applications related to cryptography and signals intelligence "
            "for secrecy orders. Cryptography patents are a known category of secrecy order targets."
        ),
        "year_start": 1951,
        "sources": [1115, 1116],
    },
    {
        "source": "Federation of American Scientists",
        "target": "Patent Secrecy Orders",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "FAS Project on Government Secrecy (Steven Aftergood) has tracked and published "
            "annual Invention Secrecy Act statistics since the 1990s — the primary public "
            "documentation of the patent secrecy system's scale."
        ),
        "year_start": 1995,
        "sources": [1116, 1117],
    },
    {
        "source": "Federation of American Scientists",
        "target": "Invention Secrecy Act of 1951",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "FAS provides the most comprehensive public analysis of the Invention Secrecy Act, "
            "including annual order counts, trend analysis, and FOIA requests for classification "
            "categories."
        ),
        "sources": [1116, 1117],
    },
    {
        "source": "Patent Secrecy Orders",
        "target": "Special Access Programs",
        "type": "feeds_into",
        "tier": "inference",
        "desc": (
            "Technologies classified via patent secrecy orders may enter Special Access Programs "
            "for further development. The secrecy order system provides the intake mechanism; "
            "SAPs provide the development environment. Connection is structural/logical, not "
            "individually documented for specific inventions."
        ),
        "sources": [1115, 1116, 1136],
    },

    # ==== COLD FUSION ====
    {
        "source": "Martin Fleischmann",
        "target": "Pons-Fleischmann Cold Fusion Announcement",
        "type": "led",
        "tier": "documented",
        "desc": (
            "Co-announced cold fusion at University of Utah press conference, March 23, 1989. "
            "Fleischmann was the senior scientist; the electrochemistry was based on his decades "
            "of experience with palladium-hydrogen systems."
        ),
        "year_start": 1989,
        "sources": [1118, 1119],
    },
    {
        "source": "Stanley Pons",
        "target": "Pons-Fleischmann Cold Fusion Announcement",
        "type": "led",
        "tier": "documented",
        "desc": (
            "Co-announced cold fusion with Fleischmann at University of Utah. Pons was department "
            "chair and the university's public face of the announcement."
        ),
        "year_start": 1989,
        "sources": [1118, 1119],
    },
    {
        "source": "Eugene Mallove",
        "target": "Pons-Fleischmann Cold Fusion Announcement",
        "type": "advocated_for",
        "tier": "documented",
        "desc": (
            "Resigned from MIT after alleging data manipulation in their cold fusion replication. "
            "Founded Infinite Energy magazine. Spent 15 years documenting the case for cold fusion "
            "until his murder in 2004."
        ),
        "year_start": 1991,
        "year_end": 2004,
        "sources": [1119, 1120, 1138],
    },
    {
        "source": "DOE",
        "target": "Pons-Fleischmann Cold Fusion Announcement",
        "type": "reviewed",
        "tier": "documented",
        "desc": (
            "DOE conducted two reviews: 1989 (ERAB panel, recommended against dedicated funding) "
            "and 2004 (more divided — roughly half found excess heat evidence compelling). Neither "
            "review led to DOE funding for cold fusion research."
        ),
        "year_start": 1989,
        "year_end": 2004,
        "sources": [1121, 1122],
    },
    {
        "source": "Martin Fleischmann",
        "target": "Stanley Pons",
        "type": "collaborated_with",
        "tier": "documented",
        "desc": (
            "Fleischmann and Pons collaborated for over five years before the 1989 announcement. "
            "Continued research together at IMRA Europe (Toyota-funded) in France until the lab "
            "closed in 1998."
        ),
        "year_start": 1984,
        "year_end": 1998,
        "sources": [1118, 1119],
    },

    # ==== RIFE / AMA ====
    {
        "source": "American Medical Association",
        "target": "Royal Raymond Rife",
        "type": "suppressed",
        "tier": "credible",
        "desc": (
            "AMA under Morris Fishbein (JAMA editor 1924-1949) allegedly orchestrated campaign to "
            "discredit Rife's frequency therapy after Fishbein's attempt to buy into Beam Ray "
            "Corporation was refused. Researchers who confirmed Rife's results recanted under "
            "AMA pressure. Equipment destroyed during trial period."
        ),
        "year_start": 1939,
        "sources": [1130, 1131],
    },
    {
        "source": "American Medical Association",
        "target": "Royal Raymond Rife",
        "type": "litigated_against",
        "tier": "documented",
        "desc": (
            "Beam Ray Corporation trial (San Diego County Court, 1939). AMA-aligned prosecution "
            "of Rife associates. During the trial period, Rife's laboratory was broken into and "
            "critical equipment damaged. Court records document the proceedings."
        ),
        "year_start": 1939,
        "sources": [1131],
    },

    # ==== STAN MEYER ====
    {
        "source": "Stanley Meyer",
        "target": "Stan Meyer Water Fuel Cell",
        "type": "invented",
        "tier": "documented",
        "desc": (
            "Developed water fuel cell technology and was granted US Patent 4,936,961 (1990). "
            "Claimed resonant voltage process could dissociate water using far less energy than "
            "conventional electrolysis. Patent is public record."
        ),
        "year_start": 1990,
        "sources": [1124, 1125],
    },
    {
        "source": "Stanley Meyer",
        "target": "Stan Meyer Water Fuel Cell",
        "type": "died_suspicious",
        "tier": "speculative",
        "desc": (
            "Meyer died March 20, 1998, age 57, during a dinner meeting. Coroner ruled cerebral "
            "aneurysm. Brother and supporters allege poisoning. No evidence of foul play was "
            "established by authorities. Death is documented; cause is speculative."
        ),
        "year_start": 1998,
        "sources": [1125, 1126],
    },

    # ==== T. TOWNSEND BROWN / ELECTROGRAVITICS ====
    {
        "source": "Thomas Townsend Brown",
        "target": "Electrogravitics Research Program",
        "type": "pioneered",
        "tier": "documented",
        "desc": (
            "Brown's Biefeld-Brown effect experiments from the 1920s onward laid the groundwork "
            "for the 1950s aerospace industry electrogravitics research programs documented in the "
            "1956 Gravity Research Group report."
        ),
        "year_start": 1928,
        "sources": [1127, 1128],
    },
    {
        "source": "Electrogravitics Research Program",
        "target": "Special Access Programs",
        "type": "classified_into",
        "tier": "inference",
        "desc": (
            "Open aerospace industry electrogravitics research (documented in mainstream press "
            "through 1955-56) vanished abruptly from public literature. The 1956 Gravity Research "
            "Group report was classified. The pattern — open research followed by sudden silence — "
            "is consistent with entry into classified programs, though no specific SAP has been "
            "identified."
        ),
        "year_start": 1957,
        "sources": [1128, 1129],
    },
    {
        "source": "Thomas Townsend Brown",
        "target": "CIA",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Brown's biographer Paul Schatzkin documented Brown's connections to intelligence "
            "community figures and his 1950s Navy demonstrations that were subsequently classified. "
            "Brown's travel to France and later work suggests intelligence community involvement, "
            "though no specific CIA relationship is declassified."
        ),
        "year_start": 1953,
        "sources": [1127],
    },

    # ==== THOMAS VALONE / PTO ====
    {
        "source": "Thomas Valone",
        "target": "Patent Secrecy Orders",
        "type": "investigated",
        "tier": "credible",
        "desc": (
            "As a USPTO patent examiner and later as director of Integrity Research Institute, "
            "Valone documented the patent secrecy system and its impact on energy inventions. "
            "His firing from the PTO for organizing a free energy conference demonstrates the "
            "institutional hostility toward these topics."
        ),
        "sources": [1129, 1133, 1134],
    },
    {
        "source": "Thomas Valone",
        "target": "Electrogravitics Research Program",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "Published 'Electrogravitics II' (2005), compiling declassified reports on "
            "electrogravitics research and T. Townsend Brown's work. Provided the most accessible "
            "collection of primary documents on the classified research program."
        ),
        "year_start": 2005,
        "sources": [1129],
    },
    {
        "source": "Thomas Valone",
        "target": "Thomas Townsend Brown",
        "type": "researched",
        "tier": "documented",
        "desc": (
            "Valone's 'Electrogravitics II' compiled and analyzed Brown's experimental results "
            "and the 1950s classified reports. Valone is one of the primary researchers keeping "
            "Brown's work in the public record."
        ),
        "sources": [1129, 1127],
    },

    # ==== JOHN HUTCHISON ====
    {
        "source": "John Hutchison",
        "target": "Nikola Tesla",
        "type": "built_on",
        "tier": "credible",
        "desc": (
            "Hutchison's apparatus uses Tesla coils as primary components. His claimed anomalous "
            "effects are attributed to combinations of Tesla coil emissions, Van de Graaff "
            "generators, and RF sources — directly building on Tesla's high-voltage research."
        ),
        "sources": [1132, 1111],
    },
    {
        "source": "John Hutchison",
        "target": "Thomas Townsend Brown",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Both researchers reported anomalous gravitational/inertial effects from "
            "electromagnetic experiments. Hutchison's levitation claims parallel Brown's "
            "electrogravitics work, though using different apparatus."
        ),
        "sources": [1132, 1127],
    },

    # ==== CROSS-LINKS TO EXISTING ENTITIES ====
    {
        "source": "Wardenclyffe Tower",
        "target": "Standard Oil",
        "type": "threatened",
        "tier": "inference",
        "desc": (
            "Tesla's wireless power transmission threatened the fossil fuel energy model. "
            "Standard Oil (Rockefeller) and J.P. Morgan controlled energy and finance respectively — "
            "free wireless power would have undermined both monopolies. The connection is "
            "structural, not based on a documented conspiracy."
        ),
        "year_start": 1901,
        "sources": [1111, 1136],
    },
    {
        "source": "Operation Paperclip",
        "target": "Electrogravitics Research Program",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "Paperclip brought Nazi scientists to the U.S. including those who worked on advanced "
            "propulsion. The timing of the electrogravitics research surge (1950s) coincides with "
            "Paperclip scientists integrating into U.S. aerospace. Direct connection to specific "
            "electrogravitics work is not documented."
        ),
        "year_start": 1950,
        "sources": [1128, 1136],
    },
    {
        "source": "Nikola Tesla",
        "target": "Operation Paperclip",
        "type": "context",
        "tier": "inference",
        "desc": (
            "Tesla's confiscated papers (1943) predated Operation Paperclip (1945) by two years. "
            "Both represent the U.S. government's pattern of seizing and classifying advanced "
            "technology research. Tesla's directed energy and propulsion notes may have informed "
            "the same programs that absorbed Paperclip scientists."
        ),
        "year_start": 1943,
        "year_end": 1945,
        "sources": [1112, 1113],
    },
    {
        "source": "DOE",
        "target": "Invention Secrecy Act of 1951",
        "type": "enforces",
        "tier": "documented",
        "desc": (
            "DOE participates in the patent secrecy order process for energy-related inventions "
            "and holds unique 'born classified' authority under the Atomic Energy Act. DOE is "
            "the primary energy-sector gatekeeper in the secrecy order system."
        ),
        "year_start": 1977,
        "sources": [1115, 1139, 1140],
    },
    {
        "source": "CIA",
        "target": "Nikola Tesla",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "Tesla's seized papers were reviewed by government officials in 1943. The OSS (CIA "
            "predecessor) was active at the time. FBI FOIA documents reference inter-agency "
            "interest in Tesla's work. Direct CIA involvement is not confirmed in declassified "
            "records but is consistent with the agency's known interest in advanced technology."
        ),
        "year_start": 1943,
        "sources": [1112],
    },
    {
        "source": "Eugene Mallove",
        "target": "DOE",
        "type": "petitioned",
        "tier": "documented",
        "desc": (
            "Mallove wrote an open letter to DOE Secretary Spencer Abraham in 2004 calling for "
            "a new review of cold fusion evidence. The 2004 DOE review occurred that year — the "
            "panel was more divided than in 1989 but DOE still declined to fund research. Mallove "
            "was murdered weeks after his letter."
        ),
        "year_start": 2004,
        "sources": [1120, 1121, 1138],
    },

    # ==== SYSTEMIC CONNECTIONS ====
    {
        "source": "Invention Secrecy Act of 1951",
        "target": "Nikola Tesla",
        "type": "context",
        "tier": "inference",
        "desc": (
            "The Act codified in law what happened to Tesla informally: government suppression "
            "of inventions deemed too disruptive. Tesla's papers were seized 8 years before the "
            "Act formalized the mechanism. The Act made Tesla's case the rule rather than the "
            "exception."
        ),
        "year_start": 1951,
        "sources": [1115, 1112],
    },
    {
        "source": "General Electric",
        "target": "Westinghouse",
        "type": "competed_with",
        "tier": "documented",
        "desc": (
            "GE (Morgan/Edison) vs. Westinghouse (Tesla) defined the War of Currents. AC won, "
            "but Morgan's creation of GE and financial pressure on Westinghouse ensured that "
            "Morgan's interests controlled the outcome regardless."
        ),
        "year_start": 1892,
        "sources": [1137],
    },
    {
        "source": "General Electric",
        "target": "Standard Oil",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "GE and Standard Oil successor companies were both Morgan/Rockefeller controlled "
            "entities that dominated American energy infrastructure — electrical and fossil fuel "
            "respectively. Their boards interlocked through the same banking networks."
        ),
        "year_start": 1892,
        "sources": [1137, 1136],
    },
    {
        "source": "Pons-Fleischmann Cold Fusion Announcement",
        "target": "DOE",
        "type": "reviewed_by",
        "tier": "documented",
        "desc": (
            "DOE was the institutional arbiter of cold fusion's fate. Two reviews (1989, 2004) "
            "both declined funding. The 2004 review was more favorable but still resulted in no "
            "action — DOE functioned as gatekeeper."
        ),
        "year_start": 1989,
        "year_end": 2004,
        "sources": [1121, 1122, 1123],
    },
]

# ============================================================
# ENTITY_SOURCES — link entities to their primary sources
# ============================================================

ENTITY_SOURCES = {
    # People
    "Nikola Tesla": [1111, 1112, 1113, 1114],
    "Thomas Townsend Brown": [1127, 1128],
    "Stanley Meyer": [1124, 1125, 1126],
    "Martin Fleischmann": [1118, 1119, 1122],
    "Stanley Pons": [1118, 1119],
    "Eugene Mallove": [1119, 1120, 1138],
    "Thomas Valone": [1129, 1133, 1134],
    "John Hutchison": [1132],
    # Organizations
    "General Electric": [1137],
    "Westinghouse": [1137, 1111],
    "American Medical Association": [1130, 1131],
    "Federation of American Scientists": [1116, 1117],
    # Agencies
    "DOE": [1121, 1139, 1140],
    # Legislation
    "Invention Secrecy Act of 1951": [1115, 1116, 1117],
    # Programs
    "Patent Secrecy Orders": [1115, 1116, 1117],
    "Electrogravitics Research Program": [1127, 1128, 1129],
    # Events
    "Pons-Fleischmann Cold Fusion Announcement": [1118, 1119, 1120, 1121, 1122, 1123],
    "Stan Meyer Water Fuel Cell": [1124, 1125, 1126],
    # Facilities
    "Wardenclyffe Tower": [1111, 1113, 1114],
}
