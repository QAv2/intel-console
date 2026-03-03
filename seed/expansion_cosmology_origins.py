"""
Cosmology & Origins — Suppressed History, Ancient Anomalies, Alternative Chronology.

Expansion layer for Intel Console.

Maps the researchers, sites, and evidence challenging mainstream historical
chronology. This is the most speculative expansion — evidence tiers are applied
with strict discipline. Most claims here are "credible" at best (legitimate
academic research that challenges consensus), many are "inference" (connecting
real evidence to larger theories), and some are "speculative" (claims requiring
substantially more evidence).

What IS documented: Gobekli Tepe's age (archaeological excavation), Younger
Dryas impact evidence published in PNAS/GSA/Nature, water erosion patterns on
the Sphinx enclosure (geological observation). What is inference or speculation:
the "lost civilization" thesis connecting these data points, Smithsonian
suppression allegations, extreme alternative chronologies.

Entities (~20): Sites (Gobekli Tepe, Puma Punku, Great Sphinx, Gunung Padang,
Baalbek), people (Graham Hancock, Randall Carlson, Robert Schoch, John Anthony
West, Klaus Schmidt, Danny Hilman Natawidjaja, Robert Bauval, Michael Cremo),
organizations (Smithsonian Institution, Geological Society of America),
concepts (Younger Dryas Impact Hypothesis).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85] — only if needed for suppression links

Evidence tiers (applied strictly):
  documented = archaeological record, peer-reviewed geology/archaeology, FOIA
  credible   = published geology challenging consensus, legitimate academic debate
  inference  = connecting documented evidence to larger theoretical frameworks
  speculative = claims rejected by mainstream without strong counter-evidence
"""

# ============================================================
# SOURCES — IDs 961-990
# ============================================================

