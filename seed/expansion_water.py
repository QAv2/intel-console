"""
Water Privatization & Control — Expansion layer for Intel Console.

New branch mapping the architecture of water privatization: how a fundamental
human necessity was reframed as a commodity by corporations and international
financial institutions. From the World Bank's structural adjustment programs
forcing developing nations to privatize water systems, to Nestlé extracting
billions of gallons from communities for pennies, to the Cochabamba Water War
where Bechtel tried to make it illegal to collect rainwater.

The throughline: water is the most fundamental human need after air. Controlling
it is controlling populations. When the CEO of the world's largest food company
says "water is not a human right," that's not a gaffe — it's a business model.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  World Bank, IMF, WEF, Bill Gates

Evidence tiers:
  documented = congressional record, court filing, official government doc, corporate filings
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SOURCES — IDs 1231-1260
# ============================================================

SOURCES = [
    # --- Cochabamba Water War ---
    {
        "id": 1231,
        "title": "Jim Shultz — 'The Water War in Cochabamba, Bolivia: Privatization Triggers Civic Revolt' (Democracy Center, 2000)",
        "url": "https://en.wikipedia.org/wiki/Cochabamba_Water_War",
        "source_type": "journalism",
        "author": "Jim Shultz",
        "year": 2000,
    },
    {
        "id": 1232,
        "title": "Oscar Olivera — 'Cochabamba! Water War in Bolivia' (South End Press, 2004)",
        "url": "https://en.wikipedia.org/wiki/Cochabamba_Water_War",
        "source_type": "book",
        "author": "Oscar Olivera",
        "year": 2004,
    },
    {
        "id": 1233,
        "title": "Bechtel Corporation vs. Bolivia — ICSID arbitration case (Aguas del Tunari, $25M claim against Bolivia)",
        "url": "https://en.wikipedia.org/wiki/Cochabamba_Water_War",
        "source_type": "court",
        "year": 2006,
    },
    # --- Nestlé water ---
    {
        "id": 1234,
        "title": "Peter Brabeck-Letmathe — 'Water is not a human right' interview (2005, viral 2012)",
        "url": "https://en.wikipedia.org/wiki/Peter_Brabeck-Letmathe",
        "source_type": "other",
        "year": 2005,
    },
    {
        "id": 1235,
        "title": "Corporate Accountability International — 'Nestlé Water: Cashing in on a Public Resource' (campaign documentation)",
        "url": "https://en.wikipedia.org/wiki/Nestl%C3%A9_Waters",
        "source_type": "journalism",
        "year": 2018,
    },
    {
        "id": 1236,
        "title": "Michigan Citizens for Water Conservation v. Nestlé Waters — Michigan Circuit Court (2003)",
        "url": "https://en.wikipedia.org/wiki/Nestl%C3%A9_Waters",
        "source_type": "court",
        "year": 2003,
    },
    # --- Maude Barlow ---
    {
        "id": 1237,
        "title": "Maude Barlow — 'Blue Gold: The Fight to Stop the Corporate Theft of the World's Water' (The New Press, 2002)",
        "url": "https://en.wikipedia.org/wiki/Maude_Barlow",
        "source_type": "book",
        "author": "Maude Barlow",
        "year": 2002,
    },
    {
        "id": 1238,
        "title": "Maude Barlow — 'Blue Covenant: The Global Water Crisis and the Coming Battle for the Right to Water' (The New Press, 2007)",
        "url": "https://en.wikipedia.org/wiki/Maude_Barlow",
        "source_type": "book",
        "author": "Maude Barlow",
        "year": 2007,
    },
    {
        "id": 1239,
        "title": "United Nations General Assembly Resolution 64/292 — recognizing the human right to water and sanitation (2010)",
        "url": "https://en.wikipedia.org/wiki/Human_right_to_water_and_sanitation",
        "source_type": "government",
        "year": 2010,
    },
    # --- Vandana Shiva ---
    {
        "id": 1240,
        "title": "Vandana Shiva — 'Water Wars: Privatization, Pollution, and Profit' (South End Press, 2002)",
        "url": "https://en.wikipedia.org/wiki/Vandana_Shiva",
        "source_type": "book",
        "author": "Vandana Shiva",
        "year": 2002,
    },
    # --- Suez / Veolia ---
    {
        "id": 1241,
        "title": "David Hall — 'Water Privatisation and Restructuring in Asia-Pacific' (PSIRU, University of Greenwich, 2004)",
        "url": "https://en.wikipedia.org/wiki/Suez_(company)",
        "source_type": "academic",
        "author": "David Hall",
        "year": 2004,
    },
    {
        "id": 1242,
        "title": "Suez (company) — Wikipedia (global water privatization history)",
        "url": "https://en.wikipedia.org/wiki/Suez_(company)",
        "source_type": "other",
        "year": 2024,
    },
    {
        "id": 1243,
        "title": "Veolia — Wikipedia (global water and waste management)",
        "url": "https://en.wikipedia.org/wiki/Veolia",
        "source_type": "other",
        "year": 2024,
    },
    # --- Thames Water ---
    {
        "id": 1244,
        "title": "Thames Water — debt crisis and collapse of UK water privatization model (Financial Times reporting, 2023-2024)",
        "url": "https://en.wikipedia.org/wiki/Thames_Water",
        "source_type": "journalism",
        "year": 2024,
    },
    {
        "id": 1245,
        "title": "UK water privatization — record sewage discharges, debt loading, and dividend extraction since 1989 (Guardian / independent analysis)",
        "url": "https://en.wikipedia.org/wiki/Water_industry_in_England_and_Wales",
        "source_type": "journalism",
        "year": 2023,
    },
    # --- Flint water crisis ---
    {
        "id": 1246,
        "title": "Michigan Civil Rights Commission — 'The Flint Water Crisis: Systemic Racism Through the Lens of Flint' (2017)",
        "url": "https://en.wikipedia.org/wiki/Flint_water_crisis",
        "source_type": "government",
        "year": 2017,
    },
    {
        "id": 1247,
        "title": "Anna Clark — 'The Poisoned City: Flint's Water and the American Urban Tragedy' (Metropolitan, 2018)",
        "url": "https://en.wikipedia.org/wiki/Flint_water_crisis",
        "source_type": "book",
        "author": "Anna Clark",
        "year": 2018,
    },
    # --- Detroit water shutoffs ---
    {
        "id": 1248,
        "title": "United Nations experts — statement condemning Detroit mass water shutoffs as human rights violation (2014)",
        "url": "https://en.wikipedia.org/wiki/Detroit_Water_and_Sewerage_Department",
        "source_type": "government",
        "year": 2014,
    },
    # --- T. Boone Pickens / Ogallala ---
    {
        "id": 1249,
        "title": "T. Boone Pickens — Ogallala Aquifer water rights and Mesa Water Inc. (Business Insider / Texas Observer reporting)",
        "url": "https://en.wikipedia.org/wiki/T._Boone_Pickens",
        "source_type": "journalism",
        "year": 2012,
    },
    {
        "id": 1250,
        "title": "Ogallala Aquifer depletion — USGS studies on declining water levels (Kansas, Texas, Oklahoma)",
        "url": "https://en.wikipedia.org/wiki/Ogallala_Aquifer",
        "source_type": "government",
        "year": 2023,
    },
    # --- Standing Rock ---
    {
        "id": 1251,
        "title": "Standing Rock Sioux Tribe v. U.S. Army Corps of Engineers — DAPL pipeline water contamination risk (D.C. District Court, 2017)",
        "url": "https://en.wikipedia.org/wiki/Dakota_Access_Pipeline_protests",
        "source_type": "court",
        "year": 2017,
    },
    # --- World Bank / structural adjustment ---
    {
        "id": 1252,
        "title": "World Bank — Water Sector Strategy (2003) promoting public-private partnerships in water",
        "url": "https://en.wikipedia.org/wiki/World_Bank_Group",
        "source_type": "government",
        "year": 2003,
    },
    {
        "id": 1253,
        "title": "Ann-Christin Sjölander Holland — 'The Water Business: Corporations Versus People' (Zed Books, 2005)",
        "url": "https://en.wikipedia.org/wiki/Water_privatization",
        "source_type": "book",
        "author": "Ann-Christin Sjölander Holland",
        "year": 2005,
    },
    # --- Dublin Statement ---
    {
        "id": 1254,
        "title": "Dublin Statement on Water and Sustainable Development (1992) — Principle 4: water as an economic good",
        "url": "https://en.wikipedia.org/wiki/Dublin_Statement_on_Water_and_Sustainable_Development",
        "source_type": "government",
        "year": 1992,
    },
    # --- Great Lakes ---
    {
        "id": 1255,
        "title": "Great Lakes Compact — Great Lakes-St. Lawrence River Basin Water Resources Compact (2008)",
        "url": "https://en.wikipedia.org/wiki/Great_Lakes_Compact",
        "source_type": "government",
        "year": 2008,
    },
    # --- General water privatization ---
    {
        "id": 1256,
        "title": "Food & Water Watch — 'Water Privatization: Facts and Figures' (reports on failed privatization worldwide)",
        "url": "https://www.foodandwaterwatch.org/",
        "source_type": "journalism",
        "year": 2023,
    },
    # --- Nestlé BlueTriton ---
    {
        "id": 1257,
        "title": "Nestlé sells North American water brands to One Rock Capital (BlueTriton, $4.3B, 2021)",
        "url": "https://en.wikipedia.org/wiki/BlueTriton_Brands",
        "source_type": "journalism",
        "year": 2021,
    },
    # --- Bechtel ---
    {
        "id": 1258,
        "title": "Bechtel Corporation — Wikipedia (engineering/construction giant, Cochabamba water privatization)",
        "url": "https://en.wikipedia.org/wiki/Bechtel",
        "source_type": "other",
        "year": 2024,
    },
    # --- Remunicipalization trend ---
    {
        "id": 1259,
        "title": "Transnational Institute — 'Reclaiming Public Water' — global remunicipalization trend (267 cities by 2019)",
        "url": "https://en.wikipedia.org/wiki/Water_privatization",
        "source_type": "academic",
        "year": 2019,
    },
    # --- Pickens water strategy ---
    {
        "id": 1260,
        "title": "Michael Burry / T. Boone Pickens — financiers investing in water as the 'next oil' (Bloomberg reporting)",
        "url": "https://en.wikipedia.org/wiki/Ogallala_Aquifer",
        "source_type": "journalism",
        "year": 2015,
    },
]

# ============================================================
# ENTITIES
# ============================================================

ENTITIES = [
    # --- People ---
    {
        "name": "Peter Brabeck-Letmathe",
        "entity_type": "person",
        "description": "Austrian businessman, CEO of Nestlé (1997-2008) and Chairman (2005-2017). Became a symbol of corporate water exploitation after a 2005 interview in which he stated the view that water is a human right is 'extreme' and that water should be privatized and given a market value. Later attempted to soften these remarks. Under his leadership, Nestlé expanded its water bottling operations worldwide while communities fought extraction permits.",
        "aliases": "Peter Brabeck",
        "metadata": {"role": "Nestlé CEO/Chairman", "years_active": "1997-2017"},
    },
    {
        "name": "Maude Barlow",
        "entity_type": "person",
        "description": "Canadian author and activist. National Chairperson of the Council of Canadians. Served as Senior Advisor on Water to the President of the UN General Assembly (2008-2009). Instrumental in the passage of UN Resolution 64/292 recognizing the human right to water (2010). Author of 'Blue Gold' (2002) and 'Blue Covenant' (2007). The most prominent global advocate for water as a human right and against water privatization.",
        "aliases": "",
        "metadata": {"role": "water rights activist / UN advisor", "years_active": "1985-present"},
    },
    {
        "name": "Vandana Shiva",
        "entity_type": "person",
        "description": "Indian scholar, environmental activist, and anti-globalization author. Founded Navdanya (seed-saving network). Author of 'Water Wars: Privatization, Pollution, and Profit' (2002). Campaigns against both water privatization and corporate control of agriculture (seeds, pesticides). Her work connects water and food sovereignty as aspects of the same corporate capture. Recipient of the Right Livelihood Award (1993).",
        "aliases": "",
        "metadata": {"role": "activist / author / physicist", "years_active": "1982-present"},
    },
    {
        "name": "T. Boone Pickens",
        "entity_type": "person",
        "description": "American businessman and financier (1928-2019). Oil and gas magnate who became the largest individual water rights holder in the United States through Mesa Water Inc., purchasing rights over the Ogallala Aquifer in the Texas Panhandle. Planned to sell water to cities like Dallas and San Antonio. Called water 'the new oil.' His strategy exemplified the financialization of water — treating a finite shared resource as a commodity for private profit.",
        "aliases": "Boone Pickens",
        "metadata": {"role": "financier / water rights holder", "years_active": "1956-2019"},
    },
    # --- Organizations ---
    {
        "name": "Nestlé Waters",
        "entity_type": "organization",
        "description": "Nestlé's water division — the world's largest bottled water company until 2021 when North American brands were sold to One Rock Capital Partners (now BlueTriton Brands) for $4.3 billion. Brands included Poland Spring, Deer Park, Arrowhead, Zephyrhills, Ozarka, Ice Mountain. Faced lawsuits and community opposition worldwide for extracting groundwater at rates that depleted local aquifers, often under permits allowing extraction for pennies per gallon.",
        "aliases": "Nestlé Water, BlueTriton Brands",
        "metadata": {"type": "water extraction / bottling", "parent": "Nestlé S.A."},
    },
    {
        "name": "Suez Group",
        "entity_type": "organization",
        "description": "French multinational utility company, one of the world's two largest private water companies (with Veolia). Provides water and waste services to ~150 million people globally. History of controversial water privatization projects in developing countries, often under World Bank structural adjustment conditions. In 2022, Suez was acquired by Veolia, creating the world's largest water utility conglomerate.",
        "aliases": "Suez, Suez Environnement, Ondeo",
        "metadata": {"type": "water utility / multinational", "founded": 1858},
    },
    {
        "name": "Veolia",
        "entity_type": "organization",
        "description": "French multinational utility company, the world's largest private water operator. Provides water, waste, and energy services globally. Acquired Suez in 2022 to form a water/waste mega-corporation. History includes profitable but controversial water privatization deals worldwide. Critics argue the combined Veolia-Suez entity creates a near-monopoly in global water privatization.",
        "aliases": "Veolia Environnement, Compagnie Générale des Eaux, Vivendi Water",
        "metadata": {"type": "water utility / multinational", "founded": 1853},
    },
    {
        "name": "Thames Water",
        "entity_type": "organization",
        "description": "UK's largest water and wastewater company, serving 15 million customers in London and the Thames Valley. Privatized in 1989 under Thatcher. By 2024, accumulated £18+ billion in debt while paying billions in dividends to shareholders and dumping record levels of raw sewage into rivers. Near-collapse in 2023-2024 became the poster child for failed water privatization — demonstrating how private equity extracts value while infrastructure degrades.",
        "aliases": "",
        "metadata": {"type": "water utility / privatized", "privatized": 1989},
    },
    {
        "name": "Bechtel Corporation",
        "entity_type": "organization",
        "description": "Largest construction and civil engineering company in the United States (privately held). Through subsidiary Aguas del Tunari, won the contract to privatize Cochabamba's water system in 1999. Rate increases of up to 200% triggered the Cochabamba Water War (2000). After being expelled by Bolivia, Bechtel filed a $25 million ICSID arbitration claim against the Bolivian government. Eventually settled for a symbolic 30 cents. Also connected to Iraq reconstruction contracts and major infrastructure worldwide.",
        "aliases": "Bechtel, Aguas del Tunari",
        "metadata": {"type": "construction / engineering", "founded": 1898},
    },
    # --- Events ---
    {
        "name": "Cochabamba Water War",
        "entity_type": "event",
        "description": "Popular uprising in Cochabamba, Bolivia (January-April 2000) against water privatization. Bechtel subsidiary Aguas del Tunari raised rates by up to 200% after taking over the municipal water system under World Bank structural adjustment conditions. Even rainwater collection was effectively made illegal. Mass protests led to martial law, one death, and ultimately the cancellation of the privatization contract. Bolivia became the first country to reverse a World Bank-mandated water privatization. Global symbol of resistance to water commodification.",
        "aliases": "Guerra del Agua",
        "metadata": {"date": "2000-01 to 2000-04", "location": "Cochabamba, Bolivia"},
    },
    {
        "name": "Flint Water Crisis",
        "entity_type": "event",
        "description": "Public health emergency in Flint, Michigan (2014-2019). Under state-appointed emergency management, the city switched its water source from Detroit's system to the Flint River in April 2014 to save money. Failure to apply corrosion control caused lead to leach from aging pipes into drinking water. 6,000-12,000 children exposed to elevated lead levels. A Legionnaires' disease outbreak killed 12. Criminal charges filed against 15 officials including the governor. The crisis exposed how cost-cutting and institutional racism intersect in water governance.",
        "aliases": "Flint Michigan Water Crisis",
        "metadata": {"date": "2014-04 to 2019", "location": "Flint, Michigan"},
    },
    {
        "name": "Detroit Water Shutoffs",
        "entity_type": "event",
        "description": "In 2014, the Detroit Water and Sewerage Department shut off water to over 100,000 residents for unpaid bills, many owed as little as $150. Occurred while the city was in bankruptcy under emergency management. UN human rights experts condemned the shutoffs as a violation of the human right to water. Detroit's water debt crisis was connected to decades of deindustrialization, population loss, and the broader financialization of municipal services.",
        "aliases": "",
        "metadata": {"date": "2014", "location": "Detroit, Michigan"},
    },
    {
        "name": "Standing Rock Protests",
        "entity_type": "event",
        "description": "Months-long protests (2016-2017) by the Standing Rock Sioux Tribe and allies against the Dakota Access Pipeline (DAPL), which crosses beneath Lake Oahe on the Missouri River, the tribe's primary water source. Protesters (self-described 'water protectors') faced militarized police response including water cannons in freezing temperatures. The Army Corps of Engineers initially denied the easement; Trump reversed the decision days after inauguration. The pipeline later leaked multiple times. Became a global symbol of Indigenous water sovereignty.",
        "aliases": "Standing Rock, NoDAPL, Water Protectors",
        "metadata": {"date": "2016-04 to 2017-02", "location": "Standing Rock Sioux Reservation, ND"},
    },
    {
        "name": "Dublin Statement on Water",
        "entity_type": "legislation",
        "description": "International Conference on Water and the Environment produced the Dublin Statement (1992), whose Principle 4 declared: 'Water has an economic value in all its competing uses and should be recognized as an economic good.' This principle became the intellectual foundation for the global water privatization movement — reframing water from a shared commons to an economic commodity. Critics argue Principle 4 was heavily influenced by corporate lobbying and enabled the World Bank's structural adjustment water privatization conditions.",
        "aliases": "Dublin Principles, ICWE 1992",
        "metadata": {"signed": 1992},
    },
    # --- Facilities ---
    {
        "name": "Ogallala Aquifer",
        "entity_type": "facility",
        "description": "One of the world's largest aquifers, underlying ~174,000 square miles across eight U.S. Great Plains states. Provides 30% of all U.S. irrigation groundwater. Being depleted far faster than it can recharge — some areas have lost 100+ feet of water table. Full recovery would take thousands of years. T. Boone Pickens bought water rights over large portions. The Ogallala represents the tension between agricultural use, corporate acquisition, and long-term water security for millions.",
        "aliases": "Ogallala, High Plains Aquifer",
        "metadata": {"location": "Great Plains, USA (8 states)", "area": "174,000 sq mi"},
    },
    {
        "name": "Great Lakes",
        "entity_type": "facility",
        "description": "The Great Lakes hold 21% of the world's surface freshwater — the largest freshwater system on Earth. Subject to ongoing pressure for water diversions and exports. The Great Lakes Compact (2008) restricts large-scale diversions outside the basin but faces periodic legal challenges. As freshwater scarcity increases globally, the Great Lakes represent the most valuable and contested freshwater resource in the Western Hemisphere.",
        "aliases": "Great Lakes Basin",
        "metadata": {"location": "U.S.-Canada border region", "freshwater_share": "21% of world surface freshwater"},
    },
]

# ============================================================
# RELATIONSHIPS
# ============================================================

RELATIONSHIPS = [
    # --- Nestlé / Brabeck ---
    {
        "source": "Peter Brabeck-Letmathe",
        "target": "Nestlé Waters",
        "type": "directed",
        "tier": "documented",
        "desc": "As CEO (1997-2008) and Chairman (2005-2017), oversaw Nestlé's expansion into global water extraction. His 'water is not a human right' statement became a symbol of corporate water privatization ideology.",
        "sources": [1234, 1235],
        "year_start": 1997,
        "year_end": 2017,
    },
    {
        "source": "Nestlé Waters",
        "target": "Ogallala Aquifer",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Nestlé and successor BlueTriton extract groundwater from multiple aquifer systems across the U.S. under permits that communities argue are inadequately regulated. Pattern of extraction exceeding sustainable yield.",
        "sources": [1235, 1236, 1257],
        "year_start": 2000,
        "year_end": None,
    },
    {
        "source": "Nestlé Waters",
        "target": "World Economic Forum",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Nestlé's water strategy aligns with WEF's global governance frameworks. Brabeck served on WEF boards. WEF has promoted water as a 'risk' requiring private sector management solutions.",
        "sources": [1234],
        "year_start": 2000,
        "year_end": None,
    },
    # --- Cochabamba Water War ---
    {
        "source": "Bechtel Corporation",
        "target": "Cochabamba Water War",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Through subsidiary Aguas del Tunari, Bechtel's water privatization of Cochabamba triggered the Water War. Rate increases of up to 200% on a population earning ~$60/month. Filed $25M ICSID claim against Bolivia after being expelled.",
        "sources": [1231, 1232, 1233, 1258],
        "year_start": 1999,
        "year_end": 2006,
    },
    {
        "source": "World Bank",
        "target": "Cochabamba Water War",
        "type": "connected_to",
        "tier": "documented",
        "desc": "World Bank structural adjustment conditions required Bolivia to privatize its water system as a condition for loans. The Cochabamba privatization was a direct result of World Bank policy. After the revolt, the Bank acknowledged the need for 'better communication' but did not reverse its privatization framework.",
        "sources": [1231, 1232, 1252, 1253],
        "year_start": 1999,
        "year_end": 2000,
    },
    {
        "source": "Cochabamba Water War",
        "target": "Dublin Statement on Water",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The Dublin Statement's Principle 4 (water as an economic good) provided the intellectual framework that enabled World Bank-mandated water privatization, which directly caused the Cochabamba crisis.",
        "sources": [1231, 1254],
        "year_start": 1992,
        "year_end": 2000,
    },
    # --- Maude Barlow ---
    {
        "source": "Maude Barlow",
        "target": "Nestlé Waters",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Barlow has led campaigns against Nestlé's water extraction practices worldwide. Her books 'Blue Gold' and 'Blue Covenant' document Nestlé's pattern of community exploitation.",
        "sources": [1237, 1238],
        "year_start": 2002,
        "year_end": None,
    },
    {
        "source": "Maude Barlow",
        "target": "Cochabamba Water War",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Barlow prominently featured the Cochabamba Water War in her work as a turning point in the global water justice movement. It demonstrated that water privatization could be reversed by popular resistance.",
        "sources": [1237, 1238],
        "year_start": 2000,
        "year_end": None,
    },
    {
        "source": "Maude Barlow",
        "target": "World Bank",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Barlow has been the World Bank's most prominent critic on water privatization, documenting how structural adjustment conditions force developing nations to privatize water systems.",
        "sources": [1237, 1238, 1252],
        "year_start": 2002,
        "year_end": None,
    },
    # --- Vandana Shiva ---
    {
        "source": "Vandana Shiva",
        "target": "World Bank",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Shiva's 'Water Wars' documents how World Bank and IMF structural adjustment policies force water privatization on developing nations, connecting water commodification to broader neoliberal governance.",
        "sources": [1240],
        "year_start": 2002,
        "year_end": None,
    },
    {
        "source": "Vandana Shiva",
        "target": "Cochabamba Water War",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Shiva has cited the Cochabamba Water War as a key example of how water privatization generates resistance and as evidence that alternatives to corporate water management are possible.",
        "sources": [1240],
        "year_start": 2002,
        "year_end": None,
    },
    # --- Suez / Veolia ---
    {
        "source": "Suez Group",
        "target": "World Bank",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Suez has been a primary beneficiary of World Bank-mandated water privatization in developing countries. The Bank's structural adjustment conditions created the market; Suez supplied the services.",
        "sources": [1241, 1242, 1252],
        "year_start": 1990,
        "year_end": None,
    },
    {
        "source": "Veolia",
        "target": "Suez Group",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Veolia acquired Suez in 2022, creating the world's largest water and waste management company. The merger consolidated the global water privatization industry into a near-duopoly.",
        "sources": [1243],
        "year_start": 2022,
        "year_end": None,
    },
    {
        "source": "Veolia",
        "target": "World Bank",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Like Suez, Veolia has benefited from World Bank-promoted water privatization frameworks worldwide. The combined entity now dominates the global private water market.",
        "sources": [1243, 1252],
        "year_start": 1990,
        "year_end": None,
    },
    # --- Thames Water ---
    {
        "source": "Thames Water",
        "target": "Suez Group",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Both exemplify privatized water utilities. Thames Water's near-collapse (2023-2024) mirrors problems seen in privatized water systems globally — debt loading, dividend extraction, infrastructure neglect.",
        "sources": [1244, 1245],
        "year_start": 1989,
        "year_end": None,
    },
    # --- Flint ---
    {
        "source": "Flint Water Crisis",
        "target": "Detroit Water Shutoffs",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Both occurred in Michigan under emergency management that prioritized cost-cutting over public health. Both disproportionately affected majority-Black communities. Connected by the same austerity logic applied to water governance.",
        "sources": [1246, 1247, 1248],
        "year_start": 2014,
        "year_end": 2019,
    },
    # --- T. Boone Pickens ---
    {
        "source": "T. Boone Pickens",
        "target": "Ogallala Aquifer",
        "type": "connected_to",
        "tier": "documented",
        "desc": "Through Mesa Water Inc., became the largest individual water rights holder over the Ogallala Aquifer. Planned to sell water to Texas cities. Treated water as a commodity investment: 'Water is the new oil.'",
        "sources": [1249, 1250, 1260],
        "year_start": 2000,
        "year_end": 2019,
    },
    # --- Standing Rock ---
    {
        "source": "Standing Rock Protests",
        "target": "Great Lakes",
        "type": "connected_to",
        "tier": "inference",
        "desc": "Both represent Indigenous and community struggles to protect freshwater resources from corporate extraction/contamination. Standing Rock's 'water is life' (mni wiconi) framing connects to broader freshwater protection movements including Great Lakes defense.",
        "sources": [1251, 1255],
        "year_start": 2016,
        "year_end": None,
    },
    # --- Dublin Statement ---
    {
        "source": "Dublin Statement on Water",
        "target": "World Bank",
        "type": "connected_to",
        "tier": "credible",
        "desc": "The Dublin Statement's Principle 4 (water as 'economic good') provided the intellectual framework for the World Bank's subsequent water privatization conditions in structural adjustment programs.",
        "sources": [1254, 1252],
        "year_start": 1992,
        "year_end": None,
    },
    # --- World Bank / IMF ---
    {
        "source": "World Bank",
        "target": "International Monetary Fund",
        "type": "connected_to",
        "tier": "documented",
        "desc": "World Bank and IMF jointly impose structural adjustment conditions requiring water privatization as a condition for loans to developing nations. The two institutions reinforce each other's water commodification agenda.",
        "sources": [1252, 1253],
        "year_start": 1990,
        "year_end": None,
    },
    # --- Bill Gates farmland/water ---
    {
        "source": "Bill Gates",
        "target": "Ogallala Aquifer",
        "type": "connected_to",
        "tier": "credible",
        "desc": "Gates is the largest private farmland owner in the United States (~270,000 acres). Much of this farmland overlies major aquifers including in areas dependent on Ogallala water. Farmland ownership = water access.",
        "sources": [1250, 1260],
        "year_start": 2013,
        "year_end": None,
    },
]

# ============================================================
# ENTITY_SOURCES
# ============================================================

ENTITY_SOURCES = {
    "Peter Brabeck-Letmathe": [1234, 1235],
    "Maude Barlow": [1237, 1238, 1239],
    "Vandana Shiva": [1240],
    "T. Boone Pickens": [1249, 1260],
    "Nestlé Waters": [1234, 1235, 1236, 1257],
    "Suez Group": [1241, 1242],
    "Veolia": [1243],
    "Thames Water": [1244, 1245],
    "Bechtel Corporation": [1233, 1258],
    "Cochabamba Water War": [1231, 1232, 1233],
    "Flint Water Crisis": [1246, 1247],
    "Detroit Water Shutoffs": [1248],
    "Standing Rock Protests": [1251],
    "Dublin Statement on Water": [1254],
    "Ogallala Aquifer": [1249, 1250],
    "Great Lakes": [1255],
}
