"""
PURSUE UAP Disclosure (2026) — Expansion layer for Intel Console.

The 2026 US government UAP records release via three lanes: the executive-branch
PURSUE program (Department of War, war.gov/UFO), the statutory NARA RG-615
collection (NDAA FY2024 §§1841–1843), and the forced NSA FOIA release. Covers
the three PURSUE tranches (May–June 2026), the Capitol UAP press conference
(June 9, 2026), key figures, and primary-source publications.

Primary substrate: verified dossier (25 claims, 3-vote adversarial verification,
0 refuted) at ~/fotw-production/season-001/research/uap-disclosure-2026/DOSSIER.md.
war.gov bot-blocks non-browser clients; verification rested on independent
reproductions (GlobalSecurity, CBS, Newsweek, NBC) plus corroborating journalism.

Source-ID range: 2900–2999.
Branch: consciousness.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence

EXISTING ENTITIES referenced by exact name (NOT duplicated):
  AARO, AATIP, Americans for Safe Aerospace, Anna Paulina Luna, Buzz Aldrin,
  Christopher Mellon, CIA, Chuck Schumer, David Fravor, David Grusch, DOE,
  Donald Trump, Executive Order 14176, FBI, Galileo Project, Gordon Cooper,
  Grusch Congressional Hearing, House Task Force on Declassification of Federal Secrets,
  J. Edgar Hoover, Jeremy Corbell, Jon Kosloski, Karl Nell, Kash Patel,
  Luis Elizondo, Mike Rounds, Neil Armstrong, NSA,
  Office of the Director of National Intelligence, Pete Hegseth,
  Project Blue Book, Roswell Incident, Ross Coulthart, Ryan Graves,
  Sol Foundation, The Pentagon, Tim Burchett, Tulsi Gabbard,
  UAP Disclosure Act, UAP Task Force
"""

# ============================================================
# SOURCES — IDs 2900–2999
# ============================================================

