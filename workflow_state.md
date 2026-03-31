## Workflow State

### Current Cycle
- Role: `Worker`
- Objective: Rewrite the `examples/` folder into fully populated, realistic end-to-end Palantir deployment engagements.
- Scope: Expand both example engagements across every artifact in the chain, upgrade the examples-facing README files, and update root overview/changelog docs to reflect the new example fidelity.

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
- `PROGRAM.md`
- `scripts/generate_docs.py`
- `evals/ARTIFACT-RUBRICS.md`
- `evals/SKILL-SCORECARD.md`

### Task Packet
1. Rewrite `examples/README.md` and both engagement-level READMEs with realistic program context.
2. Rewrite all artifact files for `acme-supply-chain` with concrete business, data, architecture, review, QA, security, deployment, training, and retro detail.
3. Rewrite all artifact files for `northstar-healthcare` to the same depth with healthcare-specific operational detail.
4. Update `PROJECT_TECHNICAL_OVERVIEW.md` and `CHANGELOG.md` to record the example-library upgrade.
5. Verify representative artifacts and lint the touched files.

### Success Criteria
- Both engagements read like real DS project artifacts rather than thin examples.
- Every artifact contains concrete stakeholders, systems, metrics, risks, handoffs, and decisions.
- The examples folder can serve as an end-to-end operator reference for realistic customer work.
- `PROJECT_TECHNICAL_OVERVIEW.md` and `CHANGELOG.md` reflect the upgraded example fidelity.

### Verification Plan
- Read representative artifacts across both engagements after generation.
- Run `ReadLints` on touched files.

### Execution Status
- Example audit complete: the folder is structurally complete but the documents are still skeletal.
- Full-content rewrite completed for both example engagements and example-facing docs.
- Root overview and changelog docs updated to reflect the higher-fidelity example library.
- Verification in progress.
