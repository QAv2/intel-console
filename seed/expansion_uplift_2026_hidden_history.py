"""
Hidden History — 2026 Uplift Expansion for Intel Console.

2025 Assassination Files Releases: Trump's Executive Order 14176 (Jan 23, 2025)
ordered full declassification of JFK, RFK, and MLK assassination records.
Between March 2025 and January 2026, approximately 94,643 pages of JFK files
were released without redactions — the largest single release of assassination
records in history. Key revelations included confirmation of CIA officer George
Joannides' direction of the DRE Cuban exile group that monitored Oswald, and
documentation of systematic CIA concealment from the Warren Commission and HSCA.

RFK files released April–June 2025 (including autopsy photographs). MLK files
released July 2025. House Task Force on Declassification of Federal Secrets
(Chair: Anna Paulina Luna) established February 2025 to oversee implementation.

NEW ENTITIES (6): Executive Order 14176, JFK Files Release (2025),
    George Joannides, Anna Paulina Luna,
    House Task Force on Declassification of Federal Secrets,
    Directorio Revolucionario Estudiantil

EXISTING ENTITIES UPDATED (11): JFK Assassination, Warren Commission, HSCA,
    Lee Harvey Oswald, David Atlee Phillips, Allen Dulles, RFK Assassination,
    MLK Assassination, Sirhan Sirhan, ARRB, Jim Garrison

EXISTING ENTITIES REFERENCED: CIA, FBI, NSA, Donald Trump, Robert F. Kennedy,
    Martin Luther King Jr., James Earl Ray, Jack Ruby, Clay Shaw,
    E. Howard Hunt, John McCone, Office of the Director of National Intelligence

Evidence tiers:
  documented = official government document, court filing, FOIA, congressional record
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 2100–2199 (hidden_history allotment)
# ============================================================

SOURCES = [
    # Government / Archive
    {
        "id": 2100,
        "title": "National Archives — 2025 Release of JFK Assassination Records",
        "url": "https://www.archives.gov/research/jfk/release2025",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 2101,
        "title": "National Archives — JFK Assassination Records",
        "url": "https://www.archives.gov/research/jfk",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 2102,
        "title": "HSCA Final Report — Findings on the Assassination of President Kennedy",
        "url": "https://www.archives.gov/research/jfk/select-committee-report",
        "source_type": "government",
        "year": 1979,
    },
    # Reference / Encyclopedic
    {
        "id": 2103,
        "title": "Executive Order 14176 — Declassification of Assassination Records (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Executive_Order_14176",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2104,
        "title": "George Joannides — CIA officer and JFK assassination connection (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/George_Joannides",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2105,
        "title": "Anna Paulina Luna — U.S. Representative and Task Force chair (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Anna_Paulina_Luna",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2106,
        "title": "President John F. Kennedy Assassination Records Collection Act of 1992 (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/President_John_F._Kennedy_Assassination_Records_Collection_Act_of_1992",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2107,
        "title": "Assassination of Robert F. Kennedy — 2025 files release (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Assassination_of_Robert_F._Kennedy",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2108,
        "title": "Assassination of Martin Luther King Jr. — 2025 files release (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Assassination_of_Martin_Luther_King_Jr.",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2109,
        "title": "Directorio Revolucionario Estudiantil — CIA-funded Cuban exile group (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Directorio_Revolucionario_Estudiantil",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2110,
        "title": "David Atlee Phillips — CIA officer and JMWAVE operations (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/David_Atlee_Phillips",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2111,
        "title": "United States House Select Committee on Assassinations (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/United_States_House_Select_Committee_on_Assassinations",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2112,
        "title": "Allen Dulles — CIA Director and Warren Commissioner (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Allen_Dulles",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2113,
        "title": "Warren Commission (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Warren_Commission",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2114,
        "title": "Assassination Records Review Board (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Assassination_Records_Review_Board",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2115,
        "title": "Lee Harvey Oswald (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Lee_Harvey_Oswald",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2116,
        "title": "Sirhan Sirhan (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Sirhan_Sirhan",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 2117,
        "title": "Jim Garrison — Orleans Parish District Attorney (Wikipedia)",
        "url": "https://en.wikipedia.org/wiki/Jim_Garrison",
        "source_type": "other",
        "year": 2025,
    },
]

# ============================================================
# ENTITIES (6 new)
# ============================================================

ENTITIES = [
    {
        "name": "Executive Order 14176",
        "entity_type": "legislation",
        "description": (
            "Presidential directive signed by Donald Trump on January 23, 2025, ordering "
            "full declassification of records concerning the assassinations of President "
            "John F. Kennedy, Senator Robert F. Kennedy, and the Reverend Dr. Martin Luther "
            "King Jr. Directed the Director of National Intelligence to develop a JFK records "
            "release plan within 15 days and RFK/MLK plans within 45 days. Trump gave the "
            "signing pen to Robert F. Kennedy Jr., his nominee for HHS Secretary. "
            "Implementation produced the largest single release of assassination records in "
            "history: approximately 94,643 pages of JFK files released between March 2025 and "
            "January 2026 without redactions, followed by RFK files in April through June 2025 "
            "and MLK files in July 2025. The order prompted Speaker Mike Johnson to establish "
            "the House Task Force on Declassification of Federal Secrets in February 2025."
        ),
        "aliases": "EO 14176, Assassination Files Declassification Order",
        "metadata": {
            "date": "2025-01-23",
            "location": "Washington, D.C.",
        },
    },
    {
        "name": "JFK Files Release (2025)",
        "entity_type": "event",
        "description": (
            "Largest single declassification of JFK assassination records, released by the "
            "National Archives pursuant to Executive Order 14176. Six batches between March 18, "
            "2025 and January 30, 2026: 31,419 pages (March 18, 7 PM); 37,127 pages (March 18, "
            "10:30 PM); 14,318 pages (March 20); 53 pages (March 26); 704 pages (April 3); "
            "and 11,022 pages (January 30, 2026) — totaling approximately 94,643 pages across "
            "2,709 PDF files, all released without redactions. Key revelations included "
            "confirmation that CIA officer George Joannides directed the DRE Cuban exile group "
            "that monitored Lee Harvey Oswald in New Orleans, extensive documentation of CIA "
            "surveillance of Oswald prior to the assassination, and evidence of systematic CIA "
            "concealment from the Warren Commission and HSCA. Some records contained personal "
            "information of living individuals, prompting coordination with the Social Security "
            "Administration for protective measures."
        ),
        "aliases": "2025 JFK Declassification, JFK Files 2025",
        "metadata": {
            "date": "2025-03-18",
            "location": "Washington, D.C.",
        },
    },
    {
        "name": "George Joannides",
        "entity_type": "person",
        "description": (
            "CIA intelligence officer (1922-1990) who served from 1950 to 1979, reaching "
            "GS-16 supergrade rank. As Chief of the Psychological Warfare Branch at JMWAVE, "
            "the CIA's Miami station, Joannides directed and financed the Directorio "
            "Revolucionario Estudiantil (DRE) at $25,000 per month under the AMSPEL program. "
            "The DRE had direct confrontational contact with Lee Harvey Oswald in New Orleans "
            "in August 1963, three months before the Kennedy assassination. In 1978-79, "
            "Joannides was assigned as CIA liaison to the HSCA, where he concealed his DRE "
            "role from investigators. HSCA chief counsel G. Robert Blakey later stated "
            "Joannides 'obstructed our investigation.' Investigator Dan Hardway characterized "
            "his actions as a 'covert operation' to obstruct the probe. Documents released in "
            "March 2025 under Executive Order 14176 confirmed Joannides used the cover name "
            "'Howard' with the DRE — a connection the CIA had denied to the Warren Commission, "
            "HSCA, and ARRB for decades, claiming 'Howard' was merely a routing indicator. "
            "Received the Career Intelligence Medal in July 1981, with his HSCA liaison work "
            "cited among the reasons."
        ),
        "aliases": "Howard, Mr. Howard, Walter Newby",
        "metadata": {
            "nationality": "American",
            "born": "1922",
            "died": "1990",
            "status": "deceased",
            "role": "CIA officer, JMWAVE Psychological Warfare Branch chief",
        },
    },
    {
        "name": "Anna Paulina Luna",
        "entity_type": "person",
        "description": (
            "U.S. Representative (R-FL-13). In February 2025, appointed by Speaker Mike "
            "Johnson to chair the House Task Force on Declassification of Federal Secrets, "
            "established in response to Executive Order 14176 ordering release of JFK, RFK, "
            "and MLK assassination files. Under Luna's leadership, the task force expanded its "
            "scope beyond assassination records to include UAP transparency and whistleblower "
            "protection hearings by September 2025. Jefferson Morley, former Washington Post "
            "reporter and Mary Ferrell Foundation vice president, testified at the task force's "
            "first hearing. Luna received a report from Russian Ambassador Alexander Darchiev "
            "containing Russia's purported findings on the Kennedy assassination, which she "
            "called 'of massive historical significance.' Initiated a lawsuit against the U.S. "
            "government seeking release of NBC journalist Dave Wiegman Jr.'s and WBAP-TV "
            "journalist James Darnell's films from Dealey Plaza."
        ),
        "aliases": "Rep. Luna",
        "metadata": {
            "nationality": "American",
            "role": "U.S. Representative (R-FL-13), Chair of House Declassification Task Force",
        },
    },
    {
        "name": "House Task Force on Declassification of Federal Secrets",
        "entity_type": "organization",
        "description": (
            "Congressional task force established in February 2025 by Speaker Mike Johnson, "
            "chaired by Rep. Anna Paulina Luna (R-FL). Created in response to Executive Order "
            "14176 to oversee implementation of the declassification of JFK, RFK, and MLK "
            "assassination records. By September 2025, the task force expanded its scope to "
            "include hearings on UAP transparency and whistleblower protection. Jefferson "
            "Morley, former Washington Post reporter and vice president of the Mary Ferrell "
            "Foundation, testified at the task force's inaugural hearing on JFK records. "
            "The task force represents the first standing congressional body dedicated to "
            "overseeing the declassification process since the Assassination Records Review "
            "Board concluded its work in 1998."
        ),
        "aliases": "House Declassification Task Force, Luna Task Force",
        "metadata": {
            "type": "congressional task force",
            "founded": 2025,
        },
    },
    {
        "name": "Directorio Revolucionario Estudiantil",
        "entity_type": "organization",
        "description": (
            "Cuban student anti-Castro exile group founded in 1960, relocated to Miami where "
            "it became the largest anti-Castro student organization by 1963. Financed by the "
            "CIA at $25,000 per month under the AMSPEL program, directed by CIA officer George "
            "Joannides from the JMWAVE station's Psychological Warfare Branch. In August 1963, "
            "DRE member Carlos Bringuier confronted Lee Harvey Oswald distributing pro-Castro "
            "leaflets in New Orleans, leading to Oswald's arrest and a subsequent radio debate "
            "between Oswald and DRE members — a recording of which was sent to Joannides. "
            "Immediately after the Kennedy assassination on November 22, 1963, the DRE launched "
            "a public campaign asserting Oswald had acted on behalf of Cuba's government, "
            "aiming to create pressure for a U.S. attack on Cuba. CIA support ended December "
            "1966. The CIA's concealment of its direction of the DRE from the Warren Commission "
            "and HSCA was confirmed by documents released in March 2025."
        ),
        "aliases": "DRE, Revolutionary Student Directorate",
        "metadata": {
            "type": "anti-Castro exile group",
            "founded": 1960,
            "location": "Miami, Florida",
        },
    },
]

# ============================================================
# RELATIONSHIPS (30)
# ============================================================

RELATIONSHIPS = [
    # ---- Executive Order 14176 ----
    {
        "source": "Donald Trump",
        "target": "Executive Order 14176",
        "type": "signed_into_law",
        "tier": "documented",
        "desc": (
            "Signed Executive Order 14176 on January 23, 2025, ordering full "
            "declassification of records concerning the assassinations of JFK, RFK, and MLK. "
            "Gave the signing pen to Robert F. Kennedy Jr."
        ),
        "year_start": 2025,
        "sources": [2100, 2103],
    },
    {
        "source": "Executive Order 14176",
        "target": "JFK Files Release (2025)",
        "type": "caused",
        "tier": "documented",
        "desc": (
            "EO 14176 directed the DNI to develop a JFK records release plan within 15 days. "
            "Implementation produced the release of approximately 94,643 pages between March "
            "2025 and January 2026."
        ),
        "year_start": 2025,
        "sources": [2100, 2103],
    },
    {
        "source": "Executive Order 14176",
        "target": "JFK Assassination",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "EO 14176 ordered full declassification of all remaining records concerning the "
            "assassination of President John F. Kennedy."
        ),
        "year_start": 2025,
        "sources": [2103],
    },
    {
        "source": "Executive Order 14176",
        "target": "RFK Assassination",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "EO 14176 ordered declassification of records concerning the assassination of "
            "Senator Robert F. Kennedy. Plans due within 45 days. Files released April "
            "through June 2025."
        ),
        "year_start": 2025,
        "sources": [2103, 2107],
    },
    {
        "source": "Executive Order 14176",
        "target": "MLK Assassination",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "EO 14176 ordered declassification of records concerning the assassination of "
            "Reverend Dr. Martin Luther King Jr. Plans due within 45 days. Files released "
            "July 2025."
        ),
        "year_start": 2025,
        "sources": [2103, 2108],
    },
    {
        "source": "Executive Order 14176",
        "target": "CIA",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "EO 14176 directed the CIA to declassify and release assassination records. The "
            "CIA had previously appealed to withhold documents on national security grounds."
        ),
        "year_start": 2025,
        "sources": [2103, 2106],
    },
    {
        "source": "Executive Order 14176",
        "target": "FBI",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "EO 14176 directed the FBI to declassify and release assassination records. "
            "The FBI had previously appealed to withhold documents."
        ),
        "year_start": 2025,
        "sources": [2103],
    },
    {
        "source": "Executive Order 14176",
        "target": "Office of the Director of National Intelligence",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "EO 14176 directed the Director of National Intelligence to develop a JFK records "
            "release plan within 15 days and RFK/MLK plans within 45 days."
        ),
        "year_start": 2025,
        "sources": [2103],
    },
    # ---- JFK Files Release (2025) ----
    {
        "source": "JFK Files Release (2025)",
        "target": "JFK Assassination",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "Released approximately 94,643 pages of previously classified JFK assassination "
            "records across six batches between March 2025 and January 2026 without redactions."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [2100, 2101],
    },
    {
        "source": "JFK Files Release (2025)",
        "target": "Lee Harvey Oswald",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "Released documents revealed the extent of CIA surveillance of Oswald prior to "
            "the assassination, including monitoring through the DRE and CIA station activities."
        ),
        "year_start": 2025,
        "sources": [2100, 2106, 2115],
    },
    {
        "source": "JFK Files Release (2025)",
        "target": "George Joannides",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Released documents confirmed Joannides used the cover name 'Howard' with the DRE "
            "and directed the group during its contact with Oswald — a connection the CIA had "
            "denied to the Warren Commission, HSCA, and ARRB for decades."
        ),
        "year_start": 2025,
        "sources": [2100, 2104],
    },
    {
        "source": "JFK Files Release (2025)",
        "target": "CIA",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Released documents revealed systematic CIA concealment of operational connections "
            "to individuals and groups that had contact with Oswald, including the DRE "
            "directorship and JMWAVE surveillance operations."
        ),
        "year_start": 2025,
        "sources": [2100, 2104, 2106],
    },
    {
        "source": "JFK Files Release (2025)",
        "target": "HSCA",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "Released documents confirmed the HSCA was obstructed by CIA liaison George "
            "Joannides, who concealed his own operational role directing the DRE during its "
            "contact with Oswald."
        ),
        "year_start": 2025,
        "sources": [2100, 2104, 2111],
    },
    {
        "source": "JFK Files Release (2025)",
        "target": "Warren Commission",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "Released documents further documented the extent to which the CIA withheld "
            "information from the Warren Commission, including the existence and role of "
            "George Joannides as DRE handler."
        ),
        "year_start": 2025,
        "sources": [2100, 2104, 2113],
    },
    {
        "source": "JFK Files Release (2025)",
        "target": "Allen Dulles",
        "type": "documented",
        "tier": "credible",
        "desc": (
            "Released documents revealed the scope of CIA concealment from the Warren "
            "Commission during Dulles' tenure as a member — the agency he formerly directed "
            "withheld operational information about the DRE and Oswald surveillance from "
            "the commission he served on."
        ),
        "year_start": 2025,
        "sources": [2100, 2112],
    },
    # ---- George Joannides ----
    {
        "source": "George Joannides",
        "target": "CIA",
        "type": "employed_by",
        "tier": "documented",
        "desc": (
            "CIA intelligence officer from 1950 to 1979. Reached GS-16 supergrade rank. "
            "Served as Chief of the Psychological Warfare Branch at JMWAVE, the CIA's Miami "
            "station. Received the Career Intelligence Medal in July 1981."
        ),
        "year_start": 1950,
        "year_end": 1979,
        "sources": [2104],
    },
    {
        "source": "George Joannides",
        "target": "Directorio Revolucionario Estudiantil",
        "type": "handler_of",
        "tier": "documented",
        "desc": (
            "Directed and financed the DRE at $25,000 per month under the CIA's AMSPEL "
            "program from JMWAVE. Operated under cover names 'Howard' and 'Walter Newby.' "
            "Managed a staff of 24 with a $1.5 million budget. Confirmed by 2025 declassified "
            "records."
        ),
        "year_start": 1962,
        "year_end": 1964,
        "sources": [2104, 2109],
    },
    {
        "source": "George Joannides",
        "target": "HSCA",
        "type": "covered_for",
        "tier": "documented",
        "desc": (
            "Assigned as CIA liaison to the HSCA in 1978-79. Concealed his own prior role "
            "directing the DRE from investigators. HSCA chief counsel G. Robert Blakey stated "
            "Joannides 'obstructed our investigation.' Investigator Dan Hardway characterized "
            "his actions as a 'covert operation' to obstruct the probe."
        ),
        "year_start": 1978,
        "year_end": 1979,
        "sources": [2104, 2111],
    },
    {
        "source": "George Joannides",
        "target": "Lee Harvey Oswald",
        "type": "monitored",
        "tier": "credible",
        "desc": (
            "Directed the DRE, which had confrontational contact with Oswald in New Orleans "
            "in August 1963. A recording of Oswald's radio debate with DRE members was sent "
            "to Joannides. The operational chain — Joannides directing the DRE which monitored "
            "Oswald — is documented; the inference is that Joannides was aware of the monitoring."
        ),
        "year_start": 1963,
        "sources": [2104, 2109],
    },
    {
        "source": "George Joannides",
        "target": "David Atlee Phillips",
        "type": "worked_for",
        "tier": "credible",
        "desc": (
            "Both served at JMWAVE, the CIA's Miami station, during the same period. Phillips "
            "ran anti-Castro propaganda operations and managed the Mexico City station "
            "monitoring of Oswald. Joannides ran the Psychological Warfare Branch directing "
            "the DRE. Both operated within the same anti-Castro operational infrastructure."
        ),
        "year_start": 1962,
        "year_end": 1964,
        "sources": [2104, 2110],
    },
    # ---- Anna Paulina Luna ----
    {
        "source": "Anna Paulina Luna",
        "target": "House Task Force on Declassification of Federal Secrets",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Appointed by Speaker Mike Johnson in February 2025 to chair the House Task Force "
            "on Declassification of Federal Secrets."
        ),
        "year_start": 2025,
        "sources": [2105],
    },
    {
        "source": "Anna Paulina Luna",
        "target": "JFK Files Release (2025)",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "As chair of the House Declassification Task Force, oversaw congressional review "
            "of the JFK files release. Initiated a lawsuit seeking additional assassination "
            "films from NBC and WBAP-TV. Received a report from Russian Ambassador Darchiev "
            "containing Russia's purported JFK findings."
        ),
        "year_start": 2025,
        "sources": [2105],
    },
    {
        "source": "Anna Paulina Luna",
        "target": "Donald Trump",
        "type": "ally_of",
        "tier": "credible",
        "desc": (
            "Republican aligned with the Trump administration. Her appointment to chair the "
            "House Declassification Task Force was a direct response to Trump's Executive "
            "Order 14176."
        ),
        "year_start": 2025,
        "sources": [2105],
    },
    # ---- House Task Force ----
    {
        "source": "House Task Force on Declassification of Federal Secrets",
        "target": "Executive Order 14176",
        "type": "resulted_from",
        "tier": "documented",
        "desc": (
            "Established in February 2025 by Speaker Johnson in direct response to Trump's "
            "EO 14176 ordering declassification of assassination records."
        ),
        "year_start": 2025,
        "sources": [2105, 2103],
    },
    {
        "source": "House Task Force on Declassification of Federal Secrets",
        "target": "CIA",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Task force oversight included review of CIA's handling of assassination records "
            "and the agency's prior appeals to withhold documents on national security grounds."
        ),
        "year_start": 2025,
        "sources": [2105],
    },
    {
        "source": "House Task Force on Declassification of Federal Secrets",
        "target": "JFK Files Release (2025)",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Congressional task force provided oversight of the JFK files release process. "
            "Jefferson Morley testified at its inaugural hearing on JFK records."
        ),
        "year_start": 2025,
        "sources": [2105],
    },
    # ---- Directorio Revolucionario Estudiantil ----
    {
        "source": "Directorio Revolucionario Estudiantil",
        "target": "CIA",
        "type": "funded_by",
        "tier": "documented",
        "desc": (
            "CIA financed the DRE at $25,000 per month under the AMSPEL program, directed by "
            "CIA officer George Joannides from the JMWAVE Psychological Warfare Branch."
        ),
        "year_start": 1962,
        "year_end": 1966,
        "sources": [2109, 2104],
    },
    {
        "source": "Directorio Revolucionario Estudiantil",
        "target": "Lee Harvey Oswald",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "DRE members had direct contact with Oswald in New Orleans in August 1963. "
            "Member Carlos Bringuier confronted Oswald distributing pro-Castro leaflets, "
            "leading to Oswald's arrest and a radio debate. After the assassination, the DRE "
            "launched a campaign linking Oswald to Cuba."
        ),
        "year_start": 1963,
        "sources": [2109, 2115],
    },
    {
        "source": "Directorio Revolucionario Estudiantil",
        "target": "JFK Assassination",
        "type": "involved_in",
        "tier": "credible",
        "desc": (
            "CIA-funded group that monitored Oswald three months before the assassination, "
            "then immediately launched a campaign blaming Cuba. The CIA's concealment of its "
            "DRE directorship from all subsequent investigations suggests the DRE-Oswald "
            "contact was operationally significant."
        ),
        "year_start": 1963,
        "sources": [2109, 2104],
    },
    {
        "source": "ARRB",
        "target": "JFK Files Release (2025)",
        "type": "preceded",
        "tier": "documented",
        "desc": (
            "The ARRB's declassification work (1994-1998) was the predecessor to the 2025 "
            "release. The 2025 release of 94,643 pages was the largest single release since "
            "the ARRB concluded its mandate."
        ),
        "year_start": 1998,
        "year_end": 2025,
        "sources": [2114, 2100],
    },
]

# ============================================================
# ENTITY → SOURCE mappings
# ============================================================

ENTITY_SOURCES = {
    "Executive Order 14176": [2100, 2103, 2106],
    "JFK Files Release (2025)": [2100, 2101, 2103, 2106],
    "George Joannides": [2104, 2109, 2111],
    "Anna Paulina Luna": [2105],
    "House Task Force on Declassification of Federal Secrets": [2105, 2103],
    "Directorio Revolucionario Estudiantil": [2109, 2104],
}

# ============================================================
# ENTITY UPDATES (11 updates to existing entities)
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "JFK Assassination",
        "description_append": (
            "2025 update: On January 23, 2025, President Trump signed Executive Order 14176 "
            "ordering full declassification of remaining JFK assassination records. Between "
            "March 18 and April 3, 2025, the National Archives released approximately 83,621 "
            "pages across 2,569 PDF files without redactions, with an additional 11,022 pages "
            "on January 30, 2026 — totaling approximately 94,643 pages across 2,709 PDFs. "
            "The released documents confirmed CIA officer George Joannides directed the DRE "
            "Cuban exile group that monitored Oswald in New Orleans months before the "
            "assassination, and that Joannides subsequently obstructed the HSCA investigation "
            "while serving as CIA liaison. The House Task Force on Declassification of Federal "
            "Secrets, chaired by Rep. Anna Paulina Luna, was established in February 2025 to "
            "oversee the implementation."
        ),
        "sources": [2100, 2103],
    },
    {
        "name": "Warren Commission",
        "description_append": (
            "2025 update: Documents released under Executive Order 14176 (March 2025) further "
            "documented the extent to which the CIA withheld assassination-related information "
            "from the Warren Commission, including the existence and role of George Joannides "
            "as CIA case officer directing the DRE — a Cuban exile group that had direct "
            "contact with Lee Harvey Oswald in New Orleans in August 1963. The CIA had denied "
            "the existence of this handler to the Commission."
        ),
        "sources": [2100, 2104, 2113],
    },
    {
        "name": "HSCA",
        "description_append": (
            "2025 update: Documents released in March 2025 under Executive Order 14176 "
            "confirmed that CIA officer George Joannides, who served as the agency's liaison "
            "to the HSCA, had personally directed and financed the DRE during the period of "
            "its contact with Oswald — a fact he concealed from investigators. The CIA had "
            "previously denied this connection when queried about the DRE's handler 'Howard.' "
            "The 2025 releases validated the committee's 1979 conspiracy finding and "
            "documented the full scope of CIA obstruction of its investigation."
        ),
        "sources": [2100, 2104, 2111],
    },
    {
        "name": "Lee Harvey Oswald",
        "description_append": (
            "2025 update: Documents released under Executive Order 14176 (March 2025) revealed "
            "the extent of CIA surveillance of Oswald prior to the assassination, including "
            "monitoring through the CIA-directed DRE Cuban exile group in New Orleans. The "
            "releases confirmed that CIA officer George Joannides directed the DRE, which had "
            "confrontational contact with Oswald in August 1963, and that the CIA concealed "
            "this operational connection from the Warren Commission, HSCA, and ARRB."
        ),
        "sources": [2100, 2104, 2115],
    },
    {
        "name": "David Atlee Phillips",
        "description_append": (
            "2025 update: The 2025 declassified files provided additional context for Phillips' "
            "role at JMWAVE, the CIA's Miami station, where George Joannides served under the "
            "Psychological Warfare Branch directing the DRE. Phillips oversaw anti-Castro "
            "propaganda operations from the same station during the same period. Both operated "
            "within the CIA's anti-Castro infrastructure that intersected with Oswald's "
            "activities in New Orleans."
        ),
        "sources": [2104, 2110],
    },
    {
        "name": "Allen Dulles",
        "description_append": (
            "2025 update: Documents released under Executive Order 14176 (March 2025) further "
            "documented the scope of CIA concealment from the Warren Commission during Dulles' "
            "tenure as a member. The releases confirmed the agency withheld operational "
            "information about the DRE and Oswald surveillance from the commission — "
            "underscoring the conflict of interest in having a former CIA director investigate "
            "the agency's potential complicity."
        ),
        "sources": [2100, 2112],
    },
    {
        "name": "RFK Assassination",
        "description_append": (
            "2025 update: In April through June 2025, pursuant to Executive Order 14176, "
            "assassination records related to Robert F. Kennedy were declassified and released "
            "by the National Archives. The release included autopsy photographs showing "
            "Kennedy's gunshot wounds. Kerry Kennedy (RFK's daughter) opposed the release, "
            "calling the photos 'graphic, explicit photos of his mangled body.' Robert F. "
            "Kennedy Jr., then serving as HHS Secretary in the Trump administration, defended "
            "the release while describing the decision as 'agonizing.'"
        ),
        "sources": [2103, 2107],
    },
    {
        "name": "MLK Assassination",
        "description_append": (
            "2025 update: In July 2025, pursuant to Executive Order 14176 signed January 23, "
            "2025, assassination records related to Martin Luther King Jr. were declassified "
            "and released by the National Archives. Many of the FBI surveillance records had "
            "been scheduled to remain classified until 2027."
        ),
        "sources": [2103, 2108],
    },
    {
        "name": "Sirhan Sirhan",
        "description_append": (
            "2025-2026 update: As of 2026, Sirhan Sirhan remains incarcerated at R.J. Donovan "
            "Correctional Facility in San Diego. His seventeenth parole denial was issued "
            "March 1, 2023. The 2025 release of RFK assassination files under Executive Order "
            "14176 included autopsy photographs but did not resolve the longstanding questions "
            "about whether additional shooters were present."
        ),
        "sources": [2116, 2107],
    },
    {
        "name": "ARRB",
        "description_append": (
            "2025 update: The 2025 release of JFK assassination records under Executive Order "
            "14176 represented the largest single release since the ARRB concluded its mandate "
            "in 1998. Between March 2025 and January 2026, approximately 94,643 pages across "
            "2,709 PDFs were released without redactions. The House Task Force on "
            "Declassification of Federal Secrets, chaired by Rep. Anna Paulina Luna, was "
            "established in February 2025 as a de facto successor to the ARRB's oversight role."
        ),
        "sources": [2100, 2114],
    },
    {
        "name": "Jim Garrison",
        "description_append": (
            "2025 update: The 2025 declassification of JFK files under Executive Order 14176 "
            "provided further vindication of Garrison's core thesis of CIA involvement. "
            "Released documents confirmed that CIA officer George Joannides directed the DRE "
            "group connected to Oswald and subsequently obstructed the HSCA investigation — "
            "demonstrating the pattern of intelligence community concealment Garrison alleged "
            "during his 1967-69 prosecution of Clay Shaw."
        ),
        "sources": [2100, 2104, 2117],
    },
]

# ============================================================
# GEO_COORDS — for new entities only
# ============================================================

GEO_COORDS = {
    "Executive Order 14176": (38.8977, -77.0365, "documented", "White House, Washington DC"),
    "JFK Files Release (2025)": (38.8937, -77.0230, "documented", "National Archives, Washington DC"),
    "George Joannides": (25.7617, -80.1918, "credible", "JMWAVE station area, Miami FL"),
    "Anna Paulina Luna": (38.8899, -77.0091, "credible", "US Capitol, Washington DC"),
    "House Task Force on Declassification of Federal Secrets": (
        38.8899, -77.0091, "credible", "US Capitol, Washington DC"
    ),
    "Directorio Revolucionario Estudiantil": (
        25.7617, -80.1918, "credible", "Miami, Florida - DRE base of operations"
    ),
}

# ============================================================
# PHOTO_CANDIDATES — for new persons/orgs
# ============================================================

PHOTO_CANDIDATES = {
    "Anna Paulina Luna": (
        "https://upload.wikimedia.org/wikipedia/commons/6/6b/"
        "Anna_Paulina_Luna_118th_Congress_portrait_%28cropped%29.jpg"
    ),
}
