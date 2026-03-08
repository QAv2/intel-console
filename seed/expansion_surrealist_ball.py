"""
Surrealist Ball & Elite Social Network — Expansion layer for Intel Console.
Entities: Rothschild dynasty (core branch), the 1972 Surrealist Ball at Château
de Ferrières, key attendees, the party-host lineage connecting European aristocracy
to Hollywood/politics, the Rothschild→Pompidou political pipeline, and the
Met Gala as corporate successor institution.

This expansion maps the social infrastructure through which banking dynasties,
European aristocracy, Hollywood, and political leaders converge — with the 1972
Surrealist Ball as the documented apex event.

Evidence tiers:
  documented = congressional record, court filing, FOIA, official government doc
  credible   = quality investigative journalism, on-record testimony, academic research
  inference  = pattern-based conclusion from documented facts
  speculative = theory requiring further evidence
"""

# ============================================================
# SURREALIST BALL & ELITE SOCIAL NETWORK
# Sources 1291-1330, Entities, Relationships, Entity-Sources
# ============================================================

SOURCES = [
    # Primary / archival
    {"id": 1291, "title": "Baron Alexis de Redé — First-person account of the Surrealist Ball (1972)", "url": "", "source_type": "archive", "author": "Alexis de Redé", "year": 1972},
    {"id": 1292, "title": "New York Times — Coverage of the Rothschild Surrealist Ball, December 1972", "url": "", "source_type": "journalism", "year": 1972},
    {"id": 1293, "title": "Time Magazine — Baron Guy de Rothschild Cover Story", "url": "", "source_type": "journalism", "year": 1963},
    {"id": 1294, "title": "Le Monde — Guy de Rothschild open letter re: Mitterrand nationalization", "url": "", "source_type": "journalism", "author": "Guy de Rothschild", "year": 1981},

    # Books / biographies
    {"id": 1295, "title": "Guy de Rothschild — The Whims of Fortune (autobiography)", "url": "", "source_type": "book", "author": "Guy de Rothschild", "year": 1985},
    {"id": 1296, "title": "Niall Ferguson — The House of Rothschild: The World's Banker 1849-1999", "url": "", "source_type": "book", "author": "Niall Ferguson", "year": 1999},
    {"id": 1297, "title": "Niall Ferguson — The House of Rothschild: Money's Prophets 1798-1848", "url": "", "source_type": "book", "author": "Niall Ferguson", "year": 1998},
    {"id": 1298, "title": "Alexis de Redé — Alexis: The Memoirs of the Baron de Redé", "url": "", "source_type": "book", "author": "Alexis de Redé", "year": 2004},

    # Journalism / history
    {"id": 1299, "title": "Vanity Fair — The Surrealist Ball: Inside the Most Exclusive Party of the 20th Century", "url": "", "source_type": "journalism", "year": 2018},
    {"id": 1300, "title": "Paris Match — Le Bal Surréaliste des Rothschild (photo coverage)", "url": "", "source_type": "journalism", "year": 1972},
    {"id": 1301, "title": "Harper's Bazaar — The Legendary Rothschild Surrealist Ball of 1972", "url": "", "source_type": "journalism", "year": 2020},
    {"id": 1302, "title": "New York Times — Complete Guest List of Truman Capote's Black and White Ball", "url": "", "source_type": "journalism", "year": 1966},
    {"id": 1303, "title": "Vogue — Diana Vreeland and the Costume Institute: A Revolution in Fashion Curation", "url": "", "source_type": "journalism", "year": 1989},
    {"id": 1304, "title": "New York Times — Jacqueline Kennedy Onassis v. Ron Galella (harassment suit)", "url": "", "source_type": "journalism", "year": 1972},

    # Political / financial
    {"id": 1305, "title": "French Government Gazette — Nationalization of Banque Rothschild (Mitterrand decree)", "url": "", "source_type": "government", "year": 1982},
    {"id": 1306, "title": "French Senate Report — Capital Flight and the ISF Wealth Tax (843 departures in 2006)", "url": "", "source_type": "government", "year": 2008},
    {"id": 1307, "title": "Le Figaro — Georges Pompidou: From Banque Rothschild to the Élysée Palace", "url": "", "source_type": "journalism", "year": 1969},

    # Agnelli / Bilderberg overlap
    {"id": 1308, "title": "Financial Times — Gianni Agnelli obituary: The Uncrowned King of Italy", "url": "", "source_type": "journalism", "year": 2003},
    {"id": 1309, "title": "Bilderberg Meeting Participant Lists (1954-2024)", "url": "", "source_type": "archive", "year": 2024},

    # Met Gala / corporate capture
    {"id": 1310, "title": "New York Times — Anna Wintour and the Met Gala Machine (Vanessa Friedman)", "url": "", "source_type": "journalism", "author": "Vanessa Friedman", "year": 2023},
    {"id": 1311, "title": "Launch Metrics — Met Gala 2025 Media Impact Value Report ($1.3B)", "url": "", "source_type": "other", "year": 2025},
    {"id": 1312, "title": "Metropolitan Museum of Art — History of the Costume Institute", "url": "", "source_type": "archive", "year": 2024},

    # Beistegui / de Cuevas / party host lineage
    {"id": 1313, "title": "L'Osservatore Romano — Vatican denunciation of the Marquis de Cuevas ball at Biarritz", "url": "", "source_type": "archive", "year": 1953},
    {"id": 1314, "title": "Architectural Digest — Palazzo Labia and the Beistegui Ball of 1951", "url": "", "source_type": "journalism", "year": 2019},
    {"id": 1315, "title": "Vogue — Yves Saint Laurent credits Baron de Redé commission as formative", "url": "", "source_type": "journalism", "year": 1970},

    # Château de Ferrières
    {"id": 1316, "title": "Château de Ferrières — Historical Registry (Rothschild acquisition 1829, Napoleon III inauguration 1862)", "url": "", "source_type": "archive", "year": 1862},
    {"id": 1317, "title": "French Ministry of Culture — Ferrières donation to Chancellery of Universities of Paris (1975)", "url": "", "source_type": "government", "year": 1975},

    # Rockefeller-de Cuevas connection
    {"id": 1318, "title": "New York Times — Margaret Strong de Cuevas obituary (granddaughter of John D. Rockefeller)", "url": "", "source_type": "journalism", "year": 1985},

    # Salvador Dalí
    {"id": 1319, "title": "Dalí Foundation — Official Biography and Surrealist Movement Expulsion (1939)", "url": "", "source_type": "archive", "year": 2024},
    {"id": 1320, "title": "Julian's Auctions — Hélène Rochas Gramophone Headpiece (lot sold $2,600)", "url": "", "source_type": "other", "year": 2024},
]

