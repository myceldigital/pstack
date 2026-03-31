## Workflow State

### Current Cycle
- Role: `Planner`
- Objective: Turn `pstack` into a serious operator-grade deployment system by adding a real `PROGRAM.md`, making `conductor.json` the source of truth, completing the artifact system, and adding examples/evals.
- Scope: Extend the conductor schema, add doc generation, tighten `README.md`, create missing artifact templates, add operator governance matrices, and ship end-to-end benchmark engagements.

### Relevant Sources Read
- `README.md`
- `ARCHITECTURE.md`
- `ETHOS.md`
- `AGENTS.md`
- `PROJECT_TECHNICAL_OVERVIEW.md`
- `docs/skills.md`
- `install.sh`
- `conductor.json`
- `skills/bootcamp/SKILL.md`
- `skills/data-connector/SKILL.md`
- `skills/foundry-security/SKILL.md`
- `skills/apollo-deployer/SKILL.md`
- `skills/careful/SKILL.md`
- `skills/freeze/SKILL.md`
- `skills/guard/SKILL.md`
- Existing templates under `templates/`

### Task Packet
1. Expand `conductor.json` into the canonical skill and artifact registry, including governance metadata, generated-doc settings, and example/eval references.
2. Add a generator script that renders the skill inventory and artifact chain into `README.md` and `docs/skills.md`.
3. Create `PROGRAM.md` as the operator manual with phase gates, execution cadence, concurrency rules, escalation paths, governance boundaries, and artifact acceptance rules.
4. Add the missing artifact templates so every conductor artifact has a template, rubric, and example coverage.
5. Add `examples/` with at least one supply chain and one healthcare/manufacturing-style end-to-end engagement.
6. Add `evals/` with realistic benchmark cases, scoring rubrics, and golden/reference expectations.
7. Update `PROJECT_TECHNICAL_OVERVIEW.md` and `CHANGELOG.md`, then run generator/consistency verification.

### Success Criteria
- `PROGRAM.md` exists and acts as an operator manual instead of a project overview.
- `README.md` no longer drifts from `conductor.json` for skill inventory and artifact flow.
- Every artifact named in `conductor.json` has a corresponding template file.
- `examples/` includes at least two realistic engagement directories with chained artifacts.
- `evals/` exists with benchmark cases, rubrics, and expected-output guidance.
- `PROJECT_TECHNICAL_OVERVIEW.md` and `CHANGELOG.md` reflect the new system design.

### Verification Plan
- Run the new generator script and confirm it rewrites the generated sections cleanly.
- Run `rg` checks to ensure every conductor artifact filename exists under `templates/` and appears under `examples/`.
- Run targeted Python validation against `conductor.json`, generated docs, and example/eval inventory.

### Execution Status
- `conductor.json` expanded into the canonical registry for phases, skills, artifacts, governance, examples, and eval cases.
- `scripts/generate_docs.py` added and used to regenerate `README.md` and `docs/skills.md`.
- `PROGRAM.md` added as the operator manual.
- Template coverage completed for all conductor artifacts.
- Example engagements and eval scaffolding added for supply chain and healthcare scenarios.
