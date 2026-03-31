# OSDK Build Status: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Upstream:** `ONTOLOGY-ARCHITECTURE.md`

## Application Summary

| App | Why OSDK | Primary users | Status | Scope locked? |
|-----|----------|---------------|--------|---------------|
| Transfer Center Escalation Console | transfer-center workflow needs fine-grained role logic, acknowledgment routing, and audit detail beyond Workshop convenience | transfer center coordinators, throughput supervisors | GREEN | Yes |

## Integration Surface

| Object/action/function | Access type | OAuth scope | Notes |
|------------------------|-------------|-------------|-------|
| `TransferRequest` | read/update acknowledgement only | `transfer.read`, `transfer.acknowledge` | no clinical-system writeback |
| `PatientFlowCase` | read | `patientflow.read` | de-identified operational context only |
| `capacityRiskBand()` | read | `function.read` | summary banner for supervisors |

## Build Status

| Area | Status | Evidence | Gap |
|------|--------|----------|-----|
| Auth flow | Done | hospital SSO and role mapping tested in staging | prod group sync pending |
| Core user flow | Done | coordinator can acknowledge, assign, and note next step | secure-message integration intentionally deferred |
| Error handling | In progress | expired session and invalid role states handled | duplicate acknowledgment race still needs hardening |

## Next Steps

1. [ ] Validate that OSDK remains the right choice for transfer-center role complexity.
2. [ ] Hand OAuth scope decisions to `/foundry-security`.
3. [ ] Record remaining production hardening gaps before QA sign-off.
