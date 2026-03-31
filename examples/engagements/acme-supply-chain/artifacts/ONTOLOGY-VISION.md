# Ontology Vision: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Upstream:** `BOOTCAMP-SCOPE.md`  
**Mode:** SELECTIVE

## Vision Summary

The bootcamp ontology is centered on operational decisions, not generic supply-chain reporting. The initial build models order risk, supplier commitments, in-transit shipment status, and constrained inventory well enough to support expedite and escalation choices, while intentionally deferring broader planning and finance domains.

## Object Type Hierarchy

### Core Object Types (Bootcamp Build)

| Object Type | Description | Backing Source | Key Properties | Est. Row Count |
|-------------|-------------|----------------|----------------|---------------|
| `OrderLine` | customer-facing make/ship obligation at the promise-date level | SAP ECC | order number, customer promise date, priority code, shortage flag | 180k active |
| `Shipment` | physical movement of a constrained component or finished assembly | Blue Yonder TMS + EDI 214 | current milestone, ETA, carrier, lane, delay minutes | 22k active |
| `InventoryPosition` | available and projected inventory for a material at a plant/DC | Kinaxis export + SAP | on-hand, available-to-promise, coverage hours, substitute available | 14k active |
| `SupplierCommit` | supplier-confirmed quantity/date for an open PO line | Supplier portal + SAP | confirmed date, open qty, commit confidence, supplier tier | 96k active |
| `RiskCase` | normalized operational exception requiring triage | derived transform | risk type, severity, root cause, owner, aging | 3k active |
| `ExpediteRequest` | governed request to spend money or re-prioritize logistics | derived + workflow input | decision type, approval state, cost estimate, rationale | 400 monthly |

### Extended Object Types (Phase 2)

| Object Type | Description | Backing Source | Phase |
|-------------|-------------|----------------|-------|
| `CarrierCapacitySlot` | lane-level booked and available carrier capacity | TMS + carrier API | Phase 2 |
| `QualityHold` | inventory blocked for quality release | MES + QMS | Phase 2 |
| `CustomerPriorityAgreement` | contractual service commitments driving expedite policy | CRM + contract repository | Phase 3 |

## Link Topology

| From | Relationship | To | Cardinality | Operational Meaning |
|------|-------------|-----|-------------|-------------------|
| `OrderLine` | requires | `InventoryPosition` | many-to-one | an order line depends on material availability at a site |
| `OrderLine` | fulfilled_by | `Shipment` | one-to-many | inbound or outbound shipment status affects promise-date confidence |
| `OrderLine` | constrained_by | `SupplierCommit` | one-to-many | supplier commit variance drives shortage risk |
| `RiskCase` | targets | `OrderLine` | many-to-one | the risk case is the triage wrapper around a specific impacted order |
| `RiskCase` | explained_by | `Shipment` | optional many-to-one | shipment delay as primary causal signal |
| `RiskCase` | explained_by | `SupplierCommit` | optional many-to-one | supplier short-ship or delay as primary causal signal |
| `ExpediteRequest` | created_for | `RiskCase` | many-to-one | governed action request tied to a named risk |

## Action Types

| Action | Trigger | Modifies | Validates | Downstream Effect |
|--------|---------|----------|-----------|-------------------|
| `CreateExpediteRequest` | risk severity >= high and planner wants intervention | `ExpediteRequest` | approval tier, cost center, reason code | routes to logistics lead for approval |
| `AssignRiskOwner` | triage handoff needed | `RiskCase.owner` | owner in allowed role set | creates accountability and SLA tracking |
| `AcknowledgeSupplierEscalation` | buyer has contacted supplier | `RiskCase` + `SupplierCommit` note | escalation reason mandatory | preserves audit trail for follow-up |
| `CloseRiskCase` | causal signal cleared and order safe | `RiskCase.status` | no unresolved blockers | removes from active triage queue |

## Interfaces

| Interface | Properties | Applied To |
|-----------|------------|------------|
| `Ownable` | owner, owner team, due by | `RiskCase`, `ExpediteRequest` |
| `RegionScoped` | region, business unit, plant code | `OrderLine`, `Shipment`, `InventoryPosition`, `SupplierCommit` |
| `FreshnessTracked` | source timestamp, age minutes, confidence band | `Shipment`, `SupplierCommit`, `InventoryPosition` |

## Functions

| Function | Input | Output | Purpose |
|----------|-------|--------|---------|
| `riskSeverityScore()` | order line, shipment, inventory, supplier signals | integer 0-100 | consistent prioritization across planners |
| `recommendedIntervention()` | risk case plus cost/service data | recommendation enum | suggest expedite vs wait vs escalate supplier |
| `promiseDateConfidence()` | supply and transit signals | confidence band | explain how safe the promise date currently is |

## Phased Rollout

| Phase | Object Types | Links | Actions | Timeline |
|-------|-------------|-------|---------|----------|
| Bootcamp | `OrderLine`, `Shipment`, `InventoryPosition`, `SupplierCommit`, `RiskCase`, `ExpediteRequest` | critical-path links only | create expedite, assign owner, acknowledge escalation | Days 1-5 |
| Phase 2 | add `CarrierCapacitySlot`, `QualityHold` | lane-capacity and quality blocking links | carrier alternative review | Weeks 2-5 |
| Phase 3 | add customer agreement and network balancing surfaces | enterprise policy links | broader reallocation and customer-date negotiation actions | Months 2-6 |

## Design Decisions

| Decision | Options Considered | Chosen | Rationale |
|----------|-------------------|--------|-----------|
| risk object strategy | compute inline on order line vs separate `RiskCase` object | separate `RiskCase` | keeps triage workflow, ownership, and aging explicit |
| supplier modeling | supplier-level only vs supplier commit line level | commit-line level | planners need line-level causality, not aggregated scorecards |
| writeback scope | direct TMS mutation vs governed request object | governed request object | avoids unsafe production mutation during pilot |
| inventory abstraction | single ATP number vs explicit inventory-position object | explicit object | gives root-cause explainability across plant and substitution context |
