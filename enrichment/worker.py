"""
Enrichment worker — processes a batch of people against the full entity list.
Uses Gemini API with Google Search grounding to identify missing relationships.

Usage: python3 worker.py --batch 0
"""
import json, os, sys, time, argparse, fcntl

# Load API keys from ~/.env
def _load_env():
    env_path = os.path.expanduser('~/.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    os.environ[k.strip()] = v.strip()
_load_env()

from google import genai
from google.genai import types

BASE = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE, 'results')
LEDGER_PATH = os.path.join(BASE, 'ledger.jsonl')
SUB_BATCH_SIZE = 10  # people per API call
MODEL = 'gemini-2.5-flash'

RELATIONSHIP_TYPES = [
    'member_of', 'founder_of', 'director_of', 'employed_by', 'worked_for',
    'appointed_by', 'advisor_to', 'boss_of', 'subordinate_of', 'successor_to',
    'predecessor_of', 'affiliated_with', 'associate_of', 'ally_of',
    'funded_by', 'funded', 'investor_in', 'financial_connection',
    'asset_of', 'operated', 'operated_by', 'created', 'authorized',
    'investigated', 'investigated_by', 'exposed', 'testified_at',
    'co_conspirator_of', 'implicated_in', 'accused', 'convicted_in',
    'intelligence_link', 'participated_in', 'influenced', 'mentored_by',
    'married_to', 'related_to', 'business_partner', 'legal_counsel',
    'lobbyist_for', 'spokesperson_for', 'critic_of', 'whistleblower_on',
    'attended', 'hosted_by', 'recruited_by', 'enabled',
    'directed', 'led', 'supervised', 'collaborated_with',
]

PROMPT_TEMPLATE = """You are an OSINT analyst auditing an intelligence database for missing relationships.

TASK: For each person below, identify ALL verifiable relationships to entities in the master list that are NOT already captured in their current connections.

PEOPLE TO AUDIT:
{people_block}

MASTER ENTITY LIST ({entity_count} entities):
{entity_list}

ALREADY DISCOVERED BY OTHER AGENTS (skip these):
{ledger_block}

RULES:
- Only output relationships you are confident are factually accurate based on public record
- Use Google Search to verify connections when possible
- Evidence tier must be "documented" (official records, court filings, legislation) or "credible" (quality journalism, on-record testimony, academic research)
- Use specific relationship types from this list: {rel_types}
- Do NOT use vague types like "connected_to" or "associated_with" — be specific about the nature of the connection
- Do NOT repeat relationships already in the person's current connections or the ledger
- Include year_start/year_end when known (null if unknown)
- The "source" field is the person's exact name, "target" is the exact entity name from the master list

Output ONLY a JSON array of relationship objects. No commentary, no markdown fences.
Example format:
[
  {{"source": "Person Name", "target": "Entity Name", "type": "member_of", "tier": "documented", "desc": "Served on the board of directors 2001-2005", "year_start": 2001, "year_end": 2005}},
  ...
]

If no new relationships are found for a person, omit them entirely (empty results are fine).
Output the JSON array now:"""


def load_shared_data():
    with open(os.path.join(BASE, 'entity_list.json')) as f:
        entity_list = json.load(f)
    return entity_list


def load_batch(batch_num):
    with open(os.path.join(BASE, f'batch_{batch_num}.json')) as f:
        return json.load(f)


def read_ledger():
    """Read all discovered relationships from the shared ledger."""
    entries = []
    try:
        with open(LEDGER_PATH, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))
    except FileNotFoundError:
        pass
    return entries


