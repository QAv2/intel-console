"""
UAP Programs / Crash Retrieval — Expansion layer for Intel Console.

Maps the UAP reverse-engineering infrastructure: the programs, facilities,
contractors, and people involved in crash retrieval, materials analysis,
and technology exploitation. This extends the existing UAP disclosure expansion
(which covers the legislative/whistleblower side) with the operational programs.

Entities (~20): Key figures (Robert Bigelow, Eric Davis, Colm Kelleher,
Jacques Vallée, Kit Green, James Lacatski, Lue Elizondo [already exists],
David Grusch [already exists]), organizations (NIDS, Bigelow Aerospace,
Battelle Memorial Institute, Lockheed Skunk Works, SAIC), programs
(AAWSAP, BAASS, Project Blue Book [already exists]), facilities (Skinwalker Ranch,
S-4/Area 51, Wright-Patterson AFB), events/docs (Wilson-Davis Memo, Roswell).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], DIA [from consciousness expansion], DARPA [90],
  Luis Elizondo [292], David Grusch [293], David Fravor [294],
  Ryan Graves [295], AATIP [303], Project Blue Book [304],
  UAP Task Force [305], Hal Puthoff [from consciousness expansion],
  Daniel Sheehan [289], New Paradigm Institute [299],
  Lockheed Martin [from MIC expansion], Northrop Grumman [from MIC expansion]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 781-810
# ============================================================

SOURCES = [
    # --- AAWSAP / BAASS ---
    {
        "id": 781,
        "title": "James Lacatski, Colm Kelleher, George Knapp — Skinwalkers at the Pentagon: An Insiders' Account of the Secret Government UFO Program",
        "url": "https://en.wikipedia.org/wiki/Skinwalkers_at_the_Pentagon",
        "source_type": "journalism",
        "author": "James Lacatski, Colm Kelleher, George Knapp",
        "year": 2021,
    },
    {
        "id": 782,
        "title": "DIA — Advanced Aerospace Weapon System Applications Program (AAWSAP) contract with Bigelow Aerospace (FOIA)",
        "url": "https://www.theblackvault.com/documentarchive/the-advanced-aerospace-weapon-system-applications-program-aawsap-documentation/",
        "source_type": "government",
        "year": 2008,
    },
    {
        "id": 783,
        "title": "38 DIRDs (Defense Intelligence Reference Documents) — commissioned by AAWSAP/DIA, covering advanced propulsion, metamaterials, warp drive, etc.",
        "url": "https://www.theblackvault.com/documentarchive/the-dia-dird-documents/",
        "source_type": "government",
        "year": 2009,
    },
    # --- Wilson-Davis Memo ---
    {
        "id": 784,
        "title": "Admiral Thomas Wilson / Dr. Eric Davis — Notes from Oct 16, 2002 meeting (Wilson-Davis Memo, leaked 2019)",
        "url": "https://www.theblackvault.com/documentarchive/the-wilson-davis-notes/",
        "source_type": "other",
        "year": 2002,
    },
    # --- Jacques Vallée ---
    {
        "id": 785,
        "title": "Jacques Vallée — Trinity: The Best-Kept Secret (San Antonio, NM crash, 1945)",
        "url": "https://en.wikipedia.org/wiki/Jacques_Vall%C3%A9e",
        "source_type": "journalism",
        "author": "Jacques Vallée, Paola Harris",
        "year": 2021,
    },
    {
        "id": 786,
        "title": "Jacques Vallée & Paola Harris — Trinity testimony and materials analysis",
        "url": "https://en.wikipedia.org/wiki/Jacques_Vall%C3%A9e",
        "source_type": "journalism",
        "author": "Jacques Vallée",
        "year": 2021,
    },
    # --- Skinwalker Ranch ---
    {
        "id": 787,
        "title": "Colm Kelleher & George Knapp — Hunt for the Skinwalker: Science Confronts the Unexplained at a Remote Ranch in Utah",
        "url": "https://en.wikipedia.org/wiki/Hunt_for_the_Skinwalker",
        "source_type": "journalism",
        "author": "Colm Kelleher, George Knapp",
        "year": 2005,
    },
    # --- Robert Bigelow ---
    {
        "id": 788,
        "title": "Robert Bigelow — 60 Minutes interview: 'I'm absolutely convinced' aliens exist and have visited Earth (2017)",
        "url": "https://en.wikipedia.org/wiki/Robert_Bigelow",
        "source_type": "journalism",
        "year": 2017,
    },
    # --- Battelle ---
    {
        "id": 789,
        "title": "Battelle Memorial Institute — Project Blue Book Special Report No. 14 (1955, statistical analysis of UFO sightings)",
        "url": "https://en.wikipedia.org/wiki/Project_Blue_Book#Special_Report_No._14",
        "source_type": "government",
        "year": 1955,
    },
    {
        "id": 790,
        "title": "Anthony Bragalia — FOIA response from DIA on metamaterial analysis (2021, references Bigelow Aerospace contract)",
        "url": "https://www.theblackvault.com/documentarchive/ufo-meta-material-analysis-documents/",
        "source_type": "government",
        "year": 2021,
    },
    # --- Roswell ---
    {
        "id": 791,
        "title": "GAO Report — Results of a Search for Records Concerning the 1947 Crash Near Roswell, New Mexico",
        "url": "https://www.gao.gov/products/nsiad-95-187",
        "source_type": "government",
        "year": 1995,
    },
    {
        "id": 792,
        "title": "Jesse Marcel Jr. — The Roswell Legacy: The Untold Story of the First Military Officer at the 1947 Crash Site",
        "url": "https://en.wikipedia.org/wiki/Jesse_Marcel",
        "source_type": "journalism",
        "author": "Jesse Marcel Jr.",
        "year": 2007,
    },
    {
        "id": 793,
        "title": "USAF Roswell Report — Case Closed (1997) — Project Mogul explanation",
        "url": "https://en.wikipedia.org/wiki/Roswell_incident",
        "source_type": "government",
        "year": 1997,
    },
    # --- Eric Davis ---
    {
        "id": 794,
        "title": "Eric Davis — DIRD author, Earthtech International physicist, co-author of analysis on exotic propulsion",
        "url": "https://en.wikipedia.org/wiki/Eric_W._Davis",
        "source_type": "academic",
        "year": 2009,
    },
    # --- Kit Green ---
    {
        "id": 795,
        "title": "Kit Green — former CIA Office of Scientific Intelligence, Weird Desk, connection to UAP programs",
        "url": "https://en.wikipedia.org/wiki/Kit_Green",
        "source_type": "other",
        "year": 2019,
    },
    # --- Grusch testimony details ---
    {
        "id": 796,
        "title": "David Grusch — ICIG complaint and congressional testimony on non-human intelligence crash retrieval programs (2023)",
        "url": "https://www.congress.gov/event/118th-congress/house-event/116282",
        "source_type": "congressional",
        "year": 2023,
    },
    # --- Lockheed / Skunk Works ---
    {
        "id": 797,
        "title": "Ben Rich — Skunk Works: A Personal Memoir of My Years at Lockheed (attributed statements on ET technology)",
        "url": "https://en.wikipedia.org/wiki/Ben_Rich",
        "source_type": "other",
        "author": "Ben Rich",
        "year": 1994,
    },
    # --- Area 51 ---
    {
        "id": 798,
        "title": "Annie Jacobsen — Area 51: An Uncensored History of America's Top-Secret Military Base",
        "url": "https://en.wikipedia.org/wiki/Area_51:_An_Uncensored_History_of_America%27s_Top-Secret_Military_Base",
        "source_type": "journalism",
        "author": "Annie Jacobsen",
        "year": 2011,
    },
    {
        "id": 799,
        "title": "CIA acknowledges Area 51 existence — declassified U-2 history (2013)",
        "url": "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB434/",
        "source_type": "government",
        "year": 2013,
    },
    # --- George Knapp ---
    {
        "id": 800,
        "title": "George Knapp — investigative journalist, KLAS-TV. First to interview Bob Lazar. Co-author Skinwalker books.",
        "url": "https://en.wikipedia.org/wiki/George_Knapp_(journalist)",
        "source_type": "journalism",
        "year": 1989,
    },
    # --- NIDS ---
    {
        "id": 801,
        "title": "NIDS (National Institute for Discovery Science) — Bigelow's private UFO/paranormal research org (1995-2004)",
        "url": "https://en.wikipedia.org/wiki/National_Institute_for_Discovery_Science",
        "source_type": "other",
        "year": 1995,
    },
    # --- Wright-Patterson ---
    {
        "id": 802,
        "title": "Wright-Patterson AFB — Foreign Technology Division / Air Force Materiel Command, historical connection to UAP materials",
        "url": "https://en.wikipedia.org/wiki/Wright-Patterson_Air_Force_Base",
        "source_type": "other",
        "year": 1947,
    },
    # --- Sol Foundation ---
    {
        "id": 803,
        "title": "Sol Foundation — Stanford-affiliated think tank on UAP implications, founded by Peter Skafish and Garry Nolan",
        "url": "https://thesolfoundation.org/",
        "source_type": "academic",
        "year": 2023,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Key Figures ---
    {
        "name": "Robert Bigelow",
        "entity_type": "person",
        "description": "Billionaire founder of Bigelow Aerospace and Budget Suites. Founded NIDS (1995) to study UAP/paranormal. Purchased Skinwalker Ranch. Won $22M DIA AAWSAP contract (2008) through Bigelow Aerospace Advanced Space Studies (BAASS). On 60 Minutes: 'I'm absolutely convinced' aliens have visited Earth.",
        "aliases": "",
        "metadata": {"role": "entrepreneur / UAP researcher", "years_active": "1995-present"},
    },
    {
        "name": "Eric Davis",
        "entity_type": "person",
        "description": "Astrophysicist at EarthTech International (Hal Puthoff's firm). Author of multiple DIRDs for AAWSAP. Authored the notes from the 2002 meeting with Admiral Wilson describing a UAP reverse-engineering program (Wilson-Davis Memo). Briefed congressional committees.",
        "aliases": "Eric W. Davis",
        "metadata": {"role": "physicist / DIRD author", "years_active": "2000-present"},
    },
    {
        "name": "Colm Kelleher",
        "entity_type": "person",
        "description": "Biochemist. Deputy Administrator of NIDS, then BAASS program manager for AAWSAP. Co-authored 'Hunt for the Skinwalker' and 'Skinwalkers at the Pentagon.' Managed the 38 DIRD studies and field investigations for the DIA program.",
        "aliases": "",
        "metadata": {"role": "NIDS/BAASS scientist", "years_active": "1996-2012"},
    },
    {
        "name": "Jacques Vallée",
        "entity_type": "person",
        "description": "Computer scientist, astrophysicist, and UFO researcher. Worked with J. Allen Hynek on Project Blue Book data. Proposed the interdimensional hypothesis. Investigated crash retrieval materials. Co-authored 'Trinity' on 1945 San Antonio crash. Consulted for AAWSAP.",
        "aliases": "",
        "metadata": {"role": "scientist / UFO researcher", "years_active": "1961-present"},
    },
    {
        "name": "Kit Green",
        "entity_type": "person",
        "description": "Former CIA Officer of Scientific Intelligence ('Weird Desk'). Neurologist. Examined people claiming anomalous experiences/injuries from UAP encounters. Connected to AAWSAP/BAASS through medical analysis of UAP witness injuries. Bridge between CIA and UAP research community.",
        "aliases": "Christopher Kit Green",
        "metadata": {"role": "CIA scientist / neurologist", "years_active": "1969-present"},
    },
    {
        "name": "James Lacatski",
        "entity_type": "person",
        "description": "DIA rocket scientist who conceived and managed the AAWSAP program. Visited Skinwalker Ranch, experienced anomalous phenomena personally. His encounter at the ranch directly motivated the creation of AAWSAP. Co-author of 'Skinwalkers at the Pentagon.'",
        "aliases": "",
        "metadata": {"role": "DIA program manager", "years_active": "2008-2012"},
    },
    {
        "name": "George Knapp",
        "entity_type": "person",
        "description": "Investigative journalist, KLAS-TV Las Vegas. First to report Bob Lazar's S-4 claims (1989). George Polk Award winner. Co-authored Skinwalker books with Kelleher. Key journalist connecting public to UAP program revelations.",
        "aliases": "",
        "metadata": {"role": "investigative journalist", "years_active": "1989-present"},
    },
    # --- Organizations ---
    {
        "name": "NIDS",
        "entity_type": "organization",
        "description": "National Institute for Discovery Science. Founded by Robert Bigelow (1995). Studied UAP, cattle mutilations, Skinwalker Ranch phenomena. Board included Kit Green, Hal Puthoff, Edgar Mitchell, John Alexander. Disbanded 2004. Personnel and data transitioned to BAASS for AAWSAP.",
        "aliases": "National Institute for Discovery Science",
        "metadata": {"type": "research organization", "years_active": "1995-2004"},
    },
    {
        "name": "Bigelow Aerospace",
        "entity_type": "organization",
        "description": "Robert Bigelow's aerospace company. Won $22M AAWSAP contract from DIA (2008) through BAASS subsidiary. Developed inflatable space habitats (BEAM module on ISS). Stored UAP metamaterials under government contract. Bridge between private aerospace and UAP investigation.",
        "aliases": "BAASS, Bigelow Aerospace Advanced Space Studies",
        "metadata": {"type": "aerospace/research", "years_active": "1999-present"},
    },
    {
        "name": "Battelle Memorial Institute",
        "entity_type": "organization",
        "description": "World's largest independent R&D organization. Conducted statistical analysis for Project Blue Book (Special Report No. 14, 1955) — found significant percentage of cases 'unknown.' Historical connection to materials analysis of anomalous debris. Operates several DOE national laboratories.",
        "aliases": "Battelle",
        "metadata": {"type": "research institute", "founded": 1929},
    },
    {
        "name": "Sol Foundation",
        "entity_type": "organization",
        "description": "Stanford University-affiliated think tank on UAP implications, founded 2023. Hosted inaugural symposium at Stanford with Grusch, Nolan, Loeb, Vallée. Focuses on policy, scientific, and philosophical implications of non-human intelligence.",
        "aliases": "",
        "metadata": {"type": "think tank", "founded": 2023},
    },
    # --- Programs ---
    {
        "name": "AAWSAP",
        "entity_type": "program",
        "description": "Advanced Aerospace Weapon System Applications Program. DIA program (2008-2012) managed by James Lacatski, contracted to Bigelow's BAASS. Broader than AATIP — investigated UAP, Skinwalker Ranch phenomena, produced 38 DIRDs on exotic technologies. $22M budget from Sen. Harry Reid's initiative.",
        "aliases": "Advanced Aerospace Weapon System Applications Program",
        "metadata": {"type": "intelligence program", "years_active": "2008-2012"},
    },
    # --- Facilities ---
    {
        "name": "Skinwalker Ranch",
        "entity_type": "facility",
        "description": "512-acre ranch in Uintah Basin, Utah. Site of documented anomalous phenomena including UAP, poltergeist activity, cattle mutilation, and interdimensional entities. Owned by Terry Sherman, then Robert Bigelow (1996-2016), now Brandon Fugal. Studied by NIDS, then BAASS/AAWSAP.",
        "aliases": "Sherman Ranch",
        "metadata": {"location": "Uintah County, Utah"},
    },
    {
        "name": "Area 51",
        "entity_type": "facility",
        "description": "Classified USAF facility within Nevada Test and Training Range. CIA acknowledged its existence in 2013 (U-2 development history). Bob Lazar claimed S-4 facility nearby housed recovered craft (1989). Central to UAP lore. Grusch testimony references legacy programs at contractor facilities.",
        "aliases": "Groom Lake, S-4, Dreamland, Paradise Ranch",
        "metadata": {"location": "Lincoln County, Nevada"},
    },
    {
        "name": "Wright-Patterson AFB",
        "entity_type": "facility",
        "description": "Home of Air Force Materiel Command and Foreign Technology Division. Hosted Project Blue Book. Historical reports place recovered UAP materials at the base (Hangar 18 legend). Sen. Barry Goldwater confirmed he was denied access to a classified area related to UFO materials.",
        "aliases": "Wright-Pat, Hangar 18",
        "metadata": {"location": "Dayton, Ohio"},
    },
    # --- Events ---
    {
        "name": "Wilson-Davis Memo",
        "entity_type": "event",
        "description": "Notes by Dr. Eric Davis from Oct 16, 2002 meeting with Admiral Thomas Wilson (former DIA Director/J-2). Wilson described being denied access to a UAP reverse-engineering Special Access Program run by a defense contractor. Leaked 2019. Davis confirmed the notes are authentic.",
        "aliases": "Wilson-Davis Notes, Wilson Leak",
        "metadata": {"date": "2002-10-16"},
    },
    {
        "name": "Roswell Incident",
        "entity_type": "event",
        "description": "July 1947 crash near Roswell, New Mexico. Army initially announced recovery of 'flying disc,' then retracted to 'weather balloon.' USAF later claimed Project Mogul (1994) and crash test dummies (1997). GAO found key records from Roswell Army Air Field were destroyed without explanation. First responder testimony contradicts official explanation.",
        "aliases": "Roswell Crash, Roswell UFO Incident",
        "metadata": {"date": "1947-07-08", "location": "Roswell, New Mexico"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- AAWSAP / BAASS ---
    {
        "source": "DIA",
        "target": "AAWSAP",
        "type": "operated",
        "tier": "documented",
        "desc": "DIA managed AAWSAP program (2008-2012). $22M budget secured through Sen. Harry Reid. Contracted to Bigelow's BAASS.",
        "sources": [781, 782],
        "year_start": 2008,
        "year_end": 2012,
    },
    {
        "source": "James Lacatski",
        "target": "AAWSAP",
        "type": "directed",
        "tier": "documented",
        "desc": "DIA rocket scientist who conceived and managed AAWSAP. His personal experience at Skinwalker Ranch motivated the program.",
        "sources": [781, 782],
        "year_start": 2008,
        "year_end": 2012,
    },
    {
        "source": "Bigelow Aerospace",
        "target": "AAWSAP",
        "type": "contracted_by",
        "tier": "documented",
        "desc": "Won $22M DIA contract for AAWSAP through BAASS subsidiary. Produced 38 DIRDs and conducted field investigations.",
        "sources": [781, 782, 783],
        "year_start": 2008,
        "year_end": 2012,
    },
    {
        "source": "Robert Bigelow",
        "target": "Bigelow Aerospace",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded Bigelow Aerospace. Created BAASS subsidiary specifically for AAWSAP contract.",
        "sources": [788],
        "year_start": 1999,
        "year_end": None,
    },
    {
        "source": "Colm Kelleher",
        "target": "AAWSAP",
        "type": "participated_in",
        "tier": "documented",
        "desc": "BAASS program manager for AAWSAP. Managed the 38 DIRD studies and field investigations.",
        "sources": [781],
        "year_start": 2008,
        "year_end": 2012,
    },
    {
        "source": "Eric Davis",
        "target": "AAWSAP",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Authored multiple DIRDs for AAWSAP on exotic propulsion and spacetime metrics. Key scientific contributor.",
        "sources": [783, 794],
        "year_start": 2008,
        "year_end": 2012,
    },
    {
        "source": "Hal Puthoff",
        "target": "AAWSAP",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Contributed to AAWSAP as scientific advisor. Authored DIRDs. Bridge from Stargate consciousness research to UAP investigation.",
        "sources": [783],
        "year_start": 2008,
        "year_end": 2012,
    },
    {
        "source": "Luis Elizondo",
        "target": "AAWSAP",
        "type": "connected_to",
        "tier": "credible",
        "desc": "AATIP (subset/successor of AAWSAP) directed by Elizondo at Pentagon. Relationship between AATIP and AAWSAP has been subject of debate.",
        "sources": [781],
        "year_start": 2010,
        "year_end": 2017,
    },
    # --- NIDS ---
    {
        "source": "Robert Bigelow",
        "target": "NIDS",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded NIDS in 1995 to study UAP and paranormal phenomena. Board included Puthoff, Kit Green, Edgar Mitchell.",
        "sources": [787, 801],
        "year_start": 1995,
        "year_end": 2004,
    },
    {
        "source": "Colm Kelleher",
        "target": "NIDS",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Deputy Administrator of NIDS. Led field investigations at Skinwalker Ranch.",
        "sources": [787, 801],
        "year_start": 1996,
        "year_end": 2004,
    },
    {
        "source": "Kit Green",
        "target": "NIDS",
        "type": "member_of",
        "tier": "documented",
        "desc": "NIDS Science Advisory Board member. Former CIA Officer of Scientific Intelligence. Examined UAP experiencer medical cases.",
        "sources": [795, 801],
        "year_start": 1995,
        "year_end": 2004,
    },
    {
        "source": "Kit Green",
        "target": "CIA",
        "type": "worked_for",
        "tier": "documented",
        "desc": "CIA Officer of Scientific Intelligence ('Weird Desk'). Assessed anomalous phenomena reports for the Agency.",
        "sources": [795],
        "year_start": 1969,
        "year_end": 1985,
    },
    # --- Jacques Vallée ---
    {
        "source": "Jacques Vallée",
        "target": "AAWSAP",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Consulted for AAWSAP/BAASS. Provided historical UAP research and materials analysis expertise.",
        "sources": [785, 786],
        "year_start": 2008,
        "year_end": 2012,
    },
    {
        "source": "Jacques Vallée",
        "target": "Project Blue Book",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Worked with J. Allen Hynek at Northwestern on Blue Book data analysis. Pioneer of scientific approach to UFO research.",
        "sources": [785],
        "year_start": 1963,
        "year_end": 1969,
    },
    # --- Wilson-Davis ---
    {
        "source": "Eric Davis",
        "target": "Wilson-Davis Memo",
        "type": "authored",
        "tier": "credible",
        "desc": "Authored notes from 2002 meeting with Admiral Wilson. Davis has confirmed the notes are authentic. Describes being told of UAP reverse-engineering SAP.",
        "sources": [784],
        "year_start": 2002,
        "year_end": 2002,
    },
    {
        "source": "David Grusch",
        "target": "Wilson-Davis Memo",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Grusch's congressional testimony corroborates Wilson-Davis claims: described legacy crash retrieval and reverse-engineering programs run by defense contractors.",
        "sources": [784, 796],
        "year_start": 2023,
        "year_end": 2023,
    },
    # --- Battelle ---
    {
        "source": "Battelle Memorial Institute",
        "target": "Project Blue Book",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Conducted statistical analysis for Blue Book (Special Report No. 14, 1955). Found significant percentage of cases genuinely 'unknown.'",
        "sources": [789],
        "year_start": 1952,
        "year_end": 1955,
    },
    # --- Skinwalker Ranch ---
    {
        "source": "Robert Bigelow",
        "target": "Skinwalker Ranch",
        "type": "owned_by",
        "tier": "documented",
        "desc": "Purchased Skinwalker Ranch in 1996. NIDS then BAASS conducted field research there for 20 years.",
        "sources": [787, 788],
        "year_start": 1996,
        "year_end": 2016,
    },
    {
        "source": "AAWSAP",
        "target": "Skinwalker Ranch",
        "type": "investigated",
        "tier": "documented",
        "desc": "AAWSAP included Skinwalker Ranch investigation as part of its anomalous phenomena research mandate.",
        "sources": [781],
        "year_start": 2008,
        "year_end": 2012,
    },
    # --- Roswell ---
    {
        "source": "Roswell Incident",
        "target": "Wright-Patterson AFB",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Multiple witnesses reported recovered materials shipped to Wright-Patterson (then Wright Field). Foreign Technology Division housed there.",
        "sources": [791, 792, 802],
        "year_start": 1947,
        "year_end": 1947,
    },
    # --- Sol Foundation ---
    {
        "source": "Jacques Vallée",
        "target": "Sol Foundation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Participated in Sol Foundation inaugural symposium at Stanford. Contributes scientific expertise to policy discussions.",
        "sources": [803],
        "year_start": 2023,
        "year_end": None,
    },
    {
        "source": "David Grusch",
        "target": "Sol Foundation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Presented at Sol Foundation symposium. Foundation provides academic legitimacy to UAP disclosure discussion.",
        "sources": [796, 803],
        "year_start": 2023,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Robert Bigelow": [781, 787, 788, 801],
    "Eric Davis": [783, 784, 794],
    "Colm Kelleher": [781, 787],
    "Jacques Vallée": [785, 786],
    "Kit Green": [795, 801],
    "James Lacatski": [781, 782],
    "George Knapp": [781, 787, 800],
    "NIDS": [787, 801],
    "Bigelow Aerospace": [781, 782, 788],
    "Battelle Memorial Institute": [789],
    "Sol Foundation": [803],
    "AAWSAP": [781, 782, 783],
    "Skinwalker Ranch": [781, 787],
    "Area 51": [798, 799],
    "Wright-Patterson AFB": [789, 802],
    "Wilson-Davis Memo": [784],
    "Roswell Incident": [791, 792, 793],
}
