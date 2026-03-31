# Pipeline Build Status: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Upstream:** `PIPELINE-ARCHITECTURE.md`, `DATA-CONNECTION-STATUS.md`, `ONTOLOGY-ARCHITECTURE.md`

## Build Summary

| Dataset | Layer | Purpose | Build status | Data quality | Ontology ready? |
|---------|-------|---------|--------------|--------------|-----------------|
| `/acme/output/order_lines_enriched` | OUTPUT | customer promise and shortage context | GREEN | 98.9/100 | Yes |
| `/acme/output/shipment_status` | OUTPUT | live transit and delay status | GREEN | 97.2/100 | Yes |
| `/acme/output/supplier_commits` | OUTPUT | supplier commit intelligence | AMBER | 93.4/100 | Yes |
| `/acme/output/inventory_positions` | OUTPUT | coverage and substitution posture | GREEN | 96.8/100 | Yes |
| `/acme/output/risk_cases` | OUTPUT | operational exception queue | GREEN | 95.9/100 | Yes |
| `/acme/output/expedite_requests` | OUTPUT | governed action trail | GREEN | 99.4/100 | Yes |

## Transform Inventory

| Transform | Input(s) | Output | Tool | Incremental strategy | Owner |
|-----------|----------|--------|------|----------------------|-------|
| `normalize_order_lines_pb` | SAP order lines | order lines clean | PB | snapshot+delta | data engineer |
| `shipment_status_cr` | TMS shipments + EDI events | shipment status | CR | append event merge | platform engineer |
| `supplier_commit_conform_pb` | supplier CSV + supplier master | supplier commits | PB | daily snapshot | data engineer |
| `inventory_projection_pb` | planning export + site master | inventory positions | PB | full refresh | planner-engineering pair |
| `risk_case_builder_cr` | all output datasets | risk cases | CR | full over pilot scope | platform engineer |

## Quality Checks

| Check | Dataset | Threshold | Current result | Action if failed |
|-------|---------|-----------|----------------|------------------|
| Null primary keys | all outputs | 0 | 0 | block publish |
| Duplicate business keys | supplier commits | <0.5% | 0.18% | quarantine duplicate rows |
| Freshness | shipment status | <30 min | 17 min median | page source owner if exceeded |
| Root-cause coverage | risk cases | >95% | 96.7% | hold review until causality restored |
| Confidence-band population | supplier commits | >97% | 94.1% | AMBER, retain freshness warning |

## Backing Readiness

| Ontology object/link/action dependency | Supporting dataset or transform | Ready? | Gap |
|---------------------------------------|----------------------------------|--------|-----|
| `OrderLine` object | `/acme/output/order_lines_enriched` | Yes | none |
| `Shipment` object | `/acme/output/shipment_status` | Yes | none |
| `RiskCase` object | `risk_case_builder_cr` | Yes | supplier freshness caveat surfaced |
| `CreateExpediteRequest` action | `/acme/output/expedite_requests` + approval rules | Yes | production approval group still pilot-only |
| `riskCaseToSupplierCommit` link | supplier commit conformance + join map | Yes | 3.3% unresolved vendor part IDs remain |

## Exception Path Readiness

| Workflow or exception path | Trigger | Primary handling path | Manual fallback | Residual risk if fallback remains | Ready for review? |
|----------------------------|---------|-----------------------|-----------------|-----------------------------------|-------------------|
| Late-arriving EDI events | shipment milestone delayed >30 min | event-merge transform reorders and recomputes latest state | planner refresh + logistics lead verification | one cycle of stale ETA can inflate severity | Yes |
| Missing supplier intraday update | supplier portal file not refreshed by 06:00 local | freshness rule downgrades confidence and highlights supplier risk case | buyer phones supplier and adds note to case | same-day supplier recovery may be invisible until manual note | Yes |
| Unmapped supplier part number | supplier file contains unknown vendor material code | conformance job routes line to unresolved crosswalk queue | planner excludes line from expedite recommendation | some shortage causality stays partial until master data fixed | No |

## Blockers And Decisions

| Blocker | Impact | Needs architecture change? | Needs DS decision? |
|---------|--------|----------------------------|--------------------|
| unresolved supplier part crosswalk for 11 vendors | supplier-driven risk cases can under-link to order lines | No | Yes |
| intraday supplier portal delta not available | supplier confidence remains AMBER in pilot | No | Yes |
| global plant expansion requested before pilot hardening | performance and support burden increase | Yes | Yes |

## Next Steps

1. [ ] Hand validated outputs to review and QA.
2. [ ] Flag any ontology-backing mismatch immediately.
3. [ ] Make every exception path and manual fallback explicit before calling the build review-ready.
4. [ ] Keep incremental strategy and quality thresholds aligned with the architecture doc.