def append_to_ledger(relationships):
    """Append new relationships to the shared ledger (atomic append)."""
    with open(LEDGER_PATH, 'a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        for rel in relationships:
            f.write(json.dumps(rel, separators=(',', ':')) + '\n')
        fcntl.flock(f, fcntl.LOCK_UN)


def build_people_block(people):
    """Format people with their current connections for the prompt."""
    lines = []
    for p in people:
        conns = p.get('current_connections', [])
        conn_str = ', '.join(
            f"{c['type']}→{c.get('entity_name', '?')}"
            for c in conns[:15]
        ) if conns else '(none)'
        lines.append(f"- {p['name']} (id={p['id']}): {p['description'][:120]}")
        lines.append(f"  Current: {conn_str}")
    return '\n'.join(lines)


def build_entity_list_str(entity_list):
    """Compact entity list for the prompt."""
    return '\n'.join(f"- {e['name']} ({e['type']})" for e in entity_list)


def build_ledger_block(ledger_entries, people_names):
    """Filter ledger to entries relevant to this sub-batch's people."""
    relevant = []
    name_set = set(people_names)
    for entry in ledger_entries:
        if entry.get('source') in name_set or entry.get('target') in name_set:
            relevant.append(f"  {entry['source']} → {entry['target']} ({entry['type']})")
    if not relevant:
        return '(none yet)'
    return '\n'.join(relevant[:100])


def enrich_people_with_entity_names(people, entity_list):
    """Add entity names to current connections for display."""
    id_to_name = {e['id']: e['name'] for e in entity_list}
    for p in people:
        for conn in p.get('current_connections', []):
            conn['entity_name'] = id_to_name.get(conn.get('entity_id'), '?')


def call_api(client, prompt):
    """Make a single Gemini API call with Google Search grounding."""
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())],
            temperature=0.2,
            max_output_tokens=8192,
        ),
    )
    return response.text


def parse_response(text):
    """Parse JSON array from API response, handling common issues."""
    text = text.strip()
    # Strip markdown fences if present
    if text.startswith('```'):
        text = text.split('\n', 1)[1] if '\n' in text else text[3:]
    if text.endswith('```'):
        text = text.rsplit('```', 1)[0]
    text = text.strip()
    if text.startswith('json'):
        text = text[4:].strip()

    try:
        result = json.loads(text)
        if isinstance(result, list):
            return result
        return []
    except json.JSONDecodeError as e:
        print(f"  WARNING: JSON parse error: {e}")
        print(f"  Raw response (first 500 chars): {text[:500]}")
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch', type=int, required=True)
    args = parser.parse_args()

    batch_num = args.batch
    print(f"[Batch {batch_num}] Starting enrichment worker (Gemini 2.5 Flash + Search)")

    # Load data
    entity_list = load_shared_data()
    people = load_batch(batch_num)
    enrich_people_with_entity_names(people, entity_list)

    entity_list_str = build_entity_list_str(entity_list)
    client = genai.Client()

    output_path = os.path.join(RESULTS_DIR, f'batch_{batch_num}.jsonl')
    total_found = 0

    # Process in sub-batches
    for i in range(0, len(people), SUB_BATCH_SIZE):
        sub_batch = people[i:i + SUB_BATCH_SIZE]
        sub_num = i // SUB_BATCH_SIZE
        people_names = [p['name'] for p in sub_batch]

        print(f"[Batch {batch_num}] Sub-batch {sub_num}: {', '.join(people_names[:5])}{'...' if len(people_names) > 5 else ''}")

        # Read current ledger for dedup context
        ledger = read_ledger()
        ledger_block = build_ledger_block(ledger, people_names)

        # Build prompt
        prompt = PROMPT_TEMPLATE.format(
            people_block=build_people_block(sub_batch),
            entity_count=len(entity_list),
            entity_list=entity_list_str,
            ledger_block=ledger_block,
            rel_types=', '.join(RELATIONSHIP_TYPES),
        )

        # Call API with retry
        relationships = []
        for attempt in range(3):
            try:
                response_text = call_api(client, prompt)
                relationships = parse_response(response_text)
                break
            except Exception as e:
                err_str = str(e)
                if '429' in err_str or 'RESOURCE_EXHAUSTED' in err_str:
                    wait = 30 * (attempt + 1)
                    print(f"  Rate limited, waiting {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"  ERROR (attempt {attempt+1}): {err_str[:120]}")
                    if attempt == 2:
                        print(f"  Giving up on this sub-batch")

        # Filter valid relationships
        valid = []
        for rel in relationships:
            if not all(k in rel for k in ('source', 'target', 'type', 'tier')):
                continue
            if rel['tier'] not in ('documented', 'credible'):
                continue
            if rel['type'] in ('connected_to', 'associated_with'):
                continue
            valid.append(rel)

        # Append to ledger and batch output
        if valid:
            append_to_ledger(valid)
            with open(output_path, 'a') as f:
                for rel in valid:
                    f.write(json.dumps(rel, separators=(',', ':')) + '\n')

        total_found += len(valid)
        print(f"  Found {len(valid)} new relationships (total so far: {total_found})")

        # Rate limit courtesy — Gemini free tier is 15 RPM
        time.sleep(5)

    print(f"[Batch {batch_num}] COMPLETE — {total_found} relationships found")
    print(f"[Batch {batch_num}] Results: {output_path}")


if __name__ == '__main__':
    main()
