"""
Latin America Cluster — Expansion layer for Intel Console.

Maps the narco-intelligence nexus: CIA covert operations in Latin America,
the drug trafficking-intelligence symbiosis documented by the Kerry Committee
and Gary Webb, Operation Condor, and direct Epstein connections to Colombian
and Mexican elites.

Key threads:
- Oliver North coordinated Iran-Contra from NSC; declassified notebooks show
  drug trafficking knowledge
- Manuel Noriega: CIA asset ($200K/year), BCCI client ($23M laundered), drug
  trafficker, School of the Americas graduate, U.S. eventually invaded to remove
- Felix Rodriguez: CIA paramilitary career spanning Bay of Pigs (1961), Che
  Guevara capture (1967), Phoenix Program (Vietnam), Iran-Contra (El Salvador)
- Gary Webb's "Dark Alliance" exposed CIA-Contra-crack cocaine nexus; CIA
  internal memo "Managing a Nightmare" documented their media campaign against him
- Operation Condor: CIA-supported transnational repression network, Kissinger
  documented involvement, $8M covert operations in Chile alone
- SETCO Aviation: owned by drug trafficker Juan Matta Ballesteros, simultaneously
  served as principal Contra supply airline
- Kerry Committee: 1,166-page Senate report documented Contra drug trafficking,
  State Dept chose 4 companies controlled by drug traffickers for Contra aid
- Andres Pastrana: Colombian president on Epstein flight logs (March 2003),
  37 file references in 2026 DOJ release, photos with Maxwell in military uniforms

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Jeffrey Epstein [1], Ghislaine Maxwell [2], Jean-Luc Brunel [135],
  Bill Clinton [32], Donald Trump [33], Henry Kissinger [111],
  CIA [85], FBI [87], NSA [86], DOJ [89], DARPA [90],
  BCCI [54], Barry Seal [24], Southern Air Transport [93],
  Iran-Contra [96], William Casey [6], John Poindexter [29],
  George H.W. Bush [212], Ronald Reagan [211],
  Prince Bandar bin Sultan [176], Safari Club [186]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 397+ (continuing from existing 396)
# ============================================================

SOURCES = [
    {
        "id": 397,
        "title": "Lawrence Walsh — Final Report of the Independent Counsel for Iran/Contra Matters (1993). Chapters cover Oliver North (Ch. 2), Felix Rodriguez (Ch. 21), and Contra resupply network.",
        "url": "https://irp.fas.org/offdocs/walsh/",
        "source_type": "government",
        "author": "Lawrence Walsh",
        "year": 1993,
    },
    {
        "id": 398,
        "title": "Kerry Committee — 'Drugs, Law Enforcement and Foreign Policy' (April 13, 1989). 1,166-page Senate report documenting Contra drug trafficking, SETCO as principal Contra airline, State Dept contracts with drug trafficker-controlled companies.",
        "url": "https://archive.org/details/Kerry-Report-Drugs-Contras",
        "source_type": "congressional",
        "author": "Senate Subcommittee on Terrorism, Narcotics, and International Operations",
        "year": 1989,
    },
    {
        "id": 399,
        "title": "National Security Archive — Oliver North Notebooks declassified (2,000 pages, released May 1990 after FOIA lawsuit). Contains entries noting awareness of drug connections, planes used to 'run drugs,' criminal records of crew.",
        "url": "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB113/index.htm",
        "source_type": "foia",
        "year": 1990,
    },
    {
        "id": 400,
        "title": "CIA Reading Room — Manuel Noriega documents (CIA-RDP90M00005R000700110051-2). Documents CIA payments to Noriega; George H.W. Bush paid Noriega $110,000 as CIA Director in 1976.",
        "url": "https://www.cia.gov/readingroom/document/cia-rdp90m00005r000700110051-2",
        "source_type": "foia",
        "year": 1976,
    },
    {
        "id": 401,
        "title": "National Security Archive — 'Operation Condor: A Network of Transnational Repression — 50 Years' (declassified State Department and CIA documents confirming U.S. facilitation of communications for Condor)",
        "url": "https://nsarchive.gwu.edu/briefing-book/southern-cone/2025-11-26/operation-condor-network-transnational-repression-50-years",
        "source_type": "foia",
        "year": 2025,
    },
    {
        "id": 402,
        "title": "Church Commission — 'Covert Action in Chile, 1963-1973' (Senate Select Committee, 1975). Found U.S. covert involvement 'extensive and continuous,' $8 million spent on Chilean intervention 1970-1973.",
        "url": "https://www.intelligence.senate.gov/sites/default/files/94chile.pdf",
        "source_type": "congressional",
        "year": 1975,
    },
    {
        "id": 403,
        "title": "Gary Webb — 'Dark Alliance: The CIA, the Contras, and the Crack Cocaine Explosion' (San Jose Mercury News, August 18-20, 1996; expanded into book 1998). Documented Contra-linked dealers funneling cocaine profits to CIA-backed Contras.",
        "url": "https://www.democracynow.org/2014/10/6/inside_the_dark_alliance_gary_webb",
        "source_type": "journalism",
        "author": "Gary Webb",
        "year": 1996,
    },
    {
        "id": 404,
        "title": "The Intercept — 'Managing a Nightmare: How the CIA Watched Over the Destruction of Gary Webb' (2014, FOIA documents showing CIA actively tracked and facilitated media criticism of Webb)",
        "url": "https://theintercept.com/2014/09/25/managing-nightmare-cia-media-destruction-gary-webb/",
        "source_type": "journalism",
        "year": 2014,
    },
    {
        "id": 405,
        "title": "CIA Inspector General — Report on CIA-Contra drug trafficking allegations (1998, two volumes). Confirmed CIA 'failed to fully investigate or act upon allegations that the anti-Sandinista forces it supported were engaged in drug trafficking.'",
        "url": "https://irp.fas.org/cia/product/cocaine2/",
        "source_type": "government",
        "year": 1998,
    },
    {
        "id": 406,
        "title": "Colombia Reports — 'Colombia's former president on Jeffrey Epstein's Lolita jet flight logbook' (Andres Pastrana on March 2003 flights with Maxwell and Brunel)",
        "url": "https://colombiareports.com/colombias-former-president-on-jeffrey-epsteins-lolita-jet-flight-logbook/",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 407,
        "title": "ColombiaOne — 'Epstein Files: Latin America's Elite' (February 2026, Pastrana's 37 document references, photos with Maxwell in Colombian Air Force uniforms, criminal complaint filed)",
        "url": "https://colombiaone.com/2026/02/10/epstein-files-latin-america-elite/",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 408,
        "title": "DropSite News — 'Jeffrey Epstein, Iran-Contra Planes, Leslie Wexner' (December 2025, Ryan Grim/Maz Hussain/Sam Berger). Epstein facilitated Wexner's acquisition of SAT aircraft previously used in Iran-Contra, relocated to Columbus, Ohio.",
        "url": "https://www.dropsitenews.com/p/jeffrey-epstein-iran-contra-planes-leslie-wexner-pottinger-leese-arms-weapons-smuggling",
        "source_type": "journalism",
        "author": "Ryan Grim, Maz Hussain, Sam Berger",
        "year": 2025,
    },
    {
        "id": 409,
        "title": "SOA Watch — 'Notorious SOA Graduates' (comprehensive list of School of the Americas graduates involved in human rights abuses, coups, and atrocities across Latin America)",
        "url": "https://soaw.org/notorious-soa-graduates",
        "source_type": "journalism",
        "year": 2024,
    },
    {
        "id": 410,
        "title": "National Security Archive — 'Chile and the United States: Declassified Documents' (NSA briefing books including declassified PDB from September 11, 1973 coup, Kissinger phone recordings)",
        "url": "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB8/nsaebb8i.htm",
        "source_type": "foia",
        "year": 2023,
    },
    {
        "id": 411,
        "title": "CIA Inspector General — 'Allegations of Connections Between CIA and the Contras in Cocaine Trafficking' (Volume II: The Contra Story). Names SETCO as principal Contra airline, documents pilot drug trafficking.",
        "url": "https://irp.fas.org/cia/product/cocaine2/pilots.html",
        "source_type": "government",
        "year": 1998,
    },
    {
        "id": 412,
        "title": "DOJ Office of Inspector General — 'The CIA-Contra-Crack Cocaine Controversy' (1997). Chapter 11 covers John Hull's Costa Rica ranch, DEA informant reports of cocaine at Hull's airstrip.",
        "url": "https://oig.justice.gov/sites/default/files/archive/special/9712/ch11p2.htm",
        "source_type": "government",
        "year": 1997,
    },
    {
        "id": 413,
        "title": "MercoPress — 'Colombia ruling-party candidate to file criminal complaint against ex-president Pastrana over Epstein files' (February 9, 2026)",
        "url": "https://en.mercopress.com/2026/02/09/colombia-ruling-party-candidate-to-file-criminal-complaint-against-ex-president-pastrana-over-epstein-files",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 414,
        "title": "National Security Archive — 'Oliver North's Checkered Iran-Contra Record' (declassified notebooks, congressional testimony, shredding of documents)",
        "url": "https://nsarchive.gwu.edu/briefing-book/iran/2018-05-16/oliver-norths-checkered-iran-contra-record",
        "source_type": "foia",
        "year": 2018,
    },
    {
        "id": 415,
        "title": "National Security Archive — 'Operation Condor: Cable Suggests U.S. Role' (declassified 2001, State Department document confirming U.S. facilitated communications for Condor network)",
        "url": "https://nsarchive2.gwu.edu/NSAEBB/NSAEBB73/",
        "source_type": "foia",
        "year": 2001,
    },
    {
        "id": 416,
        "title": "NBC News — 'New Mexico AG reopens investigation into Epstein's Zorro Ranch' (February 2026, AG Raul Torrez acts on information from DOJ file release)",
        "url": "https://www.nbcnews.com/politics/politics-news/new-mexico-probe-jeffrey-epstein-zorro-ranch-rcna259292",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 417,
        "title": "J. Patrice McSherry — 'Predatory States: Operation Condor and Covert War in Latin America' (academic, Rowman & Littlefield, 2005). Documents at least 654 victims of transnational kidnapping, torture, and disappearance.",
        "url": "https://rowman.com/ISBN/9780742536876",
        "source_type": "academic",
        "author": "J. Patrice McSherry",
        "year": 2005,
    },
    {
        "id": 418,
        "title": "Senate BCCI Report — 'The BCCI Affair' (Kerry-Brown, 1992). Chapter 4 covers BCCI criminality including Noriega's $23M laundered through BCCI London branches, Amjad Awan as Noriega's personal banker.",
        "url": "https://irp.fas.org/congress/1992_rpt/bcci/04crime.htm",
        "source_type": "congressional",
        "year": 1992,
    },
]


# ============================================================
# ENTITIES — 11 new (6 people + 3 organizations + 1 program + 1 event)
# ============================================================

ENTITIES = [
    # --- PEOPLE ---
    {
        "name": "Oliver North",
        "entity_type": "person",
        "description": (
            "U.S. Marine Lt. Colonel and National Security Council staff member under "
            "Reagan. Primary operational coordinator of the Iran-Contra affair — directed "
            "the White House covert Contra resupply program from the NSC.\n\n"
            "Declassified notebooks (2,000 pages, released May 1990 after FOIA lawsuit by "
            "National Security Archive) contain entries noting awareness of drug connections: "
            "one entry notes a DC-4 acquired through 'Foley' was 'used at one time to run "
            "drugs, and part of the crew had criminal records.' The plane belonged to Miami "
            "company Vortex, run by Michael Palmer, one of the largest marijuana traffickers "
            "in the U.S. Palmer received over $300,000 from the Nicaraguan Humanitarian Aid "
            "Office (NHAO) for Contra supply flights.\n\n"
            "In 1984, intervened to get Honduran General Jose Bueso Rosa a reduced sentence "
            "to protect the Contra program — Bueso Rosa had plotted to assassinate the "
            "Honduran president and fund it with proceeds from 760 pounds of cocaine.\n\n"
            "Televised congressional testimony July 7-14, 1987. Convicted of aiding "
            "obstruction of Congress, accepting illegal gratuity, and altering/destroying "
            "documents. Conviction reversed on appeal (tainted by immunized testimony)."
        ),
        "metadata": {},
    },
    {
        "name": "Manuel Noriega",
        "entity_type": "person",
        "description": (
            "Head of Panamanian military intelligence (G-2) from 1968; de facto ruler of "
            "Panama 1983-1989. Born February 11, 1934, Panama City. Died May 29, 2017.\n\n"
            "On CIA payroll from 1971 despite U.S. knowledge of his drug trafficking. CIA "
            "Director George H.W. Bush paid Noriega $110,000 in 1976. Carter suspended "
            "payments; Reagan reinstated in 1981. Received $200,000 from CIA in 1986 alone. "
            "Payroll cut off 1987 after protests.\n\n"
            "Iran-Contra role: supported Contra resupply operations through Panama in exchange "
            "for U.S. turning blind eye to drug trafficking. BCCI laundered $23 million of "
            "Noriega's criminal proceeds through London branches; his personal BCCI banker "
            "was Amjad Awan (convicted 1991, 12-year sentence). Graduate of the U.S. Army "
            "School of the Americas.\n\n"
            "December 20, 1989: U.S. invaded Panama (Operation Just Cause). Noriega "
            "surrendered January 3, 1990. Convicted April 1992 on 8 of 10 charges (drug "
            "trafficking, racketeering, money laundering). Sentenced to 40 years."
        ),
        "metadata": {},
    },
    {
        "name": "Felix Rodriguez",
        "entity_type": "person",
        "description": (
            "Cuban-American CIA paramilitary operations officer. Born 1941 in Havana. Career "
            "spanning three decades of CIA operations across four continents.\n\n"
            "Bay of Pigs (1961): entered Cuba clandestinely before the invasion for "
            "intelligence gathering. Bolivia (1967): CIA recruited Rodriguez to head the team "
            "hunting Che Guevara; interrogated Guevara, present at his execution. Vietnam "
            "(1971): flew over 300 helicopter sorties for Operation Phoenix, shot down 5 "
            "times.\n\n"
            "Iran-Contra: ran the Contra supply depot at Ilopango Air Base in El Salvador "
            "from September 1985, using alias 'Maximo (Max) Gomez.' Established relationship "
            "with Salvadoran General Juan Rafael Bustillo. Met regularly with Oliver North. "
            "Met Reagan and Bush at the White House during height of operations.\n\n"
            "Autobiography: 'Shadow Warrior: The CIA Hero of a Hundred Unknown Battles' (1989)."
        ),
        "metadata": {},
    },
    {
        "name": "Augusto Pinochet",
        "entity_type": "person",
        "description": (
            "Military general who seized power September 11, 1973 in CIA-backed coup "
            "overthrowing democratically elected President Salvador Allende of Chile. Born "
            "November 25, 1915. Died December 10, 2006.\n\n"
            "CIA spent $8 million between 1970-1973 on Chilean intervention — over $3 million "
            "in 1972 alone. Church Commission (1975) found U.S. covert involvement 'extensive "
            "and continuous' from 1963-1973. Declassified 2023 documents show Nixon and "
            "Kissinger knew of military plans to overthrow Allende days before the coup. CIA "
            "briefed Nixon on the morning of the coup that Chilean military were 'determined "
            "to restore political and economic order.'\n\n"
            "Chile was a founding member and key coordinator of Operation Condor — the "
            "transnational repression network across Southern Cone dictatorships. At least "
            "654 documented victims of transnational kidnapping, torture, and disappearance."
        ),
        "metadata": {},
    },
    {
        "name": "Gary Webb",
        "entity_type": "person",
        "description": (
            "Investigative journalist. Born August 31, 1955, Corona, California.\n\n"
            "'Dark Alliance': published August 18-20, 1996 in the San Jose Mercury News. "
            "Three-part series documenting that Nicaraguan Contra-linked drug dealers funneled "
            "cocaine profits to CIA-backed Contras, and this cocaine fueled the Los Angeles "
            "crack epidemic. Expanded into book (1998).\n\n"
            "Media backlash: Washington Post, NYT, and LA Times attacked the series. Mercury "
            "News editor Jerry Ceppos published a partial retraction. Webb was reassigned and "
            "resigned. FOIA documents obtained by The Intercept (2014) revealed CIA actively "
            "tracked and facilitated the media destruction — internal CIA memo titled "
            "'Managing a Nightmare.'\n\n"
            "Partial vindication: 1998 CIA Inspector General Frederick Hitz released two "
            "reports confirming CIA 'failed to fully investigate or act upon allegations that "
            "the anti-Sandinista forces it supported were engaged in drug trafficking.'\n\n"
            "Died December 10, 2004, Sacramento. Found with two gunshot wounds to the head. "
            "Sacramento County coroner ruled suicide."
        ),
        "metadata": {},
    },
    {
        "name": "Andres Pastrana",
        "entity_type": "person",
        "description": (
            "President of Colombia 1998-2002. Born August 17, 1954, Bogota.\n\n"
            "Appears on Jeffrey Epstein flight logs: March 20, 2003 flight from Teterboro "
            "to Palm Beach, and March 21 from Palm Beach to Nassau. Ghislaine Maxwell and "
            "Jean-Luc Brunel were on both flights. Pastrana admitted traveling from Nassau to "
            "Havana, Cuba at invitation of Fidel Castro, using Epstein's transport — this leg "
            "does NOT appear in FAA records.\n\n"
            "Referenced in at least 37 files in the January 2026 DOJ release, including email "
            "exchanges with Maxwell from 2003-2004. Released files include photos of Pastrana "
            "and Maxwell wearing Colombian Air Force pilot uniforms. Maxwell claimed Pastrana "
            "organized 'the party' in Colombia where she flew a Black Hawk helicopter over "
            "the Amazon. April 2003 FedEx shipment from Epstein to Pastrana documented.\n\n"
            "February 9, 2026: Colombian ruling-party candidate filed criminal complaint "
            "against Pastrana over the Epstein files."
        ),
        "metadata": {},
    },
    # --- ORGANIZATIONS ---
    {
        "name": "Medellín Cartel",
        "entity_type": "organization",
        "description": (
            "Colombian drug cartel based in Medellín, active 1976-1993. Responsible for the "
            "majority of cocaine entering the United States in the 1980s.\n\n"
            "Intelligence connections: CIA supported paramilitary groups fighting Pablo "
            "Escobar in 1992-93. CIA provided materiel support and helped form Los Pepes "
            "(Perseguidos por Pablo Escobar), combining Cali Cartel members, Escobar's "
            "former associates, and Colombian military. U.S. Embassy Joint Task Force worked "
            "with the Colombian Search Bloc that killed Escobar on December 2, 1993.\n\n"
            "BCCI connection: Operation C-Chase (U.S. Customs/IRS undercover operation, "
            "1986-1988) convicted six BCCI officers and a Colombian businessman of laundering "
            "$14 million in Medellín cocaine profits through BCCI Panama, Luxembourg, and "
            "LOANS Switzerland.\n\n"
            "Barry Seal worked as cocaine courier for the cartel while simultaneously working "
            "for CIA and DEA. Seal imported an estimated $3-5 billion worth of drugs / ~56 "
            "tons of cocaine into the U.S. The cartel assassinated Seal on February 19, 1986 "
            "in Baton Rouge."
        ),
        "metadata": {},
    },
    {
        "name": "SETCO Aviation",
        "entity_type": "organization",
        "description": (
            "Aviation company based in Honduras. Founded by Honduran drug lord Juan Matta "
            "Ballesteros — a 1983 U.S. Customs Investigative Report stated: 'SETCO Aviation "
            "is a corporation formed by American businessmen who are dealing with Juan Matta "
            "Ballesteros and are smuggling narcotics into the United States.'\n\n"
            "Beginning in 1984, SETCO was the principal company used by the Contras in "
            "Honduras to transport supplies and personnel for the FDN (Fuerza Democratica "
            "Nicaraguense). Simultaneously transported cocaine to the U.S. from Honduras.\n\n"
            "Matta Ballesteros was classified by the DEA as a 'Class I DEA violator' — "
            "identified in 1985 as responsible for 'perhaps a third, perhaps more than half' "
            "of all cocaine moving from Colombia to the United States. He was also involved "
            "in the 1985 murder of DEA agent Enrique Camarena. When the local DEA office "
            "moved against Matta in 1983, 'it was shut down.'\n\n"
            "Named in both the Kerry Committee Report and CIA Inspector General Report as "
            "the key example of drug trafficker-Contra symbiosis."
        ),
        "metadata": {},
    },
    {
        "name": "School of the Americas",
        "entity_type": "organization",
        "description": (
            "U.S. military training institution at Fort Benning (now Fort Moore), Columbus, "
            "Georgia. Founded 1946. Trained over 60,000 Latin American military, law "
            "enforcement, and security personnel by 2000. Renamed WHINSEC (Western Hemisphere "
            "Institute for Security Cooperation) in 2001 after sustained criticism.\n\n"
            "Notable graduates include: Manuel Noriega (Panama dictator), Hugo Banzer Suarez "
            "(Bolivia dictator), Efrain Rios Montt (Guatemala dictator, convicted of "
            "genocide), plus officers involved in: the 1981 El Mozote massacre (900 civilians "
            "killed, El Salvador), 1980 assassination of Archbishop Oscar Romero (El "
            "Salvador), and 1989 Jesuit massacre (6 priests + housekeeper + daughter at UCA, "
            "El Salvador — UN panel found 19 of 27 killers were SOA graduates).\n\n"
            "Declassified CIA documents from 1976 show plans for Operation Condor were "
            "developed at the School of the Americas."
        ),
        "aliases": "SOA, WHINSEC, Western Hemisphere Institute for Security Cooperation",
        "metadata": {},
    },
    # --- PROGRAM ---
    {
        "name": "Operation Condor",
        "entity_type": "program",
        "description": (
            "Formal system to coordinate repression among Southern Cone countries: Argentina, "
            "Uruguay, Chile, Paraguay, Bolivia, Brazil. Active mid-1970s to early 1980s.\n\n"
            "U.S. support documented: Washington provided military intelligence, training, "
            "financial assistance, advanced computers, tracking technology, and access to a "
            "continental telecommunications system ('Condortel') housed in the Panama Canal "
            "Zone. CIA provided computers for storing databanks of thousands of politically "
            "suspect individuals.\n\n"
            "At least 654 documented victims of transnational kidnapping, torture, and "
            "disappearance between 1976-1980. Declassified 2001 State Department document "
            "confirmed U.S. facilitated communications for Condor. Kissinger was Secretary "
            "of State during its establishment; declassified documents show Nixon/Kissinger "
            "awareness and support.\n\n"
            "Plans were developed at the U.S. Army School of the Americas. Chile under "
            "Pinochet was a founding member and key coordinator."
        ),
        "metadata": {},
    },
    # --- EVENT ---
    {
        "name": "Kerry Committee Investigation",
        "entity_type": "event",
        "description": (
            "Senate Subcommittee on Terrorism, Narcotics, and International Operations, "
            "chaired by Senator John Kerry. Investigated 1987-1989. Produced a 1,166-page "
            "report released April 13, 1989: 'Drugs, Law Enforcement and Foreign Policy.'\n\n"
            "Key findings:\n"
            "- 'Substantial evidence of drug smuggling... on the part of individual Contras, "
            "Contra suppliers, Contra pilots, mercenaries who worked with the Contras, and "
            "Contra supporters.'\n"
            "- 'Senior U.S. policy makers were not immune to the idea that drug money was a "
            "perfect solution to the Contras' funding problems.'\n"
            "- State Department chose four companies controlled by drug traffickers to provide "
            "Contra humanitarian assistance — drug traffickers received U.S. taxpayer funds.\n"
            "- Named SETCO Aviation as the principal Contra supply airline, owned by drug "
            "trafficker Juan Matta Ballesteros.\n\n"
            "Kerry also led the Senate investigation into BCCI, tracking drug traffickers to "
            "Noriega (1988) and Noriega's dirty money to BCCI and 'some of the top "
            "powerbrokers in Washington.'"
        ),
        "metadata": {},
    },
]


# ============================================================
# RELATIONSHIPS — ~30 new connections
# ============================================================

RELATIONSHIPS = [
    # =========================================
    # GROUP 1: IRAN-CONTRA LATIN DIMENSION (10)
    # =========================================
    {
        "source": "Oliver North",
        "target": "Iran-Contra",
        "type": "coordinated",
        "tier": "documented",
        "desc": "Primary NSC operational coordinator of the Iran-Contra affair. Directed the White House covert Contra resupply program. Declassified notebooks show awareness of drug trafficking connections. Convicted (reversed on appeal).",
        "sources": [397, 399, 414],
    },
    {
        "source": "Oliver North",
        "target": "Felix Rodriguez",
        "type": "associated_with",
        "tier": "documented",
        "desc": "North and Rodriguez met regularly during Contra resupply operations. Rodriguez ran the supply depot at Ilopango Air Base in El Salvador; North coordinated from the NSC in Washington.",
        "sources": [397],
    },
    {
        "source": "Manuel Noriega",
        "target": "CIA",
        "type": "asset_of",
        "tier": "documented",
        "desc": "On CIA payroll from 1971. CIA Director George H.W. Bush paid Noriega $110,000 in 1976. Reagan reinstated payments in 1981. Received $200,000 in 1986 alone. Payroll cut 1987. U.S. invaded Panama to remove him December 1989.",
        "sources": [400, 397],
        "year_start": 1971,
        "year_end": 1987,
    },
    {
        "source": "Manuel Noriega",
        "target": "Iran-Contra",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Supported Contra resupply operations through Panama in exchange for U.S. turning blind eye to his drug trafficking. Panama served as logistics hub for Contra supply chain.",
        "sources": [397, 398],
    },
    {
        "source": "Manuel Noriega",
        "target": "BCCI",
        "type": "client_of",
        "tier": "documented",
        "desc": "BCCI laundered $23 million of Noriega's criminal proceeds through London branches. Personal banker was BCCI officer Amjad Awan (convicted 1991, 12-year sentence). CIA payments to Noriega channeled through BCCI accounts.",
        "sources": [418, 398],
    },
    {
        "source": "Manuel Noriega",
        "target": "School of the Americas",
        "type": "trained_at",
        "tier": "documented",
        "desc": "Graduate of the U.S. Army School of the Americas at Fort Benning, Georgia. One of many Latin American dictators trained there.",
        "sources": [409],
    },
    {
        "source": "Felix Rodriguez",
        "target": "CIA",
        "type": "asset_of",
        "tier": "documented",
        "desc": "Career CIA paramilitary officer spanning three decades: Bay of Pigs (1961), Che Guevara capture and execution in Bolivia (1967), Operation Phoenix in Vietnam (1971), Iran-Contra resupply from El Salvador (1985+). Met Reagan and Bush at the White House.",
        "sources": [397],
        "year_start": 1961,
    },
    {
        "source": "Felix Rodriguez",
        "target": "Iran-Contra",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Ran the Contra supply depot at Ilopango Air Base in El Salvador from September 1985 using alias 'Maximo Gomez.' Managed resupply flights. Regular contact with Oliver North.",
        "sources": [397],
        "year_start": 1985,
    },
    {
        "source": "SETCO Aviation",
        "target": "Iran-Contra",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Principal company used by the Contras in Honduras to transport supplies and personnel from 1984. Named in Kerry Committee Report and CIA IG Report. Simultaneously transported cocaine to the U.S. — owned by DEA 'Class I violator' Juan Matta Ballesteros.",
        "sources": [398, 411],
        "year_start": 1984,
    },
    {
        "source": "Manuel Noriega",
        "target": "George H.W. Bush",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Bush paid Noriega $110,000 as CIA Director in 1976. Noriega remained on CIA payroll through the Reagan/Bush era. Bush ultimately ordered the invasion of Panama (Operation Just Cause, December 1989) to remove him.",
        "sources": [400],
        "year_start": 1976,
        "year_end": 1989,
    },

    # =========================================
    # GROUP 2: OPERATION CONDOR (5)
    # =========================================
    {
        "source": "CIA",
        "target": "Operation Condor",
        "type": "operated",
        "tier": "documented",
        "desc": "CIA provided military intelligence, training, financial assistance, computers for surveillance databanks, and access to Condortel communications system in the Panama Canal Zone. Declassified State Department document (2001) confirmed U.S. facilitated communications.",
        "sources": [401, 415, 417],
        "year_start": 1975,
    },
    {
        "source": "Henry Kissinger",
        "target": "Operation Condor",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Secretary of State during Condor's establishment. Declassified documents show Nixon/Kissinger awareness and support. Church Commission found U.S. covert involvement in Chile 'extensive and continuous' from 1963-1973. $8 million spent on Chilean intervention alone.",
        "sources": [402, 410, 401],
    },
    {
        "source": "Augusto Pinochet",
        "target": "Operation Condor",
        "type": "participated_in",
        "tier": "documented",
        "desc": "Chile under Pinochet was a founding member and key coordinator of Operation Condor. At least 654 documented victims of transnational kidnapping, torture, and disappearance.",
        "sources": [401, 417],
        "year_start": 1975,
    },
    {
        "source": "Augusto Pinochet",
        "target": "CIA",
        "type": "installed_by",
        "tier": "documented",
        "desc": "CIA-backed coup overthrew President Allende on September 11, 1973. CIA spent $8 million on Chilean intervention 1970-1973. Declassified 2023 PDB shows CIA briefed Nixon on the morning of the coup. Church Commission documented 'extensive and continuous' covert involvement.",
        "sources": [402, 410],
        "year_start": 1973,
    },
    {
        "source": "Operation Condor",
        "target": "School of the Americas",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Declassified CIA documents from 1976 show plans for Operation Condor were developed at the School of the Americas and the Conference of American Armies.",
        "sources": [401, 409],
    },

    # =========================================
    # GROUP 3: DRUG-INTELLIGENCE NEXUS (7)
    # =========================================
    {
        "source": "Gary Webb",
        "target": "CIA",
        "type": "investigated",
        "tier": "documented",
        "desc": "'Dark Alliance' (1996) documented CIA-Contra-crack cocaine nexus. CIA responded with internal memo 'Managing a Nightmare' — actively tracked and facilitated media destruction of Webb. 1998 CIA IG confirmed CIA 'failed to investigate' Contra drug trafficking.",
        "sources": [403, 404, 405],
        "year_start": 1996,
    },
    {
        "source": "Gary Webb",
        "target": "Iran-Contra",
        "type": "investigated",
        "tier": "documented",
        "desc": "'Dark Alliance' focused specifically on Contra-linked drug dealers funneling cocaine profits to CIA-backed Contras, and this cocaine fueling the Los Angeles crack epidemic.",
        "sources": [403],
        "year_start": 1996,
    },
    {
        "source": "Kerry Committee Investigation",
        "target": "Iran-Contra",
        "type": "investigated",
        "tier": "documented",
        "desc": "Two-year Senate investigation (1987-1989) produced 1,166-page report documenting 'substantial evidence of drug smuggling on the part of individual Contras, Contra suppliers, Contra pilots.' Found senior policymakers were 'not immune to the idea that drug money was a perfect solution.'",
        "sources": [398],
        "year_start": 1987,
        "year_end": 1989,
    },
    {
        "source": "Kerry Committee Investigation",
        "target": "BCCI",
        "type": "investigated",
        "tier": "documented",
        "desc": "Kerry led both the Contra drug trafficking investigation and the BCCI investigation. Tracked drug traffickers to Noriega (1988), and Noriega's dirty money to BCCI and 'some of the top powerbrokers in Washington.'",
        "sources": [398, 418],
    },
    {
        "source": "Kerry Committee Investigation",
        "target": "SETCO Aviation",
        "type": "investigated",
        "tier": "documented",
        "desc": "Kerry Report named SETCO as the principal Contra supply airline, documented that it was owned by drug trafficker Juan Matta Ballesteros, and identified State Department contracts with drug trafficker-controlled companies.",
        "sources": [398, 411],
    },
    {
        "source": "Medellín Cartel",
        "target": "BCCI",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Operation C-Chase (U.S. Customs/IRS undercover operation, 1986-1988) convicted six BCCI officers of laundering $14 million in Medellín cocaine profits through BCCI Panama, Luxembourg, and LOANS Switzerland.",
        "sources": [418],
        "year_start": 1986,
    },
    {
        "source": "Barry Seal",
        "target": "Medellín Cartel",
        "type": "associated_with",
        "tier": "documented",
        "desc": "Worked as cocaine courier for the Medellín Cartel while simultaneously working for CIA and DEA. Imported an estimated $3-5 billion worth of drugs / ~56 tons of cocaine. Cartel assassinated Seal on February 19, 1986 in Baton Rouge.",
        "sources": [398, 405],
        "year_start": 1982,
        "year_end": 1986,
    },

    # =========================================
    # GROUP 4: EPSTEIN CONNECTIONS (4)
    # =========================================
    {
        "source": "Andres Pastrana",
        "target": "Jeffrey Epstein",
        "type": "associated_with",
        "tier": "documented",
        "desc": "On Epstein flight logs (March 2003, Teterboro→Palm Beach→Nassau). Referenced in at least 37 files in 2026 DOJ release. Email exchanges with Maxwell. FedEx shipment from Epstein to Pastrana (April 2003). February 2026: criminal complaint filed in Colombia.",
        "sources": [406, 407, 413],
        "year_start": 2003,
    },
    {
        "source": "Andres Pastrana",
        "target": "Ghislaine Maxwell",
        "type": "associated_with",
        "tier": "documented",
        "desc": "On the same March 2003 flights. Photos in released files show Pastrana and Maxwell wearing Colombian Air Force pilot uniforms. Maxwell claimed Pastrana organized 'the party' in Colombia where she flew a Black Hawk helicopter over the Amazon. Email exchanges 2003-2004.",
        "sources": [406, 407],
        "year_start": 2003,
    },
    {
        "source": "Andres Pastrana",
        "target": "Jean-Luc Brunel",
        "type": "associated_with",
        "tier": "documented",
        "desc": "On the same March 2003 flights (Teterboro→Palm Beach→Nassau). Epstein emailed Brunel (April 10, 2003): 'Call Pastrana about a big house in Cuba.'",
        "sources": [406, 407],
        "year_start": 2003,
    },
    {
        "source": "Southern Air Transport",
        "target": "Medellín Cartel",
        "type": "associated_with",
        "tier": "documented",
        "desc": "1996: Customs agents discovered cocaine aboard a SAT plane delivering 'fresh flowers' from Colombia. SAT was 'of record' in DEA's database from January 1985 through September 1990 for 'alleged involvement in cocaine trafficking.' SAT shut down in 1998 — weeks before CIA IG released findings on Contra cocaine.",
        "sources": [408, 405],
        "year_start": 1985,
        "year_end": 1998,
    },

    # =========================================
    # GROUP 5: CROSS-CONNECTIONS (4)
    # =========================================
    {
        "source": "School of the Americas",
        "target": "CIA",
        "type": "associated_with",
        "tier": "documented",
        "desc": "U.S. military institution that trained 60,000+ Latin American military/security personnel. Operation Condor plans developed there. Trained dictators (Noriega, Banzer, Rios Montt), death squad leaders, and coup participants across Latin America.",
        "sources": [409, 401],
        "year_start": 1946,
    },
    {
        "source": "Oliver North",
        "target": "CIA",
        "type": "associated_with",
        "tier": "documented",
        "desc": "NSC coordinator working closely with CIA on Contra resupply. North's notebooks document meetings with CIA officers and knowledge of CIA-connected drug trafficking by Contra supply pilots and companies.",
        "sources": [397, 399],
    },
    {
        "source": "SETCO Aviation",
        "target": "Medellín Cartel",
        "type": "associated_with",
        "tier": "documented",
        "desc": "SETCO's founder Juan Matta Ballesteros was identified by DEA as responsible for 'perhaps a third, perhaps more than half' of all cocaine from Colombia to the U.S. SETCO simultaneously served as the principal Contra supply airline — drug trafficking and Contra resupply were the same operation.",
        "sources": [398, 411],
    },
    {
        "source": "Medellín Cartel",
        "target": "CIA",
        "type": "associated_with",
        "tier": "documented",
        "desc": "CIA supported paramilitary groups fighting Escobar in 1992-93, helped form Los Pepes. Barry Seal worked for both the Medellín Cartel and CIA simultaneously. Kerry Committee and CIA IG documented the CIA-Contra-cocaine nexus. SETCO (owned by drug trafficker) served as principal Contra airline with CIA knowledge.",
        "sources": [405, 398, 411],
    },
]


# ============================================================
# ENTITY-SOURCE LINKS — which sources document each entity
# ============================================================

ENTITY_SOURCES = {
    "Oliver North": [397, 399, 414],
    "Manuel Noriega": [397, 398, 400, 418],
    "Felix Rodriguez": [397],
    "Augusto Pinochet": [401, 402, 410, 417],
    "Gary Webb": [403, 404, 405],
    "Andres Pastrana": [406, 407, 413, 416],
    "Medellín Cartel": [398, 405, 418],
    "SETCO Aviation": [398, 411],
    "School of the Americas": [401, 409],
    "Operation Condor": [401, 415, 417],
    "Kerry Committee Investigation": [398],
}
