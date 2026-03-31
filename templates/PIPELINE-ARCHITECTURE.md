# Pipeline Architecture Template

**Usage:** Produced by `/pipeline-plan`. Consumed by `/data-connector`, `/pipeline-builder`.

---

# Pipeline Architecture: [Customer Name]

**Date:** [YYYY-MM-DD]
**Upstream:** BOOTCAMP-SCOPE.md, ONTOLOGY-VISION.md

## Source-to-Ontology Data Flow

| Source System | Connection | Raw Dataset | Clean Dataset | Transform | Output | Object Type |
|---------------|-----------|-------------|---------------|-----------|--------|-------------|
| | | | | | | |

## Connection Configuration

### [Source Name]

```
Type: [JDBC / REST API / S3 / SFTP / Agent / Streaming]
Details: [host, port, auth method]
Sync Mode: [Batch / Incremental / CDC / Streaming]
Schedule: [Frequency]
Agent Required: [Yes/No]
```

## Transform DAG

```
RAW → CLEAN → TRANSFORM → OUTPUT

Layer 0 (RAW): No transforms, exact copy
Layer 1 (CLEAN): Dedup, type cast, null standardize, column rename
Layer 2 (TRANSFORM): Joins, business logic, enrichment
Layer 3 (OUTPUT): Final schema for ontology backing
```

## Pipeline Tool Assignments

| Transform | Tool | Rationale |
|-----------|------|-----------|
| | [PB/CR] | |

## Incremental Strategy

| Pipeline | Strategy | Key Column | Notes |
|----------|----------|-----------|-------|
| | [Full/Append/Snapshot+Delta/CDC] | | |

## Data Quality Checks

| Output Dataset | PK Unique | Null Check | FK Valid | Row Count Range | Freshness |
|----------------|-----------|-----------|---------|-----------------|-----------|
| | | | | | |

## Schedule

| Pipeline | Trigger | Schedule | Dependencies |
|----------|---------|----------|-------------|
| | [Time/Upstream] | | |

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| | | |
