# Security Audit: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Compliance:** HIPAA

## Summary

| Domain | Critical | High | Medium | Low |
|--------|----------|------|--------|-----|
| Ontology permissions | 0 | 0 | 1 | 0 |
| AIP agents | 0 | 0 | 1 | 0 |
| OSDK applications | 0 | 0 | 1 | 1 |
| Data governance | 0 | 1 | 1 | 0 |
| Apollo deployment | 0 | 0 | 0 | 1 |

## Permission Matrix

| Object Type | Read | Edit | Actions | Markings |
|-------------|------|------|---------|----------|
| `PatientFlowCase` | command center, transfer center, unit leadership | owner assignment only | assign flow owner | site + role-group marking |
| `Bed` | command center, unit leadership | none | mark bed clean delay | site + unit marking |
| `DischargeBarrier` | command center, care management, EVS leads | escalation state only | escalate barrier | site + service-line marking |
| `TransferRequest` | transfer center, throughput supervisors | acknowledgment only | acknowledge transfer escalation | site + transfer-center marking |

## Findings

- **High / Data governance:** raw EVS export includes free-text note fragments that can contain room identifiers and incidental PHI. Exploitation scenario: broad raw-dataset access would expose data outside the command-center purpose. Remediation: redact free text before any non-admin surface and restrict raw access to engineering only.
- **Medium / AIP:** capacity copilot must not include patient names or free-text notes even when users ask. Exploitation scenario: agent broadens PHI exposure during command huddles. Remediation: maintain field-level allowlist and refusal evals.
- **Medium / OSDK:** transfer console role mapping is correct in staging but production group synchronization is not yet proven. Remediation: complete pre-cutover identity sync validation.
- **Low / OSDK:** acknowledgment audit feed lacks support-rota metadata. Remediation: attach on-call ownership before production cutover.
- **Low / Deployment:** executive Slate board must remain aggregate-only. Remediation: keep patient-level drillthrough disabled by policy and permission.

## Verdict

ACCEPTABLE_RISK
