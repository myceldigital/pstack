# Workshop Build Status: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Upstream:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-ARCHITECTURE.md`

## App Summary

| App/Page | Primary operator | Decision supported | Status | Ready for demo? |
|----------|------------------|--------------------|--------|-----------------|
| Risk Queue | regional planner | which risk case to triage first | GREEN | Yes |
| Order Drilldown | planner + buyer | is the promise date truly at risk and why | GREEN | Yes |
| Expedite Approval | logistics lead | approve or reject expedite spend | AMBER | Yes |
| Supplier Triage | buyer | escalate supplier or accept delay | GREEN | Yes |

## Widget And Flow Inventory

| Page | Widget/Event | Backing object/action | State |
|------|--------------|----------------------|-------|
| Risk Queue | priority grid with severity and deadline | `RiskCase` | Done |
| Risk Queue | filter chips by plant, customer, root cause | `RiskCase` interface props | Done |
| Order Drilldown | supply-causality timeline | `OrderLine`, `Shipment`, `SupplierCommit` | Done |
| Expedite Approval | create expedite request form | `CreateExpediteRequest` | In progress |
| Supplier Triage | supplier note panel | `RiskCase` + commit note | Done |

## UX Decisions

| Decision | Why | Locked? | Follow-up |
|----------|-----|---------|----------|
| queue-first landing page | planners start in triage, not dashboards | Yes | keep as default in pilot |
| confidence badge next to each recommendation | source freshness is core to trust | Yes | add hover explanation text |
| approval page limited to high/critical cases | keep pilot narrow and auditable | Yes | phase 2 may add medium-risk override |
| no map view in bootcamp | visual lane map looked impressive but slowed decision flow | Yes | revisit only if logistics team asks |

## Demo Gaps

| Gap | User impact | Workaround | Owner |
|-----|-------------|------------|-------|
| expedite approval page lacks finance-code dropdown integration | approver types placeholder code during demo | use pilot code list embedded in form | Workshop builder |
| supplier note history not yet threaded | buyers see latest note only | link to detail table beneath widget | Workshop builder |
| mobile layout not optimized | field supervisors will prefer laptop in pilot | keep mobile out of scope | DS |

## Next Steps

1. [ ] Confirm the demo flow maps directly to the headline expedite decision.
2. [ ] Hand app context and action wiring to `/aip-architect`.
3. [ ] Record the finance-code integration gap so it does not silently ship to production.
