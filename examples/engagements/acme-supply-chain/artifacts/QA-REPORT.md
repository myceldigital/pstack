# QA Report: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Overall Health Score:** 91% [PASS]

## Domain Scores

| Domain | Tests | Pass | Fail | Score | Grade |
|--------|-------|------|------|-------|-------|
| Pipelines | 18 | 16 | 2 | 89 | B+ |
| Ontology | 14 | 14 | 0 | 97 | A |
| AIP Agents | 10 | 9 | 1 | 90 | A- |
| Workshop | 12 | 11 | 1 | 92 | A- |
| **TOTAL** | **54** | **50** | **4** | **91** | **A-** |

## Failing Tests

| Test | Domain | Expected | Actual | Severity |
|------|--------|----------|--------|----------|
| supplier freshness badge on order drilldown | Workshop | every supplier-driven recommendation shows confidence downgrade | one panel omits badge on compact layout | Medium |
| unresolved vendor crosswalk queue alert | Pipelines | all unresolved supplier part IDs create alert event | 2 low-volume vendors did not page correctly | Medium |
| OSDK finance code validation | AIP/OSDK | invalid code blocked before draft save | invalid code surfaces at submit time instead | Low |
| draft assistant ambiguity response | AIP Agents | strong warning when shipment and supplier signals conflict | response acceptable but too concise | Low |

## Deployment Recommendation

DEPLOY_WITH_MONITORING

The pilot is acceptable for a controlled North America rollout because the core expedite decision path is strong, governance is explicit, and no critical security findings remain open. Production approval requires the supplier-freshness UX patch and crosswalk alert fix to land before general planner access is enabled.
