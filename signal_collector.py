#!/usr/bin/env python3
"""Signal Collector — polls public feeds, matches entity names, stores hits.

Usage:
    uv run python signal_collector.py          # one-shot run
    crontab: 0 */6 * * * cd ~/intel-console && uv run python signal_collector.py
"""

import json
import os
import re
import sqlite3
import time
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

import feedparser

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "intel.db")

# Minimum name length to build a pattern for (skips CIA, NSA, FBI, MI6, etc.)
MIN_MATCH_LENGTH = 6

# RSS feeds to poll
RSS_FEEDS = {
    "reuters": "https://feeds.reuters.com/reuters/topNews",
    "bbc": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "guardian": "https://www.theguardian.com/us-news/rss",
    "npr": "https://feeds.npr.org/1001/rss.xml",
    "aljazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "ap": "https://rsshub.app/apnews/topics/apf-topnews",
}

# Government API endpoints
FED_REGISTER_URL = (
    "https://www.federalregister.gov/api/v1/documents.json"
    "?per_page=50&order=newest&conditions[type][]=NOTICE&conditions[type][]=RULE"
)
SEC_EDGAR_SEARCH_URL = "https://efts.sec.gov/LATEST/search-index?q={query}&dateRange=custom&startdt={start}&enddt={end}&from=0&size=10"
OFAC_SDN_URL = "https://www.treasury.gov/ofac/downloads/sdn.xml"

# User-Agent for government APIs
UA = "IntelConsole/1.0 (civilian OSINT research tool)"


class EntityMatcher:
    """Builds regex patterns from entity names + aliases for headline matching."""

    def __init__(self, db: sqlite3.Connection):
        self.patterns: list[tuple[re.Pattern, int, str]] = []
        self._org_names: list[tuple[str, int]] = []

        rows = db.execute("SELECT id, name, aliases, entity_type FROM entities").fetchall()
        raw: list[tuple[str, int, str]] = []
        for row in rows:
            eid, name, aliases, etype = row
            names = [name]
            if aliases:
                names.extend(a.strip() for a in aliases.split(",") if a.strip())
            for n in names:
                if len(n) >= MIN_MATCH_LENGTH:
                    raw.append((n, eid, n))
            # Track org names for SEC queries
            if etype == "organization" and len(name) >= MIN_MATCH_LENGTH:
                self._org_names.append((name, eid))

        # Sort longest first so "Jeffrey Epstein" matches before "Epstein"
        raw.sort(key=lambda x: len(x[0]), reverse=True)

        for name_str, eid, matched in raw:
            try:
                pat = re.compile(r"\b" + re.escape(name_str) + r"\b", re.IGNORECASE)
                self.patterns.append((pat, eid, matched))
            except re.error:
                continue

    def match(self, text: str) -> list[tuple[int, str]]:
        """Return [(entity_id, matched_name), ...] for all entities found in text."""
        hits: list[tuple[int, str]] = []
        seen: set[int] = set()
        for pat, eid, matched in self.patterns:
            if eid not in seen and pat.search(text):
                hits.append((eid, matched))
                seen.add(eid)
        return hits

    @property
    def org_names(self) -> list[tuple[str, int]]:
        return self._org_names


def collect_rss(matcher: EntityMatcher) -> list[dict]:
    """Poll RSS feeds, match headlines against entities."""
    signals = []
    for feed_name, feed_url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(feed_url)
        except Exception as e:
            print(f"  [RSS] {feed_name}: error — {e}")
            continue

        count = 0
        for entry in feed.entries:
            title = entry.get("title", "")
            summary = entry.get("summary", "")
            text = f"{title} {summary}"
            link = entry.get("link", "")
            if not link:
                continue

            published = entry.get("published", "")

            hits = matcher.match(text)
            for eid, matched in hits:
                signals.append({
                    "entity_id": eid,
                    "source_feed": feed_name,
                    "headline": title[:500],
                    "url": link[:2000],
                    "snippet": summary[:300] if summary else "",
                    "matched_name": matched,
                    "published_at": published[:100] if published else "",
                })
                count += 1

        print(f"  [RSS] {feed_name}: {len(feed.entries)} entries → {count} signals")

    return signals


