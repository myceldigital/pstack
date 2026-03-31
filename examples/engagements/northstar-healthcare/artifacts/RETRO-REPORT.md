# Deployment Retrospective: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Duration:** 5-day bootcamp + 2-week hardening sprint  
**DS:** Aaron Mensah

## Scorecard

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Use cases delivered | 2 | 2 | GREEN |
| QA health score | >=85% | 90% | GREEN |
| Critical issues at deploy | 0 | 0 | GREEN |
| Training delivered | 4 audience groups | 4 audience groups | GREEN |

## What Worked

| What | Why | Replicable | Recommendation |
|------|-----|-----------|----------------|
| operations-only ontology framing | kept the program out of unsafe clinical territory | Yes | use explicit non-clinical language in all healthcare examples |
| de-identified shared screens | improved stakeholder comfort with broader command-center visibility | Yes | default to minimal PHI surfaces |
| barrier object tied to downstream bed demand | made discharge work feel operationally urgent | Yes | keep blocker-to-capacity linkage explicit |

## What Didn't Work

| What | Why | Impact | Prevention |
|------|-----|--------|------------|
| hourly staffing source was too coarse during peak shift change | queue confidence had to be downgraded more often than expected | some nurses still double-checked externally | challenge staffing-feed cadence on day 1 |
| transfer acknowledgment idempotency was left late | duplicate action edge case stayed open into QA | support concern for transfer center | treat high-frequency operator actions as early hardening targets |
| printable huddle support lagged | one shift still preferred paper workflow | slower adoption on that shift | include low-friction print/export needs earlier |

## Per-Use-Case Results

| Use Case | Status | Scoped Metric | Achieved | Gap |
|----------|--------|---------------|----------|-----|
| prioritize bed assignment | Delivered | median assignment latency < 20 min | 18 min in simulation | needs live peak-shift validation |
| accelerate discharge readiness | Delivered | avoidable delay minutes down 15% | 13% in rehearsal data | likely closes with stronger barrier ownership |

## Recommendations

1. Expand to more hospitals only after staffing freshness limitations are operationally accepted or materially improved.
2. Harden transfer-console idempotency and command-center print/export support before broader release.
3. Feed the healthcare governance and de-identified UI patterns back into `pstack` examples and templates.
