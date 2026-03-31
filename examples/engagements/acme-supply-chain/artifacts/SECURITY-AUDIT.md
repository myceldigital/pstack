# Security Audit: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Compliance:** SOC2 + customer procurement controls

## Summary

| Domain | Critical | High | Medium | Low |
|--------|----------|------|--------|-----|
| Ontology permissions | 0 | 0 | 1 | 1 |
| AIP agents | 0 | 0 | 1 | 0 |
| OSDK applications | 0 | 1 | 1 | 0 |
| Data governance | 0 | 0 | 1 | 1 |
| Apollo deployment | 0 | 0 | 0 | 1 |

## Permission Matrix

| Object Type | Read | Edit | Actions | Markings |
|-------------|------|------|---------|----------|
| `OrderLine` | planners, buyers, executives | none | none | business-unit restricted |
| `Shipment` | planners, logistics, executives | none | none | lane + region marking |
| `RiskCase` | planners, buyers, logistics | planners can assign owner | create governed requests only | region + customer-priority marking |
| `ExpediteRequest` | planners, approvers, finance | approvers only on approval fields | create/update governed action | approval-tier marking |

## Findings

- **High / OSDK:** approval console currently requests write scope broader than the minimum draft-only behavior needed in staging. Exploitation scenario: an over-scoped token could create or update approval records outside the pilot region. Remediation: split draft-write from approval-submit permissions and region-scope the API layer.
- **Medium / AIP:** draft assistant can reference supplier notes that sometimes include free-text email fragments. Exploitation scenario: accidental leakage of contact details in broader agent context. Remediation: redact contact text before inclusion and scope context to approved fields only.
- **Medium / Ontology permissions:** procurement users can currently view all plants in pilot staging. Risk: unnecessary cross-region visibility. Remediation: enforce business-unit and region filters before production pilot.
- **Low / Data governance:** one EDI raw dataset retains partner file names that reveal carrier codes. Remediation: hash file names in raw metadata before wider access.
- **Low / Deployment:** rollback owners are named but on-call rota is not yet attached to the runbook. Remediation: finalize support schedule before cutover.

## Verdict

ACCEPTABLE_RISK
