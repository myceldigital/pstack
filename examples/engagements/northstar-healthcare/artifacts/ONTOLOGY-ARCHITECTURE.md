# Ontology Architecture: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Upstream:** `ONTOLOGY-VISION.md`, `BOOTCAMP-SCOPE.md`

## Object Types

### PatientFlowCase

```
Display Name: Patient Flow Case
Plural: Patient Flow Cases
Description: Operational representation of a patient waiting on placement, transfer, or discharge movement.
Primary Key: patient_flow_case_id (string)
Title Property: case_label
Icon: hospital-bed
Backing Dataset: /northstar/patient_flow/output/patient_flow_cases
```

| Property | Display Name | Type | Backing Column | Required | Editable | Searchable | Description |
|----------|-------------|------|----------------|----------|----------|------------|-------------|
| `patient_flow_case_id` | Flow Case ID | string | patient_flow_case_id | Yes | No | Yes | canonical operational case key |
| `case_label` | Case Label | string | case_label | Yes | No | Yes | de-identified operational label |
| `site` | Site | string | site_code | Yes | No | Yes | hospital/site |
| `current_state` | Current State | string | current_state | Yes | No | Yes | awaiting bed, discharge pending, transfer pending |
| `urgency_tier` | Urgency | string | urgency_tier | Yes | No | Yes | routine, urgent, critical |
| `required_level_of_care` | Level of Care | string | level_of_care | Yes | No | Yes | med-surg, telemetry, ICU |
| `placement_priority_score` | Placement Score | integer | placement_priority_score | Yes | No | No | operational priority |
| `owner` | Flow Owner | string | owner | No | Yes | Yes | command-center coordinator |

### Bed

```
Display Name: Bed
Plural: Beds
Description: Staffed or blocked inpatient bed represented at operational readiness level.
Primary Key: bed_id (string)
Title Property: bed_label
Icon: bed
Backing Dataset: /northstar/patient_flow/output/beds
```

| Property | Display Name | Type | Backing Column | Required | Editable | Searchable | Description |
|----------|-------------|------|----------------|----------|----------|------------|-------------|
| `bed_id` | Bed ID | string | bed_id | Yes | No | Yes | room/bed unique key |
| `bed_label` | Bed | string | bed_label | Yes | No | Yes | human-readable room/bed |
| `unit` | Unit | string | unit_name | Yes | No | Yes | nursing unit |
| `level_of_care` | Level of Care | string | level_of_care | Yes | No | Yes | capability of bed |
| `isolation_capability` | Isolation Capability | string | isolation_capability | No | No | Yes | none/contact/airborne |
| `clean_status` | Clean Status | string | clean_status | Yes | No | Yes | clean, dirty, in-progress |
| `staffed_flag` | Staffed | boolean | staffed_flag | Yes | No | No | whether bed is safely usable |

### DischargeBarrier

```
Display Name: Discharge Barrier
Plural: Discharge Barriers
Description: Operational blocker preventing expected discharge or downstream bed release.
Primary Key: discharge_barrier_id (string)
Title Property: barrier_title
Icon: warning
Backing Dataset: /northstar/patient_flow/output/discharge_barriers
```

| Property | Display Name | Type | Backing Column | Required | Editable | Searchable | Description |
|----------|-------------|------|----------------|----------|----------|------------|-------------|
| `discharge_barrier_id` | Barrier ID | string | discharge_barrier_id | Yes | No | Yes | unique barrier key |
| `barrier_title` | Barrier | string | barrier_title | Yes | No | Yes | operational summary |
| `barrier_type` | Barrier Type | string | barrier_type | Yes | No | Yes | transport, placement, case management, EVS |
| `owner_team` | Owner Team | string | owner_team | Yes | No | Yes | accountable function |
| `aging_minutes` | Aging Minutes | integer | aging_minutes | Yes | No | No | duration open |
| `target_clear_time` | Target Clear Time | timestamp | target_clear_time | No | Yes | Yes | expected resolution time |
| `escalation_state` | Escalation State | string | escalation_state | Yes | Yes | Yes | none, pending, escalated, acknowledged |

## Link Types

| Name | From | To | Cardinality | FK Column | Display (fwd) | Display (rev) |
|------|------|-----|-------------|-----------|---------------|---------------|
| `flowCaseToBed` | `PatientFlowCase` | `Bed` | many-to-many | bed_id | candidate bed | candidate for flow case |
| `flowCaseToBarrier` | `PatientFlowCase` | `DischargeBarrier` | one-to-many | discharge_barrier_id | blocked by barrier | impacts patient flow |
| `flowCaseToTransferRequest` | `PatientFlowCase` | `TransferRequest` | optional one-to-one | transfer_request_id | represented by transfer request | represented in command queue |
| `bedToStaffingWindow` | `Bed` | `StaffingWindow` | many-to-one | staffing_window_id | covered by staffing window | covers bed |

## Action Types

### AssignFlowOwner

```
Display Name: Assign Flow Owner
Description: Assign a capacity nurse or transfer-center coordinator to an operational flow case.
Object Type: PatientFlowCase
```

| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| `owner` | string | Yes | must resolve to allowed operational group |
| `due_by` | timestamp | Yes | must be current shift or later |

**Logic:** updates case ownership and creates visible SLA timer.  
**Audit:** Yes

### EscalateBarrier

```
Display Name: Escalate Barrier
Description: Escalate a discharge or turnover barrier when its aging breaches threshold.
Object Type: DischargeBarrier
```

| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| `escalation_reason` | string | Yes | must use controlled reason code |
| `escalate_to` | string | Yes | allowed team lead or supervisor |

**Logic:** marks barrier escalated and emits operational notification event.  
**Audit:** Yes
