"""
9/11 Structural — Expansion layer for Intel Console.

Maps the 9/11 event complex: the attack itself, the intelligence failures
(or deliberate stand-down), the Saudi connections revealed in the 28 Pages,
the neoconservative policy apparatus (PNAC) that anticipated and exploited it,
the surveillance state it enabled, and the investigation that was designed
to not ask the hard questions.

Entities (~22): Key actors (bin Laden, KSM, Atta, al-Hazmi, al-Mihdhar),
intelligence officials (Tenet, Clarke, Rice), investigation (9/11 Commission,
Zelikow), whistleblowers (Edmonds, Bob Graham), policy architects (PNAC),
programs (Able Danger, Stellar Wind), legislation (PATRIOT Act, AUMF),
facilities (WTC, Pentagon).

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], NSA [86], FBI [87], George W. Bush [243],
  Dick Cheney [244], Donald Rumsfeld [245], Colin Powell [246],
  Prince Bandar bin Sultan [168], Saudi GID [170], Carlyle Group [176],
  Saudi Binladin Group [175], George H.W. Bush [242]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 626-660
# ============================================================

SOURCES = [
    # --- 9/11 Commission ---
    {
        "id": 626,
        "title": "The 9/11 Commission Report — Final Report of the National Commission on Terrorist Attacks Upon the United States",
        "url": "https://www.9-11commission.gov/report/911Report.pdf",
        "source_type": "government",
        "year": 2004,
    },
    {
        "id": 627,
        "title": "Joint Inquiry Into Intelligence Community Activities Before and After the Terrorist Attacks of September 11, 2001 — '28 Pages' (declassified 2016)",
        "url": "https://intelligence.house.gov/sites/intelligence.house.gov/files/documents/declasspart4.pdf",
        "source_type": "congressional",
        "year": 2016,
    },
    # --- NIST Reports ---
    {
        "id": 628,
        "title": "NIST NCSTAR 1 — Final Report on the Collapse of the World Trade Center Towers",
        "url": "https://www.nist.gov/publications/final-report-collapse-world-trade-center-towers",
        "source_type": "government",
        "year": 2005,
    },
    {
        "id": 629,
        "title": "NIST NCSTAR 1A — Final Report on the Collapse of World Trade Center Building 7",
        "url": "https://www.nist.gov/publications/final-report-collapse-world-trade-center-building-7",
        "source_type": "government",
        "year": 2008,
    },
    {
        "id": 630,
        "title": "University of Alaska Fairbanks — A Structural Reevaluation of the Collapse of World Trade Center 7 (Hulsey et al.)",
        "url": "https://ine.uaf.edu/wtc7",
        "source_type": "academic",
        "author": "J. Leroy Hulsey et al.",
        "year": 2020,
    },
    # --- PNAC ---
    {
        "id": 631,
        "title": "PNAC — Rebuilding America's Defenses: Strategy, Forces and Resources For a New Century",
        "url": "https://web.archive.org/web/20130730120521/http://www.newamericancentury.org/RebsuildingAmericasDefenses.pdf",
        "source_type": "other",
        "year": 2000,
    },
    # --- Key Books ---
    {
        "id": 632,
        "title": "Richard Clarke — Against All Enemies: Inside America's War on Terror",
        "url": "https://en.wikipedia.org/wiki/Against_All_Enemies",
        "source_type": "journalism",
        "author": "Richard A. Clarke",
        "year": 2004,
    },
    {
        "id": 633,
        "title": "Philip Shenon — The Commission: The Uncensored History of the 9/11 Investigation",
        "url": "https://en.wikipedia.org/wiki/The_Commission_(Shenon_book)",
        "source_type": "journalism",
        "author": "Philip Shenon",
        "year": 2008,
    },
    {
        "id": 634,
        "title": "Bob Graham — Intelligence Matters: The CIA, the FBI, Saudi Arabia, and the Failure of America's War on Terror",
        "url": "https://en.wikipedia.org/wiki/Bob_Graham",
        "source_type": "journalism",
        "author": "Bob Graham",
        "year": 2004,
    },
    {
        "id": 635,
        "title": "Sibel Edmonds — Classified Woman: The Sibel Edmonds Story",
        "url": "https://en.wikipedia.org/wiki/Sibel_Edmonds",
        "source_type": "journalism",
        "author": "Sibel Edmonds",
        "year": 2012,
    },
    {
        "id": 636,
        "title": "Anthony Summers & Robbyn Swan — The Eleventh Day: The Full Story of 9/11",
        "url": "https://en.wikipedia.org/wiki/The_Eleventh_Day",
        "source_type": "journalism",
        "author": "Anthony Summers",
        "year": 2011,
    },
    # --- Able Danger ---
    {
        "id": 637,
        "title": "Rep. Curt Weldon — Able Danger congressional testimony and floor speech",
        "url": "https://en.wikipedia.org/wiki/Able_Danger",
        "source_type": "congressional",
        "year": 2005,
    },
    # --- Stellar Wind / NSA Surveillance ---
    {
        "id": 638,
        "title": "James Risen & Eric Lichtblau — Bush Lets U.S. Spy on Callers Without Courts (New York Times)",
        "url": "https://www.nytimes.com/2005/12/16/politics/bush-lets-us-spy-on-callers-without-courts.html",
        "source_type": "journalism",
        "author": "James Risen, Eric Lichtblau",
        "year": 2005,
    },
    # --- Saudi Connections ---
    {
        "id": 639,
        "title": "FBI documents on Saudi embassy payments to 9/11 hijackers (released via FOIA lawsuit by 9/11 families)",
        "url": "https://www.floridabulldog.org/2021/09/fbi-documents-point-to-saudi-hand-behind-9-11/",
        "source_type": "government",
        "year": 2021,
    },
    {
        "id": 640,
        "title": "Princess Haifa (wife of Prince Bandar) payments to al-Bayoumi — 28 Pages and FBI investigation",
        "url": "https://en.wikipedia.org/wiki/Alleged_Saudi_role_in_September_11_attacks",
        "source_type": "congressional",
        "year": 2016,
    },
    # --- CIA Tracking of Hijackers ---
    {
        "id": 641,
        "title": "CIA tracking of al-Mihdhar and al-Hazmi — Kuala Lumpur meeting surveillance (DOJ IG report)",
        "url": "https://oig.justice.gov/sites/default/files/archive/special/s0606/final.pdf",
        "source_type": "government",
        "year": 2004,
    },
    # --- Zelikow Conflicts ---
    {
        "id": 642,
        "title": "Philip Zelikow conflicts of interest — pre-9/11 memo on catastrophic terrorism, co-author with Rice",
        "url": "https://en.wikipedia.org/wiki/Philip_D._Zelikow",
        "source_type": "other",
        "year": 2004,
    },
    # --- Pentagon Accounting ---
    {
        "id": 643,
        "title": "Donald Rumsfeld announces $2.3 trillion in untracked Pentagon transactions — DoD news briefing (Sep 10, 2001)",
        "url": "https://web.archive.org/web/20020305205839/http://www.defenselink.mil/speeches/2001/s20010910-secdef.html",
        "source_type": "government",
        "year": 2001,
    },
    # --- PATRIOT Act / AUMF ---
    {
        "id": 644,
        "title": "USA PATRIOT Act — Public Law 107-56 (signed Oct 26, 2001)",
        "url": "https://www.congress.gov/107/plaws/publ56/PLAW-107publ56.htm",
        "source_type": "government",
        "year": 2001,
    },
    {
        "id": 645,
        "title": "Authorization for Use of Military Force — Public Law 107-40 (signed Sep 18, 2001)",
        "url": "https://www.congress.gov/107/plaws/publ40/PLAW-107publ40.htm",
        "source_type": "government",
        "year": 2001,
    },
    # --- Moussaoui Trial ---
    {
        "id": 646,
        "title": "United States v. Zacarias Moussaoui — trial records and Saudi connection testimony",
        "url": "https://en.wikipedia.org/wiki/Zacarias_Moussaoui",
        "source_type": "court",
        "year": 2006,
    },
    # --- Architects & Engineers ---
    {
        "id": 647,
        "title": "Architects & Engineers for 9/11 Truth — petition signed by 3,600+ building professionals",
        "url": "https://www.ae911truth.org/",
        "source_type": "other",
        "year": 2006,
    },
    # --- 9/11 Families ---
    {
        "id": 648,
        "title": "9/11 victim families' lawsuit against Saudi Arabia — JASTA (Justice Against Sponsors of Terrorism Act) litigation",
        "url": "https://en.wikipedia.org/wiki/Justice_Against_Sponsors_of_Terrorism_Act",
        "source_type": "court",
        "year": 2016,
    },
    # --- Russ Baker ---
    {
        "id": 649,
        "title": "Russ Baker — Family of Secrets: The Bush Dynasty, America's Invisible Government, and the Hidden History of the Last Fifty Years",
        "url": "https://en.wikipedia.org/wiki/Family_of_Secrets",
        "source_type": "journalism",
        "author": "Russ Baker",
        "year": 2009,
    },
    # --- Sibel Edmonds DOJ IG ---
    {
        "id": 650,
        "title": "DOJ Inspector General Report — Review of the FBI's Actions in Connection With Allegations Raised by Contract Linguist Sibel Edmonds",
        "url": "https://oig.justice.gov/sites/default/files/archive/special/0501/final.pdf",
        "source_type": "government",
        "year": 2005,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Key Actors ---
    {
        "name": "Osama bin Laden",
        "entity_type": "person",
        "description": "Founder of Al-Qaeda. CIA-backed mujahideen fighter in 1980s Afghanistan (Operation Cyclone). Saudi exile. Masterminded 9/11 attacks per official account. Family's Saudi Binladin Group had business relationship with Carlyle Group, where George H.W. Bush was advisor.",
        "aliases": "OBL, Usama bin Ladin",
        "metadata": {"role": "Al-Qaeda founder", "years_active": "1988-2011"},
    },
    {
        "name": "Khalid Sheikh Mohammed",
        "entity_type": "person",
        "description": "Principal architect of the 9/11 attacks per 9/11 Commission. Captured in Pakistan 2003. Waterboarded 183 times, rendering his testimony legally compromised. Military tribunal repeatedly delayed.",
        "aliases": "KSM",
        "metadata": {"role": "9/11 mastermind", "years_active": "1993-2003"},
    },
    {
        "name": "Mohamed Atta",
        "entity_type": "person",
        "description": "Lead hijacker and pilot of American Airlines Flight 11 (North Tower). Identified by Able Danger data-mining program as Al-Qaeda member before 9/11, but information reportedly destroyed by DOD lawyers.",
        "aliases": "",
        "metadata": {"role": "lead hijacker", "years_active": "1999-2001"},
    },
    {
        "name": "Nawaf al-Hazmi",
        "entity_type": "person",
        "description": "9/11 hijacker on Flight 77 (Pentagon). CIA tracked him at Kuala Lumpur Al-Qaeda summit in Jan 2000 but failed to watchlist him or notify FBI for 18 months. Received financial support from Saudi embassy contacts in San Diego.",
        "aliases": "",
        "metadata": {"role": "hijacker", "years_active": "2000-2001"},
    },
    {
        "name": "Khalid al-Mihdhar",
        "entity_type": "person",
        "description": "9/11 hijacker on Flight 77 (Pentagon). CIA monitored his attendance at Kuala Lumpur Al-Qaeda meeting (Jan 2000) and knew he had a US visa, but did not notify FBI or add him to watchlist until August 2001.",
        "aliases": "",
        "metadata": {"role": "hijacker", "years_active": "2000-2001"},
    },
    # --- Intelligence Officials ---
    {
        "name": "George Tenet",
        "entity_type": "person",
        "description": "CIA Director 1997-2004. Briefed Bush on 'Bin Ladin Determined to Strike in US' PDB (Aug 6, 2001). Provided 'slam dunk' Iraq WMD intelligence. CIA under his watch failed to share hijacker tracking information with FBI.",
        "aliases": "",
        "metadata": {"role": "CIA Director", "years_active": "1997-2004"},
    },
    {
        "name": "Richard Clarke",
        "entity_type": "person",
        "description": "National Coordinator for Security and Counterterrorism under Clinton and Bush. Testified that repeated urgent warnings about Al-Qaeda were ignored by Bush administration officials before 9/11. His book 'Against All Enemies' detailed the failures.",
        "aliases": "",
        "metadata": {"role": "counterterrorism chief", "years_active": "1992-2003"},
    },
    {
        "name": "Condoleezza Rice",
        "entity_type": "person",
        "description": "National Security Advisor 2001-2005, Secretary of State 2005-2009. Received multiple pre-9/11 warnings including the Aug 6, 2001 PDB. Testified she could not have anticipated planes used as weapons — contradicted by multiple prior studies. Co-authored book with Philip Zelikow.",
        "aliases": "Condi",
        "metadata": {"role": "National Security Advisor", "years_active": "2001-2009"},
    },
    # --- Investigation ---
    {
        "name": "Philip Zelikow",
        "entity_type": "person",
        "description": "Executive Director of the 9/11 Commission — effectively controlled the investigation. Had co-authored book with Condoleezza Rice. Wrote 1998 paper on 'catastrophic terrorism' eerily predicting 9/11-type event. Commission members later said he limited their inquiry.",
        "aliases": "",
        "metadata": {"role": "9/11 Commission Executive Director", "years_active": "2003-2004"},
    },
    {
        "name": "9/11 Commission",
        "entity_type": "organization",
        "description": "National Commission on Terrorist Attacks Upon the United States. Initially resisted by Bush administration. Underfunded ($15M vs $50M for Columbia shuttle investigation). Executive Director Zelikow had conflicts of interest. Commission members later admitted key questions went unasked.",
        "aliases": "National Commission on Terrorist Attacks",
        "metadata": {"type": "investigation", "years_active": "2002-2004"},
    },
    # --- Whistleblowers ---
    {
        "name": "Sibel Edmonds",
        "entity_type": "person",
        "description": "FBI contract linguist and whistleblower. Discovered FBI had pre-9/11 intelligence about the attacks that was suppressed. DOJ invoked 'state secrets' privilege to gag her testimony. DOJ Inspector General confirmed her allegations were 'supported' and FBI retaliated against her.",
        "aliases": "",
        "metadata": {"role": "FBI whistleblower", "years_active": "2001-2012"},
    },
    {
        "name": "Bob Graham",
        "entity_type": "person",
        "description": "U.S. Senator, Chair of Senate Intelligence Committee. Co-chaired Joint Inquiry into 9/11. Fought for 14 years to declassify the '28 Pages' documenting Saudi government connections to the hijackers. Called Saudi involvement 'the most serious national security scandal of our time.'",
        "aliases": "",
        "metadata": {"role": "Senator / Joint Inquiry Co-Chair", "years_active": "1987-2005"},
    },
    # --- Policy / Neoconservative Apparatus ---
    {
        "name": "PNAC",
        "entity_type": "organization",
        "description": "Project for the New American Century. Neoconservative think tank (1997-2009). 2000 report 'Rebuilding America's Defenses' stated transformation of US military would be slow 'absent some catastrophic and catalyzing event — like a new Pearl Harbor.' Signatories included Cheney, Rumsfeld, Wolfowitz, Jeb Bush.",
        "aliases": "Project for the New American Century",
        "metadata": {"type": "think tank", "years_active": "1997-2009"},
    },
    # --- Al-Qaeda ---
    {
        "name": "Al-Qaeda",
        "entity_type": "organization",
        "description": "Militant organization founded by Osama bin Laden (1988). Originally mujahideen fighters supported by CIA in 1980s Afghanistan (Operation Cyclone). Carried out 9/11 attacks. Saudi funding documented in 28 Pages.",
        "aliases": "al-Qa'ida",
        "metadata": {"type": "militant organization", "years_active": "1988-present"},
    },
    # --- Programs ---
    {
        "name": "Operation Able Danger",
        "entity_type": "program",
        "description": "DOD data-mining program that identified Mohamed Atta and other hijackers as Al-Qaeda members before 9/11. Lt. Col. Anthony Shaffer testified that DOD lawyers blocked sharing this intelligence with FBI. Data reportedly destroyed.",
        "aliases": "Able Danger",
        "metadata": {"type": "military intelligence", "years_active": "1999-2001"},
    },
    {
        "name": "Stellar Wind",
        "entity_type": "program",
        "description": "NSA warrantless surveillance program authorized by Bush after 9/11. Intercepted domestic communications without FISA court approval. Revealed by NYT in 2005. Later partially legalized by amendments to FISA. William Binney (NSA whistleblower) exposed the pre-9/11 capabilities.",
        "aliases": "The Program, President's Surveillance Program",
        "metadata": {"type": "surveillance program", "years_active": "2001-2007"},
    },
    # --- Legislation ---
    {
        "name": "USA PATRIOT Act",
        "entity_type": "legislation",
        "description": "Signed Oct 26, 2001 — 45 days after 9/11. 342-page bill passed with minimal debate. Dramatically expanded surveillance authority, eliminated barriers between foreign and domestic intelligence, enabled mass metadata collection. Many provisions pre-written before 9/11.",
        "aliases": "PATRIOT Act",
        "metadata": {"type": "legislation", "year": 2001},
    },
    {
        "name": "Authorization for Use of Military Force (2001)",
        "entity_type": "legislation",
        "description": "Signed Sep 18, 2001 — one week after 9/11. Authorized president to use 'all necessary and appropriate force' against those connected to 9/11. Used to justify wars in Afghanistan, Iraq (disputed), and ongoing global military operations for 20+ years.",
        "aliases": "AUMF 2001",
        "metadata": {"type": "legislation", "year": 2001},
    },
    # --- Facilities ---
    {
        "name": "World Trade Center",
        "entity_type": "facility",
        "description": "Seven-building complex in Manhattan. Twin Towers (WTC 1 & 2) struck by hijacked aircraft, collapsed. WTC 7 collapsed later that day despite not being hit by a plane — NIST attributed to fire, UAF study found fire alone could not have caused the collapse. 2,977 people killed.",
        "aliases": "WTC, Twin Towers",
        "metadata": {"location": "New York City"},
    },
    {
        "name": "The Pentagon",
        "entity_type": "facility",
        "description": "U.S. Department of Defense headquarters. Struck by Flight 77 on 9/11, killing 189 people. Impact area housed accounting offices investigating the $2.3 trillion in untracked transactions announced by Rumsfeld the day before. Surveillance footage of impact largely withheld.",
        "aliases": "",
        "metadata": {"location": "Arlington, Virginia"},
    },
    # --- Events ---
    {
        "name": "September 11 Attacks",
        "entity_type": "event",
        "description": "Coordinated terrorist attacks on Sept 11, 2001. Four hijacked aircraft. WTC Towers destroyed, Pentagon damaged, Flight 93 crashed in Pennsylvania. 2,977 killed. Led to PATRIOT Act, AUMF, wars in Afghanistan and Iraq. Saudi connections suppressed for 15 years (28 Pages).",
        "aliases": "9/11",
        "metadata": {"date": "2001-09-11"},
    },
    {
        "name": "WTC Building 7 Collapse",
        "entity_type": "event",
        "description": "47-story WTC 7 collapsed at 5:20 PM on 9/11 at near free-fall speed despite not being hit by a plane. NIST attributed to fire (2008). UAF study (2020) concluded fire alone could not have caused the observed collapse. Building housed SEC, CIA, IRS, and Secret Service offices. Multiple files for ongoing investigations destroyed.",
        "aliases": "Building 7, WTC 7",
        "metadata": {"date": "2001-09-11"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Al-Qaeda / Hijackers ---
    {
        "source": "Osama bin Laden",
        "target": "Al-Qaeda",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded Al-Qaeda in 1988 from mujahideen networks. CIA had supported these fighters in 1980s Afghanistan.",
        "sources": [626],
        "year_start": 1988,
        "year_end": 2011,
    },
    {
        "source": "Khalid Sheikh Mohammed",
        "target": "September 11 Attacks",
        "type": "planned",
        "tier": "documented",
        "desc": "Principal architect of 9/11 per 9/11 Commission. Captured 2003. Testimony compromised by 183 waterboarding sessions.",
        "sources": [626],
        "year_start": 1996,
        "year_end": 2001,
    },
    {
        "source": "Mohamed Atta",
        "target": "September 11 Attacks",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Lead hijacker, piloted Flight 11 into North Tower. Pre-identified by Able Danger but intelligence not shared.",
        "sources": [626, 637],
        "year_start": 2001,
        "year_end": 2001,
    },
    {
        "source": "Al-Qaeda",
        "target": "September 11 Attacks",
        "type": "executed",
        "tier": "documented",
        "desc": "Al-Qaeda carried out the 9/11 attacks using 19 hijackers on 4 commercial aircraft.",
        "sources": [626],
        "year_start": 2001,
        "year_end": 2001,
    },
    # --- CIA Tracking Failures ---
    {
        "source": "CIA",
        "target": "Nawaf al-Hazmi",
        "type": "monitored",
        "tier": "documented",
        "desc": "CIA tracked al-Hazmi at Kuala Lumpur Al-Qaeda summit (Jan 2000) but failed to watchlist or notify FBI for 18 months.",
        "sources": [626, 641],
        "year_start": 2000,
        "year_end": 2001,
    },
    {
        "source": "CIA",
        "target": "Khalid al-Mihdhar",
        "type": "monitored",
        "tier": "documented",
        "desc": "CIA knew al-Mihdhar attended Al-Qaeda meeting and had US visa. Did not add to watchlist until Aug 2001, weeks before attack.",
        "sources": [626, 641],
        "year_start": 2000,
        "year_end": 2001,
    },
    # --- Intelligence Officials ---
    {
        "source": "George Tenet",
        "target": "CIA",
        "type": "directed",
        "tier": "documented",
        "desc": "CIA Director during 9/11. Briefed Bush on 'Bin Ladin Determined to Strike' PDB. Agency failed to share hijacker info with FBI.",
        "sources": [626, 632],
        "year_start": 1997,
        "year_end": 2004,
    },
    {
        "source": "Richard Clarke",
        "target": "September 11 Attacks",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Counterterrorism chief who testified his repeated urgent warnings about Al-Qaeda were ignored by Bush administration officials.",
        "sources": [632],
        "year_start": 2001,
        "year_end": 2001,
    },
    {
        "source": "Condoleezza Rice",
        "target": "September 11 Attacks",
        "type": "connected_to",
        "tier": "documented",
        "desc": "NSA who received Aug 6, 2001 PDB titled 'Bin Ladin Determined to Strike in US.' Claimed attack could not have been anticipated.",
        "sources": [626, 632],
        "year_start": 2001,
        "year_end": 2001,
    },
    {
        "source": "Philip Zelikow",
        "target": "9/11 Commission",
        "type": "directed",
        "tier": "documented",
        "desc": "Executive Director who controlled the investigation. Had co-authored book with Condoleezza Rice — documented conflict of interest.",
        "sources": [633, 642],
        "year_start": 2003,
        "year_end": 2004,
    },
    {
        "source": "Philip Zelikow",
        "target": "Condoleezza Rice",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Co-authored 'Germany Unified and Europe Transformed' with Rice. Served on her NSC transition team. Investigated the administration while professionally connected to it.",
        "sources": [633, 642],
        "year_start": 1995,
        "year_end": 2004,
    },
    {
        "source": "9/11 Commission",
        "target": "September 11 Attacks",
        "type": "investigated",
        "tier": "documented",
        "desc": "Official investigation initially resisted by Bush admin. Underfunded ($15M). Zelikow conflicts. Key questions unasked per members.",
        "sources": [626, 633],
        "year_start": 2002,
        "year_end": 2004,
    },
    # --- Whistleblowers ---
    {
        "source": "Sibel Edmonds",
        "target": "FBI",
        "type": "worked_for",
        "tier": "documented",
        "desc": "FBI contract linguist who discovered suppressed pre-9/11 intelligence. DOJ gagged her under state secrets privilege. IG confirmed allegations.",
        "sources": [635, 650],
        "year_start": 2001,
        "year_end": 2002,
    },
    {
        "source": "Sibel Edmonds",
        "target": "September 11 Attacks",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Whistleblower who exposed that FBI had pre-9/11 intelligence that was deliberately suppressed. DOJ invoked state secrets.",
        "sources": [635, 650],
        "year_start": 2002,
        "year_end": 2012,
    },
    {
        "source": "Bob Graham",
        "target": "September 11 Attacks",
        "type": "investigated",
        "tier": "documented",
        "desc": "Co-chaired Joint Inquiry. Fought 14 years to declassify 28 Pages documenting Saudi government connections to hijackers.",
        "sources": [627, 634],
        "year_start": 2002,
        "year_end": 2016,
    },
    # --- Saudi Connections ---
    {
        "source": "Prince Bandar bin Sultan",
        "target": "September 11 Attacks",
        "type": "connected_to",
        "tier": "documented",
        "desc": "28 Pages revealed his wife's payments to Saudi intelligence agent in San Diego who aided hijackers al-Hazmi and al-Mihdhar.",
        "sources": [627, 639, 640],
        "year_start": 2000,
        "year_end": 2001,
    },
    {
        "source": "Saudi GID",
        "target": "Al-Qaeda",
        "type": "funded",
        "tier": "credible",
        "desc": "28 Pages and FBI documents indicate Saudi government and intelligence officials provided financial support to hijackers.",
        "sources": [627, 639],
        "year_start": 1996,
        "year_end": 2001,
    },
    {
        "source": "Carlyle Group",
        "target": "Saudi Binladin Group",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Bin Laden family invested in Carlyle Group. George H.W. Bush attended Carlyle investor meeting with Shafig bin Laden on morning of 9/11.",
        "sources": [636, 649],
        "year_start": 1998,
        "year_end": 2001,
    },
    # --- PNAC / Neoconservative Apparatus ---
    {
        "source": "Dick Cheney",
        "target": "PNAC",
        "type": "member_of",
        "tier": "documented",
        "desc": "Signatory of PNAC's founding statement of principles. PNAC's 2000 report anticipated need for 'new Pearl Harbor' to catalyze military transformation.",
        "sources": [631],
        "year_start": 1997,
        "year_end": 2001,
    },
    {
        "source": "Donald Rumsfeld",
        "target": "PNAC",
        "type": "member_of",
        "tier": "documented",
        "desc": "PNAC signatory. Announced $2.3 trillion in untracked Pentagon transactions on Sept 10, 2001 — accounting offices hit next day.",
        "sources": [631, 643],
        "year_start": 1997,
        "year_end": 2001,
    },
    # --- Programs ---
    {
        "source": "Operation Able Danger",
        "target": "Mohamed Atta",
        "type": "identified",
        "tier": "credible",
        "desc": "DOD data-mining program identified Atta as Al-Qaeda before 9/11. DOD lawyers ordered data destroyed. Lt. Col. Shaffer's testimony corroborated.",
        "sources": [637],
        "year_start": 2000,
        "year_end": 2001,
    },
    {
        "source": "NSA",
        "target": "Stellar Wind",
        "type": "operated",
        "tier": "documented",
        "desc": "NSA operated warrantless surveillance program authorized by Bush after 9/11. Revealed by NYT in 2005.",
        "sources": [638],
        "year_start": 2001,
        "year_end": 2007,
    },
    # --- Legislation ---
    {
        "source": "George W. Bush",
        "target": "USA PATRIOT Act",
        "type": "authorized",
        "tier": "documented",
        "desc": "Signed PATRIOT Act 45 days after 9/11. Dramatically expanded surveillance powers with minimal congressional debate.",
        "sources": [644],
        "year_start": 2001,
        "year_end": 2001,
    },
    {
        "source": "George W. Bush",
        "target": "Authorization for Use of Military Force (2001)",
        "type": "authorized",
        "tier": "documented",
        "desc": "Signed AUMF one week after 9/11. Used to justify wars and military operations for 20+ years.",
        "sources": [645],
        "year_start": 2001,
        "year_end": 2001,
    },
    # --- WTC 7 ---
    {
        "source": "WTC Building 7 Collapse",
        "target": "September 11 Attacks",
        "type": "connected_to",
        "tier": "documented",
        "desc": "47-story building collapsed at near free-fall speed without plane impact. NIST says fire. UAF study disagrees. Housed SEC/CIA/IRS offices.",
        "sources": [629, 630, 647],
        "year_start": 2001,
        "year_end": 2001,
    },
    # --- George H.W. Bush / Carlyle ---
    {
        "source": "George H.W. Bush",
        "target": "Carlyle Group",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Senior advisor to Carlyle Group. Attended investor meeting with Shafig bin Laden on morning of September 11, 2001.",
        "sources": [636, 649],
        "year_start": 1998,
        "year_end": 2003,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Osama bin Laden": [626, 636],
    "Khalid Sheikh Mohammed": [626, 646],
    "Mohamed Atta": [626, 637],
    "Nawaf al-Hazmi": [626, 641, 627],
    "Khalid al-Mihdhar": [626, 641, 627],
    "George Tenet": [626, 632],
    "Richard Clarke": [632],
    "Condoleezza Rice": [626, 632, 642],
    "Philip Zelikow": [633, 642],
    "9/11 Commission": [626, 633],
    "Sibel Edmonds": [635, 650],
    "Bob Graham": [627, 634],
    "PNAC": [631],
    "Al-Qaeda": [626, 627],
    "Operation Able Danger": [637],
    "Stellar Wind": [638],
    "USA PATRIOT Act": [644],
    "Authorization for Use of Military Force (2001)": [645],
    "World Trade Center": [626, 628, 629],
    "The Pentagon": [626, 643],
    "September 11 Attacks": [626, 627, 633, 636],
    "WTC Building 7 Collapse": [629, 630, 647],
}
