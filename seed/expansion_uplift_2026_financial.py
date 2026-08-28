"""
Financial Control — August 2026 uplift expansion for Intel Console.

Brings the Financial Control branch up to date through August 28, 2026.
Covers the JPMorgan-Epstein accountability arc (Wyden Senate investigation,
$1.3B retroactive SARs, named executives), crypto-political nexus
(World Liberty Financial, GENIUS Act, CZ pardon, Strategic Bitcoin Reserve),
Federal Reserve conflicts (Warsh confirmation, Trump v. Cook, IEEPA tariff
ruling), BIS leadership transition, and foundation updates.

NEW ENTITIES (10):
  Kevin Warsh, World Liberty Financial, GENIUS Act, Changpeng Zhao,
  Strategic Bitcoin Reserve, IEEPA Tariff Ruling (2026),
  Trump v. Cook (2026), Wyden Epstein-JPMorgan Investigation (2025),
  Pablo Hernández de Cos, Mary Erdoes

EXISTING ENTITIES referenced (NOT duplicated):
  Donald Trump [33], Jeffrey Epstein [1], JPMorgan Chase [56],
  Federal Reserve System [331], DOJ [89], Ronald Lauder [121],
  BlackRock [395], Jes Staley [124], Leon Black [30],
  Ghislaine Maxwell [2], 2008 Financial Crisis [411],
  Bank for International Settlements [394], International Monetary Fund [398],
  Goldman Sachs [401], World Economic Forum [818], Larry Fink [405],
  Wexner House Oversight Deposition (2026) [105],
  Bill & Melinda Gates Foundation [482], Open Society Foundations [707],
  Deutsche Bank [57], Apollo Global Management [69]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1900–1938
# ============================================================

SOURCES = [
    # --- JPMorgan / Epstein / Wyden investigation ---
    {
        "id": 1900,
        "title": "How J.P. Morgan Enabled Jeffrey Epstein — NPR / NYT Magazine",
        "url": "https://www.npr.org/2025/09/09/nx-s1-5535548/how-j-p-morgan-enabled-jeffrey-epstein",
        "source_type": "journalism",
        "author": "NPR",
        "year": 2025,
    },
    {
        "id": 1901,
        "title": "Continuing Epstein Investigation, Wyden Probes Major JPMorgan Chase Compliance Failures — Senate Finance Committee",
        "url": "https://www.finance.senate.gov/ranking-members-news/continuing-epstein-investigation-wyden-probes-major-jpmorgan-chase-compliance-failures",
        "source_type": "congressional",
        "year": 2025,
    },
    {
        "id": 1902,
        "title": "Wyden Releases New Analysis Detailing How Top JPMorgan Chase Executives Enabled Epstein's Sex Trafficking Operation — Senate Finance Committee",
        "url": "https://www.finance.senate.gov/ranking-members-news/continuing-epstein-investigation-wyden-releases-new-analysis-detailing-how-top-jpmorgan-chase-executives-enabled-epsteins-sex-trafficking-operation",
        "source_type": "congressional",
        "year": 2025,
    },
    {
        "id": 1903,
        "title": "Memorandum to Senator Wyden on JPMC-Epstein (redacted) — Senate Finance Committee",
        "url": "https://www.finance.senate.gov/imo/media/doc/memorandum_to_senator_wyden_on_jpmc-epstein_redactedpdf.pdf",
        "source_type": "congressional",
        "year": 2025,
    },
    # --- Jes Staley FCA ---
    {
        "id": 1904,
        "title": "Upper Tribunal Upholds Jes Staley Ban — UK Financial Conduct Authority",
        "url": "https://www.fca.org.uk/news/press-releases/upper-tribunal-upholds-jes-staley-ban",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 1905,
        "title": "Ex-Barclays CEO Staley's Lifetime FCA Ban to Remain — Banking Dive",
        "url": "https://www.bankingdive.com/news/jes-staley-fca-lifetime-ban-banking-epstein-barclays-uk/751754/",
        "source_type": "journalism",
        "year": 2025,
    },
    # --- Federal Reserve / Kevin Warsh ---
    {
        "id": 1906,
        "title": "Federal Reserve Board Names Jerome H. Powell as Chair Pro Tempore; Warsh to Be Sworn In — Federal Reserve",
        "url": "https://www.federalreserve.gov/newsevents/pressreleases/other20260515a.htm",
        "source_type": "government",
        "year": 2026,
    },
    {
        "id": 1907,
        "title": "Kevin Warsh — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Kevin_Warsh",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1908,
        "title": "Senate Panel Advances Kevin Warsh's Nomination for US Fed Chair — Al Jazeera",
        "url": "https://www.aljazeera.com/economy/2026/4/29/senate-panel-advances-kevin-warshs-nomination-for-us-fed-chair",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 1909,
        "title": "Powell's Term as Federal Reserve Chair Comes to an End as Warsh Takes On Role — Spectrum News",
        "url": "https://spectrumlocalnews.com/us/snplus/politics/2026/05/15/jerome-powell-term-chair-kevin-warsh-president-trump-interest-rates-criticim-",
        "source_type": "journalism",
        "year": 2026,
    },
    # --- Lisa Cook / Trump v. Cook ---
    {
        "id": 1910,
        "title": "Court Prevents Trump from Firing Fed Governor — SCOTUSblog",
        "url": "https://www.scotusblog.com/2026/06/court-prevents-trump-from-firing-fed-governor/",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 1911,
        "title": "Lisa Cook Responds to Supreme Court Fed Ruling Against Trump — Newsweek",
        "url": "https://www.newsweek.com/supreme-court-federal-reserve-lisa-cook-donald-trump-12135615",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 1912,
        "title": "Supreme Court Rules Trump Cannot Fire Fed Governor Lisa Cook for Now — CNBC",
        "url": "https://www.cnbc.com/2026/06/29/supreme-court-lisa-cook-trump-federal-reserve.html",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 1913,
        "title": "Supreme Court Rules Trump Can't Fire Fed Member Lisa Cook — NBC News",
        "url": "https://www.nbcnews.com/politics/supreme-court/supreme-court-rules-trump-cannot-fire-fed-member-lisa-cook-grants-powe-rcna234931",
        "source_type": "journalism",
        "year": 2026,
    },
    # --- Stephen Miran ---
    {
        "id": 1914,
        "title": "Stephen Miran — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Stephen_Miran",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1915,
        "title": "Fed's Stephen Miran Resigns from White House Post — CNBC",
        "url": "https://www.cnbc.com/2026/02/03/feds-stephen-miran-resigns-from-white-house-post.html",
        "source_type": "journalism",
        "year": 2026,
    },
    # --- GENIUS Act ---
    {
        "id": 1916,
        "title": "GENIUS Act — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/GENIUS_Act",
        "source_type": "other",
        "year": 2025,
    },
    {
        "id": 1917,
        "title": "GENIUS Act Signed into Law: US Enacts Federal Stablecoin Legislation — Mayer Brown",
        "url": "https://www.mayerbrown.com/en/insights/publications/2025/07/genius-act-signed-into-law-us-enacts-federal-stablecoin-legislation",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 1918,
        "title": "Stablecoin Legislation: The Senate Passes the GENIUS Act — Sullivan & Cromwell",
        "url": "https://www.sullcrom.com/insights/memo/2025/June/Stablecoin-Legislation-Senate-Passes-GENIUS-Act",
        "source_type": "journalism",
        "year": 2025,
    },
    # --- World Liberty Financial ---
    {
        "id": 1919,
        "title": "World Liberty Financial — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/World_Liberty_Financial",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1920,
        "title": "Trump Family-Backed Crypto Firm World Liberty Gets Conditional Bank Charter Approval — CNBC",
        "url": "https://www.cnbc.com/2026/08/14/world-liberty-trump-occ-bank-charter-stablecoin.html",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 1921,
        "title": "Trump Reports Over $1 Billion in Income From Crypto Ventures — Time",
        "url": "https://time.com/article/2026/07/01/trump-2025-financial-disclosure-crypto-world-liberty-financial/",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 1922,
        "title": "Trump-Backed World Liberty Financial Raises $550 Million in Token Sales — Fortune",
        "url": "https://fortune.com/crypto/2025/03/18/trump-backed-world-liberty-financial-raises-550-million-token-sales",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 1923,
        "title": "Trump-Linked Crypto Venture World Liberty Trust Granted Bank Status — ABC News",
        "url": "https://abcnews.com/Business/trump-linked-crypto-venture-world-liberty-trust-granted/story?id=135668756",
        "source_type": "journalism",
        "year": 2026,
    },
    # --- Changpeng Zhao / Binance pardon ---
    {
        "id": 1924,
        "title": "Trump Pardons Binance Founder Changpeng Zhao — CNN",
        "url": "https://www.cnn.com/2025/10/23/politics/binance-founder-trump-pardon",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 1925,
        "title": "Trump Pardons Binance Founder CZ Zhao — CNBC",
        "url": "https://www.cnbc.com/2025/10/23/trump-pardons-binance-founder-cz-zhao.html",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 1926,
        "title": "Trump Pardons Binance Founder Changpeng Zhao — PBS NewsHour",
        "url": "https://www.pbs.org/newshour/amp/politics/trump-pardons-binance-founder-changpeng-zhao",
        "source_type": "journalism",
        "year": 2025,
    },
    {
        "id": 1927,
        "title": "Changpeng Zhao — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Changpeng_Zhao",
        "source_type": "other",
        "year": 2026,
    },
    {
        "id": 1928,
        "title": "Pardon of Changpeng Zhao — U.S. Department of Justice Office of the Pardon Attorney",
        "url": "https://www.justice.gov/pardon/media/1416576/dl?inline=",
        "source_type": "government",
        "year": 2025,
    },
    {
        "id": 1929,
        "title": "Pardoned Binance Founder Zhao Says His Business Relationship with the Trumps Was 'Misconstrued' — CNBC",
        "url": "https://www.cnbc.com/2026/01/23/pardon-binance-founder-cz-trump.html",
        "source_type": "journalism",
        "year": 2026,
    },
    # --- IEEPA tariff ruling ---
    {
        "id": 1930,
        "title": "Supreme Court Strikes Down IEEPA Tariffs: What Now — WilmerHale",
        "url": "https://www.wilmerhale.com/en/insights/client-alerts/20260220-supreme-court-strikes-down-ieepa-tariffs-what-now",
        "source_type": "journalism",
        "year": 2026,
    },
    {
        "id": 1931,
        "title": "The Remaining Questions After the Supreme Court's Tariffs Ruling — SCOTUSblog",
        "url": "https://www.scotusblog.com/2026/03/the-remaining-questions-after-the-supreme-courts-tariffs-ruling/",
        "source_type": "journalism",
        "year": 2026,
    },
    # --- BIS / Pablo Hernández de Cos ---
    {
        "id": 1932,
        "title": "Pablo Hernández de Cos — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Pablo_Hern%C3%A1ndez_de_Cos",
        "source_type": "other",
        "year": 2026,
    },
    # --- Strategic Bitcoin Reserve ---
    {
        "id": 1933,
        "title": "Strategic Bitcoin Reserve — Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Strategic_Bitcoin_Reserve",
        "source_type": "other",
        "year": 2026,
    },
    # --- Jerome Powell 2025-26 ---
    {
        "id": 1934,
        "title": "Jerome Powell — Wikipedia (2025-2026 events)",
        "url": "https://en.wikipedia.org/wiki/Jerome_Powell",
        "source_type": "other",
        "year": 2026,
    },
    # --- Gates Foundation wind-down ---
    {
        "id": 1935,
        "title": "Bill & Melinda Gates Foundation — Wikipedia (2025 wind-down announcement)",
        "url": "https://en.wikipedia.org/wiki/Bill_%26_Melinda_Gates_Foundation",
        "source_type": "other",
        "year": 2026,
    },
    # --- IMF leadership ---
    {
        "id": 1936,
        "title": "IMF Managing Director Kristalina Georgieva Proposes the Appointment of Daniel Katz as FDMD — IMF",
        "url": "https://www.imf.org/en/news/articles/2025/09/18/pr25302-imf-md-kristalina-georgieva-proposes-the-appointment-of-daniel-katz-as-fdmd",
        "source_type": "government",
        "year": 2025,
    },
    # --- Open Society Foundations ---
    {
        "id": 1937,
        "title": "Open Society Foundations — Wikipedia (2025 federal investigation)",
        "url": "https://en.wikipedia.org/wiki/Open_Society_Foundations",
        "source_type": "other",
        "year": 2026,
    },
    # --- Jane Lauder / Warsh family connection ---
    {
        "id": 1938,
        "title": "Jane Lauder — Wikipedia (Warsh-Lauder family connection)",
        "url": "https://en.wikipedia.org/wiki/Jane_Lauder",
        "source_type": "other",
        "year": 2026,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    {
        "name": "Kevin Warsh",
        "entity_type": "person",
        "description": (
            "Kevin Michael Warsh (b. 1970). 17th Chair of the Federal Reserve, "
            "confirmed by the Senate on May 13, 2026 in a 54-45 vote — the narrowest "
            "margin in Fed history. Nominated by President Trump on January 30, 2026 to "
            "succeed Jerome Powell. Former Morgan Stanley executive (1996-2002) "
            "specializing in mergers and acquisitions. Served as special assistant to "
            "President George W. Bush on the National Economic Council (2002-2006), then "
            "as a Federal Reserve Governor (2006-2011), where he served during the 2008 "
            "financial crisis. Married to Jane Lauder, daughter of Ronald Lauder (World "
            "Jewish Congress president, Estee Lauder heir, Mega Group member). This "
            "family connection places Warsh within the Lauder orbit already mapped in "
            "the Mega Group cluster. Sworn in on May 22, 2026 by Justice Clarence Thomas "
            "for a four-year term ending 2030."
        ),
        "aliases": "Kevin M. Warsh",
        "metadata": {
            "nationality": "American",
            "born": "1970-04-13",
            "role": "Chair of the Federal Reserve (May 2026-)",
            "prior_role": "Federal Reserve Governor 2006-2011; Morgan Stanley VP 1996-2002",
        },
    },
    {
        "name": "World Liberty Financial",
        "entity_type": "organization",
        "description": (
            "Crypto venture launched in 2024 by the Trump family and associates "
            "including Zachary Folkman, Chase Herro, and Steve and Zach Witkoff. Donald "
            "Trump holds the title 'chief crypto advocate' while Eric Trump and Donald "
            "Trump Jr. serve as 'Web3 ambassadors.' Trump business entities hold "
            "approximately 60% ownership and receive 75% of token sale revenue. Launched "
            "the USD1 stablecoin (March 2025), backed by U.S. Treasuries and dollars, "
            "reaching $2 billion in circulation by late 2025. Abu Dhabi sovereign wealth "
            "fund MGX invested $2 billion (May 2025), drawing conflict-of-interest "
            "scrutiny given concurrent U.S.-UAE diplomatic negotiations. In August 2026, "
            "the Office of the Comptroller of the Currency granted conditional approval "
            "for World Liberty Trust Company to establish a national trust bank for "
            "stablecoin issuance. Trump reported over $1.4 billion in crypto income for "
            "2025, with WLF and the separate $TRUMP memecoin (launched January 17, 2025, "
            "operated by CIC Digital LLC) comprising the majority. Binance administered "
            "the WLF trading platform, raising concerns after Trump pardoned Binance "
            "founder Changpeng Zhao in October 2025."
        ),
        "aliases": "WLF, World Liberty Trust",
        "metadata": {
            "type": "crypto / stablecoin",
            "founded": 2024,
            "location": "United States",
        },
    },
    {
        "name": "GENIUS Act",
        "entity_type": "legislation",
        "description": (
            "Guiding and Establishing National Innovation for U.S. Stablecoins Act "
            "(Public Law 119-27). Federal legislation establishing the first "
            "comprehensive regulatory framework for payment stablecoins in the United "
            "States. Passed the Senate on June 17, 2025 (68-30) and the House on July "
            "17, 2025 (308-122). Signed into law by President Trump on July 18, 2025. "
            "Sponsored by Senator Bill Hagerty (R-TN). Key provisions require stablecoins "
            "to be backed one-for-one by U.S. dollars or low-risk assets. Issuers are "
            "subject to federal or state regulation depending on size. Compliant "
            "stablecoins are excluded from SEC and CFTC jurisdiction as securities or "
            "commodities but receive no FDIC insurance or direct Federal Reserve access. "
            "Consumer advocates including the New York Attorney General criticized "
            "insufficient fraud protections. The legislation created the regulatory "
            "framework under which Trump's World Liberty Financial operates its USD1 "
            "stablecoin."
        ),
        "aliases": "GENIUS Act of 2025, Stablecoin Act",
        "metadata": {
            "type": "federal legislation",
            "signed": "2025-07-18",
            "public_law": "119-27",
        },
    },
    {
        "name": "Changpeng Zhao",
        "entity_type": "person",
        "description": (
            "Changpeng Zhao (b. 1977). Chinese-Canadian billionaire, founder and former "
            "CEO of Binance, the world's largest cryptocurrency exchange. Pleaded guilty "
            "in November 2023 to violating the Bank Secrecy Act by failing to implement "
            "anti-money laundering controls at Binance, which processed transactions for "
            "sanctioned entities including Hamas, al-Qaeda, and ISIS. Binance paid a "
            "$4.3 billion corporate fine; Zhao personally fined $50 million. Sentenced to "
            "four months in federal prison, served at FCI Lompoc, released September 27, "
            "2024. Granted a full and unconditional presidential pardon by Donald Trump on "
            "October 23, 2025. The White House characterized the original prosecution as "
            "a 'Biden witch hunt.' The Wall Street Journal and CNBC documented that "
            "Binance administered the trading platform for Trump's World Liberty Financial "
            "venture, raising conflict-of-interest concerns about the pardon. Binance "
            "spent $800,000 on lobbying for clemency."
        ),
        "aliases": "CZ",
        "metadata": {
            "nationality": "Chinese-Canadian",
            "born": "1977",
            "role": "Founder, Binance",
            "status": "pardoned",
        },
    },
    {
        "name": "Strategic Bitcoin Reserve",
        "entity_type": "event",
        "description": (
            "Executive order signed by President Donald Trump on March 6, 2025, "
            "establishing the United States Strategic Bitcoin Reserve and a separate U.S. "
            "Digital Asset Stockpile. The reserve is funded by approximately 200,000 BTC "
            "already held by the federal government from criminal forfeitures and "
            "seizures, reported at approximately 328,372 BTC as of February 2026, making "
            "the U.S. the largest known state holder of bitcoin. On March 3, 2025, Trump "
            "announced the reserve would also encompass Solana, Cardano, Ripple, and "
            "Ethereum. Senator Cynthia Lummis introduced companion legislation on March "
            "11 to purchase an additional one million BTC over five years. The executive "
            "order directed Treasury to evaluate legal factors and propose legislation "
            "within 60 days; both deadlines passed without public updates. Part of the "
            "broader Trump administration crypto policy agenda that included the GENIUS "
            "Act, the Changpeng Zhao pardon, and the World Liberty Financial venture."
        ),
        "aliases": "Strategic Bitcoin Reserve EO, US Bitcoin Reserve",
        "metadata": {
            "type": "executive order",
            "signed": "2025-03-06",
        },
    },
    {
        "name": "IEEPA Tariff Ruling (2026)",
        "entity_type": "event",
        "description": (
            "U.S. Supreme Court decision striking down President Trump's use of the "
            "International Emergency Economic Powers Act (IEEPA) to impose tariffs. "
            "Consolidated cases (V.O.S. Selections and Learning Resources) argued "
            "November 5, 2025; decided February 20, 2026. The Court ruled 6-3 that "
            "IEEPA does not authorize presidential tariffs. Majority opinion by Chief "
            "Justice Roberts, joined fully by Justices Gorsuch and Barrett, and in part "
            "by Justices Sotomayor, Kagan, and Jackson. Dissent by Justices Thomas, "
            "Alito, and Kavanaugh. The Court held that tariff power is 'a branch of the "
            "taxing power' reserved to Congress under Article I, and that Congress "
            "deliberately excluded tariff language from IEEPA. Trump issued an executive "
            "order the same day revoking IEEPA tariffs; a replacement 10% global tariff "
            "took effect under Section 122 of the Trade Act of 1974 on February 24, "
            "2026. The ruling on refunds was left to the Court of International Trade."
        ),
        "aliases": "IEEPA Tariff Case, SCOTUS Tariff Decision 2026",
        "metadata": {
            "type": "supreme court ruling",
            "date": "2026-02-20",
            "vote": "6-3",
        },
    },
    {
        "name": "Trump v. Cook (2026)",
        "entity_type": "event",
        "description": (
            "U.S. Supreme Court ruling (docket 25A312) in which the Court prevented "
            "President Trump from firing Federal Reserve Governor Lisa Cook. In August "
            "2025, Trump posted on Truth Social a letter terminating Cook, citing alleged "
            "mortgage fraud on properties in Michigan and Georgia. Cook sued, arguing "
            "removal violated the Federal Reserve Act's for-cause requirement and her "
            "Fifth Amendment rights. District Judge Jia Cobb ordered reinstatement; the "
            "D.C. Circuit upheld the injunction. On June 29, 2026, the Supreme Court "
            "ruled 5-4 that Cook could remain in her position while litigation proceeds. "
            "Majority: Chief Justice Roberts, Justices Sotomayor, Kagan, Kavanaugh, and "
            "Jackson. Dissent: Thomas, Alito, Gorsuch, Barrett. Roberts wrote that 'not "
            "only the fact of independence but also the appearance of independence is key "
            "to the Federal Reserve's design.' The ruling was a preliminary injunction, "
            "not a final decision on the merits. Trump subsequently initiated a formal "
            "for-cause process."
        ),
        "aliases": "Lisa Cook Case, Fed Independence Case",
        "metadata": {
            "type": "supreme court ruling",
            "date": "2026-06-29",
            "vote": "5-4",
            "docket": "25A312",
        },
    },
    {
        "name": "Wyden Epstein-JPMorgan Investigation (2025)",
        "entity_type": "event",
        "description": (
            "Senate Finance Committee investigation led by Ranking Member Ron Wyden into "
            "JPMorgan Chase's role in enabling Jeffrey Epstein's financial operations. "
            "Launched after a September 2025 New York Times Magazine investigation "
            "documented how top JPMorgan executives overrode internal compliance warnings "
            "to maintain Epstein as a client. Key findings in the committee's November "
            "20, 2025 memorandum: the bank filed only $4.3 million in suspicious activity "
            "reports while Epstein was alive, versus approximately $1.3 billion in "
            "retroactive filings after his 2019 death — a 300-fold discrepancy. Named "
            "executives included Mary Erdoes (head of asset and wealth management, "
            "maintained constant contact with Epstein), John Duffy (former Private "
            "Banking CEO, counseled Epstein on executing suspicious cash withdrawals), "
            "and Jamie Dimon (CEO, received direct reports on the Epstein relationship). "
            "The investigation documented $25 million in payments from Epstein's JPMorgan "
            "accounts to Ghislaine Maxwell and $170 million to Epstein from Leon Black."
        ),
        "aliases": "Wyden JPMorgan Investigation, Senate Epstein-JPMorgan Probe",
        "metadata": {
            "type": "congressional investigation",
            "date": "2025-09-25",
        },
    },
    {
        "name": "Pablo Hernández de Cos",
        "entity_type": "person",
        "description": (
            "Spanish economist (b. January 20, 1971, Madrid). General Manager of the "
            "Bank for International Settlements from July 1, 2025, succeeding Agustin "
            "Carstens for a five-year term. Previously served as the 70th Governor of "
            "the Bank of Spain (June 2018 - June 2024) and Chairman of the Basel "
            "Committee on Banking Supervision (March 2019 - 2024), where he oversaw the "
            "finalization of Basel III capital standards. Career Bank of Spain economist "
            "from 1997 with a stint as advisor to the European Central Bank executive "
            "board (2004-2007). As BIS head, Hernandez de Cos oversees the institution "
            "that coordinates central bank policy globally, sets banking supervision "
            "standards, and hosts bimonthly meetings of central bank governors. The BIS "
            "under his tenure has positioned itself as an institutional counterweight to "
            "the proliferation of private stablecoins, advocating central bank digital "
            "currencies."
        ),
        "aliases": "Pablo Hernandez de Cos",
        "metadata": {
            "nationality": "Spanish",
            "born": "1971-01-20",
            "role": "General Manager, Bank for International Settlements (Jul 2025-)",
            "prior_role": "Governor, Bank of Spain 2018-2024",
        },
    },
    {
        "name": "Mary Erdoes",
        "entity_type": "person",
        "description": (
            "Mary Callahan Erdoes (b. 1967). CEO of JPMorgan Chase's Asset and Wealth "
            "Management division since 2009, overseeing over $4 trillion in client "
            "assets. Named in the Senate Finance Committee's November 2025 investigation "
            "as a top JPMorgan executive who maintained 'constant contact' with Jeffrey "
            "Epstein. The committee's memorandum identified Erdoes as one of several "
            "senior executives aware of Epstein's relationship with the bank whose "
            "conduct the investigation sought to explain. Erdoes was not individually "
            "charged with wrongdoing. Graduated from Georgetown University (BA) and "
            "Harvard Business School (MBA). Joined JPMorgan in 1996 as a managing "
            "director in fixed income. The Wyden investigation focused on whether "
            "executives including Erdoes exercised adequate oversight of Epstein's "
            "suspicious financial activity during the years the bank processed $1.1 "
            "billion in suspicious wires."
        ),
        "aliases": "Mary Callahan Erdoes",
        "metadata": {
            "nationality": "American",
            "born": "1967",
            "role": "CEO, JPMorgan Asset & Wealth Management (2009-)",
        },
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Kevin Warsh ---
    {
        "source": "Kevin Warsh",
        "target": "Federal Reserve System",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "17th Chair of the Federal Reserve, confirmed May 13, 2026 in a 54-45 "
            "vote — the narrowest in Fed history. Sworn in May 22, 2026 for a four-year "
            "term. Succeeded Jerome Powell, whose term ended May 15, 2026."
        ),
        "year_start": 2026,
        "year_end": 2030,
        "sources": [1906, 1907, 1908, 1909],
    },
    {
        "source": "Donald Trump",
        "target": "Kevin Warsh",
        "type": "appointed",
        "tier": "documented",
        "desc": (
            "Nominated Warsh as Federal Reserve Chair on January 30, 2026. Senate "
            "confirmed 54-45 on May 13, 2026."
        ),
        "year_start": 2026,
        "sources": [1906, 1908],
    },
    {
        "source": "Kevin Warsh",
        "target": "Ronald Lauder",
        "type": "family_of",
        "tier": "documented",
        "desc": (
            "Son-in-law of Ronald Lauder through marriage to Jane Lauder (2002). Jane "
            "is Ronald's daughter and an Estee Lauder Companies heiress. This places the "
            "Fed Chair within the Lauder-Mega Group orbit already documented in the "
            "console's financial cluster."
        ),
        "sources": [1907, 1938],
    },
    {
        "source": "Kevin Warsh",
        "target": "2008 Financial Crisis",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Served on the Federal Reserve Board of Governors (2006-2011) during the "
            "2008 financial crisis, participating in the emergency lending decisions "
            "that defined the Fed's crisis response."
        ),
        "year_start": 2008,
        "year_end": 2009,
        "sources": [1907],
    },
    # --- World Liberty Financial ---
    {
        "source": "Donald Trump",
        "target": "World Liberty Financial",
        "type": "founder_of",
        "tier": "documented",
        "desc": (
            "Trump entities hold approximately 60% ownership and receive 75% of token "
            "sale revenue. Trump serves as 'chief crypto advocate.' His 2025 financial "
            "disclosure reported over $1.4 billion in crypto income, predominantly from "
            "WLF and the $TRUMP memecoin."
        ),
        "year_start": 2024,
        "sources": [1919, 1920, 1921],
    },
    {
        "source": "World Liberty Financial",
        "target": "GENIUS Act",
        "type": "regulated_by",
        "tier": "documented",
        "desc": (
            "The GENIUS Act (signed July 2025) created the regulatory framework under "
            "which World Liberty Financial operates its USD1 stablecoin. The OCC's "
            "August 2026 conditional bank charter approval for WLF Trust Company applied "
            "this framework."
        ),
        "year_start": 2025,
        "sources": [1916, 1917, 1920],
    },
    {
        "source": "Changpeng Zhao",
        "target": "World Liberty Financial",
        "type": "business_partner",
        "tier": "credible",
        "desc": (
            "Binance, founded by Zhao, administered the trading platform for World "
            "Liberty Financial. The Wall Street Journal reported the partnership was "
            "established by August 2025, creating a financial connection between the "
            "pardoned Binance founder and the presidential crypto venture."
        ),
        "year_start": 2025,
        "sources": [1924, 1925, 1929],
    },
    {
        "source": "World Liberty Financial",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "WLF's August 2026 OCC conditional bank charter for stablecoin issuance "
            "creates a presidential-family-owned entity operating within the U.S. "
            "banking system alongside the Federal Reserve's traditional monetary "
            "architecture."
        ),
        "year_start": 2026,
        "sources": [1920, 1923],
    },
    # --- GENIUS Act ---
    {
        "source": "Donald Trump",
        "target": "GENIUS Act",
        "type": "signed_into_law",
        "tier": "documented",
        "desc": (
            "Signed the GENIUS Act into law on July 18, 2025. The legislation passed "
            "the Senate 68-30 on June 17 and the House 308-122 on July 17, 2025."
        ),
        "year_start": 2025,
        "sources": [1916, 1917],
    },
    {
        "source": "GENIUS Act",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The stablecoin regulatory framework interacts with the Federal Reserve's "
            "monetary architecture: stablecoin issuers must hold reserves in U.S. "
            "dollars or equivalent, but stablecoins receive no FDIC insurance or direct "
            "Fed access, creating a parallel payment system."
        ),
        "year_start": 2025,
        "sources": [1916, 1918],
    },
    # --- Changpeng Zhao ---
    {
        "source": "Donald Trump",
        "target": "Changpeng Zhao",
        "type": "pardoned",
        "tier": "documented",
        "desc": (
            "Full and unconditional presidential pardon issued October 23, 2025. Zhao "
            "had pleaded guilty in November 2023 to Bank Secrecy Act violations at "
            "Binance ($4.3 billion corporate fine). The pardon came after reporting "
            "that Binance administered the Trump family's WLF trading platform."
        ),
        "year_start": 2025,
        "sources": [1924, 1925, 1926, 1928],
    },
    {
        "source": "Changpeng Zhao",
        "target": "DOJ",
        "type": "investigated_by",
        "tier": "documented",
        "desc": (
            "Prosecuted by the DOJ for violating the Bank Secrecy Act. Pleaded guilty "
            "November 2023. Binance fined $4.3 billion; Zhao personally fined $50 "
            "million and sentenced to four months in federal prison. Served sentence at "
            "FCI Lompoc, released September 27, 2024. Pardoned October 2025."
        ),
        "year_start": 2023,
        "year_end": 2025,
        "sources": [1927, 1928],
    },
    # --- Strategic Bitcoin Reserve ---
    {
        "source": "Donald Trump",
        "target": "Strategic Bitcoin Reserve",
        "type": "signed_into_law",
        "tier": "documented",
        "desc": (
            "Signed executive order on March 6, 2025 establishing the U.S. Strategic "
            "Bitcoin Reserve using approximately 200,000 BTC from federal criminal "
            "forfeitures."
        ),
        "year_start": 2025,
        "sources": [1933],
    },
    {
        "source": "Strategic Bitcoin Reserve",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "inference",
        "desc": (
            "The establishment of a federal bitcoin reserve, making the U.S. the "
            "largest known state holder of bitcoin, creates an alternative reserve "
            "asset framework alongside the Federal Reserve's traditional dollar-based "
            "monetary system. Inference based on structural positioning."
        ),
        "year_start": 2025,
        "sources": [1933],
    },
    {
        "source": "Strategic Bitcoin Reserve",
        "target": "World Liberty Financial",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Both the Strategic Bitcoin Reserve EO (March 2025) and World Liberty "
            "Financial are elements of the Trump administration's crypto policy agenda. "
            "The reserve announcement on March 3 specifically named multiple "
            "cryptocurrencies, boosting the broader ecosystem in which WLF operates."
        ),
        "year_start": 2025,
        "sources": [1933, 1919],
    },
    {
        "source": "Strategic Bitcoin Reserve",
        "target": "DOJ",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The Strategic Bitcoin Reserve is funded by BTC already held by the federal "
            "government from DOJ criminal forfeitures and seizures, reported at "
            "approximately 328,372 BTC as of February 2026."
        ),
        "year_start": 2025,
        "sources": [1933],
    },
    # --- IEEPA Tariff Ruling ---
    {
        "source": "IEEPA Tariff Ruling (2026)",
        "target": "Donald Trump",
        "type": "target_of",
        "tier": "documented",
        "desc": (
            "The Supreme Court struck down Trump's use of IEEPA to impose tariffs in a "
            "6-3 ruling on February 20, 2026, holding that IEEPA does not authorize "
            "presidential tariffs. Trump issued an executive order the same day revoking "
            "the tariffs."
        ),
        "year_start": 2026,
        "sources": [1930, 1931],
    },
    {
        "source": "IEEPA Tariff Ruling (2026)",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "The ruling reshaped U.S. economic policy by invalidating the tariff "
            "regime that had significantly affected trade, inflation, and Federal "
            "Reserve interest rate calculations throughout 2025."
        ),
        "year_start": 2026,
        "sources": [1930],
    },
    {
        "source": "IEEPA Tariff Ruling (2026)",
        "target": "Trump v. Cook (2026)",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Twin Supreme Court cases from the 2025-2026 term both addressing the "
            "limits of presidential economic power: IEEPA tariffs (Feb 2026, 6-3 "
            "against Trump) and Fed independence (Jun 2026, 5-4 for Cook). Together "
            "they defined the judicial boundary on executive authority over the "
            "financial system."
        ),
        "year_start": 2026,
        "sources": [1930, 1910],
    },
    # --- Trump v. Cook ---
    {
        "source": "Trump v. Cook (2026)",
        "target": "Donald Trump",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Trump attempted to fire Fed Governor Lisa Cook in August 2025 — the first "
            "such removal in the Fed's 111-year history. The Supreme Court ruled 5-4 on "
            "June 29, 2026 that Cook could remain while litigation proceeds."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1910, 1911, 1912, 1913],
    },
    {
        "source": "Trump v. Cook (2026)",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The case tested the constitutional independence of the Federal Reserve. "
            "Chief Justice Roberts wrote that 'not only the fact of independence but "
            "also the appearance of independence is key to the Federal Reserve's "
            "design.' The ruling upheld for-cause removal protections for Fed governors."
        ),
        "year_start": 2026,
        "sources": [1910, 1912, 1913],
    },
    # --- Wyden Investigation ---
    {
        "source": "Wyden Epstein-JPMorgan Investigation (2025)",
        "target": "JPMorgan Chase",
        "type": "investigated",
        "tier": "documented",
        "desc": (
            "Senate Finance Committee investigation documented severe compliance "
            "failures: $4.3 million in SARs filed while Epstein was alive versus $1.3 "
            "billion retroactively after his 2019 death. Named top executives who "
            "overrode internal compliance warnings."
        ),
        "year_start": 2025,
        "sources": [1900, 1901, 1902, 1903],
    },
    {
        "source": "Wyden Epstein-JPMorgan Investigation (2025)",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The investigation centered on how JPMorgan's institutional failures "
            "enabled Epstein's financial operations over nearly two decades, documenting "
            "4,725 suspicious wires totaling $1.1 billion."
        ),
        "year_start": 2025,
        "sources": [1900, 1902, 1903],
    },
    {
        "source": "Jes Staley",
        "target": "Wyden Epstein-JPMorgan Investigation (2025)",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "Staley identified in the investigation as a key executive whose personal "
            "relationship with Epstein was central to JPMorgan's failure to flag "
            "suspicious activity. His 1,200+ emails with Epstein were part of the "
            "evidentiary record."
        ),
        "year_start": 2025,
        "sources": [1900, 1902],
    },
    {
        "source": "Mary Erdoes",
        "target": "Wyden Epstein-JPMorgan Investigation (2025)",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "Named in the Senate Finance Committee memorandum as a top JPMorgan "
            "executive who maintained 'constant contact' with Epstein. The investigation "
            "examined whether Erdoes and other executives exercised adequate oversight."
        ),
        "year_start": 2025,
        "sources": [1902, 1903],
    },
    {
        "source": "Leon Black",
        "target": "Wyden Epstein-JPMorgan Investigation (2025)",
        "type": "subject_of",
        "tier": "documented",
        "desc": (
            "The investigation documented that approximately $170 million in payments "
            "from Leon Black to Epstein were processed through JPMorgan accounts, "
            "exceeding earlier public reporting of $158 million."
        ),
        "year_start": 2025,
        "sources": [1902, 1903],
    },
    {
        "source": "Wyden Epstein-JPMorgan Investigation (2025)",
        "target": "Ghislaine Maxwell",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The investigation documented $25 million or more in payments from "
            "Epstein's JPMorgan accounts to Ghislaine Maxwell, including a $19 million "
            "one-time payment."
        ),
        "year_start": 2025,
        "sources": [1902, 1903],
    },
    {
        "source": "Wyden Epstein-JPMorgan Investigation (2025)",
        "target": "DOJ",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The investigation referenced Treasury Department documents and the DOJ "
            "Epstein Library materials in its analysis of JPMorgan's compliance "
            "failures."
        ),
        "year_start": 2025,
        "sources": [1901, 1902],
    },
    {
        "source": "Wyden Epstein-JPMorgan Investigation (2025)",
        "target": "Wexner House Oversight Deposition (2026)",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "Parallel congressional investigations into the Epstein financial network: "
            "the Senate Finance Committee's JPMorgan probe (2025) and the House "
            "Oversight Committee's Wexner deposition (February 2026) both examined how "
            "financial institutions and wealthy associates enabled Epstein."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1901, 1902],
    },
    # --- Mary Erdoes standalone edges ---
    {
        "source": "Mary Erdoes",
        "target": "JPMorgan Chase",
        "type": "employed_by",
        "tier": "documented",
        "desc": (
            "CEO of JPMorgan's Asset and Wealth Management division since 2009, "
            "overseeing over $4 trillion in client assets. Joined the bank in 1996."
        ),
        "year_start": 1996,
        "sources": [1902],
    },
    {
        "source": "Mary Erdoes",
        "target": "Jeffrey Epstein",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "The Senate Finance Committee's November 2025 memorandum documented that "
            "Erdoes, as a top JPMorgan executive, maintained 'constant contact' with "
            "Jeffrey Epstein. The nature and extent of this contact was a focus of the "
            "investigation."
        ),
        "sources": [1902, 1903],
    },
    # --- JPMorgan / Maxwell / Leon Black cross-links ---
    {
        "source": "JPMorgan Chase",
        "target": "Ghislaine Maxwell",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Senate Finance Committee documented $25 million or more in payments from "
            "Epstein's JPMorgan accounts to Ghislaine Maxwell, including a single $19 "
            "million transfer. The bank's compliance systems failed to flag these "
            "payments."
        ),
        "sources": [1902, 1903],
    },
    {
        "source": "Leon Black",
        "target": "JPMorgan Chase",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "Senate Finance Committee documented approximately $170 million in payments "
            "from Leon Black to Epstein processed through JPMorgan accounts, exceeding "
            "earlier public reporting of $158 million."
        ),
        "sources": [1902, 1903],
    },
    # --- Pablo Hernández de Cos ---
    {
        "source": "Pablo Hernández de Cos",
        "target": "Bank for International Settlements",
        "type": "director_of",
        "tier": "documented",
        "desc": (
            "General Manager of the BIS from July 1, 2025, succeeding Agustin Carstens "
            "for a five-year term. Previously Governor of the Bank of Spain (2018-2024) "
            "and Chairman of the Basel Committee on Banking Supervision (2019-2024)."
        ),
        "year_start": 2025,
        "year_end": 2030,
        "sources": [1932],
    },
    {
        "source": "Pablo Hernández de Cos",
        "target": "International Monetary Fund",
        "type": "connected_to",
        "tier": "credible",
        "desc": (
            "As BIS General Manager, coordinates with the IMF on global financial "
            "stability policy. The BIS and IMF jointly publish reports on systemic risk "
            "and have aligned on concerns about stablecoin proliferation threatening "
            "monetary sovereignty."
        ),
        "year_start": 2025,
        "sources": [1932],
    },
    # --- Donald Trump / Federal Reserve System ---
    {
        "source": "Donald Trump",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "documented",
        "desc": (
            "2025-2026 conflict with Fed independence: attempted to fire Governor Lisa "
            "Cook (August 2025), DOJ issued grand jury subpoenas to Chair Powell "
            "(January 2026, later quashed), nominated Warsh as Powell's replacement. "
            "Trump posted 'Powell's termination cannot come fast enough' (April 2025)."
        ),
        "year_start": 2025,
        "year_end": 2026,
        "sources": [1910, 1934, 1906],
    },
]

# ============================================================
# ENTITY → SOURCE mappings
# ============================================================

ENTITY_SOURCES = {
    "Kevin Warsh": [1906, 1907, 1908, 1909, 1938],
    "World Liberty Financial": [1919, 1920, 1921, 1922, 1923],
    "GENIUS Act": [1916, 1917, 1918],
    "Changpeng Zhao": [1924, 1925, 1926, 1927, 1928, 1929],
    "Strategic Bitcoin Reserve": [1933],
    "IEEPA Tariff Ruling (2026)": [1930, 1931],
    "Trump v. Cook (2026)": [1910, 1911, 1912, 1913],
    "Wyden Epstein-JPMorgan Investigation (2025)": [1900, 1901, 1902, 1903],
    "Pablo Hernández de Cos": [1932],
    "Mary Erdoes": [1902, 1903],
}

# ============================================================
# ENTITY UPDATES — modifies EXISTING entities
# ============================================================

ENTITY_UPDATES = [
    {
        "name": "JPMorgan Chase",
        "description_append": (
            "2025-2026 update: A September 2025 New York Times Magazine investigation "
            "revealed how top JPMorgan executives overrode internal compliance warnings "
            "to maintain Epstein as a client. Senate Finance Committee Ranking Member "
            "Ron Wyden launched an investigation, releasing a detailed memorandum on "
            "November 20, 2025 documenting severe underreporting: the bank filed only "
            "$4.3 million in suspicious activity reports while Epstein was alive, versus "
            "approximately $1.3 billion in retroactive filings after his 2019 death. "
            "The investigation named Mary Erdoes (head of asset and wealth management), "
            "John Duffy (former Private Banking CEO), and Jamie Dimon as executives who "
            "had direct knowledge of the Epstein relationship. The committee documented "
            "$25 million in payments from Epstein's accounts to Ghislaine Maxwell and "
            "$170 million in payments to Epstein from Leon Black processed through "
            "JPMorgan."
        ),
        "sources": [1900, 1901, 1902, 1903],
    },
    {
        "name": "Jes Staley",
        "description_append": (
            "2025 update: On June 26, 2025, the UK Upper Tribunal upheld the FCA's "
            "decision to ban Staley from holding senior management roles in financial "
            "services. The FCA issued a Final Notice on July 23, 2025. The Tribunal "
            "reduced the proposed fine from 1.8 million pounds to 1.1 million pounds "
            "after Barclays declined to pay deferred shares to which Staley had been "
            "entitled. The ban was based on Staley's approval of a letter to the FCA "
            "containing misleading statements about his relationship with Epstein, "
            "specifically claiming he did not have a close relationship when documented "
            "emails showed Staley described Epstein as one of his 'deepest' and 'most "
            "cherished' friends. This represents the final regulatory outcome."
        ),
        "sources": [1904, 1905],
    },
    {
        "name": "Federal Reserve System",
        "description_append": (
            "2025-2026 update: President Trump nominated Kevin Warsh as Fed Chair on "
            "January 30, 2026; the Senate confirmed Warsh 54-45 on May 13, 2026 — the "
            "narrowest confirmation in Fed history. Jerome Powell served as chair pro "
            "tempore until Warsh's swearing-in on May 22, 2026. In August 2025, Trump "
            "attempted to fire Fed Governor Lisa Cook — the first such removal in the "
            "Fed's 111-year history. The Supreme Court ruled 5-4 on June 29, 2026 (Trump "
            "v. Cook, 25A312) that Cook could remain, with Chief Justice Roberts writing "
            "that 'the appearance of independence is key to the Federal Reserve's "
            "design.' Stephen Miran served as CEA Chairman (March 2025) before "
            "appointment to the Fed Board (confirmed 48-47, September 15, 2025) "
            "replacing departing Governor Adriana Kugler. In January 2026, the DOJ "
            "issued grand jury subpoenas to Powell regarding congressional testimony; "
            "a federal judge quashed the subpoenas in March 2026, finding them designed "
            "to 'harass and pressure.'"
        ),
        "sources": [1906, 1907, 1910, 1912, 1914, 1915, 1934],
    },
    {
        "name": "Bank for International Settlements",
        "description_append": (
            "2025 update: Pablo Hernandez de Cos assumed office as General Manager on "
            "July 1, 2025, succeeding Agustin Carstens for a five-year term. The "
            "former Bank of Spain Governor (2018-2024) and Basel Committee Chairman "
            "(2019-2024) took the helm as the BIS positioned itself as an institutional "
            "counterweight to the proliferation of private stablecoins, publishing "
            "reports warning of risks to monetary sovereignty and financial stability "
            "and advocating central bank digital currencies."
        ),
        "sources": [1932],
    },
    {
        "name": "Bill & Melinda Gates Foundation",
        "description_append": (
            "2025 update: In May 2025, Bill Gates announced the foundation will cease "
            "all operations by December 31, 2045, setting a fixed end date rather than "
            "tying closure to the founders' lifespans. The announcement superseded "
            "earlier plans to spend down the endowment within 20 years of the last "
            "surviving founder's death. The foundation continues to spend approximately "
            "$9 billion annually across global health, education, and development."
        ),
        "sources": [1935],
    },
    {
        "name": "Leon Black",
        "description_append": (
            "2025 update: The Senate Finance Committee's November 2025 investigation "
            "into JPMorgan Chase and Epstein documented that Leon Black paid "
            "approximately $170 million to Epstein over several years through JPMorgan "
            "accounts. This figure, documented through Treasury records reviewed by "
            "committee investigators, exceeds earlier public reporting of the $158 "
            "million that prompted Black's resignation from Apollo's chairmanship in "
            "2021."
        ),
        "sources": [1902, 1903],
    },
    {
        "name": "International Monetary Fund",
        "description_append": (
            "2025 update: Managing Director Kristalina Georgieva, reappointed for a "
            "second five-year term beginning October 2024, proposed Daniel Katz — Chief "
            "of Staff to U.S. Treasury Secretary Scott Bessent — as First Deputy "
            "Managing Director, effective October 6, 2025. The appointment placed a "
            "Trump administration ally in the IMF's second-highest position, continuing "
            "the longstanding pattern of U.S. influence over international financial "
            "institutions."
        ),
        "sources": [1936],
    },
    {
        "name": "Open Society Foundations",
        "description_append": (
            "2025 update: Alexander Soros serves as chairman following the 2023 "
            "leadership transition, with Binaifer Nowrojee as president from June 2024. "
            "The foundation underwent a 40% reduction in international staff following "
            "the transition. Under President Trump's second term, federal prosecutors "
            "received directives to investigate OSF for potential charges including "
            "racketeering, wire fraud, and material support for terrorism, based on "
            "claims the foundation 'poured over $80 million into groups tied to "
            "terrorism or extremist violence.' OSF called the investigation a "
            "'politically motivated attack' and denied funding terrorism. Assets "
            "reported at $23 billion."
        ),
        "sources": [1937],
    },
    {
        "name": "Deutsche Bank",
        "description_append": (
            "2025-2026 update: CEO Christian Sewing's contract was extended through "
            "April 2029 (March 2025). New leadership appointments included Marcus "
            "Chromik as Chief Risk Officer (May 2025) and Raja Akram as Chief Financial "
            "Officer (March 2026). Revenue rose to 32.1 billion euros with net income "
            "of 6.1 billion euros in 2025. No new Epstein-related regulatory actions or "
            "Trump loan litigation developments were publicly documented in this period."
        ),
        "sources": [1907],
    },
    {
        "name": "Apollo Global Management",
        "description_append": (
            "2025-2026 update: Marc Rowan remains as Chairman and CEO following Leon "
            "Black's 2021 departure; Black holds no executive role. In 2026, the DOJ "
            "began publishing a searchable Epstein files repository in which names of "
            "current Apollo leadership (Rowan and COO Scott Kleinman) appeared, though "
            "the DOJ noted that 'the presence of names in the repository does not by "
            "itself establish the nature or context of any interaction.' Senate Finance "
            "Committee Ranking Member Wyden indicated in late 2025 that his Epstein "
            "follow-the-money investigation would continue."
        ),
        "sources": [1902],
    },
    {
        "name": "BlackRock",
        "description_append": (
            "2026 update: CEO Larry Fink served as WEF co-chair alongside Andre "
            "Hoffmann when WEF President Borge Brende resigned on February 26, 2026 "
            "over Epstein file revelations. Fink and Hoffmann oversaw the completion "
            "of an independent investigation by outside counsel. BlackRock's AUM "
            "continued past $10 trillion."
        ),
        "sources": [444, 448],
    },
]

# ============================================================
# GEO_COORDS — for NEW entities only
# ============================================================

GEO_COORDS = {
    "Kevin Warsh": (38.8927, -77.0462, "credible", "Federal Reserve Board, Washington DC"),
    "World Liberty Financial": (40.7128, -74.0060, "inference", "New York City, corporate base"),
    "GENIUS Act": (38.8899, -77.0091, "credible", "US Capitol, Washington DC"),
    "Changpeng Zhao": (25.2048, 55.2708, "credible", "Dubai, UAE — primary residence post-release"),
    "Strategic Bitcoin Reserve": (38.8977, -77.0365, "credible", "White House, Washington DC"),
    "IEEPA Tariff Ruling (2026)": (38.8907, -77.0044, "documented", "US Supreme Court, Washington DC"),
    "Trump v. Cook (2026)": (38.8907, -77.0044, "documented", "US Supreme Court, Washington DC"),
    "Wyden Epstein-JPMorgan Investigation (2025)": (38.8846, -77.0122, "credible", "US Senate, Washington DC"),
    "Pablo Hernández de Cos": (47.5543, 7.5917, "credible", "BIS headquarters, Basel, Switzerland"),
    "Mary Erdoes": (40.7580, -73.9720, "credible", "JPMorgan Chase headquarters, New York"),
}

# ============================================================
# PHOTO_CANDIDATES — for NEW persons/orgs
# ============================================================

PHOTO_CANDIDATES = {
    "Kevin Warsh": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Official_portrait_of_Kevin_M._Warsh_%28cropped%292.jpg",
    "Changpeng Zhao": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Changpeng_Zhao_in_2022.jpg",
    "Pablo Hernández de Cos": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Pablo_Hernandez_de_Cos_-_official_portrait_2025.jpg",
    "Mary Erdoes": "https://upload.wikimedia.org/wikipedia/commons/7/74/Mary_Callahan_Erdoes.jpg",
}
