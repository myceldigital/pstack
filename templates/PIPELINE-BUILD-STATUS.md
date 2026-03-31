# Pipeline Build Status Template

**Usage:** Produced by `/pipeline-builder`. Consumed by `/foundry-reviewer`, `/foundry-qa`.

---

# Pipeline Build Status: [Customer Name]

**Date:** [YYYY-MM-DD]
**Upstream:** `PIPELINE-ARCHITECTURE.md`, `DATA-CONNECTION-STATUS.md`, `ONTOLOGY-ARCHITECTURE.md`

## Build Summary

| Dataset | Layer | Purpose | Build status | Data quality | Ontology ready? |
|---------|-------|---------|--------------|--------------|-----------------|
| [orders_enriched] | OUTPUT | [decision support] | [GREEN/AMBER/RED] | [score] | [Yes/No] |

## Transform Inventory

| Transform | Input(s) | Output | Tool | Incremental strategy | Owner |
|-----------|----------|--------|------|----------------------|-------|
| [name] | [datasets] | [dataset] | [PB/CR] | [full/incremental] | [role] |

## Quality Checks

| Check | Dataset | Threshold | Current result | Action if failed |
|-------|---------|-----------|----------------|------------------|
| Null primary keys | [dataset] | [0] | [result] | [resolution] |
| Duplicate business keys | [dataset] | [<0.5%] | [result] | [resolution] |
| Freshness | [dataset] | [window] | [result] | [resolution] |

## Backing Readiness

| Ontology object/link/action dependency | Supporting dataset or transform | Ready? | Gap |
|---------------------------------------|----------------------------------|--------|-----|
| [Shipment object] | [shipments_curated] | [Yes/No] | [detail] |

## Blockers And Decisions

| Blocker | Impact | Needs architecture change? | Needs DS decision? |
|---------|--------|----------------------------|--------------------|
| [Issue] | [What breaks] | [Yes/No] | [Yes/No] |

## Next Steps

1. [ ] Hand validated outputs to review and QA.
2. [ ] Flag any ontology-backing mismatch immediately.
3. [ ] Keep incremental strategy and quality thresholds aligned with the architecture doc.
