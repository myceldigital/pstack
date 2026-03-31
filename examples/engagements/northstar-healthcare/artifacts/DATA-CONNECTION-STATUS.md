# Data Connection Status: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Upstream:** `PIPELINE-ARCHITECTURE.md`, `BOOTCAMP-SCOPE.md`  
**Environment:** Staging

## Summary

| Source | Type | Owner | Readiness | Status | Last sync | Notes |
|--------|------|-------|-----------|--------|-----------|-------|
| Epic Clarity | JDBC | Nisha Gupta | 9/10 | GREEN | 2026-03-31 09:30 CT | PHI-scoped replica access approved |
| TeleTracking | API | Luis Ortega | 8/10 | GREEN | 2026-03-31 09:46 CT | 5-minute polling stable |
| Transfer Center | API + CSV | Hannah Lee | 7/10 | GREEN | 2026-03-31 09:40 CT | status mapping validated |
| Kronos staffing | CSV | Monique Fields | 6/10 | AMBER | 2026-03-31 09:00 CT | hourly refresh is slower than surge workflow |
| EVS mobile export | CSV | Robert Hale | 6/10 | AMBER | 2026-03-31 09:15 CT | free-text notes require redaction |

## Connection Details

### Epic Clarity
- Connection mode: network allowlist + read replica
- Authentication pattern: service account from hospital identity vault
- Sync strategy: snapshot+delta by ADT and discharge-order timestamps
- Schedule: every 15 minutes
- Raw dataset path: `/northstar/raw/epic/adt`
- Clean dataset path: `/northstar/clean/epic/adt_clean`
- Preconditions verified:
  - [x] network reachable
  - [x] credentials tested
  - [x] source schema sampled
  - [x] permissions confirmed
  - [x] timezone handling documented

### EVS mobile export
- Connection mode: managed S3 landing from vendor batch export
- Authentication pattern: vendor drop to customer-controlled bucket
- Sync strategy: snapshot file with row-level dedupe
- Schedule: every 15 minutes
- Raw dataset path: `/northstar/raw/evs/tasks`
- Clean dataset path: `/northstar/clean/evs/tasks_clean`
- Preconditions verified:
  - [x] network reachable
  - [x] credentials tested
  - [x] source schema sampled
  - [x] permissions confirmed
  - [ ] timezone handling documented

## First-Stage Cleaning

| Raw dataset | Clean dataset | Tool | Key cleaning actions | Status |
|-------------|---------------|------|----------------------|--------|
| `/northstar/raw/epic/adt` | `/northstar/clean/epic/adt_clean` | Code Repo | PHI field minimization, site mapping, encounter status normalization | GREEN |
| `/northstar/raw/bedboard/beds` | `/northstar/clean/bedboard/beds_clean` | Pipeline Builder | bed-status harmonization, unit mapping, isolation code normalization | GREEN |
| `/northstar/raw/evs/tasks` | `/northstar/clean/evs/tasks_clean` | Code Repo | free-text redaction, task status mapping, room linkage | AMBER |

## Health Monitoring

| Check | Threshold | Alert owner | Current state |
|-------|-----------|-------------|---------------|
| Connectivity | every 5 min | platform operations | OK |
| Freshness | < 2x expected delay | command center manager | WARN on staffing |
| Schema stability | no breaking changes | data engineering lead | OK |

## Blockers And Decisions

| Issue | Severity | Needs DS decision? | Resolution path |
|-------|----------|--------------------|-----------------|
| staffing data only hourly | High | Yes | accept hourly source for pilot and downgrade recommendation confidence |
| EVS notes include unsafe free text | High | No | redact notes before clean layer publish |
| one hospital uses custom hold-bed code set | Medium | No | site-specific mapping in bed-readiness pipeline |

## Next Steps

1. [ ] Confirm all critical pilot-hospital feeds are green before full rehearsal.
2. [ ] Hand off clean datasets and blocker notes to `/pipeline-builder`.
3. [ ] Escalate hourly staffing limitation as an explicit pilot operating assumption.
