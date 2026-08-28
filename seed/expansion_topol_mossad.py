"""
Chaim Topol / Mossad — Expansion layer for Intel Console.

April 2023 revelation: Haaretz reported that the family of Israeli actor
Chaim Topol (1935-2023) confirmed on the record that he worked for the
Mossad for years. His handler was Peter Zvi Malkin — the operative who
physically seized Adolf Eichmann in Buenos Aires in 1960. Topol's fame
as Tevye in Fiddler on the Roof functioned as operational cover, gaining
him access to countries where Israel had no official presence.

Also adds Benjamin Netanyahu (-> power branch) wired into the intelligence
cluster through Mossad oversight, Jonathan Pollard, and the 2025-2026
Iran operations.

Entities: Chaim Topol, Peter Zvi Malkin, Isser Harel, Eichmann Capture (1960),
          Fiddler on the Roof (1971 film), Six-Day War, Benjamin Netanyahu

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Mossad [88], Jonathan Pollard [522], Rafi Eitan [53], Donald Trump [33],
  Vladimir Putin [678], Unit 8200 [524], Meir Dagan [204],
  Shabtai Shavit [203], Efraim Halevy [207], James Angleton [17],
  Operation Roaring Lion [507], Operation Epic Fury [506],
  Operation Midnight Hammer [508], Ali Khamenei [499]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1500-1599
# ============================================================

SOURCES = [
    # ----- Topol / Mossad revelation (April 2023) -----
    {
        "id": 1500,
        "title": "Haaretz — Revealed: Chaim Topol's Secret Life as a Mossad Agent",
        "url": "https://www.haaretz.com/israel-news/2023-04-13/ty-article-magazine/.highlight/revealed-chaim-topols-secret-life-as-a-mossad-agent/00000187-7acb-d484-adef-facf860c0000",
        "source_type": "journalism",
        "author": "Haaretz",
        "year": 2023,
    },
    {
        "id": 1501,
        "title": "Times of Israel — Chaim Topol's Family Says He Had a Hidden Role as an Operative for Mossad",
        "url": "https://www.timesofisrael.com/chaim-topols-family-says-he-had-a-hidden-role-as-an-operative-for-mossad/",
        "source_type": "journalism",
        "author": "Times of Israel",
        "year": 2023,
    },
    {
        "id": 1502,
        "title": "Jerusalem Post — Chaim Topol's Secret Life as Mossad Operative Revealed by Family",
        "url": "https://www.jpost.com/israel-news/article-739243",
        "source_type": "journalism",
        "author": "Jerusalem Post",
        "year": 2023,
    },
    {
        "id": 1503,
        "title": "Deadline — Topol, Fiddler on the Roof Star, Was Secret Agent for Mossad, Family Claims",
        "url": "https://deadline.com/2023/04/topol-fiddler-on-the-roof-secret-agent-for-mossad-family-claims-1235326138/",
        "source_type": "journalism",
        "author": "Deadline",
        "year": 2023,
    },
    {
        "id": 1504,
        "title": "Jewish Chronicle — Chaim Topol's Family: Our Dad Wasn't a Secret Agent",
        "url": "https://www.thejc.com/news/world/chaim-topols-family-our-dad-wasnt-a-secret-agent-t7ddasvu",
        "source_type": "journalism",
        "author": "Jewish Chronicle",
        "year": 2023,
    },
    # ----- Topol biography -----
    {
        "id": 1505,
        "title": "Chaim Topol — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Chaim_Topol",
        "source_type": "other",
        "year": 2023,
    },
    # ----- Peter Zvi Malkin -----
    {
        "id": 1506,
        "title": "Peter Malkin — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Peter_Malkin",
        "source_type": "other",
        "year": 2023,
    },
    # ----- Isser Harel -----
    {
        "id": 1507,
        "title": "Isser Harel — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Isser_Harel",
        "source_type": "other",
        "year": 2023,
    },
    # ----- Eichmann Capture -----
    {
        "id": 1508,
        "title": "Capture and Trial of Adolf Eichmann — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Capture_and_trial_of_Adolf_Eichmann",
        "source_type": "other",
        "year": 2023,
    },
    {
        "id": 1509,
        "title": "Yad Vashem — The Eichmann Trial",
        "url": "https://www.yadvashem.org/holocaust/eichmann-trial.html",
        "source_type": "archive",
        "year": 2023,
    },
    # ----- Fiddler on the Roof (film) -----
    {
        "id": 1510,
        "title": "Fiddler on the Roof (film) — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Fiddler_on_the_Roof_(film)",
        "source_type": "other",
        "year": 2023,
    },
    # ----- Six-Day War -----
    {
        "id": 1511,
        "title": "Six-Day War — Britannica",
        "url": "https://www.britannica.com/event/Six-Day-War",
        "source_type": "other",
        "year": 2023,
    },
    # ----- Benjamin Netanyahu biography -----
    {
        "id": 1512,
        "title": "Benjamin Netanyahu — Britannica",
        "url": "https://www.britannica.com/biography/Benjamin-Netanyahu",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1513,
        "title": "ICC Pre-Trial Chamber I — Arrest Warrants for Netanyahu and Gallant (Situation in Palestine)",
        "url": "https://www.icc-cpi.int/news/situation-state-palestine-icc-pre-trial-chamber-i-rejects-state-israels-challenges",
        "source_type": "court",
        "year": 2024,
    },
    {
        "id": 1514,
        "title": "Times of Israel — Netanyahu Wraps Up Trial Testimony After 98 Hearings Across 18 Months",
        "url": "https://www.timesofisrael.com/netanyahu-wraps-up-trial-testimony-after-98-hearings-across-18-months/",
        "source_type": "journalism",
        "author": "Times of Israel",
        "year": 2026,
    },
    {
        "id": 1515,
        "title": "France24 — Convicted US Spy Pollard Welcomed by Netanyahu as He Arrives in Israel",
        "url": "https://www.france24.com/en/middle-east/20201230-convicted-us-spy-pollard-welcomed-by-netanyahu-as-he-arrives-in-israel",
        "source_type": "journalism",
        "author": "France24",
        "year": 2020,
    },
    {
        "id": 1516,
        "title": "Times of Israel — David Barnea, Former Top Agent, Appointed Next Mossad Chief",
        "url": "https://www.timesofisrael.com/david-barnea-former-top-agent-appointed-next-mossad-chief/",
        "source_type": "journalism",
        "author": "Times of Israel",
        "year": 2021,
    },
    {
        "id": 1517,
        "title": "NPR — Netanyahu Rejects Trump's Gaza Peace Plan",
        "url": "https://www.npr.org/2026/08/09/nx-s1-5926459/netanyahu-rejects-trump-gaza-peace-plan-israel-hamas",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2026,
    },
    {
        "id": 1518,
        "title": "NPR — Trump and Netanyahu Meet Amid Iran War Tensions",
        "url": "https://www.npr.org/2026/07/28/g-s1-135833/trump-netanyahu-iran-war",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2026,
    },
    {
        "id": 1519,
        "title": "Haaretz — Israel's 2026 Election Set for October 27",
        "url": "https://www.haaretz.com/israel-news/elections/2026-07-12/ty-article/.premium/israels-2026-election-will-take-place-on-october-27-netanyahu-coalition-says/",
        "source_type": "journalism",
        "author": "Haaretz",
        "year": 2026,
    },
    {
        "id": 1520,
        "title": "Al Jazeera — Israel to Hold National Elections on October 27",
        "url": "https://www.aljazeera.com/news/2026/7/12/israel-to-hold-national-elections-on-october-27-parliament-says",
        "source_type": "journalism",
        "author": "Al Jazeera",
        "year": 2026,
    },
    {
        "id": 1521,
        "title": "News on AIR — Israeli PM Netanyahu Confirms Israel-US Joint Military Operation on Iran",
        "url": "https://www.newsonair.gov.in/israeli-pm-netanyahu-confirms-israel-us-joint-military-operation-on-iran",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 1522,
        "title": "Kremlin.ru — Meeting with Prime Minister of Israel Benjamin Netanyahu (Jan 30, 2020)",
        "url": "https://en.kremlin.ru/events/president/news/62698",
        "source_type": "government",
        "year": 2020,
    },
    {
        "id": 1523,
        "title": "JTA — When Bibi Went to a Philly High School",
        "url": "https://www.jta.org/jewniverse/2015/when-bibi-went-to-a-philly-high-school",
        "source_type": "journalism",
        "author": "JTA",
        "year": 2015,
    },
    {
        "id": 1524,
        "title": "Yonatan Netanyahu — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Yonatan_Netanyahu",
        "source_type": "other",
        "year": 2023,
    },
]


# ============================================================
# ENTITIES — 7 new
# ============================================================

ENTITIES = [
    {
        "name": "Chaim Topol",
        "entity_type": "person",
        "description": (
            "Chaim Topol (9 September 1935 - 8 March 2023). Israeli actor best known as "
            "Tevye in Fiddler on the Roof on London's West End (from February 1967) and in "
            "Norman Jewison's 1971 film (Oscar nomination Best Actor, Golden Globe win). "
            "Earlier starred in Sallah Shabati (1964, Golden Globe). Played Milos Columbo in "
            "For Your Eyes Only (1981). Israel Prize 2015. Served in the Nahal army "
            "entertainment troupe. Left his London Tevye run during the June 1967 Six-Day War "
            "for reserve duty, entertaining troops on the Golan Heights."
            "\n\n"
            "MOSSAD OPERATIVE: In April 2023, weeks after Topol's death from Alzheimer's, "
            "Haaretz reported that wife Galia, daughter Adi, and son Omer confirmed on the "
            "record that he worked for the Mossad for years. His handler was Peter Zvi Malkin, "
            "who visited the family in disguise. Topol carried a Minox camera and spool tape "
            "recorder. In one described operation, an Arab embassy in a European capital was "
            "bugged from a flat disguised as a dental clinic — Topol sat in the dentist's "
            "chair as a diversion while drilling masked the installation. His celebrity "
            "provided access to countries with no Israeli presence, including China and the "
            "Soviet Union. A Jewish Chronicle follow-up noted the family clarified some "
            "involvement concerned facilitating Jewish emigration from behind the Iron Curtain."
        ),
        "aliases": "Topol, Haim Topol",
        "metadata": {
            "nationality": "Israeli",
            "born": "1935-09-09",
            "died": "2023-03-08",
            "status": "deceased",
            "role": "Actor, Mossad operative",
        },
    },
    {
        "name": "Peter Zvi Malkin",
        "entity_type": "person",
        "description": (
            "Peter Zvi Malkin (27 May 1927 - 1 March 2005). Israeli intelligence operative "
            "who served 27 years in the Mossad (1948-1976), rising to Chief of Operations. "
            "Best known for physically seizing Adolf Eichmann on Garibaldi Street in San "
            "Fernando, Buenos Aires, on 11 May 1960 — the opening move of Operation Finale. "
            "Established a unit called Keshet that infiltrated embassies and airlines. Also "
            "served as handler for actor Chaim Topol during the latter's years as a Mossad "
            "operative, visiting Topol's family home in disguise and running operations "
            "including the bugging of an Arab embassy from a fake dental clinic. Post-service, "
            "Malkin became an artist and author in New York City."
        ),
        "aliases": "Zvi Malkin, Zvika Malkin, Peter Z. Malkin",
        "metadata": {
            "nationality": "Israeli",
            "born": "1927-05-27",
            "died": "2005-03-01",
            "status": "deceased",
            "role": "Mossad Chief of Operations",
        },
    },
    {
        "name": "Isser Harel",
        "entity_type": "person",
        "description": (
            "Isser Harel (1912 - 18 February 2003). Born Yisrael Halperin in Vitebsk, "
            "Russian Empire. Director of the Mossad from 1952 to 1963, while simultaneously "
            "heading the Shin Bet — an unprecedented dual role in Israeli intelligence. "
            "Personally directed Operation Finale, the capture of Adolf Eichmann in Buenos "
            "Aires in May 1960, traveling to Argentina to oversee the operation on the ground. "
            "Under his directorship, the Mossad expanded from a small domestic-focused service "
            "into a globally active intelligence agency. Succeeded by Meir Amit in 1963 after "
            "a dispute with Prime Minister David Ben-Gurion."
        ),
        "aliases": "Yisrael Halperin, Isser Halperin",
        "metadata": {
            "nationality": "Israeli",
            "born": "1912",
            "died": "2003-02-18",
            "status": "deceased",
            "role": "Mossad Director 1952-1963",
        },
    },
    {
        "name": "Eichmann Capture (1960)",
        "entity_type": "event",
        "description": (
            "Operation Finale (Hebrew: Mivtza Finale). Mossad operation to capture Adolf "
            "Eichmann, a senior architect of the Holocaust, in Buenos Aires, Argentina. On "
            "11 May 1960, a team led by Mossad director Isser Harel, with Rafi Eitan as "
            "operational commander and Peter Zvi Malkin executing the physical seizure, grabbed "
            "Eichmann on Garibaldi Street in San Fernando. He was sedated, disguised as El Al "
            "crew, and flown to Israel on 20 May. Trial opened 11 April 1961 in Jerusalem, "
            "broadcast worldwide. Executed by hanging on the night of 31 May-1 June 1962 at "
            "Ramla prison. The operation remains the most celebrated in Mossad history."
        ),
        "aliases": "Operation Finale, Operation Garibaldi, Mivtza Finale",
    },
    {
        "name": "Fiddler on the Roof (1971 film)",
        "entity_type": "publication",
        "description": (
            "Musical drama film directed by Norman Jewison, starring Chaim Topol as Tevye the "
            "milkman. Filmed at Pinewood Studios and on location in Yugoslavia (Mala Gorica "
            "and Lekenik, now Croatia). Released 3 November 1971. Topol received an Oscar "
            "nomination for Best Actor and won the Golden Globe for Best Actor in a Musical or "
            "Comedy. The role gave Topol international celebrity that, per his family's 2023 "
            "testimony to Haaretz, served as operational cover for Mossad intelligence missions "
            "in countries where Israel had no official presence."
        ),
        "aliases": "Fiddler on the Roof",
    },
    {
        "name": "Six-Day War",
        "entity_type": "event",
        "description": (
            "Arab-Israeli military conflict fought 5-10 June 1967 between Israel and the "
            "combined forces of Egypt, Syria, and Jordan. Decisive Israeli victory resulted "
            "in the capture of the Sinai Peninsula, Gaza Strip, West Bank, East Jerusalem, "
            "and the Golan Heights — tripling the territory under Israeli control. The war "
            "reshaped Middle Eastern geopolitics for decades. Multiple future Israeli "
            "intelligence and military leaders served in the conflict, including Meir Dagan "
            "(later Mossad director 2002-2011). Actor Chaim Topol left his London West End "
            "production of Fiddler on the Roof to return to Israel for reserve duty."
        ),
        "aliases": "1967 War, June War, Third Arab-Israeli War",
    },
    {
        "name": "Benjamin Netanyahu",
        "entity_type": "person",
        "description": (
            "Benjamin Netanyahu (born 21 October 1949, Tel Aviv). Prime Minister of Israel "
            "(1996-1999, 2009-2021, 2022-present). Grew up in Cheltenham Township, "
            "Pennsylvania (1963-1967); returned to Israel to enlist after high school. Served "
            "in Sayeret Matkal special forces. Brother Yonatan killed commanding the Entebbe "
            "rescue on 4 July 1976; founded the Jonathan Institute in his memory. As PM, holds "
            "direct authority over Mossad; appointed David Barnea as director in June 2021. "
            "Lobbied for decades for convicted spy Jonathan Pollard's release, personally "
            "greeting him at Ben Gurion Airport on 30 December 2020."
            "\n\n"
            "Authorized Operation Midnight Hammer (June 2025 strikes on Iran's nuclear "
            "infrastructure) and Operation Roaring Lion (February 28, 2026 coordinated strikes "
            "with US Operation Epic Fury). Met Trump on 28 July 2026; rejected Trump's "
            "15-point Gaza peace plan on 9 August 2026. ICC Pre-Trial Chamber I issued arrest "
            "warrant on 21 November 2024 for war crimes and crimes against humanity in Gaza. "
            "Ongoing corruption trial (Cases 1000/2000/4000 — fraud, breach of trust, bribery); "
            "testimony completed June 2026 after 98 hearings over 18 months. Israeli election "
            "set for 27 October 2026 after Knesset dissolution in July 2026."
        ),
        "aliases": "Bibi, Bibi Netanyahu",
        "metadata": {
            "nationality": "Israeli",
            "born": "1949-10-21",
            "status": "active",
            "role": "Prime Minister of Israel (1996-99, 2009-21, 2022-present)",
        },
    },
]


# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ================================================================
    # CHAIM TOPOL
    # ================================================================
    {
        "source": "Chaim Topol",
        "target": "Mossad",
        "type": "asset_of",
        "tier": "credible",
        "desc": (
            "On-record family testimony reported by Haaretz (April 2023). Wife Galia, "
            "daughter Adi, and son Omer confirmed Topol worked for the Mossad for years "
            "with Peter Zvi Malkin as handler. Tier is credible rather than documented "
            "because the confirmation is journalistic (family interview) not official "
            "government disclosure. A Jewish Chronicle follow-up noted the family pushed "
            "back on the full 'secret agent' characterization, clarifying some missions "
            "concerned facilitating Jewish emigration."
        ),
        "sources": [1500, 1501, 1502, 1504],
    },
    {
        "source": "Peter Zvi Malkin",
        "target": "Chaim Topol",
        "type": "handler_of",
        "tier": "credible",
        "desc": (
            "Family testimony in Haaretz (April 2023) identified Malkin as Topol's Mossad "
            "handler. Wife Galia recalled Malkin visiting the family home in disguise, "
            "entering through the backyard. Daughter Adi recounted asking Malkin how he got "
            "in without a key; he replied: 'You call that a lock?' Malkin and Topol ran "
            "operations including the bugging of an Arab embassy from a fake dental clinic."
        ),
        "sources": [1500, 1501, 1506],
    },
    {
        "source": "Chaim Topol",
        "target": "Fiddler on the Roof (1971 film)",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "Starred as Tevye in the 1971 Norman Jewison film. Oscar nomination for Best "
            "Actor (lost to Gene Hackman); Golden Globe win for Best Actor Musical or Comedy. "
            "Also played Tevye on London's West End from February 1967."
        ),
        "sources": [1505, 1510],
    },
    {
        "source": "Chaim Topol",
        "target": "Fiddler on the Roof (1971 film)",
        "type": "used_as_cover",
        "tier": "credible",
        "desc": (
            "Family testimony confirmed to Haaretz that Topol's international celebrity "
            "as Tevye functioned as operational cover for Mossad missions. His fame gave "
            "him access to countries where Israel had no official presence, including China "
            "and the Soviet Union. Mossad missions coincided with his years playing Tevye "
            "on London's West End."
        ),
        "sources": [1500, 1501, 1503],
    },
    {
        "source": "Chaim Topol",
        "target": "Six-Day War",
        "type": "participated_in",
        "tier": "credible",
        "desc": (
            "Left his London West End production of Fiddler on the Roof during the June "
            "1967 Six-Day War to return to Israel. Assigned to reserve duty with the army "
            "entertainment troupe on the Golan Heights."
        ),
        "sources": [1500, 1505],
    },

    # ================================================================
    # PETER ZVI MALKIN
    # ================================================================
    {
        "source": "Peter Zvi Malkin",
        "target": "Mossad",
        "type": "worked_for",
        "tier": "documented",
        "desc": (
            "Served 27 years in the Mossad (1948-1976), rising to Chief of Operations. "
            "Established a unit called Keshet that infiltrated embassies and airlines. "
            "One of the longest-serving Mossad operatives of the founding generation."
        ),
        "sources": [1506],
    },
    {
        "source": "Peter Zvi Malkin",
        "target": "Eichmann Capture (1960)",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "Executed the physical seizure of Adolf Eichmann on Garibaldi Street in San "
            "Fernando, Buenos Aires, on 11 May 1960. Malkin grabbed Eichmann as he walked "
            "home from a bus stop, reportedly saying 'Un momentito, senor.' The capture was "
            "the opening move of Operation Finale."
        ),
        "sources": [1506, 1508],
    },

    # ================================================================
    # ISSER HAREL
    # ================================================================
    {
        "source": "Isser Harel",
        "target": "Mossad",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Director of the Mossad from 1952 to 1963 — the longest-serving director in "
            "the agency's history. Simultaneously headed the Shin Bet, an unprecedented dual "
            "role. Transformed Mossad from a small service into a globally active intelligence "
            "agency. Succeeded by Meir Amit."
        ),
        "year_start": 1952,
        "year_end": 1963,
        "sources": [1507],
    },
    {
        "source": "Isser Harel",
        "target": "Eichmann Capture (1960)",
        "type": "led",
        "tier": "documented",
        "desc": (
            "Personally directed Operation Finale from Buenos Aires. Traveled to Argentina "
            "to oversee the capture of Eichmann, manage the safe house, and coordinate the "
            "extraction to Israel. The operation, completed under his command, remains the "
            "most celebrated in Mossad history."
        ),
        "sources": [1507, 1508, 1509],
    },

    # ================================================================
    # EICHMANN CAPTURE — cross-links to existing entities
    # ================================================================
    {
        "source": "Rafi Eitan",
        "target": "Eichmann Capture (1960)",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "Served as operational commander of the Eichmann capture team in Buenos Aires "
            "under Isser Harel's overall direction. Eitan managed the field operatives, "
            "including Peter Zvi Malkin who executed the physical seizure. The same Rafi "
            "Eitan who later headed LAKAM and directed the Jonathan Pollard espionage "
            "operation."
        ),
        "sources": [1508, 1509],
    },
    {
        "source": "Mossad",
        "target": "Eichmann Capture (1960)",
        "type": "operated",
        "tier": "documented",
        "desc": (
            "The Eichmann capture was a Mossad operation conducted in May 1960 under "
            "director Isser Harel. The team kidnapped Adolf Eichmann from Buenos Aires "
            "and smuggled him to Israel for trial. The operation demonstrated Mossad's "
            "global reach and remains its most publicly celebrated mission."
        ),
        "sources": [1507, 1508, 1509],
    },

    # ================================================================
    # SIX-DAY WAR — cross-links
    # ================================================================
    {
        "source": "Meir Dagan",
        "target": "Six-Day War",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "Served as an IDF officer in the 1967 Six-Day War. Dagan was a decorated "
            "veteran of both the 1967 and 1973 wars, later rising to Major General before "
            "being appointed Mossad director in 2002 by PM Ariel Sharon."
        ),
        "sources": [1511],
    },

    # ================================================================
    # INTELLIGENCE CROSS-LINKS
    # ================================================================
    {
        "source": "James Angleton",
        "target": "Isser Harel",
        "type": "intelligence_link",
        "tier": "credible",
        "desc": (
            "Angleton served as CIA counterintelligence chief (1954-1975) and was the "
            "primary CIA liaison to Israeli intelligence during Harel's directorship of "
            "Mossad (1952-1963). The institutional relationship between CIA and Mossad "
            "was built during their overlapping tenures. Ronen Bergman documents this "
            "liaison as foundational to US-Israeli intelligence cooperation."
        ),
        "sources": [1507],
    },

    # ================================================================
    # BENJAMIN NETANYAHU
    # ================================================================
    {
        "source": "Benjamin Netanyahu",
        "target": "Donald Trump",
        "type": "ally_of",
        "tier": "documented",
        "desc": (
            "Longstanding political alliance. Trump recognized Jerusalem as Israel's capital "
            "(2017) and Israeli sovereignty over the Golan Heights (2019). The two coordinated "
            "on Operation Midnight Hammer (June 2025) and the broader Iran campaign. Met on "
            "28 July 2026 amid Iran tensions. Netanyahu rejected Trump's 15-point Gaza peace "
            "plan on 9 August 2026, demanding Hamas disarm first."
        ),
        "year_start": 2017,
        "sources": [1517, 1518, 1521],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Operation Roaring Lion",
        "type": "authorized",
        "tier": "documented",
        "desc": (
            "As Prime Minister, authorized Operation Roaring Lion — Israel's parallel "
            "military operation against Iran conducted in coordination with US Operation "
            "Epic Fury on 28 February 2026. Netanyahu publicly confirmed the joint US-Israel "
            "operation."
        ),
        "year_start": 2026,
        "sources": [1521, 1518],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Operation Midnight Hammer",
        "type": "authorized",
        "tier": "documented",
        "desc": (
            "As Prime Minister, authorized Operation Midnight Hammer — the June 2025 "
            "US/Israeli strikes on Iran's nuclear infrastructure at Natanz, Fordow, and "
            "Isfahan. This operation set the context for the broader military escalation "
            "culminating in Operation Roaring Lion / Epic Fury in February 2026."
        ),
        "year_start": 2025,
        "sources": [1518, 1521],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Operation Epic Fury",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Netanyahu confirmed the joint US-Israel military operation on Iran. While "
            "Operation Epic Fury was the US codename for the American component, Netanyahu "
            "coordinated directly with Trump on the combined campaign that included both "
            "Epic Fury and Israel's Operation Roaring Lion on 28 February 2026."
        ),
        "year_start": 2026,
        "sources": [1521, 1518],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Jonathan Pollard",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Netanyahu lobbied for decades for Pollard's release from US federal prison. "
            "Israel granted Pollard citizenship in 1995 under Netanyahu's advocacy. On "
            "30 December 2020, Netanyahu personally greeted Pollard at Ben Gurion Airport "
            "upon his emigration to Israel, presenting him with an Israeli ID and saying "
            "'Welcome home.'"
        ),
        "sources": [1515, 1512],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Vladimir Putin",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Approximately 20 documented meetings between 2009-2021 — more than twice "
            "as many as Netanyahu held with US presidents in the same period. Met in "
            "Moscow on 30 January 2020 to discuss the Middle East peace plan. Relationship "
            "strained after September 2018 IL-20 shootdown during an Israeli strike on Syria."
        ),
        "year_start": 2009,
        "sources": [1522, 1512],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Mossad",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "As Prime Minister, holds direct authority over the Mossad — the service "
            "reports to the PM. Appointed David Barnea as Mossad director in June 2021, "
            "tasking him with preventing Iran from acquiring nuclear weapons. Previously "
            "appointed Efraim Halevy as director during his first term (1998)."
        ),
        "year_start": 1996,
        "sources": [1516, 1512],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Efraim Halevy",
        "type": "appointed",
        "tier": "credible",
        "desc": (
            "Appointed Halevy as Mossad director in 1998 during his first term as Prime "
            "Minister. Halevy served until 2002, bridging the directorships of Shabtai "
            "Shavit and Meir Dagan. The PM appoints the Mossad director under Israeli law."
        ),
        "year_start": 1998,
        "sources": [1512],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Ali Khamenei",
        "type": "targeted",
        "tier": "documented",
        "desc": (
            "As PM, authorized the Israeli military operations (Operation Midnight Hammer "
            "in June 2025 and Operation Roaring Lion on 28 February 2026) that, in "
            "coordination with US Operation Epic Fury, resulted in the death of Supreme "
            "Leader Khamenei during the opening strikes."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1518, 1521],
    },
]


# ============================================================
# ENTITY -> SOURCE mappings
# ============================================================

ENTITY_SOURCES = {
    "Chaim Topol": [1500, 1501, 1502, 1503, 1504, 1505],
    "Peter Zvi Malkin": [1500, 1501, 1506],
    "Isser Harel": [1507, 1508],
    "Eichmann Capture (1960)": [1508, 1509],
    "Fiddler on the Roof (1971 film)": [1500, 1510],
    "Six-Day War": [1511],
    "Benjamin Netanyahu": [1512, 1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524],
}


# ============================================================
# ENTITY_UPDATES — modifications to existing DB entities
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "Mossad",
        "description_append": (
            "2023 update: In April 2023, Haaretz reported that the family of Israeli actor "
            "Chaim Topol (1935-2023) confirmed on the record that he worked as a Mossad "
            "operative for years, with Peter Zvi Malkin as his handler. Topol's international "
            "celebrity as Tevye in Fiddler on the Roof provided operational cover for "
            "intelligence missions in countries where Israel had no official presence. The "
            "revelation adds to the documented pattern of Mossad leveraging civilian assets — "
            "Robert Maxwell, Ari Ben-Menashe — for intelligence operations."
        ),
        "sources": [1500, 1501, 1502],
    },
]


# ============================================================
# GEO_COORDS — for every new entity
# ============================================================

GEO_COORDS = {
    "Chaim Topol": (32.0853, 34.7818, "inference", "Born and based in Tel Aviv"),
    "Peter Zvi Malkin": (40.7128, -74.0060, "credible", "Based in New York City post-service, died there 2005"),
    "Isser Harel": (32.0853, 34.7818, "inference", "Mossad HQ area, Tel Aviv"),
    "Eichmann Capture (1960)": (-34.4546, -58.5575, "documented", "Garibaldi Street, San Fernando, Buenos Aires"),
    "Fiddler on the Roof (1971 film)": (45.58, 16.18, "credible", "Filmed in Lekenik/Mala Gorica, Croatia (then Yugoslavia)"),
    "Six-Day War": (31.7683, 35.2137, "credible", "Jerusalem, focal point of the conflict"),
    "Benjamin Netanyahu": (31.7683, 35.2137, "inference", "Prime Minister's Office, Jerusalem"),
}


# ============================================================
# PHOTO_CANDIDATES — Wikimedia Commons URLs for persons
# ============================================================

PHOTO_CANDIDATES = {
    "Chaim Topol": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Chaim_Topol%2C_1967_%28cropped%29.jpg",
    "Benjamin Netanyahu": "https://upload.wikimedia.org/wikipedia/commons/7/74/Benjamin_Netanyahu%2C_February_2023.jpg",
}
