"""
Bioweapons — Expansion layer for Intel Console.

New branch mapping the architecture of biological weapons development, dual-use
research, and the deliberate obscuring of state-sponsored bioweapons programs.
From Unit 731's immunity deal through Fort Detrick's decades of weaponization,
the Soviet Biopreparat program, and the modern gain-of-function controversy.

The throughline: every major bioweapons program was built by governments, covered
up by governments, and the scientists who built them were protected by governments.
Unit 731 got immunity. Paperclip scientists got new careers. Biopreparat defectors
were debriefed and ignored. Fort Detrick's most dangerous critic died falling from
a window.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], Pentagon [87], Operation Paperclip, EcoHealth Alliance,
  Peter Daszak, Ralph Baric, Anthony Fauci, NIH, WHO

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1201-1230
# ============================================================

SOURCES = [
    # --- Unit 731 ---
    {
        "id": 1201,
        "title": "Sheldon Harris — 'Factories of Death: Japanese Biological Warfare, 1932-1945, and the American Cover-Up' (Routledge, 2002)",
        "url": "https://en.wikipedia.org/wiki/Unit_731",
        "source_type": "book",
        "author": "Sheldon H. Harris",
        "year": 2002,
    },
    {
        "id": 1202,
        "title": "Hal Gold — 'Unit 731: Testimony' (Tuttle, 1996) — firsthand accounts of biological warfare experiments",
        "url": "https://en.wikipedia.org/wiki/Unit_731",
        "source_type": "book",
        "author": "Hal Gold",
        "year": 1996,
    },
    {
        "id": 1203,
        "title": "Government Accountability Office — Report on Unit 731 records and immunity agreements (1999)",
        "url": "https://en.wikipedia.org/wiki/Unit_731",
        "source_type": "government",
        "year": 1999,
    },
    # --- Shirō Ishii ---
    {
        "id": 1204,
        "title": "Shirō Ishii — Wikipedia (Unit 731 commander, immunity deal with U.S.)",
        "url": "https://en.wikipedia.org/wiki/Shir%C5%8D_Ishii",
        "source_type": "other",
        "year": 2024,
    },
    # --- Fort Detrick ---
    {
        "id": 1205,
        "title": "Ed Regis — 'The Biology of Doom: America's Secret Germ Warfare Project' (Holt, 1999)",
        "url": "https://en.wikipedia.org/wiki/Fort_Detrick",
        "source_type": "book",
        "author": "Ed Regis",
        "year": 1999,
    },
    {
        "id": 1206,
        "title": "USAMRIID — U.S. Army Medical Research Institute of Infectious Diseases, Fort Detrick, Maryland",
        "url": "https://en.wikipedia.org/wiki/USAMRIID",
        "source_type": "government",
        "year": 2024,
    },
    {
        "id": 1207,
        "title": "Fort Detrick lab shutdown by CDC after safety failures — New York Times (August 2019)",
        "url": "https://www.nytimes.com/2019/08/05/health/germs-fort-detrick-biohazard.html",
        "source_type": "journalism",
        "year": 2019,
    },
    # --- Frank Olson ---
    {
        "id": 1208,
        "title": "H.P. Albarelli — 'A Terrible Mistake: The Murder of Frank Olson and the CIA's Secret Cold War Experiments' (Trine Day, 2009)",
        "url": "https://en.wikipedia.org/wiki/Frank_Olson",
        "source_type": "book",
        "author": "H.P. Albarelli",
        "year": 2009,
    },
    {
        "id": 1209,
        "title": "Frank Olson — Wikipedia (Fort Detrick scientist, suspicious death 1953, 1994 exhumation found blunt force trauma)",
        "url": "https://en.wikipedia.org/wiki/Frank_Olson",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 1210,
        "title": "Wormwood — Errol Morris documentary on Frank Olson's death (Netflix, 2017)",
        "url": "https://en.wikipedia.org/wiki/Wormwood_(TV_series)",
        "source_type": "documentary",
        "author": "Errol Morris",
        "year": 2017,
    },
    # --- Ken Alibek / Biopreparat ---
    {
        "id": 1211,
        "title": "Ken Alibek — 'Biohazard: The Chilling True Story of the Largest Covert Biological Weapons Program in the World' (Random House, 1999)",
        "url": "https://en.wikipedia.org/wiki/Ken_Alibek",
        "source_type": "book",
        "author": "Ken Alibek",
        "year": 1999,
    },
    {
        "id": 1212,
        "title": "Biopreparat — Wikipedia (Soviet biological weapons program)",
        "url": "https://en.wikipedia.org/wiki/Biopreparat",
        "source_type": "other",
        "year": 2024,
    },
    # --- William Patrick III ---
    {
        "id": 1213,
        "title": "William C. Patrick III — Fort Detrick bioweapons scientist, consulted on anthrax dissemination for CIA (obit and interviews)",
        "url": "https://en.wikipedia.org/wiki/William_C._Patrick_III",
        "source_type": "other",
        "year": 2010,
    },
    # --- Sverdlovsk anthrax ---
    {
        "id": 1214,
        "title": "Jeanne Guillemin — 'Anthrax: The Investigation of a Deadly Outbreak' (University of California Press, 1999)",
        "url": "https://en.wikipedia.org/wiki/Sverdlovsk_anthrax_leak",
        "source_type": "book",
        "author": "Jeanne Guillemin",
        "year": 1999,
    },
    {
        "id": 1215,
        "title": "Matthew Meselson et al. — 'The Sverdlovsk Anthrax Outbreak of 1979' (Science, 1994)",
        "url": "https://doi.org/10.1126/science.7973702",
        "source_type": "academic",
        "author": "Matthew Meselson et al.",
        "year": 1994,
    },
    # --- 2001 Anthrax attacks / Amerithrax ---
    {
        "id": 1216,
        "title": "FBI — Amerithrax Investigation Summary (2010)",
        "url": "https://www.justice.gov/archive/amerithrax/docs/amx-investigative-summary.pdf",
        "source_type": "government",
        "year": 2010,
    },
    {
        "id": 1217,
        "title": "National Academy of Sciences — Review of the Scientific Approaches Used During the FBI's Investigation of the 2001 Anthrax Letters (2011)",
        "url": "https://nap.nationalacademies.org/catalog/13098",
        "source_type": "academic",
        "year": 2011,
    },
    {
        "id": 1218,
        "title": "ProPublica — 'The Anthrax Files' (investigation questioning FBI's case against Bruce Ivins)",
        "url": "https://www.propublica.org/series/the-anthrax-files",
        "source_type": "journalism",
        "author": "ProPublica",
        "year": 2011,
    },
    # --- MKNaomi ---
    {
        "id": 1219,
        "title": "Church Committee — Alleged Assassination Plots Involving Foreign Leaders (1975, includes MKNaomi biological weapons provisions)",
        "url": "https://en.wikipedia.org/wiki/Project_MKNAOMI",
        "source_type": "congressional",
        "year": 1975,
    },
    {
        "id": 1220,
        "title": "Church Committee — testimony on CIA shellfish toxin and biological agents stockpile (violation of Nixon order)",
        "url": "https://en.wikipedia.org/wiki/Project_MKNAOMI",
        "source_type": "congressional",
        "year": 1975,
    },
    # --- Biological Weapons Convention ---
    {
        "id": 1221,
        "title": "United Nations — Convention on the Prohibition of Biological Weapons (BWC, entered into force 1975)",
        "url": "https://en.wikipedia.org/wiki/Biological_Weapons_Convention",
        "source_type": "government",
        "year": 1975,
    },
    # --- Dugway Proving Ground ---
    {
        "id": 1222,
        "title": "Dugway Proving Ground — U.S. Army testing facility for biological and chemical defense (Utah)",
        "url": "https://en.wikipedia.org/wiki/Dugway_Proving_Ground",
        "source_type": "government",
        "year": 2024,
    },
    {
        "id": 1223,
        "title": "Dugway Proving Ground live anthrax shipments to labs across U.S. (2015 incident)",
        "url": "https://en.wikipedia.org/wiki/Dugway_Proving_Ground",
        "source_type": "journalism",
        "year": 2015,
    },
    # --- DTRA ---
    {
        "id": 1224,
        "title": "DTRA — Defense Threat Reduction Agency, mission and operations",
        "url": "https://en.wikipedia.org/wiki/Defense_Threat_Reduction_Agency",
        "source_type": "government",
        "year": 2024,
    },
    # --- Gruinard Island ---
    {
        "id": 1225,
        "title": "Gruinard Island — UK anthrax testing site (1942-1943), decontaminated 1986",
        "url": "https://en.wikipedia.org/wiki/Gruinard_Island",
        "source_type": "government",
        "year": 1990,
    },
    # --- Gain-of-function / dual-use context ---
    {
        "id": 1226,
        "title": "Bulletin of the Atomic Scientists — 'Lab leaks happen more than you think' (history of biosafety incidents)",
        "url": "https://thebulletin.org/",
        "source_type": "journalism",
        "year": 2023,
    },
    # --- Nixon BWC order ---
    {
        "id": 1227,
        "title": "Richard Nixon — Executive Order directing destruction of U.S. biological weapons stockpile (November 1969)",
        "url": "https://en.wikipedia.org/wiki/United_States_biological_weapons_program",
        "source_type": "government",
        "year": 1969,
    },
    # --- Paperclip bioweapon scientists ---
    {
        "id": 1228,
        "title": "Annie Jacobsen — 'Operation Paperclip: The Secret Intelligence Program That Brought Nazi Scientists to America' (Little, Brown, 2014)",
        "url": "https://en.wikipedia.org/wiki/Operation_Paperclip",
        "source_type": "journalism",
        "author": "Annie Jacobsen",
        "year": 2014,
    },
    # --- Bruce Ivins ---
    {
        "id": 1229,
        "title": "David Willman — 'The Mirage Man: Bruce Ivins, the Anthrax Attacks, and America's Rush to War' (Bantam, 2011)",
        "url": "https://en.wikipedia.org/wiki/Bruce_E._Ivins",
        "source_type": "book",
        "author": "David Willman",
        "year": 2011,
    },
    # --- General bioweapons history ---
    {
        "id": 1230,
        "title": "Jeanne Guillemin — 'Biological Weapons: From the Invention of State-Sponsored Programs to Contemporary Bioterrorism' (Columbia University Press, 2005)",
        "url": "https://en.wikipedia.org/wiki/Biological_warfare",
        "source_type": "book",
        "author": "Jeanne Guillemin",
        "year": 2005,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- People ---
    {
        "name": "Shirō Ishii",
        "entity_type": "person",
        "description": "Japanese microbiologist and army officer (1892-1959). Commander of Unit 731, the Imperial Japanese Army's covert biological and chemical warfare research unit in Harbin, Manchuria. Directed experiments on live human subjects (vivisection, plague, cholera, frostbite) killing an estimated 3,000-12,000 people. Granted immunity by the U.S. after WWII in exchange for sharing bioweapons research data. Never prosecuted for war crimes. The immunity deal is documented in declassified records.",
        "aliases": "Ishii Shirō",
        "metadata": {"role": "Unit 731 commander", "years_active": "1932-1945"},
    },
    {
        "name": "Frank Olson",
        "entity_type": "person",
        "description": "American bacteriologist and biological weapons researcher at Fort Detrick (1911-1953). Worked on aerosol delivery of biological agents. Fell to his death from a 13th-floor hotel window in New York City on November 28, 1953, nine days after being covertly dosed with LSD by CIA officer Sidney Gottlieb. Initially ruled suicide; 1994 exhumation by forensic pathologist James Starrs found cranial injuries consistent with a blow to the head before the fall. Family received a presidential apology (Ford, 1975) and congressional settlement but the full truth remains classified.",
        "aliases": "",
        "metadata": {"role": "Fort Detrick scientist", "years_active": "1943-1953"},
    },
    {
        "name": "Ken Alibek",
        "entity_type": "person",
        "description": "Kazakh-born microbiologist, born Kanatjan Alibekov. First Deputy Director of Biopreparat, the Soviet Union's bioweapons program. Defected to the United States in 1992 and revealed the full scope of Soviet bioweapons development: weaponized smallpox, plague, anthrax, Marburg, and genetically modified pathogens. Author of 'Biohazard' (1999). His testimony exposed that the USSR continued bioweapons development in violation of the 1972 BWC throughout the Cold War.",
        "aliases": "Kanatjan Alibekov",
        "metadata": {"role": "Soviet bioweapons scientist / defector", "years_active": "1975-1992"},
    },
    {
        "name": "William Patrick III",
        "entity_type": "person",
        "description": "American biological weapons scientist (1926-2010). Worked at Fort Detrick for over 30 years, specializing in weaponizing biological agents for aerosol dispersal. Held five classified patents on methods for concentrating and weaponizing anthrax and other pathogens. After the U.S. offensive program ended (1969), became a consultant. Prepared a report for the CIA on the feasibility of sending anthrax through the mail — years before the 2001 attacks.",
        "aliases": "William C. Patrick III",
        "metadata": {"role": "Fort Detrick bioweapons scientist", "years_active": "1951-2010"},
    },
    {
        "name": "Bruce Ivins",
        "entity_type": "person",
        "description": "American microbiologist at USAMRIID, Fort Detrick (1946-2008). Named by the FBI as the sole perpetrator of the 2001 anthrax attacks (Amerithrax investigation). Died by suicide in 2008 before charges were filed. The National Academy of Sciences (2011) concluded that the FBI's scientific evidence was not conclusive enough to identify a single source flask. ProPublica and other investigations questioned the FBI's case. The investigation remains controversial — Ivins may have been a scapegoat.",
        "aliases": "Bruce E. Ivins",
        "metadata": {"role": "USAMRIID microbiologist", "years_active": "1980-2008"},
    },
    # --- Agencies/Organizations ---
    {
        "name": "USAMRIID",
        "entity_type": "agency",
        "description": "U.S. Army Medical Research Institute of Infectious Diseases, Fort Detrick, Maryland. The U.S. military's primary institution for defensive research on biological threats. Successor to the offensive biological weapons program ended by Nixon in 1969. Houses some of the world's most dangerous pathogens. Shut down by the CDC in 2019 over biosafety failures (wastewater decontamination issues). Bruce Ivins, the FBI's suspect in the 2001 anthrax attacks, worked here.",
        "aliases": "Fort Detrick, U.S. Army Medical Research Institute of Infectious Diseases",
        "metadata": {"type": "military research institute", "founded": 1969},
    },
    {
        "name": "DTRA",
        "entity_type": "agency",
        "description": "Defense Threat Reduction Agency. U.S. Department of Defense agency responsible for countering weapons of mass destruction (WMD). Operates the Cooperative Threat Reduction Program (Nunn-Lugar) and funds biological defense research. Has contracted with EcoHealth Alliance and other organizations for overseas pathogen research, raising dual-use concerns. Established 1998 by consolidating previous WMD-related agencies.",
        "aliases": "Defense Threat Reduction Agency",
        "metadata": {"type": "defense agency", "founded": 1998},
    },
    {
        "name": "Biopreparat",
        "entity_type": "organization",
        "description": "The Soviet Union's massive covert biological weapons program, established in 1973 — one year after signing the Biological Weapons Convention. At its peak employed 40,000+ scientists across dozens of facilities. Weaponized anthrax, smallpox, plague, Marburg, and other agents, including genetically engineered antibiotic-resistant strains. Exposed by defectors Ken Alibek (1992) and Vladimir Pasechnik (1989). Russia has never fully disclosed the program's scope.",
        "aliases": "",
        "metadata": {"type": "bioweapons program", "years_active": "1973-1992"},
    },
    {
        "name": "Dugway Proving Ground",
        "entity_type": "facility",
        "description": "U.S. Army testing facility in the Great Salt Lake Desert, Utah. Used for testing biological and chemical defense systems since WWII. In 2015, inadvertently shipped live anthrax samples to laboratories across the United States and to a military base in South Korea. One of the few facilities in the U.S. authorized to handle certain dangerous biological agents for testing purposes.",
        "aliases": "Dugway, DPG",
        "metadata": {"location": "Tooele County, Utah", "founded": 1942},
    },
    {
        "name": "Gruinard Island",
        "entity_type": "facility",
        "description": "Small island off the northwest coast of Scotland used by the UK government for biological weapons testing during WWII (1942-1943). Anthrax bombs were tested on sheep, contaminating the island for decades. It was not decontaminated until 1986 (using formaldehyde solution and seawater) and declared safe in 1990. A reminder that state bioweapons testing has long-lasting environmental consequences.",
        "aliases": "Gruinard, Anthrax Island",
        "metadata": {"location": "Gruinard Bay, Scotland, UK", "years_active": "1942-1943"},
    },
    # --- Programs ---
    {
        "name": "Unit 731",
        "entity_type": "program",
        "description": "Imperial Japanese Army's covert biological and chemical warfare research unit based in Harbin, Manchuria (1937-1945). Conducted lethal experiments on prisoners including vivisection, deliberate infection with plague/cholera/anthrax, and frostbite experiments. Estimated 3,000-12,000 victims. All Unit 731 researchers were granted immunity by the U.S. in exchange for their data. The Khabarovsk war crimes trial (1949, Soviet) documented some activities but the U.S. suppressed evidence to protect its intelligence value.",
        "aliases": "Unit Nana-San-Ichi, Epidemic Prevention and Water Purification Department",
        "metadata": {"type": "bioweapons program", "years_active": "1937-1945"},
    },
    {
        "name": "Project MKNaomi",
        "entity_type": "program",
        "description": "Joint CIA-Fort Detrick program for developing biological weapons and toxins for covert operations (1952-1970). Successor/parallel to MKULTRA's interest in chemical incapacitation. Developed shellfish toxin, dart guns ('the nondiscernible microbioinoculator'), and assassination-capable biological agents. Stockpile was supposed to be destroyed per Nixon's 1969 order, but the Church Committee discovered CIA had retained shellfish toxin and cobra venom in violation of the presidential directive.",
        "aliases": "MKNAOMI, MK-NAOMI",
        "metadata": {"type": "covert weapons program", "years_active": "1952-1970"},
    },
    {
        "name": "Amerithrax Investigation",
        "entity_type": "event",
        "description": "FBI investigation into the 2001 anthrax letter attacks that killed 5 people and infected 17 others. Letters containing weaponized Bacillus anthracis spores were mailed to media offices and U.S. Senators Daschle and Leahy in the weeks after 9/11. FBI initially focused on Steven Hatfill (exonerated, settled for $5.8M), then named Bruce Ivins (USAMRIID) as sole perpetrator. Ivins died by suicide in 2008. NAS review (2011) found scientific evidence inconclusive. Case officially closed but widely questioned.",
        "aliases": "2001 Anthrax Attacks, Anthrax Letters",
        "metadata": {"date": "2001-09-18"},
    },
    {
        "name": "Sverdlovsk Anthrax Leak",
        "entity_type": "event",
        "description": "In April 1979, an accidental release of weaponized anthrax spores from a Soviet military compound (Compound 19) in Sverdlovsk (now Yekaterinburg) killed at least 66 people. The Soviet government blamed contaminated meat for 12 years. The truth was confirmed after the USSR collapsed — Meselson et al. published definitive evidence in Science (1994). The incident proved the Soviets were actively producing offensive bioweapons in violation of the 1972 BWC.",
        "aliases": "Sverdlovsk Incident, Compound 19 Leak",
        "metadata": {"date": "1979-04-02", "location": "Sverdlovsk (Yekaterinburg), USSR"},
    },
    {
        "name": "Unit 731 Immunity Deal",
        "entity_type": "event",
        "description": "After WWII, the U.S. government granted immunity from prosecution to all Unit 731 researchers — including commander Shirō Ishii — in exchange for their biological weapons research data. The deal was classified for decades. General Douglas MacArthur authorized the arrangement. Japan's victims received no justice. The data was used to advance the U.S. offensive biological weapons program at Fort Detrick. One of the clearest documented cases of war crimes being covered up for intelligence value.",
        "aliases": "",
        "metadata": {"date": "1946-1948"},
    },
    {
        "name": "Fort Detrick Lab Shutdown",
        "entity_type": "event",
        "description": "In August 2019, the CDC ordered USAMRIID at Fort Detrick to halt all research on dangerous pathogens after inspection found failures in the wastewater decontamination system. The shutdown lasted months. Specific details were redacted in FOIA responses. The timing — months before COVID-19 emerged — generated significant speculation but no documented causal connection has been established.",
        "aliases": "",
        "metadata": {"date": "2019-08-02"},
    },
    # --- Legislation ---
    {
        "name": "Biological Weapons Convention",
        "entity_type": "legislation",
        "description": "Convention on the Prohibition of the Development, Production and Stockpiling of Bacteriological (Biological) and Toxin Weapons. Opened for signature 1972, entered into force 1975. First multilateral disarmament treaty banning an entire category of weapons. Signed by 183 states. Has no formal verification mechanism — a critical weakness that allowed the Soviet Union to operate Biopreparat in violation for nearly two decades. The U.S. blocked a verification protocol in 2001.",
        "aliases": "BWC, BTWC",
        "metadata": {"signed": 1972, "entered_into_force": 1975},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Unit 731 ---
    {
        "source": "Shirō Ishii",
        "target": "Unit 731",
        "type": "directed",
        "tier": "documented",
        "desc": "Commanded Unit 731 from its founding through WWII. Directed biological warfare experiments on live human subjects killing thousands.",
        "sources": [1201, 1202, 1204],
        "year_start": 1937,
        "year_end": 1945,
    },
    {
        "source": "Shirō Ishii",
        "target": "Unit 731 Immunity Deal",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Granted immunity from war crimes prosecution by the U.S. in exchange for Unit 731 research data. Never faced trial despite documented atrocities.",
        "sources": [1201, 1203, 1204],
        "year_start": 1946,
        "year_end": 1948,
    },
    {
        "source": "Unit 731 Immunity Deal",
        "target": "USAMRIID",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Unit 731 data was used to advance the U.S. biological weapons program at Fort Detrick. The immunity deal directly benefited the American bioweapons program.",
        "sources": [1201, 1203, 1205],
        "year_start": 1946,
        "year_end": 1969,
    },
    {
        "source": "Unit 731",
        "target": "Operation Paperclip",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Parallel programs: just as Operation Paperclip recruited Nazi scientists, the Unit 731 immunity deal recruited Japanese bioweapons scientists. Same pattern of trading war crimes immunity for intelligence value.",
        "sources": [1201, 1228],
        "year_start": 1946,
        "year_end": 1950,
    },
    # --- Frank Olson ---
    {
        "source": "Frank Olson",
        "target": "USAMRIID",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Bacteriologist at Fort Detrick's Special Operations Division. Worked on aerosol delivery of biological agents. His death in 1953 remains one of the most suspicious incidents in bioweapons history.",
        "sources": [1208, 1209],
        "year_start": 1943,
        "year_end": 1953,
    },
    {
        "source": "Frank Olson",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Olson was covertly dosed with LSD by CIA officer Sidney Gottlieb nine days before his death. The Church Committee exposed the dosing. 1994 exhumation found blunt force trauma to the head. CIA involvement in his death is documented; the full circumstances remain classified.",
        "sources": [1208, 1209, 1210],
        "year_start": 1953,
        "year_end": 1953,
    },
    {
        "source": "Frank Olson",
        "target": "Project MKNaomi",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Olson's work on biological agents at Fort Detrick overlapped with the CIA-Fort Detrick MKNaomi program. Some researchers believe he was killed because he intended to reveal bioweapons use in Korea.",
        "sources": [1208, 1209, 1219],
        "year_start": 1952,
        "year_end": 1953,
    },
    # --- Project MKNaomi ---
    {
        "source": "CIA",
        "target": "Project MKNaomi",
        "type": "operated",
        "tier": "documented",
        "desc": "Joint CIA-Fort Detrick program for covert biological weapons. Church Committee exposed that CIA retained toxin stockpile in violation of Nixon's 1969 destruction order.",
        "sources": [1219, 1220],
        "year_start": 1952,
        "year_end": 1970,
    },
    {
        "source": "Project MKNaomi",
        "target": "USAMRIID",
        "type": "connected_to",
        "tier": "documented",
        "desc": "MKNaomi was a joint operation between CIA and Fort Detrick's Special Operations Division. Fort Detrick scientists developed the biological agents; CIA directed their operational use.",
        "sources": [1219, 1220, 1205],
        "year_start": 1952,
        "year_end": 1970,
    },
    # --- William Patrick III ---
    {
        "source": "William Patrick III",
        "target": "USAMRIID",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Spent 30+ years at Fort Detrick weaponizing biological agents. Held five classified patents on methods for concentrating anthrax and other pathogens for aerosol dispersal.",
        "sources": [1213],
        "year_start": 1951,
        "year_end": 1986,
    },
    {
        "source": "William Patrick III",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "After retirement, consulted for the CIA. Prepared a report on the feasibility of sending anthrax through the mail — years before the 2001 anthrax attacks used exactly that method.",
        "sources": [1213, 1229],
        "year_start": 1986,
        "year_end": 2001,
    },
    {
        "source": "William Patrick III",
        "target": "Amerithrax Investigation",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Patrick's expertise in weaponized anthrax delivery — including his CIA-commissioned report on mailing anthrax — made him a relevant figure in the Amerithrax investigation, though he was never named as a suspect.",
        "sources": [1213, 1216],
        "year_start": 2001,
        "year_end": 2010,
    },
    # --- Ken Alibek / Biopreparat ---
    {
        "source": "Ken Alibek",
        "target": "Biopreparat",
        "type": "directed",
        "tier": "documented",
        "desc": "First Deputy Director of Biopreparat. After defection (1992), revealed the full scope: 40,000+ scientists, weaponized smallpox, genetically modified antibiotic-resistant plague, continued in violation of BWC.",
        "sources": [1211, 1212],
        "year_start": 1975,
        "year_end": 1992,
    },
    {
        "source": "Biopreparat",
        "target": "Biological Weapons Convention",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Biopreparat was established in 1973 — one year AFTER the USSR signed the BWC. The entire program was a deliberate violation of the treaty the Soviets had just signed.",
        "sources": [1211, 1212, 1221],
        "year_start": 1973,
        "year_end": 1992,
    },
    {
        "source": "Biopreparat",
        "target": "Sverdlovsk Anthrax Leak",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The 1979 Sverdlovsk leak came from Compound 19, a Biopreparat facility producing weaponized anthrax. The cover-up lasted 12 years. Meselson et al. confirmed the military origin in Science (1994).",
        "sources": [1212, 1214, 1215],
        "year_start": 1979,
        "year_end": 1992,
    },
    # --- Amerithrax ---
    {
        "source": "Bruce Ivins",
        "target": "USAMRIID",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Microbiologist at USAMRIID for nearly three decades. Specialized in anthrax vaccine research. Named by FBI as sole perpetrator of 2001 anthrax attacks. Died before charges filed.",
        "sources": [1216, 1229],
        "year_start": 1980,
        "year_end": 2008,
    },
    {
        "source": "Bruce Ivins",
        "target": "Amerithrax Investigation",
        "type": "connected_to",
        "tier": "credible",
        "desc": "FBI named Ivins as the sole perpetrator. NAS review found the scientific evidence inconclusive for identifying a single source flask. Ivins died by suicide in 2008, leaving the case unresolved.",
        "sources": [1216, 1217, 1218, 1229],
        "year_start": 2001,
        "year_end": 2008,
    },
    {
        "source": "Amerithrax Investigation",
        "target": "USAMRIID",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The anthrax used in the 2001 attacks was the Ames strain — the same strain maintained at USAMRIID. The attack came from inside the U.S. biodefense establishment.",
        "sources": [1216, 1217],
        "year_start": 2001,
        "year_end": 2010,
    },
    # --- Fort Detrick shutdown ---
    {
        "source": "Fort Detrick Lab Shutdown",
        "target": "USAMRIID",
        "type": "connected_to",
        "tier": "documented",
        "desc": "CDC shut down USAMRIID in August 2019 over biosafety failures in wastewater decontamination. Research on dangerous pathogens halted for months. Specific details redacted in FOIA responses.",
        "sources": [1207],
        "year_start": 2019,
        "year_end": 2019,
    },
    # --- Dugway ---
    {
        "source": "Dugway Proving Ground",
        "target": "USAMRIID",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Both are U.S. Army biological defense facilities. Dugway tests biodefense systems; USAMRIID conducts research. The 2015 live anthrax shipment incident highlighted ongoing biosafety risks.",
        "sources": [1222, 1223],
        "year_start": 1942,
        "year_end": None,
    },
    {
        "source": "Dugway Proving Ground",
        "target": "The Pentagon",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Operated by the U.S. Army under DoD authority. Used for biological and chemical defense testing since WWII.",
        "sources": [1222],
        "year_start": 1942,
        "year_end": None,
    },
    # --- DTRA ---
    {
        "source": "DTRA",
        "target": "The Pentagon",
        "type": "connected_to",
        "tier": "documented",
        "desc": "DoD agency responsible for countering WMD threats. Funds overseas biological research through Cooperative Threat Reduction program.",
        "sources": [1224],
        "year_start": 1998,
        "year_end": None,
    },
    {
        "source": "DTRA",
        "target": "EcoHealth Alliance",
        "type": "funded",
        "tier": "credible",
        "desc": "DTRA has funded overseas pathogen collection and research through organizations including EcoHealth Alliance. Part of the dual-use research pipeline that raises bioweapons concerns.",
        "sources": [1224, 1226],
        "year_start": 2010,
        "year_end": None,
    },
    # --- Gruinard ---
    {
        "source": "Gruinard Island",
        "target": "Unit 731",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Both represent WWII-era state bioweapons testing. UK tested anthrax on Gruinard (1942-43) while Japan's Unit 731 conducted far more extensive human experimentation. Allied nations were not innocent of bioweapons development.",
        "sources": [1225, 1201],
        "year_start": 1942,
        "year_end": 1945,
    },
    # --- BWC ---
    {
        "source": "Biological Weapons Convention",
        "target": "USAMRIID",
        "type": "connected_to",
        "tier": "documented",
        "desc": "USAMRIID was established in 1969 when Nixon ordered the end of offensive bioweapons, pivoting Fort Detrick to defensive research. The BWC (1975) codified this shift internationally. Whether 'defensive' research remains meaningfully distinct from 'offensive' is the central dual-use question.",
        "sources": [1221, 1227],
        "year_start": 1969,
        "year_end": None,
    },
    # --- Gain-of-function bridge ---
    {
        "source": "USAMRIID",
        "target": "NIH",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Both fund and conduct research on dangerous pathogens under the 'biodefense' umbrella. The gain-of-function controversy highlights how dual-use research blurs the line between defense and offense, with both institutions involved.",
        "sources": [1206, 1226],
        "year_start": 1969,
        "year_end": None,
    },
    # --- Paperclip bioweapon scientists ---
    {
        "source": "Operation Paperclip",
        "target": "USAMRIID",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Operation Paperclip brought Nazi scientists to the U.S. including those with biological/chemical weapons expertise. Some were employed at or consulted for Fort Detrick. Documented by Annie Jacobsen.",
        "sources": [1228],
        "year_start": 1945,
        "year_end": 1960,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Shirō Ishii": [1201, 1202, 1203, 1204],
    "Frank Olson": [1208, 1209, 1210],
    "Ken Alibek": [1211, 1212],
    "William Patrick III": [1213],
    "Bruce Ivins": [1216, 1217, 1218, 1229],
    "USAMRIID": [1205, 1206, 1207],
    "DTRA": [1224],
    "Biopreparat": [1211, 1212, 1214],
    "Dugway Proving Ground": [1222, 1223],
    "Gruinard Island": [1225],
    "Unit 731": [1201, 1202, 1203],
    "Project MKNaomi": [1219, 1220],
    "Amerithrax Investigation": [1216, 1217, 1218],
    "Sverdlovsk Anthrax Leak": [1214, 1215],
    "Unit 731 Immunity Deal": [1201, 1203],
    "Fort Detrick Lab Shutdown": [1207],
    "Biological Weapons Convention": [1221, 1227, 1230],
}
