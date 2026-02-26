"""
Financial Elite & Mega Group Cluster — Expansion layer for Intel Console.
Entities: Billionaire donors, hedge fund managers, and financial institutions
connected to the Epstein network.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# FINANCIAL ELITE & MEGA GROUP CLUSTER
# Source IDs: 76-95
# ============================================================

SOURCES = [
    # Journalism
    {"id": 76, "title": "MintPress News — Mega Group, Maxwells and Mossad: The Spy Story at the Heart of the Jeffrey Epstein Scandal", "url": "https://www.mintpressnews.com/mega-group-maxwells-mossad-spy-story-jeffrey-epstein-scandal/261172/", "source_type": "journalism", "author": "Whitney Webb", "year": 2019},
    {"id": 77, "title": "ProPublica/New York Times — Women Say Billionaire Philanthropist Steinhardt Asked for Sex", "url": "https://www.propublica.org/article/women-who-worked-with-billionaire-philanthropist-michael-steinhardt-say-he-repeatedly-asked-for-and-about-sex", "source_type": "journalism", "year": 2019},
    {"id": 78, "title": "Harvard Crimson — Dubin Implicated in Epstein's Alleged Sex Ring", "url": "https://www.thecrimson.com/article/2019/8/18/dubin-epstein-unsealed-docs/", "source_type": "journalism", "year": 2019},
    {"id": 79, "title": "Fortune — Former Barclays Chief Jes Staley's Profound Friendship with Epstein Revealed in Emails", "url": "https://fortune.com/2023/02/16/jes-staley-jeffrey-epstein-emails-profound-friendship-barclays/", "source_type": "journalism", "year": 2023},
    {"id": 80, "title": "NPR — Jeffrey Epstein Mentor Steven Hoffenberg Found Dead in Connecticut", "url": "https://www.npr.org/2022/08/26/1119746511/jeffrey-epstein-mentor-steven-hoffenberg-dead", "source_type": "journalism", "year": 2022},
    {"id": 81, "title": "Al Jazeera — Epstein Pressed Billionaire Media Mogul to Influence Coverage", "url": "https://www.aljazeera.com/news/2026/2/9/epstein-pressed-billionaire-media-mogul-to-influence-coverage-files-reveal", "source_type": "journalism", "year": 2026},
    {"id": 82, "title": "CBS News — Trump Insider Tom Barrack Kept in Contact with Epstein for Years", "url": "https://www.cbsnews.com/news/tom-barrack-jeffrey-epstein-files/", "source_type": "journalism", "year": 2026},
    {"id": 83, "title": "Poynter — Radar Magazine to Get Up to $25 Million from Zuckerman, Epstein", "url": "https://www.poynter.org/reporting-editing/2004/radar-mag-to-get-up-to-25-million-from-zuckerman-epstein/", "source_type": "journalism", "year": 2004},
    {"id": 84, "title": "Washington Post — Steven Hoffenberg, Ponzi Swindler and Jeffrey Epstein Mentor, Dies", "url": "https://www.washingtonpost.com/obituaries/2022/08/26/hoffenberg-ponzi-epstein-dies/", "source_type": "journalism", "year": 2022},
    # Court / Government
    {"id": 85, "title": "Towers Financial Corporation — SEC/DOJ Fraud Proceedings", "url": "", "source_type": "court", "year": 1995},
    {"id": 86, "title": "UK FCA — Jes Staley Ban for Misleading Regulators About Epstein Relationship", "url": "https://www.fca.org.uk/news/press-releases/upper-tribunal-upholds-jes-staley-ban", "source_type": "government", "year": 2023},
    {"id": 87, "title": "USVI v. JPMorgan Chase — MC2 Model Management Exhibits", "url": "https://www.justice.gov/multimedia/Court%20Records/Government%20of%20the%20United%20States%20Virgin%20Islands%20v.%20JPMorgan%20Chase%20Bank,%20N.A.,%20No.%20122-cv-10904%20(S.D.N.Y.%202022)/240-01.pdf", "source_type": "court", "year": 2022},
    {"id": 88, "title": "Tom Barrack Indictment — US v. Barrack et al. (EDNY)", "url": "", "source_type": "court", "year": 2021},
    {"id": 89, "title": "Clinton Presidential Library — Lynn Forester Letter to President Clinton (1995)", "url": "", "source_type": "government", "year": 1995},
    {"id": 90, "title": "Manhattan DA — Michael Steinhardt Surrenders 180 Looted Antiquities ($70M)", "url": "", "source_type": "court", "year": 2021},
    # Books
    {"id": 91, "title": "Nicholas Faith — The Bronfmans: The Rise and Fall of the House of Seagram", "url": "", "source_type": "book", "author": "Nicholas Faith", "year": 2006},
    {"id": 92, "title": "Bloomberg — Jes Staley and Jeffrey Epstein: Evidence That Doomed Ex-Barclays CEO's Career", "url": "https://www.bloomberg.com/features/2025-jes-staley-jeffrey-epstein-fca/", "source_type": "journalism", "year": 2025},
    {"id": 93, "title": "CNBC — Tom Barrack Charged with Illegally Lobbying Trump on Behalf of UAE", "url": "https://www.cnbc.com/2021/07/20/thomas-barrack-chairman-of-trump-2017-inaugural-fund-arrested-on-federal-charge.html", "source_type": "journalism", "year": 2021},
    {"id": 94, "title": "DOJ Epstein Files Release — Phase 1 (Feb 2026)", "url": "https://www.justice.gov/epstein/doj-disclosures", "source_type": "government", "year": 2026},
    {"id": 95, "title": "Daily Beast — Did Jeffrey Epstein Help Steven Hoffenberg Swindle $460 Million?", "url": "https://www.thedailybeast.com/did-jeffrey-epstein-help-steven-hoffenberg-swindle-dollar460-million-in-ponzi-scheme/", "source_type": "journalism", "year": 2019},
]


# ============================================================
# ENTITY DESCRIPTIONS — long-form dossiers
# ============================================================

_DESC_CHARLES_BRONFMAN = (
    "Charles Rosner Bronfman (b. 1931). Canadian-American billionaire businessman, "
    "philanthropist, and co-founder of the Mega Group with Les Wexner."
    "\n\n"
    "SEAGRAM EMPIRE: Son of Samuel Bronfman, who built the Seagram spirits empire during "
    "and after American Prohibition. Samuel Bronfman's Distillers Corporation acquired "
    "Joseph E. Seagram & Sons in 1928 and grew it into one of the world's largest "
    "beverage companies. The Bronfman family fortune traces to the Prohibition era, when "
    "the family legally exported spirits from Canada to American bootleggers — a business "
    "that intersected with organized crime networks controlled by figures like Meyer "
    "Lansky and Lucky Luciano. Charles and his brother Edgar Sr. inherited the Seagram "
    "empire upon their father's death in 1971, with Charles holding various positions "
    "from 1951 to 2000."
    "\n\n"
    "MEGA GROUP: In 1991, Charles Bronfman co-founded the Mega Group with Les Wexner — "
    "a secretive annual gathering of approximately 20 of the wealthiest pro-Israel donors "
    "in North America. The group's activities and full membership remain deliberately "
    "opaque. Jeffrey Epstein attended Mega Group meetings despite not qualifying for "
    "membership by wealth. The Mega Group has been described as the philanthropic and "
    "political coordination mechanism for an interconnected network of billionaire donors "
    "with deep ties to Israel."
    "\n\n"
    "BIRTHRIGHT ISRAEL: Co-founded the Birthright Israel program in 1994 with fellow "
    "Mega Group member Michael Steinhardt. The program provides free 10-day trips to "
    "Israel for Jewish young adults aged 18-26. By 2024, over 800,000 participants had "
    "taken the trip. Bronfman and Steinhardt each contributed $8 million initially, "
    "alongside 15 other partners pledging $5 million apiece."
    "\n\n"
    "ROBERT MAXWELL CONNECTION: Robert Maxwell — Ghislaine Maxwell's father and "
    "documented Mossad asset — was a business partner of Charles Bronfman, linking the "
    "Bronfman network to the Maxwell intelligence pipeline that later connected to "
    "Epstein."
    "\n\n"
    "PHILANTHROPY: Chairman of the Andrea and Charles Bronfman Philanthropies Inc., "
    "operating in Israel, the US, and Canada. Major donor to the Tel Aviv Performing "
    "Arts Center, Israel Museum, and Jewish educational initiatives. Also formerly "
    "owned the Montreal Expos baseball team (1968-1991)."
)

_DESC_EDGAR_BRONFMAN_SR = (
    "Edgar Miles Bronfman Sr. (1929-2013). CEO of Seagram, president of the World "
    "Jewish Congress, and patriarch of a family whose influence spans liquor, media, "
    "intelligence-adjacent philanthropy, and a connection to the NXIVM sex cult."
    "\n\n"
    "SEAGRAM LEADERSHIP: Succeeded his father Samuel Bronfman as president, treasurer, "
    "and director of Seagram in 1971. Under his leadership, Seagram became one of the "
    "world's largest beverage companies. Son Edgar Jr. took over as CEO in 1994 and "
    "controversially sold the family's $8.8 billion DuPont stake to purchase MCA/Universal "
    "Studios, then merged Seagram with Vivendi in 2000 for $42 billion — a deal that "
    "ultimately destroyed the Seagram empire and cost the Bronfman family billions."
    "\n\n"
    "WORLD JEWISH CONGRESS: Elected president in 1981, serving until 2007. Led major "
    "campaigns including exposing Austrian president Kurt Waldheim's Nazi past, "
    "advocating for Soviet Jewry, and securing Holocaust compensation from Swiss banks. "
    "His successor as WJC president was Ronald Lauder, another Mega Group-adjacent figure."
    "\n\n"
    "NXIVM CONNECTION: Daughters Clare and Sara Bronfman became deep financial backers "
    "of NXIVM, the organization led by convicted sex trafficker Keith Raniere. Clare "
    "Bronfman invested over $100 million in NXIVM and was convicted in 2020 of "
    "racketeering conspiracy and sentenced to 81 months in federal prison. Edgar Sr. "
    "tried to intervene, calling NXIVM 'a cult' after learning Clare had given Raniere "
    "a $2 million loan, but was unable to extricate his daughters before his death in "
    "2013."
    "\n\n"
    "ORGANIZED CRIME LINEAGE: The Bronfman fortune originated during Prohibition, when "
    "father Samuel Bronfman's liquor operations intersected with the same organized crime "
    "networks — Lansky, Luciano — that form the foundation layer of this database. The "
    "family's transition from bootlegging to legitimate empire mirrors the broader pattern "
    "of organized crime capital being laundered into respectable institutions."
    "\n\n"
    "NETWORK POSITION: Through Seagram, the WJC, and the Mega Group (co-founded by "
    "brother Charles), Edgar Sr. sat at the center of the same philanthropic-intelligence "
    "nexus that connected Wexner to Epstein. The pattern of a billionaire dynasty with "
    "organized crime origins, pro-Israel intelligence connections, and family members "
    "entangled in sex trafficking operations is structurally significant."
)

_DESC_RONALD_LAUDER = (
    "Ronald Steven Lauder (b. 1944). Estee Lauder heir, Mega Group member, World "
    "Jewish Congress president, and a figure at the intersection of US defense policy, "
    "Israeli intelligence infrastructure, and conservative politics."
    "\n\n"
    "DEFENSE AND DIPLOMATIC CAREER: Served as Deputy Assistant Secretary of Defense for "
    "European and NATO policy (1983-1986) under Reagan. During this Pentagon tenure, "
    "Lauder became deeply involved in Israeli politics and formed an alliance with "
    "Benjamin Netanyahu, then Israel's UN representative. Appointed US Ambassador to "
    "Austria (1986-1987) by Reagan."
    "\n\n"
    "AUSTRIAN PASSPORT QUESTION: When Jeffrey Epstein was arrested in 2019, an Austrian "
    "passport with a fake name was found in his Manhattan safe. Lauder served as US "
    "Ambassador to Austria during the period the passport was reportedly issued. "
    "Investigative journalists have noted the timing and Lauder's position, though no "
    "official document has confirmed Lauder's involvement in obtaining the passport. "
    "This remains at the inference tier."
    "\n\n"
    "NETANYAHU ALLIANCE: One of the most important individuals in Netanyahu's rise to "
    "power, particularly during his upset 1996 election victory. Major financier of "
    "Israel's right-wing Likud Party. This relationship places Lauder at the center of "
    "the US-Israel political pipeline."
    "\n\n"
    "WORLD JEWISH CONGRESS: Succeeded Edgar Bronfman Sr. as WJC president in 2007 — "
    "inheriting the same institutional platform that connects to the Mega Group network."
    "\n\n"
    "INTELLIGENCE INFRASTRUCTURE: Long-time funder of IDC Herzliya (Reichman University), "
    "an Israeli university closely associated with Mossad recruitment and intelligence "
    "research. Also founded the Neue Galerie in New York (2001), dedicated to German "
    "and Austrian art."
    "\n\n"
    "MEGA GROUP: Member of the Mega Group alongside Wexner, the Bronfmans, Steinhardt, "
    "and others. His combination of Pentagon experience, Austrian diplomatic posting, "
    "Israeli intelligence connections, and Mega Group membership makes Lauder a key "
    "connector between US defense policy and the Israeli intelligence-philanthropy nexus."
)

_DESC_MICHAEL_STEINHARDT = (
    "Michael H. Steinhardt (b. 1940). Hedge fund pioneer, Mega Group member, "
    "Birthright Israel co-founder, serial sexual harasser, and looted antiquities "
    "trafficker whose father was a Genovese crime family fence."
    "\n\n"
    "ORGANIZED CRIME ORIGINS: Father Sol Frank 'Red McGee' Steinhardt was a convicted "
    "fence for the Genovese crime family — an associate of Meyer Lansky, Vincent "
    "'Jimmy Blue Eyes' Alo, and Albert Anastasia. Sol was convicted in 1958 for buying "
    "and selling stolen jewelry. Michael has written about visiting his father in prison "
    "as a child. His initial investment capital reportedly came from a bar mitzvah gift "
    "of stolen stock from his father. This organized crime lineage directly mirrors the "
    "Bronfman family pattern of criminal-origin wealth transitioning into respectable "
    "philanthropy."
    "\n\n"
    "HEDGE FUND CAREER: Founded Steinhardt, Fine, and Berkowitz (later Steinhardt "
    "Partners) in 1967, with backing from William Salomon of Salomon Brothers and Jack "
    "Nash of Odyssey Partners. Averaged 24.5% annual returns over 28 years — nearly "
    "triple the S&P 500. Closed the fund in 1995 after a $70 million SEC/DOJ settlement "
    "related to Treasury Note market manipulation."
    "\n\n"
    "MEGA GROUP: Member of the Mega Group alongside Wexner, Bronfman, and Lauder. "
    "Co-founded Birthright Israel with Charles Bronfman in 1994 — the signature project "
    "connecting American Jewish youth to Israel through free 10-day trips."
    "\n\n"
    "SEXUAL HARASSMENT: In 2019, seven women accused Steinhardt of a pattern of sexual "
    "harassment spanning decades. Allegations included propositioning subordinates, "
    "asking a rabbi to become his concubine, and requesting threesomes with female "
    "employees. Hillel International investigated and confirmed harassment of two "
    "employees. The pattern of powerful men in this network engaging in sexual "
    "predation is structurally consistent."
    "\n\n"
    "LOOTED ANTIQUITIES: In December 2021, the Manhattan DA forced Steinhardt to "
    "surrender 180 looted antiquities valued at $70 million, plundered from 11 "
    "countries. He received an unprecedented lifetime ban on acquiring antiquities. "
    "Objects had been illegally smuggled from Bulgaria, Egypt, Greece, Iraq, Israel, "
    "Italy, Jordan, Lebanon, Libya, Syria, and Turkey."
)

_DESC_GLENN_DUBIN = (
    "Glenn Russell Dubin (b. 1957). Hedge fund billionaire whose family maintained "
    "an intimate relationship with Jeffrey Epstein before, during, and after his "
    "conviction — including allowing Epstein to serve as godfather to their children."
    "\n\n"
    "HEDGE FUND CAREER: Born to a middle-class Jewish family in Washington Heights, "
    "Manhattan. Father was a taxi driver. After Stony Brook University, began at E.F. "
    "Hutton as a retail stockbroker. Co-founded Dubin & Swieca Capital Management in "
    "1984 and Highbridge Capital Management in 1992 with childhood friend Henry Swieca. "
    "JPMorgan purchased a majority stake in Highbridge for $1.3 billion in 2004. Under "
    "Dubin, Highbridge grew to over $35 billion AUM. Founded Engineers Gate (quantitative "
    "trading) in 2013."
    "\n\n"
    "EPSTEIN RELATIONSHIP — THE EVA ANDERSSON CONNECTION: Wife Eva Andersson-Dubin dated "
    "Jeffrey Epstein from 1981 to 1990. Epstein financially supported Andersson through "
    "medical school in Sweden and California. Glenn and Eva married in 1994. Despite "
    "this history — and despite Epstein's 2008 conviction — Jeffrey Epstein was named "
    "godfather to the Dubin children."
    "\n\n"
    "POST-CONVICTION CONTACT: After Epstein's release from jail in 2009, Andersson-Dubin "
    "wrote to Epstein's probation officer stating she was '100% comfortable with Jeffrey "
    "Epstein around her children' — all of whom were under 18 at the time. Released "
    "DOJ documents (Feb 2026) show Andersson-Dubin emailed Epstein inviting him to "
    "visit when her daughter would 'have 5 friends over.' The family continued "
    "socializing with Epstein after his conviction."
    "\n\n"
    "GIUFFRE ALLEGATIONS: In her 2016 deposition, Virginia Roberts Giuffre named Glenn "
    "Dubin among businessmen she was directed to have sex with by Epstein and Maxwell. "
    "She specifically alleged being trafficked to Dubin's home while his pregnant wife "
    "was 'asleep in the next room.' Dubin denied the allegations through a spokesperson. "
    "The US Virgin Islands subpoenaed Dubin for Epstein-related documents in 2020."
)

_DESC_JES_STALEY = (
    "James Edward 'Jes' Staley (b. 1956). Senior JPMorgan executive whose deep personal "
    "relationship with Jeffrey Epstein was documented in over 1,200 emails, including "
    "apparent coded references to young women using Disney princess names."
    "\n\n"
    "JPMORGAN CAREER: Joined Morgan Guaranty Trust in 1979 after graduating from Bowdoin "
    "College. Spent 34 years at JPMorgan, rising to head of the Private Banking division "
    "in 1999 — the unit responsible for managing Epstein's accounts. Under Staley's "
    "leadership, the private bank tripled its profitability."
    "\n\n"
    "EPSTEIN RELATIONSHIP: Met Epstein through the private banking relationship in the "
    "early 2000s. Former JPMorgan CEO reportedly told Staley he should meet Epstein as "
    "one of the 'most connected' people in finance. The relationship deepened into a "
    "profound personal friendship documented in 1,200+ emails exchanged over more than "
    "a decade — continuing after Epstein's 2008 conviction."
    "\n\n"
    "THE 'SNOW WHITE' EMAILS: In July 2010, Staley emailed Epstein saying 'Say hi to "
    "Snow White.' Epstein responded: 'What character would you like next?' When Staley "
    "said 'Beauty and the Beast,' Epstein replied: 'Well one side is available.' Virgin "
    "Islands prosecutors alleged these Disney princess references were code words for "
    "young women. In a 2008 email, Staley referenced his yacht being anchored 'in front "
    "of St Jeff' — the nickname they used for Epstein's island, Little Saint James."
    "\n\n"
    "BARCLAYS CEO: Left JPMorgan in 2013, became CEO of Barclays in December 2015. "
    "Forced to resign from Barclays in November 2021 after the FCA investigated his "
    "characterization of the Epstein relationship to regulators."
    "\n\n"
    "REGULATORY BAN: The UK Financial Conduct Authority banned Staley for life from "
    "working in financial services, finding he had misled regulators about the nature "
    "and extent of his relationship with Epstein. In March 2025, during testimony in "
    "related litigation, Staley admitted to having slept with an Epstein assistant. "
    "The Upper Tribunal upheld the FCA ban."
)

_DESC_STEVEN_HOFFENBERG = (
    "Steven Jude Hoffenberg (1945-2022). Jeffrey Epstein's early business partner and "
    "mentor who ran the largest Ponzi scheme in American history before Bernie Madoff — "
    "and who claimed Epstein was the 'architect' of the fraud."
    "\n\n"
    "TOWERS FINANCIAL: Founded Towers Financial Corporation, a debt collection agency "
    "that between 1988 and 1993 operated as a Ponzi scheme defrauding investors of "
    "$475 million. Hoffenberg hired Epstein in 1987 through a British defense "
    "contractor named Douglas Leese, paying him $25,000 per month and giving him a "
    "$2 million non-repayable loan in 1988."
    "\n\n"
    "EPSTEIN AS 'ARCHITECT': In court documents, Hoffenberg repeatedly claimed Epstein "
    "was 'intimately involved' in the Ponzi scheme and called him the 'architect of the "
    "scam.' Together, they attempted corporate raids on Pan Am and Emery Air Freight "
    "using Towers Financial as their vehicle. The Pan Am bid failed partly due to the "
    "Lockerbie bombing. Epstein departed Towers before its 1993 collapse and was never "
    "charged — a pattern of escaping accountability that would repeat throughout his "
    "career."
    "\n\n"
    "NEW YORK POST: Hoffenberg briefly owned the New York Post from January to March "
    "1993, rescuing it from bankruptcy. His tenure saw mass layoffs, a staff walkout, "
    "and missed issues before the Towers Financial collapse ended his ownership."
    "\n\n"
    "CONVICTION AND IMPRISONMENT: Pleaded guilty in 1995. Sentenced to 20 years in "
    "federal prison. Served 18 years. After release, he publicly accused Epstein of "
    "being a co-conspirator in the fraud and in 2016 filed suit seeking restitution."
    "\n\n"
    "DEATH: Found dead in his apartment in Derby, Connecticut, on August 23, 2022, "
    "at age 77. His body is believed to have lain undiscovered for at least seven days. "
    "Ruled a suicide. Hoffenberg had been vocal about Epstein's criminal involvement "
    "and had expressed willingness to assist investigations. He is the third figure in "
    "this network found dead by apparent suicide after making claims against powerful "
    "interests."
)

_DESC_LYNN_FORESTER = (
    "Lynn Forester, Lady de Rothschild (b. 1954). American-British businesswoman who "
    "served as a key social connector between Jeffrey Epstein and the Clinton-Rothschild "
    "orbit."
    "\n\n"
    "CAREER: Born in Bergen County, New Jersey. Phi Beta Kappa graduate of Pomona "
    "College, honors graduate of Columbia Law School. Worked at Simpson Thacher & "
    "Bartlett before entering telecommunications, helping billionaire John Kluge acquire "
    "cellular network licenses. Founded FirstMark Communications in 1995 and its European "
    "arm in 1998, sold in a $1 billion financing deal in 2000."
    "\n\n"
    "ROTHSCHILD MARRIAGE: Introduced to Sir Evelyn de Rothschild by Henry Kissinger at "
    "the 1998 Bilderberg Group conference. Married November 30, 2000. Sir Evelyn — a "
    "member of the fabulously wealthy European banking dynasty and almost 23 years her "
    "senior — left his wife and three children for the marriage. She became chair of "
    "E.L. Rothschild, the family holding company, after Sir Evelyn's death."
    "\n\n"
    "THE 1995 CLINTON LETTER: A letter preserved in the Clinton Presidential Library, "
    "dated April 1995, from Forester to President Clinton states: 'It was a pleasure to "
    "see you recently at Senator Kennedy's house... Using my fifteen seconds of access "
    "to discuss Jeffrey Epstein and currency stabilization, I neglected to talk to you "
    "about a topic near and dear to my heart.' The letter documents that Forester was "
    "discussing Epstein with the sitting President as early as 1995 — years before "
    "Epstein's public profile emerged."
    "\n\n"
    "EPSTEIN INTRODUCTIONS: According to multiple accounts, Forester de Rothschild "
    "served as a key introducer for Epstein. Alan Dershowitz stated she introduced him "
    "to Epstein, calling him an 'interesting autodidact.' Ghislaine Maxwell stated that "
    "Forester de Rothschild introduced Prince Andrew to Epstein. These introductions "
    "placed Epstein in direct contact with British royalty, the Rothschild banking "
    "dynasty, and the Clinton political network — dramatically expanding the reach of "
    "whatever operation Epstein was running."
    "\n\n"
    "NETWORK POSITION: Forester de Rothschild sits at the intersection of Democratic "
    "politics (Clinton), European banking (Rothschild), and the Epstein social network. "
    "Her role as introducer is one of the most documented examples of how Epstein gained "
    "access to heads of state and royalty through social gatekeepers."
)

_DESC_MORT_ZUCKERMAN = (
    "Mortimer Benjamin 'Mort' Zuckerman (b. 1937). Canadian-American billionaire media "
    "mogul and real estate investor whose financial and social relationship with Epstein "
    "included co-investing in a magazine and purchasing a newspaper from the Maxwell "
    "family estate."
    "\n\n"
    "MEDIA AND REAL ESTATE EMPIRE: Co-founder and executive chairman of Boston "
    "Properties, one of the largest real estate investment trusts in the US. Acquired "
    "The Atlantic (1980) and U.S. News & World Report (1984). Purchased the New York "
    "Daily News in 1993."
    "\n\n"
    "MAXWELL CONNECTION — DAILY NEWS: Zuckerman purchased the New York Daily News from "
    "Maxwell Newspapers Inc. — the company controlled by Robert Maxwell, Ghislaine "
    "Maxwell's father and documented Mossad asset. Robert Maxwell had acquired the "
    "Daily News from the Tribune Company in March 1991, then drowned under mysterious "
    "circumstances in November 1991. The paper filed for bankruptcy in December, and "
    "Zuckerman acquired it in 1993. This direct business succession from the Maxwell "
    "media empire is noteworthy."
    "\n\n"
    "RADAR MAGAZINE — EPSTEIN CO-INVESTMENT: In 2004, Zuckerman and Epstein committed "
    "up to $25 million as equal partners to finance Radar, a celebrity and pop culture "
    "magazine. The first issue appeared in April 2005. When sexual abuse allegations "
    "against Epstein surfaced, Zuckerman rapidly disassociated and shut down the "
    "publication approximately 14 months after launch."
    "\n\n"
    "EPSTEIN SOCIAL NETWORK: Contributed to Epstein's 2003 birthday book. Attended "
    "dinners at Epstein's home. Epstein and Zuckerman communicated regularly and "
    "arranged numerous meetings, according to DOJ documents released in 2026."
    "\n\n"
    "MEDIA INFLUENCE PRESSURE: According to the 2026 DOJ document release, Epstein "
    "leveraged his relationship with Zuckerman to attempt to influence the New York "
    "Daily News's coverage of allegations against him after his 2008 conviction. "
    "Zuckerman, notably, did not kill the story. However, the attempt to use media "
    "ownership relationships to manage coverage is a documented pattern in this network."
)

_DESC_STEVE_BING = (
    "Stephen Leo Bing (1965-2020). Billionaire real estate heir, film producer, and "
    "Democratic mega-donor who was a close Clinton associate. Died June 22, 2020, after "
    "falling from the 27th floor of his Century City apartment building."
    "\n\n"
    "INHERITANCE AND CAREER: At age 18, inherited $600 million from grandfather Leo S. "
    "Bing, a prominent 1920s real estate developer. Dropped out of Stanford University "
    "to pursue entertainment, founding Shangri-La Entertainment and Shangri-La Music. "
    "Produced films including 'The Polar Express' and wrote 'Kangaroo Jack.' Invested "
    "in real estate and construction."
    "\n\n"
    "CLINTON RELATIONSHIP: One of the largest individual donors to the Clinton "
    "Foundation, contributing between $10-25 million. In August 2009, Bing provided his "
    "private Boeing 737 for Bill Clinton's mission to North Korea to secure the release "
    "of American journalists Laura Ling and Euna Lee, covering the estimated $200,000 "
    "cost. Clinton praised Bing publicly after his death."
    "\n\n"
    "POLITICAL SPENDING: Major Democratic donor who contributed millions to party "
    "officials and causes, including Hillary Clinton, Nancy Pelosi, Dick Durbin, Rahm "
    "Emanuel, and Al Franken. Supported progressive ballot initiatives in California."
    "\n\n"
    "DEATH: On June 22, 2020, Bing fell from the 27th floor of the Ten Thousand "
    "building in Century City, Los Angeles. Ruled a suicide. Friends suggested he had "
    "been depressed about isolation during the COVID-19 quarantine. At the time of "
    "his death, his liquid assets had dwindled to approximately $300,000 — having spent "
    "nearly the entire $600 million inheritance. Bing's death came approximately 10 "
    "months after Epstein's death in custody, during a period when multiple Epstein "
    "associates died under notable circumstances."
    "\n\n"
    "PERSONAL LIFE: Had a son, Damian Hurley (b. 2002), with actress Elizabeth Hurley. "
    "Initially denied paternity; a DNA test established him as the father."
)

_DESC_TOM_BARRACK = (
    "Thomas Joseph Barrack Jr. (b. 1947). Private equity billionaire, founder of Colony "
    "Capital, Donald Trump's longest-serving confidant, and a figure whose Middle East "
    "financial connections intersect with the Epstein network."
    "\n\n"
    "BACKGROUND: Grandparents were Lebanese Maronite Christians who immigrated from "
    "Zahle to the US in 1900. Raised in Culver City, California. Father was a grocer. "
    "Began career as a finance lawyer, working on project finance for Aramco in Saudi "
    "Arabia. Served as CEO of Dunn International Corporation, then Senior VP at E.F. "
    "Hutton on Wall Street, then principal with the Robert M. Bass Group."
    "\n\n"
    "COLONY CAPITAL: Founded Colony Capital in 1991 (now DigitalBridge) with initial "
    "investments from Bass and GE Capital. Grew it into one of the world's largest "
    "private equity real estate firms with operations in 19 countries. Between June "
    "2018 and Trump's presidency, Colony raised over $7 billion, with 24% coming from "
    "the UAE and Saudi Arabia."
    "\n\n"
    "TRUMP RELATIONSHIP: Friends since the 1980s New York real estate market. Barrack "
    "sold Trump a stake in a department store (1985) and the Plaza Hotel ($410M, 1988). "
    "Served as senior advisor to Trump's 2016 campaign, chairman of the 2017 Inaugural "
    "Committee (raised record-breaking funds), and in the second administration as US "
    "Ambassador to Turkey, Special Envoy for Syria, and Special Envoy for Iraq."
    "\n\n"
    "UAE INDICTMENT AND ACQUITTAL: In July 2021, indicted for acting as an unregistered "
    "agent of the UAE (April 2016-April 2018). Prosecutors alleged he inserted language "
    "praising the UAE into a Trump campaign energy speech, emailed advance drafts to UAE "
    "officials, and sought an ambassadorship that would 'give Abu Dhabi more power.' "
    "UAE sovereign wealth funds invested $374 million in Colony Capital projects. "
    "Acquitted on all charges in November 2022."
    "\n\n"
    "EPSTEIN CONTACT: DOJ documents released in February 2026 reveal Barrack was in "
    "regular, close contact with Epstein for years after Epstein's 2008 conviction. In "
    "September 2009, months after Epstein's release, Barrack wrote: 'Thinking about u, "
    "hope u r good and life is calm again.' Exchanges include invitations to private "
    "residences, introductions to diplomats and investors, and business discussions. "
    "Epstein facilitated introductions for Barrack to Peter Thiel, Ehud Barak, and "
    "Russia's UN representative Vitaly Churkin. Epstein repeatedly urged Barrack to "
    "move communications to encrypted messaging apps. No evidence Barrack participated "
    "in or had knowledge of Epstein's criminal conduct."
)


# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # ---- People ----
    {"name": "Charles Bronfman", "entity_type": "person", "description": _DESC_CHARLES_BRONFMAN, "aliases": "Charles Rosner Bronfman", "metadata": {"birth_date": "1931-06-27", "nationality": "Canadian-American", "status": "alive"}},
    {"name": "Edgar Bronfman Sr.", "entity_type": "person", "description": _DESC_EDGAR_BRONFMAN_SR, "aliases": "Edgar Miles Bronfman", "metadata": {"birth_date": "1929-06-20", "death_date": "2013-12-21", "nationality": "Canadian-American", "status": "deceased"}},
    {"name": "Ronald Lauder", "entity_type": "person", "description": _DESC_RONALD_LAUDER, "aliases": "Ronald Steven Lauder", "metadata": {"birth_date": "1944-02-26", "nationality": "American", "status": "alive"}},
    {"name": "Michael Steinhardt", "entity_type": "person", "description": _DESC_MICHAEL_STEINHARDT, "aliases": "", "metadata": {"birth_date": "1940-12-07", "nationality": "American", "status": "alive"}},
    {"name": "Glenn Dubin", "entity_type": "person", "description": _DESC_GLENN_DUBIN, "aliases": "Glenn Russell Dubin", "metadata": {"birth_date": "1957-04-13", "nationality": "American", "status": "alive"}},
    {"name": "Jes Staley", "entity_type": "person", "description": _DESC_JES_STALEY, "aliases": "James Edward Staley", "metadata": {"birth_date": "1956-12-27", "nationality": "American", "status": "alive"}},
    {"name": "Steven Hoffenberg", "entity_type": "person", "description": _DESC_STEVEN_HOFFENBERG, "aliases": "Steven Jude Hoffenberg", "metadata": {"birth_date": "1945-01-12", "death_date": "2022-08-23", "nationality": "American", "status": "deceased"}},
    {"name": "Lynn Forester de Rothschild", "entity_type": "person", "description": _DESC_LYNN_FORESTER, "aliases": "Lynn Forester, Lady de Rothschild", "metadata": {"birth_date": "1954-07-02", "nationality": "American-British", "status": "alive"}},
    {"name": "Mort Zuckerman", "entity_type": "person", "description": _DESC_MORT_ZUCKERMAN, "aliases": "Mortimer Benjamin Zuckerman", "metadata": {"birth_date": "1937-06-04", "nationality": "Canadian-American", "status": "alive"}},
    {"name": "Steve Bing", "entity_type": "person", "description": _DESC_STEVE_BING, "aliases": "Stephen Leo Bing", "metadata": {"birth_date": "1965-03-31", "death_date": "2020-06-22", "nationality": "American", "status": "deceased"}},
    {"name": "Tom Barrack", "entity_type": "person", "description": _DESC_TOM_BARRACK, "aliases": "Thomas Joseph Barrack Jr.", "metadata": {"birth_date": "1947-04-28", "nationality": "American", "status": "alive"}},

    # ---- Organizations ----
    {"name": "Towers Financial", "entity_type": "organization", "description": (
        "Towers Financial Corporation. New York debt collection agency founded by Steven "
        "Hoffenberg that operated as the largest Ponzi scheme in American history prior to "
        "Bernie Madoff, defrauding investors of $475 million between 1988 and 1993. Jeffrey "
        "Epstein was hired by Hoffenberg in 1987 at $25,000 per month plus a $2 million "
        "non-repayable loan. Hoffenberg later called Epstein the 'architect of the scam' in "
        "court documents. Together they attempted failed corporate raids on Pan Am and Emery "
        "Air Freight. Hoffenberg briefly used Towers to acquire the New York Post in 1993 "
        "before the scheme collapsed. Epstein departed before the collapse and was never "
        "charged — establishing the pattern of escaping accountability that defined his career. "
        "Towers Financial represents the origin story of Epstein's financial career: learning "
        "the mechanics of large-scale financial fraud."
    ), "aliases": "Towers Financial Corporation"},
    {"name": "Seagram", "entity_type": "organization", "description": (
        "Seagram Company Ltd. One of the world's largest beverage companies, built by the "
        "Bronfman family. Founded as Distillers Corporation by Samuel Bronfman in Montreal "
        "in 1924, acquiring Joseph E. Seagram & Sons in 1928. The Bronfman fortune originated "
        "during American Prohibition, when the family legally exported spirits from Canada to "
        "US bootleggers — a business that intersected with organized crime networks controlled "
        "by Meyer Lansky and Lucky Luciano. Sons Edgar Sr. and Charles inherited the empire "
        "in 1971. Seagram held a 25% stake in DuPont (the largest shareholder) before Edgar "
        "Jr. sold it for $8.8 billion in 1995 to acquire MCA/Universal Studios. In 2000, "
        "Edgar Jr. merged Seagram with Vivendi in a $42 billion deal that destroyed the "
        "family empire — the Bronfmans' 8.6% of Vivendi Universal was worth a fraction of "
        "the original Seagram. Distilling assets went to Pernod Ricard and Diageo. The "
        "Bronfman-Seagram network is central to the Mega Group and the broader web of "
        "pro-Israel billionaire philanthropy connected to the Epstein operation."
    ), "aliases": "Seagram Company, Distillers Corporation-Seagram"},
    {"name": "Birthright Israel", "entity_type": "organization", "description": (
        "Birthright Israel (Taglit). Free 10-day trip program for Jewish young adults aged "
        "18-26 to visit Israel. Co-founded in 1994 by Mega Group members Charles Bronfman "
        "and Michael Steinhardt, with the first trip in 1999. Motivated by the 1990 National "
        "Jewish Population Survey showing 52% intermarriage rates. Bronfman and Steinhardt "
        "each contributed $8 million initially. Funded 67% by individual donors, 27% by the "
        "Israeli government, 3% by Jewish federations, and 3% by the Jewish Agency. Over "
        "800,000 participants by 2024. Birthright represents the Mega Group's signature "
        "public initiative — connecting American Jewish identity to the Israeli state through "
        "the same network of billionaire donors whose members intersect with the Epstein "
        "operation."
    ), "aliases": "Taglit, Taglit-Birthright Israel"},
    {"name": "Colony Capital", "entity_type": "organization", "description": (
        "Colony Capital LLC (now DigitalBridge). Private equity real estate firm founded by "
        "Tom Barrack in 1991, with initial investments from Robert M. Bass and GE Capital. "
        "Grew into one of the world's largest PE real estate firms with operations in 19 "
        "countries. During Trump's presidency, Colony raised over $7 billion, with 24% "
        "coming from UAE and Saudi sovereign wealth funds — $374 million from UAE entities "
        "alone, per the DOJ indictment. Barrack was indicted in 2021 for acting as an "
        "unregistered agent of the UAE while simultaneously chairing Trump's inaugural "
        "committee — though acquitted in 2022. Rebranded as DigitalBridge in June 2021, "
        "pivoting to digital infrastructure. The firm represents the financial pipeline "
        "between Gulf state sovereign wealth and Trump-aligned political influence."
    ), "aliases": "DigitalBridge, Colony Capital LLC"},
]


# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # ---- Charles Bronfman ----
    {"source": "Charles Bronfman", "target": "Mega Group", "type": "founder_of", "tier": "documented", "desc": "Co-founded the Mega Group with Les Wexner in 1991 — secretive gathering of wealthiest pro-Israel donors.", "sources": [76, 11]},
    {"source": "Charles Bronfman", "target": "Seagram", "type": "director_of", "tier": "documented", "desc": "Held various executive positions at Seagram from 1951 to 2000. Co-inherited the empire with brother Edgar Sr. in 1971.", "sources": [91]},
    {"source": "Charles Bronfman", "target": "Birthright Israel", "type": "founder_of", "tier": "documented", "desc": "Co-founded Birthright Israel in 1994 with Michael Steinhardt. Each contributed $8 million initially.", "sources": [76]},
    {"source": "Charles Bronfman", "target": "Robert Maxwell", "type": "associate_of", "tier": "credible", "desc": "Business partner of Robert Maxwell — connecting Bronfman network to Maxwell intelligence pipeline.", "sources": [76]},
    {"source": "Charles Bronfman", "target": "Edgar Bronfman Sr.", "type": "family_of", "tier": "documented", "desc": "Brothers who co-inherited the Seagram empire upon father Samuel's death in 1971.", "sources": [91]},

    # ---- Edgar Bronfman Sr. ----
    {"source": "Edgar Bronfman Sr.", "target": "Seagram", "type": "director_of", "tier": "documented", "desc": "President, treasurer, and CEO of Seagram from 1971 until son Edgar Jr. succeeded him in 1994.", "sources": [91]},
    {"source": "Edgar Bronfman Sr.", "target": "Mega Group", "type": "member_of", "tier": "credible", "desc": "Connected to the Mega Group through brother Charles's co-founding role and shared philanthropic-political network.", "sources": [76]},
    {"source": "Edgar Bronfman Sr.", "target": "Ronald Lauder", "type": "connected_to", "tier": "documented", "desc": "Lauder succeeded Edgar Bronfman Sr. as president of the World Jewish Congress in 2007.", "sources": [76]},

    # ---- Ronald Lauder ----
    {"source": "Ronald Lauder", "target": "Mega Group", "type": "member_of", "tier": "credible", "desc": "Member of the Mega Group, the secretive annual gathering of the wealthiest pro-Israel donors.", "sources": [76]},
    {"source": "Ronald Lauder", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "inference", "desc": "Lauder was US Ambassador to Austria when Epstein's fraudulent Austrian passport was reportedly issued. No official document confirms involvement.", "sources": [76, 11]},
    {"source": "Ronald Lauder", "target": "Mossad", "type": "connected_to", "tier": "inference", "desc": "Long-time funder of IDC Herzliya (Reichman University), closely associated with Mossad recruitment. Deputy Assistant SecDef with deep Israeli connections.", "sources": [76]},

    # ---- Michael Steinhardt ----
    {"source": "Michael Steinhardt", "target": "Mega Group", "type": "member_of", "tier": "credible", "desc": "Member of the Mega Group alongside Wexner, Bronfman, Lauder.", "sources": [76]},
    {"source": "Michael Steinhardt", "target": "Birthright Israel", "type": "founder_of", "tier": "documented", "desc": "Co-founded Birthright Israel in 1994 with Charles Bronfman. Chairman of the board.", "sources": [76, 77]},
    {"source": "Michael Steinhardt", "target": "Meyer Lansky", "type": "connected_to", "tier": "credible", "desc": "Father Sol 'Red McGee' Steinhardt was a Genovese crime family fence and associate of Meyer Lansky, Jimmy Blue Eyes Alo, and Albert Anastasia.", "sources": [76, 11]},
    {"source": "Michael Steinhardt", "target": "Genovese Crime Family", "type": "connected_to", "tier": "credible", "desc": "Father Sol Steinhardt was a convicted fence for the Genovese crime family.", "sources": [76]},

    # ---- Glenn Dubin ----
    {"source": "Glenn Dubin", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "documented", "desc": "Intimate family relationship. Epstein named godfather to Dubin children. Socialized before and after Epstein's conviction.", "sources": [78, 29, 94]},
    {"source": "Glenn Dubin", "target": "Jeffrey Epstein", "type": "procured_for", "tier": "credible", "desc": "Virginia Giuffre alleged in 2016 deposition she was trafficked to Dubin while his pregnant wife slept in the next room. Dubin denied.", "sources": [29, 78]},
    {"source": "Glenn Dubin", "target": "JPMorgan Chase", "type": "connected_to", "tier": "documented", "desc": "JPMorgan purchased majority stake in Dubin's Highbridge Capital Management for $1.3 billion in 2004.", "sources": [78]},

    # ---- Jes Staley ----
    {"source": "Jes Staley", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "documented", "desc": "1,200+ emails over a decade. 'Snow White' coded references. Referenced anchoring yacht at 'St Jeff' (Little Saint James). Relationship persisted after conviction.", "sources": [79, 86, 92]},
    {"source": "Jes Staley", "target": "JPMorgan Chase", "type": "employed_by", "tier": "documented", "desc": "34 years at JPMorgan. Head of Private Banking from 1999 — the unit managing Epstein's accounts.", "sources": [79, 4]},
    {"source": "Jes Staley", "target": "Little Saint James", "type": "connected_to", "tier": "credible", "desc": "Emails reference anchoring yacht 'in front of St Jeff' — their nickname for Epstein's island.", "sources": [79, 92]},

    # ---- Steven Hoffenberg ----
    {"source": "Steven Hoffenberg", "target": "Jeffrey Epstein", "type": "employed_by", "tier": "documented", "desc": "Hired Epstein in 1987 at $25,000/month plus $2M non-repayable loan. Called Epstein 'architect' of $475M Ponzi scheme.", "sources": [80, 84, 85, 95]},
    {"source": "Steven Hoffenberg", "target": "Towers Financial", "type": "founder_of", "tier": "documented", "desc": "Founded Towers Financial Corporation, which ran the largest pre-Madoff Ponzi scheme ($475M, 1988-1993).", "sources": [85, 80]},
    {"source": "Jeffrey Epstein", "target": "Towers Financial", "type": "connected_to", "tier": "documented", "desc": "Worked at Towers Financial 1987-1993. Hoffenberg called him 'architect of the scam.' Attempted Pan Am and Emery Air Freight raids. Never charged.", "sources": [85, 95]},

    # ---- Lynn Forester de Rothschild ----
    {"source": "Lynn Forester de Rothschild", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "documented", "desc": "Friends with Epstein. 1995 letter to Clinton discusses Epstein. Introduced Epstein to Dershowitz and reportedly to Prince Andrew.", "sources": [89, 11]},
    {"source": "Lynn Forester de Rothschild", "target": "Bill Clinton", "type": "connected_to", "tier": "documented", "desc": "1995 letter to Clinton discusses 'Jeffrey Epstein and currency stabilization.' Attended events at Senator Kennedy's house.", "sources": [89]},
    {"source": "Lynn Forester de Rothschild", "target": "Alan Dershowitz", "type": "introduced_by", "tier": "credible", "desc": "Dershowitz stated Forester de Rothschild introduced him to Epstein, calling him an 'interesting autodidact.'", "sources": [11, 89]},

    # ---- Mort Zuckerman ----
    {"source": "Mort Zuckerman", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "documented", "desc": "Co-invested $25M in Radar Magazine (2004). Attended dinners at Epstein's home. Epstein pressured Zuckerman to influence Daily News coverage.", "sources": [81, 83, 94]},
    {"source": "Mort Zuckerman", "target": "Robert Maxwell", "type": "connected_to", "tier": "documented", "desc": "Purchased the New York Daily News from Maxwell Newspapers Inc. after Robert Maxwell's 1991 death — direct business succession from the Maxwell media empire.", "sources": [81]},
    {"source": "Mort Zuckerman", "target": "Mega Group", "type": "connected_to", "tier": "credible", "desc": "Mega Group-adjacent figure. Part of the same billionaire pro-Israel philanthropic network.", "sources": [76]},

    # ---- Steve Bing ----
    {"source": "Steve Bing", "target": "Bill Clinton", "type": "patron_of", "tier": "documented", "desc": "Donated $10-25M to Clinton Foundation. Provided his Boeing 737 for Clinton's 2009 North Korea mission (~$200K cost).", "sources": [94]},

    # ---- Tom Barrack ----
    {"source": "Tom Barrack", "target": "Donald Trump", "type": "advisor_to", "tier": "documented", "desc": "Friends since 1980s NYC real estate. Senior advisor to 2016 campaign. Inaugural Committee chair. Now US Ambassador to Turkey.", "sources": [82, 88, 93]},
    {"source": "Tom Barrack", "target": "Jeffrey Epstein", "type": "associate_of", "tier": "documented", "desc": "Regular close contact documented in 100+ texts/emails (DOJ 2026 release). Continued post-conviction. Epstein facilitated introductions to Thiel, Barak, diplomats.", "sources": [82, 94]},
    {"source": "Tom Barrack", "target": "Colony Capital", "type": "founder_of", "tier": "documented", "desc": "Founded Colony Capital in 1991. Built it into one of the world's largest PE real estate firms.", "sources": [93]},
    {"source": "Tom Barrack", "target": "Peter Thiel", "type": "connected_to", "tier": "documented", "desc": "Epstein facilitated introduction between Barrack and Peter Thiel, per DOJ documents.", "sources": [82, 94]},
    {"source": "Tom Barrack", "target": "Ehud Barak", "type": "connected_to", "tier": "documented", "desc": "Epstein facilitated introduction between Barrack and former Israeli PM Ehud Barak, per DOJ documents.", "sources": [82, 94]},

    # ---- MC2 Model Management ----
    {"source": "Jeffrey Epstein", "target": "MC2 Model Management", "type": "financed_by", "tier": "documented", "desc": "Epstein provided up to $1 million in 2004 seed funding to launch MC2 with Jean-Luc Brunel.", "sources": [87, 29]},
    {"source": "Ghislaine Maxwell", "target": "MC2 Model Management", "type": "connected_to", "tier": "credible", "desc": "Named alongside Epstein and Brunel in court filings alleging MC2 was used as a pipeline for sex trafficking of minors.", "sources": [87, 29]},

    # ---- Organization relationships ----
    {"source": "Seagram", "target": "Mega Group", "type": "connected_to", "tier": "credible", "desc": "Bronfman family fortune from Seagram funded Mega Group activities. Charles co-founded it; Edgar Sr. connected through shared network.", "sources": [76, 91]},
    {"source": "Colony Capital", "target": "Donald Trump", "type": "connected_to", "tier": "documented", "desc": "Colony raised $7B+ during Trump era, 24% from UAE/Saudi. Barrack chaired inaugural committee while Colony received $374M in UAE sovereign wealth investment.", "sources": [88, 93]},

    # ---- Cross-cluster connections ----
    {"source": "Charles Bronfman", "target": "Les Wexner", "type": "associate_of", "tier": "documented", "desc": "Co-founded the Mega Group together in 1991. Coordinated billionaire pro-Israel philanthropy and political activity.", "sources": [76, 11]},
    {"source": "Michael Steinhardt", "target": "Charles Bronfman", "type": "associate_of", "tier": "documented", "desc": "Co-founded Birthright Israel together in 1994. Fellow Mega Group members.", "sources": [76, 77]},
    {"source": "Ronald Lauder", "target": "Les Wexner", "type": "associate_of", "tier": "credible", "desc": "Fellow Mega Group members. Both connected to the pro-Israel billionaire philanthropic network surrounding Epstein.", "sources": [76]},
    {"source": "Jes Staley", "target": "Glenn Dubin", "type": "connected_to", "tier": "credible", "desc": "Both in Epstein's inner financial circle. Staley ran JPMorgan private bank; JPMorgan bought Dubin's Highbridge Capital.", "sources": [79, 78]},
    {"source": "Lynn Forester de Rothschild", "target": "Ghislaine Maxwell", "type": "connected_to", "tier": "credible", "desc": "Maxwell stated Forester de Rothschild introduced Prince Andrew to Epstein — placing both women in the introducer role for the network.", "sources": [11]},
    {"source": "Steve Bing", "target": "Jeffrey Epstein", "type": "connected_to", "tier": "credible", "desc": "Both in Clinton's orbit. Bing's death (June 2020) came 10 months after Epstein's death — during period of multiple notable deaths of Epstein associates.", "sources": [94]},
    {"source": "Mort Zuckerman", "target": "MC2 Model Management", "type": "connected_to", "tier": "inference", "desc": "Zuckerman's media empire (Daily News) and co-investment with Epstein (Radar) placed him in Epstein's business network alongside the MC2 trafficking pipeline.", "sources": [81, 83]},
]


# ============================================================
# ENTITY-SOURCE LINKS
# ============================================================

ENTITY_SOURCES = {
    'Birthright Israel': [76, 77],
    'Charles Bronfman': [76, 91, 11],
    'Colony Capital': [88, 93, 82],
    'Edgar Bronfman Sr.': [76, 91, 11],
    'Glenn Dubin': [78, 29, 94],
    'Jes Staley': [79, 86, 92, 4],
    'Lynn Forester de Rothschild': [89, 11],
    'Michael Steinhardt': [76, 77, 90, 11],
    'Mort Zuckerman': [81, 83, 94],
    'Ronald Lauder': [76, 11],
    'Seagram': [91, 76],
    'Steve Bing': [94],
    'Steven Hoffenberg': [80, 84, 85, 95],
    'Tom Barrack': [82, 88, 93, 94],
    'Towers Financial': [85, 80, 95],
}