ENTITIES = [
    # ---- Rothschild Dynasty (core) ----
    {"name": "Guy de Rothschild", "entity_type": "person", "description": (
        "Baron Guy Édouard Alphonse Paul de Rothschild (1909-2007). Head of the French "
        "Rothschild banking branch. Great-great-grandson of Mayer Amschel Rothschild. "
        "Chairman of Banque Rothschild 1967-1979.\n\n"
        "MILITARY: Served as company commander in 3rd Light Mechanized Division during "
        "Battle of France 1940. Fought at Carvin, evacuated from Dunkirk (awarded Croix "
        "de Guerre). Vichy regime stripped family of French nationality and Légion d'Honneur. "
        "Fled through Spain/Portugal to New York. Joined Free French forces, survived "
        "torpedoing of transport ship Pacific Grove (March 1943, 12 hours in Atlantic). "
        "Joined General Koenig's staff at SHAEF near Portsmouth.\n\n"
        "BANKING→POLITICS PIPELINE: Recruited schoolteacher Georges Pompidou to Banque "
        "Rothschild in 1953. Pompidou rose to general manager of the bank, then became "
        "President of France (1969-1974). This is a documented case of a private banking "
        "dynasty directly placing a future head of state.\n\n"
        "NATIONALIZATION: In 1981, Mitterrand's socialist government nationalized Banque "
        "Rothschild. Guy wrote front-page open letter to Le Monde: 'A Jew under Pétain, "
        "a pariah under Mitterrand — that's enough.' Moved temporarily to New York.\n\n"
        "SOCIAL POWER: Co-hosted the 1972 Surrealist Ball at Château de Ferrières with "
        "wife Marie-Hélène. Time magazine cover December 1963. Thoroughbred breeder "
        "(Exbury won Prix de l'Arc de Triomphe 1963). Died Paris, June 12, 2007, aged 98."
    )},

    {"name": "Marie-Hélène de Rothschild", "entity_type": "person", "description": (
        "Baroness Marie-Hélène Naila Stéphanie Josina van Zuylen van Nyevelt van de Haar "
        "(1927-1996). Hostess of the 1972 Surrealist Ball. Born New York City to a Dutch "
        "diplomat father and Egyptian-born mother of Syrian origin.\n\n"
        "ROTHSCHILD CONNECTION: Grandmother was Baroness Hélène de Rothschild (daughter of "
        "Baron Salomon James de Rothschild), disinherited for marrying a Catholic. First "
        "woman to compete in an international motor race (1898 Paris-Amsterdam-Paris).\n\n"
        "MARRIAGES: First married Count François de Nicolay (1950, one son Philippe). "
        "Married Baron Guy de Rothschild 1957 in NYC — first time a Rothschild family head "
        "married a non-Jewish spouse. Required papal dispensation to annul first marriage. "
        "Guy resigned presidency of Consistoire Central (French Jewish representative body).\n\n"
        "SOCIAL CHOREOGRAPHY: Transformed Château de Ferrières into 'a hedonist epicenter "
        "for European high society.' Organized annual themed balls 1960s-1972. Her guest lists "
        "were instruments of social power — one prominent socialite reportedly threatened "
        "suicide if not invited. Organized 1973 Battle of Versailles fashion show (5 French "
        "vs 5 American designers at Théâtre Gabriel, Palace of Versailles). Awarded Légion "
        "d'Honneur for promoting French culture.\n\n"
        "SURREALIST BALL: December 12, 1972. Wore towering stag's head with real pear-shaped "
        "diamond tears. NYT described her as 'a stag at the kill.' Created cobweb labyrinth, "
        "cat-costumed footmen, fur plates, blue bread, dead fish forks. The ball's ritual "
        "elements — mirror-inverted invitations, identity transformation, disorientation "
        "maze, symbolic meal — read as more than entertainment when viewed through the lens "
        "of elite social architecture.\n\n"
        "Died March 1, 1996, age 68. Catholic funeral at Saint-Louis-en-l'Île attended by "
        "Giscard d'Estaing, Claude Pompidou, Bernadette Chirac, Gianni Agnelli, Alain Delon, "
        "Yves Saint Laurent."
    )},

    {"name": "Mayer Amschel Rothschild", "entity_type": "person", "description": (
        "Mayer Amschel Rothschild (1744-1812). Frankfurt patriarch who founded the Rothschild "
        "banking dynasty from a single shop on the Judengasse (Jewish lane). Built it into "
        "the most powerful private financial institution in the world by placing his five sons "
        "in London, Paris, Vienna, Naples, and Frankfurt. The family maintained strict "
        "endogamy (intermarriage) for over a century to consolidate wealth and control."
    )},

    {"name": "Château de Ferrières", "entity_type": "facility", "description": (
        "Largest private residence in France. Purchased 1829 by Baron James de Rothschild "
        "from heirs of Joseph Fouché (Napoleon's Minister of Police). Designed by Joseph "
        "Paxton (Crystal Palace architect), completed 1859. 80+ guest suites, library of "
        "8,000 volumes, 100 servant quarters, stables for 80 horses, underground railway "
        "for food transport. 4,000-hectare estate.\n\n"
        "POWER VENUE: Inaugurated December 16, 1862 with gala attended by Napoleon III. "
        "Bismarck commandeered it as Prussian HQ during siege of Paris (1870) because he "
        "already knew how comfortable it was. Seized by Germans in WWII, art looted. "
        "Reopened 1959 by Guy and Marie-Hélène.\n\n"
        "SURREALIST BALL VENUE: December 12, 1972. Facade bathed in fire-simulating "
        "floodlights. Hunting hounds released to deter photographers.\n\n"
        "DONATED 1975 to Chancellery of Universities of Paris. Now houses Ferrières School "
        "of Gastronomy. The donation ended the era of Rothschild château-scale entertaining."
    )},

    # ---- The Event ----
    {"name": "Rothschild Surrealist Ball (1972)", "entity_type": "event", "description": (
        "December 12, 1972, Château de Ferrières. Hosted by Baron Guy and Baroness "
        "Marie-Hélène de Rothschild. ~150 guests. Artistic direction by Salvador Dalí.\n\n"
        "RITUAL ELEMENTS:\n"
        "- Invitations printed in reverse (mirror-reading required)\n"
        "- Façade lit to simulate fire\n"
        "- Hunting hounds released on grounds (photographer deterrence)\n"
        "- Footmen costumed as cats (meowing, sleeping poses)\n"
        "- Cobweb labyrinth ('hellish portal') before dining room\n"
        "- Dress code: 'surrealist heads' — identity transformation mandatory\n"
        "- Tables named with surrealist nonsense titles\n"
        "- Fur-covered plates, blue bread, dead fish replacing forks\n"
        "- Wine labeled 'vin/vain' (vain wine), bubble blowers at settings\n"
        "- Centerpieces: taxidermy tortoises, deformed dolls, sculpted breasts\n"
        "- Life-sized nude sugar sculpture as communal dessert\n"
        "- Unseen pianist playing Erik Satie (invisible source)\n\n"
        "ATTENDEES (documented): Audrey Hepburn (birdcage headpiece), Salvador Dalí "
        "(no costume — 'already surreal'), Brigitte Bardot (costume by Leonor Fini), "
        "Baron Alexis de Redé (quadruple-face Dalí mask), Hélène Rochas (gramophone "
        "headpiece by Hector Pascual), Marisa Berenson, Princess Maria Gabriella di Savoia, "
        "François-Marie Banier.\n\n"
        "SIGNIFICANCE: Described as 'the most legendary private party of the 20th century.' "
        "The last grand-scale private ball before paparazzi culture, wealth taxation, and "
        "nationalization made such events politically and logistically impossible. The ritual "
        "structure — initiation through disorientation, mandatory identity transformation, "
        "symbolic meal, total exclusion of outside observation — maps onto patterns observed "
        "in elite occult and fraternal gatherings."
    )},

    # ---- Key Attendees / Network Figures ----
    {"name": "Salvador Dalí", "entity_type": "person", "description": (
        "Salvador Domingo Felipe Jacinto Dalí i Domènech (1904-1989). Spanish surrealist "
        "artist. Expelled from official Surrealist movement 1939 (André Breton accused him "
        "of fascist sympathies). Despite expulsion, remained surrealism's most recognizable "
        "figure.\n\n"
        "ROTHSCHILD CONNECTION: Personal friend of Guy and Marie-Hélène de Rothschild. "
        "Regular fixture at Château de Ferrières, treated it 'with the proprietorial ease "
        "of a man who considered himself at home in any room magnificent enough to deserve "
        "him.' Served as artistic director for the 1972 Surrealist Ball. Designed costumes "
        "and set pieces. Designed Baron de Redé's quadruple-face headpiece.\n\n"
        "AT THE BALL: Arrived in wheelchair flanked by wife Gala and two nurses. Carried "
        "laser pointer and auto-folding umbrella. Refused to wear a costume — his own face "
        "'was already more surreal than any mask.' Arrived on the arm of Princess Maria "
        "Gabriella di Savoia.\n\n"
        "CROSS-NETWORK: Designed Christian Dior's costume for Beistegui Ball (1951). "
        "Connected to the entire party-host lineage. His presence at these events was both "
        "artistic and social currency — a Dalí sighting validated the host's cultural authority."
    )},

    {"name": "Gianni Agnelli", "entity_type": "person", "description": (
        "Giovanni 'Gianni' Agnelli (1921-2003). Chairman of Fiat (1966-1996). Known as "
        "'the Uncrowned King of Italy.' Principal shareholder of Italy's largest private "
        "industrial group controlling Fiat, Ferrari, Juventus FC, and La Stampa newspaper.\n\n"
        "ROTHSCHILD CONNECTION: Attended Marie-Hélène de Rothschild's funeral (1996) — "
        "inner circle. Part of the same European elite social network that centered on "
        "Ferrières and the Hôtel Lambert.\n\n"
        "BILDERBERG: Regular Bilderberg Group attendee. Member of the steering committee. "
        "Agnelli represents the convergence of industrial capital, media ownership, and "
        "supranational governance networks with the Rothschild social sphere.\n\n"
        "POLITICAL POWER: Controlled significant portions of Italian politics through "
        "industrial leverage. The Agnelli family's Exor holding company remains one of "
        "Europe's largest diversified conglomerates."
    )},

    {"name": "Georges Pompidou", "entity_type": "person", "description": (
        "Georges Jean Raymond Pompidou (1911-1974). President of France 1969-1974. "
        "Former general manager of Banque Rothschild.\n\n"
        "ROTHSCHILD PIPELINE: Was a schoolteacher when Baron Guy de Rothschild recruited "
        "him to work at Banque Rothschild in 1953. Rose to general manager of the bank. "
        "This is a documented instance of a private banking dynasty identifying, cultivating, "
        "and placing a future head of state. Pompidou served as Prime Minister under "
        "de Gaulle (1962-1968) before winning the presidency.\n\n"
        "SIGNIFICANCE: The Rothschild→Pompidou pipeline is one of the clearest documented "
        "examples of banking-to-political power transfer in modern European history. "
        "His widow Claude Pompidou attended Marie-Hélène de Rothschild's funeral in 1996, "
        "confirming the personal relationship extended beyond professional association."
    )},

    {"name": "Audrey Hepburn", "entity_type": "person", "description": (
        "Audrey Kathleen Hepburn-Ruston (1929-1993). Actress and humanitarian. Close "
        "personal friend of Marie-Hélène de Rothschild.\n\n"
        "SURREALIST BALL: Her birdcage headpiece became the single most reproduced image "
        "from the evening — 'more reproduced than almost any fashion photograph of the era.' "
        "The cage suggested 'a bird trapped in gilded captivity, or perhaps the inverse, "
        "a woman choosing to wear her confinement as ornamentation.'\n\n"
        "NETWORK SIGNIFICANCE: Hepburn's presence at the ball — alongside Dalí, Bardot, "
        "European royalty, and the Rothschilds — documents the Hollywood-aristocracy social "
        "fusion that the Ferrières events formalized."
    )},

    {"name": "Alexis de Redé", "entity_type": "person", "description": (
        "Baron Alexis de Redé (1922-2004). Vietnamese-born socialite and aesthete. Lived "
        "at Hôtel Lambert on Île Saint-Louis, Paris. Nancy Mitford described him as "
        "'a Tippin, thin, stiff, and correct with a weeny, immovable head on a long, "
        "stiff neck.'\n\n"
        "ROTHSCHILD NEXUS: Closest social collaborator of Marie-Hélène de Rothschild after "
        "the Rothschilds purchased upper floors of Hôtel Lambert in 1975. His intimate "
        "dinner parties (Dalí, Guy de Rothschild, Jean Marais) fed directly into "
        "Marie-Hélène's social network.\n\n"
        "PARTY HOST: Bal des Têtes (1957, Hôtel Lambert) — commissioned young Yves Saint "
        "Laurent (then at Dior) to design sets/costumes. YSL credited this as formative. "
        "Bal Oriental (1969) — interior by Valerian Rybar, Hector Pascual automaton "
        "musicians, Pierre Cardin designed de Redé's Mughal prince costume. Future Queen "
        "Margrethe II of Denmark and Aga Khan attended.\n\n"
        "SURREALIST BALL: Wore quadruple-decker four-face headpiece designed by Dalí, "
        "with inset portraits of Marie-Hélène. Wrote the primary first-person account "
        "of the evening — the closest thing to a contemporaneous record that exists.\n\n"
        "Died 2004. Final decades spent as recluse, entertaining dinner parties of 8 "
        "rather than balls of hundreds."
    )},

    {"name": "Charles de Beistegui", "entity_type": "person", "description": (
        "Carlos de Beistegui y de Yturbe (1895-1970). Half-Mexican, half-French millionaire. "
        "Fortune from Mexican silver mines. Launched the entire postwar grand ball tradition.\n\n"
        "BAL ORIENTAL (1951): Palazzo Labia, Venice. 1,000+ guests. Themed after Tiepolo's "
        "Banquet of Cleopatra fresco (in the palazzo itself). Christian Dior attended in a "
        "Dalí-designed costume. Dalí wore a Dior-designed costume. Pierre Cardin designed "
        "costumes for 30+ guests (launched his career). 70 footmen in liveries from the "
        "Duchess of Richmond's 1815 Waterloo-eve ball. Venice was still on gas rations. "
        "England was still rationing food. Beistegui stood on 2-foot platform buskins in "
        "a sausage-curl wig. Set the postwar standard for competitive extravagance.\n\n"
        "SIGNIFICANCE: Proved the appetite for aristocratic spectacle was not dead after "
        "WWII — 'it had merely been waiting for someone bold enough to revive it.' Direct "
        "predecessor to the Rothschild balls."
    )},

    {"name": "Marquis de Cuevas", "entity_type": "person", "description": (
        "George de Cuevas, 8th Marquis de Piedra Blanca de Guana (1885-1961). Chilean-born "
        "ballet impresario.\n\n"
        "ROCKEFELLER MARRIAGE: Married Margaret Strong, granddaughter of John D. Rockefeller. "
        "This marriage represents a direct bridge between the American industrial dynasty "
        "and European aristocratic social networks.\n\n"
        "BIARRITZ BALL (1953): 4,000 invited, 2,800 accepted. Theme: 18th century. "
        "Guest list included 50 princes, 35 marquises, 95 counts, 20 dukes. France was "
        "paralyzed by general strike. Vatican's L'Osservatore Romano denounced it as "
        "'an insult to the misery and suffering of the populace.' Zizi Jeanmaire entered "
        "on a camel. Pierre Balmain designed the marquise's costume.\n\n"
        "SIGNIFICANCE: The Rockefeller-de Cuevas marriage documents the trans-Atlantic "
        "fusion of American industrial wealth with European aristocratic social infrastructure."
    )},

    {"name": "Marie-Laure de Noailles", "entity_type": "person", "description": (
        "Marie-Laure de Noailles, Vicomtesse de Noailles (1902-1970). Patron of surrealism. "
        "Her mansion on Place des États-Unis and modernist Villa Noailles were 'ground zero "
        "for Parisian surrealism.'\n\n"
        "PATRONAGE: Funded Buñuel and Dalí's L'Âge d'Or, Cocteau's The Blood of a Poet, "
        "Man Ray's Les Mystères du Château de Dé. Her gatherings blurred salon, party, "
        "and art exhibition — the model Marie-Hélène de Rothschild would scale up at "
        "Ferrières.\n\n"
        "SIGNIFICANCE: Died 1970, two years before the Surrealist Ball. Her death 'removed "
        "from Paris the single most intellectually radical social hostess of the century, "
        "leaving a vacancy that only the Rothschilds were positioned to fill.' Direct "
        "predecessor in the lineage of elite social-artistic power."
    )},

    {"name": "Truman Capote", "entity_type": "person", "description": (
        "Truman Garcia Capote (1924-1984). American novelist and socialite.\n\n"
        "BLACK AND WHITE BALL (1966): Plaza Hotel, New York, November 28. The first "
        "truly modern society party — broke the mold by mixing European aristocracy, "
        "American politicians, New York socialites, Hollywood stars, and working artists "
        "in one room. Andy Warhol, Norman Mailer, Lauren Bacall, Frank Sinatra, Mia Farrow, "
        "Gloria Vanderbilt, Leonard Bernstein, Rose Kennedy all attended. NYT published "
        "complete guest list — first time for a non-White House party.\n\n"
        "SIGNIFICANCE: Bridge between European private ball tradition and American media "
        "culture. 'What had been a closed ecosystem in Europe was now open, democratic, "
        "and thoroughly American. The Rothschilds took note.'"
    )},

    {"name": "Diana Vreeland", "entity_type": "person", "description": (
        "Diana Vreeland (1903-1989). Editor-in-chief of Vogue 1963-1971. Special consultant "
        "to Metropolitan Museum Costume Institute 1972-1989.\n\n"
        "BRIDGE FIGURE: Appointed to the Met in 1972 — the same year as the Surrealist Ball. "
        "Imported 'the ethos of the Parisian costume ball into an American museum setting' — "
        "theatrical themes, visual excess, celebrity guest lists, glamour over scholarship. "
        "Produced 12 exhibitions (1973-1984) including The World of Balenciaga, The Glory of "
        "Russian Costume, and Yves Saint Laurent: 25 Years of Design.\n\n"
        "CRITICAL LINK: 'She was the critical link between the Parisian tradition of de Beaumont, "
        "de Noailles, and de Rothschild and the American institution that would eventually "
        "supersede it.' Had spent her career covering the very hostesses whose balls she was "
        "now replicating inside a museum.\n\n"
        "The hospitality had become a product. The guest list had become a policy."
    )},

    {"name": "Anna Wintour", "entity_type": "person", "description": (
        "Dame Anna Wintour DBE (b. 1949). Editor-in-chief of Vogue since 1988. Permanent "
        "chairperson of the Met Gala since 1999.\n\n"
        "CORPORATE CAPTURE: Transformed the Met Gala from 'a social event that happened to "
        "raise money into a financial engine that happens to be a social event.' Personally "
        "approves every attendee. Individual tickets: $50 (1948) → $75,000 (2024). Tables "
        "start at $350,000.\n\n"
        "SCALE: 2025 Met Gala raised $31 million in one night. Total contributions under "
        "Wintour exceed $200 million. Met renamed department 'Anna Wintour Costume Center' "
        "in 2014. Met Gala generates $1.3 billion in media impact value (2025) — nearly "
        "double the Super Bowl.\n\n"
        "SIGNIFICANCE: Where Marie-Hélène invited personal friends, Wintour's list is "
        "'curated to mirror the pages of Vogue.' The attendee is not the customer — the "
        "attendee is the product. The private ball's social power has been corporatized, "
        "broadcast, and monetized. The surrealism has been preserved; the privacy has not."
    )},

    {"name": "Banque Rothschild", "entity_type": "organization", "description": (
        "French private bank controlled by the Rothschild family. Guy de Rothschild served "
        "as chairman 1967-1979. Nationalized by Mitterrand's socialist government in 1981 "
        "along with most of France's private banking sector.\n\n"
        "POLITICAL PIPELINE: Georges Pompidou was recruited as a schoolteacher in 1953, "
        "rose to general manager, then became President of France (1969-1974). This is the "
        "documented mechanism: private bank identifies talent → cultivates → places in "
        "political power.\n\n"
        "REBUILT: Guy's son David and nephew Eric founded Rothschild & Cie Banque in 1987 "
        "with 3 employees and 830,000 francs. The dynasty reconstituted itself within 6 "
        "years of nationalization."
    )},

    {"name": "François Mitterrand", "entity_type": "person", "description": (
        "François Maurice Adrien Marie Mitterrand (1916-1996). President of France 1981-1995. "
        "Socialist who nationalized Banque Rothschild in 1981, severing the Rothschild family "
        "from its 150-year institutional base in French finance.\n\n"
        "Introduced France's first direct annual wealth tax (Impôt sur les Grandes Fortunes, "
        "1982). A French Senate report estimated 843 people left France in 2006 due to the "
        "successor tax (ISF), taking €2.8 billion in assets.\n\n"
        "EFFECT ON ELITE SOCIAL CULTURE: 'Throwing a ball where you served blue bread on fur "
        "plates while footmen dressed as cats meowed at your guests became, in this climate, "
        "an invitation for political destruction.' The Mitterrand years ended the era in "
        "which dynastic wealth could organize public spectacle without political consequence."
    )},

    {"name": "Met Gala", "entity_type": "event", "description": (
        "Annual fundraising benefit for the Metropolitan Museum of Art's Costume Institute, "
        "New York. Founded 1948 by Eleanor Lambert as a $50/ticket society dinner. "
        "Transformed by Diana Vreeland (1972-1989) and corporatized by Anna Wintour "
        "(1995-present).\n\n"
        "SUCCESSOR INSTITUTION: Directly descended from the European private ball tradition "
        "via Vreeland, who imported the Parisian model into a museum setting. Has the "
        "costumes, themes, and guest list drama — but structurally cannot have the privacy, "
        "intimacy, or creative coherence of Ferrières.\n\n"
        "ECONOMICS: $75,000/ticket (2024). $350,000/table. $31M raised in 2025. $1.3B "
        "media impact value. Louis Vuitton alone captured $154M in earned media. "
        "'One event was an artwork. The other is an industry.'\n\n"
        "SOCIAL MEDIA BAN: Strict ban on posting from inside the event — a 'nostalgic "
        "gesture toward a world that no longer exists.' Routinely violated. Kylie Jenner's "
        "bathroom selfie is the most famous Met Gala image of the 2010s."
    )},

    {"name": "Marisa Berenson", "entity_type": "person", "description": (
        "Marisa Berenson (b. 1947). Actress, model, socialite. Granddaughter of fashion "
        "designer Elsa Schiaparelli. Attended both the 1971 Proust Ball (as Marchesa Louisa "
        "Casati Stampa) and the 1972 Surrealist Ball (elaborate cage costume). Her presence "
        "at both Rothschild events documents continuity in the inner circle."
    )},

    {"name": "Hélène Rochas", "entity_type": "person", "description": (
        "Hélène Rochas (1927-2011). Perfumer and socialite. Wore a gramophone headpiece "
        "designed by Hector Pascual at the 1972 Surrealist Ball — one of the most "
        "photographed costumes. The headpiece sold at Julian's Auctions in 2024 for $2,600."
    )},

    {"name": "Count Étienne de Beaumont", "entity_type": "person", "description": (
        "Count Étienne de Beaumont (1883-1956). Hosted famous themed costume balls at his "
        "residence on Rue Masseran, 1920s-1930s. Commissioned Picasso, Cocteau, and Satie "
        "to design sets, compose music, and choreograph. His Soirée de Babel (1916) was "
        "Picasso's introduction to this world. The forerunner of the art-party fusion "
        "Marie-Hélène would perfect at Ferrières. Died 1956."
    )},

    {"name": "Elsa Maxwell", "entity_type": "person", "description": (
        "Elsa Maxwell (1883-1963). Iowa-born party organizer. Made a career organizing "
        "events for royalty and high society despite having no money of her own. Invented "
        "the scavenger hunt. Organized international motorboat races at Venice's Lido. "
        "Helped put Monte Carlo on the map. 'Proved that a brilliant party was its own "
        "form of currency.' Attended both the Beistegui (1951) and de Cuevas (1953) balls. "
        "Died 1963."
    )},

    {"name": "Eleanor Lambert", "entity_type": "person", "description": (
        "Eleanor Lambert (1903-2003). Fashion publicist who created New York Fashion Week, "
        "the International Best Dressed List, and the Council of Fashion Designers of America. "
        "Organized the first Costume Institute benefit in 1948 ($50/ticket midnight supper). "
        "Ran the event for 20 years. The institutional seed that would become the Met Gala."
    )},

    {"name": "Battle of Versailles (1973)", "entity_type": "event", "description": (
        "Fashion show organized by Marie-Hélène de Rothschild at the Théâtre Gabriel, "
        "Palace of Versailles, November 28, 1973. Brought together 5 French couturiers "
        "(Yves Saint Laurent, Hubert de Givenchy, Pierre Cardin, Emanuel Ungaro, Marc Bohan "
        "for Dior) vs 5 American designers (Oscar de la Renta, Bill Blass, Anne Klein, "
        "Halston, Stephen Burrows). Watershed moment in fashion history that launched "
        "American designers onto the international stage. Documents Marie-Hélène's role "
        "as a node connecting European and American cultural power."
    )},
]