SOURCES = [
    # ---- Government / primary ----
    {
        "id": 2900,
        "title": "PURSUE — war.gov/UFO portal (war.gov bot-blocks; verified via GlobalSecurity/CBS reproduction)",
        "url": "https://www.war.gov/UFO/",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 2901,
        "title": "Department of War — PURSUE Release 01 press release, Article 4480582 (war.gov bot-blocks; verified via reproductions)",
        "url": "https://www.war.gov/News/Releases/Release/Article/4480582",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 2902,
        "title": "Department of War — PURSUE Release 02 press release, Article 4499305 (war.gov bot-blocks; verified via reproductions)",
        "url": "https://www.war.gov/News/Releases/Release/Article/4499305",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 2903,
        "title": "Department of War — PURSUE Release 03 press release, Article 4515408 (war.gov bot-blocks; verified via reproductions)",
        "url": "https://www.war.gov/News/Releases/Release/Article/4515408",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 2904,
        "title": "National Archives — 'National Archives Releases UAP Records' press release nr25-07, April 24, 2025",
        "url": "https://www.archives.gov/press/press-releases/2025/nr25-07",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 2905,
        "title": "National Archives — Unidentified Anomalous Phenomena topic page",
        "url": "https://www.archives.gov/research/topics/uaps",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 2906,
        "title": "National Archives — UAP Records Collection, Record Group 615 research guide",
        "url": "https://www.archives.gov/research/topics/uaps/rg-615",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 2907,
        "title": "Public Law 118-31, FY2024 NDAA — §§1841–1843 (UAP Disclosure Act surviving provisions)",
        "url": "https://www.congress.gov/bill/118th-congress/house-bill/2670",
        "source_type": "congressional",
        "year": 2023,
    },
    {
        "id": 2908,
        "title": "Federal Register Presidential Documents search — zero UAP executive orders on record",
        "url": "https://www.federalregister.gov/presidential-documents",
        "source_type": "government",
        "year": 2026,
    },
    # ---- Quality journalism ----
    {
        "id": 2909,
        "title": "CBS News — 'Pentagon releases 3rd batch of declassified UFO files, including videos and audio recordings'",
        "url": "https://www.cbsnews.com/news/ufo-files-pentagon-3rd-release-documents-videos/",
        "source_type": "journalism",
        "author": "CBS News",
        "year": 2026,
    },
    {
        "id": 2910,
        "title": "PRNewswire — bipartisan congressional UAP press conference announcement, June 9, 2026",
        "url": "https://www.prnewswire.com/news-releases/bipartisan-congressional-uap-press-conference-302784861.html",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 2911,
        "title": "DefenseScoop — 'Trump directs Pentagon to begin releasing UFO files' (Feb 20, 2026)",
        "url": "https://defensescoop.com/2026/02/20/trump-pentagon-ufo-uap-disclosure-hegseth/",
        "source_type": "journalism",
        "author": "DefenseScoop",
        "year": 2026,
    },
    {
        "id": 2912,
        "title": "DefenseScoop — first PURSUE file drop coverage (May 2026)",
        "url": "https://defensescoop.com/2026/05/14/uap-trump-first-pursue-ufo-file-drop/",
        "source_type": "journalism",
        "author": "DefenseScoop",
        "year": 2026,
    },
    {
        "id": 2913,
        "title": "Newsweek — Pentagon PURSUE UAP file release coverage (2026)",
        "url": "https://www.newsweek.com/pentagon-ufo-files-pursue-release-2026",
        "source_type": "journalism",
        "author": "Newsweek",
        "year": 2026,
    },
    {
        "id": 2914,
        "title": "NBC News — Pentagon UAP disclosure coverage (2026)",
        "url": "https://www.nbcnews.com/news/us-news/pentagon-releases-ufo-uap-files-2026",
        "source_type": "journalism",
        "author": "NBC News",
        "year": 2026,
    },
    {
        "id": 2915,
        "title": "Washington Times — PURSUE UAP release coverage (2026)",
        "url": "https://www.washingtontimes.com/news/2026/jun/12/pentagon-releases-third-batch-ufo-files/",
        "source_type": "journalism",
        "author": "Washington Times",
        "year": 2026,
    },
    {
        "id": 2916,
        "title": "Stars & Stripes — Pentagon UAP disclosure coverage (2026)",
        "url": "https://www.stripes.com/theaters/us/2026-06-12/pentagon-ufo-uap-pursue-release/",
        "source_type": "journalism",
        "author": "Stars & Stripes",
        "year": 2026,
    },
    {
        "id": 2917,
        "title": "Fox/LiveNOW — Gordon Cooper-Cronkite audio detail from Release 3 (2026)",
        "url": "https://www.fox5dc.com/news/pentagon-ufo-files-gordon-cooper-cronkite-audio",
        "source_type": "journalism",
        "author": "Fox/LiveNOW wire",
        "year": 2026,
    },
    {
        "id": 2918,
        "title": "GlobalSecurity.org — reproductions of Department of War PURSUE press releases",
        "url": "https://www.globalsecurity.org/military/library/news/2026/05/mil-260508-dod01.htm",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2919,
        "title": "New York Times — 'Glowing Auras and Black Money: The Pentagon's Mysterious U.F.O. Program' (Kean, Blumenthal, Cooper)",
        "url": "https://www.nytimes.com/2017/12/16/us/politics/pentagon-program-ufo-harry-reid.html",
        "source_type": "journalism",
        "author": "Leslie Kean, Ralph Blumenthal, Helene Cooper",
        "year": 2017,
    },
    {
        "id": 2920,
        "title": "The Debrief — 'Intelligence Officials Say U.S. Has Retrieved Craft of Non-Human Origin' (Kean, Blumenthal)",
        "url": "https://thedebrief.org/intelligence-officials-say-u-s-has-retrieved-craft-of-non-human-origin/",
        "source_type": "journalism",
        "author": "Leslie Kean, Ralph Blumenthal",
        "year": 2023,
    },
    {
        "id": 2921,
        "title": "NewsNation — Pentagon third UAP file release coverage (June 2026)",
        "url": "https://www.newsnationnow.com/space/ufo/pentagon-third-ufo-file-release-2026/",
        "source_type": "journalism",
        "author": "NewsNation",
        "year": 2026,
    },
    {
        "id": 2922,
        "title": "Scientific American — Sean Kirkpatrick critical commentary on UAP claims (2024)",
        "url": "https://www.scientificamerican.com/article/the-ufo-whistleblower-and-the-scientific-method/",
        "source_type": "journalism",
        "author": "Sean Kirkpatrick",
        "year": 2024,
    },
    # ---- Reference / encyclopedic ----
    {
        "id": 2923,
        "title": "Wikipedia — NASA (National Aeronautics and Space Administration)",
        "url": "https://en.wikipedia.org/wiki/NASA",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2924,
        "title": "Wikipedia — Jared Isaacman (entrepreneur, NASA Administrator)",
        "url": "https://en.wikipedia.org/wiki/Jared_Isaacman",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2925,
        "title": "Wikipedia — Eric Burlison (U.S. Representative, Missouri 7th district)",
        "url": "https://en.wikipedia.org/wiki/Eric_Burlison",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2926,
        "title": "Wikipedia — Leslie Kean (investigative journalist)",
        "url": "https://en.wikipedia.org/wiki/Leslie_Kean",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2927,
        "title": "Wikipedia — United States Department of War (historical context and 2025 rename)",
        "url": "https://en.wikipedia.org/wiki/United_States_Department_of_War",
        "source_type": "other",
        "year": 2026,
    },
    # ---- Archives / books / FOIA ----
    {
        "id": 2928,
        "title": "FBI Vault — UFO collection (includes case file 62-HQ-83894, 1947–1968)",
        "url": "https://vault.fbi.gov/UFO",
        "source_type": "foia",
        "year": 2026,
    },
    {
        "id": 2929,
        "title": "Gordon Cooper — 'Leap of Faith: An Astronaut's Journey into the Unknown' (HarperCollins, 2000)",
        "url": "https://en.wikipedia.org/wiki/Leap_of_Faith:_An_Astronaut%27s_Journey_into_the_Unknown",
        "source_type": "book",
        "author": "Gordon Cooper with Bruce Henderson",
        "year": 2000,
    },
    {
        "id": 2930,
        "title": "Gordon Cooper — letter to Ambassador Griffith, UN Special Political Committee, November 9, 1978",
        "url": "https://documents.theblackvault.com/documents/ufos/cooperletter.pdf",
        "source_type": "archive",
        "author": "Gordon Cooper",
        "year": 1978,
    },
    {
        "id": 2931,
        "title": "Leslie Kean — 'UFOs: Generals, Pilots, and Government Officials Go on the Record' (Crown, 2010)",
        "url": "https://en.wikipedia.org/wiki/UFOs:_Generals,_Pilots,_and_Government_Officials_Go_on_the_Record",
        "source_type": "book",
        "author": "Leslie Kean",
        "year": 2010,
    },
    {
        "id": 2932,
        "title": "NSA FOIA release — 300+ pages TOP SECRET UMBRA UAP-related material (May 2026, per reporting)",
        "url": "https://www.cbsnews.com/news/nsa-ufo-files-foia-release-2026/",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 2933,
        "title": "Metabunk forum — provenance analysis of PURSUE Release 1 (PR-19 = Corbell 2023 footage; index errors PR-28/PR-29)",
        "url": "https://www.metabunk.org/threads/trump-ufo-uap-disclosure.13268/",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2934,
        "title": "DefenseScoop — Hegseth at 'Arsenal of Freedom' tour, commits to PURSUE compliance (Feb 23, 2026)",
        "url": "https://defensescoop.com/2026/02/23/hegseth-arsenal-freedom-uap-ufo-disclosure/",
        "source_type": "journalism",
        "author": "DefenseScoop",
        "year": 2026,
    },
    {
        "id": 2935,
        "title": "Liberation Times — UAP Disclosure Act legislative stall analysis (Dec 2025)",
        "url": "https://www.liberationtimes.com/home/uap-disclosure-act-stalled-fy2026",
        "source_type": "journalism",
        "author": "Liberation Times",
        "year": 2025,
    },
    {
        "id": 2936,
        "title": "Disclosure Day (2026 film) — coverage of Spielberg premiere coinciding with PURSUE Release 3",
        "url": "https://www.cbsnews.com/news/spielberg-disclosure-day-premiere-ufo-files/",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 2937,
        "title": "Wikipedia — United States UFO files (PURSUE program overview and reception)",
        "url": "https://en.wikipedia.org/wiki/United_States_UFO_files",
        "source_type": "other",
        "year": 2026,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    {
        "name": "PURSUE",
        "entity_type": "program",
        "description": (
            "Presidential Unsealing and Reporting System for UAP Encounters, established by a "
            "Trump Truth Social directive dated February 19, 2026, directing federal agencies to "
            "declassify UAP/UFO/extraterrestrial records. Hosted at war.gov/UFO by the Department "
            "of War with ODNI support. Interagency partners: White House, DOE, AARO (coordination "
            "role, not administrator despite press shorthand), NASA, FBI, and additional IC "
            "components. NARA is not a listed partner. Three tranches released: May 8, 2026 "
            "(1.2 GB docs, 1.3 GB video), May 22, 2026 (70.1 MB docs, 5.6 GB video), June 12, "
            "2026 (826 MB docs, 4.6 GB video). The founding authority is a social media directive, "
            "not a numbered executive order; the Federal Register returns zero UAP presidential "
            "documents. PURSUE archives only unresolved cases and runs parallel to statutory "
            "reporting under NDAA FY2024. Self-reported traffic: 'over 1.7 billion hits' by the "
            "third release, an unaudited administration figure. 'Artistic interpretations' in the "
            "releases are FBI-produced digital renderings from witness narratives, not captured "
            "footage. Provenance controversies: video PR-19 matched footage Jeremy Corbell released "
            "publicly in 2023; index errors (PR-28, PR-29) undermined quality-control claims. "
            "Reception: Christopher Mellon warned 'data alone is not disclosure'; former AARO "
            "director Sean Kirkpatrick said files without analysis 'will fuel speculation'; Mick "
            "West dismissed them as 'more dots, more parallax.'"
        ),
        "aliases": "Presidential Unsealing and Reporting System for UAP Encounters, war.gov/UFO, Trump UFO disclosure program",
        "metadata": {
            "status": "active",
            "location": "war.gov/UFO (The Pentagon, Arlington VA)",
        },
    },
    {
        "name": "Department of War",
        "entity_type": "agency",
        "description": (
            "The United States Department of War, the renamed Department of Defense. In September "
            "2025 (announced August 25), President Trump signed an executive order directing use of the historical "
            "'Department of War' title in official correspondence, with war.gov replacing "
            "defense.gov as the primary domain. The change is a styling directive, not a statutory "
            "rename, which would require Congressional action. Secretary of Defense Pete Hegseth "
            "adopted the title 'Secretary of War.' The department administers the PURSUE UAP "
            "disclosure program (2026) and houses AARO (All-domain Anomaly Resolution Office). "
            "Headquartered at The Pentagon, Arlington, Virginia."
        ),
        "aliases": "DOW, Department of Defense, DoD, United States Department of War",
        "metadata": {
            "status": "active",
            "location": "The Pentagon, Arlington VA",
        },
    },
    {
        "name": "NASA",
        "entity_type": "agency",
        "description": (
            "National Aeronautics and Space Administration, the United States federal agency "
            "responsible for civil space exploration, aeronautics research, and space science. "
            "Established July 29, 1958 by the National Aeronautics and Space Act. Headquartered "
            "in Washington, D.C. Named as an interagency partner in the PURSUE UAP disclosure "
            "program (2026). Apollo-era mission material — including audio debriefs, photographs, "
            "and astronaut accounts of anomalous observations — featured prominently across all "
            "three PURSUE tranches. Administrator Jared Isaacman issued a supporting statement "
            "for the first release: 'We will remain candid about what we know to be true, what we "
            "have yet to understand.' NASA independently commissioned a UAP study panel in 2022 "
            "whose report (September 2023) recommended NASA engage transparently with the topic."
        ),
        "aliases": "National Aeronautics and Space Administration",
        "metadata": {
            "status": "active",
            "location": "Washington, D.C.",
        },
    },
    {
        "name": "PURSUE Release 1 (May 8, 2026)",
        "entity_type": "event",
        "description": (
            "First tranche of declassified UAP files under the PURSUE program, published May 8, "
            "2026, simultaneously launching the war.gov/UFO portal. Contained approximately 160+ "
            "files (1.2 GB documents, 1.3 GB video) spanning 1944 to near-present. Contents "
            "included U.S. military UAP imagery, NASA Apollo-era lunar photography (Apollo 17 "
            "triangular-formation lights; Buzz Aldrin Apollo 11 'little flashes' account), 'orbs "
            "launching other orbs' law-enforcement video, and FBI case file 62-HQ-83894 (UFO "
            "investigations June 1947 to July 1968, re-released with fewer redactions). Outside "
            "researchers counted at least 100 files with remaining redactions. Official statements "
            "from Secretary of War Hegseth, DNI Gabbard, FBI Director Patel, and NASA Administrator "
            "Isaacman accompanied the release."
        ),
        "aliases": "PURSUE Release 01, PURSUE first tranche",
        "metadata": {"location": "war.gov/UFO"},
    },
    {
        "name": "PURSUE Release 2 (May 22, 2026)",
        "entity_type": "event",
        "description": (
            "Second tranche of PURSUE declassified UAP files, published May 22, 2026 by the "
            "Department of War. Contained 222 documents (70.1 MB), approximately 51 audio "
            "recordings, and over 40 videos (5.6 GB) requested by lawmakers. Notable contents: "
            "a video reportedly showing a UFO being shot down; four UFOs in formation near Iran "
            "(2022) captured on U.S. military infrared; Apollo 12 'green fireballs/orbs' material; "
            "and seven NASA mission audio recordings including the Apollo 12 medical debrief "
            "(November 1969, unexplained light phenomena), Mercury-Atlas 7 (May 24, 1962, "
            "Carpenter's 'snowflakes'), Mercury-Atlas 8 ('little white objects'), and Sandia Base "
            "records from 1948 to 1950 documenting 209 sightings in late-1940s New Mexico. The "
            "Department of War self-reported 'over 1 billion hits worldwide' in the two weeks "
            "following the site launch."
        ),
        "aliases": "PURSUE Release 02, PURSUE second tranche",
        "metadata": {"location": "war.gov/UFO"},
    },
    {
        "name": "PURSUE Release 3 (June 12, 2026)",
        "entity_type": "event",
        "description": (
            "Third PURSUE tranche, published June 12, 2026: 53 documents, 10 images/renderings, "
            "6 videos, 3 NASA audio recordings (826 MB docs, 4.6 GB video), sourced from CIA, FBI, "
            "NASA, and DOD. Ten featured items include CIA-UAP-017 (July 2008 Harare International "
            "Airport hovering object, routed to White House Situation Room), DOW-UAP-D084 (1949 "
            "Army 'Evaluation Study of the Phenomenon'), FBI FD-302/FD-1057 witness interviews "
            "(2022 to 2026), FBI orb videos (PR003/PR004), and ICA-UAP-D001 (AARO low-confidence "
            "snow-backscatter assessment of a 2022 Colorado Springs sighting). Also included: the "
            "Apollo 16 mission debrief (2+ hours) and a Gordon Cooper-Walter Cronkite audio excerpt "
            "labeled November 1962. FBI-UAP-D003 defined as an 'artistic interpretation' — an "
            "official digital rendering derived from witness narrative. The same day saw the "
            "premiere of Steven Spielberg's film 'Disclosure Day,' about a global extraterrestrial "
            "revelation, flagged by coverage as 'perhaps coincidentally' timed."
        ),
        "aliases": "PURSUE Release 03, PURSUE third tranche",
        "metadata": {"location": "war.gov/UFO"},
    },
    {
        "name": "UAP Records Collection (NARA RG-615)",
        "entity_type": "program",
        "description": (
            "The statutory lane for UAP records disclosure, distinct from the executive-branch "
            "PURSUE program. Established under Sections 1841 to 1843 of the FY2024 NDAA (Public "
            "Law 118-31) — the surviving Schumer-Rounds UAP Disclosure Act provisions. Records "
            "from ODNI, the Office of the Secretary of Defense, the FAA, and the Nuclear Regulatory "
            "Commission were transferred to NARA and accessioned into Record Group 615. Announced "
            "April 24, 2025 (press release nr25-07). NARA operates on a rolling-basis release "
            "model through the National Archives Catalog, predating the Pentagon's adoption of "
            "similar language by a full year. As of its April 2025 review date, the NARA UAP topic "
            "page contains no mention of PURSUE, any executive order, or named tranches, confirming "
            "the two mechanisms are distinct. The full UAPDA Review Board and eminent-domain "
            "provisions were stripped from the enacted version."
        ),
        "aliases": "NARA UAP Records Collection, Record Group 615, Unidentified Anomalous Phenomena Records Collection",
        "metadata": {
            "status": "active",
            "location": "National Archives, College Park MD",
        },
    },
    {
        "name": "NSA UAP FOIA Release (May 2026)",
        "entity_type": "event",
        "description": (
            "On or around May 18, 2026, the National Security Agency released over 300 pages of "
            "TOP SECRET UMBRA UAP-related material through Freedom of Information Act processes. "
            "This constitutes what the UAP disclosure dossier calls 'the forced lane' — material "
            "pried out against the government's preference, as distinguished from the executive "
            "PURSUE program and the statutory NARA collection. The release was not volunteered as "
            "part of either official program. Note: this event was documented in the research "
            "dossier but was not among the 25 claims subjected to three-vote adversarial "
            "verification; its details rely on journalism reporting rather than primary government "
            "confirmation."
        ),
        "aliases": "NSA FOIA UAP release",
        "metadata": {"location": "Fort Meade, MD"},
    },
    {
        "name": "FBI File 62-HQ-83894",
        "entity_type": "publication",
        "description": (
            "FBI case file covering UFO investigations from June 1947 through July 1968. "
            "Designated 62-HQ-83894 in FBI filing. Originally released through the FBI Vault "
            "(FOIA reading room) with significant redactions. Re-released in PURSUE Release 1 "
            "(May 8, 2026) with fewer redactions than prior versions. The file spans the Roswell "
            "era through the close of Project Blue Book and documents the FBI's parallel UFO "
            "investigative track. The Department of War claimed remaining redactions in the "
            "re-release cover only witness identities and facility locations, not UAP substance."
        ),
        "aliases": "FBI UFO file 62-HQ-83894, FBI UFO investigations file",
        "metadata": {
            "location": "FBI Headquarters, Washington D.C.",
        },
    },
    {
        "name": "Hoover-Barnes Letter (1949)",
        "entity_type": "publication",
        "description": (
            "FBI document designated FBI-UAP-D011, a January 31, 1949 letter between FBI Director "
            "J. Edgar Hoover and Reverend Charles Barnes describing beams converging in the "
            "Cascade Mountains of Washington state. Released as part of PURSUE Release 3 (June 12, "
            "2026). The letter documents an early Cold War-era report of anomalous aerial "
            "phenomena in the Pacific Northwest — the same geographic region as the 1947 Kenneth "
            "Arnold sighting that coined the term 'flying saucer.' One of ten featured items in "
            "the Release 3 carousel."
        ),
        "aliases": "FBI-UAP-D011, Hoover-Barnes Cascade letter",
        "metadata": {
            "location": "Cascade Mountains, Washington",
        },
    },
    {
        "name": "Capitol UAP Press Conference (June 9, 2026)",
        "entity_type": "event",
        "description": (
            "Bipartisan congressional and whistleblower press conference held Tuesday, June 9, "
            "2026, at 1:00 PM on the U.S. Capitol steps. Hosted by investigative journalist "
            "Leslie Kean and documentary filmmaker James Fox. Announced participants: Representatives "
            "Eric Burlison, Jared Moskowitz, Tim Burchett, and Anna Paulina Luna, plus "
            "whistleblower David Grusch, slated to discuss 'specific UAP and non-human "
            "intelligence-related evidence he encountered in deeply classified channels.' The "
            "event was timed between PURSUE Release 2 (May 22) and Release 3 (June 12), "
            "connecting congressional UAP advocacy to the executive disclosure effort."
        ),
        "aliases": "June 9 2026 Capitol UAP presser",
        "metadata": {
            "location": "U.S. Capitol steps, Washington D.C.",
        },
    },
    {
        "name": "Leslie Kean",
        "entity_type": "person",
        "description": (
            "American investigative journalist and author, load-bearing figure in the modern UAP "
            "disclosure arc. Co-authored the December 16, 2017 New York Times front-page article "
            "'Glowing Auras and Black Money' (with Ralph Blumenthal and Helene Cooper) that "
            "revealed AATIP and published the first authenticated Navy UAP videos, triggering the "
            "post-2017 congressional disclosure movement. Co-authored the June 2023 Debrief story "
            "breaking David Grusch's whistleblower allegations of a crash-retrieval program. "
            "Author of 'UFOs: Generals, Pilots, and Government Officials Go on the Record' "
            "(Crown, 2010). Co-hosted the June 9, 2026 Capitol UAP press conference alongside "
            "filmmaker James Fox."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "American",
            "role": "investigative journalist",
        },
    },
    {
        "name": "Eric Burlison",
        "entity_type": "person",
        "description": (
            "U.S. Representative for Missouri's 7th congressional district (Republican). "
            "Supportive-but-wary congressional voice on UAP disclosure. On the PURSUE releases, "
            "Burlison framed Congress's role as preventing career intelligence officials from "
            "obstructing the directive 'to prevent selective disclosure or another dead end.' "
            "Participated in the June 9, 2026 Capitol UAP press conference alongside David Grusch "
            "and fellow Representatives Moskowitz, Burchett, and Luna."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "American",
            "role": "U.S. Representative (R-MO-7)",
        },
    },
    {
        "name": "Jared Isaacman",
        "entity_type": "person",
        "description": (
            "American entrepreneur and astronaut, Administrator of NASA (confirmed early 2025). "
            "Founder and CEO of Shift4 Payments. Commanded the Inspiration4 mission (September "
            "2021), the first all-civilian orbital spaceflight, and the Polaris Dawn mission "
            "(2024). As NASA Administrator, issued a supporting statement for the first PURSUE "
            "release: 'We will remain candid about what we know to be true, what we have yet to "
            "understand.' NASA material — Apollo mission debriefs, photographs, and astronaut "
            "audio recordings — featured prominently across all three PURSUE tranches."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "American",
            "role": "NASA Administrator (2025-present)",
        },
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ---- PURSUE core structure ----
    {
        "source": "Donald Trump",
        "target": "PURSUE",
        "type": "ordered",
        "tier": "documented",
        "desc": (
            "Trump's Truth Social directive dated February 19, 2026 directed the Secretary of "
            "War and other agencies to begin releasing UAP/UFO/extraterrestrial files. This "
            "social media post is the founding authority for PURSUE; no numbered executive order "
            "exists — the Federal Register returns zero UAP presidential documents."
        ),
        "year_start": 2026,
        "sources": [2900, 2901, 2908, 2911],
    },
    {
        "source": "Department of War",
        "target": "PURSUE",
        "type": "operated",
        "tier": "documented",
        "desc": (
            "The Department of War (renamed DOD) administers the PURSUE program, hosting records "
            "at war.gov/UFO and publishing tranches via official press releases. The war.gov/UFO "
            "page names DOW as the operating authority with ODNI support."
        ),
        "year_start": 2026,
        "sources": [2900, 2901],
    },
    {
        "source": "Office of the Director of National Intelligence",
        "target": "PURSUE",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": (
            "ODNI provides support and coordination for PURSUE. DNI Tulsi Gabbard described it as "
            "'an ongoing joint declassification and release effort,' establishing ODNI's role "
            "alongside the Department of War."
        ),
        "year_start": 2026,
        "sources": [2900, 2901],
    },
    {
        "source": "AARO",
        "target": "PURSUE",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": (
            "AARO provides coordination for PURSUE, preparing files for posting alongside other "
            "agencies. The war.gov/UFO portal cross-links AARO under 'other historical UAP "
            "records' but does NOT name AARO as PURSUE's administrator. The named authority is "
            "DOW plus ODNI; press shorthand that 'AARO administers PURSUE' is not supported by "
            "the program's own page."
        ),
        "year_start": 2026,
        "sources": [2900, 2912],
    },
    {
        "source": "FBI",
        "target": "PURSUE",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "FBI is a named interagency partner in PURSUE. FBI material features prominently: "
            "case file 62-HQ-83894 (re-released in Release 1), FD-302/FD-1057 witness interviews "
            "(Release 3), orb videos, and the 1949 Hoover-Barnes correspondence."
        ),
        "year_start": 2026,
        "sources": [2900, 2901, 2903, 2909],
    },
    {
        "source": "NASA",
        "target": "PURSUE",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "NASA is a named interagency partner in PURSUE. Apollo-era mission material — "
            "debriefs, photographs, astronaut audio recordings — featured across all three "
            "tranches. Administrator Jared Isaacman issued a supporting statement for Release 1."
        ),
        "year_start": 2026,
        "sources": [2900, 2901],
    },
    {
        "source": "DOE",
        "target": "PURSUE",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "The Department of Energy is listed as an interagency partner in PURSUE on the "
            "war.gov/UFO portal page."
        ),
        "year_start": 2026,
        "sources": [2900],
    },
    {
        "source": "CIA",
        "target": "PURSUE",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "CIA contributed material to PURSUE releases. Release 3 featured CIA-UAP-017, a "
            "'never before released' July 2008 CIA report on a hovering object over Harare "
            "International Airport, Zimbabwe, routed to the White House Situation Room."
        ),
        "year_start": 2026,
        "sources": [2903, 2909],
    },
    # ---- Release → PURSUE ----
    {
        "source": "PURSUE Release 1 (May 8, 2026)",
        "target": "PURSUE",
        "type": "resulted_from",
        "tier": "documented",
        "desc": "First tranche of PURSUE, published May 8, 2026. Approximately 160+ files, 1.2 GB documents plus 1.3 GB video.",
        "year_start": 2026,
        "sources": [2901, 2918],
    },
    {
        "source": "PURSUE Release 2 (May 22, 2026)",
        "target": "PURSUE",
        "type": "resulted_from",
        "tier": "documented",
        "desc": "Second tranche of PURSUE, published May 22, 2026. 222 documents (70.1 MB), 51 audio recordings, 40+ videos (5.6 GB).",
        "year_start": 2026,
        "sources": [2902, 2918],
    },
    {
        "source": "PURSUE Release 3 (June 12, 2026)",
        "target": "PURSUE",
        "type": "resulted_from",
        "tier": "documented",
        "desc": "Third tranche of PURSUE, published June 12, 2026. 53 documents, 10 images/renderings, 6 videos, 3 NASA audio (826 MB docs, 4.6 GB video).",
        "year_start": 2026,
        "sources": [2903, 2909],
    },
    # ---- Department of War ----
    {
        "source": "Pete Hegseth",
        "target": "Department of War",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Hegseth serves as Secretary of War (styled from the September 5, 2025 executive order) / "
            "Secretary of Defense. Oversees the Department of War and the PURSUE UAP disclosure "
            "program."
        ),
        "year_start": 2025,
        "sources": [2900, 2927],
    },
    {
        "source": "Department of War",
        "target": "The Pentagon",
        "type": "located_at",
        "tier": "documented",
        "desc": "The Department of War (renamed DOD) is headquartered at The Pentagon, Arlington, Virginia.",
        "sources": [2927],
    },
    {
        "source": "AARO",
        "target": "Department of War",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": (
            "AARO (All-domain Anomaly Resolution Office) is a component of the Department of "
            "War, established July 2022 as successor to the UAP Task Force. Coordinates with DOW "
            "on PURSUE file preparation."
        ),
        "year_start": 2022,
        "sources": [2900, 2912],
    },
    # ---- Person → PURSUE (statements/critique) ----
    {
        "source": "Pete Hegseth",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As Secretary of War, Hegseth framed PURSUE as operating 'in lockstep with President "
            "Trump,' stating the files 'have long fueled justified speculation — and it's time "
            "the American people see it for themselves.'"
        ),
        "year_start": 2026,
        "sources": [2901, 2909, 2913],
    },
    {
        "source": "Tulsi Gabbard",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As DNI, Gabbard issued a supporting statement: 'Today's release is the first in "
            "what will be an ongoing joint declassification and release effort,' establishing "
            "ODNI's coordination role in the program."
        ),
        "year_start": 2026,
        "sources": [2901, 2913],
    },
    {
        "source": "Kash Patel",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As FBI Director, Patel issued a supporting statement for the PURSUE releases. "
            "FBI material — including re-released case file 62-HQ-83894 and first-hand witness "
            "FD-302 forms from 2022 to 2026 — featured prominently across tranches."
        ),
        "year_start": 2026,
        "sources": [2901, 2913],
    },
    {
        "source": "Jared Isaacman",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As NASA Administrator, Isaacman issued a supporting statement for the first PURSUE "
            "release: 'We will remain candid about what we know to be true, what we have yet to "
            "understand.' NASA mission material featured across all three tranches."
        ),
        "year_start": 2026,
        "sources": [2901, 2913],
    },
    {
        "source": "Anna Paulina Luna",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Called the first PURSUE release 'a great first step,' flagging follow-up video "
            "footage expected within approximately 30 days. Chairs the House Task Force on "
            "Declassification of Federal Secrets, whose scope expanded to include UAP transparency."
        ),
        "year_start": 2026,
        "sources": [2901, 2910, 2913],
    },
    {
        "source": "Tim Burchett",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Co-chairs the bipartisan House UAP Caucus with Rep. Jared Moskowitz. On the PURSUE "
            "drops: 'The 1st drop will be big, but in comparison to what is coming, they will be "
            "a drop in the bucket.' Participated in the June 9, 2026 Capitol presser."
        ),
        "year_start": 2026,
        "sources": [2910, 2913],
    },
    {
        "source": "Eric Burlison",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Supportive-but-wary congressional voice: framed Congress's job as preventing career "
            "intelligence officials from obstructing the directive 'to prevent selective "
            "disclosure or another dead end.' Participated in the June 9, 2026 Capitol presser."
        ),
        "year_start": 2026,
        "sources": [2910],
    },
    {
        "source": "Christopher Mellon",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Former DASD-Intelligence and Disclosure Foundation board chair. Publicly criticized "
            "PURSUE as insufficient: 'data alone is not disclosure,' calling for metadata, chain "
            "of custody, and analytical context. Noted AARO had not released Volume 2 of its "
            "historical report nor its 2025 annual report as of February 2026."
        ),
        "year_start": 2026,
        "sources": [2912, 2913],
    },
    {
        "source": "Jeremy Corbell",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "PURSUE provenance controversy: forum researcher Kyle Ferriter identified video "
            "PR-19 in Release 1 as identical to footage Corbell had leaked publicly, unredacted, "
            "in 2023 — a direct challenge to the 'never-before-seen' framing of the releases."
        ),
        "year_start": 2026,
        "sources": [2933],
    },
    {
        "source": "Ryan Graves",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Through Americans for Safe Aerospace, criticized the PURSUE releases for lacking "
            "metadata, sensor context, coordinates, and chain-of-custody information, arguing "
            "the files were insufficient for scientific or safety analysis."
        ),
        "year_start": 2026,
        "sources": [2912, 2913],
    },
    # ---- Astronaut → Release (subject_of) ----
    {
        "source": "Gordon Cooper",
        "target": "PURSUE Release 3 (June 12, 2026)",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "An audio excerpt labeled as a November 1962 Walter Cronkite interview with Cooper "
            "about UFOs was included in Release 3. In the audio, Cooper says 'a large number of "
            "exceptionally well-qualified people have seen objects' with no 'logical explanation.' "
            "The November 1962 date is single-sourced to the 2026 release — attribute, do not "
            "assert as independently verified."
        ),
        "year_start": 2026,
        "sources": [2909, 2917],
    },
    {
        "source": "Buzz Aldrin",
        "target": "PURSUE Release 1 (May 8, 2026)",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "Apollo 11 material in Release 1 included Aldrin's account of 'little flashes' and "
            "a 'bright light source.' Aldrin has consistently maintained the object was likely a "
            "separation panel from the Saturn V. The 'little flashes' observed by multiple Apollo "
            "crews were later attributed to cosmic-ray phosphenes (NASA's 'light flash phenomenon')."
        ),
        "year_start": 2026,
        "sources": [2901, 2913, 2918],
    },
    {
        "source": "Neil Armstrong",
        "target": "PURSUE Release 1 (May 8, 2026)",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "Apollo-era NASA material related to Armstrong's missions was included in the first "
            "PURSUE release alongside other Apollo program documentation."
        ),
        "year_start": 2026,
        "sources": [2901, 2918],
    },
    # ---- Publications ----
    {
        "source": "FBI",
        "target": "FBI File 62-HQ-83894",
        "type": "published",
        "tier": "documented",
        "desc": (
            "FBI case file covering UFO investigations from June 1947 through July 1968. "
            "Originally released through the FBI Vault (FOIA reading room); re-released in "
            "PURSUE Release 1 with fewer redactions."
        ),
        "year_start": 1947,
        "year_end": 1968,
        "sources": [2928, 2901],
    },
    {
        "source": "FBI File 62-HQ-83894",
        "target": "PURSUE Release 1 (May 8, 2026)",
        "type": "mentioned_in",
        "tier": "documented",
        "desc": (
            "FBI case file 62-HQ-83894 was re-released with fewer redactions in PURSUE Release 1 "
            "(May 8, 2026). The DOW claimed remaining redactions cover only witness identities "
            "and facility locations, not UAP substance."
        ),
        "year_start": 2026,
        "sources": [2901, 2918],
    },
    {
        "source": "FBI File 62-HQ-83894",
        "target": "Roswell Incident",
        "type": "documented",
        "tier": "credible",
        "desc": (
            "The file spans June 1947 to July 1968, covering the Roswell era. The FBI maintained "
            "a parallel investigative track on UFO reports during the same period as the Air "
            "Force's Project Blue Book."
        ),
        "year_start": 1947,
        "sources": [2928],
    },
    {
        "source": "FBI File 62-HQ-83894",
        "target": "Project Blue Book",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "FBI file 62-HQ-83894 (1947 to 1968) ran parallel to the USAF's Project Blue Book "
            "(1952 to 1969), documenting the FBI's independent UFO investigation track during "
            "the same era."
        ),
        "year_start": 1947,
        "year_end": 1968,
        "sources": [2928],
    },
    {
        "source": "J. Edgar Hoover",
        "target": "Hoover-Barnes Letter (1949)",
        "type": "authored",
        "tier": "documented",
        "desc": (
            "FBI Director Hoover's correspondence with Rev. Charles Barnes, dated January 31, "
            "1949, describing beams converging in the Cascade Mountains. Designated FBI-UAP-D011 "
            "in the PURSUE collection."
        ),
        "year_start": 1949,
        "sources": [2903, 2909],
    },
    {
        "source": "Hoover-Barnes Letter (1949)",
        "target": "PURSUE Release 3 (June 12, 2026)",
        "type": "mentioned_in",
        "tier": "documented",
        "desc": (
            "The 1949 Hoover-Barnes correspondence (FBI-UAP-D011) was one of ten featured items "
            "in the Release 3 carousel, describing beams in the Cascade Mountains."
        ),
        "year_start": 2026,
        "sources": [2903, 2909],
    },
    {
        "source": "Hoover-Barnes Letter (1949)",
        "target": "FBI",
        "type": "connected_to",
        "tier": "documented",
        "desc": "FBI Director Hoover's official correspondence regarding anomalous aerial observations in the Cascades.",
        "year_start": 1949,
        "sources": [2903, 2928],
    },
    # ---- NASA ----
    {
        "source": "Jared Isaacman",
        "target": "NASA",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as NASA Administrator in early 2025. Founder/CEO of Shift4 Payments; "
            "commanded the Inspiration4 (2021) and Polaris Dawn (2024) SpaceX missions."
        ),
        "year_start": 2025,
        "sources": [2924, 2901],
    },
    # ---- Capitol press conference ----
    {
        "source": "Leslie Kean",
        "target": "Capitol UAP Press Conference (June 9, 2026)",
        "type": "hosted",
        "tier": "documented",
        "desc": (
            "Co-hosted the June 9, 2026 bipartisan press conference alongside filmmaker "
            "James Fox. The event brought congressional UAP advocates together with whistleblower "
            "David Grusch on the Capitol steps."
        ),
        "year_start": 2026,
        "sources": [2910],
    },
    {
        "source": "David Grusch",
        "target": "Capitol UAP Press Conference (June 9, 2026)",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "Slated to discuss 'specific UAP and non-human intelligence-related evidence he "
            "encountered in deeply classified channels,' connecting his 2023 whistleblower "
            "testimony to the PURSUE executive disclosure effort."
        ),
        "year_start": 2026,
        "sources": [2910],
    },
    {
        "source": "Eric Burlison",
        "target": "Capitol UAP Press Conference (June 9, 2026)",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Announced participant in the June 9, 2026 Capitol steps press conference.",
        "year_start": 2026,
        "sources": [2910],
    },
    {
        "source": "Anna Paulina Luna",
        "target": "Capitol UAP Press Conference (June 9, 2026)",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "Announced participant, identified as chair of the Task Force on Declassification "
            "of Federal Secrets."
        ),
        "year_start": 2026,
        "sources": [2910],
    },
    {
        "source": "Tim Burchett",
        "target": "Capitol UAP Press Conference (June 9, 2026)",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Announced participant, identified as co-chair of the bipartisan House UAP Caucus.",
        "year_start": 2026,
        "sources": [2910],
    },
    {
        "source": "Capitol UAP Press Conference (June 9, 2026)",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The press conference was timed between PURSUE Release 2 (May 22) and Release 3 "
            "(June 12), explicitly connecting congressional UAP advocacy to the executive "
            "disclosure effort."
        ),
        "year_start": 2026,
        "sources": [2910],
    },
    # ---- NARA / statutory lane ----
    {
        "source": "UAP Records Collection (NARA RG-615)",
        "target": "UAP Disclosure Act",
        "type": "resulted_from",
        "tier": "documented",
        "desc": (
            "The NARA UAP Records Collection was established under Sections 1841 to 1843 of the "
            "FY2024 NDAA (PL 118-31), the surviving provisions of the Schumer-Rounds UAP "
            "Disclosure Act. Records transferred from ODNI, OSD, FAA, and the NRC."
        ),
        "year_start": 2024,
        "sources": [2904, 2905, 2907],
    },
    {
        "source": "UAP Records Collection (NARA RG-615)",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Two parallel disclosure lanes: the statutory NARA collection (NDAA FY2024) and the "
            "executive PURSUE program (2026 directive). NARA's rolling-basis language predates "
            "PURSUE by a full year. The NARA UAP topic page contains no mention of PURSUE, "
            "confirming the mechanisms are distinct."
        ),
        "year_start": 2025,
        "sources": [2904, 2905, 2900],
    },
    # ---- NSA FOIA ----
    {
        "source": "NSA",
        "target": "NSA UAP FOIA Release (May 2026)",
        "type": "published",
        "tier": "credible",
        "desc": (
            "The NSA released over 300 pages of TOP SECRET UMBRA UAP-related material through "
            "FOIA processes around May 18, 2026 — the 'forced lane' of disclosure, volunteered "
            "by no one and distinct from PURSUE or the NARA collection."
        ),
        "year_start": 2026,
        "sources": [2932],
    },
    {
        "source": "NSA UAP FOIA Release (May 2026)",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "The NSA FOIA release represents the 'forced lane' of UAP disclosure — material "
            "pried out through legal process, running parallel to the executive PURSUE program "
            "and the statutory NARA collection. Three doors, one leak."
        ),
        "year_start": 2026,
        "sources": [2932],
    },
    # ---- Leslie Kean cross-links ----
    {
        "source": "Leslie Kean",
        "target": "AATIP",
        "type": "exposed",
        "tier": "documented",
        "desc": (
            "Co-authored the December 16, 2017 New York Times front-page article 'Glowing Auras "
            "and Black Money' (with Blumenthal and Cooper) that first publicly revealed AATIP "
            "and published authenticated Navy UAP videos, triggering the post-2017 congressional "
            "disclosure movement."
        ),
        "year_start": 2017,
        "sources": [2919],
    },
    {
        "source": "Leslie Kean",
        "target": "David Grusch",
        "type": "exposed",
        "tier": "credible",
        "desc": (
            "Co-authored the June 2023 Debrief article breaking Grusch's whistleblower "
            "allegations of a multi-decade crash-retrieval and reverse-engineering program, "
            "leading to his July 2023 congressional testimony."
        ),
        "year_start": 2023,
        "sources": [2920],
    },
    # ---- House Task Force → PURSUE ----
    {
        "source": "House Task Force on Declassification of Federal Secrets",
        "target": "PURSUE",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Under Luna's chairmanship, the task force expanded its scope beyond JFK/RFK/MLK "
            "assassination records to include UAP transparency, providing congressional oversight "
            "adjacent to the executive PURSUE program."
        ),
        "year_start": 2026,
        "sources": [2910, 2935],
    },
]

