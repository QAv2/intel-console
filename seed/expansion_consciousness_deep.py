"""
Consciousness / Psi Research DEEP — Expansion layer for Intel Console.

Goes deeper on the government psi programs mapped in expansion_consciousness.py.
Adds the researchers, organizations, and sub-programs that didn't make the first
pass: the statistician who proved it worked (Jessica Utts), the military trainers
who operationalized it (Paul Smith, Lyn Buchanan, David Morehouse), the Army's
psi researcher who connected it to UFOs (Andrija Puharich), the scientist who
bridged psi and UFO phenomena (Jacques Vallée), and the organizations that
continued the work after government "termination" (IONS, SAIC, Farsight, PSI Tech).

The key story: the government didn't end psi research in 1995 — it transferred
capabilities to private sector contractors (SAIC) and commercial ventures (PSI
Tech, Farsight Institute) staffed by the same people who ran the classified programs.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], NSA [86], DIA, Project Stargate, Gateway Process, SRI International,
  Monroe Institute, Ingo Swann, Hal Puthoff, Russell Targ, Pat Price,
  Joseph McMoneagle, Edwin May, Dale Graff, Albert Stubblebine,
  Stargate Declassification, Church Committee [338]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1141-1170
# ============================================================

SOURCES = [
    # --- Dean Radin / IONS ---
    {
        "id": 1141,
        "title": "Dean Radin — 'The Conscious Universe: The Scientific Truth of Psychic Phenomena' (HarperOne, 1997)",
        "url": "https://en.wikipedia.org/wiki/Dean_Radin",
        "source_type": "book",
        "author": "Dean Radin",
        "year": 1997,
    },
    {
        "id": 1142,
        "title": "Dean Radin — 'Entangled Minds: Extrasensory Experiences in a Quantum Reality' (Paraview Pocket Books, 2006)",
        "url": "https://en.wikipedia.org/wiki/Dean_Radin",
        "source_type": "book",
        "author": "Dean Radin",
        "year": 2006,
    },
    {
        "id": 1143,
        "title": "Dean Radin — 'Real Magic: Ancient Wisdom, Modern Science, and a Guide to the Secret Power of the Universe' (Harmony, 2018)",
        "url": "https://en.wikipedia.org/wiki/Dean_Radin",
        "source_type": "book",
        "author": "Dean Radin",
        "year": 2018,
    },
    {
        "id": 1144,
        "title": "Institute of Noetic Sciences (IONS) — official website and research programs",
        "url": "https://noetic.org/",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 1145,
        "title": "Edgar Mitchell — founding of IONS after Apollo 14 consciousness experience (1973)",
        "url": "https://en.wikipedia.org/wiki/Institute_of_Noetic_Sciences",
        "source_type": "other",
        "year": 1973,
    },
    # --- Jessica Utts ---
    {
        "id": 1146,
        "title": "Jessica Utts — 'An Assessment of the Evidence for Psychic Functioning' (Journal of Scientific Exploration, 1996)",
        "url": "https://www.ics.uci.edu/~jutts/air.pdf",
        "source_type": "academic",
        "author": "Jessica Utts",
        "year": 1996,
    },
    {
        "id": 1147,
        "title": "Utts & Hyman — Debate on statistical evidence for psi in the AIR review of Stargate (1995)",
        "url": "https://www.ics.uci.edu/~jutts/hyman.html",
        "source_type": "academic",
        "author": "Jessica Utts, Ray Hyman",
        "year": 1995,
    },
    # --- Military Remote Viewers / Trainers ---
    {
        "id": 1148,
        "title": "Paul H. Smith — 'Reading the Enemy's Mind: Inside Star Gate, America's Psychic Espionage Program' (Tor Books, 2005)",
        "url": "https://en.wikipedia.org/wiki/Paul_H._Smith",
        "source_type": "book",
        "author": "Paul H. Smith",
        "year": 2005,
    },
    {
        "id": 1149,
        "title": "Lyn Buchanan — 'The Seventh Sense: The Secrets of Remote Viewing as Told by a Psychic Spy for the U.S. Military' (Paraview, 2003)",
        "url": "https://en.wikipedia.org/wiki/Lyn_Buchanan",
        "source_type": "book",
        "author": "Lyn Buchanan",
        "year": 2003,
    },
    {
        "id": 1150,
        "title": "David Morehouse — 'Psychic Warrior: The True Story of America's Foremost Psychic Spy' (St. Martin's, 1996)",
        "url": "https://en.wikipedia.org/wiki/David_Morehouse",
        "source_type": "book",
        "author": "David Morehouse",
        "year": 1996,
    },
    {
        "id": 1151,
        "title": "Angela Dellafiora Ford — DIA remote viewer who located fugitive Charles Jordan (1989, declassified)",
        "url": "https://www.cia.gov/readingroom/collection/stargate",
        "source_type": "government",
        "year": 1989,
    },
    # --- Jim Marrs ---
    {
        "id": 1152,
        "title": "Jim Marrs — 'PSI Spies: The True Story of America's Psychic Warfare Program' (New Page Books, 2007)",
        "url": "https://en.wikipedia.org/wiki/Jim_Marrs",
        "source_type": "book",
        "author": "Jim Marrs",
        "year": 2007,
    },
    # --- Andrija Puharich ---
    {
        "id": 1153,
        "title": "Andrija Puharich — 'The Sacred Mushroom: Key to the Door of Eternity' (Doubleday, 1959)",
        "url": "https://en.wikipedia.org/wiki/Andrija_Puharich",
        "source_type": "book",
        "author": "Andrija Puharich",
        "year": 1959,
    },
    {
        "id": 1154,
        "title": "Andrija Puharich — 'Uri: A Journal of the Mystery of Uri Geller' (Anchor, 1974)",
        "url": "https://en.wikipedia.org/wiki/Andrija_Puharich",
        "source_type": "book",
        "author": "Andrija Puharich",
        "year": 1974,
    },
    {
        "id": 1155,
        "title": "Andrija Puharich — U.S. Army psi research at Camp Detrick and Round Table Foundation (1950s-60s)",
        "url": "https://en.wikipedia.org/wiki/Andrija_Puharich",
        "source_type": "other",
        "year": 1960,
    },
    # --- Jacques Vallée ---
    {
        "id": 1156,
        "title": "Jacques Vallée — 'Passport to Magonia: From Folklore to Flying Saucers' (Regnery, 1969)",
        "url": "https://en.wikipedia.org/wiki/Jacques_Vall%C3%A9e",
        "source_type": "book",
        "author": "Jacques Vallée",
        "year": 1969,
    },
    {
        "id": 1157,
        "title": "Jacques Vallée — 'Messengers of Deception: UFO Contacts and Cults' (And/Or Press, 1979)",
        "url": "https://en.wikipedia.org/wiki/Jacques_Vall%C3%A9e",
        "source_type": "book",
        "author": "Jacques Vallée",
        "year": 1979,
    },
    {
        "id": 1158,
        "title": "Jacques Vallée — 'Forbidden Science' journal series (volumes 1-4, documenting psi research and UFO investigations from inside)",
        "url": "https://en.wikipedia.org/wiki/Jacques_Vall%C3%A9e",
        "source_type": "book",
        "author": "Jacques Vallée",
        "year": 1992,
    },
    # --- SAIC ---
    {
        "id": 1159,
        "title": "SAIC — Science Applications International Corporation took over Stargate research from SRI (1991-1995)",
        "url": "https://en.wikipedia.org/wiki/Science_Applications_International_Corporation",
        "source_type": "other",
        "year": 1995,
    },
    # --- PSI Tech ---
    {
        "id": 1160,
        "title": "PSI Tech — Technical Remote Viewing company founded by military Stargate personnel (Ed Dames)",
        "url": "https://en.wikipedia.org/wiki/Ed_Dames",
        "source_type": "other",
        "year": 1989,
    },
    # --- Farsight Institute ---
    {
        "id": 1161,
        "title": "Courtney Brown — 'Cosmic Voyage: A Scientific Discovery of Extraterrestrials Visiting Earth' (Dutton, 1996)",
        "url": "https://en.wikipedia.org/wiki/Courtney_Brown_(researcher)",
        "source_type": "book",
        "author": "Courtney Brown",
        "year": 1996,
    },
    {
        "id": 1162,
        "title": "Farsight Institute — Scientific Research Institute for the Study of Non-Local Consciousness",
        "url": "https://farsight.org/",
        "source_type": "other",
        "year": 2024,
    },
    # --- Sub-programs ---
    {
        "id": 1163,
        "title": "Project Scanate — CIA's initial remote viewing evaluation at SRI (1973, declassified)",
        "url": "https://www.cia.gov/readingroom/collection/stargate",
        "source_type": "government",
        "year": 1973,
    },
    {
        "id": 1164,
        "title": "Project Grill Flame — Army remote viewing program (1978-1983, INSCOM)",
        "url": "https://en.wikipedia.org/wiki/Stargate_Project",
        "source_type": "government",
        "year": 1983,
    },
    {
        "id": 1165,
        "title": "Project Center Lane — successor to Grill Flame under INSCOM (1983-1985)",
        "url": "https://en.wikipedia.org/wiki/Stargate_Project",
        "source_type": "government",
        "year": 1985,
    },
    {
        "id": 1166,
        "title": "Project Sun Streak — DIA remote viewing program (1986-1990)",
        "url": "https://en.wikipedia.org/wiki/Stargate_Project",
        "source_type": "government",
        "year": 1990,
    },
    # --- Ed Dames ---
    {
        "id": 1167,
        "title": "Ed Dames — Army officer, Stargate participant, PSI Tech founder, Art Bell appearances",
        "url": "https://en.wikipedia.org/wiki/Ed_Dames",
        "source_type": "other",
        "year": 2024,
    },
    # --- Stargate coverup ---
    {
        "id": 1168,
        "title": "CIA transferred Stargate capabilities rather than terminating them — Annie Jacobsen, Phenomena (2017)",
        "url": "https://en.wikipedia.org/wiki/Phenomena_(book)",
        "source_type": "journalism",
        "author": "Annie Jacobsen",
        "year": 2017,
    },
    # --- Edgar Mitchell / Apollo 14 ---
    {
        "id": 1169,
        "title": "Edgar Mitchell — Apollo 14 astronaut who conducted unauthorized ESP experiment in space (1971)",
        "url": "https://en.wikipedia.org/wiki/Edgar_Mitchell",
        "source_type": "other",
        "year": 1971,
    },
    # --- Hyman skeptical response ---
    {
        "id": 1170,
        "title": "Ray Hyman — 'Evaluation of Program on Anomalous Mental Phenomena' (skeptical counter-analysis for AIR review, 1995)",
        "url": "https://www.ics.uci.edu/~jutts/hyman.html",
        "source_type": "academic",
        "author": "Ray Hyman",
        "year": 1995,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Researchers ---
    {
        "name": "Dean Radin",
        "entity_type": "person",
        "description": "Parapsychologist and Chief Scientist at IONS. Former researcher at Princeton (PEAR lab), University of Edinburgh, and SRI International. Published meta-analyses of psi research showing statistical significance far beyond chance across hundreds of studies. Author of 'The Conscious Universe' (1997), 'Entangled Minds' (2006), 'Real Magic' (2018). His work represents the most rigorous statistical case for psi phenomena in the literature.",
        "aliases": "",
        "metadata": {"role": "parapsychologist / IONS chief scientist", "years_active": "1985-present"},
    },
    {
        "name": "Jessica Utts",
        "entity_type": "person",
        "description": "Professor of Statistics at UC Irvine. Commissioned by the American Institutes for Research (AIR) to provide statistical evaluation of the Stargate remote viewing data (1995). Her conclusion: the statistical results are far beyond what is expected by chance, and 'psychic functioning has been well established.' Skeptic Ray Hyman agreed the results were anomalous but proposed alternative explanations. Utts served as President of the American Statistical Association (2016).",
        "aliases": "",
        "metadata": {"role": "statistician / UC Irvine / ASA president", "years_active": "1995-present"},
    },
    {
        "name": "Jim Marrs",
        "entity_type": "person",
        "description": "American journalist and author (1943-2017). Wrote 'PSI Spies' (2007) documenting the Stargate program from participants' accounts. Also authored 'Crossfire' (JFK assassination, basis for Oliver Stone's 'JFK') and 'Rule by Secrecy.' One of the few journalists to connect remote viewing programs to the broader intelligence-suppression architecture.",
        "aliases": "",
        "metadata": {"role": "journalist / author", "years_active": "1989-2017"},
    },
    # --- Military Remote Viewers / Trainers ---
    {
        "name": "Paul Smith",
        "entity_type": "person",
        "description": "Captain (ret.), U.S. Army. One of only five military personnel trained in Coordinate Remote Viewing (CRV) directly by Ingo Swann at SRI. Served in the DIA Stargate unit 1983-1990. Author of 'Reading the Enemy's Mind' (2005), the most detailed insider account. Now teaches CRV commercially and serves as president of the International Remote Viewing Association (IRVA).",
        "aliases": "Paul H. Smith",
        "metadata": {"role": "military remote viewer / CRV trainer", "years_active": "1983-present"},
    },
    {
        "name": "Lyn Buchanan",
        "entity_type": "person",
        "description": "Sergeant First Class (ret.), U.S. Army. Military remote viewer in the Stargate unit. Trained in CRV under Ingo Swann. After military service, founded Problems>Solutions>Innovations (P>S>I) to provide commercial remote viewing services and training. Author of 'The Seventh Sense' (2003). Known for database of controlled remote viewing sessions.",
        "aliases": "Leonard Buchanan",
        "metadata": {"role": "military remote viewer / trainer", "years_active": "1984-present"},
    },
    {
        "name": "David Morehouse",
        "entity_type": "person",
        "description": "Major (ret.), U.S. Army. Remote viewer in the Stargate program. Author of 'Psychic Warrior' (1996), one of the first public accounts of the military remote viewing program. His book's publication was controversial within the unit. Later taught remote viewing commercially. His account is more dramatic than other participants' but covers the same operational program.",
        "aliases": "",
        "metadata": {"role": "military remote viewer / author", "years_active": "1988-present"},
    },
    {
        "name": "Angela Dellafiora Ford",
        "entity_type": "person",
        "description": "DIA civilian remote viewer in the Stargate program. Most famous for her 1989 session that accurately located fugitive Charles Jordan — she identified his location as 'Lowell, Wyoming' and he was found 100 miles away in Lovell, Wyoming. This operational success was declassified and became one of the most cited examples of remote viewing producing actionable intelligence.",
        "aliases": "Angela Ford",
        "metadata": {"role": "DIA remote viewer", "years_active": "1986-1995"},
    },
    {
        "name": "Ed Dames",
        "entity_type": "person",
        "description": "Major (ret.), U.S. Army. Served in the Stargate remote viewing unit. Co-founded PSI Tech (1989), one of the first commercial remote viewing companies, while still on active duty. Known for frequent media appearances (Art Bell's Coast to Coast AM) making dramatic predictions. Controversial within the RV community for sensationalism that other participants say discredited the field.",
        "aliases": "Edward Dames",
        "metadata": {"role": "military remote viewer / PSI Tech founder", "years_active": "1983-present"},
    },
    # --- Andrija Puharich ---
    {
        "name": "Andrija Puharich",
        "entity_type": "person",
        "description": "Medical doctor and parapsychologist (1918-1995). Conducted psi research for the U.S. Army at Camp Detrick in the 1950s through his Round Table Foundation. Brought Uri Geller from Israel to SRI for testing in the 1970s. Connected to both Army intelligence psi programs and MKULTRA-adjacent research. His work bridged military psi research, psychedelic experimentation, and UFO phenomena decades before these threads converged publicly.",
        "aliases": "Henry Karel Puharich",
        "metadata": {"role": "Army psi researcher / parapsychologist", "years_active": "1947-1995"},
    },
    # --- Jacques Vallée ---
    {
        "name": "Jacques Vallée",
        "entity_type": "person",
        "description": "French-American astronomer, computer scientist, and venture capitalist. Co-developed ARPANET protocols at Stanford. Conducted UFO research at Northwestern under J. Allen Hynek, then independently for decades. Proposed the 'interdimensional hypothesis' — that UFO phenomena are not extraterrestrial but involve consciousness manipulation across dimensions. Worked with Hal Puthoff at SRI. His 'Forbidden Science' journals document the intersection of psi research, UFO investigations, and intelligence community involvement from the inside. Served as AAWSAP consultant.",
        "aliases": "",
        "metadata": {"role": "astronomer / computer scientist / UFO researcher", "years_active": "1962-present"},
    },
    {
        "name": "Edgar Mitchell",
        "entity_type": "person",
        "description": "Apollo 14 astronaut and sixth person to walk on the Moon (1971). During the return flight, conducted unauthorized ESP experiments with collaborators on Earth. The experience of seeing Earth from space triggered a profound consciousness shift he called 'savikalpa samadhi.' Founded the Institute of Noetic Sciences (IONS) in 1973 to study consciousness scientifically. Became an outspoken advocate for UFO disclosure and psi research until his death in 2016.",
        "aliases": "",
        "metadata": {"role": "astronaut / IONS founder", "years_active": "1971-2016"},
    },
    # --- Organizations ---
    {
        "name": "IONS",
        "entity_type": "organization",
        "description": "Institute of Noetic Sciences. Founded by Apollo 14 astronaut Edgar Mitchell in 1973 in Petaluma, California. Conducts peer-reviewed research on consciousness, psi phenomena, and mind-matter interaction. Dean Radin served as Chief Scientist. Has published in mainstream journals. Represents the most institutionally respectable continuation of psi research after government programs were 'terminated.'",
        "aliases": "Institute of Noetic Sciences",
        "metadata": {"type": "research institute", "founded": 1973},
    },
    {
        "name": "SAIC",
        "entity_type": "organization",
        "description": "Science Applications International Corporation. Major defense contractor headquartered in San Diego. Took over the Stargate remote viewing research program from SRI International in 1991 when Edwin May moved the project. Operated the program under DIA contract until 'termination' in 1995. The transfer from an academic institution (SRI) to a classified defense contractor reduced transparency and public accountability.",
        "aliases": "Science Applications International Corporation",
        "metadata": {"type": "defense contractor", "founded": 1969},
    },
    {
        "name": "PSI Tech",
        "entity_type": "organization",
        "description": "Technical Remote Viewing company founded in 1989 by Ed Dames and other Stargate personnel while some were still on active duty. One of the first commercial ventures to offer remote viewing services and training to the public. Represents the privatization pipeline: classified military capabilities transferred to commercial entities staffed by the same people.",
        "aliases": "Psi Tech, Technical Remote Viewing Inc.",
        "metadata": {"type": "commercial RV company", "founded": 1989},
    },
    {
        "name": "Farsight Institute",
        "entity_type": "organization",
        "description": "Founded by Courtney Brown (Emory University political scientist) in 1995. Conducts remote viewing research and publishes results. Brown was trained in CRV by Ed Dames / PSI Tech. The institute's work is more speculative than military-era research — claiming remote viewing of Mars, historical events, and extraterrestrial targets. Controversial even within the remote viewing community for claims that extend beyond verifiable targets.",
        "aliases": "",
        "metadata": {"type": "remote viewing research", "founded": 1995},
    },
    # --- Sub-programs ---
    {
        "name": "Project Scanate",
        "entity_type": "program",
        "description": "CIA's initial evaluation of remote viewing at SRI International (1973). The name combined 'scan' and 'gate' (later reversed to 'Stargate'). Ingo Swann and Pat Price were the primary subjects. Price's accurate description of a Soviet military installation at Semipalatinsk from coordinates alone convinced the CIA to expand funding. Declassified documents confirm the program and its results.",
        "aliases": "SCANATE",
        "metadata": {"type": "intelligence program", "years_active": "1973-1976"},
    },
    {
        "name": "Project Grill Flame",
        "entity_type": "program",
        "description": "U.S. Army INSCOM remote viewing program (1978-1983). Successor to initial CIA work at SRI. Operated at Fort Meade, Maryland under INSCOM. First operational military remote viewing unit. Joseph McMoneagle was Remote Viewer #001. Renamed Center Lane in 1983 when Albert Stubblebine took command of INSCOM.",
        "aliases": "Grill Flame, GONDOLA WISH",
        "metadata": {"type": "intelligence program", "years_active": "1978-1983"},
    },
    {
        "name": "Project Center Lane",
        "entity_type": "program",
        "description": "Successor to Grill Flame under INSCOM (1983-1985). Operated under Albert Stubblebine's command. Focused on training additional remote viewers in the CRV methodology developed by Ingo Swann. Paul Smith, Lyn Buchanan, and others trained during this period. Renamed Sun Streak when transferred to DIA in 1986.",
        "aliases": "Center Lane",
        "metadata": {"type": "intelligence program", "years_active": "1983-1985"},
    },
    {
        "name": "Project Sun Streak",
        "entity_type": "program",
        "description": "DIA remote viewing program (1986-1990). Successor to Center Lane after the program was transferred from Army INSCOM to DIA management. Dale Graff served as project manager. Renamed Stargate in 1991. The program was operational — producing intelligence products used by military and intelligence consumers.",
        "aliases": "Sun Streak",
        "metadata": {"type": "intelligence program", "years_active": "1986-1990"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Dean Radin / IONS ---
    {
        "source": "Dean Radin",
        "target": "IONS",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Chief Scientist at IONS. Conducted peer-reviewed psi research including meta-analyses of remote viewing, presentiment, and mind-matter interaction experiments.",
        "sources": [1141, 1142, 1144],
        "year_start": 2001,
        "year_end": None,
    },
    {
        "source": "Dean Radin",
        "target": "SRI International",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Worked at SRI International before joining IONS. Connected to the same psi research lineage as Puthoff and Targ.",
        "sources": [1141],
        "year_start": 1985,
        "year_end": 1993,
    },
    {
        "source": "Dean Radin",
        "target": "Project Stargate",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Radin's meta-analyses incorporate Stargate data. His statistical work independently confirmed the anomalous results Utts found in the AIR review.",
        "sources": [1141, 1146],
        "year_start": 1997,
        "year_end": None,
    },
    # --- Jessica Utts ---
    {
        "source": "Jessica Utts",
        "target": "Project Stargate",
        "type": "investigated",
        "tier": "documented",
        "desc": "Commissioned by AIR to statistically evaluate Stargate data (1995). Concluded: 'psychic functioning has been well established.' Her analysis used standard statistical methods accepted by the American Statistical Association.",
        "sources": [1146, 1147],
        "year_start": 1995,
        "year_end": 1995,
    },
    {
        "source": "Jessica Utts",
        "target": "Stargate Declassification",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Utts' positive statistical assessment was part of the AIR review that preceded the 1995 declassification. Despite her findings confirming significance, the CIA terminated the program.",
        "sources": [1146, 1147],
        "year_start": 1995,
        "year_end": 1995,
    },
    # --- Jim Marrs ---
    {
        "source": "Jim Marrs",
        "target": "Project Stargate",
        "type": "investigated",
        "tier": "credible",
        "desc": "Authored 'PSI Spies' (2007) documenting the Stargate program from extensive interviews with program participants. One of the most comprehensive journalistic accounts.",
        "sources": [1152],
        "year_start": 2007,
        "year_end": 2007,
    },
    # --- Military Remote Viewers ---
    {
        "source": "Paul Smith",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Served in the DIA remote viewing unit 1983-1990. One of five trained in CRV directly by Ingo Swann at SRI. Author of the most detailed insider account.",
        "sources": [1148],
        "year_start": 1983,
        "year_end": 1990,
    },
    {
        "source": "Paul Smith",
        "target": "Ingo Swann",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Trained in Coordinate Remote Viewing (CRV) directly by Ingo Swann at SRI International. One of only five military personnel to receive this training.",
        "sources": [1148],
        "year_start": 1983,
        "year_end": 1984,
    },
    {
        "source": "Paul Smith",
        "target": "Project Center Lane",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Trained and served during the Center Lane period (1983-1985) when CRV training was expanded under INSCOM.",
        "sources": [1148, 1165],
        "year_start": 1983,
        "year_end": 1985,
    },
    {
        "source": "Lyn Buchanan",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Military remote viewer in the Stargate unit. Trained in CRV. Founded P>S>I after military service to continue commercial remote viewing.",
        "sources": [1149],
        "year_start": 1984,
        "year_end": 1992,
    },
    {
        "source": "David Morehouse",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Remote viewer in the Stargate program. His 1996 book 'Psychic Warrior' was one of the first public accounts, published shortly after declassification.",
        "sources": [1150],
        "year_start": 1988,
        "year_end": 1994,
    },
    {
        "source": "Angela Dellafiora Ford",
        "target": "DIA",
        "type": "worked_for",
        "tier": "documented",
        "desc": "DIA civilian remote viewer in the Stargate unit. Her 1989 session locating fugitive Charles Jordan ('Lowell, WY' → found in Lovell, WY) became one of the most cited operational RV successes.",
        "sources": [1151],
        "year_start": 1986,
        "year_end": 1995,
    },
    {
        "source": "Angela Dellafiora Ford",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Participated in operational remote viewing sessions for intelligence consumers. Charles Jordan case declassified as proof of operational utility.",
        "sources": [1151],
        "year_start": 1986,
        "year_end": 1995,
    },
    # --- Ed Dames / PSI Tech ---
    {
        "source": "Ed Dames",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Army officer in the Stargate remote viewing unit. Later became the most publicly visible (and controversial) program alumnus through media appearances.",
        "sources": [1167, 1148],
        "year_start": 1983,
        "year_end": 1989,
    },
    {
        "source": "Ed Dames",
        "target": "PSI Tech",
        "type": "founded",
        "tier": "documented",
        "desc": "Co-founded PSI Tech in 1989 while still on active duty. Commercialized Technical Remote Viewing methodology from the classified program.",
        "sources": [1160, 1167],
        "year_start": 1989,
        "year_end": None,
    },
    {
        "source": "PSI Tech",
        "target": "Project Stargate",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Founded by Stargate personnel using classified CRV methodology. Represents the privatization of military psi capabilities.",
        "sources": [1160],
        "year_start": 1989,
        "year_end": None,
    },
    # --- Farsight ---
    {
        "source": "Farsight Institute",
        "target": "PSI Tech",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Courtney Brown trained in CRV through PSI Tech / Ed Dames before founding Farsight. Second-generation privatization of military RV capabilities.",
        "sources": [1161, 1162],
        "year_start": 1995,
        "year_end": None,
    },
    # --- SAIC ---
    {
        "source": "SAIC",
        "target": "SRI International",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Took over the Stargate research program from SRI in 1991 when Edwin May transferred. Same research, different (more classified) institutional home.",
        "sources": [1159],
        "year_start": 1991,
        "year_end": 1995,
    },
    {
        "source": "Edwin May",
        "target": "SAIC",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Moved the Stargate research program from SRI to SAIC in 1991. Directed the program at SAIC until termination in 1995.",
        "sources": [1159],
        "year_start": 1991,
        "year_end": 1995,
    },
    {
        "source": "SAIC",
        "target": "Project Stargate",
        "type": "operated",
        "tier": "documented",
        "desc": "Operated the Stargate research component under DIA contract (1991-1995). Defense contractor housing classified psi research.",
        "sources": [1159],
        "year_start": 1991,
        "year_end": 1995,
    },
    # --- Andrija Puharich ---
    {
        "source": "Andrija Puharich",
        "target": "CIA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Conducted psi research at Camp Detrick through his Round Table Foundation in the 1950s. Connected to MKULTRA-adjacent Army psi programs. Brought Uri Geller to SRI for testing.",
        "sources": [1153, 1154, 1155],
        "year_start": 1952,
        "year_end": 1975,
    },
    {
        "source": "Andrija Puharich",
        "target": "SRI International",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Brought Uri Geller from Israel to SRI for psi testing in the early 1970s. His introduction connected Israeli psi subjects to the American military-research complex.",
        "sources": [1154],
        "year_start": 1972,
        "year_end": 1975,
    },
    # --- Jacques Vallée ---
    {
        "source": "Jacques Vallée",
        "target": "SRI International",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Worked with Hal Puthoff at SRI on psi research. His 'Forbidden Science' journals document the intersection of RV research and UFO investigations from inside SRI.",
        "sources": [1156, 1158],
        "year_start": 1972,
        "year_end": 1985,
    },
    {
        "source": "Jacques Vallée",
        "target": "Hal Puthoff",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Collaborated at SRI. Vallée's UFO research and Puthoff's psi research overlapped — both dealt with anomalous consciousness phenomena. Documented in Forbidden Science journals.",
        "sources": [1158],
        "year_start": 1972,
        "year_end": None,
    },
    # --- Edgar Mitchell / IONS ---
    {
        "source": "Edgar Mitchell",
        "target": "IONS",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded IONS in 1973 after his consciousness experience during Apollo 14 return flight. Created an institutional home for scientific consciousness research.",
        "sources": [1145, 1169],
        "year_start": 1973,
        "year_end": 2016,
    },
    # --- Sub-programs chain ---
    {
        "source": "Project Scanate",
        "target": "Project Stargate",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Initial CIA remote viewing evaluation (1973) that proved the concept. Success of Scanate led to expanded funding and eventually the full Stargate program.",
        "sources": [1163],
        "year_start": 1973,
        "year_end": 1976,
    },
    {
        "source": "CIA",
        "target": "Project Scanate",
        "type": "operated",
        "tier": "documented",
        "desc": "CIA initiated and funded Project Scanate at SRI in 1973. First formal government remote viewing evaluation program.",
        "sources": [1163],
        "year_start": 1973,
        "year_end": 1976,
    },
    {
        "source": "Project Grill Flame",
        "target": "Project Stargate",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Army INSCOM remote viewing program (1978-1983). First operational military RV unit. Predecessor in the Scanate→Grill Flame→Center Lane→Sun Streak→Stargate chain.",
        "sources": [1164],
        "year_start": 1978,
        "year_end": 1983,
    },
    {
        "source": "Project Center Lane",
        "target": "Project Grill Flame",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Direct successor to Grill Flame under INSCOM (1983). Same unit, new name, expanded CRV training under Stubblebine's command.",
        "sources": [1165],
        "year_start": 1983,
        "year_end": 1985,
    },
    {
        "source": "Project Sun Streak",
        "target": "Project Center Lane",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Successor to Center Lane after transfer from INSCOM to DIA management (1986). Same program, same personnel, new oversight.",
        "sources": [1166],
        "year_start": 1986,
        "year_end": 1990,
    },
    {
        "source": "DIA",
        "target": "Project Sun Streak",
        "type": "operated",
        "tier": "documented",
        "desc": "DIA took over management from INSCOM in 1986. Dale Graff served as DIA program manager for Sun Streak.",
        "sources": [1166],
        "year_start": 1986,
        "year_end": 1990,
    },
    {
        "source": "DIA",
        "target": "Project Grill Flame",
        "type": "connected_to",
        "tier": "documented",
        "desc": "DIA provided intelligence tasking to Grill Flame before formally taking over management. Consumers of RV intelligence products.",
        "sources": [1164],
        "year_start": 1978,
        "year_end": 1983,
    },
    # --- Coverup relationship ---
    {
        "source": "CIA",
        "target": "Stargate Declassification",
        "type": "suppressed_by",
        "tier": "credible",
        "desc": "Multiple Stargate participants and researchers (Jacobsen, Smith, Marrs) document that CIA did not terminate psi capabilities in 1995 — it transferred them to private sector. The 'termination' was a cover story.",
        "sources": [1168, 1148, 1152],
        "year_start": 1995,
        "year_end": None,
    },
    # --- Ingo Swann CRV training chain ---
    {
        "source": "Ingo Swann",
        "target": "Project Center Lane",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Developed and taught Coordinate Remote Viewing (CRV) to military personnel during the Center Lane period. Smith, Buchanan, and others trained directly under Swann.",
        "sources": [1148],
        "year_start": 1983,
        "year_end": 1985,
    },
    # --- Joseph McMoneagle / Grill Flame ---
    {
        "source": "Joseph McMoneagle",
        "target": "Project Grill Flame",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Remote Viewer #001. First recruited into the program during the Grill Flame period at Fort Meade. Served from inception through termination.",
        "sources": [1164],
        "year_start": 1978,
        "year_end": 1983,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Dean Radin": [1141, 1142, 1143, 1144],
    "Jessica Utts": [1146, 1147],
    "Jim Marrs": [1152],
    "Paul Smith": [1148],
    "Lyn Buchanan": [1149],
    "David Morehouse": [1150],
    "Angela Dellafiora Ford": [1151],
    "Ed Dames": [1160, 1167],
    "Andrija Puharich": [1153, 1154, 1155],
    "Jacques Vallée": [1156, 1157, 1158],
    "Edgar Mitchell": [1145, 1169],
    "IONS": [1144, 1145],
    "SAIC": [1159],
    "PSI Tech": [1160, 1167],
    "Farsight Institute": [1161, 1162],
    "Project Scanate": [1163],
    "Project Grill Flame": [1164],
    "Project Center Lane": [1165],
    "Project Sun Streak": [1166],
}
