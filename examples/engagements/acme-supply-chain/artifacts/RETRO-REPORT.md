# Deployment Retrospective: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Duration:** 5-day bootcamp + 2-week hardening sprint  
**DS:** Maya Chen

## Scorecard

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Use cases delivered | 2 | 2 | GREEN |
| QA health score | >=85% | 91% | GREEN |
| Critical issues at deploy | 0 | 0 | GREEN |
| Training delivered | 3 operator groups | 3 operator groups | GREEN |

## What Worked

| What | Why | Replicable | Recommendation |
|------|-----|-----------|----------------|
| risk-case object separated decision workflow from raw data complexity | planners could reason in operational terms | Yes | keep explicit exception object in similar control-tower builds |
| freshness and confidence surfaced early | trust conversations happened before demo polish | Yes | make freshness unavoidable in all examples and templates |
| queue-first Workshop design | operators adopted it faster than dashboard-heavy layouts | Yes | default to decision queue over executive summary pages |

## What Didn't Work

| What | Why | Impact | Prevention |
|------|-----|--------|------------|
| supplier portal was daily-only | bootcamp assumed more timely updates than reality | created one major trust caveat | force earlier source-freshness contract review |
| finance approval integration started too late | team optimized for triage before governance detail | approval console remained partially hard-coded | pull approval-path design into day 2 |
| unresolved vendor part crosswalk got buried in support workflow | hidden data-quality queue | small but real blind spots in supplier causality | expose crosswalk debt as first-class artifact metric |

## Per-Use-Case Results

| Use Case | Status | Scoped Metric | Achieved | Gap |
|----------|--------|---------------|----------|-----|
| expedite at-risk orders | Delivered | decision latency < 45 min | 38 min in pilot simulation | needs live production validation |
| supplier delay triage | Delivered | buyer investigation time < 10 min | 11 min median | likely closes after note-history improvement |

## Recommendations

1. Expand to one additional region only after supplier freshness caveat is either fixed or accepted in operating policy.
2. Pull finance and approval-path design earlier in future DS-led control-tower bootcamps.
3. Feed the exception-path and freshness lessons back into `pstack` templates and examples.
