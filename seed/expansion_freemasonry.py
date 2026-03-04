"""
Freemasonry Deep Dive — Intelligence & Power Connections: Expansion layer for Intel Console.

Maps the documented intersections between Freemasonry, intelligence agencies, financial
scandals, and political power structures. This is one of the most myth-encrusted topics
in conspiracy research — the expansion applies strict evidence tiering to separate what
is DOCUMENTED from what is inference or speculation.

Three clusters of hard evidence anchor this expansion:

1. P2 LODGE / BANCO AMBROSIANO (DOCUMENTED): The Propaganda Due (P2) lodge under
   Licio Gelli is the single best-documented case of a Masonic lodge operating as a
   covert political-intelligence network. Italian parliamentary investigation (1981)
   exposed 962 members including cabinet ministers, military chiefs, intelligence
   heads, and financiers. The Banco Ambrosiano collapse ($1.4B) and Roberto Calvi's
   murder ("God's Banker," found hanging under Blackfriars Bridge, 1982) directly
   connect P2 to Vatican Bank (IOR), CIA Cold War financing, and organized crime.
   This is not speculation — it is Italian parliamentary record, court proceedings,
   and banking forensics.

2. SMOM-CIA PIPELINE (DOCUMENTED): The Sovereign Military Order of Malta is a
   Vatican-recognized sovereign entity whose American members included Allen Dulles,
   William Casey, William Donovan (OSS founder), James Jesus Angleton, and Alexander
   Haig. This is not a secret — SMOM membership is a matter of record. The pattern
   of senior CIA/intelligence officials holding SMOM membership documents an
   institutional bridge between Vatican intelligence networks and American covert
   operations, particularly during the Cold War.

3. ALBERT PIKE & THE SCOTTISH RITE (DOCUMENTED/MIXED): Pike's role as Sovereign
   Grand Commander of the Scottish Rite Southern Jurisdiction (1859-1891) and his
   authorship of "Morals and Dogma" are documented history. His Confederate military
   service and post-war rehabilitation through Masonic networks are documented. The
   "Three World Wars" letter attributed to Pike is almost certainly a fabrication
   (first appeared in 1958, no original exists) — this expansion explicitly flags it.

What is DOCUMENTED: P2 membership lists, Calvi's death, Banco Ambrosiano forensics,
SMOM membership rosters, Pike's writings, Scottish Rite organizational history,
Grand Orient/UGLE schism, Masonic membership of specific intelligence directors.

What is INFERENCE: Masonic networks as intelligence recruitment pipelines (pattern
fits but causal mechanism not proven for all cases).

What is SPECULATIVE: Claims about Masonic control of governments, "Luciferian"
theology derived from out-of-context Pike quotes, grand unified conspiracy theories.

Entities (20): People (Albert Pike, Manly P. Hall, Licio Gelli, Roberto Calvi,
P.D. Houston, Albert Mackey, William Donovan), Organizations (Scottish Rite
Southern Jurisdiction, York Rite, Propaganda Due, United Grand Lodge of England,
Grand Orient de France, Shriners, Sovereign Military Order of Malta, Knights
Templar), Events (P2 Lodge Scandal, Calvi Murder, Banco Ambrosiano Collapse),
Facilities (House of the Temple).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA, FBI, NSA, MI5, MI6, Mossad, Vatican,
  Allen Dulles, J. Edgar Hoover, William Casey,
  Skull and Bones, Bohemian Club,
  Thule Society, Ordo Templi Orientis, Temple of Set,
  Aleister Crowley, Jack Parsons, Michael Aquino, OSS, MKULTRA

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 991-1020
# ============================================================

SOURCES = [
    # --- Albert Pike / Scottish Rite ---
    {
        "id": 991,
        "title": "Albert Pike — Morals and Dogma of the Ancient and Accepted Scottish Rite of Freemasonry (1871)",
        "url": "https://en.wikipedia.org/wiki/Morals_and_Dogma_of_the_Ancient_and_Accepted_Scottish_Rite_of_Freemasonry",
        "source_type": "book",
        "author": "Albert Pike",
        "year": 1871,
    },
    {
        "id": 992,
        "title": "Walter Lee Brown — A Life of Albert Pike (University of Arkansas Press, 1997)",
        "url": "https://en.wikipedia.org/wiki/Albert_Pike",
        "source_type": "academic",
        "author": "Walter Lee Brown",
        "year": 1997,
    },
    {
        "id": 993,
        "title": "Scottish Rite of Freemasonry, SJ — Official history of the Supreme Council, 33°, Southern Jurisdiction",
        "url": "https://scottishrite.org/about/history/",
        "source_type": "archive",
        "year": 1801,
    },
    # --- Manly P. Hall ---
    {
        "id": 994,
        "title": "Manly P. Hall — The Secret Teachings of All Ages: An Encyclopedic Outline of Masonic, Hermetic, Qabbalistic and Rosicrucian Symbolical Philosophy (1928)",
        "url": "https://en.wikipedia.org/wiki/The_Secret_Teachings_of_All_Ages",
        "source_type": "book",
        "author": "Manly Palmer Hall",
        "year": 1928,
    },
    {
        "id": 995,
        "title": "Louis Sahagun — 'Manly Palmer Hall: Master of the Mysteries' (Los Angeles Times obituary and profile, 1990)",
        "url": "https://en.wikipedia.org/wiki/Manly_Palmer_Hall",
        "source_type": "journalism",
        "author": "Louis Sahagun",
        "year": 1990,
    },
    # --- P2 Lodge / Gelli ---
    {
        "id": 996,
        "title": "Italian Parliamentary Commission of Inquiry into the P2 Lodge (Commissione parlamentare d'inchiesta sulla Loggia P2, Anselmi Commission, final report 1984)",
        "url": "https://en.wikipedia.org/wiki/Propaganda_Due",
        "source_type": "government",
        "year": 1984,
    },
    {
        "id": 997,
        "title": "Philip Willan — Puppetmasters: The Political Use of Terrorism in Italy (2002)",
        "url": "https://en.wikipedia.org/wiki/Strategy_of_tension",
        "source_type": "book",
        "author": "Philip Willan",
        "year": 2002,
    },
    {
        "id": 998,
        "title": "David Yallop — In God's Name: An Investigation into the Murder of Pope John Paul I (1984)",
        "url": "https://en.wikipedia.org/wiki/In_God%27s_Name",
        "source_type": "book",
        "author": "David Yallop",
        "year": 1984,
    },
    {
        "id": 999,
        "title": "Larry Gurwin — The Calvi Affair: Death of a Banker (1983)",
        "url": "https://en.wikipedia.org/wiki/Roberto_Calvi",
        "source_type": "book",
        "author": "Larry Gurwin",
        "year": 1983,
    },
    {
        "id": 1000,
        "title": "Italian Court proceedings — Calvi murder trial (Rome, acquittals 2007; appeal upheld 2010; forensic evidence of murder vs. suicide)",
        "url": "https://en.wikipedia.org/wiki/Roberto_Calvi#Death",
        "source_type": "court",
        "year": 2007,
    },
    {
        "id": 1001,
        "title": "Rupert Cornwell — God's Banker: The Life and Death of Roberto Calvi (1984)",
        "url": "https://en.wikipedia.org/wiki/Roberto_Calvi",
        "source_type": "book",
        "author": "Rupert Cornwell",
        "year": 1984,
    },
    # --- Banco Ambrosiano / Vatican Bank ---
    {
        "id": 1002,
        "title": "Bank of Italy — Official report on Banco Ambrosiano collapse ($1.4B in unsecured loans to shell companies, 1982)",
        "url": "https://en.wikipedia.org/wiki/Banco_Ambrosiano",
        "source_type": "government",
        "year": 1982,
    },
    {
        "id": 1003,
        "title": "Gerald Posner — God's Bankers: A History of Money and Power at the Vatican (2015)",
        "url": "https://en.wikipedia.org/wiki/God%27s_Bankers",
        "source_type": "book",
        "author": "Gerald Posner",
        "year": 2015,
    },
    # --- SMOM ---
    {
        "id": 1004,
        "title": "Francesca Ferraris — The Sovereign Military Order of Malta: International Relations and Diplomacy (academic study of SMOM's sovereign status and geopolitical role)",
        "url": "https://en.wikipedia.org/wiki/Sovereign_Military_Order_of_Malta",
        "source_type": "academic",
        "year": 2009,
    },
    {
        "id": 1005,
        "title": "Martin A. Lee — 'Their Will Be Done' (intelligence community connections to SMOM and Opus Dei, Mother Jones, 1983)",
        "url": "https://en.wikipedia.org/wiki/Sovereign_Military_Order_of_Malta",
        "source_type": "journalism",
        "author": "Martin A. Lee",
        "year": 1983,
    },
    {
        "id": 1006,
        "title": "Carl Bernstein — 'The Holy Alliance' (Reagan, John Paul II, and the anti-Communist partnership, TIME, 1992)",
        "url": "https://en.wikipedia.org/wiki/Sovereign_Military_Order_of_Malta",
        "source_type": "journalism",
        "author": "Carl Bernstein",
        "year": 1992,
    },
    # --- William Donovan / OSS ---
    {
        "id": 1007,
        "title": "Douglas Waller — Wild Bill Donovan: The Spymaster Who Created the OSS and Modern American Espionage (2011)",
        "url": "https://en.wikipedia.org/wiki/William_J._Donovan",
        "source_type": "book",
        "author": "Douglas Waller",
        "year": 2011,
    },
    # --- Masonic-Intelligence General ---
    {
        "id": 1008,
        "title": "Stephen Knight — The Brotherhood: The Explosive Expose of the Secret World of the Freemasons (1984)",
        "url": "https://en.wikipedia.org/wiki/The_Brotherhood_(book)",
        "source_type": "book",
        "author": "Stephen Knight",
        "year": 1984,
    },
    {
        "id": 1009,
        "title": "John J. Robinson — Born in Blood: The Lost Secrets of Freemasonry (1989, Templar-Masonic lineage theory)",
        "url": "https://en.wikipedia.org/wiki/Born_in_Blood:_The_Lost_Secrets_of_Freemasonry",
        "source_type": "book",
        "author": "John J. Robinson",
        "year": 1989,
    },
    # --- Albert Mackey ---
    {
        "id": 1010,
        "title": "Albert G. Mackey — An Encyclopaedia of Freemasonry and Its Kindred Sciences (1874, revised editions through 1929)",
        "url": "https://en.wikipedia.org/wiki/Albert_Mackey",
        "source_type": "book",
        "author": "Albert G. Mackey",
        "year": 1874,
    },
    # --- UGLE / Grand Orient ---
    {
        "id": 1011,
        "title": "United Grand Lodge of England — Official history and constitutions (tercentenary documentation, 1717-2017)",
        "url": "https://en.wikipedia.org/wiki/United_Grand_Lodge_of_England",
        "source_type": "archive",
        "year": 1717,
    },
    {
        "id": 1012,
        "title": "Grand Orient de France — Official history (est. 1773, removed requirement for belief in Supreme Being in 1877)",
        "url": "https://en.wikipedia.org/wiki/Grand_Orient_de_France",
        "source_type": "archive",
        "year": 1773,
    },
    # --- Knights Templar ---
    {
        "id": 1013,
        "title": "Malcolm Barber — The Trial of the Templars (Cambridge University Press, 2nd ed. 2006)",
        "url": "https://en.wikipedia.org/wiki/Trials_of_the_Knights_Templar",
        "source_type": "academic",
        "author": "Malcolm Barber",
        "year": 2006,
    },
    {
        "id": 1014,
        "title": "Dan Jones — The Templars: The Rise and Spectacular Fall of God's Holy Warriors (2017)",
        "url": "https://en.wikipedia.org/wiki/Knights_Templar",
        "source_type": "book",
        "author": "Dan Jones",
        "year": 2017,
    },
    # --- House of the Temple ---
    {
        "id": 1015,
        "title": "House of the Temple — National Historic Landmark designation (Scottish Rite headquarters, Washington D.C., designed by John Russell Pope, completed 1915)",
        "url": "https://en.wikipedia.org/wiki/House_of_the_Temple",
        "source_type": "archive",
        "year": 1915,
    },
    # --- Shriners ---
    {
        "id": 1016,
        "title": "Shriners International — Official history (Ancient Arabic Order of the Nobles of the Mystic Shrine, founded 1870, appendant body requiring Masonic membership until 2000)",
        "url": "https://en.wikipedia.org/wiki/Shriners",
        "source_type": "archive",
        "year": 1870,
    },
    # --- York Rite ---
    {
        "id": 1017,
        "title": "York Rite / American Rite — General Grand Chapter, General Grand Council, Grand Encampment documentation (three-body system: Royal Arch, Cryptic, Commandery)",
        "url": "https://en.wikipedia.org/wiki/York_Rite",
        "source_type": "archive",
        "year": 1797,
    },
    # --- P.D. Houston ---
    {
        "id": 1018,
        "title": "Supreme Council, 33°, SJ — Official records of Sovereign Grand Commanders (P.D. Houston served 2003-2019)",
        "url": "https://scottishrite.org/about/sgc/",
        "source_type": "archive",
        "year": 2003,
    },
    # --- Strategy of Tension / NATO / Gladio ---
    {
        "id": 1019,
        "title": "Daniele Ganser — NATO's Secret Armies: Operation Gladio and Terrorism in Western Europe (2005)",
        "url": "https://en.wikipedia.org/wiki/NATO%27s_Secret_Armies",
        "source_type": "academic",
        "author": "Daniele Ganser",
        "year": 2005,
    },
    # --- Hoover / FBI Masonic connections ---
    {
        "id": 1020,
        "title": "Athan Theoharis — J. Edgar Hoover, Sex, and Crime: An Historical Antidote (2004, includes Masonic affiliations and relationship with Scottish Rite)",
        "url": "https://en.wikipedia.org/wiki/J._Edgar_Hoover",
        "source_type": "academic",
        "author": "Athan Theoharis",
        "year": 2004,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- People ---
    {
        "name": "Albert Pike",
        "entity_type": "person",
        "description": "Attorney, Confederate general, and Freemason who served as Sovereign Grand Commander of the Scottish Rite Southern Jurisdiction (1859-1891). Authored 'Morals and Dogma' (1871), the defining philosophical text of Scottish Rite Freemasonry. Convicted of treason for inciting Native American tribes against the Union during the Civil War, later pardoned by President Andrew Johnson (himself a Mason). His statue stood in Washington D.C. until removed in 2020. The 'Three World Wars' letter often attributed to Pike is almost certainly a fabrication — first appearing in William Guy Carr's 1958 book with no verifiable original. Pike's actual documented influence was in codifying Scottish Rite degree work and establishing the House of the Temple as the center of American Freemasonry.",
        "aliases": "Sovereign Grand Commander Pike",
        "metadata": {"role": "Sovereign Grand Commander, Scottish Rite SJ", "birth_date": "1809-12-29", "death_date": "1891-04-02"},
    },
    {
        "name": "Manly P. Hall",
        "entity_type": "person",
        "description": "Canadian-born author and mystic who wrote 'The Secret Teachings of All Ages' (1928) at age 27 — an encyclopedic synthesis of Masonic, Hermetic, Qabbalistic, and Rosicrucian philosophy. Founded the Philosophical Research Society in Los Angeles (1934). Received the 33rd degree of the Scottish Rite in 1973 (honorary, for his contributions to Masonic scholarship). Hall's work bridges Freemasonry and the broader Western esoteric tradition, and his PRS library became a significant occult research archive. His death in 1990 was followed by controversy over the disposition of his estate and rare book collection.",
        "aliases": "Manly Palmer Hall",
        "metadata": {"role": "Masonic scholar / author", "birth_date": "1901-03-18", "death_date": "1990-08-29"},
    },
    {
        "name": "Licio Gelli",
        "entity_type": "person",
        "description": "Italian financier and fascist who served as Venerable Master of the Propaganda Due (P2) Masonic lodge. Fought for Franco in the Spanish Civil War and for Mussolini's Black Shirts. Recruited by U.S. Army Counter Intelligence Corps (CIC) after WWII. Built P2 into a shadow government — the 1981 membership list exposed 962 names including 44 parliamentarians, 3 cabinet ministers, military intelligence chiefs, heads of all three Italian intelligence services, industrialists, and media magnates. Connected to CIA through Cold War anti-communist operations, to NATO's stay-behind network (Gladio), and to the Vatican Bank through Roberto Calvi. Convicted of fraud related to Banco Ambrosiano collapse. Fled to South America, extradited, died under house arrest (2015).",
        "aliases": "The Puppet Master",
        "metadata": {"role": "P2 Lodge Grand Master", "birth_date": "1919-04-21", "death_date": "2015-12-15"},
    },
    {
        "name": "Roberto Calvi",
        "entity_type": "person",
        "description": "Italian banker, chairman of Banco Ambrosiano (Italy's largest private bank). Known as 'God's Banker' for his close relationship with the Vatican Bank (IOR). P2 lodge member. Banco Ambrosiano collapsed in 1982 with $1.4 billion in losses — much of it channeled through Vatican Bank-controlled shell companies in Panama and Luxembourg. Found hanging under Blackfriars Bridge in London on June 18, 1982, with bricks in his pockets and £10,000 in cash. Initially ruled suicide. Forensic re-examination (2002) and Italian prosecutors concluded it was murder. Five defendants (including Mafia figures and Gelli's associates) acquitted in 2007 due to insufficient evidence, though the court stated murder was probable. The name 'Blackfriars' was widely noted as a Masonic reference.",
        "aliases": "God's Banker",
        "metadata": {"role": "Banco Ambrosiano chairman", "birth_date": "1920-04-13", "death_date": "1982-06-18"},
    },
    {
        "name": "P.D. Houston",
        "entity_type": "person",
        "description": "Ronald A. Seale, known in Masonic context as Sovereign Grand Commander of the Scottish Rite Southern Jurisdiction (2003-2019). Modernized Scottish Rite operations and public outreach during his tenure. Under his leadership, the Scottish Rite maintained its position as the largest Masonic appendant body in the United States, headquartered at the House of the Temple in Washington D.C. Represents the contemporary institutional face of American Freemasonry — organizational, philanthropic, largely divorced from the intelligence-connected era of the mid-20th century.",
        "aliases": "Sovereign Grand Commander",
        "metadata": {"role": "Sovereign Grand Commander, Scottish Rite SJ (2003-2019)"},
    },
    {
        "name": "Albert Mackey",
        "entity_type": "person",
        "description": "American Freemason, physician, and author. Secretary General of the Supreme Council, Scottish Rite Southern Jurisdiction (served under Albert Pike). Authored 'An Encyclopaedia of Freemasonry' (1874), the standard Masonic reference work for over a century. His scholarship codified Masonic jurisprudence, symbolism, and ritual, establishing the intellectual framework that Pike built upon in 'Morals and Dogma.' Together, Pike and Mackey defined American Masonic scholarship in the 19th century.",
        "aliases": "Albert Gallatin Mackey",
        "metadata": {"role": "Masonic scholar / Secretary General", "birth_date": "1807-03-12", "death_date": "1881-06-20"},
    },
    {
        "name": "William Donovan",
        "entity_type": "person",
        "description": "U.S. Army Major General who founded the Office of Strategic Services (OSS, 1942), the direct predecessor of the CIA. Awarded the Medal of Honor in WWI. As OSS Director, built the first centralized U.S. intelligence agency, recruiting from Wall Street, Ivy League, and Catholic networks. Knight of the Sovereign Military Order of Malta (SMOM) — his SMOM membership established the template for the CIA-Vatican intelligence channel that continued through Allen Dulles, William Casey, and James Angleton. Received the Grand Cross of the Order of St. Sylvester from Pope Pius XII (1944). His Catholic faith and Vatican connections were instrumental in OSS operations in Italy during WWII.",
        "aliases": "Wild Bill Donovan",
        "metadata": {"role": "OSS founder / SMOM Knight", "birth_date": "1883-01-01", "death_date": "1959-02-08"},
    },
    # --- Organizations ---
    {
        "name": "Scottish Rite Southern Jurisdiction",
        "entity_type": "organization",
        "description": "The Supreme Council, 33°, Ancient and Accepted Scottish Rite of Freemasonry, Southern Jurisdiction, USA. Founded in Charleston, SC (1801) — the oldest and largest Scottish Rite body in the world. Headquartered at the House of the Temple in Washington D.C. since 1915. Under Albert Pike's 32-year leadership (1859-1891), it became the dominant philosophical tradition in American Freemasonry. The 33rd degree is conferred by invitation only. During the mid-20th century, multiple members held positions in U.S. intelligence agencies — J. Edgar Hoover was a 33rd degree Scottish Rite Mason. The organization's headquarters sits 13 blocks north of the White House.",
        "aliases": "Scottish Rite SJ, Supreme Council 33° SJ, Ancient and Accepted Scottish Rite",
        "metadata": {"type": "Masonic body", "founded": 1801, "headquarters": "Washington, D.C."},
    },
    {
        "name": "York Rite",
        "entity_type": "organization",
        "description": "Collection of three Masonic bodies that confer degrees beyond the Blue Lodge: Royal Arch Masonry (Chapter), Cryptic Masonry (Council), and Knights Templar (Commandery). Also called the American Rite. The York Rite Knights Templar Commandery is the only Masonic body that requires Christian faith for membership. Historically the primary alternative to the Scottish Rite system in American Freemasonry. The York Rite's Templar degree explicitly claims lineage from the medieval Knights Templar — a historical claim that is symbolically meaningful but not supported by documented organizational continuity.",
        "aliases": "American Rite, York Rite Bodies",
        "metadata": {"type": "Masonic body", "founded": 1797},
    },
    {
        "name": "Propaganda Due",
        "entity_type": "organization",
        "description": "Italian Masonic lodge (Propaganda 2, or P2) that operated as a clandestine political-intelligence network under Licio Gelli. Originally a legitimate lodge under the Grand Orient of Italy, it became a covert organization after Gelli took control in 1966. Italian parliamentary investigation (1981) exposed 962 members including 44 members of parliament, 3 cabinet ministers, all heads of Italian intelligence services, 195 military officers, financiers, and media owners. The Anselmi Commission (1984) concluded P2 operated as 'a state within the state.' Connected to CIA through Cold War anti-communist funding, NATO's Operation Gladio stay-behind network, the Banco Ambrosiano collapse, and the Italian 'strategy of tension.' Dissolved by Italian law in 1982.",
        "aliases": "P2 Lodge, P2, Loggia Propaganda Due",
        "metadata": {"type": "clandestine Masonic lodge", "founded": 1877, "dissolved": 1982},
    },
    {
        "name": "United Grand Lodge of England",
        "entity_type": "organization",
        "description": "The governing body of Freemasonry in England, Wales, and the Channel Islands. Formed in 1813 by the merger of the 'Antients' and 'Moderns' Grand Lodges. Considers itself the oldest Grand Lodge in the world (tracing to 1717). Requires members to profess belief in a Supreme Being — the defining point of the 1877 schism with the Grand Orient de France. UGLE recognition is the standard of 'regular' Freemasonry worldwide. Historically intertwined with the British establishment — multiple members of the royal family have served as Grand Master. Stephen Knight's 'The Brotherhood' (1984) documented UGLE members' influence in British police, judiciary, and civil service.",
        "aliases": "UGLE, Grand Lodge of England",
        "metadata": {"type": "Masonic governing body", "founded": 1717, "headquarters": "London"},
    },
    {
        "name": "Grand Orient de France",
        "entity_type": "organization",
        "description": "The largest Masonic obedience in France, founded 1773. In 1877, removed the requirement for members to believe in a Supreme Being — causing a permanent schism with the United Grand Lodge of England and the broader 'regular' Masonic world. This makes the Grand Orient 'irregular' in UGLE's view, but it is the dominant form of Freemasonry in continental Europe and Latin America. Historically associated with secularism, republicanism, and anti-clericalism. Played a documented role in the French Revolution, the establishment of the Third Republic, and the 1905 separation of church and state in France. Members included Voltaire, Marquis de Lafayette, and numerous Third Republic politicians.",
        "aliases": "GODF, GOdF",
        "metadata": {"type": "Masonic governing body", "founded": 1773, "headquarters": "Paris"},
    },
    {
        "name": "Shriners",
        "entity_type": "organization",
        "description": "Fraternal order formally known as the Ancient Arabic Order of the Nobles of the Mystic Shrine, founded in New York City (1870) by Walter M. Fleming and William J. Florence. Required Master Mason status for membership until 2000 (when requirement changed to any Mason). Known publicly for Shriners Hospitals for Children (22 facilities) and festive parades. At its peak (1980s) had nearly 1 million members. The Shrine represents the social and philanthropic face of American Freemasonry — the fun-loving counterpart to the philosophical Scottish Rite and the Christian York Rite. Presidents Harding, Roosevelt (FDR), and Truman were Shriners.",
        "aliases": "Ancient Arabic Order of the Nobles of the Mystic Shrine, Shriners International, AAONMS",
        "metadata": {"type": "Masonic appendant body", "founded": 1870},
    },
    {
        "name": "Sovereign Military Order of Malta",
        "entity_type": "organization",
        "description": "Catholic lay religious order with sovereign status under international law — maintains diplomatic relations with over 100 states. Claims continuity from the Knights Hospitaller (founded 1099). Headquarters in Rome. The American Association of SMOM reads as a who's-who of the intelligence establishment: William Donovan (OSS founder), Allen Dulles (CIA Director), William Casey (CIA Director), James Jesus Angleton (CIA counterintelligence chief), Alexander Haig (Secretary of State), and William F. Buckley Jr. The concentration of senior intelligence officials in a Vatican-connected sovereign order documents an institutional channel between American intelligence and the Vatican that operated continuously from WWII through the Cold War.",
        "aliases": "SMOM, Knights of Malta, Order of Malta, Sovereign Military Hospitaller Order of Saint John",
        "metadata": {"type": "Catholic sovereign order", "founded": 1099, "headquarters": "Rome"},
    },
    {
        "name": "Knights Templar",
        "entity_type": "organization",
        "description": "Medieval Catholic military order (Poor Fellow-Soldiers of Christ and of the Temple of Solomon), founded circa 1119 during the Crusades. Became enormously wealthy through banking, land holdings, and papal privileges. Suppressed by Pope Clement V under pressure from King Philip IV of France (1312). Leaders including Grand Master Jacques de Molay were burned at the stake (1314). The Templar suppression created a mythos that Freemasonry later claimed as heritage — the York Rite Knights Templar degree and the Scottish Rite's higher degrees explicitly reference Templar symbolism. Whether there is actual organizational continuity (as claimed) or symbolic adoption (as historians generally conclude) remains debated. The Templar banking system — letters of credit, international transfers — prefigured modern international banking.",
        "aliases": "Poor Fellow-Soldiers of Christ, Templars, Order of the Temple",
        "metadata": {"type": "medieval military order", "founded": 1119, "suppressed": 1312},
    },
    # --- Events ---
    {
        "name": "P2 Lodge Scandal",
        "entity_type": "event",
        "description": "Political crisis triggered in March 1981 when Italian magistrates investigating banker Michele Sindona raided Licio Gelli's villa in Arezzo and discovered P2's membership list — 962 names including 44 members of parliament, 3 cabinet ministers, chiefs of all three Italian intelligence services (SISMI, SISDE, CESIS), 195 military officers (12 generals), heads of Italy's financial police, media magnates, and industrialists. Prime Minister Arnaldo Forlani's government fell. The Anselmi Commission parliamentary investigation (1984) concluded P2 had operated as 'a state within the state' and 'a secret structure that had the incredible capacity to control a state's institutions.' P2 was dissolved by law. The scandal exposed the intersection of Freemasonry, intelligence services, NATO stay-behind operations, and organized crime in Cold War Italy.",
        "aliases": "P2 Scandal",
        "metadata": {"date": "1981-03", "location": "Italy"},
    },
    {
        "name": "Calvi Murder",
        "entity_type": "event",
        "description": "Roberto Calvi, chairman of Banco Ambrosiano and P2 member, was found dead on June 18, 1982, hanging from scaffolding under Blackfriars Bridge in London. His pockets contained bricks and approximately £10,000 in cash in three currencies. Initially ruled suicide by a London coroner's inquest. A second inquest (1983) returned an open verdict. Independent forensic examination (2002) commissioned by his family found evidence inconsistent with suicide — no traces of rust or paint on his hands despite allegedly climbing scaffolding. Italian prosecutors charged five people with murder (2005), including Mafia boss Pippo Calo and Gelli associate Flavio Carboni. All acquitted (2007) due to insufficient evidence, though the court acknowledged murder was the probable cause of death. The location — Blackfriars Bridge — was widely interpreted as a Masonic message (Black Friars = Dominicans, referenced in Masonic symbolism).",
        "aliases": "Death of Roberto Calvi, Blackfriars Bridge Murder",
        "metadata": {"date": "1982-06-18", "location": "London, Blackfriars Bridge"},
    },
    {
        "name": "Banco Ambrosiano Collapse",
        "entity_type": "event",
        "description": "Largest bank failure in Italian history at the time. Banco Ambrosiano collapsed in June 1982 with $1.4 billion in unsecured loans, much of it channeled through shell companies in Panama, Luxembourg, and the Bahamas controlled by or connected to the Vatican Bank (Istituto per le Opere di Religione, IOR). Calvi had been funneling money through these channels at the direction of P2's Gelli and with the involvement of IOR head Archbishop Paul Marcinkus. The Vatican denied legal responsibility but paid $241 million to creditors in a 'voluntary contribution' (1984). The collapse exposed the convergence of P2, Vatican Bank, CIA Cold War financing (some funds allegedly went to Solidarity in Poland and anti-communist operations in Latin America), and Sicilian Mafia money laundering. Calvi was found dead days after the collapse.",
        "aliases": "Ambrosiano Collapse",
        "metadata": {"date": "1982-06", "location": "Milan / Vatican City"},
    },
    # --- Facility ---
    {
        "name": "House of the Temple",
        "entity_type": "facility",
        "description": "Headquarters of the Supreme Council, 33°, Scottish Rite of Freemasonry, Southern Jurisdiction. Located at 1733 16th Street NW, Washington D.C. — 13 blocks due north of the White House. Designed by architect John Russell Pope (who also designed the Jefferson Memorial and National Archives) and completed in 1915. Modeled on the Mausoleum at Halicarnassus (one of the Seven Wonders of the Ancient World). Houses the remains of Albert Pike in a crypt. Contains an extensive Masonic library and museum. National Historic Landmark. The building's location and grandeur reflect the institutional power of American Freemasonry in the early 20th century — and its proximity to the White House has been noted by researchers mapping power geography in the capital.",
        "aliases": "",
        "metadata": {"address": "1733 16th Street NW, Washington, D.C.", "completed": 1915, "architect": "John Russell Pope"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # === ALBERT PIKE / SCOTTISH RITE / HOUSE OF THE TEMPLE ===
    {
        "source": "Albert Pike",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "led",
        "tier": "documented",
        "desc": "Sovereign Grand Commander of the Scottish Rite SJ for 32 years (1859-1891). Rewrote degree rituals and authored 'Morals and Dogma,' defining the philosophical framework of American Freemasonry.",
        "sources": [991, 992, 993],
        "year_start": 1859,
        "year_end": 1891,
    },
    {
        "source": "Albert Pike",
        "target": "Albert Mackey",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Mackey served as Secretary General under Pike's leadership of the Scottish Rite SJ. Together they codified American Masonic scholarship — Pike writing 'Morals and Dogma,' Mackey writing the 'Encyclopaedia of Freemasonry.'",
        "sources": [991, 992, 1010],
        "year_start": 1859,
        "year_end": 1881,
    },
    {
        "source": "Albert Pike",
        "target": "House of the Temple",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Pike's remains are interred in the House of the Temple. The building — completed 24 years after his death — was constructed as the permanent headquarters of the Supreme Council he led. His legacy defines the institution.",
        "sources": [992, 1015],
        "year_start": 1891,
        "year_end": None,
    },
    {
        "source": "Scottish Rite Southern Jurisdiction",
        "target": "House of the Temple",
        "type": "operates",
        "tier": "documented",
        "desc": "The House of the Temple has served as headquarters of the Scottish Rite SJ since its completion in 1915. Located 13 blocks north of the White House at 1733 16th Street NW.",
        "sources": [993, 1015],
        "year_start": 1915,
        "year_end": None,
    },
    {
        "source": "P.D. Houston",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "led",
        "tier": "documented",
        "desc": "Served as Sovereign Grand Commander (2003-2019), modernizing operations and public engagement. Represents the contemporary institutional leadership of the Scottish Rite.",
        "sources": [1018],
        "year_start": 2003,
        "year_end": 2019,
    },
    {
        "source": "Albert Mackey",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "served_in",
        "tier": "documented",
        "desc": "Secretary General of the Supreme Council, 33°, SJ. His 'Encyclopaedia of Freemasonry' (1874) became the standard reference work for Masonic jurisprudence and symbolism.",
        "sources": [1010, 993],
        "year_start": 1859,
        "year_end": 1881,
    },
    # --- Hoover / Scottish Rite ---
    {
        "source": "J. Edgar Hoover",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "member_of",
        "tier": "documented",
        "desc": "33rd Degree Mason, Scottish Rite SJ. Received his 33rd degree in 1955. Maintained a close relationship with the Scottish Rite throughout his FBI directorship (1924-1972). His Masonic membership is documented in Scottish Rite records and multiple biographies.",
        "sources": [1020, 1008],
        "year_start": 1920,
        "year_end": 1972,
    },
    {
        "source": "Manly P. Hall",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Received the 33rd degree (honorary) in 1973 for his contributions to Masonic scholarship. His 'Secret Teachings of All Ages' (1928) is considered a masterwork of esoteric philosophy that bridges Masonic tradition with the broader Western mystery tradition.",
        "sources": [994, 995],
        "year_start": 1928,
        "year_end": 1990,
    },
    {
        "source": "Manly P. Hall",
        "target": "Ordo Templi Orientis",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Hall's work in 'The Secret Teachings of All Ages' covers OTO-adjacent traditions (Hermeticism, Qabalah, Rosicrucianism). Both Hall and OTO operated in the Los Angeles esoteric milieu. No direct OTO membership documented, but intellectual and social overlap existed in the Southern California occult community.",
        "sources": [994, 995],
        "year_start": 1928,
        "year_end": 1990,
    },
    # === P2 LODGE CLUSTER ===
    {
        "source": "Licio Gelli",
        "target": "Propaganda Due",
        "type": "led",
        "tier": "documented",
        "desc": "Venerable Master of P2 from 1966. Built the lodge into a clandestine political-intelligence network with 962 documented members including cabinet ministers, intelligence chiefs, and military officers. Italian parliamentary record (Anselmi Commission, 1984).",
        "sources": [996, 997],
        "year_start": 1966,
        "year_end": 1981,
    },
    {
        "source": "Licio Gelli",
        "target": "CIA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Recruited by U.S. Army Counter Intelligence Corps after WWII. Documented contacts with CIA station in Rome during Cold War anti-communist operations. P2's role in the Italian 'strategy of tension' aligned with CIA/NATO objectives. Multiple investigators (Willan, Ganser) document CIA financial support flowing through P2 channels.",
        "sources": [996, 997, 1019],
        "year_start": 1945,
        "year_end": 1981,
    },
    {
        "source": "Licio Gelli",
        "target": "Roberto Calvi",
        "type": "directed",
        "tier": "documented",
        "desc": "Calvi was a P2 member operating under Gelli's direction. Gelli used Calvi and Banco Ambrosiano as the financial arm of P2's operations — funneling money through Vatican Bank shell companies. Italian court proceedings document the Gelli-Calvi financial relationship.",
        "sources": [996, 999, 1001],
        "year_start": 1975,
        "year_end": 1982,
    },
    {
        "source": "Roberto Calvi",
        "target": "Propaganda Due",
        "type": "member_of",
        "tier": "documented",
        "desc": "P2 member. Used Banco Ambrosiano as the financial vehicle for P2 operations, channeling $1.4B through Vatican Bank-controlled shell companies. His P2 membership is documented in the seized membership list.",
        "sources": [996, 999, 1002],
        "year_start": 1975,
        "year_end": 1982,
    },
    {
        "source": "Roberto Calvi",
        "target": "Calvi Murder",
        "type": "victim_of",
        "tier": "documented",
        "desc": "Found dead under Blackfriars Bridge, London (June 18, 1982). Forensic evidence points to murder. Italian court acknowledged murder as probable cause of death despite acquitting defendants (2007).",
        "sources": [999, 1000, 1001],
        "year_start": 1982,
        "year_end": 1982,
    },
    {
        "source": "Roberto Calvi",
        "target": "Banco Ambrosiano Collapse",
        "type": "caused",
        "tier": "documented",
        "desc": "As chairman, Calvi's management (under P2/Gelli direction) created the $1.4B in unsecured loans that caused the collapse. He was found dead days after the bank failed.",
        "sources": [999, 1001, 1002],
        "year_start": 1982,
        "year_end": 1982,
    },
    {
        "source": "Calvi Murder",
        "target": "Banco Ambrosiano Collapse",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Calvi died within days of the bank's collapse. The timing — with Calvi about to face trial and potentially expose P2's financial network — points to murder to prevent testimony. Court proceedings treat the two events as directly linked.",
        "sources": [999, 1000, 1002],
        "year_start": 1982,
        "year_end": 1982,
    },
    {
        "source": "Propaganda Due",
        "target": "P2 Lodge Scandal",
        "type": "subject_of",
        "tier": "documented",
        "desc": "The 1981 raid on Gelli's villa exposed P2's membership list and triggered the parliamentary investigation. The Anselmi Commission concluded P2 was 'a state within the state.' P2 dissolved by law in 1982.",
        "sources": [996, 997],
        "year_start": 1981,
        "year_end": 1984,
    },
    {
        "source": "P2 Lodge Scandal",
        "target": "Banco Ambrosiano Collapse",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The P2 exposure (1981) precipitated the Banco Ambrosiano collapse (1982). Once Gelli's network was exposed, the financial channels he controlled through Calvi unraveled. Sequential domino: raid → scandal → bank collapse → Calvi death.",
        "sources": [996, 1002, 1003],
        "year_start": 1981,
        "year_end": 1982,
    },
    # --- P2 connections to existing entities ---
    {
        "source": "Propaganda Due",
        "target": "CIA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "P2 functioned within the CIA's Cold War anti-communist infrastructure in Italy. CIA funding flowed through P2 channels for the Italian 'strategy of tension.' Gelli had documented CIC/CIA contacts. The Anselmi Commission identified foreign intelligence connections.",
        "sources": [996, 997, 1019],
        "year_start": 1966,
        "year_end": 1981,
    },
    {
        "source": "Banco Ambrosiano Collapse",
        "target": "CIA",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Investigators allege some Banco Ambrosiano funds were channeled through Vatican Bank to CIA-backed anti-communist operations, including Solidarity in Poland and covert operations in Latin America. The full financial trail remains partially obscured by Vatican banking secrecy.",
        "sources": [1002, 1003, 1006],
        "year_start": 1978,
        "year_end": 1982,
    },
    # === SMOM-CIA PIPELINE ===
    {
        "source": "William Donovan",
        "target": "Sovereign Military Order of Malta",
        "type": "member_of",
        "tier": "documented",
        "desc": "Knight of SMOM. His membership established the OSS/CIA-Vatican channel. Received the Grand Cross of the Order of St. Sylvester from Pope Pius XII (1944) for wartime service. His SMOM membership is documented in biographical and order records.",
        "sources": [1004, 1005, 1007],
        "year_start": 1927,
        "year_end": 1959,
    },
    {
        "source": "William Donovan",
        "target": "OSS",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded and directed the Office of Strategic Services (1942-1945), the direct predecessor of the CIA. Built the first centralized American intelligence agency, recruiting from elite networks including Catholic and Masonic circles.",
        "sources": [1007],
        "year_start": 1942,
        "year_end": 1945,
    },
    {
        "source": "Allen Dulles",
        "target": "Sovereign Military Order of Malta",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Dulles maintained connections with SMOM as CIA Director. His brother John Foster Dulles (Secretary of State) had parallel Vatican contacts. The Dulles brothers' Catholic establishment connections facilitated the CIA-Vatican intelligence pipeline that SMOM members helped maintain.",
        "sources": [1005, 1006],
        "year_start": 1953,
        "year_end": 1961,
    },
    {
        "source": "William Casey",
        "target": "Sovereign Military Order of Malta",
        "type": "member_of",
        "tier": "documented",
        "desc": "Knight of SMOM. As CIA Director (1981-87), Casey used Vatican and SMOM channels for covert anti-communist operations, particularly in Poland (Solidarity) and Central America. Carl Bernstein's 1992 TIME investigation documented the Reagan-Vatican 'Holy Alliance' that Casey helped coordinate.",
        "sources": [1005, 1006],
        "year_start": 1971,
        "year_end": 1987,
    },
    {
        "source": "Sovereign Military Order of Malta",
        "target": "CIA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Multiple CIA directors and senior officials were SMOM members: Donovan (OSS), Dulles, Casey, Angleton. This concentration of intelligence leadership in a Vatican-recognized sovereign order documents an institutional bridge between American intelligence and Vatican networks spanning from WWII through the Cold War.",
        "sources": [1004, 1005, 1006, 1007],
        "year_start": 1942,
        "year_end": 1987,
    },
    # === UGLE / GRAND ORIENT SCHISM ===
    {
        "source": "United Grand Lodge of England",
        "target": "Grand Orient de France",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The 1877 schism: GODF removed the requirement for belief in a Supreme Being, and UGLE withdrew recognition. This split divided global Freemasonry into 'regular' (UGLE-recognized, deist) and 'irregular' (continental, secular) branches — a division that persists today. The schism reflects deeper philosophical differences: Anglo-Saxon Freemasonry stayed tied to Christianity/deism; continental Freemasonry embraced Enlightenment secularism.",
        "sources": [1011, 1012],
        "year_start": 1877,
        "year_end": None,
    },
    {
        "source": "United Grand Lodge of England",
        "target": "MI5",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Stephen Knight's 'The Brotherhood' (1984) documented significant Masonic membership among British police, judiciary, and intelligence officers. UGLE's intertwining with the British establishment is widely acknowledged — multiple royals have served as Grand Master. Direct UGLE-MI5 institutional coordination is inference, but individual overlap is documented.",
        "sources": [1008, 1011],
        "year_start": 1717,
        "year_end": None,
    },
    {
        "source": "Grand Orient de France",
        "target": "MI6",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Continental Masonic networks provided intelligence contacts during both World Wars. French Masonic resistance networks operated during WWII, with some MI6/SOE liaison. The connection is institutional-cultural rather than direct organizational control.",
        "sources": [1008, 1012],
        "year_start": 1914,
        "year_end": 1945,
    },
    # === KNIGHTS TEMPLAR / HISTORICAL LINEAGE ===
    {
        "source": "Knights Templar",
        "target": "York Rite",
        "type": "connected_to",
        "tier": "inference",
        "desc": "The York Rite Knights Templar Commandery claims symbolic lineage from the medieval Templars. Historians generally view this as symbolic adoption rather than organizational continuity — there is a 400-year gap (1312-1717) with no documented chain. John J. Robinson's 'Born in Blood' (1989) argues for continuity through stonemason guilds, but this remains a minority academic position.",
        "sources": [1009, 1013, 1014, 1017],
        "year_start": 1312,
        "year_end": None,
    },
    {
        "source": "Knights Templar",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Scottish Rite higher degrees reference Templar symbolism, particularly the Rose Croix (18th degree) and Kadosh (30th degree). Pike's 'Morals and Dogma' discusses Templar history and symbolism extensively. The connection is mythological and symbolic — used to construct the narrative of ancient wisdom transmitted through secret channels.",
        "sources": [991, 993, 1013],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Knights Templar",
        "target": "Sovereign Military Order of Malta",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Templars and Hospitallers (SMOM's predecessors) were contemporary Crusader military orders. After the Templar suppression (1312), much Templar property was transferred to the Hospitallers by papal decree. SMOM thus has documented historical continuity from the Crusader era that the Masonic Templar degrees can only claim symbolically.",
        "sources": [1004, 1013, 1014],
        "year_start": 1099,
        "year_end": 1312,
    },
    # === CROSS-REFERENCES TO EXISTING ENTITIES ===
    {
        "source": "Scottish Rite Southern Jurisdiction",
        "target": "Skull and Bones",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both are initiatic secret societies with hierarchical degree structures, elite recruitment, and documented influence on American political leadership. No direct organizational link, but significant membership overlap — individuals were often members of both. They represent parallel power networks: Skull and Bones at Yale, Scottish Rite in broader American civic life.",
        "sources": [993, 1008],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Propaganda Due",
        "target": "Bohemian Club",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both represent elite social networks that operated as influence channels parallel to formal government structures. P2 in Italy, Bohemian Club in the U.S. No direct organizational connection, but both illustrate the pattern of elite clubs serving as informal governance and intelligence coordination mechanisms.",
        "sources": [996, 997],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Thule Society",
        "target": "Grand Orient de France",
        "type": "connected_to",
        "tier": "inference",
        "desc": "The Thule Society drew from the same Western esoteric tradition as continental Freemasonry but inverted it toward volkisch nationalism and racial mysticism. The Nazis later suppressed German Freemasonry, viewing it as a Jewish-internationalist conspiracy — illustrating how occult fraternalism could produce both Enlightenment universalism (GODF) and ethno-nationalist extremism (Thule).",
        "sources": [1012, 1008],
        "year_start": 1918,
        "year_end": 1935,
    },
    {
        "source": "Aleister Crowley",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Crowley held various Masonic degrees (irregular lines) and drew extensively from Masonic symbolism in constructing OTO's degree system. His Thelemic reinterpretation of Masonic ritual represents the heterodox branch of the esoteric tradition — where Pike's Scottish Rite stayed within deist orthodoxy, Crowley pushed toward explicit occultism.",
        "sources": [991, 994],
        "year_start": None,
        "year_end": None,
    },
    {
        "source": "Shriners",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Shrine required Scottish Rite (32nd degree) or York Rite (Knights Templar) membership until 2000. This made it the social capstone of American Freemasonry — members had already passed through the philosophical (Scottish Rite) or Christian (York Rite) pathways. Multiple U.S. Presidents were Shriners: Harding, FDR, Truman.",
        "sources": [1016, 993],
        "year_start": 1870,
        "year_end": None,
    },
    {
        "source": "York Rite",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The two primary Masonic appendant body systems in the United States. Both build on Blue Lodge (first 3 degrees). Scottish Rite adds degrees 4-33 with philosophical/deist emphasis; York Rite adds Royal Arch, Cryptic, and Templar degrees with Christian emphasis. Many Masons belong to both.",
        "sources": [993, 1017],
        "year_start": 1801,
        "year_end": None,
    },
    # --- FBI / Masonic connection ---
    {
        "source": "J. Edgar Hoover",
        "target": "House of the Temple",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Hoover was a 33rd degree Scottish Rite Mason and frequent presence at the House of the Temple. His FBI career (1924-1972) coincided with the peak of Masonic influence in American civic life. The proximity of FBI headquarters and the House of the Temple — both in central Washington — symbolizes the institutional overlap.",
        "sources": [1020, 1015],
        "year_start": 1920,
        "year_end": 1972,
    },
    # --- Gelli / Thule parallel ---
    {
        "source": "Licio Gelli",
        "target": "Thule Society",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Gelli fought for Mussolini's Black Shirts and Franco in Spain before building P2. The Thule Society fed into the Nazi party. Both represent the pattern of esoteric/fraternal organizations being captured by fascist political operators — secret societies as vehicles for authoritarian power rather than Enlightenment ideals.",
        "sources": [996, 997],
        "year_start": None,
        "year_end": None,
    },
    # --- MKULTRA / Masonic overlap ---
    {
        "source": "MKULTRA",
        "target": "Scottish Rite Southern Jurisdiction",
        "type": "connected_to",
        "tier": "inference",
        "desc": "MKULTRA's behavioral modification research and Masonic initiatic ritual both deal in the transformation of consciousness through structured ordeal. Some researchers (Levenda) note the conceptual parallel. Dulles (who authorized MKULTRA) had connections to SMOM and elite fraternal networks. No documented direct link between MKULTRA and Masonic institutions, but the personnel overlap in the intelligence community creates an indirect connection.",
        "sources": [1008],
        "year_start": 1953,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Albert Pike": [991, 992, 993],
    "Manly P. Hall": [994, 995],
    "Licio Gelli": [996, 997, 1019],
    "Roberto Calvi": [999, 1000, 1001, 1002],
    "P.D. Houston": [1018],
    "Albert Mackey": [1010, 993],
    "William Donovan": [1004, 1005, 1007],
    "Scottish Rite Southern Jurisdiction": [991, 992, 993, 1015],
    "York Rite": [1009, 1017],
    "Propaganda Due": [996, 997, 998, 1019],
    "United Grand Lodge of England": [1008, 1011],
    "Grand Orient de France": [1012],
    "Shriners": [1016],
    "Sovereign Military Order of Malta": [1004, 1005, 1006],
    "Knights Templar": [1009, 1013, 1014],
    "P2 Lodge Scandal": [996, 997],
    "Calvi Murder": [999, 1000, 1001],
    "Banco Ambrosiano Collapse": [1002, 1003],
    "House of the Temple": [993, 1015],
}
