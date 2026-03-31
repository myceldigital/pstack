# Ontology Vision: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Upstream:** `BOOTCAMP-SCOPE.md`  
**Mode:** SELECTIVE

## Vision Summary

The ontology focuses on operational flow, not clinical treatment decisions. It models the patient-placement queue, staffed-bed capacity, discharge barriers, and transfer escalations in a way that gives operators shared truth while preserving PHI boundaries and keeping recommendation logic explainable.

## Object Type Hierarchy

### Core Object Types (Bootcamp Build)

| Object Type | Description | Backing Source | Key Properties | Est. Row Count |
|-------------|-------------|----------------|----------------|---------------|
| `PatientFlowCase` | operational view of a patient awaiting placement, discharge, or transfer action | Epic + TeleTracking + transfer queue | current state, urgency tier, destination need, discharge readiness | 1.8k active |
| `Bed` | staffed or blocked inpatient bed | TeleTracking | room, level of care, isolation capability, clean status, staffed flag | 2.4k |
| `DischargeBarrier` | operational blocker delaying discharge or downstream movement | Epic discharge workflow + EVS + case management notes | barrier type, owner team, target clear time, aging | 520 active |
| `TransferRequest` | interfacility or ED-to-inpatient placement request | transfer-center system | requesting site, required level of care, urgency, acceptance state | 190 active |
| `StaffingWindow` | current and upcoming unit staffing posture | Kronos export | staffed beds, nurse ratio, charge nurse on duty, variance to plan | 140 active windows |

### Extended Object Types (Phase 2)

| Object Type | Description | Backing Source | Phase |
|-------------|-------------|----------------|-------|
| `TransportTask` | patient transport bottleneck for room movement | transport dispatch system | Phase 2 |
| `ObservationConversionCase` | observation-to-inpatient decision queue | Epic utilization management | Phase 2 |
| `ORBoardingCase` | surgical boarding impact on throughput | OR scheduling systems | Phase 3 |

## Link Topology

| From | Relationship | To | Cardinality | Operational Meaning |
|------|-------------|-----|-------------|-------------------|
| `PatientFlowCase` | candidates_for | `Bed` | one-to-many | patient may qualify for several beds but only one is operationally optimal |
| `PatientFlowCase` | blocked_by | `DischargeBarrier` | one-to-many | unresolved barriers prevent movement |
| `PatientFlowCase` | influenced_by | `StaffingWindow` | many-to-one | staffing posture constrains available beds |
| `TransferRequest` | represented_by | `PatientFlowCase` | one-to-one | transfer request becomes actionable in same command queue |
| `Bed` | covered_by | `StaffingWindow` | many-to-one | bed availability is meaningful only if staffing exists |

## Action Types

| Action | Trigger | Modifies | Validates | Downstream Effect |
|--------|---------|----------|-----------|-------------------|
| `AssignFlowOwner` | a case needs accountability | `PatientFlowCase.owner` | owner in allowed operational roles | creates clear coordinator ownership |
| `EscalateBarrier` | discharge barrier aging exceeds threshold | `DischargeBarrier` | escalation reason required | pages accountable team lead |
| `AcknowledgeTransferEscalation` | transfer center needs unit response | `TransferRequest` | acknowledgment timestamp + responder | audit trail for throughput review |
| `MarkBedCleanDelay` | EVS task exceeds SLA | `Bed` + linked turnover task | task exists and bed not yet ready | exposes room turnover bottleneck |

## Interfaces

| Interface | Properties | Applied To |
|-----------|------------|------------|
| `ShiftScoped` | site, unit, shift, role group | `PatientFlowCase`, `Bed`, `StaffingWindow` |
| `Escalatable` | owner, aging, escalation state, due by | `DischargeBarrier`, `TransferRequest`, `PatientFlowCase` |
| `FreshnessTracked` | source timestamp, age, confidence | `StaffingWindow`, `Bed`, `TransferRequest` |

## Functions

| Function | Input | Output | Purpose |
|----------|-------|--------|---------|
| `placementPriorityScore()` | patient-flow, bed, staffing, barrier signals | integer 0-100 | prioritize placement queue |
| `dischargeBlockerSummary()` | barrier set | structured summary | explain what must clear next |
| `capacityRiskBand()` | staffed beds, pending discharges, incoming demand | low/medium/high | support command-center pacing |

## Phased Rollout

| Phase | Object Types | Links | Actions | Timeline |
|-------|-------------|-------|---------|----------|
| Bootcamp | `PatientFlowCase`, `Bed`, `DischargeBarrier`, `TransferRequest`, `StaffingWindow` | core placement and blockage links | assign owner, escalate barrier, acknowledge transfer | Days 1-5 |
| Phase 2 | add transport and observation-conversion views | transport and utilization links | transport escalation | Weeks 2-6 |
| Phase 3 | add surgical-flow overlays | broader perioperative capacity links | OR backlog escalations | Months 2-6 |

## Design Decisions

| Decision | Options Considered | Chosen | Rationale |
|----------|-------------------|--------|-----------|
| patient object scope | generic patient object vs operational case object | operational `PatientFlowCase` | keeps focus on throughput and avoids unnecessary PHI spread |
| staffing representation | static unit attribute vs time-window object | `StaffingWindow` object | staffing changes by shift and must be visible as a first-class constraint |
| transfer modeling | separate queue only vs unified flow case | linked but distinct `TransferRequest` | preserves transfer-center workflow and audit semantics |
| recommendation language | best-bed recommendation vs ranked operational options | ranked options with rationale | safer and more acceptable to nursing leadership |
