# Improvement Proposal: Tighten exception-path coverage in build artifacts

**Status:** Candidate
**Origin Episode:** `memory/episodes/acme-supply-chain-2026-03-31.json`
**Scope:** templates + evals

## Problem

Build artifacts currently make it too easy to hide a half-manual exception path behind an overall healthy status.

## Target Files

- `templates/PIPELINE-BUILD-STATUS.md`
- `evals/ARTIFACT-RUBRICS.md`

## Proposed Change

Add a dedicated exception-path readiness section to the pipeline build template and require the rubric to fail when manual fallback remains implicit.

## Expected Benefit

- Reviewers catch partial manual workflows earlier.
- QA gets explicit visibility into negative-path readiness.

## Required Evals

- `pipeline-healthcare`
- `improvement-loop`

## Promotion Gate

- [ ] `python3 scripts/evaluate_improvement.py --proposal memory/proposals/2026-03-31-exception-path-coverage.md`
- [ ] Human review completed
- [ ] Canonical-file patch reviewed separately from the proposal
