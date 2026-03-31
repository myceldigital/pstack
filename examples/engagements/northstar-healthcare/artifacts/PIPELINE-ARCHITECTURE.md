# Pipeline Architecture: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Upstream:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-VISION.md`

## Source-to-Ontology Data Flow

| Source System | Connection | Raw Dataset | Clean Dataset | Transform | Output | Object Type |
|---------------|-----------|-------------|---------------|-----------|--------|-------------|
| Epic Clarity | JDBC | `/northstar/raw/epic/adt` | `/northstar/clean/epic/adt_clean` | `patient_flow_case_builder_cr` | `/northstar/output/patient_flow_cases` | `PatientFlowCase` |
| TeleTracking | API | `/northstar/raw/bedboard/beds` | `/northstar/clean/bedboard/beds_clean` | `bed_readiness_pb` | `/northstar/output/beds` | `Bed` |
| Transfer Center | API + CSV | `/northstar/raw/transfer/requests` | `/northstar/clean/transfer/requests_clean` | `transfer_request_merge_pb` | `/northstar/output/transfer_requests` | `TransferRequest` |
| Kronos staffing | CSV | `/northstar/raw/staffing/windows` | `/northstar/clean/staffing/windows_clean` | `staffing_window_pb` | `/northstar/output/staffing_windows` | `StaffingWindow` |
| EVS mobile export | CSV | `/northstar/raw/evs/tasks` | `/northstar/clean/evs/tasks_clean` | `discharge_barrier_builder_cr` | `/northstar/output/discharge_barriers` | `DischargeBarrier` |

## Connection Configuration

### Epic Clarity

```
Type: JDBC
Details: read-only replica, PHI-scoped service account, customer network access required
Sync Mode: Incremental by encounter and order update timestamps
Schedule: every 15 minutes
Agent Required: Yes
```

### TeleTracking

```
Type: REST API
Details: internal bed-board API with token auth
Sync Mode: Snapshot+delta
Schedule: every 5 minutes
Agent Required: No
```

### Kronos staffing

```
Type: CSV export
Details: hourly staffing roster from nursing operations analyst
Sync Mode: Snapshot
Schedule: hourly on the half hour
Agent Required: No
```

## Transform DAG

```
RAW -> CLEAN -> TRANSFORM -> OUTPUT

Layer 0 (RAW): preserve Epic, bed-board, transfer, staffing, and EVS payloads with PHI controls
Layer 1 (CLEAN): code normalization, unit/site mapping, role mapping, free-text redaction
Layer 2 (TRANSFORM): placement score inputs, discharge barrier extraction, transfer queue merge, staffed-bed derivation
Layer 3 (OUTPUT): patient flow cases, beds, transfer requests, discharge barriers, staffing windows
```

## Pipeline Tool Assignments

| Transform | Tool | Rationale |
|-----------|------|-----------|
| `patient_flow_case_builder_cr` | CR | joins multiple operational domains and enforces PHI-safe field set |
| `bed_readiness_pb` | PB | straightforward bed-state normalization |
| `transfer_request_merge_pb` | PB | queue merge and status mapping |
| `staffing_window_pb` | PB | simple hourly derivation |
| `discharge_barrier_builder_cr` | CR | extracts barrier semantics and redacts unsafe text |

## Incremental Strategy

| Pipeline | Strategy | Key Column | Notes |
|----------|----------|-----------|-------|
| Epic ADT | Snapshot+Delta | `event_ts` | retain change history for queue debugging |
| bed-board | Snapshot+Delta | `last_changed_at` | frequent refresh due to room turnover |
| transfer requests | Snapshot+Delta | `updated_at` | preserve escalation timeline |
| staffing windows | Full | export timestamp | hourly file small enough for full recompute |
| discharge barriers | Full over pilot units | n/a | deterministic rebuild after redaction and joins |

## Data Quality Checks

| Output Dataset | PK Unique | Null Check | FK Valid | Row Count Range | Freshness |
|----------------|-----------|-----------|---------|-----------------|-----------|
| `/northstar/output/patient_flow_cases` | 100% | state + site > 99.8% | bed candidate links 97% | 1.4k-2.0k | < 20 min |
| `/northstar/output/beds` | 100% | clean status 99.7% | staffing link 95% | 2.2k-2.6k | < 10 min |
| `/northstar/output/discharge_barriers` | 100% | owner team 96% | flow-case link 99% | 400-650 | < 20 min |
| `/northstar/output/transfer_requests` | 100% | urgency 99% | flow-case link 98% | 120-220 | < 20 min |

## Schedule

| Pipeline | Trigger | Schedule | Dependencies |
|----------|---------|----------|-------------|
| Epic ingest | Time | every 15 min | network agent healthy |
| bed-board ingest | Time | every 5 min | API token valid |
| transfer queue ingest | Time | every 15 min | source export and API alignment |
| staffing ingest | Time | hourly | analyst export published |
| barrier build | Upstream | after Epic, EVS, and bed outputs | all pilot-unit datasets green |

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| staffing file is too slow during rapid shift changes | bed availability can look safer than reality | show staffing freshness and confidence prominently |
| EVS notes contain PHI-adjacent text | compliance exposure | strip free text and retain coded blocker semantics only |
| one hospital uses local bed-status codes | inconsistent bed readiness | maintain site-specific mapping and validation tests |
| demand to write back directly into Epic grows | governance risk and project expansion | keep bootcamp actions acknowledgement-only |
