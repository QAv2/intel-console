"""
Supranational Organizations & Think Tanks — Expansion layer for Intel Console.

Maps the transnational governance layer: the elite coordinating bodies that
operate above nation-state politics. Bilderberg, Trilateral Commission, CFR,
Club of Rome, and the foundations that fund them. These are the organizations
that set policy agendas across multiple governments simultaneously.

Carroll Quigley (Bill Clinton's Georgetown mentor) documented the existence
of this network in 'Tragedy and Hope' (1966), writing from the inside.

Entities (~16): Key architects (David Rockefeller, Zbigniew Brzezinski,
George Soros, Nelson Rockefeller), organizations (Bilderberg, Trilateral
Commission, CFR, Club of Rome, Chatham House, Brookings, RAND), foundations
(Open Society, Rockefeller Foundation, Carnegie Endowment, Ford Foundation).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], Henry Kissinger [111], Kissinger Associates [115],
  World Economic Forum [309], Klaus Schwab [311],
  Bohemian Club [260], Carlyle Group [176],
  Allen Dulles [from JFK expansion]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 701-725
# ============================================================

SOURCES = [
    # --- Carroll Quigley ---
    {
        "id": 701,
        "title": "Carroll Quigley — Tragedy and Hope: A History of the World in Our Time",
        "url": "https://archive.org/details/TragedyAndHope",
        "source_type": "academic",
        "author": "Carroll Quigley",
        "year": 1966,
    },
    # --- David Rockefeller ---
    {
        "id": 702,
        "title": "David Rockefeller — Memoirs (autobiography, discusses CFR, Trilateral Commission, Bilderberg)",
        "url": "https://en.wikipedia.org/wiki/David_Rockefeller",
        "source_type": "other",
        "author": "David Rockefeller",
        "year": 2002,
    },
    # --- Bilderberg ---
    {
        "id": 703,
        "title": "Bilderberg Meetings — official press releases and participant lists",
        "url": "https://bilderbergmeetings.org/",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 704,
        "title": "Daniel Estulin — The True Story of the Bilderberg Group",
        "url": "https://en.wikipedia.org/wiki/Daniel_Estulin",
        "source_type": "journalism",
        "author": "Daniel Estulin",
        "year": 2005,
    },
    {
        "id": 705,
        "title": "Bilderberg founding by Prince Bernhard of the Netherlands (1954) — historical record",
        "url": "https://en.wikipedia.org/wiki/Bilderberg_meeting",
        "source_type": "other",
        "year": 1954,
    },
    # --- Trilateral Commission ---
    {
        "id": 706,
        "title": "Trilateral Commission — founding documents and membership lists",
        "url": "https://www.trilateral.org/",
        "source_type": "other",
        "year": 1973,
    },
    {
        "id": 707,
        "title": "Holly Sklar (ed.) — Trilateralism: The Trilateral Commission and Elite Planning for World Management",
        "url": "https://en.wikipedia.org/wiki/Trilateral_Commission",
        "source_type": "academic",
        "author": "Holly Sklar",
        "year": 1980,
    },
    # --- Council on Foreign Relations ---
    {
        "id": 708,
        "title": "Peter Grose — Continuing the Inquiry: The Council on Foreign Relations from 1921 to 1996",
        "url": "https://en.wikipedia.org/wiki/Council_on_Foreign_Relations",
        "source_type": "academic",
        "author": "Peter Grose",
        "year": 1996,
    },
    {
        "id": 709,
        "title": "CFR — War and Peace Studies project (1939-1945): shaped post-WWII international order",
        "url": "https://en.wikipedia.org/wiki/War_and_Peace_Studies",
        "source_type": "academic",
        "year": 1945,
    },
    {
        "id": 710,
        "title": "CFR membership and Annual Reports — documented overlap with CIA, State Dept, Treasury leadership",
        "url": "https://www.cfr.org/",
        "source_type": "other",
        "year": 2024,
    },
    # --- Club of Rome ---
    {
        "id": 711,
        "title": "Club of Rome — The Limits to Growth (Meadows et al., 1972)",
        "url": "https://en.wikipedia.org/wiki/The_Limits_to_Growth",
        "source_type": "academic",
        "year": 1972,
    },
    # --- Chatham House ---
    {
        "id": 712,
        "title": "Chatham House (Royal Institute of International Affairs) — founding and the Chatham House Rule",
        "url": "https://en.wikipedia.org/wiki/Chatham_House",
        "source_type": "other",
        "year": 1920,
    },
    # --- Brzezinski ---
    {
        "id": 713,
        "title": "Zbigniew Brzezinski — Between Two Ages: America's Role in the Technetronic Era",
        "url": "https://en.wikipedia.org/wiki/Between_Two_Ages",
        "source_type": "academic",
        "author": "Zbigniew Brzezinski",
        "year": 1970,
    },
    {
        "id": 714,
        "title": "Zbigniew Brzezinski — The Grand Chessboard: American Primacy and Its Geostrategic Imperatives",
        "url": "https://en.wikipedia.org/wiki/The_Grand_Chessboard",
        "source_type": "academic",
        "author": "Zbigniew Brzezinski",
        "year": 1997,
    },
    # --- Soros / Open Society ---
    {
        "id": 715,
        "title": "George Soros — Open Society Foundations annual reports and grantee database",
        "url": "https://www.opensocietyfoundations.org/",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 716,
        "title": "George Soros — Soros on Soros: Staying Ahead of the Curve (autobiography)",
        "url": "https://en.wikipedia.org/wiki/George_Soros",
        "source_type": "other",
        "author": "George Soros",
        "year": 1995,
    },
    # --- Foundations / CIA Conduits ---
    {
        "id": 717,
        "title": "Church Committee — CIA Use of Foundations as Funding Conduits (Book I, Chapter IX)",
        "url": "https://www.intelligence.senate.gov/sites/default/files/94755_I.pdf",
        "source_type": "congressional",
        "year": 1976,
    },
    {
        "id": 718,
        "title": "Frances Stonor Saunders — The Cultural Cold War: The CIA and the World of Arts and Letters",
        "url": "https://en.wikipedia.org/wiki/The_Cultural_Cold_War",
        "source_type": "academic",
        "author": "Frances Stonor Saunders",
        "year": 1999,
    },
    # --- RAND ---
    {
        "id": 719,
        "title": "Alex Abella — Soldiers of Reason: The RAND Corporation and the Rise of the American Empire",
        "url": "https://en.wikipedia.org/wiki/RAND_Corporation",
        "source_type": "journalism",
        "author": "Alex Abella",
        "year": 2008,
    },
    # --- Brookings ---
    {
        "id": 720,
        "title": "Brookings Institution — founding history and policy influence (est. 1916)",
        "url": "https://en.wikipedia.org/wiki/Brookings_Institution",
        "source_type": "other",
        "year": 1916,
    },
    # --- Carnegie ---
    {
        "id": 721,
        "title": "Carnegie Endowment for International Peace — founding (Andrew Carnegie, 1910) and Cold War role",
        "url": "https://en.wikipedia.org/wiki/Carnegie_Endowment_for_International_Peace",
        "source_type": "other",
        "year": 1910,
    },
    # --- Nelson Rockefeller ---
    {
        "id": 722,
        "title": "Nelson Rockefeller — VP, 4-term NY governor, Rockefeller Commission on CIA (1975)",
        "url": "https://en.wikipedia.org/wiki/Nelson_Rockefeller",
        "source_type": "other",
        "year": 1975,
    },
    # --- Quigley Georgetown ---
    {
        "id": 723,
        "title": "Carroll Quigley — Georgetown professor, Clinton mentor, 'Anglo-American Establishment' historian",
        "url": "https://en.wikipedia.org/wiki/Carroll_Quigley",
        "source_type": "academic",
        "year": 1981,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Key Architects ---
    {
        "name": "David Rockefeller",
        "entity_type": "person",
        "description": "Chairman of Chase Manhattan Bank. Chairman of CFR (1970-1985). Co-founder of Trilateral Commission with Brzezinski (1973). Bilderberg steering committee. In his Memoirs (2002), wrote: 'If that's the charge, I stand guilty, and I am proud of it' regarding accusations of conspiring toward 'one world' governance.",
        "aliases": "",
        "metadata": {"role": "banker / think tank architect", "years_active": "1946-2017"},
    },
    {
        "name": "Zbigniew Brzezinski",
        "entity_type": "person",
        "description": "National Security Advisor under Carter. Co-founder of Trilateral Commission with David Rockefeller. Architect of Carter's Afghanistan policy (supporting mujahideen against USSR — later became Al-Qaeda). His books laid out the framework for American global hegemony and technetronic control.",
        "aliases": "Zbig",
        "metadata": {"role": "National Security Advisor / strategist", "years_active": "1966-2017"},
    },
    {
        "name": "George Soros",
        "entity_type": "person",
        "description": "Billionaire investor and philanthropist. Founder of Open Society Foundations (1993). 'Broke the Bank of England' (1992). Funds civil society organizations globally through OSF. Connected to Bilderberg, CFR. Subject of both legitimate criticism and conspiracy theories.",
        "aliases": "György Schwartz",
        "metadata": {"role": "investor / philanthropist", "years_active": "1969-present"},
    },
    {
        "name": "Nelson Rockefeller",
        "entity_type": "person",
        "description": "Vice President (1974-77), 4-term NY governor. Chaired the Rockefeller Commission investigating CIA domestic activities (1975) — widely seen as limited hangout. Rockefeller dynasty central to founding of CFR, Trilateral Commission, and major foundations.",
        "aliases": "",
        "metadata": {"role": "VP / Governor", "years_active": "1940-1979"},
    },
    # --- Organizations ---
    {
        "name": "Bilderberg Group",
        "entity_type": "organization",
        "description": "Annual invitation-only conference of 120-150 political leaders, business executives, academics, and media from North America and Western Europe. Founded 1954 by Prince Bernhard of the Netherlands at Hotel de Bilderberg. Operates under Chatham House Rule. Participant lists published since 2010; proceedings remain secret.",
        "aliases": "Bilderberg Meetings, Bilderberg Conference",
        "metadata": {"type": "elite coordinating body", "founded": 1954},
    },
    {
        "name": "Trilateral Commission",
        "entity_type": "organization",
        "description": "Private organization founded 1973 by David Rockefeller and Zbigniew Brzezinski to foster cooperation between North America, Western Europe, and Japan. Jimmy Carter was a member before becoming president. Membership reads like a who's who of Western political and financial elite.",
        "aliases": "",
        "metadata": {"type": "elite coordinating body", "founded": 1973},
    },
    {
        "name": "Council on Foreign Relations",
        "entity_type": "organization",
        "description": "Founded 1921 from the 'Inquiry' group that advised Woodrow Wilson at Versailles. Most influential foreign policy think tank in the US. Members have included virtually every Secretary of State, CIA Director, and major media figure for a century. War and Peace Studies project (1939-45) designed the post-WWII order.",
        "aliases": "CFR",
        "metadata": {"type": "think tank", "founded": 1921},
    },
    {
        "name": "Club of Rome",
        "entity_type": "organization",
        "description": "International think tank founded 1968. Published 'The Limits to Growth' (1972) — influential study on resource depletion and population. Criticized for promoting depopulation narrative. Members include heads of state, Nobel laureates, and business leaders.",
        "aliases": "",
        "metadata": {"type": "think tank", "founded": 1968},
    },
    {
        "name": "Chatham House",
        "entity_type": "organization",
        "description": "Royal Institute of International Affairs. Founded 1920 as the British counterpart to CFR — both emerged from the same Paris Peace Conference (1919) discussions. Origin of the 'Chatham House Rule' (non-attribution of remarks). Major influence on British foreign policy.",
        "aliases": "RIIA, Royal Institute of International Affairs",
        "metadata": {"type": "think tank", "founded": 1920},
    },
    {
        "name": "Brookings Institution",
        "entity_type": "organization",
        "description": "Oldest US think tank (1916). Considered centrist/center-left. Significant influence on economic and foreign policy. Consistently ranked among most influential think tanks globally. Close ties to Democratic administrations.",
        "aliases": "Brookings",
        "metadata": {"type": "think tank", "founded": 1916},
    },
    {
        "name": "RAND Corporation",
        "entity_type": "organization",
        "description": "Global policy think tank created by Douglas Aircraft Company for the U.S. military (1948). Developed game theory, nuclear strategy (MAD), systems analysis for Pentagon. Produced the Pentagon Papers. Deep integration with military-intelligence establishment.",
        "aliases": "RAND",
        "metadata": {"type": "think tank / defense research", "founded": 1948},
    },
    {
        "name": "Open Society Foundations",
        "entity_type": "foundation",
        "description": "Founded by George Soros (1993). World's largest private funder of civil society groups ($32B+ granted). Operates in 120+ countries. Funds democracy promotion, human rights, media, education. Critics argue it promotes regime change and undermines national sovereignty.",
        "aliases": "OSF, Open Society Institute",
        "metadata": {"type": "foundation", "founded": 1993},
    },
    {
        "name": "Rockefeller Foundation",
        "entity_type": "foundation",
        "description": "Founded 1913 by John D. Rockefeller. Funded public health, agriculture (Green Revolution), social science. Church Committee documented CIA use of foundations as funding conduits during Cold War — Rockefeller Foundation among those identified.",
        "aliases": "",
        "metadata": {"type": "foundation", "founded": 1913},
    },
    {
        "name": "Carnegie Endowment for International Peace",
        "entity_type": "foundation",
        "description": "Founded 1910 by Andrew Carnegie. Global think tank on international affairs. Early leadership overlapped extensively with CFR. Alger Hiss was president (1946-1949) before his espionage conviction. Key node in the elite foreign policy establishment.",
        "aliases": "Carnegie Endowment, CEIP",
        "metadata": {"type": "foundation/think tank", "founded": 1910},
    },
    {
        "name": "Ford Foundation",
        "entity_type": "foundation",
        "description": "Founded 1936 by Henry Ford. Became one of world's largest foundations. Church Committee documented CIA's use of Ford Foundation as a conduit for covert funding during the Cultural Cold War. Also funded civil rights, arts, and education independently.",
        "aliases": "",
        "metadata": {"type": "foundation", "founded": 1936},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- David Rockefeller ---
    {
        "source": "David Rockefeller",
        "target": "Trilateral Commission",
        "type": "founded",
        "tier": "documented",
        "desc": "Co-founded with Brzezinski in 1973 to foster cooperation between North America, Europe, and Japan.",
        "sources": [702, 706],
        "year_start": 1973,
        "year_end": 2017,
    },
    {
        "source": "David Rockefeller",
        "target": "Council on Foreign Relations",
        "type": "directed",
        "tier": "documented",
        "desc": "Chairman 1970-1985. The CFR's most prominent leader in the 20th century. Family connection to CFR since founding.",
        "sources": [702, 708],
        "year_start": 1970,
        "year_end": 1985,
    },
    {
        "source": "David Rockefeller",
        "target": "Bilderberg Group",
        "type": "member_of",
        "tier": "documented",
        "desc": "Member of Bilderberg steering committee for decades. Attended regularly.",
        "sources": [702, 703],
        "year_start": 1954,
        "year_end": 2017,
    },
    # --- Brzezinski ---
    {
        "source": "Zbigniew Brzezinski",
        "target": "Trilateral Commission",
        "type": "founded",
        "tier": "documented",
        "desc": "Co-founded with David Rockefeller. Served as first director. Recruited Jimmy Carter as member before his presidential run.",
        "sources": [706, 707, 713],
        "year_start": 1973,
        "year_end": 2017,
    },
    {
        "source": "Zbigniew Brzezinski",
        "target": "Council on Foreign Relations",
        "type": "member_of",
        "tier": "documented",
        "desc": "Long-standing CFR member. Used CFR as platform for policy influence across multiple administrations.",
        "sources": [708, 714],
        "year_start": 1960,
        "year_end": 2017,
    },
    # --- Soros ---
    {
        "source": "George Soros",
        "target": "Open Society Foundations",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded OSF in 1993. Has given $32B+ to the network of foundations operating in 120+ countries.",
        "sources": [715, 716],
        "year_start": 1993,
        "year_end": None,
    },
    {
        "source": "George Soros",
        "target": "Council on Foreign Relations",
        "type": "member_of",
        "tier": "documented",
        "desc": "CFR member and donor. Participates in the elite foreign policy establishment.",
        "sources": [710, 716],
        "year_start": 1990,
        "year_end": None,
    },
    # --- Nelson Rockefeller ---
    {
        "source": "Nelson Rockefeller",
        "target": "Rockefeller Foundation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Rockefeller dynasty central to the foundation. Nelson served as trustee. Family foundation integral to elite network.",
        "sources": [722],
        "year_start": 1940,
        "year_end": 1979,
    },
    {
        "source": "Nelson Rockefeller",
        "target": "Council on Foreign Relations",
        "type": "member_of",
        "tier": "documented",
        "desc": "CFR member. Rockefeller family central to CFR from its founding.",
        "sources": [708, 722],
        "year_start": 1940,
        "year_end": 1979,
    },
    # --- Kissinger ---
    {
        "source": "Henry Kissinger",
        "target": "Council on Foreign Relations",
        "type": "member_of",
        "tier": "documented",
        "desc": "Long-standing CFR member and director. CFR was his primary platform for policy influence before government service.",
        "sources": [708, 710],
        "year_start": 1956,
        "year_end": 2023,
    },
    {
        "source": "Henry Kissinger",
        "target": "Bilderberg Group",
        "type": "member_of",
        "tier": "documented",
        "desc": "Regular Bilderberg attendee for decades. Key connector between US and European political elites.",
        "sources": [703, 704],
        "year_start": 1957,
        "year_end": 2023,
    },
    {
        "source": "Henry Kissinger",
        "target": "Trilateral Commission",
        "type": "member_of",
        "tier": "documented",
        "desc": "Trilateral Commission member. Connected across all three major elite coordinating bodies.",
        "sources": [706],
        "year_start": 1973,
        "year_end": 2023,
    },
    # --- Klaus Schwab ---
    {
        "source": "Klaus Schwab",
        "target": "Bilderberg Group",
        "type": "member_of",
        "tier": "documented",
        "desc": "WEF founder attended Bilderberg meetings. WEF and Bilderberg share significant membership overlap.",
        "sources": [703],
        "year_start": 1992,
        "year_end": None,
    },
    # --- CFR / Chatham House ---
    {
        "source": "Council on Foreign Relations",
        "target": "Chatham House",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Founded as sister organizations from same Paris Peace Conference discussions (1919). CFR for US, Chatham House for UK.",
        "sources": [708, 712],
        "year_start": 1920,
        "year_end": None,
    },
    # --- CIA / Foundation Conduits ---
    {
        "source": "CIA",
        "target": "Ford Foundation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Church Committee documented CIA's use of Ford Foundation as conduit for covert funding during Cultural Cold War.",
        "sources": [717, 718],
        "year_start": 1950,
        "year_end": 1967,
    },
    {
        "source": "CIA",
        "target": "Rockefeller Foundation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Church Committee identified Rockefeller Foundation among foundations used as CIA funding conduits during Cold War.",
        "sources": [717, 718],
        "year_start": 1950,
        "year_end": 1967,
    },
    {
        "source": "Allen Dulles",
        "target": "Council on Foreign Relations",
        "type": "member_of",
        "tier": "documented",
        "desc": "CFR president (1927-1933) before becoming CIA Director. CFR-CIA personnel overlap has been continuous since founding.",
        "sources": [708],
        "year_start": 1927,
        "year_end": 1969,
    },
    # --- RAND / DARPA ---
    {
        "source": "RAND Corporation",
        "target": "DARPA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "RAND conducts extensive research for DOD and DARPA. Developed nuclear strategy, game theory, systems analysis used by military.",
        "sources": [719],
        "year_start": 1958,
        "year_end": None,
    },
    # --- Bohemian Club ---
    {
        "source": "David Rockefeller",
        "target": "Bohemian Club",
        "type": "member_of",
        "tier": "documented",
        "desc": "Bohemian Club member. The club represents another node in the elite social network alongside Bilderberg, CFR, and Trilateral.",
        "sources": [702],
        "year_start": 1950,
        "year_end": 2017,
    },
    # --- WEF / Trilateral ---
    {
        "source": "World Economic Forum",
        "target": "Trilateral Commission",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Significant membership overlap. Both serve as elite coordinating bodies — Trilateral for geopolitics, WEF for public-private partnerships.",
        "sources": [706],
        "year_start": 1973,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "David Rockefeller": [701, 702, 703, 706, 708],
    "Zbigniew Brzezinski": [706, 707, 713, 714],
    "George Soros": [715, 716],
    "Nelson Rockefeller": [722],
    "Bilderberg Group": [703, 704, 705],
    "Trilateral Commission": [706, 707],
    "Council on Foreign Relations": [701, 708, 709, 710],
    "Club of Rome": [711],
    "Chatham House": [712],
    "Brookings Institution": [720],
    "RAND Corporation": [719],
    "Open Society Foundations": [715],
    "Rockefeller Foundation": [717],
    "Carnegie Endowment for International Peace": [721],
    "Ford Foundation": [717, 718],
}
