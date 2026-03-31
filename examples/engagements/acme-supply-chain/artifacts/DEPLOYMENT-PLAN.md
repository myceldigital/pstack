# Deployment Plan: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Environment:** Hybrid  
**Strategy:** Canary

## Pre-Deployment Checklist

- [x] QA health score: 91% (>=85% required)
- [x] Security audit: `ACCEPTABLE_RISK`
- [x] Stakeholder approval: Elena Rossi, Marcus Bell, Dana Patel
- [x] Rollback plan documented

## Deployment Steps

1. Publish pilot datasets and ontology to North America staging with planner-only access; confirm 24-hour backfill succeeds.
2. Enable Workshop risk queue and order drilldown for the Midwest planning pod and logistics approvers only.
3. Turn on governed expedite-request workflow with finance observers and monitor first five approved requests manually.
4. Enable executive Slate wallboard after planner workflow is stable to avoid leadership using pre-pilot numbers.

## Release Channel Configuration

| Channel | Environment | Bake Time | Rollback Trigger |
|---------|-------------|-----------|-----------------|
| CANARY | NA staging | 24h | failed pipeline or stale data > 60 min |
| STABLE | NA pilot production | 72h | planner complaint volume > threshold or approval defects |
| RELEASE | broader NA region | manual | steering committee go/no-go only |

## Post-Deploy Verification

- [ ] Data connections syncing within agreed freshness windows.
- [ ] Pipeline builds succeeding on three consecutive cycles.
- [ ] Ontology objects populating with expected regional counts.
- [ ] Workshop apps loading under real planner identities.
- [ ] AIP agents responding with cited evidence and refusal behavior intact.
- [ ] Authentication working for planners, buyers, and approvers.
- [ ] Performance acceptable under 08:00 planning peak.

## Rollback Procedure

1. Disable pilot user groups from Workshop, OSDK, and Slate surfaces.
2. Revert ontology/action exposure to read-only analytics baseline.
3. Route planners back to existing spreadsheet plus TMS fallback process while defects are triaged.

## Monitoring (72-hour window)

| Metric | Threshold | Alert Channel |
|--------|-----------|---------------|
| Pipeline failure rate | >0% on core outputs | `#acme-pilot-ops` |
| App error rate | >1% | `#acme-pilot-ops` |
| Data freshness | >2x expected | pager + DS text bridge |
| Expedite approval failure | >0 on submitted requests | logistics lead bridge |
| User trust incident | >=3 planner complaints/day | DS daily triage |
