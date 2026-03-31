# OSDK Build Status Template

**Usage:** Produced by `/osdk-developer`. Consumed by `/foundry-reviewer`, `/foundry-security`, `/foundry-qa`.

---

# OSDK Build Status: [Customer Name]

**Date:** [YYYY-MM-DD]
**Upstream:** `ONTOLOGY-ARCHITECTURE.md`

## Application Summary

| App | Why OSDK | Primary users | Status | Scope locked? |
|-----|----------|---------------|--------|---------------|
| [Planner app] | [custom workflow not feasible in Workshop] | [ops planners] | [GREEN/AMBER/RED] | [Yes/No] |

## Integration Surface

| Object/action/function | Access type | OAuth scope | Notes |
|------------------------|-------------|-------------|-------|
| [Shipment] | [read] | [shipment.read] | [note] |

## Build Status

| Area | Status | Evidence | Gap |
|------|--------|----------|-----|
| Auth flow | [Done/In progress/Blocked] | [what works] | [issue] |
| Core user flow | [Done/In progress/Blocked] | [what works] | [issue] |
| Error handling | [Done/In progress/Blocked] | [what works] | [issue] |

## Next Steps

1. [ ] Validate that OSDK was truly necessary.
2. [ ] Hand OAuth scope decisions to `/foundry-security`.
3. [ ] Record any production hardening gaps before QA.
