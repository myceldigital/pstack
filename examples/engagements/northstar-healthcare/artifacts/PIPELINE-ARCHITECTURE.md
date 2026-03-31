# Pipeline Architecture: Northstar Healthcare Patient Flow

## Source To Ontology Flow

- Raw ingestion from customer systems
- Clean layer normalization
- Curated operational model
- Output datasets backing ontology objects and links

## Scheduling

- Critical feeds: hourly
- Supporting feeds: daily

## Quality Gates

- freshness
- key integrity
- duplicate suppression
