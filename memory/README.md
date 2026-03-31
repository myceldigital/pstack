# Memory

`pstack` memory is artifact-first and gated. The repo does not learn by silently mutating core skills during a customer engagement. It learns by extracting reusable patterns from finished work, drafting bounded proposals, and only promoting them after human review plus eval coverage.

## Layout

- `episodes/`: structured per-engagement memory
- `semantic/`: cross-engagement patterns and anti-patterns
- `operator/`: operator- and DS-specific memory structures
- `proposals/`: candidate repo improvements waiting for promotion
- `templates/`: canonical templates for memory and proposal artifacts
- `schemas/`: machine-readable validation targets for memory artifacts

## Promotion Rule

1. Curate a structured episode.
2. Draft an improvement proposal.
3. Evaluate proposal readiness with `python3 scripts/evaluate_improvement.py`.
4. Replay the proposal against structured eval fixtures with `python3 scripts/replay_improvement_case.py --proposal ...`.
5. Compare `HEAD` vs candidate target files with `python3 scripts/promote_improvement.py --proposal ...`.
6. Require human review before any canonical repo edit lands.
