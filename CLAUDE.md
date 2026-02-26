# Intel Console — Ground Rules

## Evidence Discipline
- Every relationship MUST have an evidence tier: documented, credible, inference, speculative
- Every relationship MUST link to at least one source with URL or citation
- Never upgrade a tier without new evidence — always explain the basis
- "Connected_to" is the weakest relationship type — use specific types when possible

## Legal Constraints
- This is a civilian OSINT research tool — all data from public sources
- Sources: congressional records, court filings, FOIA, journalism, academic research
- No classified material, no hacked data, no doxing of private individuals
- Evidence tiers exist to distinguish what's proven from what's inferred

## Code Standards
- Backend: FastAPI + aiosqlite, async everywhere
- Frontend: vanilla JS + SVG (no dependencies), no build step
- SQLite with FTS5 for search
- All API responses use Pydantic models
