# OSDK Build Status: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Upstream:** `ONTOLOGY-ARCHITECTURE.md`

## Application Summary

| App | Why OSDK | Primary users | Status | Scope locked? |
|-----|----------|---------------|--------|---------------|
| Expedite Approval Console | approval workflow needs custom finance and exception logic not ideal in pure Workshop | logistics approvers, supply-chain finance | AMBER | Yes |

## Integration Surface

| Object/action/function | Access type | OAuth scope | Notes |
|------------------------|-------------|-------------|-------|
| `RiskCase` | read | `riskcase.read` | pull evidence into approval page |
| `ExpediteRequest` | read/write draft only | `expedite.read`, `expedite.write` | submit still approval-gated |
| `recommendedIntervention()` | read | `function.read` | display recommendation rationale |

## Build Status

| Area | Status | Evidence | Gap |
|------|--------|----------|-----|
| Auth flow | Done | SSO login works in staging | prod group mapping pending |
| Core user flow | In progress | approver can review request and save decision note | SAP cost-center validation not wired |
| Error handling | In progress | invalid scope and expired session paths tested | finance-system outage state still basic |

## Next Steps

1. [ ] Validate that OSDK was truly necessary for finance-integrated approval.
2. [ ] Hand OAuth scope decisions to `/foundry-security`.
3. [ ] Record production hardening gaps before QA signs off on rollout.
