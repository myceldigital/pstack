# Changelog

## 2026-03-31

- Rewrote the `examples/` library into detailed synthetic customer engagements so both sample projects now read like real DS delivery artifacts across discovery, architecture, build, governance, QA, deployment, training, and retrospective phases.
- Bootstrapped the repository for first GitHub publication by adding `PROJECT_TECHNICAL_OVERVIEW.md`, `workflow_state.md`, and a minimal `.gitignore` so the project is understandable and clean to publish.
- Published rationale: establish `pstack` as a shareable, root-documented GitHub repository with the required planning and project-overview metadata in place from the first commit.
- Configured GitHub repository metadata and protection baseline by setting the description, README homepage, discovery topics, and a standard `main` branch review policy to make the repo easier to discover and safer to change.
- Upgraded the repo into a real operator system by introducing `PROGRAM.md`, expanding `conductor.json` into the canonical skill/artifact/governance registry, generating `README.md` and `docs/skills.md` from it, completing all named artifact templates, and adding end-to-end examples plus eval rubrics and scorecards.
- Added a first-pass gated self-improvement loop with `memory/`, `/memory-curator`, `/skill-improver`, conductor support for improvement artifacts, and `scripts/evaluate_improvement.py` so the repo can learn from completed engagements without live uncontrolled mutation.
- Added `scripts/promote_improvement.py` to compare `HEAD` vs candidate proposal-target files against required benchmark-case rubrics before promotion, so improvement proposals have an actual before/after gate instead of only structural validation.
- Added structured `fixture.json` files per eval case plus `scripts/replay_improvement_case.py`, and rewired promotion scoring to use replayed fixture outputs instead of rubric-keyword coverage so proposal gates measure concrete expected file content.
- Tightened the `pipeline-healthcare` fixture so the exception-path proposal only gets credit after `templates/PIPELINE-BUILD-STATUS.md` adds an explicit exception-path readiness section and `evals/ARTIFACT-RUBRICS.md` adds matching manual-fallback language.
- Implemented the exception-path proposal by adding an `Exception Path Readiness` section to `templates/PIPELINE-BUILD-STATUS.md` and a matching explicit manual-fallback rule to `evals/ARTIFACT-RUBRICS.md`, so the replay gate now rewards the claimed improvement on the real target files.
