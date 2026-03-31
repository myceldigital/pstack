# Pipeline Build Status: Northstar Healthcare Patient Flow

## Output Datasets

| Dataset | Purpose | Status |
|---------|---------|--------|
| operational_core | main operator view | GREEN |
| risk_enriched | prioritization | GREEN |
| exception_queue | escalation | AMBER |

## Build Notes

- Main transforms produce ontology-ready keys.
- Exception path still needs one late-joining source.