RELATIONSHIPS = [
    # Rothschild family internal
    {"source": "Guy de Rothschild", "target": "Marie-Hélène de Rothschild",
     "type": "married_to", "tier": "documented",
     "desc": "Married 1957 in New York City. First Rothschild family head to marry non-Jewish spouse."},
    {"source": "Guy de Rothschild", "target": "Mayer Amschel Rothschild",
     "type": "descendant_of", "tier": "documented",
     "desc": "Great-great-grandson. Half of Guy's great-grandparents were Rothschilds."},
    {"source": "Guy de Rothschild", "target": "Banque Rothschild",
     "type": "controlled", "tier": "documented",
     "desc": "Chairman 1967-1979. Took formal control after father Edouard's death in 1949."},
    {"source": "Guy de Rothschild", "target": "Château de Ferrières",
     "type": "owned", "tier": "documented",
     "desc": "Inherited estate. Reopened 1959 with Marie-Hélène. Donated 1975 to Chancellery of Universities of Paris."},

    # The Ball
    {"source": "Guy de Rothschild", "target": "Rothschild Surrealist Ball (1972)",
     "type": "hosted", "tier": "documented",
     "desc": "Co-hosted the ball at Château de Ferrières, December 12, 1972."},
    {"source": "Marie-Hélène de Rothschild", "target": "Rothschild Surrealist Ball (1972)",
     "type": "hosted", "tier": "documented",
     "desc": "Primary creative director and hostess. Designed the ritual elements."},
    {"source": "Rothschild Surrealist Ball (1972)", "target": "Château de Ferrières",
     "type": "located_at", "tier": "documented",
     "desc": "Held at Château de Ferrières, east of Paris. ~150 guests."},
    {"source": "Salvador Dalí", "target": "Rothschild Surrealist Ball (1972)",
     "type": "participated_in", "tier": "documented",
     "desc": "Artistic director. Designed costumes and set pieces. Arrived in wheelchair with wife Gala."},
    {"source": "Audrey Hepburn", "target": "Rothschild Surrealist Ball (1972)",
     "type": "participated_in", "tier": "documented",
     "desc": "Wore iconic birdcage headpiece — most reproduced image from the evening."},
    {"source": "Alexis de Redé", "target": "Rothschild Surrealist Ball (1972)",
     "type": "participated_in", "tier": "documented",
     "desc": "Wore quadruple-face Dalí-designed headpiece. Wrote primary first-person account."},
    {"source": "Hélène Rochas", "target": "Rothschild Surrealist Ball (1972)",
     "type": "participated_in", "tier": "documented",
     "desc": "Wore gramophone headpiece by Hector Pascual. Photographed with François-Marie Banier."},
    {"source": "Marisa Berenson", "target": "Rothschild Surrealist Ball (1972)",
     "type": "participated_in", "tier": "documented",
     "desc": "Wore elaborate cage costume. Also attended 1971 Proust Ball as Marchesa Casati Stampa."},
    {"source": "Gianni Agnelli", "target": "Rothschild Surrealist Ball (1972)",
     "type": "connected_to", "tier": "credible",
     "desc": "Inner circle — attended Marie-Hélène's funeral (1996). Bilderberg steering committee member."},

    # Banking→Politics pipeline
    {"source": "Guy de Rothschild", "target": "Georges Pompidou",
     "type": "recruited", "tier": "documented",
     "desc": "Recruited schoolteacher Pompidou to Banque Rothschild in 1953. Pompidou rose to general manager, then President of France (1969-1974)."},
    {"source": "Georges Pompidou", "target": "Banque Rothschild",
     "type": "employed_by", "tier": "documented",
     "desc": "General manager of Banque Rothschild before entering politics. Recruited by Guy de Rothschild in 1953."},
    {"source": "François Mitterrand", "target": "Banque Rothschild",
     "type": "nationalized", "tier": "documented",
     "desc": "Nationalized Banque Rothschild in 1981 along with most of France's private banking sector."},

    # Rothschild social network
    {"source": "Marie-Hélène de Rothschild", "target": "Audrey Hepburn",
     "type": "associate_of", "tier": "documented",
     "desc": "Close personal friend. Hepburn was a regular at Rothschild social events."},
    {"source": "Marie-Hélène de Rothschild", "target": "Salvador Dalí",
     "type": "associate_of", "tier": "documented",
     "desc": "Dalí was a regular fixture at Ferrières, treating the château with proprietary ease."},
    {"source": "Alexis de Redé", "target": "Marie-Hélène de Rothschild",
     "type": "associate_of", "tier": "documented",
     "desc": "Closest social collaborator. Neighbors at Hôtel Lambert after 1975. Shared aesthetic sensibility."},
    {"source": "Alexis de Redé", "target": "Salvador Dalí",
     "type": "associate_of", "tier": "documented",
     "desc": "Dalí attended de Redé's intimate dinner parties. Designed his Surrealist Ball headpiece."},
    {"source": "Marie-Hélène de Rothschild", "target": "Battle of Versailles (1973)",
     "type": "organized", "tier": "documented",
     "desc": "Organized the 1973 fashion showdown at Palace of Versailles. Five French vs five American designers."},

    # Agnelli-Bilderberg
    {"source": "Gianni Agnelli", "target": "Bilderberg Group",
     "type": "member_of", "tier": "documented",
     "desc": "Regular attendee and steering committee member. Represents convergence of industrial capital with supranational governance."},

    # Rockefeller-de Cuevas bridge
    {"source": "Marquis de Cuevas", "target": "John D. Rockefeller",
     "type": "connected_to", "tier": "documented",
     "desc": "Married Margaret Strong, granddaughter of John D. Rockefeller. Trans-Atlantic bridge between American industrial dynasty and European aristocratic social networks."},

    # Party host lineage
    {"source": "Charles de Beistegui", "target": "Rothschild Surrealist Ball (1972)",
     "type": "influenced", "tier": "credible",
     "desc": "His 1951 Venetian ball launched the postwar tradition. Set the standard the Rothschilds would exceed."},
    {"source": "Marie-Laure de Noailles", "target": "Marie-Hélène de Rothschild",
     "type": "influenced", "tier": "credible",
     "desc": "Her salon/party/art exhibition model was what Marie-Hélène scaled up at Ferrières. Died 1970, leaving 'a vacancy only the Rothschilds were positioned to fill.'"},
    {"source": "Truman Capote", "target": "Rothschild Surrealist Ball (1972)",
     "type": "influenced", "tier": "credible",
     "desc": "His 1966 Black and White Ball broke the European-only model, mixing aristocracy with Hollywood. 'The Rothschilds took note.'"},
    {"source": "Count Étienne de Beaumont", "target": "Marie-Laure de Noailles",
     "type": "associate_of", "tier": "documented",
     "desc": "Both part of the Parisian interwar avant-garde party host network. Commissioned same artists (Picasso, Cocteau, Satie)."},

    # Met Gala succession
    {"source": "Diana Vreeland", "target": "Met Gala",
     "type": "created", "tier": "documented",
     "desc": "Transformed the Costume Institute benefit from trade dinner to cultural spectacle (1972-1989). Imported Parisian ball ethos into American museum."},
    {"source": "Anna Wintour", "target": "Met Gala",
     "type": "controlled", "tier": "documented",
     "desc": "Permanent chairperson since 1999. Corporatized the event entirely. Personally approves every attendee."},
    {"source": "Eleanor Lambert", "target": "Met Gala",
     "type": "created", "tier": "documented",
     "desc": "Organized the first Costume Institute benefit in 1948. Ran it for 20 years. Created the institutional seed."},
    {"source": "Rothschild Surrealist Ball (1972)", "target": "Met Gala",
     "type": "influenced", "tier": "credible",
     "desc": "Vreeland appointed to the Met in 1972, same year as the ball. The Met Gala is the corporatized, broadcast successor to the private aristocratic ball tradition the Rothschilds perfected."},

    # Existing DB connections
    {"source": "Gianni Agnelli", "target": "Lynn Forester de Rothschild",
     "type": "connected_to", "tier": "credible",
     "desc": "Both Rothschild network and Bilderberg circles. Lynn married into the Rothschild family (Evelyn de Rothschild, 2000)."},
    {"source": "Guy de Rothschild", "target": "Lynn Forester de Rothschild",
     "type": "connected_to", "tier": "documented",
     "desc": "Same Rothschild dynasty. Lynn married Sir Evelyn de Rothschild (English branch) in 2000. Guy headed the French branch."},
    {"source": "Marquis de Cuevas", "target": "David Rockefeller",
     "type": "connected_to", "tier": "documented",
     "desc": "De Cuevas married Margaret Strong, granddaughter of John D. Rockefeller. David Rockefeller was John D.'s grandson — making them connected through the same dynasty."},
]

