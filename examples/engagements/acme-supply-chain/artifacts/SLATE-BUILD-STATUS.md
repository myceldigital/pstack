# Slate Build Status: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Upstream:** `ONTOLOGY-ARCHITECTURE.md`

## Application Summary

| App | Why Slate | Primary workflow | Status | Demo ready? |
|-----|-----------|------------------|--------|-------------|
| Executive Service-Risk Wallboard | leadership wanted a highly formatted morning review surface spanning plants and customer tiers | 08:00 executive stand-up | GREEN | Yes |

## Integration Inventory

| Surface | Data source | Interaction pattern | State |
|---------|-------------|---------------------|-------|
| KPI header | ontology functions | read-only | Done |
| customer-risk heatmap | aggregated risk-case dataset | read-only | Done |
| top-10 expedite cost panel | risk + request datasets | read-only drillthrough | Done |

## Quality Risks

| Risk | Why it matters | Mitigation |
|------|----------------|------------|
| custom KPI formatting could drift from Workshop logic | leaders may see different numbers than planners | share one backing aggregate dataset |
| wallboard becomes default operator surface | wrong audience may bypass operational workflow | keep it read-only and position as executive view only |
| demand for more custom visuals expands scope | maintenance burden rises quickly | freeze scope to leadership review needs |

## Next Steps

1. [ ] Keep Slate scope narrow and justified.
2. [ ] Hand actual user flows to reviewer and QA.
3. [ ] Record custom integration and maintenance burden explicitly for phase-2 decisions.
