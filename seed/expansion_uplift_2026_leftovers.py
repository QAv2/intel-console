"""
2026-08 refresh — leftover thin nodes from the Disclosure Scrolls batch that no
branch agent wired (Quigley, Rhodes, Zappa, NRO, US Space Force). Documented
historical edges only; Wikipedia used as `other` for uncontroversial facts.
"""

SOURCES = [
    {"id": 2800, "title": "Carroll Quigley — Wikipedia (Georgetown; Tragedy and Hope; Clinton's 1992 acceptance speech)",
     "url": "https://en.wikipedia.org/wiki/Carroll_Quigley", "source_type": "other", "year": 2026},
    {"id": 2801, "title": "Bill Clinton — 1992 Democratic National Convention acceptance speech (names Quigley)",
     "url": "https://www.presidency.ucsb.edu/documents/address-accepting-the-presidential-nomination-the-democratic-national-convention-new-york",
     "source_type": "archive", "author": "The American Presidency Project", "year": 1992},
    {"id": 2802, "title": "Cecil Rhodes — Wikipedia (wills, Rhodes Scholarship, 'secret society' provision)",
     "url": "https://en.wikipedia.org/wiki/Cecil_Rhodes", "source_type": "other", "year": 2026},
    {"id": 2803, "title": "Carroll Quigley, The Anglo-American Establishment (1981; written 1949) — full text at Internet Archive",
     "url": "https://archive.org/details/TheAnglo-AmericanEstablishment", "source_type": "book",
     "author": "Carroll Quigley", "year": 1981},
    {"id": 2804, "title": "Rhodes Scholarship — Wikipedia (Bill Clinton, Rhodes Scholar 1968)",
     "url": "https://en.wikipedia.org/wiki/Rhodes_Scholarship", "source_type": "other", "year": 2026},
    {"id": 2805, "title": "Frank Zappa — Wikipedia (Edgewood Arsenal childhood; Laurel Canyon; The Mothers)",
     "url": "https://en.wikipedia.org/wiki/Frank_Zappa", "source_type": "other", "year": 2026},
    {"id": 2806, "title": "National Reconnaissance Office — Wikipedia (founded 1961; existence declassified 1992; CIA/USAF staffing)",
     "url": "https://en.wikipedia.org/wiki/National_Reconnaissance_Office", "source_type": "other", "year": 2026},
    {"id": 2807, "title": "NRO — About the NRO (official)", "url": "https://www.nro.gov/About-NRO/",
     "source_type": "government", "year": 2026},
    {"id": 2808, "title": "United States Space Force — Wikipedia (established 20 Dec 2019 by the FY2020 NDAA)",
     "url": "https://en.wikipedia.org/wiki/United_States_Space_Force", "source_type": "other", "year": 2026},
    {"id": 2809, "title": "Space Force — About (official)", "url": "https://www.spaceforce.mil/About-Us/About-Space-Force/",
     "source_type": "government", "year": 2026},
]

ENTITIES = []

