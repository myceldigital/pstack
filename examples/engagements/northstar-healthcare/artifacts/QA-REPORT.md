# QA Report: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Overall Health Score:** 90% [PASS]

## Domain Scores

| Domain | Tests | Pass | Fail | Score | Grade |
|--------|-------|------|------|-------|-------|
| Pipelines | 20 | 18 | 2 | 90 | A- |
| Ontology | 15 | 15 | 0 | 96 | A |
| AIP Agents | 10 | 10 | 0 | 95 | A |
| Workshop | 12 | 10 | 2 | 87 | B+ |
| **TOTAL** | **57** | **53** | **4** | **90** | **A-** |

## Failing Tests

| Test | Domain | Expected | Actual | Severity |
|------|--------|----------|--------|----------|
| stale staffing confidence downgrade | Pipelines/Workshop | ranking confidence drops clearly when staffing feed stale >90 min | one compact queue view shows warning but not confidence text | Medium |
| duplicate transfer acknowledgment | OSDK | second ack attempt returns idempotent no-op | duplicate click creates duplicate audit note | Medium |
| unit-specific telemetry bed-code mapping | Workshop | all pilot units mapped to clean status correctly | one telemetry unit uses fallback generic code | Low |
| printable huddle export | Workshop | export preserves queue ordering and barrier owner | export exists but omits owner team | Low |

## Deployment Recommendation

DEPLOY_WITH_MONITORING

The pilot is acceptable for two hospitals under close operational monitoring because the core placement and discharge workflows are solid, the compliance posture is bounded, and the system avoids clinical advice. Production cutover should wait for the stale-staffing UX patch and transfer-acknowledgment idempotency fix.