SOURCES = [
    # --- Gobekli Tepe ---
    {
        "id": 961,
        "title": "Klaus Schmidt — 'Gobekli Tepe: A Stone Age Sanctuary in South-Eastern Anatolia' (ex oriente, 2012)",
        "url": "https://en.wikipedia.org/wiki/G%C3%B6bekli_Tepe",
        "source_type": "academic",
        "author": "Klaus Schmidt",
        "year": 2012,
    },
    {
        "id": 962,
        "title": "Dietrich et al. — 'The role of cult and feasting in the emergence of Neolithic communities' (Antiquity, 2012)",
        "url": "https://doi.org/10.1017/S0003598X00047840",
        "source_type": "academic",
        "author": "Oliver Dietrich et al.",
        "year": 2012,
    },
    {
        "id": 963,
        "title": "National Geographic — 'The Birth of Religion: The World's First Temple' (cover story, June 2011)",
        "url": "https://www.nationalgeographic.com/magazine/article/gobeki-tepe",
        "source_type": "journalism",
        "year": 2011,
    },
    # --- Younger Dryas Impact ---
    {
        "id": 964,
        "title": "Firestone et al. — 'Evidence for an extraterrestrial impact 12,900 years ago' (PNAS, 2007)",
        "url": "https://doi.org/10.1073/pnas.0706977104",
        "source_type": "academic",
        "author": "Richard B. Firestone et al.",
        "year": 2007,
    },
    {
        "id": 965,
        "title": "Kennett et al. — 'Nanodiamonds in the Younger Dryas boundary sediment layer' (Science, 2009)",
        "url": "https://doi.org/10.1126/science.1170تم1",
        "source_type": "academic",
        "author": "Douglas J. Kennett et al.",
        "year": 2009,
    },
    {
        "id": 966,
        "title": "Moore et al. — 'Sediment cores from White Pond, South Carolina, contain a platinum anomaly, pyrogenic carbon peak, and coprophilous spore decline at 12.8 ka' (Scientific Reports, 2019)",
        "url": "https://doi.org/10.1038/s41598-019-51552-8",
        "source_type": "academic",
        "author": "Christopher R. Moore et al.",
        "year": 2019,
    },
    {
        "id": 967,
        "title": "Wolbach et al. — 'Extraordinary Biomass-Burning Episode and Impact Winter Triggered by the Younger Dryas Cosmic Impact' (Journal of Geology, 2018)",
        "url": "https://doi.org/10.1086/695703",
        "source_type": "academic",
        "author": "Wendy S. Wolbach et al.",
        "year": 2018,
    },
    {
        "id": 968,
        "title": "Sweatman & Tsikritsis — 'Decoding Gobekli Tepe with Archaeoastronomy: What Does the Fox Say?' (Mediterranean Archaeology and Archaeometry, 2017)",
        "url": "https://doi.org/10.5281/zenodo.400780",
        "source_type": "academic",
        "author": "Martin B. Sweatman, Dimitrios Tsikritsis",
        "year": 2017,
    },
    # --- Sphinx Water Erosion ---
    {
        "id": 969,
        "title": "Robert Schoch — 'Redating the Great Sphinx of Giza' (presented at GSA annual meeting, 1991; published in KMT: A Modern Journal of Ancient Egypt, 1992)",
        "url": "https://www.robertschoch.com/sphinxcontent.html",
        "source_type": "academic",
        "author": "Robert M. Schoch",
        "year": 1992,
    },
    {
        "id": 970,
        "title": "Robert Schoch — 'Voices of the Rocks: A Scientist Looks at Catastrophes and Ancient Civilizations' (Harmony Books, 1999)",
        "url": "https://en.wikipedia.org/wiki/Robert_M._Schoch",
        "source_type": "book",
        "author": "Robert M. Schoch",
        "year": 1999,
    },
    {
        "id": 971,
        "title": "John Anthony West — 'Serpent in the Sky: The High Wisdom of Ancient Egypt' (Julian Press, 1993 revised edition)",
        "url": "https://en.wikipedia.org/wiki/John_Anthony_West",
        "source_type": "book",
        "author": "John Anthony West",
        "year": 1993,
    },
    # --- Graham Hancock ---
    {
        "id": 972,
        "title": "Graham Hancock — 'Fingerprints of the Gods: The Evidence of Earth's Lost Civilization' (Crown, 1995)",
        "url": "https://en.wikipedia.org/wiki/Fingerprints_of_the_Gods",
        "source_type": "book",
        "author": "Graham Hancock",
        "year": 1995,
    },
    {
        "id": 973,
        "title": "Graham Hancock — 'Magicians of the Gods: The Forgotten Wisdom of Earth's Lost Civilization' (Coronet, 2015)",
        "url": "https://en.wikipedia.org/wiki/Magicians_of_the_Gods",
        "source_type": "book",
        "author": "Graham Hancock",
        "year": 2015,
    },
    {
        "id": 974,
        "title": "Netflix — 'Ancient Apocalypse' Season 1 (Graham Hancock, 2022)",
        "url": "https://en.wikipedia.org/wiki/Ancient_Apocalypse",
        "source_type": "documentary",
        "author": "Graham Hancock",
        "year": 2022,
    },
    # --- Randall Carlson ---
    {
        "id": 975,
        "title": "Randall Carlson — 'Kosmographia' podcast and published lectures on Younger Dryas impact geology and sacred geometry",
        "url": "https://randallcarlson.com/",
        "source_type": "other",
        "author": "Randall Carlson",
        "year": 2015,
    },
    # --- Bauval ---
    {
        "id": 976,
        "title": "Robert Bauval — 'The Orion Mystery: Unlocking the Secrets of the Pyramids' (Crown, 1994)",
        "url": "https://en.wikipedia.org/wiki/The_Orion_Mystery",
        "source_type": "book",
        "author": "Robert Bauval",
        "year": 1994,
    },
    {
        "id": 977,
        "title": "Robert Bauval & Graham Hancock — 'The Message of the Sphinx: A Quest for the Hidden Legacy of Mankind' (Crown, 1996)",
        "url": "https://en.wikipedia.org/wiki/Robert_Bauval",
        "source_type": "book",
        "author": "Robert Bauval, Graham Hancock",
        "year": 1996,
    },
    # --- Cremo ---
    {
        "id": 978,
        "title": "Michael Cremo & Richard Thompson — 'Forbidden Archaeology: The Hidden History of the Human Race' (Bhaktivedanta Institute, 1993)",
        "url": "https://en.wikipedia.org/wiki/Forbidden_Archeology",
        "source_type": "book",
        "author": "Michael Cremo, Richard Thompson",
        "year": 1993,
    },
    # --- Gunung Padang ---
    {
        "id": 979,
        "title": "Natawidjaja et al. — 'Geo-archaeological prospecting of Gunung Padang megalithic site' (presented at AGU Fall Meeting, 2013)",
        "url": "https://en.wikipedia.org/wiki/Gunung_Padang",
        "source_type": "academic",
        "author": "Danny Hilman Natawidjaja et al.",
        "year": 2013,
    },
    {
        "id": 980,
        "title": "Natawidjaja et al. — 'Geo-archaeological evidence of a buried megalithic pyramid at Gunung Padang, West Java' (Archaeological Prospection, 2024)",
        "url": "https://doi.org/10.1002/arp.1912",
        "source_type": "academic",
        "author": "Danny Hilman Natawidjaja et al.",
        "year": 2024,
    },
    # --- Puma Punku ---
    {
        "id": 981,
        "title": "Jean-Pierre Protzen & Stella Nair — 'Who Taught the Inca Stonemasons Their Skills? A Comparison of Tiahuanaco and Inca Cut-Stone Masonry' (JSAH, 1997)",
        "url": "https://doi.org/10.2307/991200",
        "source_type": "academic",
        "author": "Jean-Pierre Protzen, Stella Nair",
        "year": 1997,
    },
    {
        "id": 982,
        "title": "Alexei Vranich — 'The Construction and Reconstruction of Ritual Space at Tiwanaku, Bolivia' (Journal of Field Archaeology, 2006)",
        "url": "https://doi.org/10.1179/009346906791071972",
        "source_type": "academic",
        "author": "Alexei Vranich",
        "year": 2006,
    },
    # --- Baalbek ---
    {
        "id": 983,
        "title": "Daniel Lohmann — 'Giant Strides towards Monumentality: The Architecture of the Jupiter Sanctuary in Baalbek/Heliopolis' (Bollettino di Archeologia Online, 2010)",
        "url": "https://en.wikipedia.org/wiki/Baalbek",
        "source_type": "academic",
        "author": "Daniel Lohmann",
        "year": 2010,
    },
    # --- Smithsonian suppression allegations ---
    {
        "id": 984,
        "title": "Vine Deloria Jr. — 'Red Earth, White Lies: Native Americans and the Myth of Scientific Fact' (Fulcrum, 1997)",
        "url": "https://en.wikipedia.org/wiki/Vine_Deloria_Jr.",
        "source_type": "book",
        "author": "Vine Deloria Jr.",
        "year": 1997,
    },
    {
        "id": 985,
        "title": "Smithsonian Institution — Annual Reports documenting mound surveys (Bureau of Ethnology, 1882-1895)",
        "url": "https://www.si.edu/object/siris_sil_877528",
        "source_type": "archive",
        "year": 1894,
    },
    # --- General / Cross-cutting ---
    {
        "id": 986,
        "title": "Joe Rogan Experience #872 — Graham Hancock & Randall Carlson (2016, 3.5 hrs)",
        "url": "https://en.wikipedia.org/wiki/The_Joe_Rogan_Experience",
        "source_type": "other",
        "year": 2016,
    },
    {
        "id": 987,
        "title": "Joe Rogan Experience #1284 — Graham Hancock (2019, discusses Younger Dryas evidence updates)",
        "url": "https://en.wikipedia.org/wiki/The_Joe_Rogan_Experience",
        "source_type": "other",
        "year": 2019,
    },
    {
        "id": 988,
        "title": "SAA (Society for American Archaeology) — open letter criticizing Netflix 'Ancient Apocalypse' (2022)",
        "url": "https://www.saa.org/quick-nav/saa-media-room/saa-news/2022/12/01/saa-letter-to-netflix",
        "source_type": "academic",
        "year": 2022,
    },
    {
        "id": 989,
        "title": "Clube & Napier — 'The Cosmic Serpent: A Catastrophist Approach to Earth History' (Faber & Faber, 1982)",
        "url": "https://en.wikipedia.org/wiki/Victor_Clube",
        "source_type": "book",
        "author": "Victor Clube, Bill Napier",
        "year": 1982,
    },
    {
        "id": 990,
        "title": "Holliday et al. — 'The Younger Dryas impact hypothesis: A requiem' (Earth-Science Reviews, 2023 — critical review of YDIH evidence)",
        "url": "https://doi.org/10.1016/j.earscirev.2023.104521",
        "source_type": "academic",
        "author": "Vance T. Holliday et al.",
        "year": 2023,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Sites/Discoveries ---
    {
        "name": "Gobekli Tepe",
        "entity_type": "facility",
        "description": "Megalithic sanctuary in southeastern Turkey, dated to ~9600-8000 BCE by radiocarbon — at least 6,000 years older than Stonehenge. Excavated by Klaus Schmidt (1995-2014). Features massive T-shaped limestone pillars (up to 6m, 10+ tons) with carved animal reliefs, arranged in circular enclosures. Pre-dates agriculture, pottery, and metallurgy, overturning the assumption that complex monumental construction required settled agricultural society. UNESCO World Heritage Site since 2018.",
        "aliases": "Gobekli Tepe, Potbelly Hill",
        "metadata": {"location": "Sanliurfa Province, Turkey", "date_range": "~9600-8000 BCE"},
    },
    {
        "name": "Puma Punku",
        "entity_type": "facility",
        "description": "Part of the Tiwanaku complex near Lake Titicaca, Bolivia, at 3,850m elevation. Features precision-cut andesite and diorite blocks (one estimated at 131 metric tons) with interlocking H-shaped blocks and flat surfaces. Mainstream dating: ~536-600 CE (Tiwanaku V period). The precision of stone-cutting and scale of material transport remain subjects of academic debate — some blocks sourced from quarries 10+ km away at high altitude.",
        "aliases": "Pumapunku, Puma Puncu",
        "metadata": {"location": "Tiwanaku, Bolivia", "date_range": "~536-600 CE (mainstream)"},
    },
    {
        "name": "Great Sphinx",
        "entity_type": "facility",
        "description": "Limestone monument on the Giza Plateau, Egypt. Mainstream dating: ~2500 BCE (reign of Pharaoh Khafre, 4th Dynasty). Robert Schoch's geological analysis (1991) identified vertical weathering patterns in the Sphinx enclosure consistent with prolonged rainfall erosion — precipitation levels not seen in Egypt since before ~5000 BCE (possibly much earlier). This 'water erosion hypothesis' implies the Sphinx core may predate the conventionally accepted date by thousands of years. Debated but not refuted by geologists.",
        "aliases": "Sphinx of Giza",
        "metadata": {"location": "Giza, Egypt", "date_mainstream": "~2500 BCE"},
    },
    {
        "name": "Younger Dryas Impact Hypothesis",
        "entity_type": "event",
        "description": "Scientific hypothesis proposing that one or more extraterrestrial impacts or airbursts ~12,800 years ago triggered the Younger Dryas cold period, megafaunal extinctions, and the collapse of the Clovis culture. First formally proposed by Firestone et al. in PNAS (2007). Supporting evidence includes platinum anomalies, nanodiamonds, meltglass, and biomass-burning markers in the boundary layer across multiple continents. Published in PNAS, Science, Nature, GSA, and Journal of Geology. Remains actively debated — some researchers have published critiques questioning the impact markers.",
        "aliases": "YDIH, Younger Dryas Boundary event, YDB hypothesis",
        "metadata": {"date": "~12,800 years ago", "status": "active scientific debate"},
    },
    {
        "name": "Gunung Padang",
        "entity_type": "facility",
        "description": "Megalithic site on a volcanic hill in West Java, Indonesia. Surface layer of columnar basalt arrangements dated to ~3000 BCE. Controversial deep-layer dating by Danny Hilman Natawidjaja and team claims buried construction as old as ~25,000-27,000 years (based on radiocarbon of soil between stone layers), which would make it the oldest known pyramid-like structure. Published in Archaeological Prospection (2024) but disputed — critics argue the radiocarbon dates reflect natural geological formations, not human construction. Indonesian government has both supported and distanced itself from the claims.",
        "aliases": "Gunung Padang Megalithic Site",
        "metadata": {"location": "Cianjur, West Java, Indonesia", "date_range": "~3000 BCE surface; deep dating disputed"},
    },
    {
        "name": "Baalbek",
        "entity_type": "facility",
        "description": "Ancient temple complex in Lebanon's Beqaa Valley. Roman-era Temple of Jupiter sits atop a massive pre-Roman platform featuring the 'Trilithon' — three stones each weighing ~800 metric tons, among the largest cut stones in the ancient world. A fourth unfinished block ('Stone of the Pregnant Woman,' ~1,000 tons) remains in the quarry. While Roman attribution is documented, the megalithic foundation platform's construction methods and dating remain debated. The engineering required to move 800-ton blocks is extraordinary by any historical standard.",
        "aliases": "Heliopolis, Baalbek temple complex",
        "metadata": {"location": "Beqaa Valley, Lebanon", "date_range": "Roman temple 1st-3rd c. CE; platform debated"},
    },
    # --- People ---
    {
        "name": "Graham Hancock",
        "entity_type": "person",
        "description": "British journalist and author. Best known for 'Fingerprints of the Gods' (1995) which proposed an advanced civilization existed before the Ice Age and was destroyed by cataclysm ~12,800 years ago. Updated thesis in 'Magicians of the Gods' (2015) incorporating Younger Dryas impact evidence. Netflix series 'Ancient Apocalypse' (2022) drew both massive viewership and sharp criticism from academic archaeology (SAA open letter). Not an archaeologist — a journalist who synthesizes evidence from multiple fields into a speculative framework.",
        "aliases": "",
        "metadata": {"role": "journalist / author", "years_active": "1995-present"},
    },
    {
        "name": "Randall Carlson",
        "entity_type": "person",
        "description": "Geologist, master builder, and independent researcher specializing in catastrophism and sacred geometry. Has conducted extensive geological fieldwork documenting evidence of catastrophic flooding in the Pacific Northwest (Channeled Scablands) consistent with Younger Dryas meltwater events. Collaborates with Graham Hancock. His geological observations — documented in field photographs and geological surveys — are more rigorous than the speculative frameworks they are sometimes used to support. Presents research through Kosmographia podcast and lectures.",
        "aliases": "",
        "metadata": {"role": "geologist / researcher", "years_active": "1990s-present"},
    },
    {
        "name": "Robert Schoch",
        "entity_type": "person",
        "description": "Geologist and associate professor at Boston University (College of General Studies). Presented the Sphinx water erosion hypothesis at the 1991 GSA annual meeting and in peer-reviewed publications. His geological analysis of vertical weathering patterns in the Sphinx enclosure remains the most substantive scientific challenge to mainstream Egyptological dating. Endorsed by geologists who reviewed the rock; contested by Egyptologists on archaeological grounds. Later work on 'solar outburst' theory at end of Ice Age is more speculative.",
        "aliases": "Robert M. Schoch",
        "metadata": {"role": "geologist / Boston University", "years_active": "1991-present"},
    },
    {
        "name": "John Anthony West",
        "entity_type": "person",
        "description": "Independent Egyptologist and author (1932-2018). Authored 'Serpent in the Sky' (1979, revised 1993), which drew on R.A. Schwaller de Lubicz's work to argue Egyptian civilization was far older than conventionally accepted. Recruited Robert Schoch to conduct geological analysis of the Sphinx. Their collaboration produced the water erosion hypothesis. Won Emmy for documentary 'Mystery of the Sphinx' (1993, hosted by Charlton Heston). Not formally trained as a geologist — his contribution was the question, not the geological analysis.",
        "aliases": "JAW",
        "metadata": {"role": "author / independent Egyptologist", "years_active": "1979-2018"},
    },
    {
        "name": "Klaus Schmidt",
        "entity_type": "person",
        "description": "German archaeologist (1953-2014) at the German Archaeological Institute (DAI). Led excavations at Gobekli Tepe from 1995 until his death. His work established the site's radiocarbon-confirmed dating (Pre-Pottery Neolithic A/B, ~9600-8000 BCE) and its revolutionary implication: complex monumental architecture preceded agriculture. Famous statement: 'First came the temple, then the city.' His work is mainstream accepted archaeology that nonetheless overturned longstanding assumptions about the Neolithic Revolution.",
        "aliases": "",
        "metadata": {"role": "archaeologist / DAI", "years_active": "1995-2014"},
    },
    {
        "name": "Danny Hilman Natawidjaja",
        "entity_type": "person",
        "description": "Indonesian geologist at the Indonesian Institute of Sciences (LIPI/BRIN). Led geological surveys at Gunung Padang using ground-penetrating radar, seismic tomography, and core drilling. Published controversial deep-layer dating claims (up to ~27,000 years) in Archaeological Prospection (2024). His work has been both promoted by the Indonesian government and criticized by archaeologists who question whether the deep radiocarbon dates reflect human construction rather than natural geological features.",
        "aliases": "Danny Hilman",
        "metadata": {"role": "geologist / BRIN Indonesia", "years_active": "2011-present"},
    },
    {
        "name": "Robert Bauval",
        "entity_type": "person",
        "description": "Belgian-born author of Egyptian origin. Proposed the Orion Correlation Theory (1994): the three Giza pyramids were positioned to mirror Orion's Belt, with the Nile representing the Milky Way. Published 'The Orion Mystery' (1994) and co-authored 'The Message of the Sphinx' with Graham Hancock (1996). The pattern-matching claim is visually suggestive but astronomically and archaeologically contested — mainstream Egyptologists consider it pseudoarchaeology. The hypothesis is unfalsifiable as presented.",
        "aliases": "",
        "metadata": {"role": "author / researcher", "years_active": "1994-present"},
    },
    {
        "name": "Michael Cremo",
        "entity_type": "person",
        "description": "Author and researcher associated with the Bhaktivedanta Institute (Hare Krishna). Co-authored 'Forbidden Archaeology' (1993) with Richard Thompson, cataloguing anomalous archaeological finds (human artifacts in geologically ancient strata) that were allegedly ignored or suppressed by mainstream science. The book's thesis — that anatomically modern humans have existed for millions of years — is rejected by virtually all mainstream archaeologists and geologists. Motivated by Vedic cosmology rather than empirical methodology. Included here as the extreme end of alternative chronology.",
        "aliases": "Michael A. Cremo",
        "metadata": {"role": "author / Vedic researcher", "years_active": "1993-present"},
    },
    # --- Organizations ---
    {
        "name": "Smithsonian Institution",
        "entity_type": "organization",
        "description": "World's largest museum and research complex (est. 1846). Bureau of Ethnology (1879-1965) conducted systematic surveys of Native American mounds, producing landmark publications. Allegations of suppression: critics (notably Vine Deloria Jr.) accuse the Smithsonian of dismissing or losing anomalous finds (giant skeletons, pre-Clovis artifacts) that challenged prevailing paradigms. Some documented cases of artifacts entering collections and not being published exist, but systematic intentional suppression is unproven. The institution's sheer size means items can be effectively 'lost' without conspiracy.",
        "aliases": "Smithsonian, SI",
        "metadata": {"type": "museum / research complex", "founded": 1846},
    },
    {
        "name": "Geological Society of America",
        "entity_type": "organization",
        "description": "Major professional geoscience organization (est. 1888). Relevant here because GSA meetings and publications have been venues for both the Sphinx water erosion hypothesis (Schoch's 1991 presentation) and Younger Dryas impact research. The fact that these heterodox ideas were presented at GSA distinguishes them from fringe claims — they entered the peer-review process and received serious geological consideration, even when they challenged archaeological consensus.",
        "aliases": "GSA",
        "metadata": {"type": "scientific society", "founded": 1888},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Gobekli Tepe ---
    {
        "source": "Klaus Schmidt",
        "target": "Gobekli Tepe",
        "type": "investigated",
        "tier": "documented",
        "desc": "Led excavations at Gobekli Tepe from 1995 until his death in 2014. Established the site's Pre-Pottery Neolithic dating (~9600-8000 BCE) through standard radiocarbon methods, overturning assumptions about the Neolithic Revolution.",
        "sources": [961, 962, 963],
        "year_start": 1995,
        "year_end": 2014,
    },
    {
        "source": "Gobekli Tepe",
        "target": "Younger Dryas Impact Hypothesis",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Gobekli Tepe's construction begins near the end of the Younger Dryas (~9600 BCE). Sweatman & Tsikritsis (2017) proposed Pillar 43 encodes a comet impact event. The temporal proximity is documented; the causal connection is speculative interpretation of iconography.",
        "sources": [961, 968],
        "year_start": None,
        "year_end": None,
    },
    # --- Sphinx Water Erosion ---
    {
        "source": "Robert Schoch",
        "target": "Great Sphinx",
        "type": "investigated",
        "tier": "credible",
        "desc": "Conducted geological analysis identifying vertical precipitation-induced weathering patterns in the Sphinx enclosure (1991). Presented at GSA. Implies the Sphinx core predates the conventional ~2500 BCE date by potentially thousands of years. Published geological work, debated but not refuted on geological grounds.",
        "sources": [969, 970],
        "year_start": 1991,
        "year_end": None,
    },
    {
        "source": "John Anthony West",
        "target": "Robert Schoch",
        "type": "connected_to",
        "tier": "documented",
        "desc": "West recruited Schoch to apply geological analysis to the Sphinx. West provided the hypothesis (from Schwaller de Lubicz), Schoch provided the geological expertise. Their collaboration produced the water erosion thesis.",
        "sources": [969, 971],
        "year_start": 1990,
        "year_end": 1993,
    },
    {
        "source": "John Anthony West",
        "target": "Great Sphinx",
        "type": "investigated",
        "tier": "credible",
        "desc": "Challenged mainstream Sphinx dating based on Schwaller de Lubicz's observation of water erosion. Emmy-winning documentary 'Mystery of the Sphinx' (1993). His contribution was the question; Schoch provided the geological evidence.",
        "sources": [971],
        "year_start": 1979,
        "year_end": 2018,
    },
    {
        "source": "Robert Schoch",
        "target": "Geological Society of America",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Presented Sphinx water erosion hypothesis at the 1991 GSA annual meeting. The presentation at a major geological society distinguishes this from fringe claims — it entered the peer-review process.",
        "sources": [969],
        "year_start": 1991,
        "year_end": 1991,
    },
    # --- Graham Hancock ---
    {
        "source": "Graham Hancock",
        "target": "Younger Dryas Impact Hypothesis",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Hancock adopted the Younger Dryas impact as the cataclysmic mechanism for his lost civilization thesis in 'Magicians of the Gods' (2015). The scientific evidence for the impact event is independent of Hancock's broader claims — he connects real evidence to a speculative framework.",
        "sources": [973, 974],
        "year_start": 2015,
        "year_end": None,
    },
    {
        "source": "Graham Hancock",
        "target": "Gobekli Tepe",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Hancock argues Gobekli Tepe represents a remnant or teaching site of a pre-Ice Age civilization. The site's documented age is used as evidence, but the 'lost civilization' interpretation goes far beyond what the archaeological record supports.",
        "sources": [973, 974],
        "year_start": 2015,
        "year_end": None,
    },
    {
        "source": "Graham Hancock",
        "target": "Great Sphinx",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Co-authored 'The Message of the Sphinx' with Bauval (1996). Argues the Sphinx is far older than mainstream dating, incorporating Schoch's water erosion evidence into his lost civilization framework.",
        "sources": [972, 977],
        "year_start": 1995,
        "year_end": None,
    },
    {
        "source": "Graham Hancock",
        "target": "Randall Carlson",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Documented collaboration: joint Joe Rogan appearances (2016, 2019), shared fieldwork, complementary research. Carlson provides geological evidence for catastrophism; Hancock synthesizes it into civilizational narrative.",
        "sources": [975, 986, 987],
        "year_start": 2015,
        "year_end": None,
    },
    # --- Randall Carlson ---
    {
        "source": "Randall Carlson",
        "target": "Younger Dryas Impact Hypothesis",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Independently researched geological evidence for catastrophic Younger Dryas flooding in the Pacific Northwest (Channeled Scablands). His geological fieldwork documenting meltwater features is more rigorous than the broader speculative frameworks it supports.",
        "sources": [975, 986],
        "year_start": 1990,
        "year_end": None,
    },
    # --- Younger Dryas Impact — Scientific Record ---
    {
        "source": "Younger Dryas Impact Hypothesis",
        "target": "Geological Society of America",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Multiple YDI papers presented at GSA meetings and published in GSA-affiliated journals. The hypothesis has been taken seriously enough for sustained peer-reviewed debate in major geological venues, even as some researchers contest the evidence.",
        "sources": [964, 966, 967, 990],
        "year_start": 2007,
        "year_end": None,
    },
    # --- Bauval ---
    {
        "source": "Robert Bauval",
        "target": "Great Sphinx",
        "type": "connected_to",
        "tier": "speculative",
        "desc": "Orion Correlation Theory (1994): proposed Giza pyramids mirror Orion's Belt. Pattern-matching is visually suggestive but astronomically contested. Co-authored 'The Message of the Sphinx' with Hancock. Mainstream Egyptology considers this pseudoarchaeology.",
        "sources": [976, 977],
        "year_start": 1994,
        "year_end": None,
    },
    {
        "source": "Robert Bauval",
        "target": "Graham Hancock",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Co-authored 'The Message of the Sphinx' (1996). Bauval's Orion Correlation combined with Hancock's lost civilization thesis. Long-standing collaboration in alternative Egyptology.",
        "sources": [977],
        "year_start": 1996,
        "year_end": None,
    },
    # --- Smithsonian ---
    {
        "source": "Smithsonian Institution",
        "target": "Gobekli Tepe",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Smithsonian Magazine has published extensively on Gobekli Tepe. The institution's mainstream coverage of the site represents acceptance of the documented archaeology, not the speculative interpretations layered onto it.",
        "sources": [963],
        "year_start": 2008,
        "year_end": None,
    },
    {
        "source": "Michael Cremo",
        "target": "Smithsonian Institution",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Cremo alleges Smithsonian systematically ignored or suppressed anomalous archaeological finds. Some documented cases of artifacts entering collections and not being published, but systematic intentional suppression is unproven. Deloria also made similar allegations regarding Native American evidence.",
        "sources": [978, 984, 985],
        "year_start": 1993,
        "year_end": None,
    },
    # --- Gunung Padang ---
    {
        "source": "Danny Hilman Natawidjaja",
        "target": "Gunung Padang",
        "type": "investigated",
        "tier": "credible",
        "desc": "Led geological survey using GPR, seismic tomography, and core drilling. Published deep-layer dating claims (up to ~27,000 years) in Archaeological Prospection (2024). Published but disputed — critics question whether radiocarbon dates reflect human construction vs. natural geology.",
        "sources": [979, 980],
        "year_start": 2011,
        "year_end": None,
    },
    {
        "source": "Graham Hancock",
        "target": "Gunung Padang",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Hancock featured Gunung Padang in 'Ancient Apocalypse' (2022) as evidence for his lost civilization thesis. The site's controversial deep dating aligns with his pre-Ice Age framework but the dating itself remains disputed.",
        "sources": [974, 979],
        "year_start": 2022,
        "year_end": None,
    },
    # --- Cremo ---
    {
        "source": "Michael Cremo",
        "target": "Puma Punku",
        "type": "connected_to",
        "tier": "speculative",
        "desc": "Cremo cites Tiwanaku/Puma Punku as evidence for his extreme alternative chronology. His claims about the site far exceed the archaeological evidence and are rejected by mainstream researchers. Included as the speculative extreme.",
        "sources": [978],
        "year_start": 1993,
        "year_end": None,
    },
    # --- Academic controversy ---
    {
        "source": "Graham Hancock",
        "target": "Smithsonian Institution",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Hancock has alleged that mainstream archaeological institutions, including the Smithsonian, resist evidence challenging established chronology. The SAA (not Smithsonian) issued an open letter against his Netflix series. Institutional resistance is documented; intentional suppression is unproven.",
        "sources": [974, 988],
        "year_start": 2022,
        "year_end": None,
    },
    # --- Baalbek ---
    {
        "source": "Baalbek",
        "target": "Puma Punku",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both sites feature megalithic blocks of extraordinary size and precision that stretch the limits of conventionally understood ancient engineering. Often compared in alternative history literature. The connection is thematic — no direct historical link is established.",
        "sources": [983, 981],
        "year_start": None,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Gobekli Tepe": [961, 962, 963, 968],
    "Puma Punku": [981, 982],
    "Great Sphinx": [969, 970, 971, 976, 977],
    "Younger Dryas Impact Hypothesis": [964, 965, 966, 967, 989, 990],
    "Gunung Padang": [979, 980],
    "Baalbek": [983],
    "Graham Hancock": [972, 973, 974, 977, 986, 987],
    "Randall Carlson": [975, 986, 987],
    "Robert Schoch": [969, 970],
    "John Anthony West": [971],
    "Klaus Schmidt": [961, 962],
    "Danny Hilman Natawidjaja": [979, 980],
    "Robert Bauval": [976, 977],
    "Michael Cremo": [978],
    "Smithsonian Institution": [984, 985],
    "Geological Society of America": [964, 969],
}
