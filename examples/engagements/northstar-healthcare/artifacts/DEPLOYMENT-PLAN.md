# Deployment Plan: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Environment:** Cloud  
**Strategy:** Canary

## Pre-Deployment Checklist

- [x] QA health score: 90% (>=85% required)
- [x] Security audit: `ACCEPTABLE_RISK`
- [x] Stakeholder approval: Rebecca Long, Denise Harper, Luis Ortega
- [x] Rollback plan documented

## Deployment Steps

1. Deploy ontology, pipelines, and Workshop surfaces to staging for the two pilot hospitals and validate one full daytime shift.
2. Enable capacity queue and discharge barrier board for command-center nurses and care-management leads only.
3. Enable transfer-center OSDK console after role mapping is validated in production identity groups.
4. Enable aggregate-only executive Slate board after operational users have completed first-week training.

## Release Channel Configuration

| Channel | Environment | Bake Time | Rollback Trigger |
|---------|-------------|-----------|-----------------|
| CANARY | pilot staging | 24h | stale staffing or bed feed beyond threshold |
| STABLE | two-hospital pilot | 72h | command-center trust incident or duplicate transfer ack |
| RELEASE | broader system rollout | manual | steering committee approval only |

## Post-Deploy Verification

- [ ] Data connections syncing on expected cadence.
- [ ] Pipeline builds succeeding for three consecutive cycles.
- [ ] Ontology objects populating with expected counts by site.
- [ ] Workshop command-center pages loading under real roles.
- [ ] AIP agents responding with operational-only, de-identified guidance.
- [ ] Authentication working for command center, transfer center, and leaders.
- [ ] Performance acceptable during 16:00 discharge surge window.

## Rollback Procedure

1. Remove pilot user groups from patient-flow operational surfaces.
2. Revert command-center users to existing Epic + bed-board operating process.
3. Freeze new escalation acknowledgments in OSDK console while defects are triaged.

## Monitoring (72-hour window)

| Metric | Threshold | Alert Channel |
|--------|-----------|---------------|
| Pipeline failure rate | >0% on core outputs | `#northstar-flow-war-room` |
| App error rate | >1% | `#northstar-flow-war-room` |
| Data freshness | >2x expected | DS bridge + nurse leader text tree |
| Duplicate transfer ack | >0 | transfer-center on-call |
| PHI leakage incident | >0 | security bridge immediately |
