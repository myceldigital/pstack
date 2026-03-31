# Ontology Architecture: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Upstream:** `ONTOLOGY-VISION.md`, `BOOTCAMP-SCOPE.md`

## Object Types

### OrderLine

```
Display Name: Customer Order Line
Plural: Customer Order Lines
Description: A promised customer order line whose fulfillment risk is actively monitored.
Primary Key: order_line_id (string)
Title Property: order_line_label
Icon: shipping-box
Backing Dataset: /acme/supply_chain/output/order_lines_enriched
```

| Property | Display Name | Type | Backing Column | Required | Editable | Searchable | Description |
|----------|-------------|------|----------------|----------|----------|------------|-------------|
| `order_line_id` | Order Line ID | string | order_line_id | Yes | No | Yes | canonical unique key |
| `order_line_label` | Order Line | string | order_line_label | Yes | No | Yes | order + line display label |
| `customer_name` | Customer | string | customer_name | Yes | No | Yes | sold-to customer |
| `promise_date` | Promise Date | date | customer_promise_date | Yes | No | Yes | committed ship date |
| `priority_code` | Priority Code | string | priority_code | Yes | No | Yes | high-touch service tier |
| `shortage_flag` | Shortage Flag | boolean | shortage_flag | Yes | No | No | indicates constrained material |
| `promise_confidence` | Promise Confidence | string | promise_confidence_band | Yes | No | Yes | high/medium/low confidence |
| `recommended_action` | Recommended Action | string | recommended_action | No | No | Yes | model output for triage |

### Shipment

```
Display Name: Shipment
Plural: Shipments
Description: Physical shipment carrying constrained material or customer-bound finished goods.
Primary Key: shipment_id (string)
Title Property: shipment_reference
Icon: truck
Backing Dataset: /acme/supply_chain/output/shipment_status
```

| Property | Display Name | Type | Backing Column | Required | Editable | Searchable | Description |
|----------|-------------|------|----------------|----------|----------|------------|-------------|
| `shipment_id` | Shipment ID | string | shipment_id | Yes | No | Yes | unique shipment key |
| `shipment_reference` | Shipment Reference | string | shipment_reference | Yes | No | Yes | carrier-facing identifier |
| `carrier_name` | Carrier | string | carrier_name | Yes | No | Yes | executing carrier |
| `current_milestone` | Milestone | string | current_milestone | Yes | No | Yes | latest operational milestone |
| `eta_timestamp` | ETA | timestamp | eta_timestamp | No | No | Yes | current ETA |
| `delay_minutes` | Delay Minutes | integer | delay_minutes | No | No | No | computed lateness |
| `freshness_minutes` | Data Age Minutes | integer | freshness_minutes | Yes | No | No | source staleness indicator |

### RiskCase

```
Display Name: Supply Risk Case
Plural: Supply Risk Cases
Description: Actionable operational exception representing a threatened order promise.
Primary Key: risk_case_id (string)
Title Property: risk_case_title
Icon: warning
Backing Dataset: /acme/supply_chain/output/risk_cases
```

| Property | Display Name | Type | Backing Column | Required | Editable | Searchable | Description |
|----------|-------------|------|----------------|----------|----------|------------|-------------|
| `risk_case_id` | Risk Case ID | string | risk_case_id | Yes | No | Yes | unique exception key |
| `risk_case_title` | Title | string | risk_case_title | Yes | No | Yes | human-readable risk summary |
| `severity` | Severity | string | severity | Yes | No | Yes | low/medium/high/critical |
| `root_cause_type` | Root Cause | string | root_cause_type | Yes | No | Yes | transit, supplier, inventory, quality |
| `owner` | Owner | string | owner | No | Yes | Yes | assigned planner or buyer |
| `aging_hours` | Aging Hours | decimal | aging_hours | Yes | No | No | time since case opened |
| `decision_deadline` | Decision Deadline | timestamp | decision_deadline | Yes | No | Yes | latest safe intervention time |
| `status` | Status | string | case_status | Yes | Yes | Yes | open, in review, escalated, closed |

### ExpediteRequest

```
Display Name: Expedite Request
Plural: Expedite Requests
Description: Governed request to spend for freight expedite or re-sequence critical supply.
Primary Key: expedite_request_id (string)
Title Property: expedite_request_title
Icon: lightning
Backing Dataset: /acme/supply_chain/output/expedite_requests
```

| Property | Display Name | Type | Backing Column | Required | Editable | Searchable | Description |
|----------|-------------|------|----------------|----------|----------|------------|-------------|
| `expedite_request_id` | Expedite Request ID | string | expedite_request_id | Yes | No | Yes | request key |
| `expedite_request_title` | Title | string | expedite_request_title | Yes | No | Yes | summary label |
| `request_type` | Request Type | string | request_type | Yes | No | Yes | premium freight, supplier escalation, production resequence |
| `approval_state` | Approval State | string | approval_state | Yes | Yes | Yes | draft, pending, approved, rejected |
| `estimated_cost_usd` | Estimated Cost | decimal | estimated_cost_usd | No | Yes | No | expected spend |
| `reason_code` | Reason Code | string | reason_code | Yes | Yes | Yes | controlled justification |
| `approver_role` | Approver Role | string | approver_role | Yes | No | Yes | owner of final go/no-go |

## Link Types

| Name | From | To | Cardinality | FK Column | Display (fwd) | Display (rev) |
|------|------|-----|-------------|-----------|---------------|---------------|
| `orderLineToShipment` | `OrderLine` | `Shipment` | many-to-many | shipment_id | fulfilled by shipment | impacts order lines |
| `orderLineToRiskCase` | `OrderLine` | `RiskCase` | one-to-many | risk_case_id | has risk case | targets order line |
| `riskCaseToExpediteRequest` | `RiskCase` | `ExpediteRequest` | one-to-many | expedite_request_id | has expedite request | created for risk case |
| `riskCaseToSupplierCommit` | `RiskCase` | `SupplierCommit` | many-to-one | supplier_commit_id | caused by supplier commit | contributes to risk case |

## Action Types

### CreateExpediteRequest

```
Display Name: Create Expedite Request
Description: Create a governed expedite or escalation request tied to an active risk case.
Object Type: RiskCase
```

| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| `request_type` | string | Yes | must be in approved enum |
| `estimated_cost_usd` | decimal | No | must be >= 0 |
| `reason_code` | string | Yes | controlled code list |
| `justification` | string | Yes | minimum 20 characters |

**Logic:** creates a pending expedite request record and sets risk case status to `in_review` if approval is required.  
**Audit:** Yes

### AssignRiskOwner

```
Display Name: Assign Risk Owner
Description: Assign a planner or buyer to an active supply risk case.
Object Type: RiskCase
```

| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| `owner` | string | Yes | must resolve to approved role group |
| `due_by` | timestamp | Yes | must be in the future |

**Logic:** updates ownership fields and emits SLA tracking event.  
**Audit:** Yes