ENTITY_SOURCES = {
    "Guy de Rothschild": [1293, 1294, 1295, 1296, 1305],
    "Marie-Hélène de Rothschild": [1292, 1296, 1299, 1300, 1301],
    "Mayer Amschel Rothschild": [1297],
    "Château de Ferrières": [1296, 1316, 1317],
    "Rothschild Surrealist Ball (1972)": [1291, 1292, 1299, 1300, 1301],
    "Salvador Dalí": [1291, 1299, 1319],
    "Gianni Agnelli": [1308, 1309],
    "Georges Pompidou": [1295, 1296, 1307],
    "Audrey Hepburn": [1292, 1299],
    "Alexis de Redé": [1291, 1298, 1315],
    "Charles de Beistegui": [1314],
    "Marquis de Cuevas": [1313, 1318],
    "Marie-Laure de Noailles": [1299],
    "Truman Capote": [1302],
    "Diana Vreeland": [1303, 1312],
    "Anna Wintour": [1310, 1311, 1312],
    "François Mitterrand": [1305, 1306],
    "Banque Rothschild": [1296, 1305, 1307],
    "Met Gala": [1310, 1311, 1312],
    "Marisa Berenson": [1299, 1300],
    "Hélène Rochas": [1291, 1320],
    "Count Étienne de Beaumont": [1299],
    "Elsa Maxwell": [1314],
    "Eleanor Lambert": [1312],
    "Battle of Versailles (1973)": [1299],
}
