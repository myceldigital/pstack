# Pipeline Build Status: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Upstream:** `PIPELINE-ARCHITECTURE.md`, `DATA-CONNECTION-STATUS.md`, `ONTOLOGY-ARCHITECTURE.md`

## Build Summary

| Dataset | Layer | Purpose | Build status | Data quality | Ontology ready? |
|---------|-------|---------|--------------|--------------|-----------------|
| `/northstar/output/patient_flow_cases` | OUTPUT | command-center queue | GREEN | 97.8/100 | Yes |
| `/northstar/output/beds` | OUTPUT | bed readiness and capability | GREEN | 98.1/100 | Yes |
| `/northstar/output/discharge_barriers` | OUTPUT | blocker management | GREEN | 95.6/100 | Yes |
| `/northstar/output/transfer_requests` | OUTPUT | transfer-center queue | GREEN | 96.9/100 | Yes |
| `/northstar/output/staffing_windows` | OUTPUT | staffed-bed posture | AMBER | 92.8/100 | Yes |

## Transform Inventory

| Transform | Input(s) | Output | Tool | Incremental strategy | Owner |
|-----------|----------|--------|------|----------------------|-------|
| `patient_flow_case_builder_cr` | Epic ADT + bed board + transfer queue | patient flow cases | CR | snapshot+delta | platform engineer |
| `bed_readiness_pb` | bed-board | beds | PB | snapshot+delta | data engineer |
| `transfer_request_merge_pb` | transfer API + CSV | transfer requests | PB | snapshot+delta | data engineer |
| `staffing_window_pb` | Kronos staffing | staffing windows | PB | full hourly | nursing ops analyst |
| `discharge_barrier_builder_cr` | Epic + EVS + case-management states | discharge barriers | CR | full over pilot units | platform engineer |

## Quality Checks

| Check | Dataset | Threshold | Current result | Action if failed |
|-------|---------|-----------|----------------|------------------|
| Null primary keys | all outputs | 0 | 0 | block publish |
| Candidate-bed validity | patient flow cases | >97% | 97.4% | quarantine invalid candidate set |
| Staffing freshness | staffing windows | <90 min | 63 min median | degrade confidence when stale |
| Barrier owner coverage | discharge barriers | >95% | 95.2% | route unknown owner to command-center fallback queue |
| PHI redaction | EVS-derived barrier data | 100% | 100% in sampled test set | block publish on any leakage |

## Backing Readiness

| Ontology object/link/action dependency | Supporting dataset or transform | Ready? | Gap |
|---------------------------------------|----------------------------------|--------|-----|
| `PatientFlowCase` object | `/northstar/output/patient_flow_cases` | Yes | staffing confidence caveat remains |
| `Bed` object | `/northstar/output/beds` | Yes | one local site code mapping still monitored |
| `DischargeBarrier` object | `discharge_barrier_builder_cr` | Yes | owner-team mapping sparse for one service line |
| `AssignFlowOwner` action | patient flow cases + role groups | Yes | none |
| `EscalateBarrier` action | discharge barriers + escalation routing | Yes | on-call rota integration in progress |

## Exception Path Readiness

| Workflow or exception path | Trigger | Primary handling path | Manual fallback | Residual risk if fallback remains | Ready for review? |
|----------------------------|---------|-----------------------|-----------------|-----------------------------------|-------------------|
| Staffing feed stale during surge | latest staffing file older than 90 minutes | confidence downgrade and command-center warning | call nursing supervisor and update shift board manually | temporary overstatement of available beds | Yes |
| EVS task missing for dirty bed | room status says dirty but no active clean task | auto-create barrier stub and page EVS lead | charge nurse phones EVS supervisor | room turnover delay remains manual until task reconciled | Yes |
| Transfer acceptance note not synced | transfer center updates API before CSV | API path wins and CSV patch follows | transfer center lead confirms disposition by secure call | a small set of transfer cases may display ambiguous state for one cycle | Yes |

## Blockers And Decisions

| Blocker | Impact | Needs architecture change? | Needs DS decision? |
|---------|--------|----------------------------|--------------------|
| hourly staffing source remains operationally coarse | placement confidence can only be medium during rapid shift changes | No | Yes |
| one service line does not consistently populate discharge barrier owner | escalations route to fallback queue | No | No |
| request for direct Epic writeback emerged during demo prep | governance and scope risk | Yes | Yes |

## Next Steps

1. [ ] Hand validated outputs to review and QA.
2. [ ] Flag any ontology-backing mismatch immediately.
3. [ ] Make every exception path and manual fallback explicit before calling the build review-ready.
4. [ ] Keep incremental strategy and quality thresholds aligned with the architecture doc.
