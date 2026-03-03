"""
Financial System Deep — Central Banking, Derivatives, Market Manipulation.

Expansion layer for Intel Console. Maps the structural architecture of the
global financial system: the central banking hierarchy (BIS → Fed → national
banks), the asset management oligopoly (BlackRock/Vanguard/State Street),
the revolving door between Wall Street and Treasury, and the key crises and
scandals that reveal how the system actually operates.

This is NOT the Epstein financial cluster (that's expansion_financial.py).
This maps the system itself: who controls monetary policy, who owns the
corporations, who bailed out whom in 2008, who rigged LIBOR, who killed
Glass-Steagall, and how the petrodollar system was established.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Jeffrey Epstein [1], Les Wexner [4], Mega Group [66],
  JPMorgan Chase [56], Deutsche Bank [57], BCCI [54],
  Federal Reserve System [489], Alan Greenspan [250],
  Henry Kissinger [111], CIA [85], NSA [86], DOJ [89],
  J.P. Morgan [481], John D. Rockefeller [480], Paul Warburg [485],
  David Rockefeller [430], Bill Clinton [32]

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 901-930
# ============================================================

SOURCES = [
    # --- FCIC (Financial Crisis Inquiry Commission) ---
    {
        "id": 901,
        "title": "Financial Crisis Inquiry Commission — Final Report (Jan 2011, congressionally mandated investigation of 2008 crisis)",
        "url": "https://www.govinfo.gov/content/pkg/GPO-FCIC/pdf/GPO-FCIC.pdf",
        "source_type": "congressional",
        "year": 2011,
    },
    # --- Senate Investigations ---
    {
        "id": 902,
        "title": "U.S. Senate Permanent Subcommittee on Investigations — Wall Street and the Financial Crisis: Anatomy of a Financial Collapse (Carl Levin, April 2011)",
        "url": "https://www.hsgac.senate.gov/subcommittees/investigations/media/senate-investigations-subcommittee-releases-levin-coburn-report-on-the-financial-crisis",
        "source_type": "congressional",
        "year": 2011,
    },
    {
        "id": 903,
        "title": "U.S. Senate Banking Committee — Gramm-Leach-Bliley Act (Financial Services Modernization Act of 1999, repealed Glass-Steagall)",
        "url": "https://www.congress.gov/bill/106th-congress/senate-bill/900",
        "source_type": "congressional",
        "year": 1999,
    },
    # --- GAO / Government Accountability Office ---
    {
        "id": 904,
        "title": "GAO — Federal Reserve Bank Governance: Opportunities Exist to Broaden Director Recruitment Efforts and Improve Transparency (GAO-12-18, Oct 2011)",
        "url": "https://www.gao.gov/products/gao-12-18",
        "source_type": "government",
        "year": 2011,
    },
    {
        "id": 905,
        "title": "GAO — Federal Reserve System: Opportunities Exist to Strengthen Policies and Processes for Managing Emergency Lending (GAO-11-696, July 2011)",
        "url": "https://www.gao.gov/products/gao-11-696",
        "source_type": "government",
        "year": 2011,
    },
    # --- TARP / Bailout ---
    {
        "id": 906,
        "title": "SIGTARP — Quarterly Report to Congress (Special Inspector General for the Troubled Asset Relief Program)",
        "url": "https://www.sigtarp.gov/",
        "source_type": "government",
        "year": 2009,
    },
    {
        "id": 907,
        "title": "Emergency Economic Stabilization Act of 2008 (TARP authorization, Public Law 110-343)",
        "url": "https://www.congress.gov/bill/110th-congress/house-bill/1424",
        "source_type": "congressional",
        "year": 2008,
    },
    # --- LIBOR ---
    {
        "id": 908,
        "title": "DOJ — Barclays Bank PLC Admits Misconduct Related to LIBOR and EURIBOR (June 2012, $453M settlement)",
        "url": "https://www.justice.gov/opa/pr/barclays-bank-plc-admits-misconduct-related-submissions-london-interbank-offered-rate-and",
        "source_type": "court",
        "year": 2012,
    },
    {
        "id": 909,
        "title": "U.S. Senate Banking Committee — LIBOR: What Happened, What's Next? (Hearing, July 2012)",
        "url": "https://www.banking.senate.gov/hearings/taking-stock-of-the-libor-scandal",
        "source_type": "congressional",
        "year": 2012,
    },
    # --- BIS ---
    {
        "id": 910,
        "title": "Adam LeBor — Tower of Basel: The Shadowy History of the Secret Bank That Runs the World",
        "url": "https://en.wikipedia.org/wiki/Tower_of_Basel",
        "source_type": "journalism",
        "author": "Adam LeBor",
        "year": 2013,
    },
    {
        "id": 911,
        "title": "BIS — Annual Report (Bank for International Settlements, est. 1930)",
        "url": "https://www.bis.org/publ/arpdf/ar2024e.htm",
        "source_type": "other",
        "year": 2024,
    },
    # --- BlackRock / Asset Management ---
    {
        "id": 912,
        "title": "Fichtner, Heemskerk, Garcia-Bernardo — Hidden Power of the Big Three? Passive Index Funds, Re-concentration of Corporate Ownership, and New Financial Risk (Business and Politics, Vol. 19, No. 2)",
        "url": "https://doi.org/10.1017/bap.2017.6",
        "source_type": "academic",
        "author": "Jan Fichtner, Eelke M. Heemskerk, Javier Garcia-Bernardo",
        "year": 2017,
    },
    {
        "id": 913,
        "title": "U.S. Senate Budget Committee — BlackRock, Vanguard, and State Street: Index Fund Giants and the Concentration of Corporate Ownership (Hearing, Dec 2022)",
        "url": "https://www.budget.senate.gov/chairman/newsroom/press/chairman-sanders-to-hold-hearing-on-corporate-greed-and-consolidation",
        "source_type": "congressional",
        "year": 2022,
    },
    # --- Petrodollar ---
    {
        "id": 914,
        "title": "Bloomberg — The Untold Story Behind Saudi Arabia's 41-Year U.S. Debt Secret (May 2016, declassified Treasury data)",
        "url": "https://www.bloomberg.com/news/features/2016-05-30/the-untold-story-behind-saudi-arabia-s-41-year-u-s-debt-secret",
        "source_type": "journalism",
        "year": 2016,
    },
    {
        "id": 915,
        "title": "David E. Spiro — The Hidden Hand of American Hegemony: Petrodollar Recycling and International Markets",
        "url": "https://en.wikipedia.org/wiki/Petrodollar_recycling",
        "source_type": "academic",
        "author": "David E. Spiro",
        "year": 1999,
    },
    # --- Investigative Journalism ---
    {
        "id": 916,
        "title": "Matt Taibbi — The Great American Bubble Machine (Rolling Stone, Goldman Sachs exposé)",
        "url": "https://www.rollingstone.com/politics/politics-news/the-great-american-bubble-machine-195229/",
        "source_type": "journalism",
        "author": "Matt Taibbi",
        "year": 2009,
    },
    {
        "id": 917,
        "title": "Nomi Prins — All the Presidents' Bankers: The Hidden Alliances That Drive American Power",
        "url": "https://en.wikipedia.org/wiki/Nomi_Prins",
        "source_type": "journalism",
        "author": "Nomi Prins",
        "year": 2014,
    },
    {
        "id": 918,
        "title": "Nomi Prins — Collusion: How Central Bankers Rigged the World",
        "url": "https://www.nomiprins.com/books",
        "source_type": "journalism",
        "author": "Nomi Prins",
        "year": 2018,
    },
    # --- Glass-Steagall ---
    {
        "id": 919,
        "title": "PBS Frontline — The Long Demise of Glass-Steagall (timeline of lobbying and repeal)",
        "url": "https://www.pbs.org/wgbh/pages/frontline/shows/wallstreet/weill/demise.html",
        "source_type": "journalism",
        "year": 2003,
    },
    # --- Revolving Door / Rubin ---
    {
        "id": 920,
        "title": "Robert Kuttner — Other People's Money: The Decline of the American Banking System (on deregulation and the Rubin doctrine)",
        "url": "https://en.wikipedia.org/wiki/Robert_Kuttner",
        "source_type": "journalism",
        "author": "Robert Kuttner",
        "year": 2007,
    },
    # --- SWIFT ---
    {
        "id": 921,
        "title": "New York Times — Bank Data Secretly Reviewed by U.S. to Fight Terror (Terrorist Finance Tracking Program / SWIFT surveillance, June 2006)",
        "url": "https://www.nytimes.com/2006/06/23/washington/23intel.html",
        "source_type": "journalism",
        "year": 2006,
    },
    {
        "id": 922,
        "title": "European Parliament — Resolution on US Surveillance of SWIFT Financial Data (July 2006, condemning secret access)",
        "url": "https://www.europarl.europa.eu/doceo/document/TA-6-2006-0317_EN.html",
        "source_type": "government",
        "year": 2006,
    },
    # --- Exchange Stabilization Fund ---
    {
        "id": 923,
        "title": "U.S. Treasury — Exchange Stabilization Fund (ESF) — authorized under Gold Reserve Act of 1934, operates without congressional oversight",
        "url": "https://home.treasury.gov/policy-issues/international/exchange-stabilization-fund",
        "source_type": "government",
        "year": 2024,
    },
    # --- Plunge Protection Team ---
    {
        "id": 924,
        "title": "Executive Order 12631 — Working Group on Financial Markets (March 18, 1988, created by Reagan after 1987 crash)",
        "url": "https://www.archives.gov/federal-register/codification/executive-order/12631.html",
        "source_type": "government",
        "year": 1988,
    },
    {
        "id": 925,
        "title": "Washington Post — Plunge Protection Team (Brett D. Fromson, Feb 1997, first public reporting on Working Group operations)",
        "url": "https://www.washingtonpost.com/archive/business/1997/02/23/the-plunge-protection-team/",
        "source_type": "journalism",
        "year": 1997,
    },
    # --- IMF / World Bank ---
    {
        "id": 926,
        "title": "Joseph Stiglitz — Globalization and Its Discontents (former World Bank chief economist critique of IMF/World Bank structural adjustment)",
        "url": "https://en.wikipedia.org/wiki/Globalization_and_Its_Discontents",
        "source_type": "academic",
        "author": "Joseph Stiglitz",
        "year": 2002,
    },
    {
        "id": 927,
        "title": "John Perkins — Confessions of an Economic Hit Man (on IMF/World Bank debt trap strategies in developing nations)",
        "url": "https://en.wikipedia.org/wiki/Confessions_of_an_Economic_Hit_Man",
        "source_type": "journalism",
        "author": "John Perkins",
        "year": 2004,
    },
    # --- Geithner / NY Fed ---
    {
        "id": 928,
        "title": "Neil Barofsky — Bailout: An Inside Account of How Washington Abandoned Main Street While Rescuing Wall Street (SIGTARP inspector general memoir)",
        "url": "https://en.wikipedia.org/wiki/Neil_Barofsky",
        "source_type": "journalism",
        "author": "Neil Barofsky",
        "year": 2012,
    },
    # --- Fed Emergency Lending ---
    {
        "id": 929,
        "title": "Bloomberg — Secret Fed Loans Gave Banks $13 Billion Undisclosed to Congress (Nov 2011, FOIA-obtained data on emergency lending)",
        "url": "https://www.bloomberg.com/news/articles/2011-11-28/secret-fed-loans-undisclosed-to-congress-gave-banks-13-billion-in-income",
        "source_type": "journalism",
        "year": 2011,
    },
    # --- BlackRock and Government ---
    {
        "id": 930,
        "title": "Federal Reserve — BlackRock Financial Markets Advisory engaged by NY Fed to manage Bear Stearns and AIG asset portfolios (2008-2009)",
        "url": "https://www.newyorkfed.org/markets/maidenlane.html",
        "source_type": "government",
        "year": 2008,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- Organizations ---
    {
        "name": "Bank for International Settlements",
        "entity_type": "organization",
        "description": (
            "Central bank of central banks, headquartered in Basel, Switzerland. "
            "Founded in 1930 ostensibly to manage WWI reparations, but quickly became "
            "the coordination hub for central banks worldwide. 63 member central banks. "
            "Operates above national sovereignty — its officials have diplomatic immunity, "
            "its assets cannot be seized, and it is not subject to any national jurisdiction. "
            "\n\n"
            "NAZI GOLD CONTROVERSY: Continued operations during WWII, facilitating gold "
            "transfers from the Reichsbank (including looted gold). Its president, Thomas "
            "McKittrick, was an American who maintained relations with both Allied and Axis "
            "central bankers throughout the war. Bretton Woods delegates voted to dissolve "
            "the BIS (1944) but the resolution was never implemented — the BIS survived "
            "and expanded. "
            "\n\n"
            "CURRENT ROLE: Hosts the Basel Committee on Banking Supervision (sets global "
            "capital requirements), the Financial Stability Board, and bimonthly meetings "
            "of central bank governors. Sets the rules that national central banks follow. "
            "No democratic accountability to any electorate."
        ),
        "aliases": "BIS, Basel",
        "metadata": {"type": "central bank coordinating body", "founded": 1930, "hq": "Basel, Switzerland"},
    },
    {
        "name": "BlackRock",
        "entity_type": "organization",
        "description": (
            "World's largest asset manager — over $10 trillion in assets under management "
            "(2024). Founded by Larry Fink in 1988 (originally within Blackstone Group, "
            "spun off 1994). Aladdin risk management platform processes over $21 trillion "
            "in assets across the financial system. "
            "\n\n"
            "CORPORATE CONTROL: BlackRock is the largest or second-largest shareholder in "
            "virtually every major public corporation in America. Combined with Vanguard and "
            "State Street, the 'Big Three' passive index fund managers collectively hold "
            "the single largest block of shares in 88% of S&P 500 firms. "
            "\n\n"
            "GOVERNMENT ENTANGLEMENT: Hired by the Federal Reserve in 2008 to manage the "
            "toxic asset portfolios from Bear Stearns and AIG bailouts (Maiden Lane vehicles). "
            "Hired again in 2020 for COVID emergency lending. Critics call it a 'fourth branch "
            "of government.' Larry Fink consults regularly with heads of state and central "
            "bankers worldwide."
        ),
        "aliases": "BLK",
        "metadata": {"type": "asset management", "founded": 1988, "aum": "$10+ trillion"},
    },
    {
        "name": "Vanguard",
        "entity_type": "organization",
        "description": (
            "Second-largest asset manager globally — over $8.6 trillion in AUM (2024). "
            "Founded by John Bogle in 1975, pioneered low-cost index fund investing. "
            "Unique mutual ownership structure: Vanguard is owned by its funds, which are "
            "owned by their shareholders. "
            "\n\n"
            "CONCENTRATION OF OWNERSHIP: Along with BlackRock and State Street, Vanguard "
            "is a top-three shareholder in nearly every major public company. Academic research "
            "(Fichtner et al., 2017) shows the Big Three have reconcentrated corporate "
            "ownership to levels not seen since the early 20th century — but with even less "
            "accountability than the old 'money trust' that the Pujo Committee investigated."
        ),
        "aliases": "Vanguard Group",
        "metadata": {"type": "asset management", "founded": 1975, "aum": "$8.6+ trillion"},
    },
    {
        "name": "State Street Corporation",
        "entity_type": "organization",
        "description": (
            "Third-largest asset manager globally, oldest financial institution in the US "
            "(founded 1792). Over $4.1 trillion in AUM (2024), $43 trillion in assets under "
            "custody. Operates the SPDR (Spider) family of ETFs, including SPY (largest ETF "
            "in the world). "
            "\n\n"
            "THE BIG THREE: Together with BlackRock and Vanguard, State Street completes "
            "the 'Big Three' passive index fund oligopoly. They collectively cast votes "
            "on behalf of millions of retail investors who have no say in how those votes "
            "are used — giving three firms outsized influence over corporate governance, "
            "executive compensation, and strategic direction of virtually every major company."
        ),
        "aliases": "State Street, SSgA, State Street Global Advisors",
        "metadata": {"type": "asset management / custody bank", "founded": 1792, "aum": "$4.1+ trillion"},
    },
    {
        "name": "International Monetary Fund",
        "entity_type": "organization",
        "description": (
            "International financial institution (189 member countries) providing loans to "
            "nations in balance-of-payments crises. Founded at Bretton Woods conference (1944). "
            "Headquartered in Washington, D.C. "
            "\n\n"
            "STRUCTURAL ADJUSTMENT: IMF loans come with conditions — privatization of state "
            "assets, austerity, trade liberalization, deregulation. Critics (Stiglitz, Perkins) "
            "argue these conditions benefit Western banks and corporations while devastating "
            "local economies. The pattern: crisis → loan → conditions → foreign acquisition "
            "of assets. "
            "\n\n"
            "VOTING POWER: Unlike the UN (one country, one vote), IMF voting is weighted by "
            "financial contribution. The US holds veto power (~16.5% of votes; 85% threshold "
            "needed for major decisions). Europe and Japan hold most of the rest. Developing "
            "nations that borrow the most have the least say."
        ),
        "aliases": "IMF",
        "metadata": {"type": "international financial institution", "founded": 1944, "hq": "Washington, D.C."},
    },
    {
        "name": "World Bank",
        "entity_type": "organization",
        "description": (
            "International financial institution providing loans and grants to developing "
            "nations. Founded alongside the IMF at Bretton Woods (1944). By tradition, the "
            "World Bank president is always an American (nominated by the US president), while "
            "the IMF managing director is always European. "
            "\n\n"
            "DEVELOPMENT OR DEBT TRAP: World Bank loans fund infrastructure, but conditions "
            "often require hiring Western contractors and opening markets. John Perkins (former "
            "economic consultant) described the system: inflate project costs, issue loans the "
            "country cannot repay, then extract resources and political concessions. Stiglitz "
            "(World Bank chief economist 1997-2000) resigned and became its most prominent critic. "
            "\n\n"
            "Notable presidents include Robert McNamara (from DOD, Vietnam War architect), "
            "Paul Wolfowitz (from DOD, Iraq War architect), and Robert Zoellick (from Goldman Sachs)."
        ),
        "aliases": "IBRD, International Bank for Reconstruction and Development",
        "metadata": {"type": "international financial institution", "founded": 1944, "hq": "Washington, D.C."},
    },
    {
        "name": "SWIFT",
        "entity_type": "organization",
        "description": (
            "Society for Worldwide Interbank Financial Telecommunication. Belgian cooperative "
            "that provides the global messaging system for international bank transfers. Over "
            "11,000 institutions in 200+ countries. Not a bank — it carries payment instructions. "
            "\n\n"
            "WEAPONIZATION: After 9/11, the US secretly accessed SWIFT data through the "
            "Terrorist Finance Tracking Program (exposed by NYT in 2006, European Parliament "
            "condemned the surveillance). In 2012 and again in 2022, the US pressured SWIFT "
            "to disconnect Iran and Russia respectively, effectively weaponizing the global "
            "payments infrastructure as a sanctions tool. This accelerated BRICS nations' "
            "development of alternative payment systems (China's CIPS, Russia's SPFS)."
        ),
        "aliases": "Society for Worldwide Interbank Financial Telecommunication",
        "metadata": {"type": "financial messaging network", "founded": 1973, "hq": "La Hulpe, Belgium"},
    },
    {
        "name": "Goldman Sachs",
        "entity_type": "organization",
        "description": (
            "Global investment bank, one of the most powerful financial institutions in the "
            "world. Founded 1869. Known as 'Government Sachs' for its extraordinary revolving "
            "door with the US Treasury and other government agencies. "
            "\n\n"
            "REVOLVING DOOR: Robert Rubin (Goldman co-chairman → Clinton Treasury Secretary → "
            "pushed Glass-Steagall repeal → Citigroup board, $126M compensation). Hank Paulson "
            "(Goldman CEO → Bush Treasury Secretary → designed TARP bailout that saved Goldman). "
            "Gary Cohn (Goldman president → Trump National Economic Council). Also: Jon Corzine, "
            "Robert Zoellick (World Bank president), Mark Carney (Bank of Canada, Bank of England). "
            "\n\n"
            "CRISIS PROFITEERING: Senate investigation found Goldman simultaneously marketed "
            "mortgage-backed securities to clients while betting against them. Paid $550M SEC "
            "fine (2010). Matt Taibbi called it 'a great vampire squid wrapped around the face "
            "of humanity.'"
        ),
        "aliases": "GS, Government Sachs",
        "metadata": {"type": "investment bank", "founded": 1869},
    },
    {
        "name": "Citigroup",
        "entity_type": "organization",
        "description": (
            "Global banking conglomerate formed by the 1998 merger of Citicorp and Travelers "
            "Group — a merger that was technically illegal under Glass-Steagall, which was then "
            "repealed the following year to make it retroactively legal. Robert Rubin, who as "
            "Treasury Secretary had pushed Glass-Steagall repeal, joined Citigroup's board "
            "within weeks of leaving office, earning $126M over the next decade. "
            "\n\n"
            "2008 CRISIS: Required $45 billion in TARP funds and $306 billion in government "
            "asset guarantees — the largest bailout of the crisis. The bank whose creation "
            "required destroying Depression-era safeguards nearly destroyed the global economy "
            "a decade later."
        ),
        "aliases": "Citi, Citicorp",
        "metadata": {"type": "commercial bank", "founded": 1998, "predecessor": "Citicorp (1812)"},
    },
    {
        "name": "Plunge Protection Team",
        "entity_type": "organization",
        "description": (
            "Informal name for the President's Working Group on Financial Markets, created "
            "by Executive Order 12631 (Reagan, March 1988) after the 1987 stock market crash. "
            "Members: Secretary of the Treasury (chair), Fed Chair, SEC Chair, CFTC Chair. "
            "\n\n"
            "Officially advisory, but Washington Post reporting (1997) revealed the group "
            "coordinates direct market intervention during crashes. The PPT can direct the "
            "Exchange Stabilization Fund, coordinate Fed actions, and signal confidence to "
            "markets. Its operations are not disclosed, its meetings are not public, and its "
            "interventions leave no official record."
        ),
        "aliases": "PPT, Working Group on Financial Markets, President's Working Group",
        "metadata": {"type": "government body", "founded": 1988},
    },
    {
        "name": "Exchange Stabilization Fund",
        "entity_type": "organization",
        "description": (
            "Treasury Department fund established by the Gold Reserve Act of 1934. Originally "
            "funded by the government's gold revaluation profit. Operates under the exclusive "
            "control of the Treasury Secretary — the only large government fund that does not "
            "require congressional appropriation or oversight. "
            "\n\n"
            "Can be used to buy or sell foreign currencies, provide financing to foreign "
            "governments, and intervene in financial markets. Used to backstop the Mexican "
            "peso crisis (1994-95, $20B) when Congress refused to authorize funds. The ESF's "
            "balance sheet and operations are largely opaque."
        ),
        "aliases": "ESF",
        "metadata": {"type": "government fund", "founded": 1934},
    },
    # --- People ---
    {
        "name": "Larry Fink",
        "entity_type": "person",
        "description": (
            "CEO and co-founder of BlackRock. Former First Boston bond trader. Built "
            "BlackRock into the world's largest asset manager ($10+ trillion AUM). Created "
            "the Aladdin risk analytics platform used across the financial system. "
            "\n\n"
            "INFLUENCE: Annual letter to CEOs is treated as a de facto policy directive for "
            "corporate America. Regularly consulted by heads of state, central bankers, and "
            "Treasury officials. BlackRock was hired by the Federal Reserve in both 2008 and "
            "2020 crises to manage emergency asset purchases — making Fink simultaneously the "
            "largest private asset manager and a quasi-governmental crisis manager."
        ),
        "aliases": "Laurence D. Fink",
        "metadata": {"role": "CEO, BlackRock", "years_active": "1988-present"},
    },
    {
        "name": "Timothy Geithner",
        "entity_type": "person",
        "description": (
            "President of the Federal Reserve Bank of New York (2003-2009), then Obama's "
            "Treasury Secretary (2009-2013). Protege of Robert Rubin and Larry Summers. As "
            "NY Fed president, he was the primary regulator of Wall Street banks in the "
            "years leading up to the 2008 crisis — and then became the architect of the "
            "bailout that rescued those same banks. "
            "\n\n"
            "BAILOUT ARCHITECTURE: Geithner championed full repayment of AIG's counterparty "
            "obligations (100 cents on the dollar to Goldman Sachs, Deutsche Bank, and others), "
            "rejected proposals to force bank bondholders to share losses, and opposed Swedish-"
            "style nationalization. After leaving Treasury, joined Warburg Pincus (private equity). "
            "SIGTARP inspector Neil Barofsky detailed how Geithner's Treasury repeatedly "
            "prioritized Wall Street over homeowners and taxpayers."
        ),
        "aliases": "Tim Geithner",
        "metadata": {"role": "NY Fed President / Treasury Secretary", "years_active": "2003-2013"},
    },
    {
        "name": "Hank Paulson",
        "entity_type": "person",
        "description": (
            "CEO of Goldman Sachs (1999-2006), then George W. Bush's Treasury Secretary "
            "(2006-2009). As Goldman CEO, oversaw the bank's massive expansion into mortgage-"
            "backed securities. As Treasury Secretary, designed and forced through the $700 "
            "billion TARP bailout — which saved Goldman Sachs from collapse. "
            "\n\n"
            "THE WEEKEND THAT CHANGED EVERYTHING: Sept 2008 — Paulson decided to let Lehman "
            "Brothers fail (Goldman's rival) while saving AIG (Goldman's largest counterparty, "
            "owed Goldman $13 billion). Former Goldman board member held AIG shares worth "
            "$850,000 at the time. Paulson had received an unprecedented ethics waiver from "
            "the IRS allowing him to defer taxes on $500M in Goldman stock sold upon entering "
            "government."
        ),
        "aliases": "Henry M. Paulson Jr.",
        "metadata": {"role": "Goldman CEO / Treasury Secretary", "years_active": "1999-2009"},
    },
    {
        "name": "Robert Rubin",
        "entity_type": "person",
        "description": (
            "Co-chairman of Goldman Sachs, then Bill Clinton's Treasury Secretary (1995-1999), "
            "then Citigroup board member and senior counselor. The architect of financial "
            "deregulation whose career epitomizes the Wall Street-Washington revolving door. "
            "\n\n"
            "GLASS-STEAGALL REPEAL: As Treasury Secretary, Rubin pushed for repeal of the "
            "Glass-Steagall Act (accomplished via Gramm-Leach-Bliley, 1999). Glass-Steagall "
            "had separated commercial and investment banking since 1933. Within weeks of "
            "leaving Treasury, Rubin joined Citigroup — the very conglomerate that could not "
            "have existed without the repeal he championed. Earned $126M at Citigroup over the "
            "next decade. Citigroup required $45B in TARP bailout funds in 2008. "
            "\n\n"
            "Also blocked Brooksley Born's attempts to regulate derivatives at the CFTC, "
            "which contributed directly to the 2008 crisis."
        ),
        "aliases": "Robert Edward Rubin",
        "metadata": {"role": "Goldman co-chair / Treasury Secretary / Citigroup", "years_active": "1966-2009"},
    },
    {
        "name": "Ben Bernanke",
        "entity_type": "person",
        "description": (
            "Chairman of the Federal Reserve (2006-2014). Academic economist (Princeton) "
            "specializing in the Great Depression. Appointed by George W. Bush, reappointed "
            "by Obama. Managed the Fed's response to the 2008 financial crisis. "
            "\n\n"
            "CRISIS RESPONSE: Orchestrated the largest monetary intervention in Fed history — "
            "slashed interest rates to zero, created emergency lending facilities, launched "
            "quantitative easing (QE), and opened secret $16+ trillion in emergency loans to "
            "banks worldwide (disclosed only through Bloomberg FOIA and GAO audit, 2011). "
            "Defended the bailout of Bear Stearns and AIG while allowing Lehman Brothers to "
            "fail. Won the Nobel Prize in Economics (2022) for research on bank runs — ironic "
            "given the bank runs he oversaw."
        ),
        "aliases": "Ben S. Bernanke",
        "metadata": {"role": "Federal Reserve Chairman", "years_active": "2006-2014"},
    },
    # --- Events ---
    {
        "name": "Glass-Steagall Repeal",
        "entity_type": "event",
        "description": (
            "The 1999 Gramm-Leach-Bliley Act repealed the Glass-Steagall Act of 1933, which "
            "had separated commercial banking (deposits, loans) from investment banking "
            "(securities, trading). Glass-Steagall was enacted after the 1929 crash to prevent "
            "banks from gambling with depositors' money. "
            "\n\n"
            "LOBBYING: The financial industry spent over $300 million lobbying for repeal "
            "in the 1990s. Citicorp's merger with Travelers Group (1998) was technically "
            "illegal under Glass-Steagall — the law was then changed to accommodate the "
            "merger. Robert Rubin pushed repeal as Treasury Secretary, then joined Citigroup. "
            "\n\n"
            "CONSEQUENCES: Allowed commercial banks to engage in speculative trading with "
            "federally insured deposits. Directly enabled the creation of the mortgage-backed "
            "securities that caused the 2008 crisis. The 'too big to fail' banks that "
            "required bailouts were all conglomerates that Glass-Steagall would have prohibited."
        ),
        "aliases": "Gramm-Leach-Bliley Act, Financial Services Modernization Act of 1999",
        "metadata": {"date": "1999-11-12"},
    },
    {
        "name": "2008 Financial Crisis",
        "entity_type": "event",
        "description": (
            "Global financial crisis triggered by the collapse of the US subprime mortgage "
            "market. Lehman Brothers filed for bankruptcy (Sept 15, 2008) — the largest in "
            "US history ($639B in assets). AIG required $182B in government bailout. "
            "\n\n"
            "TARP BAILOUT: Emergency Economic Stabilization Act (Oct 2008) authorized $700B "
            "in taxpayer funds to purchase toxic assets from banks. Major recipients: "
            "Citigroup ($45B), Bank of America ($45B), AIG ($40B), JPMorgan ($25B), Goldman "
            "Sachs ($10B). Simultaneously, the Fed secretly lent $16+ trillion in emergency "
            "funds to banks worldwide (GAO-11-696). "
            "\n\n"
            "ACCOUNTABILITY: Zero senior bank executives were criminally prosecuted. The "
            "FCIC concluded the crisis was 'avoidable' and caused by 'widespread failures "
            "in financial regulation,' 'dramatic breakdowns in corporate governance,' and "
            "'systemic breakdown in accountability and ethics.' 8.7 million jobs lost, "
            "10 million foreclosures, $19.2 trillion in household wealth destroyed."
        ),
        "aliases": "Great Recession, Global Financial Crisis, TARP Bailout, 2008 Crash",
        "metadata": {"date": "2007-2009"},
    },
    {
        "name": "LIBOR Scandal",
        "entity_type": "event",
        "description": (
            "Systematic manipulation of the London Interbank Offered Rate — the benchmark "
            "interest rate underpinning $350+ trillion in financial contracts worldwide "
            "(mortgages, student loans, derivatives, municipal bonds). "
            "\n\n"
            "COLLUSION: Multiple major banks (Barclays, UBS, Deutsche Bank, Rabobank, "
            "JPMorgan, Citigroup, Bank of America, and others) were found to have colluded "
            "to manipulate LIBOR submissions for profit and to hide their true borrowing costs "
            "during the 2008 crisis. Trader chats revealed casual, systematic rigging: "
            "'Dude. I owe you big time!' "
            "\n\n"
            "PENALTIES: Over $9 billion in fines across participating banks. Barclays was "
            "first to settle ($453M, 2012). Several traders imprisoned. LIBOR itself was "
            "phased out and replaced by SOFR (2023). But the scandal revealed that the most "
            "fundamental price in global finance was set by a phone poll of banks who were "
            "lying about it."
        ),
        "aliases": "LIBOR rigging, LIBOR manipulation, rate-rigging scandal",
        "metadata": {"date": "2003-2012 (manipulation period), 2012-2015 (enforcement)"},
    },
    {
        "name": "Petrodollar System",
        "entity_type": "event",
        "description": (
            "Agreement established in 1974-75 between the United States (Kissinger/Nixon "
            "administration) and Saudi Arabia: Saudi Arabia would price all oil exports in "
            "US dollars and recycle surplus petrodollars into US Treasury securities, and "
            "the US would provide military protection for the Saudi regime. "
            "\n\n"
            "MECHANISM: Because every nation must buy oil, every nation must hold dollars — "
            "creating permanent global demand for USD. This allows the US to run persistent "
            "trade deficits and fund its military through debt that the world is structurally "
            "compelled to buy. The arrangement was kept classified for 41 years until Bloomberg "
            "obtained declassified Treasury data (2016). "
            "\n\n"
            "CURRENT EROSION: China's yuan-denominated oil contracts with Saudi Arabia, "
            "Russia, and Iran. BRICS nations developing alternative settlement systems. "
            "The petrodollar system underpins US hegemony — its erosion is the most "
            "consequential financial shift of the 21st century."
        ),
        "aliases": "Petrodollar recycling, Kissinger-Saudi oil deal",
        "metadata": {"date": "1974-1975"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- BIS hierarchy ---
    {
        "source": "Bank for International Settlements",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Fed is a BIS member institution. BIS hosts bimonthly meetings of central bank governors and sets Basel capital requirements that the Fed implements domestically. BIS operates above national sovereignty with diplomatic immunity.",
        "sources": [910, 911],
        "year_start": 1930,
        "year_end": None,
    },
    {
        "source": "Bank for International Settlements",
        "target": "International Monetary Fund",
        "type": "connected_to",
        "tier": "documented",
        "desc": "BIS, IMF, and World Bank form the triad of international financial governance established in the 1930s-1940s. BIS predates the Bretton Woods institutions and coordinates central bank policy that the IMF enforces at national level.",
        "sources": [910, 926],
        "year_start": 1944,
        "year_end": None,
    },
    {
        "source": "International Monetary Fund",
        "target": "World Bank",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Twin Bretton Woods institutions. IMF provides short-term crisis loans with structural adjustment conditions; World Bank provides long-term development loans. Both headquartered in Washington, voting weighted by financial contribution, US holds veto in both.",
        "sources": [926, 927],
        "year_start": 1944,
        "year_end": None,
    },
    # --- Big Three asset management oligopoly ---
    {
        "source": "BlackRock",
        "target": "Vanguard",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Together with State Street, BlackRock and Vanguard form the 'Big Three' passive index fund managers. Academic research (2017) found they collectively are the largest shareholder in 88% of S&P 500 firms, reconcentrating corporate ownership to levels unseen since the Pujo Committee era.",
        "sources": [912, 913],
        "year_start": 2000,
        "year_end": None,
    },
    {
        "source": "BlackRock",
        "target": "State Street Corporation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Big Three member. BlackRock, Vanguard, and State Street together vote the shares of trillions in index fund holdings, giving three firms outsized influence over corporate governance in nearly every major public company.",
        "sources": [912, 913],
        "year_start": 2000,
        "year_end": None,
    },
    {
        "source": "Vanguard",
        "target": "State Street Corporation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Big Three member. The three largest index fund managers collectively hold controlling blocks in most major corporations, creating a new form of 'universal ownership' that concentrates voting power without the capital commitment of traditional ownership.",
        "sources": [912, 913],
        "year_start": 2000,
        "year_end": None,
    },
    # --- Larry Fink / BlackRock ---
    {
        "source": "Larry Fink",
        "target": "BlackRock",
        "type": "founded",
        "tier": "documented",
        "desc": "Co-founded BlackRock in 1988 (originally within Blackstone Group, spun off 1994). Built it into the world's largest asset manager. Serves as chairman and CEO.",
        "sources": [912, 930],
        "year_start": 1988,
        "year_end": None,
    },
    {
        "source": "BlackRock",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "documented",
        "desc": "NY Fed hired BlackRock Financial Markets Advisory in 2008 to manage Bear Stearns and AIG toxic asset portfolios (Maiden Lane vehicles). Hired again in 2020 for COVID emergency bond-buying. BlackRock simultaneously manages trillions in private assets and executes Fed policy.",
        "sources": [929, 930],
        "year_start": 2008,
        "year_end": None,
    },
    # --- Goldman Sachs revolving door ---
    {
        "source": "Hank Paulson",
        "target": "Goldman Sachs",
        "type": "worked_for",
        "tier": "documented",
        "desc": "CEO of Goldman Sachs (1999-2006). Oversaw Goldman's expansion into mortgage-backed securities. Left to become Treasury Secretary.",
        "sources": [901, 916],
        "year_start": 1999,
        "year_end": 2006,
    },
    {
        "source": "Hank Paulson",
        "target": "2008 Financial Crisis",
        "type": "connected_to",
        "tier": "documented",
        "desc": "As Treasury Secretary, designed the $700B TARP bailout. Let Lehman Brothers (Goldman rival) fail while saving AIG (which owed Goldman $13B). Received IRS ethics waiver to defer taxes on $500M in Goldman stock sold upon entering government.",
        "sources": [901, 906, 907],
        "year_start": 2008,
        "year_end": 2009,
    },
    {
        "source": "Robert Rubin",
        "target": "Goldman Sachs",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Co-chairman of Goldman Sachs before becoming Clinton's Treasury Secretary (1995-1999). Goldman career established the Wall Street-Washington pipeline he later institutionalized.",
        "sources": [917, 919, 920],
        "year_start": 1966,
        "year_end": 1993,
    },
    {
        "source": "Robert Rubin",
        "target": "Glass-Steagall Repeal",
        "type": "connected_to",
        "tier": "documented",
        "desc": "As Treasury Secretary, Rubin was the primary advocate for repealing Glass-Steagall. The Gramm-Leach-Bliley Act (1999) removed Depression-era banking safeguards. Within weeks of leaving office, Rubin joined Citigroup — the very conglomerate enabled by the repeal.",
        "sources": [903, 919, 920],
        "year_start": 1995,
        "year_end": 1999,
    },
    {
        "source": "Robert Rubin",
        "target": "Citigroup",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Joined Citigroup board and senior counselor role within weeks of leaving Treasury. Earned $126M over the next decade. Citigroup's existence as a commercial-investment bank conglomerate depended on the Glass-Steagall repeal Rubin had championed.",
        "sources": [919, 920, 901],
        "year_start": 1999,
        "year_end": 2009,
    },
    {
        "source": "Robert Rubin",
        "target": "Bill Clinton",
        "type": "worked_for",
        "tier": "documented",
        "desc": "Served as Clinton's Treasury Secretary (1995-1999). Shaped the administration's financial deregulation agenda including Glass-Steagall repeal and blocking derivatives regulation.",
        "sources": [917, 919],
        "year_start": 1995,
        "year_end": 1999,
    },
    # --- Geithner / NY Fed / Bailout ---
    {
        "source": "Timothy Geithner",
        "target": "Federal Reserve System",
        "type": "worked_for",
        "tier": "documented",
        "desc": "President of the NY Fed (2003-2009) — the most powerful regional Fed bank, primary regulator of Wall Street. Failed to prevent the crisis at the institutions he regulated, then became the architect of their bailout.",
        "sources": [901, 905, 928],
        "year_start": 2003,
        "year_end": 2009,
    },
    {
        "source": "Timothy Geithner",
        "target": "2008 Financial Crisis",
        "type": "connected_to",
        "tier": "documented",
        "desc": "As NY Fed president, oversaw the Bear Stearns rescue and AIG bailout. As Obama Treasury Secretary, championed full AIG counterparty payouts (100 cents on dollar to Goldman, Deutsche Bank). SIGTARP inspector Barofsky documented how Geithner prioritized Wall Street over homeowners.",
        "sources": [901, 906, 928],
        "year_start": 2008,
        "year_end": 2013,
    },
    {
        "source": "Timothy Geithner",
        "target": "Goldman Sachs",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Geithner's NY Fed oversaw Goldman's conversion to a bank holding company (Sept 2008), enabling Goldman to access Fed emergency lending. AIG bailout funneled $13B to Goldman at full value. Geithner protege of Robert Rubin (Goldman alumnus).",
        "sources": [901, 928, 929],
        "year_start": 2008,
        "year_end": 2009,
    },
    # --- Bernanke / Fed / Crisis ---
    {
        "source": "Ben Bernanke",
        "target": "Federal Reserve System",
        "type": "led",
        "tier": "documented",
        "desc": "Federal Reserve Chairman (2006-2014). Managed the largest monetary intervention in Fed history: zero interest rates, quantitative easing, $16+ trillion in secret emergency loans to global banks.",
        "sources": [901, 905, 929],
        "year_start": 2006,
        "year_end": 2014,
    },
    {
        "source": "Ben Bernanke",
        "target": "2008 Financial Crisis",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Orchestrated the Fed's crisis response — emergency lending facilities, Bear Stearns rescue, AIG bailout, quantitative easing. Bloomberg FOIA revealed the Fed secretly lent $16+ trillion to banks worldwide, far exceeding the publicly disclosed TARP.",
        "sources": [901, 905, 929],
        "year_start": 2007,
        "year_end": 2009,
    },
    # --- Glass-Steagall → Crisis chain ---
    {
        "source": "Glass-Steagall Repeal",
        "target": "2008 Financial Crisis",
        "type": "connected_to",
        "tier": "credible",
        "desc": "FCIC found that deregulation was a key cause of the crisis. Glass-Steagall repeal allowed commercial banks to engage in speculative trading with insured deposits, creating the 'too big to fail' conglomerates that required bailout.",
        "sources": [901, 903, 919],
        "year_start": 1999,
        "year_end": 2008,
    },
    {
        "source": "Glass-Steagall Repeal",
        "target": "Citigroup",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Citicorp-Travelers merger (1998) was technically illegal under Glass-Steagall. The law was repealed the next year to accommodate the merger. Citigroup then became the poster child for 'too big to fail' — requiring $45B in TARP funds.",
        "sources": [903, 919, 901],
        "year_start": 1998,
        "year_end": 2008,
    },
    # --- TARP / Crisis relationships ---
    {
        "source": "2008 Financial Crisis",
        "target": "Goldman Sachs",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Goldman received $10B in TARP funds, plus $13B through the AIG counterparty bailout. Senate investigation found Goldman simultaneously sold mortgage securities to clients while betting against them. $550M SEC fine (2010). Zero criminal prosecutions.",
        "sources": [901, 902, 906, 916],
        "year_start": 2008,
        "year_end": 2010,
    },
    {
        "source": "2008 Financial Crisis",
        "target": "JPMorgan Chase",
        "type": "connected_to",
        "tier": "documented",
        "desc": "JPMorgan received $25B in TARP funds. Also acquired Bear Stearns at fire-sale price ($2/share, later $10) with $30B in Fed guarantees — brokered by Geithner's NY Fed. Emerged from the crisis larger and more dominant.",
        "sources": [901, 906, 907],
        "year_start": 2008,
        "year_end": 2009,
    },
    {
        "source": "2008 Financial Crisis",
        "target": "Deutsche Bank",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Deutsche Bank received $11.8B through AIG counterparty payouts (second only to Goldman). Also received Fed emergency lending. Later paid $7.2B for its role in mortgage securities fraud (2017 DOJ settlement).",
        "sources": [901, 905, 929],
        "year_start": 2008,
        "year_end": 2009,
    },
    # --- LIBOR scandal ---
    {
        "source": "LIBOR Scandal",
        "target": "Deutsche Bank",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Deutsche Bank paid $2.5B in LIBOR manipulation penalties (2015) — the largest fine in the scandal. Bank traders systematically rigged rate submissions for profit.",
        "sources": [908, 909],
        "year_start": 2005,
        "year_end": 2015,
    },
    {
        "source": "LIBOR Scandal",
        "target": "JPMorgan Chase",
        "type": "connected_to",
        "tier": "documented",
        "desc": "JPMorgan was among the panel banks submitting LIBOR rates. Paid settlements for rate manipulation. The scandal revealed that the most fundamental price in global finance was systematically rigged.",
        "sources": [908, 909],
        "year_start": 2005,
        "year_end": 2013,
    },
    # --- Petrodollar ---
    {
        "source": "Henry Kissinger",
        "target": "Petrodollar System",
        "type": "created",
        "tier": "credible",
        "desc": "Kissinger negotiated the petrodollar agreement with Saudi Arabia (1974-75): oil priced exclusively in USD, surplus recycled into US Treasuries, in exchange for US military protection. Kept classified for 41 years.",
        "sources": [914, 915],
        "year_start": 1974,
        "year_end": 1975,
    },
    {
        "source": "Petrodollar System",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Petrodollar recycling creates structural global demand for US dollars and Treasuries, enabling the Fed to maintain the dollar as world reserve currency and the US to run persistent deficits financed by foreign central banks.",
        "sources": [914, 915],
        "year_start": 1974,
        "year_end": None,
    },
    # --- SWIFT weaponization ---
    {
        "source": "SWIFT",
        "target": "NSA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "US secretly accessed SWIFT financial data via the Terrorist Finance Tracking Program after 9/11 (exposed by NYT 2006). European Parliament condemned the surveillance. SWIFT data gave US intelligence visibility into virtually all international financial transactions.",
        "sources": [921, 922],
        "year_start": 2001,
        "year_end": None,
    },
    {
        "source": "SWIFT",
        "target": "BCCI",
        "type": "connected_to",
        "tier": "inference",
        "desc": "SWIFT provides the messaging infrastructure for international banking. BCCI's collapse (1991) demonstrated the vulnerability of the global banking system to criminal networks — SWIFT's centralized architecture later became a surveillance and sanctions tool partly in response.",
        "sources": [921],
        "year_start": 1991,
        "year_end": None,
    },
    # --- Plunge Protection Team / ESF ---
    {
        "source": "Plunge Protection Team",
        "target": "Exchange Stabilization Fund",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The PPT (Working Group on Financial Markets) can direct the ESF for market interventions. The Treasury Secretary chairs the PPT and has exclusive control of the ESF — no congressional approval needed. Combined, they form an opaque market intervention capability.",
        "sources": [923, 924, 925],
        "year_start": 1988,
        "year_end": None,
    },
    {
        "source": "Plunge Protection Team",
        "target": "Federal Reserve System",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Fed Chair sits on the PPT (Working Group on Financial Markets). PPT coordinates Fed actions with Treasury, SEC, and CFTC during market crises. Operations are not publicly disclosed.",
        "sources": [924, 925],
        "year_start": 1988,
        "year_end": None,
    },
    # --- Alan Greenspan links ---
    {
        "source": "Alan Greenspan",
        "target": "Glass-Steagall Repeal",
        "type": "connected_to",
        "tier": "documented",
        "desc": "As Fed Chairman, Greenspan publicly advocated for Glass-Steagall repeal and broader financial deregulation. Used Fed regulatory interpretations to weaken Glass-Steagall before its formal repeal. Later admitted to Congress (2008) that his deregulatory ideology was flawed.",
        "sources": [901, 903, 919],
        "year_start": 1987,
        "year_end": 1999,
    },
    {
        "source": "Alan Greenspan",
        "target": "2008 Financial Crisis",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Greenspan's 18-year tenure as Fed Chair (1987-2006) promoted deregulation, blocked derivatives oversight, and maintained low interest rates that fueled the housing bubble. Testified to Congress in 2008: 'I found a flaw in the model... that defines how the world works.'",
        "sources": [901, 917, 918],
        "year_start": 1987,
        "year_end": 2006,
    },
    # --- IMF/World Bank and CIA ---
    {
        "source": "International Monetary Fund",
        "target": "CIA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "IMF structural adjustment programs have repeatedly aligned with US foreign policy objectives. Perkins described economic hit men using World Bank/IMF debt to secure political compliance. Stiglitz documented how IMF conditions benefited Western financial interests over borrowing nations.",
        "sources": [926, 927],
        "year_start": 1960,
        "year_end": None,
    },
    {
        "source": "World Bank",
        "target": "Goldman Sachs",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Robert Zoellick served as World Bank president (2007-2012) after careers at Goldman Sachs and the State Department. The revolving door between Wall Street and international financial institutions mirrors the Goldman-Treasury pipeline domestically.",
        "sources": [917, 926],
        "year_start": 2007,
        "year_end": 2012,
    },
    # --- Goldman Sachs → LIBOR ---
    {
        "source": "Goldman Sachs",
        "target": "LIBOR Scandal",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Goldman Sachs was among the major banks implicated in LIBOR-related manipulation. The scandal revealed industry-wide collusion in setting the benchmark rate underlying $350+ trillion in financial contracts.",
        "sources": [908, 909],
        "year_start": 2005,
        "year_end": 2012,
    },
    # --- Federal Reserve emergency lending ---
    {
        "source": "Federal Reserve System",
        "target": "2008 Financial Crisis",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Bloomberg FOIA and GAO audit (2011) revealed the Fed secretly lent $16+ trillion to banks worldwide during the crisis — dwarfing the publicly debated $700B TARP. Lending was not disclosed to Congress. GAO found conflicts of interest among Fed officials.",
        "sources": [904, 905, 929],
        "year_start": 2007,
        "year_end": 2010,
    },
    # --- Epstein connections to financial system ---
    {
        "source": "Jeffrey Epstein",
        "target": "Goldman Sachs",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Epstein cultivated relationships across Wall Street. His financial management firm operated with extreme secrecy — no client list ever disclosed. Connected to the financial elite through Les Wexner, Mega Group, and social networks spanning Wall Street and government.",
        "sources": [916, 917],
        "year_start": 1990,
        "year_end": 2019,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Bank for International Settlements": [910, 911],
    "BlackRock": [912, 913, 930],
    "Vanguard": [912, 913],
    "State Street Corporation": [912, 913],
    "International Monetary Fund": [926, 927],
    "World Bank": [926, 927],
    "SWIFT": [921, 922],
    "Goldman Sachs": [901, 902, 916, 917],
    "Citigroup": [901, 903, 919, 920],
    "Plunge Protection Team": [924, 925],
    "Exchange Stabilization Fund": [923],
    "Larry Fink": [912, 913, 930],
    "Timothy Geithner": [901, 905, 928],
    "Hank Paulson": [901, 906, 907, 916],
    "Robert Rubin": [903, 917, 919, 920],
    "Ben Bernanke": [901, 905, 929],
    "Glass-Steagall Repeal": [903, 919],
    "2008 Financial Crisis": [901, 902, 906, 907],
    "LIBOR Scandal": [908, 909],
    "Petrodollar System": [914, 915],
}