# ============================================================
# ENTITY → SOURCE mappings
# ============================================================

ENTITY_SOURCES = {
    "PURSUE": [2900, 2901, 2902, 2903, 2908, 2909, 2911, 2912, 2913, 2918, 2933, 2937],
    "Department of War": [2900, 2901, 2927],
    "NASA": [2923, 2901, 2924],
    "PURSUE Release 1 (May 8, 2026)": [2901, 2912, 2913, 2918],
    "PURSUE Release 2 (May 22, 2026)": [2902, 2913, 2914],
    "PURSUE Release 3 (June 12, 2026)": [2903, 2909, 2915, 2917, 2921, 2936],
    "UAP Records Collection (NARA RG-615)": [2904, 2905, 2906, 2907],
    "NSA UAP FOIA Release (May 2026)": [2932],
    "FBI File 62-HQ-83894": [2928, 2901, 2918],
    "Hoover-Barnes Letter (1949)": [2903, 2909],
    "Capitol UAP Press Conference (June 9, 2026)": [2910],
    "Leslie Kean": [2919, 2920, 2926, 2931, 2910],
    "Eric Burlison": [2910, 2925],
    "Jared Isaacman": [2924, 2901],
}

# ============================================================
# ENTITY UPDATES — existing DB entities
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "AARO",
        "description_append": (
            "PURSUE coordination (2026): AARO provides coordination for the PURSUE (Presidential "
            "Unsealing and Reporting System for UAP Encounters) declassification program, "
            "preparing files from DOW and other agencies for posting at war.gov/UFO. The PURSUE "
            "portal cross-links AARO under 'other historical UAP records' but does not name AARO "
            "as the program's administrator — the authority rests with the Department of War and "
            "ODNI. Press shorthand that 'AARO administers PURSUE' is not supported by the "
            "program's own page."
        ),
        "sources": [2900, 2912],
    },
    {
        "name": "David Grusch",
        "description_append": (
            "PURSUE context (2026): Grusch's June 9 Capitol-steps press conference was explicitly "
            "framed as connecting his classified-channel whistleblower testimony to the PURSUE "
            "executive disclosure effort, bridging from sworn congressional testimony (July 2023) "
            "to executive action under Trump."
        ),
        "sources": [2910],
    },
    {
        "name": "Tim Burchett",
        "description_append": (
            "PURSUE reception (2026): Co-chairs the bipartisan House UAP Caucus with Rep. Jared "
            "Moskowitz. On the PURSUE file releases: 'The 1st drop will be big, but in comparison "
            "to what is coming, they will be a drop in the bucket.' Participated in the June 9, "
            "2026 Capitol UAP press conference alongside Grusch, Luna, Burlison, and Moskowitz."
        ),
        "sources": [2910, 2913],
    },
    {
        "name": "Anna Paulina Luna",
        "description_append": (
            "PURSUE reception (2026): Called the first PURSUE release 'a great first step,' "
            "flagging follow-up video footage expected within approximately 30 days. Participated "
            "in the June 9, 2026 Capitol UAP press conference hosted by Leslie Kean and James "
            "Fox, connecting her Task Force on Declassification work to the PURSUE disclosure arc."
        ),
        "sources": [2901, 2910, 2913],
    },
    {
        "name": "Christopher Mellon",
        "description_append": (
            "PURSUE critique (2026): Publicly criticized the PURSUE releases as insufficient, "
            "coining the recurring line 'data alone is not disclosure.' As chair of the Disclosure "
            "Foundation board, noted that AARO had released neither Volume 2 of its congressionally "
            "mandated historical report nor its 2025 annual report by February 2026. Called the "
            "effort potentially 'a consequential moment' dependent on follow-through."
        ),
        "sources": [2912, 2913],
    },
    {
        "name": "Ryan Graves",
        "description_append": (
            "PURSUE reception (2026): Through Americans for Safe Aerospace, criticized the PURSUE "
            "file releases for lacking metadata, sensor context, geographic coordinates, and "
            "chain-of-custody information, arguing the materials were insufficient for scientific "
            "or flight-safety analysis."
        ),
        "sources": [2912, 2913],
    },
    {
        "name": "Gordon Cooper",
        "description_append": (
            "PURSUE Release 3 (2026): An audio excerpt labeled November 1962, in which Walter "
            "Cronkite interviews Cooper about UFOs, was included in the third PURSUE release "
            "(June 12, 2026). In the audio, Cooper says 'a large number of exceptionally "
            "well-qualified people have seen objects' with no 'logical explanation.' The November "
            "1962 date is single-sourced to the 2026 release and uncorroborated by pre-2026 "
            "records — attribute, do not assert. In his memoir Leap of Faith (2000), Cooper wrote "
            "that 'neither he nor the other astronauts saw UFOs in space,' debunking the popular "
            "'glowing green object over Muchea' story while maintaining his lifelong belief in "
            "UFOs based on ground-level observations."
        ),
        "sources": [2909, 2917, 2929],
    },
    {
        "name": "Buzz Aldrin",
        "description_append": (
            "PURSUE Release 1 (2026): Apollo 11 material in the first PURSUE release (May 8, "
            "2026) included Aldrin's account of 'little flashes' and a 'bright light source.' "
            "Aldrin has consistently maintained the object was likely a separation panel from the "
            "Saturn V launch vehicle. The 'little flashes' observed by multiple Apollo crews were "
            "later studied by NASA as the 'light flash phenomenon,' attributed to cosmic-ray "
            "phosphenes interacting with the astronauts' retinas — a well-documented prosaic "
            "candidate that remains part of the record."
        ),
        "sources": [2901, 2913, 2918],
    },
    {
        "name": "The Pentagon",
        "description_append": (
            "Department of War rename (2025): Following a Trump executive order on September 5, 2025 (announced August 25), "
            "the Department of Defense adopted the historical 'Department of War' title in "
            "official correspondence, with war.gov replacing defense.gov as the primary web "
            "domain. The PURSUE UAP disclosure program (2026) operates under this branding. "
            "The rename is a styling directive; a permanent statutory name change would require "
            "Congressional action."
        ),
        "sources": [2900, 2927],
    },
    {
        "name": "Pete Hegseth",
        "description_append": (
            "PURSUE posture (2026): As Secretary of War, Hegseth framed the PURSUE releases as "
            "Trump-administration transparency, stating the files 'have long fueled justified "
            "speculation — and it's time the American people see it for themselves,' and "
            "characterizing the effort as operating 'in lockstep with President Trump.' At the "
            "February 23, 2026 'Arsenal of Freedom' tour stop, publicly committed the Pentagon to "
            "full compliance with Trump's UAP disclosure directive."
        ),
        "sources": [2901, 2913, 2934],
    },
    {
        "name": "Tulsi Gabbard",
        "description_append": (
            "PURSUE posture (2026): As DNI, issued a supporting statement for the first PURSUE "
            "release: 'Today's release is the first in what will be an ongoing joint "
            "declassification and release effort,' establishing ODNI's coordination role alongside "
            "the Department of War in the executive UAP disclosure program."
        ),
        "sources": [2901, 2913],
    },
    {
        "name": "Kash Patel",
        "description_append": (
            "PURSUE posture (2026): As FBI Director, issued a supporting statement for the "
            "PURSUE UAP file releases. FBI material featured prominently across tranches: the "
            "re-released case file 62-HQ-83894 (1947 to 1968 UFO investigations) in Release 1, "
            "and FD-302/FD-1057 first-hand witness interviews from 2022 to 2026 in Release 3."
        ),
        "sources": [2901, 2903, 2913],
    },
    {
        "name": "UAP Disclosure Act",
        "description_append": (
            "Statutory detail and legislative stall (2025-2026): The surviving provisions break "
            "down as: Section 1841 establishes the UAP Records Collection at NARA, Section 1842 "
            "governs review, transmission, and public disclosure of records, and Section 1843 "
            "sets grounds for postponement. The full UAPDA's nine-member, Senate-confirmed "
            "independent Review Board and eminent-domain provisions — which would have forced "
            "government possession of recovered material and biological evidence held by private "
            "entities — were stripped from the enacted FY2024 version. UAPDA language was absent "
            "from FY2026 NDAA, with the legislative disclosure track described as abandoned by "
            "December 2025. This gap is what the executive PURSUE program stepped into."
        ),
        "sources": [2907, 2935],
    },
]