def collect_federal_register(matcher: EntityMatcher) -> list[dict]:
    """Poll Federal Register API for recent notices/rules."""
    signals = []
    try:
        req = urllib.request.Request(FED_REGISTER_URL, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  [FedReg] error — {e}")
        return signals

    results = data.get("results", [])
    count = 0
    for doc in results:
        title = doc.get("title", "")
        abstract = doc.get("abstract", "") or ""
        text = f"{title} {abstract}"
        url = doc.get("html_url", "")
        pub_date = doc.get("publication_date", "")

        hits = matcher.match(text)
        for eid, matched in hits:
            signals.append({
                "entity_id": eid,
                "source_feed": "fed_register",
                "headline": title[:500],
                "url": url[:2000],
                "snippet": abstract[:300],
                "matched_name": matched,
                "published_at": pub_date,
            })
            count += 1

    print(f"  [FedReg] {len(results)} documents → {count} signals")
    return signals


def collect_sec_edgar(matcher: EntityMatcher) -> list[dict]:
    """Search SEC EDGAR full-text for organization entities."""
    signals = []
    orgs = matcher.org_names[:20]  # Cap at 20 queries
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # Look back 30 days
    start = datetime.now(timezone.utc).strftime("%Y-%m-01")

    total_hits = 0
    for name, eid in orgs:
        query = urllib.request.quote(f'"{name}"')
        url = (
            f"https://efts.sec.gov/LATEST/search-index"
            f"?q={query}&dateRange=custom&startdt={start}&enddt={today}&from=0&size=5"
        )
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "application/json",
            })
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
        except Exception:
            time.sleep(0.5)
            continue

        hits = data.get("hits", {}).get("hits", [])
        for hit in hits:
            src = hit.get("_source", {})
            filing_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company={urllib.request.quote(name)}&type=&dateb=&owner=include&count=10&search_text=&action=getcompany"
            title = src.get("display_names", [name])[0] if src.get("display_names") else name
            file_date = src.get("file_date", "")

            signals.append({
                "entity_id": eid,
                "source_feed": "sec_edgar",
                "headline": f"SEC filing: {title}",
                "url": filing_url[:2000],
                "snippet": "",
                "matched_name": name,
                "published_at": file_date,
            })
            total_hits += 1

        time.sleep(0.5)  # Rate limit

    print(f"  [SEC] {len(orgs)} org queries → {total_hits} signals")
    return signals


def collect_ofac_sdn(matcher: EntityMatcher) -> list[dict]:
    """Check OFAC SDN sanctions list for entity name matches."""
    signals = []
    try:
        req = urllib.request.Request(OFAC_SDN_URL, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            tree = ET.parse(resp)
    except Exception as e:
        print(f"  [OFAC] error — {e}")
        return signals

    root = tree.getroot()
    # Namespace handling
    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0] + "}"

    entries = root.findall(f".//{ns}sdnEntry")
    sdn_names = []
    for entry in entries:
        first = entry.findtext(f"{ns}firstName", default="")
        last = entry.findtext(f"{ns}lastName", default="")
        full = f"{first} {last}".strip()
        if full:
            uid = entry.findtext(f"{ns}uid", default="")
            sdn_names.append((full, uid))

    # Match our entities against SDN names
    count = 0
    for sdn_name, uid in sdn_names:
        hits = matcher.match(sdn_name)
        for eid, matched in hits:
            signals.append({
                "entity_id": eid,
                "source_feed": "ofac_sdn",
                "headline": f"OFAC SDN: {sdn_name}",
                "url": f"https://sanctionssearch.ofac.treas.gov/Details.aspx?id={uid}",
                "snippet": "",
                "matched_name": matched,
                "published_at": "",
            })
            count += 1

    print(f"  [OFAC] {len(entries)} SDN entries → {count} signals")
    return signals


def store_signals(db: sqlite3.Connection, signals: list[dict]) -> int:
    """INSERT OR IGNORE signals (dedup via unique index). Returns new count."""
    inserted = 0
    for s in signals:
        try:
            db.execute(
                """INSERT OR IGNORE INTO signals
                   (entity_id, source_feed, headline, url, snippet, matched_name, published_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    s["entity_id"],
                    s["source_feed"],
                    s["headline"],
                    s["url"],
                    s["snippet"],
                    s["matched_name"],
                    s["published_at"],
                ),
            )
            if db.execute("SELECT changes()").fetchone()[0] > 0:
                inserted += 1
        except sqlite3.Error as e:
            print(f"  [DB] insert error: {e}")
    db.commit()
    return inserted


def main():
    print(f"Signal Collector — {datetime.now(timezone.utc).isoformat()}")
    print(f"DB: {DB_PATH}")

    db = sqlite3.connect(DB_PATH)
    db.execute("PRAGMA foreign_keys=ON")
    matcher = EntityMatcher(db)
    print(f"Loaded {len(matcher.patterns)} name patterns from {len(set(p[1] for p in matcher.patterns))} entities\n")

    all_signals: list[dict] = []

    # RSS feeds
    print("Polling RSS feeds...")
    all_signals.extend(collect_rss(matcher))

    # Federal Register
    print("\nPolling Federal Register...")
    all_signals.extend(collect_federal_register(matcher))

    # SEC EDGAR
    print("\nPolling SEC EDGAR...")
    all_signals.extend(collect_sec_edgar(matcher))

    # OFAC SDN
    print("\nPolling OFAC SDN...")
    all_signals.extend(collect_ofac_sdn(matcher))

    # Store
    print(f"\nStoring {len(all_signals)} signals...")
    new_count = store_signals(db, all_signals)
    total = db.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    db.close()

    print(f"\nDone. {new_count} new signals stored ({total} total in DB).")


if __name__ == "__main__":
    main()
