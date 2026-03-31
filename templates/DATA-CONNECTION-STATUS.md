# Data Connection Status Template

**Usage:** Produced by `/data-connector`. Consumed by `/pipeline-builder`.

---

# Data Connection Status: [Customer Name]

**Date:** [YYYY-MM-DD]
**Upstream:** `PIPELINE-ARCHITECTURE.md`, `BOOTCAMP-SCOPE.md`
**Environment:** [Dev / Staging / Production]

## Summary

| Source | Type | Owner | Readiness | Status | Last sync | Notes |
|--------|------|-------|-----------|--------|-----------|-------|
| [ERP] | [JDBC/API/S3] | [Name] | [X/10] | [GREEN/AMBER/RED] | [timestamp] | [note] |

## Connection Details

### [Source Name]
- Connection mode: [Direct / Agent / VPN]
- Authentication pattern: [OAuth / User-pass / Service account / Kerberos]
- Sync strategy: [Snapshot / Incremental / CDC / Stream]
- Schedule: [Cron or cadence]
- Raw dataset path: `[path]`
- Clean dataset path: `[path]`
- Preconditions verified:
  - [ ] network reachable
  - [ ] credentials tested
  - [ ] source schema sampled
  - [ ] permissions confirmed
  - [ ] timezone handling documented

## First-Stage Cleaning

| Raw dataset | Clean dataset | Tool | Key cleaning actions | Status |
|-------------|---------------|------|----------------------|--------|
| [path] | [path] | [Pipeline Builder / Code Repo] | [dedupe, casting, null normalization] | [GREEN/AMBER/RED] |

## Health Monitoring

| Check | Threshold | Alert owner | Current state |
|-------|-----------|-------------|---------------|
| Connectivity | [e.g. every 5 min] | [role] | [OK/WARN/FAIL] |
| Freshness | [e.g. < 2x expected delay] | [role] | [OK/WARN/FAIL] |
| Schema stability | [no breaking changes] | [role] | [OK/WARN/FAIL] |

## Blockers And Decisions

| Issue | Severity | Needs DS decision? | Resolution path |
|-------|----------|--------------------|-----------------|
| [Issue] | [High/Med/Low] | [Yes/No] | [Action] |

## Next Steps

1. [ ] Confirm all critical sources are green.
2. [ ] Hand off clean datasets and blockers to `/pipeline-builder`.
3. [ ] Escalate any production-credential or network issue to the DS.
