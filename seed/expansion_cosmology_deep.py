"""
Cosmology & Origins DEEP — Expansion layer for Intel Console.

Goes deeper on the archaeological anomalies mapped in expansion_cosmology_origins.py.
Adds researchers who challenged mainstream chronology with physical evidence (Brien
Foerster's elongated skulls, Christopher Dunn's precision machining thesis, Flinders
Petrie's early precision measurements), prophetic/channeled sources (Edgar Cayce,
Zecharia Sitchin), and the additional anomalous sites that don't fit the standard
narrative (Yonaguni, Derinkuyu, Sacsayhuamán, Nan Madol, Carnac, Teotihuacan).

Evidence tiers applied with strict discipline — most of this is inference or
speculative. What IS documented: physical measurements of sites, DNA results on
skulls, precision machining marks. What is inference: connecting these to a lost
civilization framework. What is speculative: channeled/prophetic accounts.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Graham Hancock, Randall Carlson, Robert Schoch, John Anthony West,
  Klaus Schmidt, Robert Bauval, Michael Cremo, Smithsonian Institution,
  Gobekli Tepe, Puma Punku, Great Sphinx, Baalbek, Younger Dryas Impact Hypothesis,
  Geological Society of America

Evidence tiers (applied strictly):
  documented = archaeological record, peer-reviewed geology/archaeology, physical measurements
  credible   = published research challenging consensus, legitimate debate
  inference  = connecting documented evidence to larger theoretical frameworks
  speculative = claims rejected by mainstream, channeled/prophetic sources
"""

# ============================================================
# SOURCES — IDs 1171-1200
# ============================================================

