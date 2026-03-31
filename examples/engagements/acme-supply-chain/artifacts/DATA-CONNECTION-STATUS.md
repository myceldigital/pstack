# Data Connection Status: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Upstream:** `PIPELINE-ARCHITECTURE.md`, `BOOTCAMP-SCOPE.md`  
**Environment:** Staging

## Summary

| Source | Type | Owner | Readiness | Status | Last sync | Notes |
|--------|------|-------|-----------|--------|-----------|-------|
| SAP ECC | JDBC | Sarah Kim | 9/10 | GREEN | 2026-03-31 09:45 CT | read-only service account verified |
| Blue Yonder TMS | API | Priya Weston | 8/10 | GREEN | 2026-03-31 09:43 CT | token rotation tested |
| SPS Commerce EDI 214 | S3 | Ben Alvarez | 7/10 | AMBER | 2026-03-31 09:05 CT | some partner events delayed by 30-45 min |
| Supplier Portal | SFTP CSV | Omar Schmitt | 6/10 | AMBER | 2026-03-31 05:32 CT | daily-only export still manual to trigger |
| Kinaxis export | S3 CSV | Laura Jensen | 7/10 | GREEN | 2026-03-31 08:15 CT | pilot sites only |

## Connection Details

### SAP ECC
- Connection mode: VPN agent
- Authentication pattern: service account with rotated password in customer vault
- Sync strategy: incremental snapshot by `AEDAT`/`UPDKZ`
- Schedule: every 15 minutes
- Raw dataset path: `/acme/raw/sap/order_lines`
- Clean dataset path: `/acme/clean/sap/order_lines_clean`
- Preconditions verified:
  - [x] network reachable
  - [x] credentials tested
  - [x] source schema sampled
  - [x] permissions confirmed
  - [x] timezone handling documented

### Supplier Portal
- Connection mode: direct SFTP
- Authentication pattern: service account + IP allowlist
- Sync strategy: daily file snapshot with file-hash detection
- Schedule: 05:30 local plant time, rerun by procurement ops if needed
- Raw dataset path: `/acme/raw/supplier/commits`
- Clean dataset path: `/acme/clean/supplier/commits_clean`
- Preconditions verified:
  - [x] network reachable
  - [x] credentials tested
  - [x] source schema sampled
  - [x] permissions confirmed
  - [ ] timezone handling documented

## First-Stage Cleaning

| Raw dataset | Clean dataset | Tool | Key cleaning actions | Status |
|-------------|---------------|------|----------------------|--------|
| `/acme/raw/sap/order_lines` | `/acme/clean/sap/order_lines_clean` | Pipeline Builder | status normalization, customer-priority enrichment, key dedupe | GREEN |
| `/acme/raw/tms/shipments` | `/acme/clean/tms/shipments_clean` | Code Repo | milestone ordering, timezone normalization, carrier code map | GREEN |
| `/acme/raw/supplier/commits` | `/acme/clean/supplier/commits_clean` | Pipeline Builder | part crosswalk, date coercion, supplier tier join | AMBER |

## Health Monitoring

| Check | Threshold | Alert owner | Current state |
|-------|-----------|-------------|---------------|
| Connectivity | every 5 min | IT integration lead | OK |
| Freshness | < 2x expected delay | DS + source owner | WARN on EDI and supplier portal |
| Schema stability | no breaking changes | data engineering lead | OK |

## Blockers And Decisions

| Issue | Severity | Needs DS decision? | Resolution path |
|-------|----------|--------------------|-----------------|
| supplier portal lacks intraday delta feed | High | Yes | accept daily feed for pilot and show freshness caveat in planner UI |
| one EU carrier sends malformed milestone code | Medium | No | exclude from pilot region and patch mapping table |
| Kinaxis export omits alternate-component recommendations for one plant | Medium | Yes | keep substitution recommendation out of day-5 demo for that plant |

## Next Steps

1. [ ] Confirm all critical pilot-region sources are green before demo rehearsal.
2. [ ] Hand off clean datasets and blocker notes to `/pipeline-builder`.
3. [ ] Escalate supplier-portal intraday limitations to the DS as an explicit phase-2 gap.
