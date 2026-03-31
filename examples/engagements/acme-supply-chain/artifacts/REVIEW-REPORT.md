# Review Report: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Scope reviewed:** Pipeline, Ontology, Workshop, AIP, OSDK, Slate

## Executive Summary

- Overall quality verdict: Strong with targeted hardening needed before production pilot.
- Biggest strength: the artifact chain preserves causality from source freshness through planner recommendation and governed action.
- Most important risk: supplier-data freshness and finance approval integration could be glossed over if the team optimizes for demo smoothness.

## Findings

| Severity | Area | Finding | Why it matters | Recommended fix | Auto-fixed? |
|----------|------|---------|----------------|-----------------|-------------|
| High | Pipeline | supplier intraday feed is daily-only, but some screens still read as near-real-time | planners may over-trust stale supplier recovery signals | show confidence downgrade everywhere supplier data is causal | No |
| Medium | Workshop | finance code selection for expedite approval is not integrated | approval workflow could fail during pilot | complete dropdown integration or require manual code-entry checklist | No |
| Medium | AIP | draft assistant confidence wording is stronger than evidence when freshness is degraded | user may treat soft recommendation as fact | inject explicit freshness caveat in prompt and eval | No |
| Low | Ontology | unresolved vendor part crosswalk queue exists outside main planner page | support path is less discoverable | link unresolved mappings from supplier triage page | No |

## Scope Discipline Check

| Question | Answer |
|----------|--------|
| Did any build skill exceed its intended scope? | No. The team resisted direct transport re-booking and kept writeback governed. |
| Did any artifact rely on invention instead of evidence? | Mostly no. One demo note implied intraday supplier freshness that the source does not yet support. |
| Is the artifact chain internally consistent? | Yes, with the supplier-freshness caveat consistently needing stronger UI language. |

## Recommended Fix Loop

1. [ ] Make supplier freshness and confidence unavoidable in every planner and agent view.
2. [ ] Finish finance code integration or downgrade the approval page to explicit pilot-only workflow.
3. [ ] Re-run targeted QA after fixes land.
