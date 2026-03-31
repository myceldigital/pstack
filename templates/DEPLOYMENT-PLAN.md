# Deployment Plan Template

**Usage:** Produced by `/apollo-deployer`.

---

# Deployment Plan: [Customer Name]

**Date:** [YYYY-MM-DD]
**Environment:** [Cloud / Hybrid / Air-gapped]
**Strategy:** [Blue-green / Canary / Direct]

## Pre-Deployment Checklist

- [ ] QA health score: [N]% (≥85% required)
- [ ] Security audit: [SECURE / ACCEPTABLE_RISK]
- [ ] Stakeholder approval: [Name]
- [ ] Rollback plan documented

## Deployment Steps

1. [Step with expected outcome]
2. [Step with expected outcome]
3. [Step with expected outcome]

## Release Channel Configuration

| Channel | Environment | Bake Time | Rollback Trigger |
|---------|-------------|-----------|-----------------|
| CANARY | Dev | 24h | Error rate >1% |
| STABLE | Staging | 48h | Error rate >0.5% |
| RELEASE | Production | — | Manual only |

## Post-Deploy Verification

- [ ] Data connections syncing
- [ ] Pipeline builds succeeding
- [ ] Ontology objects populating
- [ ] Workshop apps loading
- [ ] AIP agents responding
- [ ] Authentication working
- [ ] Performance acceptable

## Rollback Procedure

1. [Step]
2. [Step]
3. [Step]

## Monitoring (72-hour window)

| Metric | Threshold | Alert Channel |
|--------|-----------|---------------|
| Pipeline failure rate | >0% | [Channel] |
| App error rate | >1% | [Channel] |
| Data freshness | >2x expected | [Channel] |
