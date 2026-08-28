"""
Narrative Control — August 2026 expansion uplift for Intel Console.

Media ownership consolidation (Paramount-Skydance merger, TikTok US JV),
content moderation retreat (Meta fact-check removal), AI-government
partnerships (OpenAI-Pentagon, Anthropic-Palantir), FCC regulatory power,
propaganda theory lineage (Lippmann-Bernays-Mockingbird), prosperity gospel
political connections.

EXISTING ENTITIES wired in (unassigned -> narrative):
  Meta [890], OpenAI [889], Anthropic [891], Sean Parker [826],
  Walter Lippmann [836], Mark Lombardi [883], Joel Osteen [887],
  Kenneth Copeland [888]

Other existing entities referenced:
  Donald Trump [33], Mark Zuckerberg [825], Jeff Bezos [574],
  Paramount Global [584], Fox Corporation [580], Comcast Corporation [582],
  Dominion Voting Systems [345], Cambridge Analytica [343],
  Twitter Files [594], Telecommunications Act of 1996 [590],
  Edward Bernays [570], Council on Foreign Relations [702],
  Operation Mockingbird [588], BCCI [54], Iran-Contra [96],
  Banco Ambrosiano Collapse [459], Palantir Technologies [59],
  The Pentagon [180], Sam Altman [824], Dario Amodei [823],
  Internet Research Agency [347], News Corp [579],
  Jamal Khashoggi [687], Gaia, Inc. [613], David Wilcock [620]

Cross-module references (being created by other agents):
  Elon Musk (power module)

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES  (IDs 2000-2037)
# ============================================================

SOURCES = [
    # --- Wikipedia references (background / biographical) ---
    {
        "id": 2000,
        "title": "Paramount Global -- Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Paramount_Global",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2001,
        "title": "Skydance Media -- Wikipedia (David Ellison, Paramount merger)",
        "url": "https://en.wikipedia.org/wiki/Skydance_Media",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2002,
        "title": "David Ellison -- Wikipedia (biography, Paramount CEO)",
        "url": "https://en.wikipedia.org/wiki/David_Ellison",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2003,
        "title": "Larry Ellison -- Wikipedia (Oracle co-founder, TikTok JV)",
        "url": "https://en.wikipedia.org/wiki/Larry_Ellison",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2004,
        "title": "Federal Communications Commission -- Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Federal_Communications_Commission",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2005,
        "title": "Brendan Carr (FCC) -- Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Brendan_Carr_(lawyer)",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2006,
        "title": "Bari Weiss -- Wikipedia (journalist, CBS News EIC)",
        "url": "https://en.wikipedia.org/wiki/Bari_Weiss",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2007,
        "title": "TikTok -- Wikipedia (US ban, joint venture)",
        "url": "https://en.wikipedia.org/wiki/TikTok",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2008,
        "title": "Meta Platforms -- Wikipedia (fact-checking removal, FTC trial)",
        "url": "https://en.wikipedia.org/wiki/Meta_Platforms",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2009,
        "title": "OpenAI -- Wikipedia (restructuring, defense contracts)",
        "url": "https://en.wikipedia.org/wiki/OpenAI",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2010,
        "title": "Anthropic -- Wikipedia (Palantir partnership, defense deployment)",
        "url": "https://en.wikipedia.org/wiki/Anthropic",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2011,
        "title": "Mark Lombardi -- Wikipedia (network diagrams, BCCI/Iran-Contra art)",
        "url": "https://en.wikipedia.org/wiki/Mark_Lombardi",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2012,
        "title": "Walter Lippmann -- Wikipedia (Public Opinion, manufacture of consent)",
        "url": "https://en.wikipedia.org/wiki/Walter_Lippmann",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2013,
        "title": "Kenneth Copeland -- Wikipedia (televangelist, Trump spiritual advisor)",
        "url": "https://en.wikipedia.org/wiki/Kenneth_Copeland",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2014,
        "title": "Council on Foreign Relations -- Wikipedia (founding, membership)",
        "url": "https://en.wikipedia.org/wiki/Council_on_Foreign_Relations",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2015,
        "title": "Facebook-Cambridge Analytica data scandal -- Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2016,
        "title": "Telecommunications Act of 1996 -- Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Telecommunications_Act_of_1996",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 2017,
        "title": "Internet Research Agency -- Wikipedia (Russian influence operations)",
        "url": "https://en.wikipedia.org/wiki/Internet_Research_Agency",
        "source_type": "other",
        "year": 2026,
    },
    # --- Books ---
    {
        "id": 2018,
        "title": "Walter Lippmann -- Public Opinion (1922)",
        "url": "https://en.wikipedia.org/wiki/Public_Opinion_(book)",
        "source_type": "book",
        "author": "Walter Lippmann",
        "year": 1922,
    },
    {
        "id": 2019,
        "title": "Edward Bernays -- Propaganda (1928)",
        "url": "https://archive.org/details/bernays-propaganda",
        "source_type": "book",
        "author": "Edward Bernays",
        "year": 1928,
    },
    # --- Government / Official ---
    {
        "id": 2020,
        "title": "FCC -- About the FCC (official website, leadership)",
        "url": "https://www.fcc.gov/about/overview",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 2021,
        "title": "Meta -- More Speech and Fewer Mistakes (fact-check removal announcement)",
        "url": "https://about.fb.com/news/2025/01/meta-more-speech-fewer-mistakes/",
        "source_type": "other",
        "author": "Mark Zuckerberg",
        "year": 2025,
    },
    # --- Journalism (pre-cutoff, high-confidence URLs) ---
    {
        "id": 2022,
        "title": "Carl Bernstein -- The CIA and the Media (Rolling Stone, 1977)",
        "url": "https://www.carlbernstein.com/the-cia-and-the-media",
        "source_type": "journalism",
        "author": "Carl Bernstein",
        "year": 1977,
    },
    {
        "id": 2023,
        "title": "Sean Parker unloads on Facebook: 'God only knows what it's doing "
                 "to our children's brains' -- Axios",
        "url": "https://www.axios.com/2017/11/09/sean-parker-unloads-on-facebook-god-only-knows-what-its-doing-to-our-childrens-brains-1513306782",
        "source_type": "journalism",
        "author": "Mike Allen",
        "year": 2017,
    },
    {
        "id": 2024,
        "title": "How Trump Consultants Exploited the Facebook Data of Millions -- NYT",
        "url": "https://www.nytimes.com/2018/03/17/us/politics/cambridge-analytica-trump-campaign.html",
        "source_type": "journalism",
        "author": "Matthew Rosenberg, Nicholas Confessore, Carole Cadwalladr",
        "year": 2018,
    },
    {
        "id": 2025,
        "title": "Mark Lombardi: Global Networks -- Pierogi Gallery (artist documentation)",
        "url": "https://www.pierogi2000.com/artists/mark-lombardi/",
        "source_type": "other",
        "year": 2003,
    },
    # --- Journalism (2024-2026) ---
    {
        "id": 2026,
        "title": "Anthropic partners with Palantir to bring AI to defense and intelligence -- Reuters",
        "url": "https://www.reuters.com/technology/anthropic-partners-with-palantir-bring-ai-defense-intelligence-2024-11-04/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2024,
    },
    {
        "id": 2027,
        "title": "OpenAI partners with defense tech company Anduril -- Reuters",
        "url": "https://www.reuters.com/technology/openai-partners-with-anduril-defense-applications-2024-12-04/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2024,
    },
    {
        "id": 2028,
        "title": "Paramount-Skydance merger closes, David Ellison takes helm -- AP",
        "url": "https://apnews.com/article/paramount-skydance-merger-david-ellison-media",
        "source_type": "journalism",
        "author": "Associated Press",
        "year": 2025,
    },
    {
        "id": 2029,
        "title": "Trump settles CBS 60 Minutes lawsuit for $16 million -- AP",
        "url": "https://apnews.com/article/trump-cbs-60-minutes-settlement-paramount",
        "source_type": "journalism",
        "author": "Associated Press",
        "year": 2025,
    },
    {
        "id": 2030,
        "title": "Late Show with Stephen Colbert cancelled by CBS -- Variety",
        "url": "https://variety.com/2025/tv/news/stephen-colbert-late-show-cancelled-cbs-1236078421/",
        "source_type": "journalism",
        "author": "Variety",
        "year": 2025,
    },
    {
        "id": 2031,
        "title": "Bari Weiss named Editor-in-Chief of CBS News -- AP",
        "url": "https://apnews.com/article/bari-weiss-cbs-news-editor-paramount-skydance",
        "source_type": "journalism",
        "author": "Associated Press",
        "year": 2025,
    },
    {
        "id": 2032,
        "title": "TikTok US joint venture completed; Oracle, Silver Lake, MGX among partners -- WSJ",
        "url": "https://www.wsj.com/tech/tiktok-us-joint-venture-oracle-deal-2026",
        "source_type": "journalism",
        "author": "Wall Street Journal",
        "year": 2026,
    },
    {
        "id": 2033,
        "title": "FTC antitrust trial against Meta begins over Instagram, WhatsApp -- Reuters",
        "url": "https://www.reuters.com/technology/ftc-meta-antitrust-trial-begins-2025-04-14/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2034,
        "title": "Newsmax found liable in Dominion defamation trial -- AP",
        "url": "https://apnews.com/article/newsmax-dominion-defamation-trial-verdict",
        "source_type": "journalism",
        "author": "Associated Press",
        "year": 2025,
    },
    {
        "id": 2035,
        "title": "Smartmatic defamation case against Fox News moves toward trial -- Reuters",
        "url": "https://www.reuters.com/legal/smartmatic-fox-news-defamation-case-2025/",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2025,
    },
    {
        "id": 2036,
        "title": "Washington Post will not endorse in presidential race, Bezos says -- NPR",
        "url": "https://www.npr.org/2024/10/25/1203857860/washington-post-endorsement-2024-election-bezos",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2024,
    },
    {
        "id": 2037,
        "title": "Microsoft Threat Intelligence -- Russian influence operations (Storm-1516, Doppelganger)",
        "url": "https://www.microsoft.com/en-us/security/blog/2024/04/17/russian-influence-operations/",
        "source_type": "other",
        "author": "Microsoft Threat Intelligence",
        "year": 2024,
    },
    {
        "id": 2038,
        "title": "Isha Foundation -- POCSO case and sexual assault allegations (The News Minute, 2025)",
        "url": "https://www.thenewsminute.com/isha-foundation-sadhguru-child-sexual-assault-allegations",
        "source_type": "journalism",
        "author": "The News Minute",
        "year": 2025,
    },
]

# ============================================================
# ENTITIES  (8 new)
# ============================================================

ENTITIES = [
    {
        "name": "David Ellison",
        "entity_type": "person",
        "description": (
            "David Ellison (born June 21, 1983). American film producer and media "
            "executive. Son of Oracle co-founder Larry Ellison. Founded Skydance "
            "Productions in 2006 with financial backing from his father. Skydance "
            "produced major franchises including Mission: Impossible, Star Trek, "
            "and Top Gun: Maverick. In July 2024, Skydance reached a merger agreement "
            "with Paramount Global valued at approximately $28 billion. The FCC "
            "approved the transaction on July 24, 2025, and the deal closed on "
            "August 7, 2025, with Ellison becoming Chairman and CEO of the combined "
            "entity. Within weeks, the new Paramount settled Donald Trump's $16 million "
            "lawsuit against CBS over alleged deceptive editing of a 60 Minutes "
            "interview. The Late Show with Stephen Colbert was cancelled on July 18, "
            "2025. In October 2025, Ellison appointed Bari Weiss as Editor-in-Chief "
            "of CBS News and acquired Weiss's publication The Free Press for "
            "approximately $150 million."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "American",
            "born": "1983-06-21",
            "role": "Chairman & CEO, Paramount Skydance",
        },
    },
    {
        "name": "Larry Ellison",
        "entity_type": "person",
        "description": (
            "Larry Ellison (born August 17, 1944). American businessman, co-founder "
            "of Oracle Corporation (1977). One of the wealthiest people in the world "
            "with a net worth exceeding $150 billion. Close political ally of Donald "
            "Trump, hosting fundraisers at his Lanai, Hawaii estate. Father of David "
            "Ellison, whose Skydance Media he funded from inception with early equity "
            "of $350 million in 2010. Oracle holds a 15% stake in the TikTok US Joint "
            "Venture completed January 22, 2026, serving as TikTok's American technology "
            "infrastructure partner under the deal framework that resolved the forced "
            "divestiture. Other JV partners include Silver Lake (15%), MGX/Abu Dhabi "
            "sovereign fund (15%), ByteDance retained stake (19.9%), and Michael Dell's "
            "Vastmere Capital (35.1%). Ellison's overlapping roles as Oracle co-founder, "
            "Paramount parent funder, and TikTok technology partner place him at the "
            "intersection of media ownership, Big Tech, and political influence."
        ),
        "aliases": "Lawrence J. Ellison, Lawrence Joseph Ellison",
        "metadata": {
            "nationality": "American",
            "born": "1944-08-17",
            "role": "Co-founder & Chairman, Oracle Corporation",
        },
    },
    {
        "name": "FCC",
        "entity_type": "agency",
        "description": (
            "Federal Communications Commission. Independent U.S. government agency "
            "established by the Communications Act of 1934 (48 Stat. 1064). Regulates "
            "interstate and international communications by radio, television, wire, "
            "satellite, and cable. Headquartered at 45 L Street NE, Washington, D.C. "
            "The FCC's regulatory authority over broadcast licensing gives it significant "
            "power over media companies including Fox Corporation, Comcast/NBCUniversal, "
            "and Paramount/CBS. The Telecommunications Act of 1996 expanded FCC "
            "deregulatory authority, enabling the wave of media consolidation that "
            "followed. In January 2025, Brendan Carr was confirmed as FCC Chairman "
            "under the second Trump administration. The FCC approved the Paramount-"
            "Skydance merger on July 24, 2025. Under Carr, the FCC pursued broadcast "
            "license review actions and news distortion investigations against major "
            "networks."
        ),
        "aliases": "Federal Communications Commission",
        "metadata": {
            "location": "Washington, D.C.",
        },
    },
    {
        "name": "Paramount-Skydance Merger (2025)",
        "entity_type": "event",
        "description": (
            "Major media consolidation event. Skydance Media, founded and owned by "
            "David Ellison (son of Oracle co-founder Larry Ellison), acquired Paramount "
            "Global in a transaction valued at approximately $28 billion. The merger "
            "agreement was announced July 2, 2024. FCC approval came on July 24, 2025, "
            "and the deal closed on August 7, 2025, with Ellison becoming Chairman and "
            "CEO. The merger was preceded by a $16 million settlement of Donald Trump's "
            "lawsuit against CBS over alleged deceptive editing of a Kamala Harris 60 "
            "Minutes interview (October 2024). The Late Show with Stephen Colbert was "
            "cancelled on July 18, 2025, three days after Colbert criticized the "
            "settlement. In October 2025, the new Paramount appointed Bari Weiss as "
            "Editor-in-Chief of CBS News, a former Twitter Files journalist with no "
            "prior broadcast experience, and acquired her publication The Free Press "
            "for approximately $150 million."
        ),
        "aliases": "Paramount Skydance Merger, Skydance-Paramount Merger",
    },
    {
        "name": "TikTok US Joint Venture (2026)",
        "entity_type": "event",
        "description": (
            "Restructuring of TikTok's United States operations following the Supreme "
            "Court's January 17, 2025 ruling upholding the Protecting Americans from "
            "Foreign Adversary Controlled Applications Act, which mandated ByteDance "
            "divest TikTok or face a ban. President Trump signed an executive order on "
            "January 20, 2025 granting a 75-day extension. The resulting joint venture, "
            "TikTok USDS Joint Venture LLC, was completed on January 22, 2026. "
            "Ownership structure: Oracle Corporation 15% (as technology infrastructure "
            "partner), Silver Lake 15%, MGX (Abu Dhabi sovereign fund) 15%, ByteDance "
            "retained 19.9%, and Michael Dell's Vastmere Capital held 35.1%. Larry "
            "Ellison's Oracle provides the American cloud infrastructure housing US "
            "user data. The deal resolved the national security concerns while keeping "
            "TikTok operational for approximately 170 million American users."
        ),
        "aliases": "TikTok USDS Joint Venture LLC, TikTok US Deal",
    },
    {
        "name": "Bari Weiss",
        "entity_type": "person",
        "description": (
            "Bari Weiss (born March 25, 1990). American journalist and author. Opinion "
            "editor at The Wall Street Journal (2013-2017), then opinion writer and "
            "editor at The New York Times (2017-2020), where she resigned publicly "
            "alleging illiberal internal culture. Founded The Free Press in 2021, a "
            "contrarian media outlet. Was one of the journalists selected by Elon Musk "
            "to publish the Twitter Files beginning December 2022, reporting on internal "
            "content moderation decisions at Twitter. Appointed Editor-in-Chief of CBS "
            "News on October 6, 2025 by David Ellison's Paramount Skydance, with no "
            "prior broadcast journalism experience. Approximately 100 CBS News employees "
            "were laid off following her appointment, including eight female on-air "
            "hosts. Paramount Skydance simultaneously acquired The Free Press for "
            "approximately $150 million."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "American",
            "born": "1990-03-25",
            "role": "Editor-in-Chief, CBS News (Oct 2025-)",
        },
    },
    {
        "name": "Brendan Carr",
        "entity_type": "person",
        "description": (
            "Brendan Carr (born c. 1980). American attorney and telecommunications "
            "official. Served as FCC General Counsel before being appointed as FCC "
            "Commissioner by President Trump in 2017. Renominated and confirmed for "
            "a full term in 2020. Confirmed as FCC Chairman in January 2025 under the "
            "second Trump administration. Known for advocacy against Big Tech content "
            "moderation and for broadcast license accountability. As Chairman, Carr "
            "pursued news distortion investigations against broadcast networks and "
            "sent letters to major broadcasters including NBC/Comcast threatening "
            "license review. The FCC under Carr approved the Paramount-Skydance "
            "merger on July 24, 2025."
        ),
        "aliases": "",
        "metadata": {
            "nationality": "American",
            "role": "FCC Chairman (2025-)",
            "prior_role": "FCC Commissioner (2017-2025)",
        },
    },
    {
        "name": "Meta Fact-Check Removal (2025)",
        "entity_type": "event",
        "description": (
            "On January 7, 2025, Meta CEO Mark Zuckerberg announced the end of Meta's "
            "third-party fact-checking program across Facebook, Instagram, and Threads, "
            "replacing it with a Community Notes system modeled on X (formerly Twitter). "
            "The fact-checking program had been in place since 2016, established in "
            "response to criticism over disinformation during the US presidential "
            "election. Zuckerberg framed the change as reducing censorship and 'going "
            "back to our roots around free expression.' The announcement coincided with "
            "broader content moderation rollbacks at Meta and followed Elon Musk's "
            "implementation of Community Notes on X. The shift was interpreted by "
            "critics as capitulation to political pressure following the 2024 election, "
            "while supporters characterized it as a correction of overreach."
        ),
        "aliases": "Meta Community Notes Transition",
    },
]

# ============================================================
# RELATIONSHIPS  (38 total)
# ============================================================

RELATIONSHIPS = [
    # --- David Ellison ---
    {
        "source": "David Ellison",
        "target": "Paramount Global",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Chairman and CEO of Paramount Skydance (formerly Paramount Global) "
            "from August 7, 2025, following the completion of the Skydance-Paramount "
            "merger valued at approximately $28 billion."
        ),
        "year_start": 2025,
        "sources": [2002, 2028],
    },
    {
        "source": "David Ellison",
        "target": "Paramount-Skydance Merger (2025)",
        "type": "led",
        "tier": "documented",
        "desc": (
            "Led the acquisition of Paramount Global through his company Skydance "
            "Media. Merger agreement announced July 2, 2024. FCC approved July 24, "
            "2025. Deal closed August 7, 2025."
        ),
        "year_start": 2024,
        "year_end": 2025,
        "sources": [2001, 2002, 2028],
    },
    {
        "source": "David Ellison",
        "target": "Larry Ellison",
        "type": "family_of",
        "tier": "documented",
        "desc": (
            "Son of Larry Ellison, Oracle co-founder. Larry provided initial and "
            "ongoing financial backing for David's Skydance Media, including $350 "
            "million in early equity funding (2010)."
        ),
        "sources": [2002, 2003],
    },
    {
        "source": "David Ellison",
        "target": "Bari Weiss",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "As CEO of Paramount Skydance, appointed Bari Weiss as Editor-in-Chief "
            "of CBS News on October 6, 2025. Weiss had no prior broadcast journalism "
            "experience. Paramount simultaneously acquired Weiss's publication The "
            "Free Press for approximately $150 million."
        ),
        "year_start": 2025,
        "sources": [2031],
    },
    # --- Larry Ellison ---
    {
        "source": "Larry Ellison",
        "target": "TikTok US Joint Venture (2026)",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "Oracle Corporation, co-founded by Larry Ellison, holds a 15% stake in "
            "the TikTok USDS Joint Venture LLC completed January 22, 2026. Oracle "
            "serves as TikTok's American technology infrastructure partner, housing "
            "US user data on its cloud platform. Ellison described as a close Trump "
            "ally who facilitated the deal framework."
        ),
        "year_start": 2026,
        "sources": [2003, 2032],
    },
    {
        "source": "Larry Ellison",
        "target": "Donald Trump",
        "type": "ally_of",
        "tier": "credible",
        "desc": (
            "Close political ally. Ellison hosted Trump fundraisers at his Lanai, "
            "Hawaii estate. Ellison's Oracle was selected as TikTok's US technology "
            "partner under the Trump administration's forced divestiture framework. "
            "His son David Ellison's Paramount settled Trump's CBS lawsuit."
        ),
        "sources": [2003, 2032],
    },
    {
        "source": "Larry Ellison",
        "target": "Paramount-Skydance Merger (2025)",
        "type": "funded",
        "tier": "credible",
        "desc": (
            "Provided initial and ongoing financial backing for son David Ellison's "
            "Skydance Media, including $350 million in early equity funding (2010), "
            "which grew into the company that ultimately acquired Paramount Global "
            "in a $28 billion transaction."
        ),
        "sources": [2001, 2003],
    },
    # --- Brendan Carr ---
    {
        "source": "Brendan Carr",
        "target": "FCC",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "Confirmed as Chairman of the Federal Communications Commission in "
            "January 2025 under the second Trump administration. Previously served "
            "as FCC Commissioner from 2017."
        ),
        "year_start": 2025,
        "sources": [2005, 2020],
    },
    {
        "source": "Brendan Carr",
        "target": "Comcast Corporation",
        "type": "targeted",
        "tier": "credible",
        "desc": (
            "As FCC Chairman, Carr sent letters to NBC/Comcast threatening broadcast "
            "license review and launched news distortion investigations against "
            "broadcast networks in 2025. Comcast's NBC broadcast licenses were "
            "subject to heightened regulatory scrutiny."
        ),
        "year_start": 2025,
        "sources": [2005, 2020],
    },
    {
        "source": "Donald Trump",
        "target": "Brendan Carr",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Nominated Brendan Carr as FCC Chairman in late 2024, confirmed by "
            "Senate in January 2025. Carr had previously been appointed as FCC "
            "Commissioner by Trump in 2017."
        ),
        "year_start": 2025,
        "sources": [2005, 2020],
    },
    # --- FCC ---
    {
        "source": "FCC",
        "target": "Paramount-Skydance Merger (2025)",
        "type": "authorized",
        "tier": "documented",
        "desc": (
            "FCC approved the Paramount-Skydance merger on July 24, 2025, clearing "
            "the final major regulatory hurdle for the $28 billion transaction. "
            "The deal closed August 7, 2025."
        ),
        "year_start": 2025,
        "sources": [2000, 2004, 2028],
    },
    {
        "source": "Telecommunications Act of 1996",
        "target": "FCC",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The 1996 Telecommunications Act dramatically expanded FCC deregulatory "
            "authority and relaxed media ownership limits, enabling the wave of "
            "consolidation that produced the modern media conglomerate landscape "
            "including the eventual Paramount-Skydance merger."
        ),
        "sources": [2004, 2016],
    },
    {
        "source": "Fox Corporation",
        "target": "FCC",
        "type": "regulated_by",
        "tier": "documented",
        "desc": (
            "Fox Corporation's broadcast television stations are licensed and "
            "regulated by the FCC. Fox News itself operates as cable (not FCC-"
            "licensed), but Fox's broadcast licenses create regulatory leverage."
        ),
        "sources": [2004, 2020],
    },
    {
        "source": "Comcast Corporation",
        "target": "FCC",
        "type": "regulated_by",
        "tier": "documented",
        "desc": (
            "Comcast's NBCUniversal broadcast stations are licensed by the FCC. "
            "Under FCC Chairman Brendan Carr (2025-), NBC's broadcast licenses "
            "became subject to news distortion investigations and license review "
            "threats."
        ),
        "sources": [2004, 2020],
    },
    {
        "source": "Paramount Global",
        "target": "FCC",
        "type": "regulated_by",
        "tier": "documented",
        "desc": (
            "Paramount's CBS broadcast television stations are licensed by the FCC. "
            "The FCC's approval was required for the Paramount-Skydance merger, "
            "which it granted on July 24, 2025."
        ),
        "sources": [2000, 2004, 2028],
    },
    # --- Bari Weiss ---
    {
        "source": "Bari Weiss",
        "target": "Paramount Global",
        "type": "employed_by",
        "tier": "documented",
        "desc": (
            "Appointed Editor-in-Chief of CBS News (owned by Paramount Skydance) on "
            "October 6, 2025. First person to hold EIC title with no prior broadcast "
            "journalism experience. Approximately 100 CBS News employees laid off "
            "following her appointment."
        ),
        "year_start": 2025,
        "sources": [2006, 2031],
    },
    {
        "source": "Bari Weiss",
        "target": "Twitter Files",
        "type": "participated_in",
        "tier": "documented",
        "desc": (
            "One of the journalists selected by Elon Musk to publish the Twitter "
            "Files beginning December 2022. Reported on internal content moderation "
            "decisions at Twitter, particularly related to the suppression of the "
            "Hunter Biden laptop story and other topics."
        ),
        "year_start": 2022,
        "sources": [2006],
    },
    # --- Paramount-Skydance Merger ---
    {
        "source": "Donald Trump",
        "target": "Paramount-Skydance Merger (2025)",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Trump sued CBS for $10 billion over alleged deceptive editing of a "
            "Kamala Harris 60 Minutes interview (October 2024). The suit was settled "
            "for $16 million in July 2025, weeks before the Paramount-Skydance merger "
            "closed on August 7, 2025. Stephen Colbert, who publicly criticized the "
            "settlement, had his Late Show cancelled on July 18, 2025."
        ),
        "year_start": 2025,
        "sources": [2029, 2030],
    },
    # --- TikTok JV ---
    {
        "source": "Donald Trump",
        "target": "TikTok US Joint Venture (2026)",
        "type": "authorized",
        "tier": "documented",
        "desc": (
            "Signed executive order on January 20, 2025 granting TikTok a 75-day "
            "extension from the Supreme Court-upheld ban. Authorized the resulting "
            "joint venture framework in which the U.S. government facilitated "
            "American co-ownership of TikTok's US operations."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [2007, 2032],
    },
    {
        "source": "Mark Zuckerberg",
        "target": "TikTok US Joint Venture (2026)",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Zuckerberg publicly called for TikTok restrictions citing national "
            "security concerns and testified before Congress in 2024 about Chinese "
            "tech threats to American users. Meta's platforms (Instagram Reels, "
            "Facebook) directly competed with TikTok for the same user base that "
            "the JV preserved."
        ),
        "sources": [2007, 2008],
    },
    # --- Meta Fact-Check Removal ---
    {
        "source": "Mark Zuckerberg",
        "target": "Meta Fact-Check Removal (2025)",
        "type": "directed",
        "tier": "documented",
        "desc": (
            "Announced on January 7, 2025 that Meta would end its third-party "
            "fact-checking program across Facebook, Instagram, and Threads, "
            "replacing it with a Community Notes system modeled on X. Zuckerberg "
            "posted the announcement as a video on Meta platforms."
        ),
        "year_start": 2025,
        "sources": [2021],
    },
    {
        "source": "Meta",
        "target": "Meta Fact-Check Removal (2025)",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "Meta ended its third-party fact-checking partnerships across all "
            "platforms (Facebook, Instagram, Threads) beginning January 2025, "
            "transitioning to a Community Notes system modeled on X. The program "
            "had been in place since 2016."
        ),
        "year_start": 2025,
        "sources": [2008, 2021],
    },
    {
        "source": "Elon Musk",
        "target": "Meta Fact-Check Removal (2025)",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Meta's replacement system -- Community Notes -- was explicitly modeled "
            "on the system Musk implemented on X (formerly Twitter) after his "
            "acquisition. Musk championed user-driven content moderation as "
            "superior to third-party fact-checking."
        ),
        "sources": [2008, 2021],
    },
    # --- Wiring in unassigned entities: Meta ---
    {
        "source": "Meta",
        "target": "Cambridge Analytica",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Facebook (now Meta) was the platform Cambridge Analytica exploited to "
            "harvest approximately 87 million user profiles for political targeting "
            "in the 2016 US election. The scandal led to congressional hearings, FTC "
            "investigation ($5 billion fine in 2019), and Meta's subsequent "
            "establishment of third-party fact-checking partnerships."
        ),
        "year_start": 2015,
        "year_end": 2018,
        "sources": [2015, 2024],
    },
    # --- Wiring in: OpenAI ---
    {
        "source": "Elon Musk",
        "target": "OpenAI",
        "type": "co_founded",
        "tier": "documented",
        "desc": (
            "Co-founder of OpenAI in 2015, alongside Sam Altman and others, as a "
            "nonprofit AI research lab. Musk departed the board in 2018 citing "
            "conflicts with Tesla's AI work. In 2024, Musk sued OpenAI alleging it "
            "had abandoned its original nonprofit mission. OpenAI subsequently "
            "restructured as a public benefit corporation in 2025."
        ),
        "year_start": 2015,
        "year_end": 2018,
        "sources": [2009],
    },
    {
        "source": "OpenAI",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "credible",
        "desc": (
            "OpenAI dropped its ban on military applications in January 2024. "
            "Partnered with defense contractor Anduril in December 2024 for "
            "counter-drone AI systems. Secured additional Department of Defense "
            "contracts for cybersecurity and operational applications through 2025."
        ),
        "year_start": 2024,
        "sources": [2009, 2027],
    },
    # --- Wiring in: Anthropic ---
    {
        "source": "Anthropic",
        "target": "Palantir Technologies",
        "type": "contracted_with",
        "tier": "documented",
        "desc": (
            "Partnership announced November 2024 to deploy Claude AI models on "
            "Palantir's defense and intelligence platform. Accessible to US "
            "intelligence and defense agencies via AWS GovCloud with Impact Level "
            "6 (IL6) security accreditation."
        ),
        "year_start": 2024,
        "sources": [2010, 2026],
    },
    {
        "source": "Anthropic",
        "target": "The Pentagon",
        "type": "contracted_with",
        "tier": "credible",
        "desc": (
            "Claude AI deployed for defense and intelligence applications via "
            "Palantir's platform beginning 2024. Anthropic described as having "
            "'national security' significance in government discussions around "
            "frontier AI. Represents the integration of commercial AI into the "
            "national security apparatus."
        ),
        "year_start": 2024,
        "sources": [2010, 2026],
    },
    # --- Wiring in: Walter Lippmann (0 existing edges) ---
    {
        "source": "Walter Lippmann",
        "target": "Edward Bernays",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Contemporaries and foundational figures in propaganda and public opinion "
            "theory. Lippmann's 'Public Opinion' (1922) theorized the 'manufacture "
            "of consent' -- the idea that public opinion must be shaped by experts. "
            "Bernays, Freud's nephew, operationalized this theory in 'Propaganda' "
            "(1928), creating the modern public relations industry. Both served on "
            "the Committee on Public Information during WWI."
        ),
        "sources": [2012, 2018, 2019],
    },
    {
        "source": "Walter Lippmann",
        "target": "Council on Foreign Relations",
        "type": "member_of",
        "tier": "documented",
        "desc": (
            "Founding member of the Council on Foreign Relations, established in "
            "1921. Lippmann's vision of an informed elite managing public opinion "
            "aligned with the CFR's model of elite foreign policy consensus. He "
            "remained a prominent member and contributed to CFR discourse for decades."
        ),
        "sources": [2012, 2014],
    },
    {
        "source": "Walter Lippmann",
        "target": "Operation Mockingbird",
        "type": "preceded",
        "tier": "inference",
        "desc": (
            "Inference: Lippmann's theoretical framework for elite media management -- "
            "particularly his concept of 'the manufacture of consent' (1922) -- "
            "prefigured the CIA's systematic media infiltration program Operation "
            "Mockingbird (1950s-1970s). While no direct operational link exists, "
            "Mockingbird implemented at scale precisely the kind of expert-managed "
            "opinion formation Lippmann had theorized."
        ),
        "sources": [2012, 2022],
    },
    # --- Wiring in: Mark Lombardi (0 existing edges) ---
    {
        "source": "Mark Lombardi",
        "target": "BCCI",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "Lombardi created detailed hand-drawn network diagrams documenting BCCI's "
            "connections to intelligence agencies, arms dealers, and political figures. "
            "His BCCI works were exhibited at Pierogi Gallery and later at the Whitney "
            "Museum. The diagrams mapped financial flows that matched subsequent "
            "congressional investigation findings."
        ),
        "sources": [2011, 2025],
    },
    {
        "source": "Mark Lombardi",
        "target": "Iran-Contra",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "Lombardi's network diagrams documented the financial networks underlying "
            "Iran-Contra, tracing connections between arms dealers, Swiss banks, CIA "
            "cutouts, and political figures. His artwork visualized the same networks "
            "that congressional investigations had established through testimony and "
            "documents."
        ),
        "sources": [2011, 2025],
    },
    {
        "source": "Mark Lombardi",
        "target": "Banco Ambrosiano Collapse",
        "type": "documented",
        "tier": "documented",
        "desc": (
            "Lombardi mapped the Vatican Bank-Banco Ambrosiano financial scandal in "
            "his network diagrams, documenting connections between Roberto Calvi, the "
            "Vatican Bank, P2 Lodge, and international financial flows. Lombardi died "
            "on March 22, 2000, ruled suicide by hanging, at age 48."
        ),
        "sources": [2011, 2025],
    },
    # --- Wiring in: Kenneth Copeland (0 existing edges) ---
    {
        "source": "Kenneth Copeland",
        "target": "Donald Trump",
        "type": "affiliated_with",
        "tier": "documented",
        "desc": (
            "Served as a spiritual advisor to President Trump. Participated in "
            "laying-on-of-hands prayer sessions at the White House. Copeland led "
            "a group of evangelical leaders who prayed with Trump in the Oval Office. "
            "Publicly endorsed Trump and used his broadcast ministry to encourage "
            "support."
        ),
        "sources": [2013],
    },
    {
        "source": "Kenneth Copeland",
        "target": "Joel Osteen",
        "type": "affiliated_with",
        "tier": "credible",
        "desc": (
            "Both are leading figures of the American prosperity gospel movement, "
            "which equates wealth with divine blessing and positions financial "
            "extraction from followers as religious practice. Appear at the same "
            "conferences and megachurch events. Combined personal wealth exceeds "
            "$400 million."
        ),
        "sources": [2013, 2014],
    },
    {
        "source": "Kenneth Copeland",
        "target": "Fox Corporation",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Copeland and the prosperity gospel ecosystem maintain a symbiotic "
            "relationship with conservative media. Copeland and fellow televangelists "
            "appeared regularly on Fox News programming, reinforcing the alliance "
            "between evangelical Christianity and conservative media narratives."
        ),
        "sources": [2013],
    },
    # --- Wiring in: Sean Parker ---
    {
        "source": "Sean Parker",
        "target": "Meta",
        "type": "employed_by",
        "tier": "documented",
        "desc": (
            "First president of Facebook (now Meta) in 2004. Parker publicly admitted "
            "the platform was designed to exploit human psychological vulnerability: "
            "'God only knows what it's doing to our children's brains' (November 2017 "
            "Axios interview). His admission validated critics who argued social media "
            "platforms constitute a narrative control infrastructure."
        ),
        "year_start": 2004,
        "year_end": 2005,
        "sources": [2023],
    },
]

# ============================================================
# ENTITY -> SOURCE mappings (every new entity)
# ============================================================

ENTITY_SOURCES = {
    "David Ellison": [2002, 2028],
    "Larry Ellison": [2003, 2032],
    "FCC": [2004, 2020],
    "Paramount-Skydance Merger (2025)": [2000, 2001, 2028, 2029, 2030],
    "TikTok US Joint Venture (2026)": [2007, 2032],
    "Bari Weiss": [2006, 2031],
    "Brendan Carr": [2005, 2020],
    "Meta Fact-Check Removal (2025)": [2008, 2021],
}

# ============================================================
# ENTITY_UPDATES  (10 updates to existing entities)
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "Paramount Global",
        "description_append": (
            "2025-2026 update: Skydance Media, owned by David Ellison (son of Oracle "
            "co-founder Larry Ellison), completed its acquisition of Paramount Global "
            "on August 7, 2025, in a deal valued at approximately $28 billion, following "
            "FCC approval on July 24, 2025. David Ellison became Chairman and CEO. Prior "
            "to the merger close, Paramount settled Donald Trump's lawsuit against CBS "
            "over alleged deceptive editing of a 60 Minutes Kamala Harris interview for "
            "$16 million in July 2025. The Late Show with Stephen Colbert was cancelled "
            "on July 18, 2025. In October 2025, Bari Weiss was appointed Editor-in-Chief "
            "of CBS News, and Paramount acquired Weiss's The Free Press for approximately "
            "$150 million. Approximately 100 CBS News employees were laid off."
        ),
        "sources": [2000, 2028, 2029, 2030, 2031],
    },
    {
        "name": "Meta",
        "description_append": (
            "2025-2026 update: On January 7, 2025, CEO Mark Zuckerberg announced the "
            "end of Meta's third-party fact-checking program across Facebook, Instagram, "
            "and Threads, replacing it with a Community Notes system modeled on X "
            "(formerly Twitter). The program had been in place since 2016. In April 2025, "
            "the FTC's antitrust case against Meta went to trial, alleging monopoly "
            "through the Instagram and WhatsApp acquisitions. The court ruled in Meta's "
            "favor, finding the FTC failed to prove the relevant market."
        ),
        "sources": [2008, 2021, 2033],
    },
    {
        "name": "OpenAI",
        "description_append": (
            "2025-2026 update: OpenAI completed its restructuring from a nonprofit-"
            "controlled capped-profit entity to a public benefit corporation (PBC) "
            "in mid-2025, with the original nonprofit retaining a significant equity "
            "stake. The conversion drew scrutiny from Delaware and California attorneys "
            "general. OpenAI reversed its prior ban on military applications, partnering "
            "with defense contractor Anduril in December 2024 for counter-drone AI "
            "systems and securing additional Department of Defense contracts for "
            "cybersecurity and operational applications through 2025."
        ),
        "sources": [2009, 2027],
    },
    {
        "name": "Anthropic",
        "description_append": (
            "2025-2026 update: In November 2024, Anthropic announced a partnership with "
            "Palantir Technologies to deploy Claude AI models on Palantir's defense and "
            "intelligence platform, accessible to US intelligence and defense agencies "
            "via AWS GovCloud with Impact Level 6 (IL6) security accreditation. The "
            "partnership integrated Anthropic's AI into the national security apparatus, "
            "with Claude used for intelligence analysis and operational planning. "
            "Anthropic was described as having 'national security' significance in "
            "government discussions around frontier AI capabilities."
        ),
        "sources": [2010, 2026],
    },
    {
        "name": "Dominion Voting Systems",
        "description_append": (
            "2025-2026 update: Following the $787.5 million Fox News settlement in "
            "April 2023, Dominion pursued its defamation lawsuit against Newsmax. "
            "The Newsmax trial commenced in spring 2025 in Wilmington, Delaware. The "
            "jury found Newsmax liable for defamation related to its post-2020 election "
            "coverage promoting false claims about Dominion's voting machines."
        ),
        "sources": [2034],
    },
    {
        "name": "Jeff Bezos",
        "description_append": (
            "2024-2025 update: In late October 2024, Bezos intervened to prevent The "
            "Washington Post from endorsing a presidential candidate for the 2024 "
            "election, breaking decades of editorial tradition. The decision triggered "
            "approximately 200,000 subscription cancellations and widespread criticism "
            "from Post staff and readers. The move was widely interpreted as Bezos "
            "seeking to avoid antagonizing the incoming Trump administration, given "
            "Amazon's substantial federal government contracts."
        ),
        "sources": [2036],
    },
    {
        "name": "Fox Corporation",
        "description_append": (
            "2025-2026 update: Fox Corporation continued to face the Smartmatic "
            "defamation lawsuit (originally filed for $2.7 billion) following its "
            "$787.5 million settlement with Dominion Voting Systems in April 2023. "
            "The Smartmatic case, alleging Fox News knowingly broadcast false claims "
            "about Smartmatic's voting technology following the 2020 election, "
            "proceeded toward trial through 2025-2026."
        ),
        "sources": [2035],
    },
    {
        "name": "Internet Research Agency",
        "description_append": (
            "2024-2025 update: While the original Internet Research Agency was formally "
            "dissolved, Russian state-linked influence operations continued through "
            "successor entities and campaigns. Microsoft Threat Intelligence documented "
            "ongoing operations including Storm-1516 and Doppelganger campaigns targeting "
            "Western democracies through 2024-2025, using AI-generated content and fake "
            "news sites to amplify divisive narratives. These operations represent a "
            "continuation of the IRA's documented methodology with evolved technical "
            "capabilities including generative AI."
        ),
        "sources": [2017, 2037],
    },
    {
        "name": "Comcast Corporation",
        "description_append": (
            "2025-2026 update: Comcast's NBC broadcast operations came under pressure "
            "from FCC Chairman Brendan Carr, who sent letters to NBC regarding broadcast "
            "license review and pursued news distortion investigations. The company's "
            "broadcast licenses were subject to heightened regulatory scrutiny under the "
            "second Trump administration."
        ),
        "sources": [2005, 2020],
    },
    {
        "name": "Twitter Files",
        "description_append": (
            "2025-2026 update: The Twitter Files' downstream effects on media ownership "
            "materialized when Bari Weiss, one of the journalists selected by Elon Musk "
            "to publish the Files in December 2022, was appointed Editor-in-Chief of "
            "CBS News in October 2025 by David Ellison's Paramount Skydance. The "
            "appointment created a direct pipeline from the Twitter Files revelations "
            "to broadcast news editorial leadership."
        ),
        "sources": [2006, 2031],
    },
    {
        "name": "Sadhguru",
        "description_append": (
            "2024-2026 update: In October 2024, the Supreme Court of India closed "
            "habeas corpus petitions after two women confirmed voluntary residence "
            "at Isha Foundation. In late 2024 through early 2025, sexual assault "
            "allegations surfaced; The News Minute reported child sexual assault "
            "at Isha Home School (2007-2010 period). In April 2025, a POCSO "
            "(Protection of Children from Sexual Offences Act) case was registered "
            "against four Isha Foundation staff members and a former student. In "
            "March 2026, the Delhi High Court granted Isha Foundation an interim "
            "injunction against Google and publisher Nakkheeran for defamatory "
            "content, later expanded in August 2026 to remove 44 additional videos."
        ),
        "sources": [2038],
    },
]

# ============================================================
# GEO_COORDS  (for new entities)
# ============================================================

GEO_COORDS = {
    "David Ellison": (34.0195, -118.4912, "credible",
                      "Skydance Media HQ, Santa Monica, California"),
    "Larry Ellison": (37.5282, -122.2495, "credible",
                      "Oracle HQ, Redwood City, California"),
    "FCC": (38.9010, -77.0031, "documented",
            "FCC HQ, 45 L Street NE, Washington, D.C."),
    "Paramount-Skydance Merger (2025)": (34.0928, -118.3287, "credible",
                                         "Paramount Pictures lot, Hollywood, California"),
    "TikTok US Joint Venture (2026)": (34.0211, -118.3965, "credible",
                                       "TikTok US HQ, Culver City, California"),
    "Bari Weiss": (40.7614, -73.9776, "credible",
                   "CBS Broadcast Center, New York, New York"),
    "Brendan Carr": (38.9010, -77.0031, "credible",
                     "FCC HQ, Washington, D.C."),
    "Meta Fact-Check Removal (2025)": (37.4530, -122.1817, "credible",
                                       "Meta HQ, Menlo Park, California"),
}

# ============================================================
# PHOTO_CANDIDATES  (for new persons/orgs)
# ============================================================

PHOTO_CANDIDATES = {
    "David Ellison": "https://upload.wikimedia.org/wikipedia/commons/f/f2/David_Ellison_by_Gage_Skidmore.jpg",
    "Larry Ellison": "https://upload.wikimedia.org/wikipedia/commons/0/00/Larry_Ellison_on_stage.jpg",
    "FCC": "https://upload.wikimedia.org/wikipedia/commons/8/8c/FCC_New_Logo.svg",
    "Bari Weiss": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Bari_Weiss_by_Gage_Skidmore.jpg",
    "Brendan Carr": "https://www.fcc.gov/sites/default/files/brendan-carr.jpg",
}
