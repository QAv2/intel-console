"""
Dynastic Family Networks — Expansion layer for Intel Console.

Maps the multi-generational family networks that built and control the
institutional infrastructure of power: banking, oil, defense, media,
and foundations. These families created the organizations mapped in other
expansions — CFR, Trilateral Commission, major foundations, Federal Reserve.

Focus on documented, multi-generational influence rather than conspiracy
speculation. The Rockefellers created the CFR, funded CIA operations through
foundations, built Standard Oil. The Bushes span intelligence, oil, and politics
across four generations. The Harrimans bankrolled both sides of conflicts.

Entities (~16): Families and key patriarchs (John D. Rockefeller, J.P. Morgan,
Andrew Carnegie, Averell Harriman, Prescott Bush, the Warburg dynasty),
organizations (Federal Reserve, Standard Oil, J.P. Morgan & Co., Skull and Bones,
Brown Brothers Harriman), events (Jekyll Island Meeting, Pujo Committee).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  George H.W. Bush [242], George W. Bush [243],
  David Rockefeller [from supranational], Nelson Rockefeller [from supranational],
  Rockefeller Foundation [from supranational], Carnegie Endowment [from supranational],
  Ford Foundation [from supranational], Council on Foreign Relations [from supranational],
  Trilateral Commission [from supranational], Allen Dulles [from JFK],
  Carlyle Group [176], Bill Clinton [32], Henry Kissinger [111],
  Dwight D. Eisenhower [from MIC], JPMorgan Chase [56]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 821-850
# ============================================================

SOURCES = [
    # --- Rockefeller ---
    {
        "id": 821,
        "title": "Ron Chernow — Titan: The Life of John D. Rockefeller, Sr.",
        "url": "https://en.wikipedia.org/wiki/Titan:_The_Life_of_John_D._Rockefeller,_Sr.",
        "source_type": "academic",
        "author": "Ron Chernow",
        "year": 1998,
    },
    {
        "id": 822,
        "title": "Standard Oil — Supreme Court antitrust dissolution (Standard Oil Co. of New Jersey v. United States, 1911)",
        "url": "https://supreme.justia.com/cases/federal/us/221/1/",
        "source_type": "court",
        "year": 1911,
    },
    # --- J.P. Morgan ---
    {
        "id": 823,
        "title": "Ron Chernow — The House of Morgan: An American Banking Dynasty and the Rise of Modern Finance",
        "url": "https://en.wikipedia.org/wiki/The_House_of_Morgan",
        "source_type": "academic",
        "author": "Ron Chernow",
        "year": 1990,
    },
    {
        "id": 824,
        "title": "Pujo Committee — Investigation of the Money Trust (1912-1913, U.S. House Banking Committee)",
        "url": "https://en.wikipedia.org/wiki/Pujo_Committee",
        "source_type": "congressional",
        "year": 1913,
    },
    # --- Federal Reserve ---
    {
        "id": 825,
        "title": "G. Edward Griffin — The Creature from Jekyll Island: A Second Look at the Federal Reserve",
        "url": "https://en.wikipedia.org/wiki/The_Creature_from_Jekyll_Island",
        "source_type": "journalism",
        "author": "G. Edward Griffin",
        "year": 1994,
    },
    {
        "id": 826,
        "title": "Federal Reserve Act (1913) — Public Law 63-43",
        "url": "https://www.federalreservehistory.org/essays/federal-reserve-act-signed",
        "source_type": "government",
        "year": 1913,
    },
    {
        "id": 827,
        "title": "Jekyll Island Meeting (Nov 1910) — secret meeting to draft Federal Reserve plan",
        "url": "https://www.federalreservehistory.org/essays/jekyll-island-conference",
        "source_type": "other",
        "year": 1910,
    },
    # --- Bush Dynasty ---
    {
        "id": 828,
        "title": "Russ Baker — Family of Secrets: The Bush Dynasty, America's Invisible Government, and the Hidden History of the Last Fifty Years",
        "url": "https://en.wikipedia.org/wiki/Family_of_Secrets",
        "source_type": "journalism",
        "author": "Russ Baker",
        "year": 2009,
    },
    {
        "id": 829,
        "title": "Prescott Bush — Union Banking Corporation seizure under Trading with the Enemy Act (1942)",
        "url": "https://en.wikipedia.org/wiki/Prescott_Bush",
        "source_type": "government",
        "year": 1942,
    },
    {
        "id": 830,
        "title": "Kevin Phillips — American Dynasty: Aristocracy, Fortune, and the Politics of Deceit in the House of Bush",
        "url": "https://en.wikipedia.org/wiki/Kevin_Phillips_(political_commentator)",
        "source_type": "journalism",
        "author": "Kevin Phillips",
        "year": 2004,
    },
    # --- Harriman ---
    {
        "id": 831,
        "title": "Brown Brothers Harriman — corporate history (oldest and largest private investment bank in US)",
        "url": "https://en.wikipedia.org/wiki/Brown_Brothers_Harriman_%26_Co.",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 832,
        "title": "Averell Harriman — Ambassador, Governor, Cold War architect, Skull and Bones member",
        "url": "https://en.wikipedia.org/wiki/W._Averell_Harriman",
        "source_type": "other",
        "year": 2024,
    },
    # --- Warburg ---
    {
        "id": 833,
        "title": "Paul Warburg — Federal Reserve architect, first Fed board member, Kuhn Loeb partner",
        "url": "https://en.wikipedia.org/wiki/Paul_Warburg",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 834,
        "title": "James Warburg — Senate testimony: 'We shall have world government whether or not we like it' (1950)",
        "url": "https://en.wikipedia.org/wiki/James_Warburg",
        "source_type": "congressional",
        "year": 1950,
    },
    # --- Skull and Bones ---
    {
        "id": 835,
        "title": "Alexandra Robbins — Secrets of the Tomb: Skull and Bones, the Ivy League, and the Hidden Paths of Power",
        "url": "https://en.wikipedia.org/wiki/Skull_and_Bones",
        "source_type": "journalism",
        "author": "Alexandra Robbins",
        "year": 2002,
    },
    {
        "id": 836,
        "title": "Antony Sutton — America's Secret Establishment: An Introduction to the Order of Skull & Bones",
        "url": "https://en.wikipedia.org/wiki/Antony_C._Sutton",
        "source_type": "academic",
        "author": "Antony Sutton",
        "year": 1986,
    },
    # --- Carnegie ---
    {
        "id": 837,
        "title": "Andrew Carnegie — The Gospel of Wealth (1889) and establishment of Carnegie institutions",
        "url": "https://en.wikipedia.org/wiki/Andrew_Carnegie",
        "source_type": "other",
        "year": 1889,
    },
    # --- Standard Oil Dissolution ---
    {
        "id": 838,
        "title": "Ida Tarbell — The History of the Standard Oil Company (1904, muckraking exposé)",
        "url": "https://en.wikipedia.org/wiki/The_History_of_the_Standard_Oil_Company",
        "source_type": "journalism",
        "author": "Ida Tarbell",
        "year": 1904,
    },
    # --- DuPont ---
    {
        "id": 839,
        "title": "Gerard Colby — Du Pont Dynasty: Behind the Nylon Curtain",
        "url": "https://en.wikipedia.org/wiki/DuPont",
        "source_type": "journalism",
        "author": "Gerard Colby",
        "year": 1984,
    },
    {
        "id": 840,
        "title": "Nye Committee — Senate investigation of munitions industry profits and war profiteering (1934-1936)",
        "url": "https://en.wikipedia.org/wiki/Nye_Committee",
        "source_type": "congressional",
        "year": 1936,
    },
    # --- Business Plot ---
    {
        "id": 841,
        "title": "McCormack-Dickstein Committee — Investigation of alleged fascist coup attempt against FDR (Business Plot, 1934)",
        "url": "https://en.wikipedia.org/wiki/Business_Plot",
        "source_type": "congressional",
        "year": 1934,
    },
    # --- Smedley Butler ---
    {
        "id": 842,
        "title": "Major General Smedley Butler — 'War Is a Racket' (1935) and Business Plot testimony",
        "url": "https://en.wikipedia.org/wiki/Smedley_Butler",
        "source_type": "other",
        "author": "Smedley Butler",
        "year": 1935,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Patriarchs ---
    {
        "name": "John D. Rockefeller",
        "entity_type": "person",
        "description": "Founder of Standard Oil, wealthiest American in history (inflation-adjusted). Created the Rockefeller Foundation (1913), University of Chicago, Rockefeller Institute. Standard Oil dissolved by Supreme Court (1911) but successor companies (Exxon, Mobil, Chevron) made the family richer. Father of dynasty spanning finance, politics, and foundations.",
        "aliases": "JDR Sr.",
        "metadata": {"role": "industrialist / patriarch", "years_active": "1870-1937"},
    },
    {
        "name": "J.P. Morgan",
        "entity_type": "person",
        "description": "Banker who dominated American finance in the Gilded Age. J.P. Morgan & Co. bailed out the U.S. government (1895, 1907). Key architect of the Federal Reserve system (Jekyll Island). Pujo Committee investigation (1913) revealed his 'money trust' controlled the boards of 112 corporations. Son J.P. Morgan Jr. continued the dynasty.",
        "aliases": "John Pierpont Morgan",
        "metadata": {"role": "banker / financier", "years_active": "1857-1913"},
    },
    {
        "name": "Andrew Carnegie",
        "entity_type": "person",
        "description": "Steel magnate, philanthropist. Carnegie Steel was the world's largest. Sold to J.P. Morgan for $480M (1901) creating U.S. Steel. 'Gospel of Wealth' (1889) advocated using fortunes for public good. Created Carnegie Corporation, Carnegie Endowment, Carnegie libraries. Foundations later used as CIA conduits (Church Committee).",
        "aliases": "",
        "metadata": {"role": "industrialist / philanthropist", "years_active": "1865-1919"},
    },
    {
        "name": "Averell Harriman",
        "entity_type": "person",
        "description": "Diplomat, Governor of New York, Cold War architect. Partner at Brown Brothers Harriman (with Prescott Bush). Ambassador to USSR and UK. Skull and Bones member. Connected the banking, political, and intelligence establishments across four decades of U.S. foreign policy.",
        "aliases": "W. Averell Harriman",
        "metadata": {"role": "diplomat / banker", "years_active": "1920-1986"},
    },
    {
        "name": "Prescott Bush",
        "entity_type": "person",
        "description": "U.S. Senator (CT), partner at Brown Brothers Harriman. Father of George H.W. Bush, grandfather of George W. Bush. Union Banking Corporation (where he was director) seized under Trading with the Enemy Act (1942) for managing assets of Nazi industrialist Fritz Thyssen. Skull and Bones member (1917).",
        "aliases": "",
        "metadata": {"role": "Senator / banker", "years_active": "1926-1972"},
    },
    {
        "name": "Paul Warburg",
        "entity_type": "person",
        "description": "German-born banker, partner at Kuhn, Loeb & Co. Primary architect of the Federal Reserve System. Attended secret Jekyll Island meeting (1910) that drafted the plan. First member of the Federal Reserve Board. Brother Max Warburg headed M.M. Warburg & Co. in Hamburg — both sides of WWI.",
        "aliases": "",
        "metadata": {"role": "banker / Fed architect", "years_active": "1902-1932"},
    },
    {
        "name": "Smedley Butler",
        "entity_type": "person",
        "description": "Major General, most decorated Marine of his era. Wrote 'War Is a Racket' (1935) exposing military-industrial profiteering. Testified before Congress about the 'Business Plot' (1934) — alleged Wall Street coup attempt against FDR involving DuPont, Morgan interests. Committee confirmed the plot but no one was prosecuted.",
        "aliases": "",
        "metadata": {"role": "Major General / whistleblower", "years_active": "1898-1940"},
    },
    # --- Organizations ---
    {
        "name": "Standard Oil",
        "entity_type": "organization",
        "description": "Oil monopoly founded by John D. Rockefeller (1870). Controlled 91% of US oil production at peak. Dissolved by Supreme Court (1911) into 34 companies — successor companies (ExxonMobil, Chevron, etc.) made the Rockefellers wealthier. Ida Tarbell's exposé helped catalyze antitrust action.",
        "aliases": "Standard Oil Company, SO",
        "metadata": {"type": "corporation", "years_active": "1870-1911"},
    },
    {
        "name": "Brown Brothers Harriman",
        "entity_type": "organization",
        "description": "Oldest and largest private investment bank in the United States. Partners included Averell Harriman, Prescott Bush, Robert Lovett (later Secretary of Defense). Central node connecting banking to political power. Union Banking Corporation subsidiary seized for Nazi business ties (1942).",
        "aliases": "BBH",
        "metadata": {"type": "investment bank", "founded": 1931},
    },
    {
        "name": "Federal Reserve System",
        "entity_type": "organization",
        "description": "U.S. central bank created by Federal Reserve Act (1913). Planned at secret Jekyll Island meeting (1910) attended by representatives of Morgan, Rockefeller, Warburg, and Kuhn Loeb interests. Twelve regional banks with private ownership structure. Controls monetary policy, interest rates, money supply.",
        "aliases": "The Fed, Federal Reserve",
        "metadata": {"type": "central bank", "founded": 1913},
    },
    {
        "name": "Skull and Bones",
        "entity_type": "organization",
        "description": "Secret society at Yale University (est. 1832). 15 seniors 'tapped' annually. Members include multiple presidents (Taft, G.H.W. Bush, G.W. Bush), senators, CIA directors, Supreme Court justices, media moguls. Both 2004 presidential candidates (Bush and Kerry) were Bonesmen.",
        "aliases": "The Order, Order of Skull and Bones, 322",
        "metadata": {"type": "secret society", "founded": 1832},
    },
    {
        "name": "DuPont Family",
        "entity_type": "organization",
        "description": "Dynasty built on gunpowder and chemicals. DuPont was America's largest gunpowder manufacturer — Nye Committee (1934) investigated as 'merchants of death.' Connected to Business Plot against FDR. Later: nylon, Teflon, Kevlar, agrichemicals. Politically influential in Delaware for generations.",
        "aliases": "du Pont, DuPont",
        "metadata": {"type": "dynasty", "years_active": "1802-present"},
    },
    # --- Events ---
    {
        "name": "Jekyll Island Meeting",
        "entity_type": "event",
        "description": "Secret November 1910 meeting at Jekyll Island, Georgia where representatives of Morgan, Rockefeller, Warburg, and Kuhn Loeb interests drafted what became the Federal Reserve Act. Attendees used first names only to avoid identification. Acknowledged by the Federal Reserve's own history.",
        "aliases": "Jekyll Island Conference",
        "metadata": {"date": "1910-11-22", "location": "Jekyll Island, Georgia"},
    },
    {
        "name": "Business Plot",
        "entity_type": "event",
        "description": "Alleged 1933 coup attempt against FDR. Major General Smedley Butler testified that Wall Street interests (connected to DuPont, Morgan, Remington) tried to recruit him to lead a fascist veterans' march on Washington. McCormack-Dickstein Committee confirmed the plot but no one was prosecuted.",
        "aliases": "Wall Street Putsch, White House Putsch",
        "metadata": {"date": "1933-1934"},
    },
    {
        "name": "Pujo Committee",
        "entity_type": "event",
        "description": "1912-1913 congressional investigation of the 'money trust' — concentration of banking power. Found that Morgan, Rockefeller, and allied interests controlled the boards of 112 corporations worth $22.2 billion (1913 dollars). Led directly to Federal Reserve Act and Clayton Antitrust Act.",
        "aliases": "Money Trust Investigation",
        "metadata": {"date": "1912-1913"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Rockefeller ---
    {
        "source": "John D. Rockefeller",
        "target": "Standard Oil",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded Standard Oil (1870). Built the world's first industrial monopoly controlling 91% of US oil.",
        "sources": [821, 822, 838],
        "year_start": 1870,
        "year_end": 1911,
    },
    {
        "source": "John D. Rockefeller",
        "target": "Rockefeller Foundation",
        "type": "founded",
        "tier": "documented",
        "desc": "Established Rockefeller Foundation (1913) with $100M endowment. Later used as CIA conduit (Church Committee).",
        "sources": [821],
        "year_start": 1913,
        "year_end": 1937,
    },
    {
        "source": "David Rockefeller",
        "target": "John D. Rockefeller",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Grandson of John D. Rockefeller. Continued family's institutional influence through Chase Manhattan, CFR, Trilateral Commission.",
        "sources": [702, 821],
        "year_start": 1946,
        "year_end": 2017,
    },
    # --- Morgan ---
    {
        "source": "J.P. Morgan",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Morgan interests represented at Jekyll Island meeting (1910) that drafted the Federal Reserve plan. Morgan's 1907 bank panic was the catalyst for Federal Reserve creation.",
        "sources": [823, 825, 827],
        "year_start": 1910,
        "year_end": 1913,
    },
    {
        "source": "J.P. Morgan",
        "target": "Pujo Committee",
        "type": "investigated_by",
        "tier": "documented",
        "desc": "Pujo Committee investigated Morgan's 'money trust.' Found his network controlled 112 corporations worth $22.2 billion.",
        "sources": [823, 824],
        "year_start": 1912,
        "year_end": 1913,
    },
    {
        "source": "J.P. Morgan",
        "target": "JPMorgan Chase",
        "type": "founded",
        "tier": "documented",
        "desc": "J.P. Morgan & Co. evolved through mergers into JPMorgan Chase — now the largest US bank. Morgan legacy spans 150+ years of American finance.",
        "sources": [823],
        "year_start": 1871,
        "year_end": 1913,
    },
    # --- Warburg ---
    {
        "source": "Paul Warburg",
        "target": "Federal Reserve System",
        "type": "created",
        "tier": "documented",
        "desc": "Primary intellectual architect of the Federal Reserve. Attended Jekyll Island meeting. Served on first Federal Reserve Board.",
        "sources": [825, 826, 833],
        "year_start": 1910,
        "year_end": 1918,
    },
    {
        "source": "Paul Warburg",
        "target": "Jekyll Island Meeting",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Attended the secret 1910 meeting that drafted the Federal Reserve plan. His European central banking expertise was central to the design.",
        "sources": [825, 827, 833],
        "year_start": 1910,
        "year_end": 1910,
    },
    # --- Bush Dynasty ---
    {
        "source": "Prescott Bush",
        "target": "George H.W. Bush",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Father of George H.W. Bush. Founded the Bush political dynasty spanning banking, intelligence, oil, and the presidency.",
        "sources": [828, 829, 830],
        "year_start": 1924,
        "year_end": 1972,
    },
    {
        "source": "Prescott Bush",
        "target": "Brown Brothers Harriman",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Partner at BBH. Director of Union Banking Corporation, seized under Trading with the Enemy Act for managing Thyssen's Nazi assets.",
        "sources": [829, 831],
        "year_start": 1931,
        "year_end": 1972,
    },
    {
        "source": "Prescott Bush",
        "target": "Skull and Bones",
        "type": "member_of",
        "tier": "documented",
        "desc": "Tapped for Skull and Bones (1917). Part of the society's political pipeline from Yale to positions of power.",
        "sources": [835, 836],
        "year_start": 1917,
        "year_end": 1972,
    },
    {
        "source": "George H.W. Bush",
        "target": "Skull and Bones",
        "type": "member_of",
        "tier": "documented",
        "desc": "Skull and Bones member (1948). CIA Director, VP, President. Carried family's intelligence connections from BBH to CIA.",
        "sources": [835, 828],
        "year_start": 1948,
        "year_end": 2018,
    },
    {
        "source": "George W. Bush",
        "target": "Skull and Bones",
        "type": "member_of",
        "tier": "documented",
        "desc": "Skull and Bones member (1968). 2004 election: both presidential candidates (Bush and Kerry) were Bonesmen.",
        "sources": [835],
        "year_start": 1968,
        "year_end": None,
    },
    # --- Harriman ---
    {
        "source": "Averell Harriman",
        "target": "Brown Brothers Harriman",
        "type": "founded",
        "tier": "documented",
        "desc": "Co-founded Brown Brothers Harriman (1931 merger). Made it the largest private investment bank in the US.",
        "sources": [831, 832],
        "year_start": 1931,
        "year_end": 1986,
    },
    {
        "source": "Averell Harriman",
        "target": "Skull and Bones",
        "type": "member_of",
        "tier": "documented",
        "desc": "Skull and Bones member (1913). Family donated the Bones 'tomb' at Yale. Connected to Bush family through BBH.",
        "sources": [835, 832],
        "year_start": 1913,
        "year_end": 1986,
    },
    # --- Carnegie ---
    {
        "source": "Andrew Carnegie",
        "target": "Carnegie Endowment for International Peace",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded Carnegie Endowment (1910) with $10M. Also created Carnegie Corporation, Carnegie libraries, Carnegie Institute of Technology.",
        "sources": [837, 721],
        "year_start": 1910,
        "year_end": 1919,
    },
    # --- DuPont ---
    {
        "source": "DuPont Family",
        "target": "Business Plot",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Butler's testimony named DuPont-connected interests in the coup attempt. Nye Committee had investigated DuPont as 'merchants of death.' No prosecution followed.",
        "sources": [839, 840, 841],
        "year_start": 1933,
        "year_end": 1934,
    },
    # --- Butler ---
    {
        "source": "Smedley Butler",
        "target": "Business Plot",
        "type": "exposed",
        "tier": "documented",
        "desc": "Testified before Congress about Wall Street coup attempt against FDR. Committee confirmed the plot but no prosecution followed.",
        "sources": [841, 842],
        "year_start": 1934,
        "year_end": 1934,
    },
    # --- Jekyll Island ---
    {
        "source": "Jekyll Island Meeting",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Secret 1910 meeting drafted what became the Federal Reserve Act (1913). Acknowledged by the Fed's own historians.",
        "sources": [825, 826, 827],
        "year_start": 1910,
        "year_end": 1913,
    },
    # --- Allen Dulles / Skull and Bones Pipeline ---
    {
        "source": "Allen Dulles",
        "target": "Council on Foreign Relations",
        "type": "connected_to",
        "tier": "documented",
        "desc": "CFR member and president (1927-33). The CFR-CIA pipeline was established by Dulles and his circle. (Already linked in supranational expansion — this captures the dynasty dimension.)",
        "sources": [708],
        "year_start": 1927,
        "year_end": 1969,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "John D. Rockefeller": [821, 822, 838],
    "J.P. Morgan": [823, 824],
    "Andrew Carnegie": [837],
    "Averell Harriman": [831, 832],
    "Prescott Bush": [828, 829, 830, 831],
    "Paul Warburg": [825, 826, 827, 833],
    "Smedley Butler": [841, 842],
    "Standard Oil": [821, 822, 838],
    "Brown Brothers Harriman": [831],
    "Federal Reserve System": [825, 826, 827],
    "Skull and Bones": [835, 836],
    "DuPont Family": [839, 840],
    "Jekyll Island Meeting": [825, 827],
    "Business Plot": [841, 842],
    "Pujo Committee": [824],
}
