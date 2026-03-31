# Acme Supply Chain Control Tower

**Industry:** Discrete manufacturing / industrial supply chain  
**Customer footprint:** 14 plants, 3 distribution hubs, 126 tier-1 suppliers, North America + Western Europe  
**Program type:** Production-oriented pilot moving toward regional rollout

## Customer Situation

Acme Components was missing customer SLAs for high-margin industrial assemblies because expedite decisions were made late, supplier commit dates were unreliable, and planners worked out of ERP extracts plus manually maintained spreadsheets. The COO wanted one operational surface that could answer three questions before noon every day:

1. Which shipments are most likely to miss customer promise dates?
2. Which supplier or plant bottlenecks are actually driving that risk?
3. Which expedite, reallocation, or escalation action should be taken right now?

## Delivery Goal

Deliver a control-tower workflow that lets regional planners triage at-risk orders, explain the root cause behind each risk signal, and trigger governed expedite requests with an auditable approval path.

## Headline Outcome

The bootcamp-target scope focused on reducing same-day expedite decision latency from roughly 4.5 hours to less than 45 minutes for top-priority orders while also improving planner trust in supplier and inventory status.

## Artifact Chain In This Example

- `BOOTCAMP-SCOPE.md`: sponsor goals, stakeholder map, systems, risks, and bootcamp schedule
- `ONTOLOGY-VISION.md` and `ONTOLOGY-ARCHITECTURE.md`: the operational digital twin for shipments, inventory, suppliers, and risk cases
- `PIPELINE-ARCHITECTURE.md` through build-status artifacts: source onboarding and application build detail
- `REVIEW-REPORT.md`, `SECURITY-AUDIT.md`, `QA-REPORT.md`: quality and go-live gates
- `DEPLOYMENT-PLAN.md`, `TRAINING-MATERIALS.md`, `RETRO-REPORT.md`: rollout, adoption, and learning loop

## What Makes This Example Useful

This engagement shows a realistic manufacturing control-tower program with mixed data quality, late-arriving EDI events, governed writeback, and a practical DS trade-off between shipping a high-value pilot fast and over-scoping into a full global planning platform.
