"""
Ritual & Occult — Intelligence Connections: Expansion layer for Intel Console.

Maps the documented intersections between occult organizations, ritual abuse
cases, and intelligence agencies. This is not fringe speculation — it is the
documented record of how military/intelligence figures participated in occult
organizations, how those organizations intersected with covert programs, and
how institutional investigations into ritual abuse were systematically shut down.

Three threads converge here:

1. OCCULT-INTELLIGENCE PIPELINE: Jack Parsons (JPL co-founder, OTO) worked
   with L. Ron Hubbard on the Babalon Working. Aleister Crowley ran OTO and
   had documented MI6 connections. Michael Aquino (NSA, DIA) founded the
   Temple of Set as a Church of Satan offshoot. The Thule Society fed directly
   into the Nazi party. These are not parallel tracks — they are the same
   people moving between occult practice and classified work.

2. INSTITUTIONAL ABUSE INVESTIGATIONS: The Presidio case (1986-87) implicated
   Lt. Col. Aquino in child abuse at a military daycare — charges dropped
   despite 60+ victims. The Franklin Cover-Up (1988-90) exposed a child
   trafficking ring running from Boys Town through Larry King to Washington
   elites — the grand jury indicted the victims instead. The Finders (1987)
   were a CIA-connected group caught with children — FOIA documents confirm
   CIA involvement, and the investigation was shut down.

3. GOVERNMENT INFILTRATION: Scientology's Operation Snow White (1973-77) was
   the largest known infiltration of the U.S. government — 5,000 agents placed
   in 136 government agencies, stealing documents and bugging offices. Eleven
   senior Scientologists convicted. Hubbard connected to Parsons before founding
   the church.

Entities (~20): People (Jack Parsons, Aleister Crowley, Michael Aquino,
L. Ron Hubbard, Anton LaVey, Larry King, Paul Bonacci, John DeCamp),
organizations (OTO, Temple of Set, Church of Scientology, Thule Society,
Process Church, The Finders), events/programs (Presidio Abuse Case,
Franklin Cover-Up, Operation Snow White, Babalon Working).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA, FBI, NSA, DOJ, Mossad,
  Bohemian Club, Skull & Bones,
  Allen Dulles, J. Edgar Hoover,
  MKULTRA

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 843-870
# ============================================================

SOURCES = [
    # --- Jack Parsons / OTO ---
    {
        "id": 843,
        "title": "George Pendle — Strange Angel: The Otherworldly Life of Rocket Scientist John Whiteside Parsons",
        "url": "https://en.wikipedia.org/wiki/Strange_Angel_(book)",
        "source_type": "book",
        "author": "George Pendle",
        "year": 2005,
    },
    {
        "id": 844,
        "title": "John Carter — Sex and Rockets: The Occult World of Jack Parsons",
        "url": "https://en.wikipedia.org/wiki/Sex_and_Rockets",
        "source_type": "book",
        "author": "John Carter",
        "year": 1999,
    },
    # --- Aleister Crowley / MI6 ---
    {
        "id": 845,
        "title": "Richard Spence — Secret Agent 666: Aleister Crowley, British Intelligence, and the Occult",
        "url": "https://en.wikipedia.org/wiki/Secret_Agent_666",
        "source_type": "book",
        "author": "Richard B. Spence",
        "year": 2008,
    },
    {
        "id": 846,
        "title": "Tobias Churton — Aleister Crowley: The Beast in Berlin — Art, Sex, and Magick in the Weimar Republic",
        "url": "https://en.wikipedia.org/wiki/Aleister_Crowley",
        "source_type": "book",
        "author": "Tobias Churton",
        "year": 2014,
    },
    # --- Michael Aquino ---
    {
        "id": 847,
        "title": "Michael Aquino — MindWar (co-authored with Gen. Paul Vallely, 1980; expanded 2013)",
        "url": "https://en.wikipedia.org/wiki/Michael_Aquino_(Satanist)",
        "source_type": "other",
        "author": "Michael A. Aquino",
        "year": 1980,
    },
    {
        "id": 848,
        "title": "San Jose Mercury News — 'Army of the Night' (Presidio abuse investigation coverage, 1988)",
        "url": "https://en.wikipedia.org/wiki/Presidio_of_San_Francisco#Child_abuse_scandal",
        "source_type": "journalism",
        "year": 1988,
    },
    {
        "id": 849,
        "title": "Linda Goldston — San Jose Mercury News investigative series on Presidio child abuse case (60+ alleged victims)",
        "url": "https://en.wikipedia.org/wiki/Presidio_of_San_Francisco",
        "source_type": "journalism",
        "author": "Linda Goldston",
        "year": 1988,
    },
    # --- Franklin Cover-Up ---
    {
        "id": 850,
        "title": "John DeCamp — The Franklin Cover-Up: Child Abuse, Satanism, and Murder in Nebraska",
        "url": "https://en.wikipedia.org/wiki/Franklin_child_prostitution_ring_allegations",
        "source_type": "book",
        "author": "John W. DeCamp",
        "year": 1992,
    },
    {
        "id": 851,
        "title": "Nick Bryant — The Franklin Scandal: A Story of Powerbrokers, Child Abuse & Betrayal",
        "url": "https://en.wikipedia.org/wiki/Franklin_child_prostitution_ring_allegations",
        "source_type": "book",
        "author": "Nick Bryant",
        "year": 2009,
    },
    {
        "id": 852,
        "title": "Paul Bonacci v. Lawrence King — U.S. District Court ruling (Judge Warren Urbom awarded $1M default judgment to Bonacci, Feb 1999)",
        "url": "https://law.justia.com/cases/federal/district-courts/FSupp2/4/1137/2577953/",
        "source_type": "court",
        "year": 1999,
    },
    {
        "id": 853,
        "title": "Omaha World-Herald — coverage of Franklin Credit Union investigation and Larry King indictment (1988-1991)",
        "url": "https://en.wikipedia.org/wiki/Franklin_child_prostitution_ring_allegations",
        "source_type": "journalism",
        "year": 1989,
    },
    {
        "id": 854,
        "title": "Yorkshire Television — 'Conspiracy of Silence' (documentary pulled from Discovery Channel before airing, 1994)",
        "url": "https://en.wikipedia.org/wiki/Conspiracy_of_Silence_(1994_film)",
        "source_type": "documentary",
        "year": 1994,
    },
    # --- Scientology / Operation Snow White ---
    {
        "id": 855,
        "title": "United States v. Mary Sue Hubbard et al. — Criminal case No. 78-401, D.C. District Court (Operation Snow White convictions, 1979)",
        "url": "https://en.wikipedia.org/wiki/Operation_Snow_White",
        "source_type": "court",
        "year": 1979,
    },
    {
        "id": 856,
        "title": "Lawrence Wright — Going Clear: Scientology, Hollywood, and the Prison of Belief",
        "url": "https://en.wikipedia.org/wiki/Going_Clear_(book)",
        "source_type": "book",
        "author": "Lawrence Wright",
        "year": 2013,
    },
    {
        "id": 857,
        "title": "Russell Miller — Bare-Faced Messiah: The True Story of L. Ron Hubbard",
        "url": "https://en.wikipedia.org/wiki/Bare-Faced_Messiah",
        "source_type": "book",
        "author": "Russell Miller",
        "year": 1987,
    },
    # --- The Finders ---
    {
        "id": 858,
        "title": "U.S. Customs Service — 'The Finders' investigative report (1987, declassified via FOIA)",
        "url": "https://vault.fbi.gov/the-finders",
        "source_type": "foia",
        "year": 1987,
    },
    {
        "id": 859,
        "title": "FBI Vault — The Finders FOIA release (324 pages, released 2019)",
        "url": "https://vault.fbi.gov/the-finders",
        "source_type": "foia",
        "year": 2019,
    },
    {
        "id": 860,
        "title": "Washington Post — 'The Finders: Mystery of the Disappearing Children' (coverage of 1987 Tallahassee arrest and CIA connections)",
        "url": "https://en.wikipedia.org/wiki/Finders_(group)",
        "source_type": "journalism",
        "year": 1987,
    },
    # --- Thule Society ---
    {
        "id": 861,
        "title": "Nicholas Goodrick-Clarke — The Occult Roots of Nazism: Secret Aryan Cults and Their Influence on Nazi Ideology",
        "url": "https://en.wikipedia.org/wiki/The_Occult_Roots_of_Nazism",
        "source_type": "academic",
        "author": "Nicholas Goodrick-Clarke",
        "year": 1985,
    },
    {
        "id": 862,
        "title": "Peter Levenda — Unholy Alliance: A History of Nazi Involvement with the Occult",
        "url": "https://en.wikipedia.org/wiki/Peter_Levenda",
        "source_type": "book",
        "author": "Peter Levenda",
        "year": 1995,
    },
    # --- Process Church ---
    {
        "id": 863,
        "title": "Timothy Wyllie — Love Sex Fear Death: The Inside Story of the Process Church of the Final Judgment",
        "url": "https://en.wikipedia.org/wiki/Process_Church_of_the_Final_Judgment",
        "source_type": "book",
        "author": "Timothy Wyllie",
        "year": 2009,
    },
    {
        "id": 864,
        "title": "Ed Sanders — The Family: The Story of Charles Manson's Dune Buggy Attack Battalion (Process Church connections)",
        "url": "https://en.wikipedia.org/wiki/The_Family_(Sanders_book)",
        "source_type": "book",
        "author": "Ed Sanders",
        "year": 1971,
    },
    # --- Anton LaVey ---
    {
        "id": 865,
        "title": "Blanche Barton — The Secret Life of a Satanist: The Authorized Biography of Anton Szandor LaVey",
        "url": "https://en.wikipedia.org/wiki/Anton_LaVey",
        "source_type": "book",
        "author": "Blanche Barton",
        "year": 1990,
    },
    # --- MKUltra / Mind Control Context ---
    {
        "id": 866,
        "title": "Senate Select Committee on Intelligence — Project MKULTRA, the CIA's Program of Research in Behavioral Modification (1977 hearings)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/hearings/95mkultra.pdf",
        "source_type": "congressional",
        "year": 1977,
    },
    # --- Cross-cutting / General ---
    {
        "id": 867,
        "title": "Peter Levenda — Sinister Forces: A Grimoire of American Political Witchcraft (trilogy, 2005-2011)",
        "url": "https://en.wikipedia.org/wiki/Peter_Levenda",
        "source_type": "book",
        "author": "Peter Levenda",
        "year": 2005,
    },
    {
        "id": 868,
        "title": "Dave McGowan — Programmed to Kill: The Politics of Serial Murder (Finders, Presidio, Franklin connections)",
        "url": "https://en.wikipedia.org/wiki/David_McGowan",
        "source_type": "book",
        "author": "David McGowan",
        "year": 2004,
    },
    {
        "id": 869,
        "title": "FBI — Investigation of the Church of Scientology (FOIA release, multiple files)",
        "url": "https://vault.fbi.gov/scientology",
        "source_type": "foia",
        "year": 1979,
    },
    {
        "id": 870,
        "title": "JPL / Caltech — institutional history acknowledging Jack Parsons as co-founder of Jet Propulsion Laboratory (1936-1952)",
        "url": "https://en.wikipedia.org/wiki/Jack_Parsons_(rocket_engineer)",
        "source_type": "other",
        "year": 1936,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- People ---
    {
        "name": "Jack Parsons",
        "entity_type": "person",
        "description": "Rocket engineer, co-founder of Jet Propulsion Laboratory (JPL) and Aerojet. Head of OTO Agape Lodge in Pasadena. Conducted the 'Babalon Working' ritual with L. Ron Hubbard (1946). Exemplifies the occult-technology intersection — simultaneously advancing U.S. rocketry and practicing Thelemic magick under Aleister Crowley's system. Died in 1952 explosion at his home laboratory.",
        "aliases": "John Whiteside Parsons, Marvel Whiteside Parsons",
        "metadata": {"role": "rocket scientist / occultist", "birth_date": "1914-10-02", "death_date": "1952-06-17"},
    },
    {
        "name": "Aleister Crowley",
        "entity_type": "person",
        "description": "British occultist, founder of Thelema, head of Ordo Templi Orientis (OTO). Documented connections to British intelligence (MI5/MI6) — worked as agent during WWI and WWII per Richard Spence's archival research. Mentored Jack Parsons remotely through OTO hierarchy. His system of magick influenced multiple organizations that intersected with intelligence agencies.",
        "aliases": "The Great Beast, Edward Alexander Crowley",
        "metadata": {"role": "occultist / intelligence asset", "birth_date": "1875-10-12", "death_date": "1947-12-01"},
    },
    {
        "name": "Michael Aquino",
        "entity_type": "person",
        "description": "Lt. Colonel, U.S. Army. Psychological operations specialist with top-secret clearances (NSA, DIA). Founded the Temple of Set (1975) as a breakaway from Anton LaVey's Church of Satan. Co-authored 'From PSYOP to MindWar' (1980) with Gen. Paul Vallely, proposing psychotronic weapons and mass psychological manipulation. Named as suspect in the Presidio Army daycare abuse case (1986-87) — charges dropped despite 60+ alleged victims. The convergence of his military PSYOP career with his Temple of Set leadership remains one of the most documented occult-intelligence connections.",
        "aliases": "",
        "metadata": {"role": "Army PSYOP / Temple of Set founder", "birth_date": "1946-10-16", "death_date": "2019-09-01"},
    },
    {
        "name": "L. Ron Hubbard",
        "entity_type": "person",
        "description": "Science fiction writer who founded the Church of Scientology (1954). Participated in the Babalon Working with Jack Parsons at OTO Agape Lodge (1945-46), reportedly absconding with Parsons' money and girlfriend. Created Dianetics (1950) and built Scientology into a global organization. Oversaw or directed Operation Snow White — the largest known infiltration of the U.S. government. Went into hiding in 1980 to avoid legal proceedings.",
        "aliases": "Lafayette Ronald Hubbard",
        "metadata": {"role": "Scientology founder", "birth_date": "1911-03-13", "death_date": "1986-01-24"},
    },
    {
        "name": "Anton LaVey",
        "entity_type": "person",
        "description": "Founded the Church of Satan in San Francisco (1966). Authored 'The Satanic Bible' (1969). Michael Aquino was a member before splitting to form the Temple of Set. LaVey maintained connections within San Francisco's political and entertainment circles. Some researchers (Levenda, McGowan) note overlap between his social network and intelligence-connected figures in the Bay Area, though direct agency ties remain unsubstantiated.",
        "aliases": "Howard Stanton Levey",
        "metadata": {"role": "Church of Satan founder", "birth_date": "1930-04-11", "death_date": "1997-10-29"},
    },
    {
        "name": "Larry King",
        "entity_type": "person",
        "description": "NOT the television host. Manager of Franklin Credit Union in Omaha, Nebraska. Republican power broker who sang the national anthem at the 1984 Republican National Convention. Convicted of financial fraud (1991) — $40M embezzlement from Franklin Credit Union. Accused by multiple witnesses (including Paul Bonacci) of running a child trafficking ring connecting Boys Town to Washington D.C. elites. Judge Warren Urbom awarded $1M default judgment to Bonacci against King (1999).",
        "aliases": "Lawrence E. King Jr.",
        "metadata": {"role": "Franklin Credit Union manager", "birth_date": "1944-01-01"},
    },
    {
        "name": "Paul Bonacci",
        "entity_type": "person",
        "description": "Key witness in the Franklin Cover-Up. Testified under oath about being trafficked as a child through a network operating out of Boys Town, Omaha, connecting to Washington D.C. Named Larry King as a central figure. Awarded $1M in damages by U.S. District Judge Warren Urbom (1999) in civil suit against King — the judge found Bonacci's testimony credible. His account corroborated by other witnesses including Alisha Owen, though a Nebraska grand jury controversially indicted the accusers rather than the accused.",
        "aliases": "",
        "metadata": {"role": "Franklin scandal witness"},
    },
    {
        "name": "John DeCamp",
        "entity_type": "person",
        "description": "Nebraska state senator and Vietnam veteran. Investigated the Franklin Credit Union scandal and represented Paul Bonacci in his civil suit against Larry King. Authored 'The Franklin Cover-Up' (1992). His investigation documented connections between Larry King's operation, Boys Town, and figures in Washington D.C. DeCamp also identified CIA operative Robert Keith Gray as connected to the network.",
        "aliases": "John W. DeCamp",
        "metadata": {"role": "Nebraska senator / investigator", "birth_date": "1941-06-06", "death_date": "2017-07-27"},
    },
    # --- Organizations ---
    {
        "name": "Ordo Templi Orientis",
        "entity_type": "organization",
        "description": "Occult fraternal organization restructured by Aleister Crowley around his Thelemic religious system. The OTO Agape Lodge in Pasadena, led by Jack Parsons, was the nexus where rocket science met ceremonial magick. L. Ron Hubbard participated in lodge activities before founding Scientology. Crowley himself had documented British intelligence connections. The OTO represents the organizational bridge between Western esoteric tradition and the military-intelligence world through its members' dual roles.",
        "aliases": "OTO, Agape Lodge",
        "metadata": {"type": "occult fraternal order", "founded": 1895},
    },
    {
        "name": "Temple of Set",
        "entity_type": "organization",
        "description": "Occult organization founded by Lt. Col. Michael Aquino (1975) as a breakaway from Anton LaVey's Church of Satan. Distinguished from LaVey's atheistic Satanism by its theistic approach — members believe Set is a real entity. Notable because its founder simultaneously held top-secret military clearances and worked in Army PSYOP/NSA. Aquino's Temple of Set involvement was known to Army leadership and did not prevent his continued security clearances.",
        "aliases": "",
        "metadata": {"type": "occult organization", "founded": 1975},
    },
    {
        "name": "Church of Scientology",
        "entity_type": "organization",
        "description": "Religious organization founded by L. Ron Hubbard (1954). Grew from Dianetics movement. Operated the largest known infiltration of the U.S. government (Operation Snow White, 1973-77) — 5,000 covert agents in 136 government agencies. Eleven senior members convicted (1979). Maintained an intelligence bureau (Guardian's Office, later Office of Special Affairs) modeled on covert operations. Obtained IRS tax-exempt status in 1993 after extensive legal and covert pressure campaign.",
        "aliases": "Scientology, CoS",
        "metadata": {"type": "religious organization", "founded": 1954},
    },
    {
        "name": "Thule Society",
        "entity_type": "organization",
        "description": "German occult and nationalist group founded in Munich (1918). Combined volkisch mysticism, Aryan racial theory, and anti-Semitism. Key precursor to the Nazi party — members included Rudolf Hess, Hans Frank, and Alfred Rosenberg. The German Workers' Party (DAP), which Hitler joined and renamed NSDAP (Nazi Party), was founded by Thule Society member Anton Drexler. Represents the documented connection between occult societies and the rise of totalitarian political movements.",
        "aliases": "Thule-Gesellschaft",
        "metadata": {"type": "occult/political society", "founded": 1918},
    },
    {
        "name": "Process Church of the Final Judgment",
        "entity_type": "organization",
        "description": "Religious group founded in London (1966) by Robert and Mary Ann DeGrimston, former Scientologists who applied Hubbard's techniques to create their own movement. Worshipped both Christ and Satan as complementary forces. Ed Sanders alleged connections to Charles Manson's circle in 'The Family' (1971) — the Process Church sued and the passage was removed, though subsequent researchers (Levenda, Wyllie) have revisited the question. Members included some who later surfaced in intelligence-adjacent contexts.",
        "aliases": "The Process, Process Church",
        "metadata": {"type": "religious movement", "founded": 1966},
    },
    {
        "name": "The Finders",
        "entity_type": "organization",
        "description": "Washington D.C.-based group led by Marion David Pettie. In 1987, two Finders members were arrested in Tallahassee, FL with six malnourished children. U.S. Customs investigation found evidence of international trafficking and a 'clear connection to the CIA.' The investigation was transferred from Customs to FBI to CIA — at which point it was classified as an 'internal matter' and shut down. FBI FOIA release (2019, 324 pages) confirmed CIA involvement. Pettie's wife worked for CIA; Pettie himself had intelligence connections.",
        "aliases": "Finders",
        "metadata": {"type": "CIA-connected group", "founded": 1971},
    },
    # --- Programs / Events ---
    {
        "name": "Presidio Abuse Case",
        "entity_type": "event",
        "description": "Child abuse investigation at the Presidio Army base daycare center in San Francisco (1986-87). Over 60 children identified as potential victims. Lt. Col. Michael Aquino (Temple of Set founder, Army PSYOP specialist with NSA/DIA clearances) was named as a suspect by multiple children. The Army's Criminal Investigation Division investigated. Charges were dropped, officially due to jurisdictional issues and difficulty with child witness testimony. The case was extensively covered by the San Jose Mercury News.",
        "aliases": "",
        "metadata": {"date_range": "1986-1988", "location": "Presidio of San Francisco"},
    },
    {
        "name": "Franklin Cover-Up",
        "entity_type": "event",
        "description": "Scandal centered on Franklin Credit Union in Omaha, Nebraska (1988-1991). Manager Larry King embezzled $40M and was convicted of financial fraud. Multiple witnesses (Paul Bonacci, Alisha Owen, Troy Boner) testified about a child trafficking ring running from Boys Town through King to Washington D.C. elites. A Nebraska grand jury controversially indicted the accusers for perjury rather than investigating the accused. Bonacci later won a $1M civil judgment against King (1999). A documentary ('Conspiracy of Silence') was produced by Yorkshire Television for Discovery Channel but pulled before airing.",
        "aliases": "Franklin Scandal",
        "metadata": {"date_range": "1988-1999", "location": "Omaha, NE / Washington, D.C."},
    },
    {
        "name": "Operation Snow White",
        "entity_type": "event",
        "description": "Church of Scientology covert operation (1973-77) to infiltrate the U.S. government and purge unfavorable records about Scientology and L. Ron Hubbard. The largest known infiltration of the U.S. government in history — 5,000 covert agents placed in 136 government agencies including the IRS, FBI, DOJ, and DEA. Agents stole government documents and planted bugging devices. Eleven senior Scientologists convicted (1979) including Mary Sue Hubbard (L. Ron Hubbard's wife). L. Ron Hubbard was named as an unindicted co-conspirator.",
        "aliases": "",
        "metadata": {"date_range": "1973-1977"},
    },
    {
        "name": "Babalon Working",
        "entity_type": "event",
        "description": "Series of Thelemic rituals performed by Jack Parsons and L. Ron Hubbard in Pasadena (January-March 1946). Conducted under the framework of Aleister Crowley's OTO system, the rituals were intended to summon a 'moonchild' or incarnation of the goddess Babalon. Crowley, informed by OTO leaders, dismissed the working and referred to Hubbard as a 'confidence man.' Shortly after, Hubbard left with Parsons' girlfriend and money from their joint business venture. The episode marks the nexus point between rocketry, occultism, and Scientology's founder.",
        "aliases": "",
        "metadata": {"date": "1946-01", "location": "Pasadena, CA"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # === PARSONS / OTO / CROWLEY CLUSTER ===
    {
        "source": "Jack Parsons",
        "target": "Ordo Templi Orientis",
        "type": "led",
        "tier": "documented",
        "desc": "Head of OTO Agape Lodge in Pasadena. Led the lodge from early 1940s until his death in 1952.",
        "sources": [843, 844],
        "year_start": 1941,
        "year_end": 1952,
    },
    {
        "source": "Aleister Crowley",
        "target": "Ordo Templi Orientis",
        "type": "led",
        "tier": "documented",
        "desc": "Restructured OTO around his Thelemic system. Served as Outer Head of the Order from 1922 until his death.",
        "sources": [845, 846],
        "year_start": 1922,
        "year_end": 1947,
    },
    {
        "source": "Jack Parsons",
        "target": "Aleister Crowley",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Parsons led Crowley's OTO Agape Lodge. Corresponded with Crowley through OTO hierarchy. Crowley supervised remotely and was informed of the Babalon Working, which he dismissed.",
        "sources": [843, 844, 845],
        "year_start": 1941,
        "year_end": 1947,
    },
    {
        "source": "Jack Parsons",
        "target": "L. Ron Hubbard",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Hubbard participated in OTO Agape Lodge activities and co-performed the Babalon Working with Parsons (Jan-Mar 1946). Hubbard then left with Parsons' girlfriend and money. Crowley called Hubbard a 'confidence man.'",
        "sources": [843, 844, 857],
        "year_start": 1945,
        "year_end": 1946,
    },
    {
        "source": "Jack Parsons",
        "target": "Babalon Working",
        "type": "conducted",
        "tier": "documented",
        "desc": "Parsons conceived and led the Babalon Working rituals using Crowley's Thelemic framework, with Hubbard serving as 'scribe.'",
        "sources": [843, 844],
        "year_start": 1946,
        "year_end": 1946,
    },
    {
        "source": "L. Ron Hubbard",
        "target": "Babalon Working",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Served as 'scribe' during the Babalon Working. His precise role is debated — Scientology claims he was infiltrating the OTO on behalf of Naval Intelligence, though no evidence supports this.",
        "sources": [843, 844, 857],
        "year_start": 1946,
        "year_end": 1946,
    },
    # --- Parsons / Rocketry ---
    {
        "source": "Jack Parsons",
        "target": "MKULTRA",
        "type": "connected_to",
        "tier": "inference",
        "desc": "No direct connection, but Parsons exemplifies the occult-technology pipeline: co-founded JPL while leading OTO, in the same milieu where CIA would later recruit for MKULTRA's behavioral research. Parsons died (1952) before MKULTRA began (1953).",
        "sources": [843, 867],
        "year_start": 1936,
        "year_end": 1952,
    },
    # --- Crowley / Intelligence ---
    {
        "source": "Aleister Crowley",
        "target": "Mossad",
        "type": "connected_to",
        "tier": "inference",
        "desc": "No direct Mossad connection (Mossad founded 1949, Crowley died 1947), but Crowley's MI6 intelligence work established the template of occult figures serving intelligence agencies that later extended to other services.",
        "sources": [845],
        "year_start": None,
        "year_end": None,
    },
    # === AQUINO / TEMPLE OF SET / PRESIDIO ===
    {
        "source": "Michael Aquino",
        "target": "Temple of Set",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded the Temple of Set in 1975 after splitting from Anton LaVey's Church of Satan. Led the organization while simultaneously holding Army PSYOP positions and top-secret clearances.",
        "sources": [847, 865],
        "year_start": 1975,
        "year_end": 2019,
    },
    {
        "source": "Michael Aquino",
        "target": "NSA",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Held top-secret NSA clearances while serving in Army psychological operations. His Temple of Set leadership was known to Army and did not prevent continued security clearances.",
        "sources": [847, 848],
        "year_start": 1968,
        "year_end": 1990,
    },
    {
        "source": "Michael Aquino",
        "target": "Presidio Abuse Case",
        "type": "implicated_in",
        "tier": "credible",
        "desc": "Named as suspect by multiple children in the Presidio Army daycare abuse investigation (1986-87). Army CID investigated. Charges dropped — officially due to jurisdictional issues. Over 60 children identified as potential victims.",
        "sources": [848, 849, 868],
        "year_start": 1986,
        "year_end": 1988,
    },
    {
        "source": "Michael Aquino",
        "target": "Anton LaVey",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Aquino was a member of LaVey's Church of Satan before splitting to found the Temple of Set (1975). The schism was over theology — Aquino insisted Set was a real entity, not a symbol.",
        "sources": [847, 865],
        "year_start": 1969,
        "year_end": 1975,
    },
    {
        "source": "Michael Aquino",
        "target": "MKULTRA",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Aquino's 'From PSYOP to MindWar' (1980) proposed techniques (psychotronics, electromagnetic manipulation of behavior) that researchers note parallel MKULTRA successor programs. No direct participation documented, but the conceptual lineage from MKULTRA mind control to MindWar psychological operations is evident.",
        "sources": [847, 866, 867],
        "year_start": 1980,
        "year_end": None,
    },
    # --- LaVey ---
    {
        "source": "Anton LaVey",
        "target": "Michael Aquino",
        "type": "connected_to",
        "tier": "documented",
        "desc": "LaVey's Church of Satan was the incubator from which Aquino emerged. The Church of Satan → Temple of Set pipeline placed an active-duty Army PSYOP officer at the head of an occult organization.",
        "sources": [847, 865],
        "year_start": 1966,
        "year_end": 1975,
    },
    # === FRANKLIN COVER-UP CLUSTER ===
    {
        "source": "Larry King",
        "target": "Franklin Cover-Up",
        "type": "implicated_in",
        "tier": "documented",
        "desc": "Central figure in the Franklin scandal. Convicted of $40M embezzlement from Franklin Credit Union. Multiple witnesses testified he ran a child trafficking operation. Civil court found Bonacci's testimony credible (1999).",
        "sources": [850, 851, 852, 853],
        "year_start": 1988,
        "year_end": 1999,
    },
    {
        "source": "Paul Bonacci",
        "target": "Franklin Cover-Up",
        "type": "witness_in",
        "tier": "documented",
        "desc": "Key witness who testified under oath about being trafficked through Larry King's network. Awarded $1M default judgment against King by U.S. District Judge Warren Urbom (1999) who found his testimony credible.",
        "sources": [850, 851, 852],
        "year_start": 1988,
        "year_end": 1999,
    },
    {
        "source": "Paul Bonacci",
        "target": "Larry King",
        "type": "accused",
        "tier": "documented",
        "desc": "Bonacci testified King was the central organizer of the trafficking ring. Won $1M civil judgment against King (1999). Court record documents the accusation and judicial finding.",
        "sources": [852, 850],
        "year_start": 1988,
        "year_end": 1999,
    },
    {
        "source": "John DeCamp",
        "target": "Franklin Cover-Up",
        "type": "investigated",
        "tier": "documented",
        "desc": "Nebraska state senator who investigated the Franklin scandal, represented Bonacci in civil suit, and authored 'The Franklin Cover-Up' (1992). Documented connections to Washington D.C. elites.",
        "sources": [850, 851],
        "year_start": 1988,
        "year_end": 1999,
    },
    {
        "source": "John DeCamp",
        "target": "Paul Bonacci",
        "type": "represented",
        "tier": "documented",
        "desc": "DeCamp served as Bonacci's attorney in the civil suit against Larry King that resulted in the $1M judgment (1999).",
        "sources": [850, 852],
        "year_start": 1991,
        "year_end": 1999,
    },
    {
        "source": "FBI",
        "target": "Franklin Cover-Up",
        "type": "investigated",
        "tier": "documented",
        "desc": "FBI investigated the Franklin Credit Union scandal. Critics (DeCamp, Bryant) allege the FBI focused on discrediting witnesses rather than pursuing the abuse allegations. Grand jury indicted accusers for perjury.",
        "sources": [850, 851, 853],
        "year_start": 1988,
        "year_end": 1991,
    },
    # === SCIENTOLOGY / SNOW WHITE ===
    {
        "source": "L. Ron Hubbard",
        "target": "Church of Scientology",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded the Church of Scientology (1954) building on his earlier Dianetics movement (1950). Maintained control until his death in 1986.",
        "sources": [856, 857],
        "year_start": 1954,
        "year_end": 1986,
    },
    {
        "source": "Church of Scientology",
        "target": "Operation Snow White",
        "type": "operated",
        "tier": "documented",
        "desc": "Church's Guardian's Office executed Operation Snow White — the largest known infiltration of the U.S. government. 5,000 covert agents in 136 agencies. Eleven senior members convicted (1979).",
        "sources": [855, 856, 869],
        "year_start": 1973,
        "year_end": 1977,
    },
    {
        "source": "L. Ron Hubbard",
        "target": "Operation Snow White",
        "type": "directed",
        "tier": "documented",
        "desc": "Named as unindicted co-conspirator in Operation Snow White prosecution. His wife Mary Sue Hubbard was convicted. Court records establish Hubbard's directive role.",
        "sources": [855, 856],
        "year_start": 1973,
        "year_end": 1977,
    },
    {
        "source": "Operation Snow White",
        "target": "FBI",
        "type": "targeted",
        "tier": "documented",
        "desc": "Scientology agents infiltrated the FBI as part of Operation Snow White, stealing documents and planting covert agents. FBI was both a target and the agency that eventually raided Scientology offices (1977).",
        "sources": [855, 869],
        "year_start": 1973,
        "year_end": 1977,
    },
    {
        "source": "Operation Snow White",
        "target": "DOJ",
        "type": "targeted",
        "tier": "documented",
        "desc": "DOJ was among the 136 government agencies infiltrated by Scientology's Operation Snow White. DOJ ultimately prosecuted the case.",
        "sources": [855, 856],
        "year_start": 1973,
        "year_end": 1979,
    },
    # --- Process Church ---
    {
        "source": "Process Church of the Final Judgment",
        "target": "Church of Scientology",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Process Church founders Robert and Mary Ann DeGrimston were former Scientologists who applied Hubbard's auditing techniques to create their own movement. Direct organizational lineage from Scientology to Process Church.",
        "sources": [863, 856],
        "year_start": 1966,
        "year_end": 1974,
    },
    # === THE FINDERS / CIA ===
    {
        "source": "The Finders",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "U.S. Customs investigation (1987) found 'clear connection to the CIA.' Investigation transferred from Customs to CIA, classified as 'internal matter,' and shut down. FBI FOIA release (2019) confirmed CIA involvement. Group leader Pettie's wife worked for CIA.",
        "sources": [858, 859, 860],
        "year_start": 1987,
        "year_end": 1987,
    },
    {
        "source": "CIA",
        "target": "The Finders",
        "type": "covered_for",
        "tier": "credible",
        "desc": "When Customs found CIA connections, the investigation was transferred to CIA and classified as an 'internal matter' — effectively terminating the criminal investigation. Pattern consistent with CIA protecting assets.",
        "sources": [858, 859, 868],
        "year_start": 1987,
        "year_end": 1987,
    },
    # === THULE SOCIETY ===
    {
        "source": "Thule Society",
        "target": "Skull & Bones",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both secret societies with elite recruitment, political influence, and occult symbolism. No direct organizational link, but represent parallel structures in German and American contexts — elite secret societies shaping political movements.",
        "sources": [861, 867],
        "year_start": None,
        "year_end": None,
    },
    # === CROSS-CUTTING CONNECTIONS ===
    {
        "source": "Presidio Abuse Case",
        "target": "Franklin Cover-Up",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both cases emerged in the same period (1986-1990), both involved allegations of institutional child abuse with connections to powerful figures, and both investigations were effectively shut down. Researchers (DeCamp, McGowan) have noted the pattern of suppression across both cases.",
        "sources": [850, 868],
        "year_start": 1986,
        "year_end": 1991,
    },
    {
        "source": "Franklin Cover-Up",
        "target": "CIA",
        "type": "connected_to",
        "tier": "inference",
        "desc": "DeCamp identified CIA operative Robert Keith Gray as connected to the Franklin network. Nick Bryant documented additional intelligence connections. Pattern of investigation suppression consistent with intelligence protection of assets.",
        "sources": [850, 851],
        "year_start": 1988,
        "year_end": 1991,
    },
    {
        "source": "Aleister Crowley",
        "target": "Thule Society",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Crowley's OTO operated in the same German occult milieu as the Thule Society. Crowley was active in Germany (Berlin, 1930s). Both drew from the same Western esoteric tradition, though they represented different ideological streams — Thelema vs. Ariosophic volkisch mysticism.",
        "sources": [845, 846, 861],
        "year_start": 1918,
        "year_end": 1935,
    },
    {
        "source": "L. Ron Hubbard",
        "target": "Ordo Templi Orientis",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Hubbard participated in OTO Agape Lodge activities in Pasadena (1945-46) through his association with Jack Parsons. His involvement predates the founding of Dianetics/Scientology.",
        "sources": [843, 844, 857],
        "year_start": 1945,
        "year_end": 1946,
    },
    {
        "source": "Allen Dulles",
        "target": "MKULTRA",
        "type": "authorized",
        "tier": "documented",
        "desc": "As CIA Director, authorized MKULTRA in 1953. The program's behavioral modification research represents the institutional counterpart to the occult organizations' interest in altering consciousness.",
        "sources": [866],
        "year_start": 1953,
        "year_end": 1961,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Jack Parsons": [843, 844, 867, 870],
    "Aleister Crowley": [845, 846, 867],
    "Michael Aquino": [847, 848, 849, 868],
    "L. Ron Hubbard": [843, 844, 856, 857],
    "Anton LaVey": [865, 847],
    "Larry King": [850, 851, 852, 853, 854],
    "Paul Bonacci": [850, 851, 852],
    "John DeCamp": [850, 851],
    "Ordo Templi Orientis": [843, 844, 845],
    "Temple of Set": [847, 848],
    "Church of Scientology": [855, 856, 857, 869],
    "Thule Society": [861, 862],
    "Process Church of the Final Judgment": [863, 864],
    "The Finders": [858, 859, 860],
    "Presidio Abuse Case": [848, 849, 868],
    "Franklin Cover-Up": [850, 851, 852, 853, 854],
    "Operation Snow White": [855, 856, 869],
    "Babalon Working": [843, 844],
}
