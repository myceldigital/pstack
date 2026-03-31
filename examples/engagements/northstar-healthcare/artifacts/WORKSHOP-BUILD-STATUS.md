# Workshop Build Status: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Upstream:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-ARCHITECTURE.md`

## App Summary

| App/Page | Primary operator | Decision supported | Status | Ready for demo? |
|----------|------------------|--------------------|--------|-----------------|
| Capacity Queue | capacity nurse | which patient-flow case to address first | GREEN | Yes |
| Bed Matching Detail | capacity nurse + charge nurse | which bed is truly available and safe | GREEN | Yes |
| Discharge Barrier Board | case management + unit leaders | which discharge blockers need escalation | GREEN | Yes |
| Transfer Escalation View | transfer center | where a transfer is stuck and who owns next step | AMBER | Yes |

## Widget And Flow Inventory

| Page | Widget/Event | Backing object/action | State |
|------|--------------|----------------------|-------|
| Capacity Queue | ranked queue grid | `PatientFlowCase` + placement score | Done |
| Bed Matching Detail | candidate-bed table with staffing context | `Bed`, `StaffingWindow` | Done |
| Discharge Barrier Board | aging-by-owner swimlane | `DischargeBarrier` | Done |
| Transfer Escalation View | acknowledge transfer escalation button | `AcknowledgeTransferEscalation` | In progress |
| Capacity Queue | command summary banner | capacity risk function | Done |

## UX Decisions

| Decision | Why | Locked? | Follow-up |
|----------|-----|---------|----------|
| de-identified labels on shared screens | reduce unnecessary PHI spread during huddles | Yes | preserve in all command-center pages |
| ranked options instead of single "best bed" answer | nursing leadership rejected black-box certainty | Yes | retain rationale panel for every ranking |
| barrier board separate from placement queue | discharge teams own a different workflow than placement nurses | Yes | add quick links between views |
| transfer escalation kept narrow in pilot | transfer-center process differed by site | Yes | phase 2 can standardize more |

## Demo Gaps

| Gap | User impact | Workaround | Owner |
|-----|-------------|------------|-------|
| acknowledge-transfer action not yet wired to support rota | manual note still needed after click in rehearsal | transfer-center lead confirms by secure chat | Workshop builder |
| one telemetry unit lacks bed-color mapping parity | bed state appears generic | pilot scope excludes that unit for demo | Workshop builder |
| printable handoff view not optimized | some command-center staff still want paper huddle sheet | export queue summary as CSV | DS |

## Next Steps

1. [ ] Confirm the demo flow maps directly to the bed-assignment and discharge-barrier decisions.
2. [ ] Hand app context and action wiring to `/aip-architect`.
3. [ ] Record any PHI, support-rota, or site-specific compromises that should not ship unchanged.
