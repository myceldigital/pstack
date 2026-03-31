# Bootcamp Scope: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**DS:** Aaron Mensah  
**Industry:** Healthcare operations  
**Engagement type:** New operational deployment

## Executive Summary

Northstar Health wants to create a patient-flow command center spanning bed assignment, discharge readiness, and transfer escalation across its adult acute-care hospitals. The bootcamp is scoped to prove that capacity nurses can see the right bottlenecks, coordinate the next operational action, and move patients through the system faster without creating unsafe or non-compliant workflows.

## Use Cases

### Use Case 1: Prioritize Bed Assignment During Capacity Surge ★★★ HEADLINER

**Operational decision:** Which waiting patient should receive the next available staffed bed, and what blocker must be cleared first?  
**Current workflow:** Capacity nurses reconcile Epic ADT, bed-board updates, staffing rosters, and phone calls from unit charge nurses.  
**Workflow gap:** Bed status, staffing, and discharge readiness are visible in separate systems, so placements are delayed and transfer-center staff escalate manually.  
**Success metric:** Reduce median bed assignment latency from 52 minutes to under 20 minutes between bed-available signal and placement decision.  
**Data readiness:** 8/10  
**Estimated build time:** 4 bootcamp days  
**Demo audience:** COO, chief nursing officer, capacity command manager, CMIO

#### Preliminary Ontology Sketch
- Object types: `PatientFlowCase`, `Bed`, `Unit`, `DischargeBarrier`, `TransferRequest`, `StaffingWindow`
- Key relationships: patient flow case linked to current unit, candidate bed, discharge barriers, transfer request, staffing posture
- Critical properties: level of care, isolation requirement, transfer urgency, barrier aging, staffed-bed availability
- Action types: assign coordinator, escalate discharge barrier, acknowledge transfer request, mark bed-cleaning escalation

### Use Case 2: Accelerate Discharge Readiness ★★ QUICK WIN

**Operational decision:** Which discharge-ready patients are blocked by solvable operational barriers today?  
**Current workflow:** case management huddles with nursing and EVS via phone and secure chat.  
**Workflow gap:** barriers are tracked inconsistently and often not linked to downstream bed demand.  
**Success metric:** Reduce avoidable discharge delay minutes by 15% on medicine units in pilot hospitals.  
**Data readiness:** 7/10  
**Estimated build time:** 2 bootcamp days  
**Demo audience:** care management director, EVS operations lead, medicine service line leader

#### Preliminary Ontology Sketch
- Object types: `DischargeBarrier`, `BedTurnoverTask`, `PatientFlowCase`, `CareTeam`
- Key relationships: barrier to patient, barrier to accountable team, bed turnover task to bed and EVS owner
- Critical properties: barrier type, target completion time, handoff status, blocker severity
- Action types: escalate barrier, assign action owner, acknowledge room clean delay

### Deferred Use Cases

- Elective surgery smoothing: deferred because OR scheduling integration was outside the bootcamp data-access window.
- Readmission-risk intervention routing: deferred because it would broaden from operations into care-management clinical decision support.

## Data Inventory

| Source System | Data | Format | Refresh | Owner | Readiness | Bootcamp Day |
|---------------|------|--------|---------|-------|-----------|--------------|
| Epic Clarity | ADT, patient census, discharge orders, level of care | JDBC | 15 min | clinical data platform lead | 9/10 | Day 1 |
| TeleTracking | bed status, cleaning status, room readiness | API | 5 min | capacity systems manager | 8/10 | Day 1 |
| Transfer Center tool | transfer queue, acceptance notes, escalation state | CSV + API | 15 min | transfer center director | 7/10 | Day 2 |
| Kronos staffing export | staffed beds, shift assignments, charge nurse roster | CSV | hourly | nursing operations analyst | 6/10 | Day 2 |
| EVS mobile app export | room clean task status, aging, supervisor notes | CSV | 15 min | EVS operations manager | 6/10 | Day 3 |

## Stakeholder Map

| Role | Name | Cares about | Skeptical of | Demo target |
|------|------|-------------|--------------|-------------|
| COO sponsor | Rebecca Long | throughput, diversion reduction, transfer performance | another dashboard without action accountability | final-day executive demo |
| Chief Nursing Officer | Denise Harper | nurse workload and safe patient placement | black-box prioritization | day 4 walkthrough |
| Capacity command manager | Luis Ortega | faster placement and cleaner escalation | stale staffing data | daily work session |
| CMIO | Dr. Priya Raman | compliance, explainability, clinician trust | AI recommendations that look clinical | architecture and agent review |
| Transfer center director | Hannah Lee | transfer acceptance speed and visibility | unit-level resistance to central prioritization | day 3 flow review |

## Bootcamp Schedule (Proposed)

| Day | Morning | Afternoon | Demo/Check-in |
|-----|---------|-----------|---------------|
| 1 | command-center goals, Epic + TeleTracking review | patient-flow ontology sketch | sponsor checkpoint |
| 2 | transfer-center and staffing workflow mapping | pipeline plan, access scoping, PHI review | capacity manager review |
| 3 | ontology architecture lock, Workshop page flows | first bed-assignment queue slice | nurse leader walkthrough |
| 4 | agent evals, QA planning, security hardening | discharge-barrier and transfer escalation flow | CMIO + security review |
| 5 | rehearsal, rollout design, training prep | executive demo, next-phase call | steering committee |

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| staffing feed is hourly but surge decisions change faster | High | High | show staffing freshness and do not over-automate recommendations |
| patient flow scope drifts into clinical decision support | Medium | High | enforce operations-only language and remove diagnosis-driven logic |
| EVS notes include PHI-adjacent free text | Medium | High | redact or exclude unsafe note fields before ontology exposure |
| transfer center wants direct writeback into Epic | Medium | Medium | keep writeback out of bootcamp and use governed acknowledgement only |
| one hospital has different bed-status codes | Medium | Medium | normalize in clean layer and document site-specific mapping |

## Next Steps

1. [ ] DS to confirm the two pilot hospitals and throughput metrics with the COO office.
2. [ ] Customer to provide service-account access for Epic Clarity and TeleTracking.
3. [ ] Run `/ontology-vision` on bed assignment and discharge readiness scope.
4. [ ] Run `/pipeline-plan` on Epic, bed-board, staffing, transfer-center, and EVS sources.