SOURCES = [
    # --- Brien Foerster / Elongated Skulls ---
    {
        "id": 1171,
        "title": "Brien Foerster — 'Elongated Skulls of Peru and Bolivia: The Path of Viracocha' (CreateSpace, 2016)",
        "url": "https://en.wikipedia.org/wiki/Paracas_skulls",
        "source_type": "book",
        "author": "Brien Foerster",
        "year": 2016,
    },
    {
        "id": 1172,
        "title": "Paracas skulls DNA analysis — preliminary results showing anomalous mitochondrial haplogroups (2014-2018, independent labs)",
        "url": "https://en.wikipedia.org/wiki/Paracas_skulls",
        "source_type": "other",
        "year": 2018,
    },
    # --- Christopher Dunn ---
    {
        "id": 1173,
        "title": "Christopher Dunn — 'The Giza Power Plant: Technologies of Ancient Egypt' (Bear & Company, 1998)",
        "url": "https://en.wikipedia.org/wiki/Christopher_Dunn_(author)",
        "source_type": "book",
        "author": "Christopher Dunn",
        "year": 1998,
    },
    {
        "id": 1174,
        "title": "Christopher Dunn — 'Lost Technologies of Ancient Egypt: Advanced Engineering in the Temples of the Pharaohs' (Bear & Company, 2010)",
        "url": "https://en.wikipedia.org/wiki/Christopher_Dunn_(author)",
        "source_type": "book",
        "author": "Christopher Dunn",
        "year": 2010,
    },
    # --- Edgar Cayce ---
    {
        "id": 1175,
        "title": "Edgar Cayce — Association for Research and Enlightenment (A.R.E.) archives, Virginia Beach",
        "url": "https://en.wikipedia.org/wiki/Edgar_Cayce",
        "source_type": "archive",
        "year": 1945,
    },
    {
        "id": 1176,
        "title": "Thomas Sugrue — 'There Is a River: The Story of Edgar Cayce' (A.R.E. Press, 1942)",
        "url": "https://en.wikipedia.org/wiki/Edgar_Cayce",
        "source_type": "book",
        "author": "Thomas Sugrue",
        "year": 1942,
    },
    # --- Zecharia Sitchin ---
    {
        "id": 1177,
        "title": "Zecharia Sitchin — 'The 12th Planet' (Stein and Day, 1976) — first book of Earth Chronicles series",
        "url": "https://en.wikipedia.org/wiki/Zecharia_Sitchin",
        "source_type": "book",
        "author": "Zecharia Sitchin",
        "year": 1976,
    },
    {
        "id": 1178,
        "title": "Michael Heiser — critique of Sitchin's Sumerian translations (SitchinIsWrong.com)",
        "url": "https://en.wikipedia.org/wiki/Zecharia_Sitchin",
        "source_type": "academic",
        "author": "Michael S. Heiser",
        "year": 2005,
    },
    # --- Michael Tellinger ---
    {
        "id": 1179,
        "title": "Michael Tellinger — 'Slave Species of the Gods: The Secret History of the Anunnaki' (Bear & Company, 2012)",
        "url": "https://en.wikipedia.org/wiki/Michael_Tellinger",
        "source_type": "book",
        "author": "Michael Tellinger",
        "year": 2012,
    },
    {
        "id": 1180,
        "title": "Michael Tellinger — 'Adam's Calendar' stone circle complex, Mpumalanga, South Africa (2003)",
        "url": "https://en.wikipedia.org/wiki/Michael_Tellinger",
        "source_type": "other",
        "author": "Michael Tellinger",
        "year": 2003,
    },
    # --- Walter Cruttenden ---
    {
        "id": 1181,
        "title": "Walter Cruttenden — 'Lost Star of Myth and Time' (St. Lynn's Press, 2006) — binary star hypothesis and Yuga cycle",
        "url": "https://en.wikipedia.org/wiki/Binary_Research_Institute",
        "source_type": "book",
        "author": "Walter Cruttenden",
        "year": 2006,
    },
    # --- Flinders Petrie ---
    {
        "id": 1182,
        "title": "W.M. Flinders Petrie — 'The Pyramids and Temples of Gizeh' (Field & Tuer, 1883) — first precision survey of Giza",
        "url": "https://en.wikipedia.org/wiki/Flinders_Petrie",
        "source_type": "academic",
        "author": "W.M. Flinders Petrie",
        "year": 1883,
    },
    # --- Yonaguni Monument ---
    {
        "id": 1183,
        "title": "Masaaki Kimura — 'Diving Survey Report for Submarine Ruins Off Yonaguni, Japan' (Marine Science and Technology, 2004)",
        "url": "https://en.wikipedia.org/wiki/Yonaguni_Monument",
        "source_type": "academic",
        "author": "Masaaki Kimura",
        "year": 2004,
    },
    {
        "id": 1184,
        "title": "Robert Schoch — investigation of Yonaguni Monument (geological assessment, natural vs. man-made debate)",
        "url": "https://www.robertschoch.com/yonaguni.html",
        "source_type": "academic",
        "author": "Robert M. Schoch",
        "year": 1999,
    },
    # --- Derinkuyu ---
    {
        "id": 1185,
        "title": "Derinkuyu underground city — Turkish Ministry of Culture archaeological documentation",
        "url": "https://en.wikipedia.org/wiki/Derinkuyu_underground_city",
        "source_type": "government",
        "year": 1969,
    },
    # --- Sacsayhuamán ---
    {
        "id": 1186,
        "title": "Jean-Pierre Protzen — 'Inca Architecture and Construction at Ollantaytambo' (Oxford University Press, 1993)",
        "url": "https://en.wikipedia.org/wiki/Sacsayhuam%C3%A1n",
        "source_type": "academic",
        "author": "Jean-Pierre Protzen",
        "year": 1993,
    },
    # --- Nan Madol ---
    {
        "id": 1187,
        "title": "William Ayres — archaeological survey of Nan Madol, Pohnpei, Federated States of Micronesia (University of Oregon)",
        "url": "https://en.wikipedia.org/wiki/Nan_Madol",
        "source_type": "academic",
        "author": "William Ayres",
        "year": 1990,
    },
    {
        "id": 1188,
        "title": "Nan Madol — UNESCO World Heritage Site inscription (2016, endangered list)",
        "url": "https://whc.unesco.org/en/list/1503",
        "source_type": "government",
        "year": 2016,
    },
    # --- Carnac ---
    {
        "id": 1189,
        "title": "Alexander Thom — 'Megalithic Sites in Britain' (Oxford University Press, 1967) — statistical analysis of stone alignments",
        "url": "https://en.wikipedia.org/wiki/Alexander_Thom",
        "source_type": "academic",
        "author": "Alexander Thom",
        "year": 1967,
    },
    # --- Teotihuacan ---
    {
        "id": 1190,
        "title": "George Cowgill — 'State and Society at Teotihuacan, Mexico' (Annual Review of Anthropology, 1997)",
        "url": "https://en.wikipedia.org/wiki/Teotihuacan",
        "source_type": "academic",
        "author": "George Cowgill",
        "year": 1997,
    },
    {
        "id": 1191,
        "title": "Sergio Gomez — discovery of liquid mercury beneath Temple of the Feathered Serpent, Teotihuacan (2015)",
        "url": "https://en.wikipedia.org/wiki/Teotihuacan",
        "source_type": "journalism",
        "year": 2015,
    },
    # --- Younger Dryas boundary evidence ---
    {
        "id": 1192,
        "title": "Sweatman & Coombs — 'Decoding European Palaeolithic Art: Extremely Ancient Knowledge of Precession of the Equinoxes' (Athens Journal of History, 2019)",
        "url": "https://doi.org/10.30958/ajhis.5-1-1",
        "source_type": "academic",
        "author": "Martin B. Sweatman, Alistair Coombs",
        "year": 2019,
    },
    # --- Sphinx water erosion supplemental ---
    {
        "id": 1193,
        "title": "Robert Schoch — 'Forgotten Civilization: New Discoveries on the Solar-Induced Dark Age' (Inner Traditions, 2012)",
        "url": "https://en.wikipedia.org/wiki/Robert_M._Schoch",
        "source_type": "book",
        "author": "Robert M. Schoch",
        "year": 2012,
    },
    # --- General ancient sites ---
    {
        "id": 1194,
        "title": "Hugh Newman — 'Earth Grids: The Secret Patterns of Gaia's Sacred Sites' (Wooden Books, 2008)",
        "url": "https://en.wikipedia.org/wiki/Ley_line",
        "source_type": "book",
        "author": "Hugh Newman",
        "year": 2008,
    },
    {
        "id": 1195,
        "title": "Graham Hancock — 'Underworld: The Mysterious Origins of Civilization' (Crown, 2002) — submerged sites including Yonaguni",
        "url": "https://en.wikipedia.org/wiki/Graham_Hancock",
        "source_type": "book",
        "author": "Graham Hancock",
        "year": 2002,
    },
    # --- Cayce Hall of Records ---
    {
        "id": 1196,
        "title": "Edgar Cayce readings on Atlantis and Hall of Records beneath the Sphinx (A.R.E. readings #364, #378, #5750)",
        "url": "https://en.wikipedia.org/wiki/Edgar_Cayce",
        "source_type": "archive",
        "year": 1933,
    },
    # --- Petrie precision measurements supplemental ---
    {
        "id": 1197,
        "title": "Mark Lehner — 'The Complete Pyramids' (Thames & Hudson, 1997) — mainstream Egyptology reference",
        "url": "https://en.wikipedia.org/wiki/Mark_Lehner",
        "source_type": "academic",
        "author": "Mark Lehner",
        "year": 1997,
    },
    # --- Sitchin critique and Sumerian context ---
    {
        "id": 1198,
        "title": "Samuel Noah Kramer — 'The Sumerians: Their History, Culture, and Character' (University of Chicago Press, 1963) — mainstream Sumerology",
        "url": "https://en.wikipedia.org/wiki/Samuel_Noah_Kramer",
        "source_type": "academic",
        "author": "Samuel Noah Kramer",
        "year": 1963,
    },
    # --- Binary star / precession ---
    {
        "id": 1199,
        "title": "Binary Research Institute — research on the observable of the precession cycle and binary star hypothesis",
        "url": "https://www.binaryresearchinstitute.com/",
        "source_type": "other",
        "year": 2024,
    },
    # --- Tellinger stone circles ---
    {
        "id": 1200,
        "title": "Tellinger & Heine — 'Adam's Calendar: Discovering the Oldest Man-Made Structure on Earth' (Zulu Planet, 2008)",
        "url": "https://en.wikipedia.org/wiki/Michael_Tellinger",
        "source_type": "book",
        "author": "Michael Tellinger, Johan Heine",
        "year": 2008,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- People ---
    {
        "name": "Brien Foerster",
        "entity_type": "person",
        "description": "Canadian-born researcher based in Peru specializing in elongated skulls and megalithic sites. Has conducted DNA testing on Paracas skulls through independent laboratories, with preliminary results showing anomalous mitochondrial haplogroups not found in known populations. His work documents physical anomalies (cranial volume, suture patterns) but remains outside peer-reviewed channels. Author of numerous books on Peru's megalithic architecture and biological anomalies.",
        "aliases": "",
        "metadata": {"role": "independent researcher / author", "years_active": "2000s-present"},
    },
    {
        "name": "Christopher Dunn",
        "entity_type": "person",
        "description": "British-American manufacturing engineer and author. Applied modern machining expertise to analyze ancient Egyptian artifacts, identifying tool marks, precision surfaces, and manufacturing tolerances that he argues exceed what is achievable with known ancient tools. Author of 'The Giza Power Plant' (1998) and 'Lost Technologies of Ancient Egypt' (2010). His technical observations about machining precision are documented; his 'power plant' theory is speculative.",
        "aliases": "",
        "metadata": {"role": "engineer / author", "years_active": "1995-present"},
    },
    {
        "name": "Edgar Cayce",
        "entity_type": "person",
        "description": "American mystic and 'sleeping prophet' (1877-1945). Over 40 years, gave ~14,000 documented 'readings' while in trance states, covering medical diagnoses, past lives, and prophecy. His Atlantis readings described an advanced pre-diluvian civilization and predicted a 'Hall of Records' beneath the Great Sphinx. The A.R.E. (Association for Research and Enlightenment) preserves his readings in Virginia Beach. Significant cultural influence on alternative history despite being untestable channeled material.",
        "aliases": "The Sleeping Prophet",
        "metadata": {"role": "mystic / prophet", "years_active": "1901-1945"},
    },
    {
        "name": "Zecharia Sitchin",
        "entity_type": "person",
        "description": "Russian-born American author (1920-2010). Proposed that ancient Sumerian texts describe the Anunnaki as extraterrestrial beings from a planet called Nibiru who created humans through genetic engineering. Author of 'The 12th Planet' (1976) and the Earth Chronicles series. His translations of Sumerian cuneiform are rejected by mainstream Assyriologists (Heiser, Kramer). Enormously influential in alternative history and ancient astronaut theory despite being academically discredited.",
        "aliases": "",
        "metadata": {"role": "author / alternative historian", "years_active": "1976-2010"},
    },
    {
        "name": "Michael Tellinger",
        "entity_type": "person",
        "description": "South African author, musician, and politician. Claims to have identified hundreds of thousands of ancient stone circle ruins across southern Africa, with 'Adam's Calendar' (a stone circle complex in Mpumalanga) allegedly aligned astronomically and dated to 75,000+ years ago. Builds on Sitchin's Anunnaki framework. Founded the Ubuntu Party. His dating claims are rejected by mainstream archaeologists — stone circles exist but conventional dating is much younger.",
        "aliases": "",
        "metadata": {"role": "author / researcher", "years_active": "2003-present"},
    },
    {
        "name": "Walter Cruttenden",
        "entity_type": "person",
        "description": "American researcher and director of the Binary Research Institute. Proposes that the precession of the equinoxes is caused not by Earth's wobble but by the solar system's orbit around a binary companion star, with ~24,000-year cycles correlating to Hindu Yuga ages and civilizational rise/fall. Published 'Lost Star of Myth and Time' (2006). The binary star hypothesis has some astronomical precedent but remains unproven.",
        "aliases": "",
        "metadata": {"role": "researcher / Binary Research Institute", "years_active": "2001-present"},
    },
    {
        "name": "Flinders Petrie",
        "entity_type": "person",
        "description": "Sir William Matthew Flinders Petrie (1853-1942). Father of modern Egyptology and pioneer of systematic archaeological methodology. Conducted the first precision survey of the Great Pyramid (1880-1882), documenting construction tolerances of fractions of an inch across massive stone surfaces. His measurements remain foundational and reveal engineering precision that alternative researchers (Dunn, Hancock) cite as evidence of advanced lost technology. Mainstream Egyptology attributes this to skilled craftsmanship, not lost technology.",
        "aliases": "Sir Flinders Petrie, W.M.F. Petrie",
        "metadata": {"role": "archaeologist / Egyptologist", "years_active": "1880-1942"},
    },
    # --- Sites ---
    {
        "name": "Yonaguni Monument",
        "entity_type": "facility",
        "description": "Submerged rock formation off the coast of Yonaguni Island, Japan, discovered by diver Kihachiro Aratake in 1987. Features flat terraces, right angles, and step-like formations at depths of 5-25 meters. Marine geologist Masaaki Kimura argues it is a man-made structure submerged by sea level rise (~10,000 years ago). Robert Schoch and other geologists argue it is a natural sandstone formation shaped by geological processes. The debate remains unresolved — the regularity is striking but not conclusive.",
        "aliases": "Yonaguni Underwater Monument, Yonaguni Submarine Ruins",
        "metadata": {"location": "Yonaguni Island, Okinawa, Japan", "depth": "5-25m below sea level"},
    },
    {
        "name": "Derinkuyu",
        "entity_type": "facility",
        "description": "Ancient underground city in Cappadocia, Turkey, extending to a depth of approximately 85 meters across 18 levels. Could shelter an estimated 20,000 people with livestock and food stores. Features ventilation shafts, water wells, and rolling stone doors. First opened to the public in 1969. One of over 200 underground cities in Cappadocia. Conventional dating attributes construction to Phrygians (~8th-7th century BCE) with expansions by early Christians. The engineering scale is extraordinary regardless of dating.",
        "aliases": "Derinkuyu Underground City",
        "metadata": {"location": "Derinkuyu, Cappadocia, Turkey", "depth": "85m, 18 levels"},
    },
    {
        "name": "Sacsayhuamán",
        "entity_type": "facility",
        "description": "Massive stone fortress/temple complex overlooking Cusco, Peru. Features polygonal limestone walls with blocks weighing up to 200 tons, fitted together without mortar with such precision that a knife blade cannot be inserted between them. Attributed to the Inca Empire (~15th century CE) by mainstream archaeology. The precision of the polygonal jointing and the scale of stone transport remain subjects of academic and alternative debate. Some researchers question whether the megalithic foundation predates the Inca.",
        "aliases": "Saqsaywaman, Saksaq Waman",
        "metadata": {"location": "Cusco, Peru", "date_mainstream": "~15th century CE"},
    },
    {
        "name": "Nan Madol",
        "entity_type": "facility",
        "description": "Ancient city built on a series of artificial islets in the lagoon of Pohnpei, Federated States of Micronesia. Constructed from massive columnar basalt logs (some weighing 50+ tons) transported from quarries across the island. Known as the 'Venice of the Pacific.' Conventional dating: ~1200-1500 CE (Saudeleur dynasty). UNESCO World Heritage Site (2016, endangered). The logistics of transporting and stacking 50-ton basalt columns on coral reef islets remains a genuine archaeological puzzle.",
        "aliases": "Nan Madol Ruins",
        "metadata": {"location": "Pohnpei, Federated States of Micronesia", "date_mainstream": "~1200-1500 CE"},
    },
    {
        "name": "Carnac Stones",
        "entity_type": "facility",
        "description": "System of more than 3,000 megalithic standing stones in Carnac, Brittany, France. Erected between approximately 4500-3300 BCE during the Neolithic period. Arranged in parallel rows (alignments) stretching over 4 kilometers, with associated dolmens, tumuli, and enclosures. Alexander Thom's surveys suggested consistent measurement units ('megalithic yard') and astronomical alignments. The sheer scale and organization suggest coordinated effort by a large, organized society predating writing in the region.",
        "aliases": "Carnac Alignments, Alignements de Carnac",
        "metadata": {"location": "Carnac, Brittany, France", "date_range": "~4500-3300 BCE"},
    },
    {
        "name": "Teotihuacan",
        "entity_type": "facility",
        "description": "Ancient Mesoamerican city in the Valley of Mexico, reaching peak population of ~125,000-200,000 by ~450 CE. Features the Pyramid of the Sun (3rd largest pyramid on Earth), Pyramid of the Moon, and Avenue of the Dead with precise astronomical alignment. Liquid mercury discovered beneath the Temple of the Feathered Serpent (2015). The builders' identity is unknown — the Aztecs named it 'Teotihuacan' ('birthplace of the gods') centuries after its mysterious collapse ~550 CE. UNESCO World Heritage Site.",
        "aliases": "City of the Gods",
        "metadata": {"location": "San Juan Teotihuacan, Mexico", "date_range": "~100 BCE - 550 CE"},
    },
    # --- Organizations ---
    {
        "name": "Association for Research and Enlightenment",
        "entity_type": "organization",
        "description": "Founded in 1931 in Virginia Beach, Virginia to preserve and study Edgar Cayce's readings. Maintains an archive of ~14,000 readings and operates as a membership organization. Has funded archaeological research related to Cayce's claims, including Sphinx-area investigations. While mainstream science does not accept the readings as evidence, the A.R.E. represents the most organized preservation of prophetic/channeled material related to alternative chronology.",
        "aliases": "A.R.E., ARE",
        "metadata": {"type": "research/preservation organization", "founded": 1931},
    },
    {
        "name": "Binary Research Institute",
        "entity_type": "organization",
        "description": "Founded by Walter Cruttenden in Newport Beach, California. Researches the hypothesis that precession of the equinoxes is caused by the solar system's motion around a binary companion star rather than Earth's axial wobble. Hosts the Conference on Precession and Ancient Knowledge (CPAK). The hypothesis reframes civilizational cycles (Yuga, Great Year) as astronomical rather than mythological phenomena.",
        "aliases": "BRI",
        "metadata": {"type": "research institute", "founded": 2001},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Brien Foerster ---
    {
        "source": "Brien Foerster",
        "target": "Puma Punku",
        "type": "investigated",
        "tier": "credible",
        "desc": "Has conducted extensive documentation of megalithic sites across Peru and Bolivia, including Puma Punku. His photographs and measurements of precision stonework are valuable documentation regardless of interpretive framework.",
        "sources": [1171],
        "year_start": 2000,
        "year_end": None,
    },
    {
        "source": "Brien Foerster",
        "target": "Sacsayhuamán",
        "type": "investigated",
        "tier": "credible",
        "desc": "Extensively documented polygonal masonry at Sacsayhuamán and other Peruvian sites. His photographic evidence of precision jointing is documented; interpretation of pre-Inca origins is inference.",
        "sources": [1171],
        "year_start": 2000,
        "year_end": None,
    },
    {
        "source": "Brien Foerster",
        "target": "Graham Hancock",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Collaborates with Hancock on South American research. Featured in Ancient Apocalypse. Both challenge mainstream chronology of Peruvian megalithic sites.",
        "sources": [1171],
        "year_start": 2010,
        "year_end": None,
    },
    # --- Christopher Dunn ---
    {
        "source": "Christopher Dunn",
        "target": "Great Sphinx",
        "type": "investigated",
        "tier": "credible",
        "desc": "Applied modern precision machining expertise to analyze Egyptian artifacts and temple surfaces, documenting tolerances and tool marks that he argues exceed known ancient capabilities. Technical observations are documented; 'power plant' theory is speculative.",
        "sources": [1173, 1174],
        "year_start": 1995,
        "year_end": None,
    },
    {
        "source": "Christopher Dunn",
        "target": "Flinders Petrie",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Dunn's precision machining analysis builds directly on Petrie's 1883 measurements of the Great Pyramid. Petrie documented the precision; Dunn interpreted it through modern engineering knowledge.",
        "sources": [1173, 1182],
        "year_start": 1998,
        "year_end": None,
    },
    # --- Flinders Petrie ---
    {
        "source": "Flinders Petrie",
        "target": "Great Sphinx",
        "type": "investigated",
        "tier": "documented",
        "desc": "Conducted the first precision survey of the Giza Plateau (1880-1882), documenting construction tolerances with unprecedented accuracy. His measurements remain foundational for all subsequent research, mainstream and alternative.",
        "sources": [1182, 1197],
        "year_start": 1880,
        "year_end": 1883,
    },
    # --- Edgar Cayce ---
    {
        "source": "Edgar Cayce",
        "target": "Great Sphinx",
        "type": "connected_to",
        "tier": "speculative",
        "desc": "Cayce's trance readings (1930s-40s) described a 'Hall of Records' buried beneath the Sphinx, containing records of Atlantean civilization. Unfalsifiable channeled material — no Hall of Records has been found, though seismic surveys have detected subsurface anomalies.",
        "sources": [1175, 1176, 1196],
        "year_start": 1933,
        "year_end": 1945,
    },
    {
        "source": "Edgar Cayce",
        "target": "Association for Research and Enlightenment",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded A.R.E. in 1931 to preserve and study his readings. The organization continues to this day in Virginia Beach.",
        "sources": [1175, 1176],
        "year_start": 1931,
        "year_end": 1945,
    },
    {
        "source": "Association for Research and Enlightenment",
        "target": "Great Sphinx",
        "type": "connected_to",
        "tier": "credible",
        "desc": "A.R.E. has funded archaeological investigations around the Sphinx to test Cayce's 'Hall of Records' prediction. The funding and investigations are documented; the motivation is prophetic.",
        "sources": [1175, 1196],
        "year_start": 1970,
        "year_end": None,
    },
    # --- Zecharia Sitchin ---
    {
        "source": "Zecharia Sitchin",
        "target": "Baalbek",
        "type": "connected_to",
        "tier": "speculative",
        "desc": "Sitchin claimed Baalbek's megalithic platform was a landing pad for Anunnaki spacecraft. His Sumerian translations are rejected by Assyriologists (Heiser, Kramer), making the Baalbek claim entirely speculative.",
        "sources": [1177, 1178],
        "year_start": 1976,
        "year_end": None,
    },
    {
        "source": "Zecharia Sitchin",
        "target": "Puma Punku",
        "type": "connected_to",
        "tier": "speculative",
        "desc": "Incorporated Tiwanaku/Puma Punku into his Earth Chronicles narrative as Anunnaki-related. Builds on Sitchin's discredited translations of Sumerian texts.",
        "sources": [1177],
        "year_start": 1976,
        "year_end": None,
    },
    {
        "source": "Michael Tellinger",
        "target": "Zecharia Sitchin",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Tellinger explicitly builds on Sitchin's Anunnaki framework. His 'Slave Species of the Gods' is a direct extension of Sitchin's Earth Chronicles thesis applied to southern African stone circles.",
        "sources": [1179],
        "year_start": 2005,
        "year_end": None,
    },
    # --- Michael Tellinger ---
    {
        "source": "Michael Tellinger",
        "target": "Smithsonian Institution",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Tellinger claims mainstream institutions ignore the stone circles of southern Africa. His 'Adam's Calendar' dating claims are rejected by mainstream archaeologists. The sites exist but conventional dating is much younger than he claims.",
        "sources": [1179, 1180, 1200],
        "year_start": 2003,
        "year_end": None,
    },
    # --- Walter Cruttenden ---
    {
        "source": "Walter Cruttenden",
        "target": "Binary Research Institute",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded BRI to research the binary star hypothesis for precession. Hosts the Conference on Precession and Ancient Knowledge (CPAK).",
        "sources": [1181, 1199],
        "year_start": 2001,
        "year_end": None,
    },
    {
        "source": "Walter Cruttenden",
        "target": "Younger Dryas Impact Hypothesis",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Cruttenden's binary orbit hypothesis implies cyclical catastrophic periods correlating with orbital position. The Younger Dryas event could fit this cycle, though the connection is speculative.",
        "sources": [1181],
        "year_start": 2006,
        "year_end": None,
    },
    # --- Yonaguni ---
    {
        "source": "Yonaguni Monument",
        "target": "Younger Dryas Impact Hypothesis",
        "type": "connected_to",
        "tier": "inference",
        "desc": "If man-made, Yonaguni would have been above water before post-glacial sea level rise (~10,000+ years ago), placing it in the same epoch as Younger Dryas events. Temporal correlation documented; causal connection speculative.",
        "sources": [1183, 1195],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Robert Schoch",
        "target": "Yonaguni Monument",
        "type": "investigated",
        "tier": "credible",
        "desc": "Schoch visited and assessed the Yonaguni Monument, concluding it is primarily a natural geological formation modified by natural erosion processes. His geological assessment contradicts Kimura's man-made interpretation.",
        "sources": [1184],
        "year_start": 1999,
        "year_end": 1999,
    },
    {
        "source": "Graham Hancock",
        "target": "Yonaguni Monument",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Featured Yonaguni in 'Underworld' (2002) as evidence for submerged civilizations predating sea level rise. Hancock sides with Kimura's man-made interpretation against Schoch's natural formation assessment.",
        "sources": [1195],
        "year_start": 2002,
        "year_end": None,
    },
    # --- Nan Madol ---
    {
        "source": "Nan Madol",
        "target": "Baalbek",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both involve transport and placement of massive stone blocks (basalt columns / limestone blocks) in seemingly impractical locations. Thematic comparison in alternative history literature — no direct historical connection.",
        "sources": [1187, 1188],
        "year_start": None,
        "year_end": None,
    },
    # --- Teotihuacan ---
    {
        "source": "Teotihuacan",
        "target": "Great Sphinx",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both feature precise astronomical alignment and remain enigmatic regarding their builders' identity and capabilities. Mercury found beneath Teotihuacan parallels mercury deposits associated with other ancient sites. Thematic parallel, not direct connection.",
        "sources": [1190, 1191],
        "year_start": None,
        "year_end": None,
    },
    # --- Derinkuyu ---
    {
        "source": "Derinkuyu",
        "target": "Gobekli Tepe",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both in Turkey, both demonstrate engineering capabilities that challenge assumptions about ancient societies. Gobekli Tepe's monumental construction predates agriculture; Derinkuyu's underground city demonstrates massive organized labor. No proven direct connection — separated by millennia.",
        "sources": [1185],
        "year_start": None,
        "year_end": None,
    },
    # --- Sacsayhuamán ---
    {
        "source": "Sacsayhuamán",
        "target": "Puma Punku",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Both Peruvian/Bolivian megalithic sites featuring extraordinary precision stonework. Academic connection through Protzen's research on Inca and Tiwanaku stone-cutting techniques. Question of whether megalithic foundations predate Inca overlay.",
        "sources": [1186],
        "year_start": None,
        "year_end": None,
    },
    # --- Carnac ---
    {
        "source": "Carnac Stones",
        "target": "Gobekli Tepe",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both demonstrate organized, large-scale monumental construction in the Neolithic period, challenging assumptions about pre-agricultural or early agricultural societies' organizational capabilities. Thematic parallel — no direct connection.",
        "sources": [1189],
        "year_start": None,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Brien Foerster": [1171, 1172],
    "Christopher Dunn": [1173, 1174],
    "Edgar Cayce": [1175, 1176, 1196],
    "Zecharia Sitchin": [1177, 1178],
    "Michael Tellinger": [1179, 1180, 1200],
    "Walter Cruttenden": [1181, 1199],
    "Flinders Petrie": [1182, 1197],
    "Yonaguni Monument": [1183, 1184, 1195],
    "Derinkuyu": [1185],
    "Sacsayhuamán": [1186],
    "Nan Madol": [1187, 1188],
    "Carnac Stones": [1189],
    "Teotihuacan": [1190, 1191],
    "Association for Research and Enlightenment": [1175, 1176],
    "Binary Research Institute": [1181, 1199],
}