RELATIONSHIPS = [
    # ---- Carroll Quigley ----
    {"source": "Carroll Quigley", "target": "Bill Clinton", "type": "mentor_of", "tier": "documented",
     "desc": "Quigley taught Clinton at Georgetown's School of Foreign Service; Clinton named him in his 16 July 1992 nomination acceptance speech as the professor who shaped his view of the future.",
     "year_start": 1964, "year_end": 1968, "sources": [2800, 2801]},
    {"source": "Carroll Quigley", "target": "Council on Foreign Relations", "type": "documented", "tier": "documented",
     "desc": "In Tragedy and Hope (1966) and The Anglo-American Establishment (written 1949, published 1981) Quigley described the Council on Foreign Relations as the American front of the Milner Group / Round Table network he had studied from its own papers.",
     "sources": [2800, 2803]},
    {"source": "Carroll Quigley", "target": "Cecil Rhodes", "type": "documented", "tier": "documented",
     "desc": "The Anglo-American Establishment traces the secret society Rhodes founded in 1891 with William Stead and Lord Milner, and its successor bodies (Round Table groups, Royal Institute of International Affairs).",
     "sources": [2802, 2803]},
    # ---- Cecil Rhodes ----
    {"source": "Cecil Rhodes", "target": "Bill Clinton", "type": "connected_to", "tier": "documented",
     "desc": "Clinton was a Rhodes Scholar at University College, Oxford (1968–1970), under the scholarship created by Rhodes's will.",
     "year_start": 1968, "year_end": 1970, "sources": [2802, 2804]},
    {"source": "Cecil Rhodes", "target": "Council on Foreign Relations", "type": "influenced", "tier": "credible",
     "desc": "Per Quigley's archival study, the Milner Group that grew from Rhodes's society founded the Royal Institute of International Affairs (1920), whose American counterpart became the Council on Foreign Relations (1921). Credible tier: single scholarly source for the lineage claim.",
     "sources": [2803]},
    # ---- Frank Zappa ----
    {"source": "Frank Zappa", "target": "Jim Morrison", "type": "connected_to", "tier": "credible",
     "desc": "Contemporaries of the mid-1960s Laurel Canyon scene; both sons of defense establishment fathers (Zappa's father a chemical-warfare specialist at Edgewood Arsenal; Morrison's father commanded US naval forces during the Gulf of Tonkin incident).",
     "year_start": 1965, "sources": [2805]},
    {"source": "Frank Zappa", "target": "Aldous Huxley", "type": "influenced_by", "tier": "credible",
     "desc": "Zappa repeatedly cited the 1950s–60s California avant-garde and counterculture milieu in which Huxley's psychedelic writings circulated; he was a vocal critic of drug use himself. Credible: biographical reporting.",
     "sources": [2805]},
    # ---- NRO ----
    {"source": "NRO", "target": "CIA", "type": "affiliated_with", "tier": "documented",
     "desc": "Established 25 August 1961 as a joint CIA–Air Force organization to build and operate reconnaissance satellites (CORONA onward); its existence was classified until 1992. Staffed jointly by CIA and Department of Defense personnel.",
     "year_start": 1961, "sources": [2806, 2807]},
    {"source": "NRO", "target": "USAF", "type": "affiliated_with", "tier": "documented",
     "desc": "The Air Force has co-run the NRO since 1961; the Director of the NRO is traditionally an Air Force appointee or civilian within the Department of the Air Force.",
     "year_start": 1961, "sources": [2806, 2807]},
    {"source": "NRO", "target": "Office of the Director of National Intelligence", "type": "member_of", "tier": "documented",
     "desc": "One of the 18 members of the US Intelligence Community coordinated by the ODNI since 2005.",
     "year_start": 2005, "sources": [2806, 2807]},
    {"source": "NRO", "target": "NSA", "type": "connected_to", "tier": "documented",
     "desc": "NRO satellites collect signals intelligence that NSA processes; the two agencies jointly run overhead SIGINT programs.",
     "sources": [2806]},
    # ---- US Space Force ----
    {"source": "Donald Trump", "target": "US Space Force", "type": "created", "tier": "documented",
     "desc": "Signed the FY2020 National Defense Authorization Act on 20 December 2019, establishing the Space Force as the sixth armed service.",
     "year_start": 2019, "year_end": 2019, "sources": [2808, 2809]},
    {"source": "US Space Force", "target": "USAF", "type": "subordinate_of", "tier": "documented",
     "desc": "Organized within the Department of the Air Force, as the Marine Corps is within the Department of the Navy; built from Air Force Space Command.",
     "year_start": 2019, "sources": [2808, 2809]},
    {"source": "US Space Force", "target": "NRO", "type": "connected_to", "tier": "documented",
     "desc": "Space Force and the NRO share space-domain awareness and launch responsibilities; Space Force provides launch and range support for NRO reconnaissance payloads.",
     "year_start": 2019, "sources": [2807, 2808]},
]

ENTITY_SOURCES = {
    "Carroll Quigley": [2800, 2803],
    "Cecil Rhodes": [2802, 2803],
    "Frank Zappa": [2805],
    "NRO": [2806, 2807],
    "US Space Force": [2808, 2809],
}
