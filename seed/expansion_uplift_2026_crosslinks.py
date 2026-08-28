"""
2026-08 refresh — cross-module edges.

Relationships that span entities created by different uplift modules in the
same wave (deferred by the authoring agents until every entity existed).
Sources reuse ids already inserted by expansion_uplift_2026_intelligence.
"""

SOURCES = []

ENTITIES = []

RELATIONSHIPS = [
    {
        "source": "Pete Hegseth",
        "target": "Signalgate",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "As Secretary of Defense, posted detailed timing and weapons information for the "
            "15 March 2025 strikes on Houthi targets in Yemen into a Signal group chat that "
            "inadvertently included The Atlantic's editor-in-chief. The Pentagon Inspector "
            "General's December 2025 report found the postings violated Department of Defense "
            "policy on handling sensitive information."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1709, 1710, 1712],
    },
    {
        "source": "Marco Rubio",
        "target": "Signalgate",
        "type": "involved_in",
        "tier": "documented",
        "desc": (
            "Participant in the March 2025 Signal group chat ('Houthi PC small group') in which "
            "strike planning was discussed; later became acting National Security Advisor after "
            "Mike Waltz — who created the chat and added the journalist — was removed on "
            "1 May 2025."
        ),
        "year_start": 2025,
        "year_end": 2025,
        "sources": [1709, 1711],
    },
    {
        "source": "Benjamin Netanyahu",
        "target": "Operation Grim Beeper",
        "type": "authorized",
        "tier": "credible",
        "desc": (
            "In November 2024 Netanyahu publicly acknowledged approving the September 2024 "
            "pager and walkie-talkie detonations against Hezbollah, the first official Israeli "
            "acknowledgement of the operation. Tier is credible: a public statement reported "
            "by the press, not a released government document."
        ),
        "year_start": 2024,
        "year_end": 2024,
        "sources": [1713],
    },
    {
        "source": "Nord Stream Sabotage Investigation",
        "target": "Russia-Ukraine War",
        "type": "resulted_from",
        "tier": "documented",
        "desc": (
            "The September 2022 destruction of the Nord Stream 1 and 2 pipelines occurred seven "
            "months into Russia's full-scale invasion of Ukraine; German federal prosecutors' "
            "2025–2026 case names a Ukrainian national as a member of the sabotage team, placing "
            "the attack squarely within the war's energy-infrastructure dimension."
        ),
        "year_start": 2022,
        "sources": [1726, 1727],
    },
]

ENTITY_SOURCES = {}
