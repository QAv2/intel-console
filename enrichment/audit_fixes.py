#!/usr/bin/env python3
"""
Audit fixes for Disclosure Scrolls enrichment batch (batch_5).
Applies type corrections, direction fixes, and deletes bad relationships.

Run: cd ~/intel-console && python3 enrichment/audit_fixes.py
Then: python3 export_static.py
"""
import sqlite3

DB = "data/intel.db"

def get_name_map(conn):
    rows = conn.execute("SELECT id, name FROM entities").fetchall()
    return {name: eid for eid, name in rows}

def find_rel(conn, source_id, target_id, rel_type):
    """Find a relationship by source, target, and type."""
    row = conn.execute(
        "SELECT id FROM relationships WHERE source_id=? AND target_id=? AND relationship_type=?",
        (source_id, target_id, rel_type)
    ).fetchone()
    return row[0] if row else None

def update_type(conn, names, source, target, old_type, new_type, reason):
    sid = names.get(source)
    tid = names.get(target)
    if not sid or not tid:
        print(f"  [!] SKIP - entity not found: {source} or {target}")
        return
    rid = find_rel(conn, sid, tid, old_type)
    if not rid:
        print(f"  [!] SKIP - rel not found: {source} --[{old_type}]--> {target}")
        return
    conn.execute("UPDATE relationships SET relationship_type=? WHERE id=?", (new_type, rid))
    print(f"  [FIX] {source} --[{old_type}]--> {target}  =>  [{new_type}]  ({reason})")

def delete_rel(conn, names, source, target, rel_type, reason):
    sid = names.get(source)
    tid = names.get(target)
    if not sid or not tid:
        print(f"  [!] SKIP - entity not found: {source} or {target}")
        return
    rid = find_rel(conn, sid, tid, rel_type)
    if not rid:
        print(f"  [!] SKIP - rel not found: {source} --[{rel_type}]--> {target}")
        return
    conn.execute("DELETE FROM relationship_sources WHERE relationship_id=?", (rid,))
    conn.execute("DELETE FROM relationships WHERE id=?", (rid,))
    print(f"  [DEL] {source} --[{rel_type}]--> {target}  ({reason})")

def swap_and_fix(conn, names, source, target, old_type, new_source, new_target, new_type, new_desc, reason):
    """Delete old rel, insert corrected version."""
    sid = names.get(source)
    tid = names.get(target)
    if not sid or not tid:
        print(f"  [!] SKIP - entity not found: {source} or {target}")
        return
    rid = find_rel(conn, sid, tid, old_type)
    if rid:
        conn.execute("DELETE FROM relationship_sources WHERE relationship_id=?", (rid,))
        conn.execute("DELETE FROM relationships WHERE id=?", (rid,))

    nsid = names.get(new_source)
    ntid = names.get(new_target)
    if not nsid or not ntid:
        print(f"  [!] SKIP - new entity not found: {new_source} or {new_target}")
        return
    conn.execute(
        """INSERT INTO relationships (source_id, target_id, relationship_type, evidence_tier, description)
           VALUES (?, ?, ?, 'credible', ?)""",
        (nsid, ntid, new_type, new_desc)
    )
    print(f"  [SWAP] {source}--[{old_type}]-->{target}  =>  {new_source}--[{new_type}]-->{new_target}  ({reason})")