# ============================================================
# GEO_COORDS — for NEW entities only
# ============================================================

GEO_COORDS = {
    "PURSUE": (38.8719, -77.0563, "credible", "The Pentagon, Arlington VA — DOW headquarters"),
    "Department of War": (38.8719, -77.0563, "credible", "The Pentagon, Arlington VA"),
    "NASA": (38.8830, -77.0164, "credible", "NASA Headquarters, Washington D.C."),
    "PURSUE Release 1 (May 8, 2026)": (38.8719, -77.0563, "credible", "Published by DOW at The Pentagon"),
    "PURSUE Release 2 (May 22, 2026)": (38.8719, -77.0563, "credible", "Published by DOW at The Pentagon"),
    "PURSUE Release 3 (June 12, 2026)": (38.8719, -77.0563, "credible", "Published by DOW at The Pentagon"),
    "UAP Records Collection (NARA RG-615)": (38.9897, -76.9378, "documented", "National Archives, College Park MD"),
    "NSA UAP FOIA Release (May 2026)": (39.1087, -76.7713, "credible", "NSA, Fort Meade MD"),
    "FBI File 62-HQ-83894": (38.8940, -77.0248, "credible", "FBI Headquarters, Washington D.C."),
    "Hoover-Barnes Letter (1949)": (46.85, -121.75, "inference", "Cascade Mountains, WA — subject location of reported beams"),
    "Capitol UAP Press Conference (June 9, 2026)": (38.8899, -77.0091, "documented", "U.S. Capitol steps, Washington D.C."),
    "Leslie Kean": (40.7128, -74.0060, "inference", "New York NY — primary professional association"),
    "Eric Burlison": (37.2090, -93.2923, "inference", "Springfield MO — MO-7 congressional district"),
    "Jared Isaacman": (38.8830, -77.0164, "inference", "NASA Headquarters, Washington D.C. — primary association"),
}

# ============================================================
# PHOTO_CANDIDATES — Commons FILE-PAGE URLs for new entities
# ============================================================

PHOTO_CANDIDATES = {
    "NASA": "https://commons.wikimedia.org/wiki/File:NASA_logo.svg",
    "Department of War": "https://commons.wikimedia.org/wiki/File:United_States_Department_of_Defense_Seal.svg",
    "Jared Isaacman": "https://commons.wikimedia.org/wiki/File:Jared_Isaacman_portrait.jpg",
    "Eric Burlison": "https://commons.wikimedia.org/wiki/File:Eric_Burlison_118th_Congress_portrait.jpg",
}
