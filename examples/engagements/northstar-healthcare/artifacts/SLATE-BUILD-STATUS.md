# Slate Build Status: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Upstream:** `ONTOLOGY-ARCHITECTURE.md`

## Application Summary

| App | Why Slate | Primary workflow | Status | Demo ready? |
|-----|-----------|------------------|--------|-------------|
| Executive Throughput Situation Room | leadership wanted a boardroom-quality capacity narrative spanning sites, transfers, and discharge pressure | daily 16:00 throughput review | GREEN | Yes |

## Integration Inventory

| Surface | Data source | Interaction pattern | State |
|---------|-------------|---------------------|-------|
| system capacity banner | capacity-risk aggregates | read-only | Done |
| hospital comparison panel | site-level patient-flow aggregates | read-only | Done |
| transfer backlog trend | transfer-request output | read-only drillthrough | Done |

## Quality Risks

| Risk | Why it matters | Mitigation |
|------|----------------|------------|
| executives could mistake wallboard for operator workflow | wrong audience bypasses command center | keep read-only and training-specific |
| one site asks for patient-level detail in leadership room | PHI and purpose creep | deny request and preserve aggregate-only design |
| custom visual requests may expand scope weekly | maintenance burden | lock the board to leadership review questions only |

## Next Steps

1. [ ] Keep Slate scope narrow and justified.
2. [ ] Hand actual user flows to reviewer and QA.
3. [ ] Record any custom integration or governance burden explicitly.
