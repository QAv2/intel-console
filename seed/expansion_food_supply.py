"""
Food Supply Control — Expansion layer for Intel Console.

New branch mapping corporate control of the global food supply: seed monopolies
(Monsanto/Bayer, Syngenta), grain cartels (Cargill, ADM), regulatory capture
(USDA, Codex Alimentarius), and the systematic destruction of agricultural
independence through patents, terminator seeds, and predatory lawsuits against
farmers.

The throughline: control the seeds, control the food. Control the food, control
the population. When one company can patent life, sue farmers whose fields are
contaminated by their pollen, and suppress research showing their products cause
cancer — that's not a free market, it's a control system.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Monsanto (from health expansion), FDA, Bill Gates, WHO,
  Vandana Shiva (from water expansion)

Evidence tiers:
  documented = congressional record, court filing, official government doc, corporate filings
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1261-1290
# ============================================================

SOURCES = [
    # --- Monsanto Papers ---
    {
        "id": 1261,
        "title": "The Monsanto Papers — internal documents revealed through Roundup cancer litigation (U.S. Right to Know)",
        "url": "https://usrtk.org/pesticides/monsanto-papers/",
        "source_type": "court",
        "author": "U.S. Right to Know",
        "year": 2017,
    },
    {
        "id": 1262,
        "title": "Dewayne Johnson v. Monsanto — first Roundup cancer trial, $289M verdict (San Francisco Superior Court, 2018)",
        "url": "https://en.wikipedia.org/wiki/Johnson_v._Monsanto_Co.",
        "source_type": "court",
        "year": 2018,
    },
    {
        "id": 1263,
        "title": "IARC (WHO) — Monograph 112: Glyphosate classified as 'probably carcinogenic to humans' (Group 2A, 2015)",
        "url": "https://en.wikipedia.org/wiki/Glyphosate",
        "source_type": "academic",
        "year": 2015,
    },
    # --- Tyrone Hayes / Atrazine ---
    {
        "id": 1264,
        "title": "Tyrone Hayes — 'Atrazine-Induced Hermaphroditism at 0.1 ppb in American Leopard Frogs' (Environmental Health Perspectives, 2003)",
        "url": "https://doi.org/10.1289/ehp.5932",
        "source_type": "academic",
        "author": "Tyrone B. Hayes et al.",
        "year": 2003,
    },
    {
        "id": 1265,
        "title": "Rachel Aviv — 'A Valuable Reputation: After Tyrone Hayes said a chemical was harmful, its maker pursued him' (New Yorker, 2014)",
        "url": "https://www.newyorker.com/magazine/2014/02/10/a-valuable-reputation",
        "source_type": "journalism",
        "author": "Rachel Aviv",
        "year": 2014,
    },
    # --- Percy Schmeiser ---
    {
        "id": 1266,
        "title": "Monsanto Canada Inc. v. Schmeiser — Supreme Court of Canada (2004, patent law vs. farmer's rights)",
        "url": "https://en.wikipedia.org/wiki/Monsanto_Canada_Inc_v_Schmeiser",
        "source_type": "court",
        "year": 2004,
    },
    {
        "id": 1267,
        "title": "Percy Schmeiser — Wikipedia (Canadian canola farmer vs. Monsanto patent infringement suit)",
        "url": "https://en.wikipedia.org/wiki/Percy_Schmeiser",
        "source_type": "other",
        "year": 2024,
    },
    # --- Hugh Grant / Monsanto ---
    {
        "id": 1268,
        "title": "Hugh Grant (businessman) — Monsanto CEO 2003-2018, oversaw GMO expansion and Roundup defense",
        "url": "https://en.wikipedia.org/wiki/Hugh_Grant_(businessman)",
        "source_type": "other",
        "year": 2024,
    },
    # --- Robert Fraley ---
    {
        "id": 1269,
        "title": "Robert Fraley — Monsanto CTO, World Food Prize laureate (2013, for GMO development)",
        "url": "https://en.wikipedia.org/wiki/Robert_T._Fraley",
        "source_type": "other",
        "year": 2013,
    },
    # --- Bayer acquisition ---
    {
        "id": 1270,
        "title": "Bayer acquires Monsanto for $63 billion — DOJ antitrust approval with conditions (2018)",
        "url": "https://en.wikipedia.org/wiki/Bayer",
        "source_type": "government",
        "year": 2018,
    },
    # --- Cargill ---
    {
        "id": 1271,
        "title": "Brewster Kneen — 'Invisible Giant: Cargill and Its Transnational Strategies' (Pluto Press, 2002)",
        "url": "https://en.wikipedia.org/wiki/Cargill",
        "source_type": "book",
        "author": "Brewster Kneen",
        "year": 2002,
    },
    {
        "id": 1272,
        "title": "Cargill — Wikipedia (largest privately held corporation in the U.S., grain trading)",
        "url": "https://en.wikipedia.org/wiki/Cargill",
        "source_type": "other",
        "year": 2024,
    },
    # --- ADM ---
    {
        "id": 1273,
        "title": "Kurt Eichenwald — 'The Informant: A True Story' (Broadway Books, 2000) — ADM price-fixing scandal",
        "url": "https://en.wikipedia.org/wiki/Archer_Daniels_Midland",
        "source_type": "book",
        "author": "Kurt Eichenwald",
        "year": 2000,
    },
    {
        "id": 1274,
        "title": "United States v. Andreas — ADM lysine price-fixing conviction, $100M fine (7th Circuit, 2000)",
        "url": "https://en.wikipedia.org/wiki/Archer_Daniels_Midland_price-fixing_scandal",
        "source_type": "court",
        "year": 2000,
    },
    # --- Syngenta ---
    {
        "id": 1275,
        "title": "Syngenta — Wikipedia (seeds/pesticides, ChemChina/Sinochem acquisition for $43B)",
        "url": "https://en.wikipedia.org/wiki/Syngenta",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 1276,
        "title": "ChemChina acquires Syngenta for $43 billion — largest Chinese overseas acquisition (2017)",
        "url": "https://en.wikipedia.org/wiki/Syngenta",
        "source_type": "journalism",
        "year": 2017,
    },
    # --- Indian farmer suicides ---
    {
        "id": 1277,
        "title": "Centre for Human Rights and Global Justice — 'Every Thirty Minutes: Farmer Suicides, Human Rights, and the Agrarian Crisis in India' (NYU School of Law, 2011)",
        "url": "https://en.wikipedia.org/wiki/Farmers%27_suicides_in_India",
        "source_type": "academic",
        "year": 2011,
    },
    {
        "id": 1278,
        "title": "Vandana Shiva — 'The Violence of the Green Revolution' (Third World Network, 1991)",
        "url": "https://en.wikipedia.org/wiki/Vandana_Shiva",
        "source_type": "book",
        "author": "Vandana Shiva",
        "year": 1991,
    },
    # --- Terminator seeds ---
    {
        "id": 1279,
        "title": "RAFI (ETC Group) — 'Terminator Technology: The Threat to World Food Security' (1998)",
        "url": "https://en.wikipedia.org/wiki/Genetic_use_restriction_technologies",
        "source_type": "academic",
        "year": 1998,
    },
    {
        "id": 1280,
        "title": "U.S. Patent 5,723,765 — 'Control of Plant Gene Expression' (Delta and Pine Land Co. / USDA, 1998)",
        "url": "https://en.wikipedia.org/wiki/Genetic_use_restriction_technologies",
        "source_type": "government",
        "year": 1998,
    },
    # --- Codex Alimentarius ---
    {
        "id": 1281,
        "title": "Codex Alimentarius Commission — WHO/FAO food standards program (official website)",
        "url": "https://en.wikipedia.org/wiki/Codex_Alimentarius",
        "source_type": "government",
        "year": 2024,
    },
    # --- USDA ---
    {
        "id": 1282,
        "title": "USDA — revolving door with agribusiness (Center for Responsive Politics / OpenSecrets data)",
        "url": "https://en.wikipedia.org/wiki/United_States_Department_of_Agriculture",
        "source_type": "journalism",
        "year": 2023,
    },
    # --- Monsanto Protection Act ---
    {
        "id": 1283,
        "title": "Section 735 of H.R. 933 — 'Farmer Assurance Provision' a.k.a. Monsanto Protection Act (2013, expired 2013)",
        "url": "https://en.wikipedia.org/wiki/Farmer_Assurance_Provision",
        "source_type": "congressional",
        "year": 2013,
    },
    # --- DARK Act ---
    {
        "id": 1284,
        "title": "S.764 — National Bioengineered Food Disclosure Standard (DARK Act, 2016) — preempted state GMO labeling laws",
        "url": "https://en.wikipedia.org/wiki/National_Bioengineered_Food_Disclosure_Standard",
        "source_type": "congressional",
        "year": 2016,
    },
    # --- Plant Variety Protection Act ---
    {
        "id": 1285,
        "title": "Plant Variety Protection Act (1970) — U.S. law granting intellectual property protection to new plant varieties",
        "url": "https://en.wikipedia.org/wiki/Plant_Variety_Protection_Act_of_1970",
        "source_type": "government",
        "year": 1970,
    },
    # --- Bill Gates farmland ---
    {
        "id": 1286,
        "title": "Bill Gates — largest private farmland owner in U.S. (~270,000 acres, Land Report 2021)",
        "url": "https://en.wikipedia.org/wiki/Bill_Gates",
        "source_type": "journalism",
        "year": 2021,
    },
    # --- Bayer Roundup settlement ---
    {
        "id": 1287,
        "title": "Bayer to pay $10.9 billion to settle Roundup cancer claims — Reuters (2020)",
        "url": "https://www.reuters.com/article/us-bayer-litigation-settlement-idUSKBN23V2FP",
        "source_type": "journalism",
        "author": "Reuters",
        "year": 2020,
    },
    # --- ABCD grain traders ---
    {
        "id": 1288,
        "title": "Sophia Murphy et al. — 'Cereal Secrets: The World's Largest Grain Traders and Global Agriculture' (Oxfam, 2012)",
        "url": "https://en.wikipedia.org/wiki/Grain_trade",
        "source_type": "academic",
        "author": "Sophia Murphy, David Burch, Jennifer Clapp",
        "year": 2012,
    },
    # --- Syngenta atrazine defense ---
    {
        "id": 1289,
        "title": "Syngenta internal documents — campaign to discredit Tyrone Hayes' atrazine research (revealed in litigation)",
        "url": "https://en.wikipedia.org/wiki/Atrazine",
        "source_type": "court",
        "year": 2012,
    },
    # --- Seed sovereignty ---
    {
        "id": 1290,
        "title": "Vandana Shiva — 'Stolen Harvest: The Hijacking of the Global Food Supply' (South End Press, 2000)",
        "url": "https://en.wikipedia.org/wiki/Vandana_Shiva",
        "source_type": "book",
        "author": "Vandana Shiva",
        "year": 2000,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- People ---
    {
        "name": "Hugh Grant",
        "entity_type": "person",
        "description": "Scottish-American businessman. CEO of Monsanto (2003-2018) during the company's most aggressive period of GMO expansion, farmer litigation, and Roundup defense. Oversaw the $63 billion sale to Bayer (2018). Under his leadership, Monsanto fought IARC's glyphosate cancer classification, suppressed internal research on health risks (revealed in Monsanto Papers), and continued suing farmers over patented seed technology.",
        "aliases": "Hugh Grant (Monsanto)",
        "metadata": {"role": "Monsanto CEO", "years_active": "2003-2018"},
    },
    {
        "name": "Robert Fraley",
        "entity_type": "person",
        "description": "American scientist. Chief Technology Officer of Monsanto. Pioneer of plant cell transformation technology that enabled genetically modified crops. Co-recipient of the 2013 World Food Prize for his role in developing GMOs. Critics argue the Prize was effectively an industry honor — the award legitimized Monsanto's technology while the company was suppressing research on health risks and suing farmers.",
        "aliases": "Robert T. Fraley, Robb Fraley",
        "metadata": {"role": "Monsanto CTO / GMO pioneer", "years_active": "1981-2018"},
    },
    {
        "name": "Percy Schmeiser",
        "entity_type": "person",
        "description": "Canadian canola farmer (1931-2020). Sued by Monsanto for patent infringement after Roundup Ready canola was found growing in his fields — which he maintained was contaminated by wind-blown pollen from neighboring farms, not intentionally planted. Supreme Court of Canada ruled (2004) that Monsanto's patent was valid but awarded Schmeiser no damages. Became a global symbol of farmer resistance to corporate seed patents. Won the Right Livelihood Award (2007).",
        "aliases": "",
        "metadata": {"role": "farmer / seed rights activist", "years_active": "1998-2020"},
    },
    {
        "name": "Tyrone Hayes",
        "entity_type": "person",
        "description": "American biologist, Professor of Integrative Biology at UC Berkeley. Published research showing the herbicide atrazine causes hermaphroditism in frogs at extremely low concentrations (0.1 ppb). After publishing, Syngenta (atrazine's manufacturer) launched a systematic campaign to discredit him — internal documents revealed in litigation showed the company hired PR firms to attack his character, fund counter-research, and pressure his university. His case is one of the most documented examples of a corporation targeting a scientist for producing inconvenient results.",
        "aliases": "Tyrone B. Hayes",
        "metadata": {"role": "biologist / UC Berkeley", "years_active": "1998-present"},
    },
    # --- Organizations ---
    {
        "name": "Cargill",
        "entity_type": "organization",
        "description": "The largest privately held corporation in the United States by revenue (~$177 billion, 2023). One of the 'ABCD' grain traders (ADM, Bunge, Cargill, Dreyfus) that control the majority of global grain trade. Operates in food processing, animal feed, agricultural trading, and financial services across 70+ countries. Private ownership means minimal public disclosure. Has been accused of deforestation, labor abuses, and contributing to farmer dependency through vertical integration.",
        "aliases": "Cargill, Incorporated",
        "metadata": {"type": "agribusiness / commodity trading", "founded": 1865},
    },
    {
        "name": "ADM",
        "entity_type": "organization",
        "description": "Archer Daniels Midland Company. One of the 'ABCD' grain traders dominating global food commodity markets. Convicted in the lysine price-fixing scandal (1996) — executives secretly met with competitors to fix prices of animal feed additives, costing farmers and consumers hundreds of millions. FBI informant Mark Whitacre recorded the meetings. ADM paid a $100 million fine. The scandal exposed cartel behavior at the heart of the global food supply chain.",
        "aliases": "Archer Daniels Midland, Archer-Daniels-Midland",
        "metadata": {"type": "agribusiness / commodity processing", "founded": 1902},
    },
    {
        "name": "Syngenta",
        "entity_type": "organization",
        "description": "Swiss-based agrochemical and seed company, formed from the merger of Novartis Agribusiness and Zeneca Agrochemicals (2000). Produces atrazine (the most commonly detected pesticide in U.S. water), neonicotinoids (linked to bee colony collapse), and patented seed varieties. Acquired by ChemChina (now Sinochem) for $43 billion in 2017 — making China's state-owned chemical company the owner of a major Western seed and pesticide company. Launched documented campaigns to discredit scientists whose research threatened product sales (Tyrone Hayes).",
        "aliases": "",
        "metadata": {"type": "agrochemical / seed company", "founded": 2000},
    },
    {
        "name": "Bayer",
        "entity_type": "organization",
        "description": "German multinational pharmaceutical and life sciences company. Acquired Monsanto for $63 billion in 2018, absorbing its seed technology, herbicide business, and legal liabilities. By 2024 had agreed to pay $10.9+ billion to settle Roundup cancer lawsuits — making the Monsanto acquisition one of the most disastrous corporate deals in history. The acquisition concentrated seed and pesticide power: Bayer-Monsanto controls ~25% of the world's seed supply and ~25% of the pesticide market.",
        "aliases": "Bayer AG, Bayer CropScience",
        "metadata": {"type": "pharmaceutical / agrochemical", "founded": 1863},
    },
    {
        "name": "USDA",
        "entity_type": "agency",
        "description": "United States Department of Agriculture. Tasked with both promoting and regulating American agriculture — a structural conflict of interest. Revolving door between USDA leadership and agribusiness (Monsanto, ADM, etc.) is documented by OpenSecrets. Co-patented terminator seed technology (GURT) with Delta and Pine Land Company (later acquired by Monsanto). Approved genetically modified crops whose long-term effects remain debated. Critics argue USDA functions as an arm of the agribusiness industry it ostensibly regulates.",
        "aliases": "U.S. Department of Agriculture",
        "metadata": {"type": "federal agency", "founded": 1862},
    },
    {
        "name": "Codex Alimentarius Commission",
        "entity_type": "organization",
        "description": "Joint body of the WHO and FAO that develops international food standards, guidelines, and codes of practice. Established in 1963. Its standards influence food regulation worldwide. Critics argue Codex is captured by corporate interests — industry representatives participate in standard-setting, and Codex standards sometimes override stricter national regulations (e.g., on pesticide residues, labeling). Proponents argue it harmonizes food safety globally.",
        "aliases": "Codex Alimentarius, Codex",
        "metadata": {"type": "international standards body", "founded": 1963},
    },
    # --- Events ---
    {
        "name": "Indian Farmer Suicides",
        "entity_type": "event",
        "description": "Over 300,000 Indian farmers have died by suicide since 1995, disproportionately in regions that adopted Bt cotton and other cash crops requiring purchased seeds and chemical inputs. Farmers trapped in debt cycles: expensive patented seeds require expensive pesticides, crop failure means no seed saving for next season. The connection between seed patents and suicides is debated — agrarian debt crisis has multiple causes — but the pattern is concentrated in regions of GMO adoption. Vandana Shiva and NYU's Center for Human Rights have documented the connection.",
        "aliases": "BT Cotton Farmer Suicides",
        "metadata": {"date_range": "1995-present", "location": "Maharashtra, Andhra Pradesh, India"},
    },
    {
        "name": "Terminator Seeds",
        "entity_type": "event",
        "description": "Genetic Use Restriction Technologies (GURT), nicknamed 'terminator seeds' by ETC Group (1998). Technology engineered to produce sterile seeds, forcing farmers to purchase new seeds every season rather than saving and replanting. Co-patented by the USDA and Delta and Pine Land Company (U.S. Patent 5,723,765, 1998). Global outcry led to a de facto moratorium under the Convention on Biological Diversity (2000). Monsanto acquired Delta and Pine Land (2007) and promised not to commercialize — but the technology and patents remain.",
        "aliases": "GURT, Genetic Use Restriction Technology, V-GURT",
        "metadata": {"date": "1998"},
    },
    {
        "name": "ADM Price-Fixing Scandal",
        "entity_type": "event",
        "description": "In 1992-1995, ADM executives participated in a global cartel fixing prices of lysine (animal feed additive) and citric acid. FBI informant Mark Whitacre secretly recorded meetings where ADM and competitors agreed on prices and market shares. ADM paid a $100 million criminal fine (1996). Three executives convicted. Whitacre himself was later convicted of embezzlement. The scandal revealed that major food commodity companies operated as price-fixing cartels. Basis for the film 'The Informant!' (2009).",
        "aliases": "ADM Lysine Price-Fixing",
        "metadata": {"date": "1992-1996"},
    },
    {
        "name": "Monsanto Papers",
        "entity_type": "event",
        "description": "Internal Monsanto documents revealed through Roundup/glyphosate cancer litigation discovery (2017+). Showed: Monsanto ghostwrote scientific papers published under academics' names, knew about glyphosate cancer risks and suppressed the evidence, orchestrated campaigns to discredit IARC's classification, and maintained a list of 'friendly' scientists to defend its products. Published by U.S. Right to Know and Le Monde. Led to $10.9B Bayer settlement.",
        "aliases": "",
        "metadata": {"date": "2017"},
    },
    {
        "name": "Roundup Cancer Litigation",
        "entity_type": "event",
        "description": "Wave of lawsuits against Monsanto/Bayer alleging glyphosate-based herbicide Roundup causes non-Hodgkin lymphoma. First trial (Johnson v. Monsanto, 2018) awarded $289M (reduced to $78M). IARC classified glyphosate as 'probably carcinogenic' (Group 2A) in 2015. Monsanto Papers revealed the company knew of cancer risks and suppressed evidence. Bayer agreed to $10.9 billion settlement (2020) covering ~100,000 claims. Ongoing litigation continues.",
        "aliases": "Roundup Lawsuits, Glyphosate Litigation",
        "metadata": {"date_range": "2015-present"},
    },
    # --- Legislation ---
    {
        "name": "Monsanto Protection Act",
        "entity_type": "legislation",
        "description": "Section 735 of H.R. 933 (2013), officially the 'Farmer Assurance Provision.' Anonymous rider (widely attributed to Sen. Roy Blunt, written with Monsanto's input) that stripped federal courts of the authority to halt the sale or planting of genetically modified seeds — even if a court found they posed health risks. Signed into law by Obama as part of a must-pass spending bill. Expired September 2013 after public outcry. Symbol of Monsanto's legislative capture.",
        "aliases": "Farmer Assurance Provision, Section 735",
        "metadata": {"signed": 2013, "expired": 2013},
    },
    {
        "name": "DARK Act",
        "entity_type": "legislation",
        "description": "S.764 — National Bioengineered Food Disclosure Standard (2016). Officially required GMO labeling but was nicknamed the 'Deny Americans the Right to Know' (DARK) Act because it preempted stronger state labeling laws (including Vermont's), allowed QR codes instead of clear labels, and excluded many GMO-derived products. Effectively made GMO labeling so weak as to be meaningless while blocking states from implementing real labeling requirements.",
        "aliases": "National Bioengineered Food Disclosure Standard, S.764",
        "metadata": {"signed": 2016},
    },
    {
        "name": "Plant Variety Protection Act",
        "entity_type": "legislation",
        "description": "U.S. federal law (1970) granting intellectual property protection to developers of new plant varieties. Extended patent-like protections to seeds. While intended to incentivize crop development, critics argue it began the legal framework that enabled corporations like Monsanto to control seeds through IP law — transforming a shared agricultural heritage into corporate property. The Act was a precursor to utility patents on GMOs (Diamond v. Chakrabarty, 1980) and plant patents.",
        "aliases": "PVPA",
        "metadata": {"signed": 1970},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Hugh Grant / Monsanto ---
    {
        "source": "Hugh Grant",
        "target": "Monsanto",
        "type": "directed",
        "tier": "documented",
        "desc": "CEO of Monsanto 2003-2018. Oversaw GMO expansion, Roundup defense, farmer litigation, and the $63B sale to Bayer. Led the company during the Monsanto Papers revelations.",
        "sources": [1268],
        "year_start": 2003,
        "year_end": 2018,
    },
    {
        "source": "Robert Fraley",
        "target": "Monsanto",
        "type": "worked_for",
        "tier": "documented",
        "desc": "CTO of Monsanto. Pioneered the plant transformation technology that enabled GMO crops. Received the 2013 World Food Prize, which critics viewed as industry self-legitimation.",
        "sources": [1269],
        "year_start": 1981,
        "year_end": 2018,
    },
    # --- Bayer / Monsanto ---
    {
        "source": "Bayer",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Acquired Monsanto for $63B in 2018. Absorbed Monsanto's seed technology, herbicide business, and $10.9B in Roundup cancer liabilities. The combined entity controls ~25% of global seed and pesticide markets.",
        "sources": [1270, 1287],
        "year_start": 2018,
        "year_end": None,
    },
    # --- Percy Schmeiser ---
    {
        "source": "Percy Schmeiser",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Sued by Monsanto for patent infringement. Supreme Court of Canada ruled Monsanto's patent valid (2004) but awarded no damages. Schmeiser maintained contamination was from wind-blown pollen. Became global symbol of farmer resistance to seed patents.",
        "sources": [1266, 1267],
        "year_start": 1998,
        "year_end": 2004,
    },
    # --- Tyrone Hayes / Syngenta ---
    {
        "source": "Tyrone Hayes",
        "target": "Syngenta",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Hayes published research showing Syngenta's atrazine causes hormonal disruption in frogs. Syngenta launched a documented campaign to discredit him: hired PR firms, funded counter-research, and pressured his university. Internal documents revealed in litigation.",
        "sources": [1264, 1265, 1289],
        "year_start": 2003,
        "year_end": None,
    },
    {
        "source": "Syngenta",
        "target": "Tyrone Hayes",
        "type": "suppressed_by",
        "tier": "documented",
        "desc": "Syngenta's internal documents (revealed in litigation) showed systematic efforts to discredit Hayes: PR campaigns, character attacks, funded counter-research, university pressure. One of the most documented cases of corporate suppression of science.",
        "sources": [1265, 1289],
        "year_start": 2003,
        "year_end": 2014,
    },
    # --- Syngenta / ChemChina ---
    {
        "source": "Syngenta",
        "target": "Codex Alimentarius Commission",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Syngenta and other agrochemical companies participate in Codex Alimentarius standard-setting processes. Industry influence on pesticide residue limits and food standards is documented by civil society organizations.",
        "sources": [1275, 1281],
        "year_start": 2000,
        "year_end": None,
    },
    # --- Cargill ---
    {
        "source": "Cargill",
        "target": "ADM",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Both are 'ABCD' grain traders dominating global food commodity markets. Together with Bunge and Dreyfus, they control the majority of global grain trade. Oxfam documented the concentration.",
        "sources": [1271, 1272, 1288],
        "year_start": 1960,
        "year_end": None,
    },
    {
        "source": "Cargill",
        "target": "USDA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Revolving door between Cargill and USDA is documented. USDA agricultural policy and subsidies directly benefit the grain trading oligopoly that Cargill leads.",
        "sources": [1271, 1272, 1282],
        "year_start": 1960,
        "year_end": None,
    },
    # --- ADM price-fixing ---
    {
        "source": "ADM",
        "target": "ADM Price-Fixing Scandal",
        "type": "connected_to",
        "tier": "documented",
        "desc": "ADM executives participated in a global lysine price-fixing cartel. $100M fine. Three executives convicted. FBI informant Mark Whitacre recorded the meetings. Revealed cartel behavior in food commodity markets.",
        "sources": [1273, 1274],
        "year_start": 1992,
        "year_end": 1996,
    },
    # --- Monsanto Papers / Roundup ---
    {
        "source": "Monsanto",
        "target": "Monsanto Papers",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Internal documents revealed through litigation showed Monsanto ghostwrote studies, suppressed cancer evidence, and maintained 'friendly scientist' lists to defend Roundup/glyphosate.",
        "sources": [1261, 1262],
        "year_start": 2017,
        "year_end": None,
    },
    {
        "source": "Monsanto Papers",
        "target": "Roundup Cancer Litigation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The Monsanto Papers were revealed through discovery in Roundup cancer lawsuits. Internal evidence of suppressed cancer data was key to jury verdicts and the $10.9B settlement.",
        "sources": [1261, 1262, 1287],
        "year_start": 2017,
        "year_end": None,
    },
    {
        "source": "Monsanto",
        "target": "Roundup Cancer Litigation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "~100,000 plaintiffs alleged Monsanto's Roundup caused non-Hodgkin lymphoma. First verdict (Johnson, 2018) awarded $289M. IARC classified glyphosate as 'probably carcinogenic' (2015). Bayer settled for $10.9B.",
        "sources": [1262, 1263, 1287],
        "year_start": 2015,
        "year_end": None,
    },
    {
        "source": "WHO",
        "target": "Roundup Cancer Litigation",
        "type": "connected_to",
        "tier": "documented",
        "desc": "IARC (a WHO agency) classified glyphosate as 'probably carcinogenic to humans' (Group 2A) in 2015. This classification was central to the Roundup cancer lawsuits.",
        "sources": [1263],
        "year_start": 2015,
        "year_end": 2015,
    },
    # --- Indian farmer suicides ---
    {
        "source": "Indian Farmer Suicides",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Indian farmer suicides concentrated in regions of Bt cotton adoption. Vandana Shiva and NYU documented the connection between patented seed dependency, debt cycles, and farmer deaths. Monsanto denies causation; the correlation is documented.",
        "sources": [1277, 1278],
        "year_start": 1995,
        "year_end": None,
    },
    {
        "source": "Vandana Shiva",
        "target": "Indian Farmer Suicides",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Shiva has been the most prominent voice connecting Indian farmer suicides to corporate seed control. Her Navdanya network promotes seed sovereignty as an alternative to patented dependency.",
        "sources": [1277, 1278, 1290],
        "year_start": 1991,
        "year_end": None,
    },
    # --- Terminator seeds ---
    {
        "source": "Terminator Seeds",
        "target": "USDA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "The USDA co-patented terminator seed technology (GURT) with Delta and Pine Land Company (U.S. Patent 5,723,765, 1998). A federal agency co-developed technology designed to eliminate farmers' ability to save seeds.",
        "sources": [1279, 1280],
        "year_start": 1998,
        "year_end": 1998,
    },
    {
        "source": "Terminator Seeds",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Monsanto acquired Delta and Pine Land (terminator patent co-holder) in 2007. Promised not to commercialize the technology but retained the patents. The capability exists even if uncommercialzied.",
        "sources": [1279, 1280],
        "year_start": 2007,
        "year_end": None,
    },
    # --- Legislation ---
    {
        "source": "Monsanto Protection Act",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Anonymous rider widely attributed to Sen. Roy Blunt, written with Monsanto's input. Stripped courts of authority to halt GMO planting even if found harmful. Signed 2013, expired same year after public outcry.",
        "sources": [1283],
        "year_start": 2013,
        "year_end": 2013,
    },
    {
        "source": "DARK Act",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The DARK Act preempted state GMO labeling laws (including Vermont's) with a federal standard so weak as to be meaningless. Lobbied for heavily by Monsanto and the Grocery Manufacturers Association.",
        "sources": [1284],
        "year_start": 2016,
        "year_end": None,
    },
    {
        "source": "Plant Variety Protection Act",
        "target": "USDA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "PVPA (1970) began the legal framework enabling corporate seed patents. USDA administers the Act. Critics trace the path from PVPA to utility patents on GMOs to Monsanto's farmer lawsuits.",
        "sources": [1285],
        "year_start": 1970,
        "year_end": None,
    },
    # --- USDA regulatory capture ---
    {
        "source": "USDA",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Revolving door between USDA and Monsanto is documented (OpenSecrets). Former Monsanto executives have held senior USDA positions. USDA approved Monsanto's GMO crops and co-patented terminator seeds.",
        "sources": [1282, 1280],
        "year_start": 1990,
        "year_end": None,
    },
    {
        "source": "USDA",
        "target": "FDA",
        "type": "connected_to",
        "tier": "documented",
        "desc": "USDA and FDA share food regulatory authority with overlapping and sometimes conflicting jurisdictions. Both agencies have revolving doors with the industries they regulate.",
        "sources": [1282],
        "year_start": 1862,
        "year_end": None,
    },
    # --- Codex Alimentarius ---
    {
        "source": "Codex Alimentarius Commission",
        "target": "WHO",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Codex is a joint WHO/FAO body. Its food standards influence global trade rules. Critics argue industry participation in standard-setting creates conflicts of interest.",
        "sources": [1281],
        "year_start": 1963,
        "year_end": None,
    },
    # --- Bill Gates farmland ---
    {
        "source": "Bill Gates",
        "target": "USDA",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Gates is the largest private farmland owner in the U.S. (~270,000 acres). His agricultural investments benefit from USDA subsidies and policies. Gates Foundation also funds agricultural technology research.",
        "sources": [1286],
        "year_start": 2013,
        "year_end": None,
    },
    {
        "source": "Bill Gates",
        "target": "Monsanto",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Gates Foundation has purchased Monsanto stock and funded agricultural biotechnology research aligned with Monsanto's GMO model. Gates' farmland holdings and ag-tech investments create convergent interests.",
        "sources": [1286],
        "year_start": 2010,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Hugh Grant": [1268],
    "Robert Fraley": [1269],
    "Percy Schmeiser": [1266, 1267],
    "Tyrone Hayes": [1264, 1265],
    "Cargill": [1271, 1272, 1288],
    "ADM": [1273, 1274, 1288],
    "Syngenta": [1275, 1276, 1289],
    "Bayer": [1270, 1287],
    "USDA": [1280, 1282, 1285],
    "Codex Alimentarius Commission": [1281],
    "Indian Farmer Suicides": [1277, 1278],
    "Terminator Seeds": [1279, 1280],
    "ADM Price-Fixing Scandal": [1273, 1274],
    "Monsanto Papers": [1261],
    "Roundup Cancer Litigation": [1261, 1262, 1263, 1287],
    "Monsanto Protection Act": [1283],
    "DARK Act": [1284],
    "Plant Variety Protection Act": [1285],
}
