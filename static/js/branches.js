/**
 * Intel Console — Branch Configuration & Entity Mapping
 *
 * Maps all entities to 7 thematic branches with ring assignments.
 * Ring 1 = key figures (closest to center)
 * Ring 2 = supporting figures/orgs
 * Ring 3 = peripheral entities
 */

const BRANCHES = {
    political:       { label: 'Political & Government',  color: '#a63d40', angle: 0 },
    financial:       { label: 'Financial & Corporate',    color: '#b8763a', angle: 51.4 },
    hollywood:       { label: 'Hollywood & Media',        color: '#4a8a8a', angle: 102.9 },
    inner_circle:    { label: 'Inner Circle & Enablers',  color: '#7a5aa0', angle: 154.3 },
    organized_crime: { label: 'Organized Crime',          color: '#f87171', angle: 205.7 },
    intelligence:    { label: 'Intelligence & Covert',    color: '#4a7c9b', angle: 257.1 },
    legal:           { label: 'Legal & Judicial',          color: '#94a3b8', angle: 308.6 },
};

const CENTER_ENTITY_ID = 1; // Jeffrey Epstein

// entity_id → { branch, ring }
const ENTITY_BRANCH_MAP = {
    // ---- POLITICAL & GOVERNMENT ----
    // Ring 1: key political figures with direct Epstein ties
    32:  { branch: 'political', ring: 1 },  // Bill Clinton
    33:  { branch: 'political', ring: 1 },  // Donald Trump
    108: { branch: 'political', ring: 1 },  // Prince Andrew
    8:   { branch: 'political', ring: 1 },  // William Barr
    // Ring 2: politically connected, significant ties
    38:  { branch: 'political', ring: 2 },  // Alan Dershowitz
    37:  { branch: 'political', ring: 2 },  // Alexander Acosta
    5:   { branch: 'political', ring: 2 },  // Ehud Barak
    111: { branch: 'political', ring: 2 },  // Henry Kissinger
    113: { branch: 'political', ring: 2 },  // Rudy Giuliani
    // Ring 3: peripheral political entities
    31:  { branch: 'political', ring: 3 },  // Hillary Clinton
    112: { branch: 'political', ring: 3 },  // Larry Summers
    109: { branch: 'political', ring: 3 },  // Bill Richardson
    110: { branch: 'political', ring: 3 },  // George Mitchell
    114: { branch: 'political', ring: 3 },  // Sandy Berger
    29:  { branch: 'political', ring: 3 },  // John Poindexter
    75:  { branch: 'political', ring: 3 },  // Mar-a-Lago
    115: { branch: 'political', ring: 3 },  // Kissinger Associates
    117: { branch: 'political', ring: 3 },  // Prince Andrew Civil Settlement
    118: { branch: 'political', ring: 3 },  // Berger Archives Theft

    // ---- FINANCIAL & CORPORATE ----
    // Ring 1: core financial enablers
    4:   { branch: 'financial', ring: 1 },  // Les Wexner
    30:  { branch: 'financial', ring: 1 },  // Leon Black
    125: { branch: 'financial', ring: 1 },  // Steven Hoffenberg
    124: { branch: 'financial', ring: 1 },  // Jes Staley
    // Ring 2: major financial connections
    119: { branch: 'financial', ring: 2 },  // Charles Bronfman
    120: { branch: 'financial', ring: 2 },  // Edgar Bronfman Sr.
    122: { branch: 'financial', ring: 2 },  // Michael Steinhardt
    123: { branch: 'financial', ring: 2 },  // Glenn Dubin
    126: { branch: 'financial', ring: 2 },  // Lynn Forester de Rothschild
    129: { branch: 'financial', ring: 2 },  // Tom Barrack
    121: { branch: 'financial', ring: 2 },  // Ronald Lauder
    // Ring 3: peripheral financial entities
    6:   { branch: 'financial', ring: 3 },  // Peter Thiel
    7:   { branch: 'financial', ring: 3 },  // Alex Karp
    127: { branch: 'financial', ring: 3 },  // Mort Zuckerman
    128: { branch: 'financial', ring: 3 },  // Steve Bing
    56:  { branch: 'financial', ring: 3 },  // JPMorgan Chase
    57:  { branch: 'financial', ring: 3 },  // Deutsche Bank
    58:  { branch: 'financial', ring: 3 },  // Bear Stearns
    65:  { branch: 'financial', ring: 3 },  // The Limited
    66:  { branch: 'financial', ring: 3 },  // Mega Group
    68:  { branch: 'financial', ring: 3 },  // Wexner Foundation
    69:  { branch: 'financial', ring: 3 },  // Apollo Global Management
    71:  { branch: 'financial', ring: 3 },  // Glencore
    130: { branch: 'financial', ring: 3 },  // Towers Financial
    131: { branch: 'financial', ring: 3 },  // Seagram
    132: { branch: 'financial', ring: 3 },  // Birthright Israel
    133: { branch: 'financial', ring: 3 },  // Colony Capital

    // ---- HOLLYWOOD & MEDIA ----
    // Ring 1: directly tied to Epstein's social/media network
    134: { branch: 'hollywood', ring: 1 },  // Harvey Weinstein
    135: { branch: 'hollywood', ring: 1 },  // Jean-Luc Brunel
    // Ring 2: significant media/entertainment connections
    136: { branch: 'hollywood', ring: 2 },  // Kevin Spacey
    137: { branch: 'hollywood', ring: 2 },  // Woody Allen
    138: { branch: 'hollywood', ring: 2 },  // Naomi Campbell
    139: { branch: 'hollywood', ring: 2 },  // Ari Emanuel
    140: { branch: 'hollywood', ring: 2 },  // Les Moonves
    // Ring 3: orgs and events
    141: { branch: 'hollywood', ring: 3 },  // MC2 Model Management
    142: { branch: 'hollywood', ring: 3 },  // Black Cube
    143: { branch: 'hollywood', ring: 3 },  // Victoria's Secret
    116: { branch: 'hollywood', ring: 3 },  // Hollinger International
    144: { branch: 'hollywood', ring: 3 },  // Jean-Luc Brunel Death

    // ---- INNER CIRCLE & ENABLERS ----
    // Ring 1: closest associates
    2:   { branch: 'inner_circle', ring: 1 },  // Ghislaine Maxwell
    145: { branch: 'inner_circle', ring: 1 },  // Virginia Giuffre
    146: { branch: 'inner_circle', ring: 1 },  // Maria Farmer
    // Ring 2: key enablers and associates
    148: { branch: 'inner_circle', ring: 2 },  // Sarah Kellen
    149: { branch: 'inner_circle', ring: 2 },  // Nadia Marcinkova
    150: { branch: 'inner_circle', ring: 2 },  // Lesley Groff
    151: { branch: 'inner_circle', ring: 2 },  // Nicole Junkermann
    147: { branch: 'inner_circle', ring: 2 },  // Courtney Wild
    152: { branch: 'inner_circle', ring: 2 },  // Eva Andersson-Dubin
    153: { branch: 'inner_circle', ring: 2 },  // Celina Midelfart
    // Ring 3: locations, orgs, events
    67:  { branch: 'inner_circle', ring: 3 },  // Carbyne
    154: { branch: 'inner_circle', ring: 3 },  // Dalton School
    76:  { branch: 'inner_circle', ring: 3 },  // Little Saint James
    155: { branch: 'inner_circle', ring: 3 },  // Zorro Ranch
    156: { branch: 'inner_circle', ring: 3 },  // 9 East 71st Street
    157: { branch: 'inner_circle', ring: 3 },  // MCC New York
    102: { branch: 'inner_circle', ring: 3 },  // Epstein Death
    158: { branch: 'inner_circle', ring: 3 },  // Epstein Palm Beach Investigation
    159: { branch: 'inner_circle', ring: 3 },  // Maxwell Trial

    // ---- ORGANIZED CRIME ----
    // Ring 1: key mob figures connected to Epstein's world
    11:  { branch: 'organized_crime', ring: 1 },  // Roy Cohn
    18:  { branch: 'organized_crime', ring: 1 },  // Meyer Lansky
    34:  { branch: 'organized_crime', ring: 1 },  // Fat Tony Salerno
    // Ring 2: significant crime figures
    39:  { branch: 'organized_crime', ring: 2 },  // John Gotti
    35:  { branch: 'organized_crime', ring: 2 },  // Paul Castellano
    45:  { branch: 'organized_crime', ring: 2 },  // Lucky Luciano
    41:  { branch: 'organized_crime', ring: 2 },  // Nicky Scarfo
    36:  { branch: 'organized_crime', ring: 2 },  // Felix Sater
    50:  { branch: 'organized_crime', ring: 2 },  // Kenneth Shapiro
    // Ring 3: peripheral mob entities
    40:  { branch: 'organized_crime', ring: 3 },  // Angelo Bruno
    42:  { branch: 'organized_crime', ring: 3 },  // John Stanfa
    43:  { branch: 'organized_crime', ring: 3 },  // Joey Merlino
    44:  { branch: 'organized_crime', ring: 3 },  // John-John Veasey
    46:  { branch: 'organized_crime', ring: 3 },  // Bugsy Siegel
    47:  { branch: 'organized_crime', ring: 3 },  // Sammy Gravano
    48:  { branch: 'organized_crime', ring: 3 },  // Frankie Carbo
    49:  { branch: 'organized_crime', ring: 3 },  // Blinky Palermo
    51:  { branch: 'organized_crime', ring: 3 },  // Salvatore Testa
    52:  { branch: 'organized_crime', ring: 3 },  // Robert LiButti
    73:  { branch: 'organized_crime', ring: 3 },  // Bayrock Group
    74:  { branch: 'organized_crime', ring: 3 },  // Resorts International
    77:  { branch: 'organized_crime', ring: 3 },  // The Commission
    78:  { branch: 'organized_crime', ring: 3 },  // Gambino Crime Family
    79:  { branch: 'organized_crime', ring: 3 },  // Genovese Crime Family
    80:  { branch: 'organized_crime', ring: 3 },  // Lucchese Crime Family
    81:  { branch: 'organized_crime', ring: 3 },  // Philadelphia Crime Family
    82:  { branch: 'organized_crime', ring: 3 },  // Murder Incorporated
    83:  { branch: 'organized_crime', ring: 3 },  // Scarf Inc
    84:  { branch: 'organized_crime', ring: 3 },  // S&A Concrete
    106: { branch: 'organized_crime', ring: 3 },  // Commission Trial
    107: { branch: 'organized_crime', ring: 3 },  // Castellano Assassination

    // ---- INTELLIGENCE & COVERT ----
    // Ring 1: primary intelligence figures
    3:   { branch: 'intelligence', ring: 1 },  // Robert Maxwell
    10:  { branch: 'intelligence', ring: 1 },  // William Casey
    85:  { branch: 'intelligence', ring: 1 },  // CIA
    88:  { branch: 'intelligence', ring: 1 },  // Mossad
    // Ring 2: significant intelligence actors
    14:  { branch: 'intelligence', ring: 2 },  // Edwin Wilson
    15:  { branch: 'intelligence', ring: 2 },  // Frank Terpil
    16:  { branch: 'intelligence', ring: 2 },  // J. Edgar Hoover
    17:  { branch: 'intelligence', ring: 2 },  // James Angleton
    53:  { branch: 'intelligence', ring: 2 },  // Rafi Eitan
    87:  { branch: 'intelligence', ring: 2 },  // FBI
    28:  { branch: 'intelligence', ring: 2 },  // Richard Helms
    27:  { branch: 'intelligence', ring: 2 },  // Adnan Khashoggi
    // Ring 3: peripheral intelligence entities
    9:   { branch: 'intelligence', ring: 3 },  // Donald Barr
    12:  { branch: 'intelligence', ring: 3 },  // Robert Keith Gray
    13:  { branch: 'intelligence', ring: 3 },  // Craig Spence
    19:  { branch: 'intelligence', ring: 3 },  // Kamal Adham
    20:  { branch: 'intelligence', ring: 3 },  // Agha Hasan Abedi
    24:  { branch: 'intelligence', ring: 3 },  // Barry Seal
    25:  { branch: 'intelligence', ring: 3 },  // Bill Hamilton
    26:  { branch: 'intelligence', ring: 3 },  // Danny Casolaro
    54:  { branch: 'intelligence', ring: 3 },  // BCCI
    55:  { branch: 'intelligence', ring: 3 },  // First American Bank
    59:  { branch: 'intelligence', ring: 3 },  // Palantir Technologies
    60:  { branch: 'intelligence', ring: 3 },  // In-Q-Tel
    61:  { branch: 'intelligence', ring: 3 },  // Hill & Knowlton
    63:  { branch: 'intelligence', ring: 3 },  // Systematics
    64:  { branch: 'intelligence', ring: 3 },  // Southern Air Transport
    70:  { branch: 'intelligence', ring: 3 },  // CAPCOM
    72:  { branch: 'intelligence', ring: 3 },  // George Town Club
    86:  { branch: 'intelligence', ring: 3 },  // NSA
    90:  { branch: 'intelligence', ring: 3 },  // DARPA
    91:  { branch: 'intelligence', ring: 3 },  // PROMIS
    92:  { branch: 'intelligence', ring: 3 },  // Main Core
    93:  { branch: 'intelligence', ring: 3 },  // Total Information Awareness
    94:  { branch: 'intelligence', ring: 3 },  // MKULTRA
    95:  { branch: 'intelligence', ring: 3 },  // COINTELPRO
    96:  { branch: 'intelligence', ring: 3 },  // Iran-Contra
    97:  { branch: 'intelligence', ring: 3 },  // Operation Midnight Climax
    98:  { branch: 'intelligence', ring: 3 },  // LifeLog
    99:  { branch: 'intelligence', ring: 3 },  // BCCI Shutdown
    103: { branch: 'intelligence', ring: 3 },  // Danny Casolaro Death
    104: { branch: 'intelligence', ring: 3 },  // Robert Maxwell Death

    // ---- LEGAL & JUDICIAL ----
    // Ring 1: key legal/institutional entities
    89:  { branch: 'legal', ring: 1 },  // DOJ
    62:  { branch: 'legal', ring: 1 },  // Rose Law Firm
    // Ring 2: major legal events
    100: { branch: 'legal', ring: 2 },  // Epstein NPA (2007)
    101: { branch: 'legal', ring: 2 },  // Epstein Arrest (2019)
    105: { branch: 'legal', ring: 2 },  // Wexner House Oversight Deposition
    // Ring 3: peripheral legal entities
    21:  { branch: 'legal', ring: 3 },  // Clark Clifford
    22:  { branch: 'legal', ring: 3 },  // Marc Rich
    23:  { branch: 'legal', ring: 3 },  // Jackson Stephens

    // ---- RUSSIA / PUTIN EXPANSION ----
    // Political & Government
    160: { branch: 'political', ring: 2 },  // Vladimir Putin
    // Intelligence & Covert
    161: { branch: 'intelligence', ring: 2 },  // FSB
    // Organized Crime
    162: { branch: 'organized_crime', ring: 2 },  // Semion Mogilevich
    163: { branch: 'organized_crime', ring: 3 },  // Solntsevskaya Bratva
    // Financial & Corporate
    164: { branch: 'financial', ring: 2 },  // Dmitry Rybolovlev

    // ---- CHINA EXPANSION ----
    // Political & Government — Chinagate campaign finance actors
    165: { branch: 'political', ring: 2 },  // Johnny Chung
    166: { branch: 'political', ring: 2 },  // John Huang
    167: { branch: 'political', ring: 3 },  // Charlie Trie
    // Financial & Corporate — tech transfer / China business
    168: { branch: 'financial', ring: 2 },  // Bernard Schwartz
    // Political & Government — PLA intelligence actor
    169: { branch: 'political', ring: 3 },  // Liu Chaoying
    // Financial & Corporate — CITIC/Poly chairman, China business
    170: { branch: 'financial', ring: 3 },  // Wang Jun
    171: { branch: 'financial', ring: 2 },  // Desmond Shum
    // Intelligence & Covert — Chinese intelligence apparatus
    172: { branch: 'intelligence', ring: 2 },  // MSS
    173: { branch: 'intelligence', ring: 3 },  // CITIC Group
    // Financial & Corporate — Riady family conglomerate
    174: { branch: 'financial', ring: 3 },  // Lippo Group
    // Legal & Judicial — investigation events
    175: { branch: 'legal', ring: 3 },  // Cox Report (1999)

    // ---- SAUDI / GULF EXPANSION ----
    // Political & Government — Saudi royals and heads of state
    176: { branch: 'political', ring: 2 },  // Prince Bandar bin Sultan
    177: { branch: 'intelligence', ring: 2 },  // Prince Turki al-Faisal
    // Intelligence & Covert — Saudi intelligence apparatus
    178: { branch: 'intelligence', ring: 2 },  // Saudi GID
    // Political & Government — current Saudi leadership
    179: { branch: 'political', ring: 2 },  // Mohammed bin Salman
    // Intelligence & Covert — journalist with intel connections
    180: { branch: 'intelligence', ring: 3 },  // Jamal Khashoggi
    // Financial & Corporate — Saudi billionaire investor
    181: { branch: 'financial', ring: 2 },  // Al-Waleed bin Talal
    182: { branch: 'financial', ring: 3 },  // Kingdom Holding
    // Financial & Corporate — Saudi construction/investment
    183: { branch: 'financial', ring: 3 },  // Saudi Binladin Group
    184: { branch: 'financial', ring: 2 },  // Carlyle Group
    // Intelligence & Covert — arms deal / slush fund
    185: { branch: 'intelligence', ring: 3 },  // BAE Al-Yamamah Deal
    186: { branch: 'intelligence', ring: 3 },  // Safari Club
    // Intelligence & Covert — arms deal intermediary
    187: { branch: 'intelligence', ring: 3 },  // Wafic Said
    // Financial & Corporate — Saudi royal financial networks
    188: { branch: 'financial', ring: 3 },  // Prince Mohammed bin Fahd

    // ---- UK EXPANSION ----
    // Political & Government — Epstein's key UK political associate
    189: { branch: 'political', ring: 2 },  // Peter Mandelson
    // Intelligence & Covert — UK intelligence agencies
    190: { branch: 'intelligence', ring: 2 },  // MI5
    191: { branch: 'intelligence', ring: 1 },  // MI6
    // Inner Circle & Enablers — establishment protection pattern
    192: { branch: 'inner_circle', ring: 2 },  // Jimmy Savile
    // Political & Government — royal family connection
    193: { branch: 'political', ring: 3 },  // Sarah Ferguson
    // Legal & Judicial — UK law enforcement and prosecution
    194: { branch: 'legal', ring: 2 },  // Metropolitan Police
    197: { branch: 'legal', ring: 2 },  // Crown Prosecution Service
    // Intelligence & Covert — Maxwell media/intelligence infrastructure
    195: { branch: 'intelligence', ring: 3 },  // Pergamon Press
    196: { branch: 'intelligence', ring: 3 },  // Mirror Group Newspapers
    // Hollywood & Media — BBC leadership during Savile cover-up
    198: { branch: 'hollywood', ring: 3 },  // Mark Thompson
    // Inner Circle & Enablers — named in unsealed documents
    199: { branch: 'inner_circle', ring: 3 },  // Stuart Roffey
    // Intelligence & Covert — media-intelligence nexus (Maxwell parallel)
    200: { branch: 'intelligence', ring: 3 },  // Evgeny Lebedev
    // Inner Circle & Enablers — Maxwell's ocean charity cover
    201: { branch: 'inner_circle', ring: 3 },  // TerraMar Project
    // Political & Government — key event: Andrew's public accounting
    202: { branch: 'political', ring: 3 },  // Newsnight Interview

    // ---- ISRAEL (DEEPER) EXPANSION ----
    // Intelligence & Covert — key Mossad/Aman whistleblower
    203: { branch: 'intelligence', ring: 2 },  // Ari Ben-Menashe
    // Intelligence & Covert — most damaging spy for a U.S. ally
    204: { branch: 'intelligence', ring: 2 },  // Jonathan Pollard
    // Intelligence & Covert — Israeli scientific intelligence agency
    205: { branch: 'intelligence', ring: 2 },  // LAKAM
    // Intelligence & Covert — Israeli SIGINT / surveillance tech pipeline
    206: { branch: 'intelligence', ring: 2 },  // Unit 8200
    // Intelligence & Covert — privatized surveillance (Pegasus)
    207: { branch: 'intelligence', ring: 3 },  // NSO Group
    // Intelligence & Covert — Mossad director during Maxwell collapse
    208: { branch: 'intelligence', ring: 3 },  // Shabtai Shavit
    // Intelligence & Covert — Mossad director / Black Cube honorary president
    209: { branch: 'intelligence', ring: 2 },  // Meir Dagan
    // Intelligence & Covert — Mossad director / Black Cube board
    210: { branch: 'intelligence', ring: 3 },  // Efraim Halevy

    // ---- BOHEMIAN GROVE EXPANSION ----
    // Political & Government — Presidents (Ring 2: powerful but no direct Epstein ties)
    211: { branch: 'political', ring: 2 },  // Ronald Reagan
    212: { branch: 'political', ring: 2 },  // George H.W. Bush
    213: { branch: 'political', ring: 2 },  // George W. Bush
    // Political & Government — Cabinet / VP
    214: { branch: 'political', ring: 2 },  // Dick Cheney
    215: { branch: 'political', ring: 3 },  // Donald Rumsfeld
    216: { branch: 'political', ring: 3 },  // Colin Powell
    217: { branch: 'political', ring: 3 },  // Caspar Weinberger
    218: { branch: 'political', ring: 3 },  // George Shultz
    219: { branch: 'political', ring: 3 },  // Edwin Meese
    // Financial & Corporate — Fed / finance / dark money
    220: { branch: 'financial', ring: 2 },  // Alan Greenspan
    221: { branch: 'political', ring: 3 },  // Edwin Fuelner
    222: { branch: 'political', ring: 3 },  // Joseph Coors Sr
    223: { branch: 'financial', ring: 2 },  // Charles Koch
    // Legal & Judicial — Supreme Court / judicial corruption
    224: { branch: 'legal', ring: 2 },  // Harlan Crow
    225: { branch: 'legal', ring: 2 },  // Clarence Thomas
    // Political & Government — current power
    226: { branch: 'political', ring: 3 },  // David McCormick
    // Financial & Corporate — Bechtel dynasty
    227: { branch: 'financial', ring: 3 },  // Steven Bechtel Sr
    228: { branch: 'financial', ring: 3 },  // Brendan Bechtel
    229: { branch: 'financial', ring: 2 },  // Michael Bloomberg
    // Organizations
    230: { branch: 'political', ring: 2 },  // Bohemian Club
    231: { branch: 'political', ring: 2 },  // Heritage Foundation
    232: { branch: 'financial', ring: 2 },  // Bechtel Corporation
    // Events
    233: { branch: 'political', ring: 3 },  // Project 2025
    234: { branch: 'political', ring: 3 },  // Social Security Reform 1983

    // ---- FRANCE EXPANSION ----
    // Hollywood & Media — Paris modeling industry figures
    235: { branch: 'hollywood', ring: 2 },  // Gérald Marie
    236: { branch: 'hollywood', ring: 2 },  // John Casablancas
    237: { branch: 'hollywood', ring: 2 },  // Eileen Ford
    238: { branch: 'hollywood', ring: 3 },  // Claude Haddad
    // Political & Government — French Culture Minister under investigation
    239: { branch: 'political', ring: 3 },  // Jack Lang
    // Hollywood & Media — modeling agencies
    240: { branch: 'hollywood', ring: 2 },  // Elite Model Management
    241: { branch: 'hollywood', ring: 2 },  // Karin Models
    // Intelligence & Covert — French intelligence (initiated Safari Club)
    242: { branch: 'intelligence', ring: 3 },  // DGSE
    // Inner Circle & Enablers — Epstein property
    243: { branch: 'inner_circle', ring: 2 },  // 22 Avenue Foch
    // Legal & Judicial — French investigation
    244: { branch: 'legal', ring: 2 },  // French Epstein Investigation

    // ---- GERMANY EXPANSION ----
    // Financial & Corporate — Deutsche Bank personnel
    245: { branch: 'financial', ring: 2 },  // Thomas Bowers
    246: { branch: 'financial', ring: 3 },  // Rosemary Vrablic
    247: { branch: 'financial', ring: 3 },  // Tammy McFadden (whistleblower)
    248: { branch: 'financial', ring: 3 },  // William Broeksmit
    249: { branch: 'financial', ring: 3 },  // Val Broeksmit (whistleblower)
    // Intelligence & Covert — German intelligence + Scholz aide in Epstein files
    250: { branch: 'intelligence', ring: 3 },  // Philippa Sigl-Glöckner
    251: { branch: 'intelligence', ring: 2 },  // BND
    // Legal & Judicial — regulatory enforcement
    252: { branch: 'legal', ring: 2 },  // DFS Deutsche Bank Consent Order (2020)
    253: { branch: 'legal', ring: 3 },  // Deutsche Bank Russian Mirror Trading

    // ---- LATIN AMERICA EXPANSION ----
    // Political & Government — Iran-Contra principals
    254: { branch: 'political', ring: 2 },  // Oliver North
    // Intelligence & Covert — CIA assets and operatives
    255: { branch: 'intelligence', ring: 2 },  // Manuel Noriega
    256: { branch: 'intelligence', ring: 2 },  // Felix Rodriguez
    257: { branch: 'political', ring: 3 },  // Augusto Pinochet
    // Hollywood & Media — investigative journalist
    258: { branch: 'hollywood', ring: 3 },  // Gary Webb
    // Political & Government — Colombian president in Epstein files
    259: { branch: 'political', ring: 2 },  // Andres Pastrana
    // Organized Crime — drug cartel
    260: { branch: 'organized_crime', ring: 2 },  // Medellín Cartel
    // Intelligence & Covert — drug trafficker / CIA Contra airline
    261: { branch: 'intelligence', ring: 3 },  // SETCO Aviation
    262: { branch: 'intelligence', ring: 3 },  // School of the Americas
    263: { branch: 'intelligence', ring: 2 },  // Operation Condor
    // Legal & Judicial — Senate investigation
    264: { branch: 'legal', ring: 2 },  // Kerry Committee Investigation
};