def main():
    conn = sqlite3.connect(DB)
    names = get_name_map(conn)

    print("=" * 60)
    print("ENRICHMENT AUDIT — Disclosure Scrolls Batch")
    print("=" * 60)

    # ── 1. INVALID TYPE FIXES ────────────────────────────────
    print("\n── Invalid relationship type fixes ──")

    update_type(conn, names,
        "Sam Altman", "OpenAI", "CEO_of", "director_of",
        "CEO_of not a valid type")

    update_type(conn, names,
        "Sam Altman", "Peter Thiel", "mentor_by", "mentored_by",
        "typo: mentor_by → mentored_by")

    update_type(conn, names,
        "Luke Iseman", "Make Sunsets", "CEO_of", "founder_of",
        "CEO_of not valid; he founded it")

    update_type(conn, names,
        "Mark Zuckerberg", "Meta", "CEO of", "founder_of",
        "'CEO of' (with space) not valid; he founded it")

    update_type(conn, names,
        "Richard Sackler", "Purdue Pharma", "president_of", "director_of",
        "president_of not valid; director_of covers executive roles")

    update_type(conn, names,
        "Willis Harman", "IONS", "president_of", "director_of",
        "president_of not valid; director_of covers executive roles")

    update_type(conn, names,
        "Frank Keutsch", "SCoPEx", "principal_investigator_of", "led",
        "principal_investigator_of not valid; 'led' captures it")

    update_type(conn, names,
        "Bob Lazar", "Area 51", "claimed_worked_for", "affiliated_with",
        "claimed_worked_for not valid; affiliated_with (credible tier) preserves uncertainty")

    update_type(conn, names,
        "Bob Lazar", "USAF", "claimed_employed_by", "affiliated_with",
        "claimed_employed_by not valid; affiliated_with (credible tier) preserves uncertainty")

    update_type(conn, names,
        "Philip Corso", "Roswell Incident", "authored", "affiliated_with",
        "authored not valid; he wrote about it and claimed involvement")

    # ── 2. DIRECTION / LOGIC FIXES ──────────────────────────
    print("\n── Direction and logic fixes ──")

    # Clapper → Snowden "exposed" is backwards. Snowden exposed Clapper.
    swap_and_fix(conn, names,
        "James Clapper", "Edward Snowden", "exposed",
        "Edward Snowden", "James Clapper", "whistleblower_on",
        "Snowden's 2013 leaks revealed Clapper's false testimony to Congress about NSA bulk data collection.",
        "direction reversed: Snowden exposed Clapper, not vice versa")

    # Osteen → Clinton "attended" is backwards. Clinton attended Osteen's church.
    swap_and_fix(conn, names,
        "Joel Osteen", "Bill Clinton", "attended",
        "Bill Clinton", "Joel Osteen", "attended",
        "Bill Clinton attended an early morning service at Joel Osteen's Lakewood Church (2008).",
        "direction reversed: Clinton attended Osteen's church")

    # Zuckerberg → Cambridge Analytica "investigated" — Zuckerberg was investigated ABOUT CA
    update_type(conn, names,
        "Mark Zuckerberg", "Cambridge Analytica", "investigated", "implicated_in",
        "Zuckerberg didn't investigate CA; he was implicated in the scandal")

    # Sarkozy → NATO "led" — he didn't lead NATO; he pushed for intervention
    update_type(conn, names,
        "Nicolas Sarkozy", "NATO", "led", "affiliated_with",
        "Sarkozy didn't lead NATO; France participated in NATO Libya intervention")

    # Ken Kesey → Gottlieb "investigated_by" — Kesey was a volunteer subject, not investigated
    update_type(conn, names,
        "Ken Kesey", "Sidney Gottlieb", "investigated_by", "recruited_by",
        "Kesey volunteered for Gottlieb's MKUltra experiments; recruited, not investigated")

    # Richard Doty → Bennewitz "directed" — misleading type for disinformation ops
    update_type(conn, names,
        "Richard Doty", "Paul Bennewitz", "directed", "investigated",
        "'directed' implies authority over; 'investigated' better captures targeting via disinfo")

    # ── 3. DELETIONS ────────────────────────────────────────
    print("\n── Relationship deletions ──")

    # Brennan → bin Laden "participated_in" — person-to-person doesn't work
    delete_rel(conn, names,
        "John Brennan", "Osama bin Laden", "participated_in",
        "person-to-person 'participated_in' is nonsensical; should be an event entity")

    # Kermit Roosevelt → Mossadegh "directed" — misleading; already captured by Kermit → Op Ajax
    delete_rel(conn, names,
        "Kermit Roosevelt Jr.", "Mohammad Mossadegh", "directed",
        "misleading type; Kermit→Op Ajax already captures this action")

    # Cristin Kearns → John Yudkin "influenced" — Yudkin died 1995, Kearns published 2016
    delete_rel(conn, names,
        "Cristin Kearns", "John Yudkin", "influenced",
        "chronologically impossible: Yudkin died 1995, Kearns published 2016")

    # Alice Bailey → Blavatsky "influenced" (from raw batch, check if it got in)
    # This would mean Bailey influenced Blavatsky, but Blavatsky died 1891 before Bailey wrote
    rid = find_rel(conn, names.get("Alice Bailey"), names.get("Helena Blavatsky"), "influenced")
    if rid:
        delete_rel(conn, names,
            "Alice Bailey", "Helena Blavatsky", "influenced",
            "chronologically impossible: Blavatsky died 1891, Bailey wrote in 1920s")

    # Sam Altman → Peter Thiel "associate_of" — redundant with mentored_by and investor_in
    delete_rel(conn, names,
        "Sam Altman", "Peter Thiel", "associate_of",
        "redundant: already captured by mentored_by and investor_in relationships")

    # ── 4. DESCRIPTION FIXES ────────────────────────────────
    print("\n── Description improvements ──")

    # Jim Morrison → Gulf of Tonkin: add clarity that this is through his father
    sid = names.get("Jim Morrison")
    tid = names.get("Gulf of Tonkin Incident")
    if sid and tid:
        rid = find_rel(conn, sid, tid, "related_to")
        if rid:
            conn.execute(
                "UPDATE relationships SET description=? WHERE id=?",
                ("Jim Morrison's father, Admiral George S. Morrison, commanded the US naval fleet during the Gulf of Tonkin incident (1964). This military-intelligence family connection is part of the broader Laurel Canyon pattern.", rid)
            )
            print("  [DESC] Jim Morrison → Gulf of Tonkin: expanded to clarify indirect connection")

    # Christopher Mellon → AATIP: fix from "worked_for" to "affiliated_with" (he didn't work FOR AATIP)
    update_type(conn, names,
        "Christopher Mellon", "AATIP", "worked_for", "affiliated_with",
        "Mellon was Deputy ASDI, not AATIP staff; he helped disclose it")

    conn.commit()
    conn.close()

    print("\n" + "=" * 60)
    print("AUDIT COMPLETE — run: python3 export_static.py")
    print("=" * 60)


if __name__ == "__main__":
    main()
