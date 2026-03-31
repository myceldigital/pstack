# Improvement Proposal: Add earlier security checkpoint in the program flow

**Status:** Candidate
**Origin Episode:** `memory/episodes/northstar-healthcare-2026-03-31.json`
**Scope:** PROGRAM + docs

## Problem

Security issues are easier to correct when action scope and sensitive data boundaries are challenged before app polish accelerates.

## Target Files

- `PROGRAM.md`
- `docs/skills.md`

## Proposed Change

Add an earlier security-readiness checkpoint in the build-to-review handoff guidance so teams pressure-test risky actions and context scope before they feel “done.”

## Expected Benefit

- Fewer late security surprises.
- Cleaner handoff between build specialists and `/foundry-security`.

## Required Evals

- `pipeline-healthcare`
- `improvement-loop`

## Promotion Gate

- [ ] `python3 scripts/evaluate_improvement.py --proposal memory/proposals/2026-03-31-security-gate-earlier.md`
- [ ] Human review completed
- [ ] Canonical-file patch reviewed separately from the proposal
