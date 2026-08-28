"""
Stanley Kubrick / Eyes Wide Shut — restoration layer for Intel Console.

These two entities (plus Mentmore Towers) were originally direct SQL inserts
(2026-03) and were lost in a later DB rebuild because they lived in no
expansion script. Mentmore Towers is recreated by expansion_uplift_2026_elite_social;
this module restores Kubrick and the film and re-wires the Rothschild link.

EXISTING ENTITIES (referenced by name, NOT duplicated):
  Mentmore Towers, Château de Ferrières, Rothschild Surrealist Ball (1972),
  Guy de Rothschild
"""

SOURCES = [
    {"id": 2700, "title": "Stanley Kubrick — Wikipedia", "url": "https://en.wikipedia.org/wiki/Stanley_Kubrick",
     "source_type": "other", "year": 2026},
    {"id": 2701, "title": "Eyes Wide Shut — Wikipedia (production, locations, release)",
     "url": "https://en.wikipedia.org/wiki/Eyes_Wide_Shut", "source_type": "other", "year": 2026},
    {"id": 2702, "title": "Mentmore Towers — Wikipedia (Paxton design for Mayer de Rothschild; filming location for Eyes Wide Shut)",
     "url": "https://en.wikipedia.org/wiki/Mentmore_Towers", "source_type": "other", "year": 2026},
    {"id": 2703, "title": "Château de Ferrières — Wikipedia (modelled on Mentmore; Paxton; 1972 Surrealist Ball)",
     "url": "https://en.wikipedia.org/wiki/Ch%C3%A2teau_de_Ferri%C3%A8res", "source_type": "other", "year": 2026},
]

ENTITIES = [
    {
        "name": "Stanley Kubrick",
        "entity_type": "person",
        "description": (
            "Stanley Kubrick (26 July 1928 – 7 March 1999). American film director whose final "
            "film, Eyes Wide Shut (1999), depicts a masked ritual orgy of the wealthy at a "
            "country mansion. Kubrick died of a heart attack at his Hertfordshire home six days "
            "after screening his final cut to Warner Bros. executives and the film's stars; the "
            "film was released posthumously in July 1999. The mansion exteriors were shot at "
            "Mentmore Towers, the Rothschild house built by Joseph Paxton for Baron Mayer de "
            "Rothschild in the 1850s — the same architect whose design was copied for the "
            "Château de Ferrières, site of the 1972 Rothschild Surrealist Ball. Kubrick's "
            "documented career: Paths of Glory, Dr. Strangelove, 2001: A Space Odyssey, "
            "A Clockwork Orange, The Shining, Full Metal Jacket."
        ),
        "aliases": "",
        "metadata": {"nationality": "American", "born": "1928-07-26", "died": "1999-03-07",
                     "status": "deceased", "role": "Film director"},
    },
    {
        "name": "Eyes Wide Shut",
        "entity_type": "publication",
        "description": (
            "1999 film directed by Stanley Kubrick, adapted from Arthur Schnitzler's 1926 "
            "novella Traumnovelle. Its central sequence — a masked, password-protected ritual "
            "gathering of the powerful at a country estate — has become the reference image for "
            "elite secret-society gatherings in popular culture. The estate exteriors were filmed "
            "at Mentmore Towers, a Rothschild house designed by Joseph Paxton. Kubrick died on "
            "7 March 1999, six days after delivering his final cut; Warner Bros. released the film "
            "on 16 July 1999 with digital figures added to obscure the orgy scene for the US "
            "R rating. The film's sourcing of imagery from documented elite gatherings is a "
            "matter of interpretation (inference tier); the production facts are documented."
        ),
        "aliases": "EWS",
        "metadata": {"year": 1999, "role": "Film"},
    },
]

RELATIONSHIPS = [
    {"source": "Stanley Kubrick", "target": "Eyes Wide Shut", "type": "directed", "tier": "documented",
     "desc": "Directed, produced and co-wrote Eyes Wide Shut, his final film; died six days after screening the final cut (7 March 1999).",
     "year_start": 1996, "year_end": 1999, "sources": [2700, 2701]},
    {"source": "Eyes Wide Shut", "target": "Mentmore Towers", "type": "located_at", "tier": "documented",
     "desc": "The exteriors of the Somerton mansion — the masked-ritual location — were filmed at Mentmore Towers, Buckinghamshire, the Rothschild house designed by Joseph Paxton.",
     "year_start": 1997, "year_end": 1998, "sources": [2701, 2702]},
    {"source": "Mentmore Towers", "target": "Château de Ferrières", "type": "parallel_pattern", "tier": "documented",
     "desc": "Ferrières was built (1855–1859) for James de Rothschild to Paxton's Mentmore design, at the family's request that it be 'like Mentmore, but twice the size'; Ferrières later hosted the 1972 Surrealist Ball.",
     "sources": [2702, 2703]},
    {"source": "Eyes Wide Shut", "target": "Rothschild Surrealist Ball (1972)", "type": "parallel_pattern", "tier": "inference",
     "desc": "Frequently drawn comparison between the film's masked gathering and the 1972 Surrealist Ball at Ferrières (masks, a Rothschild house of the same Paxton lineage). The visual parallel is documented; any claim that the ball was a source for the film is inference.",
     "sources": [2701, 2703]},
]

ENTITY_SOURCES = {
    "Stanley Kubrick": [2700, 2701],
    "Eyes Wide Shut": [2701, 2702],
}

GEO_COORDS = {
    "Stanley Kubrick": (51.7350, -0.3250, "inference", "Childwickbury Manor, Hertfordshire"),
    "Eyes Wide Shut": (51.8481, -0.7186, "credible", "Mentmore Towers, Buckinghamshire (principal exterior location)"),
}

PHOTO_CANDIDATES = {
    "Stanley Kubrick": "https://commons.wikimedia.org/wiki/File:Kubrick_on_the_set_of_Barry_Lyndon_(1975_publicity_photo).jpg",
}
