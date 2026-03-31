# Pipeline Architecture: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Upstream:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-VISION.md`

## Source-to-Ontology Data Flow

| Source System | Connection | Raw Dataset | Clean Dataset | Transform | Output | Object Type |
|---------------|-----------|-------------|---------------|-----------|--------|-------------|
| SAP ECC | JDBC via network allowlist | `/acme/raw/sap/order_lines` | `/acme/clean/sap/order_lines_clean` | `normalize_order_lines_pb` | `/acme/output/order_lines_enriched` | `OrderLine` |
| Blue Yonder TMS | REST API | `/acme/raw/tms/shipments` | `/acme/clean/tms/shipments_clean` | `shipment_status_cr` | `/acme/output/shipment_status` | `Shipment` |
| SPS Commerce EDI 214 | S3 ingest | `/acme/raw/edi214/events` | `/acme/clean/edi214/events_clean` | `shipment_event_merge_cr` | `/acme/output/shipment_status` | `Shipment` |
| Supplier Portal | SFTP CSV | `/acme/raw/supplier/commits` | `/acme/clean/supplier/commits_clean` | `supplier_commit_conform_pb` | `/acme/output/supplier_commits` | `SupplierCommit` |
| Kinaxis export | S3 CSV | `/acme/raw/planning/inventory` | `/acme/clean/planning/inventory_clean` | `inventory_projection_pb` | `/acme/output/inventory_positions` | `InventoryPosition` |
| Derived | n/a | n/a | n/a | `risk_case_builder_cr` | `/acme/output/risk_cases` | `RiskCase` |

## Connection Configuration

### SAP ECC

```
Type: JDBC
Details: ECC6 on Oracle, read-only service account through customer VPN
Sync Mode: Incremental by changed-at timestamp
Schedule: every 15 minutes
Agent Required: Yes
```

### Blue Yonder TMS

```
Type: REST API
Details: OAuth2 client credential, shipment and milestone endpoints
Sync Mode: Incremental by lastUpdated timestamp
Schedule: every 15 minutes
Agent Required: No
```

### Supplier Portal

```
Type: SFTP CSV
Details: daily drop from managed supplier collaboration portal
Sync Mode: Snapshot with diffing on supplier commit line
Schedule: 05:30 local plant time + manual rerun option
Agent Required: No
```

## Transform DAG

```
RAW -> CLEAN -> TRANSFORM -> OUTPUT

Layer 0 (RAW): preserve SAP, TMS, EDI, supplier, and planning extracts exactly as received
Layer 1 (CLEAN): dedupe by business key, timezone normalization, part-number crosswalk, null standardization
Layer 2 (TRANSFORM): shipment event merge, supplier commit confidence, inventory coverage, promise-date confidence, risk scoring
Layer 3 (OUTPUT): ontology-ready order lines, shipments, supplier commits, inventory positions, risk cases, expedite requests
```

## Pipeline Tool Assignments

| Transform | Tool | Rationale |
|-----------|------|-----------|
| `normalize_order_lines_pb` | PB | straightforward relational cleanup with visible lineage |
| `shipment_status_cr` | CR | requires event-window logic and carrier ETA reconciliation |
| `shipment_event_merge_cr` | CR | custom ordering and late-event handling |
| `supplier_commit_conform_pb` | PB | tabular normalization and reference mapping |
| `inventory_projection_pb` | PB | predictable derivation and threshold math |
| `risk_case_builder_cr` | CR | multi-source join plus severity logic best maintained in code |

## Incremental Strategy

| Pipeline | Strategy | Key Column | Notes |
|----------|----------|-----------|-------|
| order lines | Snapshot+Delta | `last_changed_at` | retain 30-day history for regression checks |
| shipments | Append | `event_timestamp` | rebuild latest state from append-only events |
| supplier commits | Snapshot+Delta | `portal_export_date` | latest file wins with line-level diff |
| inventory positions | Full | export timestamp | small enough to recompute every run |
| risk cases | Full over pilot scope | n/a | derived for determinism during pilot |

## Data Quality Checks

| Output Dataset | PK Unique | Null Check | FK Valid | Row Count Range | Freshness |
|----------------|-----------|-----------|---------|-----------------|-----------|
| `/acme/output/order_lines_enriched` | 100% | customer + promise date > 99.9% | order-to-material 99.8% | 150k-220k | < 30 min |
| `/acme/output/shipment_status` | 100% | ETA optional, carrier required 99% | lane ref 98% | 18k-25k | < 30 min |
| `/acme/output/supplier_commits` | 100% | commit date 97% | supplier id 99.5% | 80k-110k | < 24 h |
| `/acme/output/risk_cases` | 100% | severity 100% | order line link 100% | 1k-5k | < 30 min |

## Schedule

| Pipeline | Trigger | Schedule | Dependencies |
|----------|---------|----------|-------------|
| SAP ingest | Time | every 15 min | VPN agent healthy |
| TMS ingest | Time | every 15 min | OAuth token refresh |
| EDI ingest | Upstream file arrival | near-hourly | S3 landing event |
| Supplier commit ingest | Time | daily 05:30 + on-demand | vendor file availability |
| Risk case build | Upstream | after order, shipment, inventory, supplier outputs | all core datasets green |

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| supplier commit file misses urgent same-day changes | planners may over-trust stale commit status | freshness and confidence displayed; manual override notes preserved |
| EDI events arrive out of order | false delay severity | event merge logic uses sequence window and stale-event suppression |
| part-number crosswalk incomplete | risk cases fail to connect shortage to order lines | maintain explicit unresolved-map queue for procurement ops |
| full recompute of risk cases grows too slow after pilot expansion | latency breaches planner workflow | phase 2 plan moves risk build to partitioned regional execution |
