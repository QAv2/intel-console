"""
UAP Disclosure Legal Movement — Expansion layer for Intel Console.

Source video: "Daniel Sheehan - The Lawyer Fighting for UAP Disclosure,
Crash Retrievals, and Oversight" (YouTube: LEAEkttzwYA)

Entities: Daniel Sheehan, John Mack, Steven Greer, Luis Elizondo,
David Grusch, David Fravor, Ryan Graves, Chuck Schumer, Mike Rounds,
Tim Burchett, New Paradigm Institute, Christic Institute,
Disclosure Project, Americans for Safe Aerospace, AATIP,
Project Blue Book, UAP Task Force, UAP Disclosure Act,
Enhanced UAP Whistleblower Protection Act, Grusch Congressional Hearing

Maps the documented legal-legislative architecture of UAP disclosure:
Sheehan's career arc from Pentagon Papers → Iran-Contra → Christic Institute →
John Mack defense → Disclosure Project → AATIP/Elizondo → Grusch testimony →
Schumer-Rounds UAP Disclosure Act → whistleblower protections.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  CIA [85], Iran-Contra [96]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 419+ (continuing from existing 418)
# ============================================================

SOURCES = [
    # --- Pentagon Papers / Sheehan career ---
    {
        "id": 419,
        "title": "New York Times Co. v. United States — First Amendment Encyclopedia (MTSU)",
        "url": "https://firstamendment.mtsu.edu/article/new-york-times-co-v-united-states/",
        "source_type": "academic",
        "year": 1971,
    },
    {
        "id": 420,
        "title": "Daniel Sheehan (attorney) — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Daniel_Sheehan_(attorney)",
        "source_type": "other",
        "year": 2024,
    },
    # --- Christic Institute / Avirgan v. Hull ---
    {
        "id": 421,
        "title": "Avirgan v. Hull, 932 F.2d 1572 — U.S. Court of Appeals, 11th Circuit (CourtListener)",
        "url": "https://www.courtlistener.com/opinion/561240/tony-avirgan-and-martha-honey-v-john-hull-adolfo-calero-robert-owen/",
        "source_type": "court",
        "year": 1991,
    },
    {
        "id": 422,
        "title": "Christic Institute — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Christic_Institute",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 423,
        "title": "Iran Contra Affair — Romero Institute",
        "url": "https://www.romeroinstitute.net/project-iran-contra",
        "source_type": "other",
        "year": 2024,
    },
    # --- John Mack ---
    {
        "id": 424,
        "title": "HMS Takes No Action Against 'UFO Doctor' — Harvard Crimson",
        "url": "https://www.thecrimson.com/article/1995/8/4/hms-takes-no-action-against-ufo/",
        "source_type": "journalism",
        "author": "The Harvard Crimson",
        "year": 1995,
    },
    {
        "id": 425,
        "title": "Defining Academic Freedom — Harvard Crimson",
        "url": "https://www.thecrimson.com/article/1995/6/30/defining-academic-freedom-pbsbhould-a-distinguished/",
        "source_type": "journalism",
        "author": "The Harvard Crimson",
        "year": 1995,
    },
    {
        "id": 426,
        "title": "John E. Mack obituary — PubMed Central / NIH",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC523131/",
        "source_type": "academic",
        "year": 2004,
    },
    # --- Disclosure Project ---
    {
        "id": 427,
        "title": "Group Calls for Disclosure of UFO Info — ABC News",
        "url": "https://abcnews.go.com/Technology/story?id=98572&page=1",
        "source_type": "journalism",
        "author": "ABC News",
        "year": 2001,
    },
    # --- AATIP / Elizondo ---
    {
        "id": 428,
        "title": "Secret Pentagon Program Spent Millions to Research UFOs — NPR",
        "url": "https://www.npr.org/sections/thetwo-way/2017/12/17/571446881/secret-pentagon-program-spent-millions-to-research-ufos",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2017,
    },
    {
        "id": 429,
        "title": "Defense Department Emails Confirm 2017 UAP Briefings — The Black Vault",
        "url": "https://www.theblackvault.com/documentarchive/defense-department-emails-confirm-2017-uap-briefings-further-clarify-luis-elizondos-role-in-aatip/",
        "source_type": "journalism",
        "author": "The Black Vault",
        "year": 2020,
    },
    # --- Grusch Hearing ---
    {
        "id": 430,
        "title": "UAP: Implications on National Security — House Oversight Committee Hearing Page",
        "url": "https://oversight.house.gov/hearing/unidentified-anomalous-phenomena-implications-on-national-security-public-safety-and-government-transparency/",
        "source_type": "congressional",
        "year": 2023,
    },
    {
        "id": 431,
        "title": "Full Hearing Transcript (PDF) — Congress.gov / GPO",
        "url": "https://www.congress.gov/118/meeting/house/116282/documents/HHRG-118-GO06-Transcript-20230726.pdf",
        "source_type": "congressional",
        "year": 2023,
    },
    {
        "id": 432,
        "title": "David Grusch Opening Statement (PDF) — House Oversight Committee",
        "url": "https://oversight.house.gov/wp-content/uploads/2023/07/Dave_G_HOC_Speech_FINAL_For_Trans.pdf",
        "source_type": "congressional",
        "year": 2023,
    },
    {
        "id": 433,
        "title": "Whistleblower testifies U.S. salvaged 'non-human biologics' — NPR",
        "url": "https://www.npr.org/2023/07/27/1190390376/ufo-hearing-non-human-biologics-uaps",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2023,
    },
    # --- UAP Disclosure Act / Schumer-Rounds ---
    {
        "id": 434,
        "title": "Schumer-Rounds UAP Disclosure Amendment — Press Release, Senate Democrats",
        "url": "https://www.democrats.senate.gov/newsroom/press-releases/schumer-rounds-introduce-new-legislation-to-declassify-government-records-related-to-unidentified-anomalous-phenomena-and-ufos_modeled-after-jfk-assassination-records-collection-act--as-an-amendment-to-ndaa",
        "source_type": "congressional",
        "year": 2023,
    },
    {
        "id": 435,
        "title": "S.Amdt.797 to S.2226 — Full Amendment Text (Congress.gov)",
        "url": "https://www.congress.gov/amendment/118th-congress/senate-amendment/797/text",
        "source_type": "congressional",
        "year": 2023,
    },
    {
        "id": 436,
        "title": "UAP Disclosure Act of 2024 — Full Text (New Paradigm Institute)",
        "url": "https://newparadigminstitute.org/learn/library/uap-disclosure-act-of-2024-full-text/",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 437,
        "title": "The UAP Disclosure Act: Implications for Congressional Oversight — NYU JLPP",
        "url": "https://nyujlpp.org/wp-content/uploads/2025/03/JLPP-27-2-Yang.pdf",
        "source_type": "academic",
        "year": 2025,
    },
    # --- New Paradigm Institute ---
    {
        "id": 438,
        "title": "New Paradigm Institute — Official Homepage",
        "url": "https://newparadigminstitute.org/",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 439,
        "title": "NPI Announces Citizens for Disclosure — EIN Presswire / KXAN",
        "url": "https://www.kxan.com/business/press-releases/ein-presswire/689716435/npi-announces-citizens-for-disclosure-a-grassroots-uap-transparency-initiative/",
        "source_type": "journalism",
        "year": 2024,
    },
    # --- Enhanced Whistleblower Protection Act ---
    {
        "id": 440,
        "title": "H.R.5060 — Enhanced UAP Whistleblower Protection Act of 2025 (Congress.gov)",
        "url": "https://www.congress.gov/bill/119th-congress/house-bill/5060",
        "source_type": "congressional",
        "year": 2025,
    },
    {
        "id": 441,
        "title": "Restoring Public Trust Through UAP Transparency — House Oversight Hearing",
        "url": "https://oversight.house.gov/hearing/restoring-public-trust-through-uap-transparency-and-whistleblower-protection/",
        "source_type": "congressional",
        "year": 2025,
    },
    # --- Project Blue Book ---
    {
        "id": 442,
        "title": "Unidentified Flying Objects and Air Force Project Blue Book — USAF Fact Sheet",
        "url": "https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104590/unidentified-flying-objects-and-air-force-project-blue-book/",
        "source_type": "government",
        "year": 1969,
    },
    {
        "id": 443,
        "title": "Project BLUE BOOK — Unidentified Flying Objects — National Archives (NARA)",
        "url": "https://www.archives.gov/research/military/air-force/ufos",
        "source_type": "government",
        "year": 1969,
    },
]

# ============================================================
# ENTITIES — 20 new (continuing from 264)
# ============================================================

ENTITIES = [
    # --- People ---
    {
        "name": "Daniel Sheehan",
        "entity_type": "person",
        "description": "Harvard-trained constitutional attorney. Represented NYT in Pentagon Papers (1971), led Karen Silkwood case, filed Avirgan v. Hull RICO suit exposing Iran-Contra 'Secret Team' via Christic Institute. Defended Dr. John Mack at Harvard. General Counsel for 2001 Disclosure Project. Legal counsel for AATIP whistleblower Luis Elizondo. President of New Paradigm Institute. Primary legal architect of modern UAP disclosure movement.",
        "aliases": "Danny Sheehan, Sheihan, Shiin, Xihan",
    },
    {
        "name": "John Mack",
        "entity_type": "person",
        "description": "Pulitzer Prize-winning Harvard Medical School professor of psychiatry. Conducted clinical research on alien abduction experiences. Faced unprecedented Harvard investigation (1994-1995) for his book 'Abduction: Human Encounters with Aliens.' Successfully defended by Daniel Sheehan — Harvard reaffirmed his academic freedom. Established that non-human contact testimonies are legitimate subjects for clinical research. Killed in car accident in London, 2004.",
        "aliases": "John Edward Mack",
    },
    {
        "name": "Steven Greer",
        "entity_type": "person",
        "description": "Emergency physician and founder of the Disclosure Project. Organized the May 9, 2001 National Press Club event with 20+ military/intelligence witnesses testifying about UFO encounters. Sheehan served as general counsel. The webcast drew 250,000 simultaneous viewers. Advocates for release of suppressed energy technologies alongside UAP disclosure.",
        "aliases": "Dr. Steven Greer",
    },
    {
        "name": "Luis Elizondo",
        "entity_type": "person",
        "description": "Former U.S. Army counterintelligence officer and military intelligence official. Claimed to have directed AATIP (Advanced Aerospace Threat Identification Program) at the Pentagon. Resigned October 2017 citing excessive secrecy. Provided three Navy pilot UAP videos to the New York Times, triggering the December 2017 revelations. Daniel Sheehan served as his legal counsel, helping file complaints against the Pentagon.",
        "aliases": "Lue Elizondo",
    },
    {
        "name": "David Grusch",
        "entity_type": "person",
        "description": "Former NRO representative to the UAP Task Force (GS-15). Testified before House Oversight Committee on July 26, 2023 that the U.S. possesses a 'multi-decade UAP crash retrieval and reverse-engineering program' and 'non-human biologics.' Based on interviews with 40+ witnesses over four years. His allegations confirmed Sheehan's 'secret team' theory. Filed whistleblower complaints with the Intelligence Community Inspector General.",
        "aliases": "David Charles Grusch",
    },
    {
        "name": "David Fravor",
        "entity_type": "person",
        "description": "Retired U.S. Navy Commander, former commanding officer of Black Aces Squadron (VFA-41). Eyewitness to the 2004 USS Nimitz UAP encounter ('Tic Tac' incident). Testified before House Oversight Committee on July 26, 2023 alongside David Grusch and Ryan Graves.",
        "aliases": "Cmdr. David Fravor",
    },
    {
        "name": "Ryan Graves",
        "entity_type": "person",
        "description": "Former U.S. Navy F/A-18F pilot. Executive Director of Americans for Safe Aerospace. Testified before House Oversight Committee on July 26, 2023 about repeated UAP encounters during training exercises off the U.S. East Coast (2014-2015). Advocated for pilot reporting mechanisms and flight safety protocols.",
        "aliases": "",
    },
    {
        "name": "Chuck Schumer",
        "entity_type": "person",
        "description": "U.S. Senate Majority Leader (D-NY). Lead author of the UAP Disclosure Act (S.Amdt.797), modeled on the JFK Assassination Records Collection Act of 1992. Original version included eminent domain over recovered technologies of unknown origin held by private entities. Passed as part of FY2024 NDAA but eminent domain clause stripped in conference.",
        "aliases": "Charles Schumer",
    },
    {
        "name": "Mike Rounds",
        "entity_type": "person",
        "description": "U.S. Senator (R-SD). Co-author of the bipartisan UAP Disclosure Act with Chuck Schumer. The Schumer-Rounds Amendment received bipartisan support from Rubio, Gillibrand, Young, and Heinrich.",
        "aliases": "Marion Michael Rounds",
    },
    {
        "name": "Tim Burchett",
        "entity_type": "person",
        "description": "U.S. Representative (R-TN). Lead sponsor of H.R. 5060, the Enhanced UAP Whistleblower Protection Act of 2025. Vocal advocate for UAP transparency in the House. Played key role in organizing the July 2023 House Oversight hearing on UAP.",
        "aliases": "",
    },
    # --- Organizations ---
    {
        "name": "New Paradigm Institute",
        "entity_type": "organization",
        "description": "Founded 2023 by Daniel Sheehan as initiative of the Romero Institute. Mobilizes strategic litigation and legislative advocacy for UAP disclosure. Drafted key provisions of the UAP Disclosure Act. Launched 'Citizens for Disclosure' grassroots campaign in 2024. Serves as public clearinghouse for UAP legislative tracking and witness coordination.",
        "aliases": "NPI",
    },
    {
        "name": "Christic Institute",
        "entity_type": "organization",
        "description": "Public interest law firm co-founded by Daniel Sheehan and Sara Nelson in 1980. Filed the Avirgan v. Hull RICO lawsuit (1986) — a $24M civil suit against 28 defendants including Theodore Shackley, Thomas Clines, and Richard Secord, alleging a criminal enterprise of arms/drug smuggling and the 'Secret Team' covert operations network. Case dismissed 1988; ordered to pay $1M in fees. Despite legal defeat, publicly exposed the network later confirmed by Iran-Contra congressional investigation. Succeeded by the Romero Institute.",
        "aliases": "",
    },
    {
        "name": "Disclosure Project",
        "entity_type": "organization",
        "description": "Founded by Steven Greer. Organized the landmark May 9, 2001 National Press Club event in Washington, D.C., where 20+ military, government, intelligence, and corporate witnesses testified about UFO/UAP encounters. Daniel Sheehan served as general counsel. Called for open congressional hearings and release of suppressed energy technologies.",
        "aliases": "",
    },
    {
        "name": "Americans for Safe Aerospace",
        "entity_type": "organization",
        "description": "Founded by Ryan Graves. Advocacy organization focused on flight safety and UAP reporting mechanisms for military and commercial pilots. Provides a secure channel for pilots to report anomalous encounters without career repercussions.",
        "aliases": "ASA",
    },
    # --- Programs ---
    {
        "name": "AATIP",
        "entity_type": "program",
        "description": "Advanced Aerospace Threat Identification Program. $22M Pentagon program (2007-2012) investigating UAP reports, funded through the Defense Intelligence Agency at the request of Sen. Harry Reid. Revealed to the public by the New York Times on December 16, 2017 after Luis Elizondo's resignation. Produced the 38 Defense Intelligence Reference Documents (DIRDs) on advanced propulsion, metamaterials, and spacetime metrics.",
        "aliases": "Advanced Aerospace Threat Identification Program",
    },
    {
        "name": "Project Blue Book",
        "entity_type": "program",
        "description": "Systematic USAF study of UFOs from March 1952 to December 17, 1969, headquartered at Wright-Patterson AFB, Ohio. Preceded by Project Sign (1947-1949) and Project Grudge (1949). Of 12,618 sightings investigated, 701 remained 'unidentified.' Terminated after the Condon Committee report. Daniel Sheehan, while serving as special counsel under President Carter, uncovered classified photographs from Blue Book documenting military crash retrieval operations.",
        "aliases": "",
    },
    {
        "name": "UAP Task Force",
        "entity_type": "program",
        "description": "Pentagon program established August 2020 under the Office of Naval Intelligence to investigate UAP reports from military personnel. Succeeded AATIP. Produced the June 2021 preliminary assessment confirming 144 UAP reports from 2004-2021 (143 unexplained). David Grusch served as NRO representative. Succeeded by AARO (All-domain Anomaly Resolution Office) in July 2022.",
        "aliases": "UAPTF",
    },
    # --- Legislation ---
    {
        "name": "UAP Disclosure Act",
        "entity_type": "legislation",
        "description": "Bipartisan legislation led by Schumer (D-NY) and Rounds (R-SD), modeled on the JFK Assassination Records Collection Act. Original version included eminent domain over technologies of unknown origin (TUO) and biological evidence of NHI held by private entities, plus a 9-member UAP Records Review Board with subpoena power. Passed in FY2024 NDAA (Dec 2023) but eminent domain and review board stripped in conference under defense contractor lobbying. Retained disclosure timelines and NARA record collection requirements. Reintroduced as S.Amdt.2610 in 2024.",
        "aliases": "Schumer-Rounds Amendment",
    },
    {
        "name": "Enhanced UAP Whistleblower Protection Act",
        "entity_type": "legislation",
        "description": "H.R. 5060, introduced by Rep. Tim Burchett (R-TN) and Rep. Anna Paulina Luna (R-FL). Allows current/former government employees and contractors to report UAP/NHI information to Congress. Establishes private civil cause of action for retaliation. Grants Attorney General immunity-granting authority for 5-year period. Challenges enforceability of NDAs tied to illegal misappropriation of funds in unacknowledged programs.",
        "aliases": "H.R. 5060",
    },
    # --- Events ---
    {
        "name": "Grusch Congressional Hearing",
        "entity_type": "event",
        "description": "July 26, 2023: House Oversight Subcommittee on National Security hearing titled 'Unidentified Anomalous Phenomena: Implications on National Security, Public Safety, and Government Transparency.' Witnesses: David Grusch (former NRO/UAPTF), Ryan Graves (Americans for Safe Aerospace), Ret. Cmdr. David Fravor (USS Nimitz). Grusch testified to multi-decade crash retrieval program and recovery of 'non-human biologics.' Based on interviews with 40+ witnesses.",
        "aliases": "July 2023 UAP Hearing",
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Sheehan's career arc ---
    {
        "source": "Daniel Sheehan",
        "target": "Christic Institute",
        "type": "co-founded",
        "tier": "documented",
        "desc": "Co-founded the Christic Institute in 1980 with Sara Nelson as a public interest law firm",
        "year_start": 1980,
        "sources": [420, 422],
    },
    {
        "source": "Christic Institute",
        "target": "Iran-Contra",
        "type": "exposed",
        "tier": "documented",
        "desc": "Filed Avirgan v. Hull RICO suit (1986) against 28 defendants — publicly exposed 'Secret Team' covert operations network later confirmed by Iran-Contra congressional investigation",
        "year_start": 1986,
        "year_end": 1991,
        "sources": [421, 423],
    },
    {
        "source": "Daniel Sheehan",
        "target": "John Mack",
        "type": "legal_counsel",
        "tier": "documented",
        "desc": "Served as Mack's attorney during Harvard investigation (1994-95), successfully defended his academic freedom to study alien abduction experiences",
        "year_start": 1994,
        "year_end": 1995,
        "sources": [424, 425],
    },
    {
        "source": "Daniel Sheehan",
        "target": "Disclosure Project",
        "type": "served_as",
        "tier": "documented",
        "desc": "General Counsel for the 2001 Disclosure Project National Press Club event",
        "year_start": 2001,
        "sources": [420, 427],
    },
    {
        "source": "Daniel Sheehan",
        "target": "Luis Elizondo",
        "type": "legal_counsel",
        "tier": "credible",
        "desc": "Served as legal counsel for AATIP whistleblower Elizondo, helping file complaints against the Pentagon",
        "year_start": 2017,
        "sources": [420, 428],
    },
    {
        "source": "Daniel Sheehan",
        "target": "New Paradigm Institute",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded NPI in 2023 as initiative of the Romero Institute to drive UAP disclosure litigation and legislation",
        "year_start": 2023,
        "sources": [438],
    },
    {
        "source": "New Paradigm Institute",
        "target": "UAP Disclosure Act",
        "type": "advocated_for",
        "tier": "documented",
        "desc": "NPI drafted key provisions and publicly advocated for the Schumer-Rounds UAP Disclosure Act",
        "year_start": 2023,
        "sources": [436, 438],
    },
    {
        "source": "Daniel Sheehan",
        "target": "Project Blue Book",
        "type": "investigated",
        "tier": "credible",
        "desc": "As special counsel under President Carter, Sheehan uncovered classified Blue Book photographs documenting military crash retrieval operations",
        "year_start": 1977,
        "sources": [420, 442],
    },
    # --- Greer ---
    {
        "source": "Steven Greer",
        "target": "Disclosure Project",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded the Disclosure Project and organized the May 2001 National Press Club event",
        "year_start": 2001,
        "sources": [427],
    },
    # --- Elizondo / AATIP ---
    {
        "source": "Luis Elizondo",
        "target": "AATIP",
        "type": "directed",
        "tier": "credible",
        "desc": "Claimed to have directed AATIP at the Pentagon; resigned Oct 2017 citing excessive secrecy. Role confirmed by DIA emails (Black Vault FOIA)",
        "year_start": 2010,
        "year_end": 2017,
        "sources": [428, 429],
    },
    {
        "source": "AATIP",
        "target": "CIA",
        "type": "oversight_by",
        "tier": "credible",
        "desc": "AATIP operated within Pentagon/DIA with intelligence community oversight; intersected with broader IC UAP programs",
        "year_start": 2007,
        "year_end": 2012,
        "sources": [428],
    },
    # --- Grusch ---
    {
        "source": "David Grusch",
        "target": "UAP Task Force",
        "type": "served_in",
        "tier": "documented",
        "desc": "NRO representative to the UAP Task Force (GS-15 position)",
        "year_start": 2020,
        "year_end": 2023,
        "sources": [430, 432],
    },
    {
        "source": "David Grusch",
        "target": "Grusch Congressional Hearing",
        "type": "testified_at",
        "tier": "documented",
        "desc": "Testified under oath before House Oversight Committee on July 26, 2023 about crash retrieval programs and non-human biologics",
        "year_start": 2023,
        "sources": [430, 431, 432],
    },
    {
        "source": "David Fravor",
        "target": "Grusch Congressional Hearing",
        "type": "testified_at",
        "tier": "documented",
        "desc": "Testified about 2004 USS Nimitz 'Tic Tac' UAP encounter",
        "year_start": 2023,
        "sources": [430, 431],
    },
    {
        "source": "Ryan Graves",
        "target": "Grusch Congressional Hearing",
        "type": "testified_at",
        "tier": "documented",
        "desc": "Testified about repeated UAP encounters during Navy training exercises (2014-2015)",
        "year_start": 2023,
        "sources": [430, 431],
    },
    {
        "source": "Ryan Graves",
        "target": "Americans for Safe Aerospace",
        "type": "founded",
        "tier": "documented",
        "desc": "Founded ASA to provide secure UAP reporting channels for pilots",
        "year_start": 2022,
        "sources": [430],
    },
    # --- Legislation ---
    {
        "source": "Chuck Schumer",
        "target": "UAP Disclosure Act",
        "type": "authored",
        "tier": "documented",
        "desc": "Lead author of the bipartisan UAP Disclosure Act (S.Amdt.797)",
        "year_start": 2023,
        "sources": [434, 435],
    },
    {
        "source": "Mike Rounds",
        "target": "UAP Disclosure Act",
        "type": "co-authored",
        "tier": "documented",
        "desc": "Co-author of the Schumer-Rounds UAP Disclosure Act",
        "year_start": 2023,
        "sources": [434, 435],
    },
    {
        "source": "Tim Burchett",
        "target": "Enhanced UAP Whistleblower Protection Act",
        "type": "authored",
        "tier": "documented",
        "desc": "Lead sponsor of H.R. 5060, the Enhanced UAP Whistleblower Protection Act of 2025",
        "year_start": 2025,
        "sources": [440, 441],
    },
    {
        "source": "Tim Burchett",
        "target": "Grusch Congressional Hearing",
        "type": "organized",
        "tier": "documented",
        "desc": "Played key role in organizing the July 2023 House Oversight UAP hearing",
        "year_start": 2023,
        "sources": [430],
    },
    # --- Cross-links to existing entities ---
    {
        "source": "Daniel Sheehan",
        "target": "CIA",
        "type": "investigated",
        "tier": "documented",
        "desc": "Karen Silkwood case revealed CIA plutonium smuggling via Israeli Desk; Christic Institute RICO suit targeted former CIA covert operations figures (Shackley, Clines, Secord)",
        "year_start": 1976,
        "year_end": 1991,
        "sources": [420, 421],
    },
    {
        "source": "Grusch Congressional Hearing",
        "target": "UAP Disclosure Act",
        "type": "precipitated",
        "tier": "credible",
        "desc": "Grusch's sworn testimony about crash retrieval programs accelerated legislative momentum for the Schumer-Rounds UAP Disclosure Act",
        "year_start": 2023,
        "sources": [430, 434, 437],
    },
    {
        "source": "UAP Task Force",
        "target": "AATIP",
        "type": "succeeded",
        "tier": "documented",
        "desc": "UAPTF (est. Aug 2020) succeeded AATIP as Pentagon's primary UAP investigation program",
        "year_start": 2020,
        "sources": [428, 430],
    },
    {
        "source": "Daniel Sheehan",
        "target": "David Grusch",
        "type": "supported",
        "tier": "credible",
        "desc": "Sheehan advocated for Grusch and helped push his allegations before the Senate Intelligence Committee",
        "year_start": 2023,
        "sources": [420, 433],
    },
]

# ============================================================
# ENTITY_SOURCES — link entities to their primary sources
# ============================================================

ENTITY_SOURCES = {
    "Daniel Sheehan": [419, 420, 421, 422, 423, 438],
    "John Mack": [424, 425, 426],
    "Steven Greer": [427],
    "Luis Elizondo": [428, 429],
    "David Grusch": [430, 431, 432, 433],
    "David Fravor": [430, 431],
    "Ryan Graves": [430, 431],
    "Chuck Schumer": [434, 435],
    "Mike Rounds": [434, 435],
    "Tim Burchett": [440, 441],
    "New Paradigm Institute": [436, 438, 439],
    "Christic Institute": [421, 422, 423],
    "Disclosure Project": [427],
    "Americans for Safe Aerospace": [430],
    "AATIP": [428, 429],
    "Project Blue Book": [442, 443],
    "UAP Task Force": [430],
    "UAP Disclosure Act": [434, 435, 436, 437],
    "Enhanced UAP Whistleblower Protection Act": [440, 441],
    "Grusch Congressional Hearing": [430, 431, 432, 433],
}
