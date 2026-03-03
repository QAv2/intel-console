"""
Consciousness / Psi / Gateway — Expansion layer for Intel Console.

Maps the government programs that confirmed psi phenomena are real:
Project Stargate (CIA/DIA remote viewing), the Gateway Process (Army
Intelligence consciousness exploration), SRI International's psi research,
and the Monroe Institute. This is Line 2 suppression — the deliberate
burial of consciousness research that proved human capabilities beyond
the materialist paradigm.

The irony: the intelligence community spent decades proving psi works
while the scientific establishment they fund denies it exists.

Entities (~20): Key researchers/operatives (Ingo Swann, Hal Puthoff,
Russell Targ, Pat Price, Joe McMoneagle, Robert Monroe, Edwin May,
Dale Graff, Albert Stubblebine, Jim Channon), organizations (SRI
International, Monroe Institute, DIA), programs (Project Stargate,
Project Scangate, Project Grill Flame, Project Center Lane, Project
Sun Streak, Gateway Process), documents (Gateway Process Report).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], NSA [86], DARPA [90], Church Committee [338]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 741-770
# ============================================================

SOURCES = [
    # --- Stargate / Remote Viewing ---
    {
        "id": 741,
        "title": "CIA STAR GATE collection — 89,000+ declassified documents on remote viewing programs (FOIA)",
        "url": "https://www.cia.gov/readingroom/collection/stargate",
        "source_type": "government",
        "year": 1995,
    },
    {
        "id": 742,
        "title": "AIR (American Institutes for Research) — Evaluation of the Remote Viewing Program (final Stargate review)",
        "url": "https://irp.fas.org/program/collect/air1995.pdf",
        "source_type": "government",
        "year": 1995,
    },
    {
        "id": 743,
        "title": "DIA — Review of the Department of Defense's Project STARGATE (declassified 2000)",
        "url": "https://www.dia.mil/FOIA/FOIA-Electronic-Reading-Room/",
        "source_type": "government",
        "year": 1995,
    },
    # --- Gateway Process ---
    {
        "id": 744,
        "title": "Lt. Col. Wayne McDonnell — Analysis and Assessment of Gateway Process (U.S. Army Intelligence, 1983)",
        "url": "https://www.cia.gov/readingroom/docs/CIA-RDP96-00788R001700210016-5.pdf",
        "source_type": "government",
        "author": "Wayne M. McDonnell",
        "year": 1983,
    },
    {
        "id": 745,
        "title": "CIA Gateway Process Report — missing Page 25 controversy and later release",
        "url": "https://www.vice.com/en/article/7k9qag/how-to-escape-the-confines-of-time-and-space-according-to-the-cia",
        "source_type": "journalism",
        "year": 2021,
    },
    # --- SRI Research ---
    {
        "id": 746,
        "title": "Hal Puthoff & Russell Targ — 'Information Transmission Under Conditions of Sensory Shielding' (Nature, 1974)",
        "url": "https://www.nature.com/articles/251602a0",
        "source_type": "academic",
        "author": "Harold Puthoff, Russell Targ",
        "year": 1974,
    },
    {
        "id": 747,
        "title": "Russell Targ — The Reality of ESP: A Physicist's Proof of Psychic Abilities",
        "url": "https://en.wikipedia.org/wiki/Russell_Targ",
        "source_type": "academic",
        "author": "Russell Targ",
        "year": 2012,
    },
    {
        "id": 748,
        "title": "Hal Puthoff — 'CIA-Initiated Remote Viewing Program at Stanford Research Institute' (Journal of Scientific Exploration, 1996)",
        "url": "https://www.scientificexploration.org/docs/10/jse_10_1_puthoff.pdf",
        "source_type": "academic",
        "author": "Harold Puthoff",
        "year": 1996,
    },
    # --- Ingo Swann ---
    {
        "id": 749,
        "title": "Ingo Swann — 'Natural ESP: The ESP Core and Its Raw Characteristics' and SRI documentation",
        "url": "https://en.wikipedia.org/wiki/Ingo_Swann",
        "source_type": "other",
        "author": "Ingo Swann",
        "year": 1987,
    },
    {
        "id": 750,
        "title": "Ingo Swann — Penetration: The Question of Extraterrestrial and Human Telepathy",
        "url": "https://archive.org/details/penetration_202012",
        "source_type": "other",
        "author": "Ingo Swann",
        "year": 1998,
    },
    # --- Pat Price ---
    {
        "id": 751,
        "title": "Pat Price — SRI remote viewing of Soviet military installations (confirmed by satellite, declassified)",
        "url": "https://www.cia.gov/readingroom/collection/stargate",
        "source_type": "government",
        "year": 1974,
    },
    # --- Joe McMoneagle ---
    {
        "id": 752,
        "title": "Joseph McMoneagle — Mind Trek: Exploring Consciousness, Time, and Space Through Remote Viewing",
        "url": "https://en.wikipedia.org/wiki/Joseph_McMoneagle",
        "source_type": "other",
        "author": "Joseph McMoneagle",
        "year": 1993,
    },
    {
        "id": 753,
        "title": "Joseph McMoneagle — Remote Viewing Secrets: A Handbook",
        "url": "https://en.wikipedia.org/wiki/Joseph_McMoneagle",
        "source_type": "other",
        "author": "Joseph McMoneagle",
        "year": 2000,
    },
    # --- Monroe Institute ---
    {
        "id": 754,
        "title": "Robert Monroe — Journeys Out of the Body",
        "url": "https://en.wikipedia.org/wiki/Robert_Monroe",
        "source_type": "other",
        "author": "Robert Monroe",
        "year": 1971,
    },
    {
        "id": 755,
        "title": "Monroe Institute — official history and Hemi-Sync technology",
        "url": "https://www.monroeinstitute.org/",
        "source_type": "other",
        "year": 1974,
    },
    # --- Jim Schnabel / History ---
    {
        "id": 756,
        "title": "Jim Schnabel — Remote Viewers: The Secret History of America's Psychic Spies",
        "url": "https://en.wikipedia.org/wiki/Remote_Viewers_(book)",
        "source_type": "journalism",
        "author": "Jim Schnabel",
        "year": 1997,
    },
    # --- Annie Jacobsen ---
    {
        "id": 757,
        "title": "Annie Jacobsen — Phenomena: The Secret History of the U.S. Government's Investigations into Extrasensory Perception and Psychokinesis",
        "url": "https://en.wikipedia.org/wiki/Phenomena_(book)",
        "source_type": "journalism",
        "author": "Annie Jacobsen",
        "year": 2017,
    },
    # --- Albert Stubblebine ---
    {
        "id": 758,
        "title": "Major General Albert Stubblebine III — Army Intelligence commander who championed psychic warfare programs",
        "url": "https://en.wikipedia.org/wiki/Albert_Stubblebine",
        "source_type": "other",
        "year": 2017,
    },
    # --- Jim Channon ---
    {
        "id": 759,
        "title": "Lt. Col. Jim Channon — First Earth Battalion Operations Manual (1979)",
        "url": "https://en.wikipedia.org/wiki/First_Earth_Battalion",
        "source_type": "government",
        "author": "Jim Channon",
        "year": 1979,
    },
    {
        "id": 760,
        "title": "Jon Ronson — The Men Who Stare at Goats (2004, based on First Earth Battalion)",
        "url": "https://en.wikipedia.org/wiki/The_Men_Who_Stare_at_Goats",
        "source_type": "journalism",
        "author": "Jon Ronson",
        "year": 2004,
    },
    # --- Edwin May ---
    {
        "id": 761,
        "title": "Edwin May — 'The American Institutes for Research Review of the Department of Defense's STAR GATE Program: A Commentary' (JSE, 1996)",
        "url": "https://www.scientificexploration.org/docs/10/jse_10_1_may.pdf",
        "source_type": "academic",
        "author": "Edwin C. May",
        "year": 1996,
    },
    # --- Dale Graff ---
    {
        "id": 762,
        "title": "Dale Graff — Tracks in the Psychic Wilderness: An Exploration of ESP, Remote Viewing, and Synchronicity",
        "url": "https://en.wikipedia.org/wiki/Dale_Graff",
        "source_type": "other",
        "author": "Dale Graff",
        "year": 1998,
    },
    # --- DIA ---
    {
        "id": 763,
        "title": "DIA — Defense Intelligence Agency oversight of Project Stargate (1986-1995)",
        "url": "https://en.wikipedia.org/wiki/Stargate_Project",
        "source_type": "government",
        "year": 1995,
    },
    # --- Jessica Utts Statistical Analysis ---
    {
        "id": 764,
        "title": "Jessica Utts — 'An Assessment of the Evidence for Psychic Functioning' (statistical analysis for AIR review, 1995)",
        "url": "https://www.ics.uci.edu/~jutMDL/air.pdf",
        "source_type": "academic",
        "author": "Jessica Utts",
        "year": 1995,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Key Remote Viewers ---
    {
        "name": "Ingo Swann",
        "entity_type": "person",
        "description": "Artist and psychic researcher. Co-developed Coordinate Remote Viewing (CRV) protocol with Hal Puthoff at SRI. Demonstrated ability to influence magnetometer readings, describe Jupiter's rings before Voyager confirmed them. The most documented remote viewer in government records.",
        "aliases": "",
        "metadata": {"role": "remote viewer / researcher", "years_active": "1972-2013"},
    },
    {
        "name": "Hal Puthoff",
        "entity_type": "person",
        "description": "Physicist, former NSA officer. Co-founded SRI remote viewing program with Russell Targ. Published in Nature (1974). Later founded EarthTech International and served as advisor to AATIP/AAWSAP. Bridge between consciousness research and UAP programs.",
        "aliases": "Harold E. Puthoff",
        "metadata": {"role": "physicist / SRI program director", "years_active": "1972-present"},
    },
    {
        "name": "Russell Targ",
        "entity_type": "person",
        "description": "Physicist and laser pioneer. Co-founded SRI remote viewing program with Hal Puthoff. Published in Nature (1974). Conducted hundreds of remote viewing experiments with statistical significance confirmed by independent review (Jessica Utts, 1995).",
        "aliases": "",
        "metadata": {"role": "physicist / SRI co-director", "years_active": "1972-1995"},
    },
    {
        "name": "Pat Price",
        "entity_type": "person",
        "description": "Former police commissioner and natural remote viewer. At SRI, accurately described Soviet military installation at Semipalatinsk from coordinates alone — later confirmed by satellite imagery. Died suddenly in 1975 under circumstances some researchers find suspicious.",
        "aliases": "",
        "metadata": {"role": "remote viewer", "years_active": "1973-1975"},
    },
    {
        "name": "Joseph McMoneagle",
        "entity_type": "person",
        "description": "U.S. Army Chief Warrant Officer. 'Remote Viewer #001' — first and longest-serving military remote viewer in Project Stargate. Awarded Legion of Merit for intelligence contributions through remote viewing. Participated from inception through program termination.",
        "aliases": "Joe McMoneagle",
        "metadata": {"role": "military remote viewer", "years_active": "1978-1995"},
    },
    # --- Program Directors / Military ---
    {
        "name": "Edwin May",
        "entity_type": "person",
        "description": "Nuclear physicist who directed the SRI/SAIC remote viewing research program (1985-1995) after Puthoff and Targ. Conducted rigorous statistical analyses. Continued private research after program termination.",
        "aliases": "Ed May",
        "metadata": {"role": "program director / physicist", "years_active": "1975-1995"},
    },
    {
        "name": "Dale Graff",
        "entity_type": "person",
        "description": "DIA physicist who managed the Stargate program from the Defense Intelligence Agency side. Served as both project officer and director. Personally experienced and documented precognitive dreams. Wrote about the program after declassification.",
        "aliases": "",
        "metadata": {"role": "DIA program manager", "years_active": "1976-1993"},
    },
    {
        "name": "Albert Stubblebine",
        "entity_type": "person",
        "description": "Major General, Commanding General of U.S. Army Intelligence and Security Command (INSCOM). Championed psychic warfare capabilities including remote viewing and psychokinesis. Pushed for integration of psi capabilities into military intelligence operations.",
        "aliases": "Albert Stubblebine III",
        "metadata": {"role": "Army Intelligence commander", "years_active": "1981-1984"},
    },
    {
        "name": "Jim Channon",
        "entity_type": "person",
        "description": "Lt. Colonel who authored the 'First Earth Battalion Operations Manual' (1979) — a visionary document proposing warrior monks with psychic abilities, non-lethal weapons, and consciousness-based military operations. Inspired the book/film 'The Men Who Stare at Goats.'",
        "aliases": "",
        "metadata": {"role": "Army officer / visionary", "years_active": "1979-2017"},
    },
    # --- Robert Monroe ---
    {
        "name": "Robert Monroe",
        "entity_type": "person",
        "description": "Radio broadcasting executive who experienced spontaneous out-of-body experiences. Founded the Monroe Institute (1974). Developed Hemi-Sync audio technology for consciousness exploration. His work was adopted by U.S. Army Intelligence for the Gateway Process program.",
        "aliases": "Bob Monroe",
        "metadata": {"role": "consciousness researcher / Monroe Institute founder", "years_active": "1958-1995"},
    },
    # --- Organizations ---
    {
        "name": "SRI International",
        "entity_type": "organization",
        "description": "Stanford Research Institute (renamed SRI International 1977). Hosted CIA/DIA-funded remote viewing research from 1972-1990s. Puthoff, Targ, Swann, and Price conducted experiments there. Published in Nature. Research moved to SAIC in 1991.",
        "aliases": "Stanford Research Institute, SRI",
        "metadata": {"type": "research institute", "founded": 1946},
    },
    {
        "name": "Monroe Institute",
        "entity_type": "organization",
        "description": "Founded by Robert Monroe (1974) in Faber, Virginia. Develops audio-guidance technology (Hemi-Sync) for consciousness exploration. U.S. Army Intelligence sent personnel for Gateway training. The Gateway Process report (1983) described Monroe's techniques as enabling access to non-physical dimensions.",
        "aliases": "TMI",
        "metadata": {"type": "consciousness research", "founded": 1974},
    },
    {
        "name": "DIA",
        "entity_type": "agency",
        "description": "Defense Intelligence Agency. Managed Project Stargate (remote viewing) from 1986-1995 after taking over from CIA. Also commissioned the 38 DIRDs (Defense Intelligence Reference Documents) through AAWSAP, several covering consciousness and psi phenomena.",
        "aliases": "Defense Intelligence Agency",
        "metadata": {"type": "intelligence agency", "founded": 1961},
    },
    # --- Programs ---
    {
        "name": "Project Stargate",
        "entity_type": "program",
        "description": "Umbrella name for the U.S. government's remote viewing programs (1978-1995). Previously named Grill Flame, Center Lane, Sun Streak. CIA-initiated at SRI, later managed by DIA. 89,000+ declassified documents. AIR review statistician Jessica Utts confirmed results were statistically significant.",
        "aliases": "Stargate, Grill Flame, Center Lane, Sun Streak, Scangate",
        "metadata": {"type": "intelligence program", "years_active": "1978-1995"},
    },
    {
        "name": "Gateway Process",
        "entity_type": "program",
        "description": "U.S. Army Intelligence program using Monroe Institute's Hemi-Sync technology to achieve altered states of consciousness. Lt. Col. Wayne McDonnell's 1983 report described it as a system for transcending space-time via consciousness. The report went viral in 2021 after full FOIA release (including previously missing Page 25).",
        "aliases": "Gateway Experience",
        "metadata": {"type": "consciousness program", "years_active": "1983-present"},
    },
    {
        "name": "First Earth Battalion",
        "entity_type": "program",
        "description": "Visionary military concept proposed by Lt. Col. Jim Channon (1979). Envisioned 'warrior monks' with psychic abilities, non-lethal weapons, and consciousness-based operations. Partially implemented through Stubblebine's INSCOM programs. Basis for Jon Ronson's 'The Men Who Stare at Goats.'",
        "aliases": "",
        "metadata": {"type": "military concept", "years_active": "1979-1984"},
    },
    # --- Documents/Events ---
    {
        "name": "Gateway Process Report",
        "entity_type": "event",
        "description": "Lt. Col. Wayne McDonnell's 29-page classified analysis (1983) explaining how Monroe Institute techniques work through physics of consciousness. Describes holographic universe model, consciousness as frequency, and methods for transcending space-time. Went viral on social media after 2021 FOIA release.",
        "aliases": "McDonnell Report, CIA Gateway Report",
        "metadata": {"date": "1983-06-09"},
    },
    {
        "name": "Stargate Declassification",
        "entity_type": "event",
        "description": "CIA declassified Project Stargate in 1995. AIR review found: statistician Jessica Utts confirmed results showed statistical significance far beyond chance; skeptic Ray Hyman agreed the results were anomalous but proposed methodological critiques. CIA terminated the program despite positive results — transferred to 'no one.'",
        "aliases": "",
        "metadata": {"date": "1995-11-28"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- SRI Program ---
    {
        "source": "CIA",
        "target": "Project Stargate",
        "type": "operated",
        "tier": "documented",
        "desc": "CIA initiated and funded remote viewing research at SRI from 1972. 89,000+ documents declassified in 1995.",
        "sources": [741, 748],
        "year_start": 1972,
        "year_end": 1995,
    },
    {
        "source": "DIA",
        "target": "Project Stargate",
        "type": "operated",
        "tier": "documented",
        "desc": "DIA took over management of Stargate from CIA in 1986. Managed operational remote viewing unit until termination in 1995.",
        "sources": [741, 743, 763],
        "year_start": 1986,
        "year_end": 1995,
    },
    {
        "source": "Hal Puthoff",
        "target": "SRI International",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Co-directed SRI's remote viewing research program. Published in Nature (1974). Conducted hundreds of experiments over 20+ years.",
        "sources": [746, 748],
        "year_start": 1972,
        "year_end": 1985,
    },
    {
        "source": "Russell Targ",
        "target": "SRI International",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Co-directed SRI's remote viewing program with Puthoff. Physicist and laser pioneer. Published in Nature (1974).",
        "sources": [746, 747],
        "year_start": 1972,
        "year_end": 1982,
    },
    {
        "source": "Ingo Swann",
        "target": "SRI International",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Co-developed Coordinate Remote Viewing (CRV) protocol at SRI. Most documented remote viewer. Demonstrated abilities including magnetometer influence and Jupiter ring description.",
        "sources": [741, 749, 757],
        "year_start": 1972,
        "year_end": 1988,
    },
    {
        "source": "Ingo Swann",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Key participant who co-developed the CRV methodology that became the standard protocol for government remote viewing.",
        "sources": [741, 749],
        "year_start": 1972,
        "year_end": 1988,
    },
    {
        "source": "Pat Price",
        "target": "SRI International",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Natural remote viewer at SRI. Accurately described Soviet Semipalatinsk installation from coordinates — confirmed by satellite. Died suddenly 1975.",
        "sources": [751, 756],
        "year_start": 1973,
        "year_end": 1975,
    },
    {
        "source": "Joseph McMoneagle",
        "target": "Project Stargate",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Remote Viewer #001. Longest-serving military remote viewer. Awarded Legion of Merit for intelligence contributions via remote viewing.",
        "sources": [741, 752, 753],
        "year_start": 1978,
        "year_end": 1995,
    },
    {
        "source": "Edwin May",
        "target": "SRI International",
        "type": "directed",
        "tier": "documented",
        "desc": "Directed the remote viewing research program at SRI (1985-1990) and then SAIC (1990-1995) after Puthoff departed.",
        "sources": [761],
        "year_start": 1985,
        "year_end": 1995,
    },
    {
        "source": "Dale Graff",
        "target": "DIA",
        "type": "worked_for",
        "tier": "documented",
        "desc": "DIA physicist who managed Project Stargate from the intelligence consumer side. Both program officer and director.",
        "sources": [762, 763],
        "year_start": 1976,
        "year_end": 1993,
    },
    # --- Gateway Process ---
    {
        "source": "Robert Monroe",
        "target": "Monroe Institute",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded the Monroe Institute in 1974. Developed Hemi-Sync audio technology used in Gateway Process.",
        "sources": [754, 755],
        "year_start": 1974,
        "year_end": 1995,
    },
    {
        "source": "Monroe Institute",
        "target": "Gateway Process",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Monroe Institute's Hemi-Sync technology was the basis for the Army's Gateway Process program. Military personnel trained at TMI.",
        "sources": [744, 755],
        "year_start": 1983,
        "year_end": None,
    },
    {
        "source": "Albert Stubblebine",
        "target": "Gateway Process",
        "type": "authorized",
        "tier": "credible",
        "desc": "As INSCOM commander, championed consciousness-based military programs including Gateway training and psychic warfare research.",
        "sources": [758, 760],
        "year_start": 1981,
        "year_end": 1984,
    },
    {
        "source": "Albert Stubblebine",
        "target": "Project Stargate",
        "type": "connected_to",
        "tier": "credible",
        "desc": "As Army Intelligence commander, supported and expanded the military remote viewing program under his INSCOM authority.",
        "sources": [757, 758],
        "year_start": 1981,
        "year_end": 1984,
    },
    {
        "source": "Jim Channon",
        "target": "First Earth Battalion",
        "type": "created",
        "tier": "documented",
        "desc": "Authored the First Earth Battalion Operations Manual (1979) proposing warrior monks with psychic abilities.",
        "sources": [759, 760],
        "year_start": 1979,
        "year_end": 1979,
    },
    {
        "source": "Albert Stubblebine",
        "target": "First Earth Battalion",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Partially implemented Channon's vision through INSCOM programs including psychokinesis research and remote viewing.",
        "sources": [758, 760],
        "year_start": 1981,
        "year_end": 1984,
    },
    # --- Hal Puthoff / UAP Bridge ---
    {
        "source": "Hal Puthoff",
        "target": "NSA",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Former NSA officer before joining SRI. Bridge between signals intelligence and consciousness research.",
        "sources": [748, 757],
        "year_start": 1960,
        "year_end": 1972,
    },
    # --- Declassification ---
    {
        "source": "CIA",
        "target": "Stargate Declassification",
        "type": "connected_to",
        "tier": "documented",
        "desc": "CIA declassified Stargate in 1995 and terminated the program — despite statistician finding results were significant.",
        "sources": [741, 742],
        "year_start": 1995,
        "year_end": 1995,
    },
    # --- Gateway Report ---
    {
        "source": "DIA",
        "target": "Gateway Process Report",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Army Intelligence (INSCOM/DIA) commissioned the Gateway Process analysis. McDonnell report classified until FOIA release.",
        "sources": [744, 745],
        "year_start": 1983,
        "year_end": 1983,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Ingo Swann": [741, 749, 750, 757],
    "Hal Puthoff": [746, 748, 757],
    "Russell Targ": [746, 747],
    "Pat Price": [751, 756],
    "Joseph McMoneagle": [741, 752, 753],
    "Edwin May": [761],
    "Dale Graff": [762, 763],
    "Albert Stubblebine": [757, 758, 760],
    "Jim Channon": [759, 760],
    "Robert Monroe": [754, 755],
    "SRI International": [741, 746, 748],
    "Monroe Institute": [744, 754, 755],
    "DIA": [741, 743, 763],
    "Project Stargate": [741, 742, 743, 756, 757],
    "Gateway Process": [744, 745],
    "First Earth Battalion": [759, 760],
    "Gateway Process Report": [744, 745],
    "Stargate Declassification": [741, 742],
}
