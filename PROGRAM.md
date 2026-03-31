# PROGRAM

## Mission

Run Palantir deployments like an operating program, not a prompt jam.

`pstack` exists to let one deployment strategist coordinate specialized agents without losing control of scope, customer trust, or delivery rigor. The deployment strategist owns strategy, customer politics, acceptance decisions, and production approvals. Agents own bounded analysis and bounded artifact production.

## Core Rule

No downstream skill advances on vibes.

Every phase must leave behind an artifact that is:

1. complete enough for the next specialist to use
2. explicit enough to survive a context switch
3. reviewable by the DS without re-reading the whole chat
4. honest about blockers, risk, and missing evidence

If an artifact is weak, the answer is not "push through." The answer is `retry`, `split`, or `stop`.

## Operating Roles

### Deployment Strategist

Owns:

- customer framing
- use-case priority
- strategic trade-offs
- risk acceptance
- production approvals
- when to stop work that is no longer worth doing

Does not delegate:

- permission changes in customer environments
- production deployment approval
- customer-facing scope decisions
- acceptance of unresolved security or QA risk

### Specialist Agents

Own:

- reading upstream artifacts
- producing their named artifact or bounded output
- surfacing decisions in a compressed format
- fixing obvious local issues before escalating

Do not own:

- changing engagement scope
- silently overriding upstream intent
- production-destructive operations
- inventing data, workflows, or customer constraints

## Safety Posture

Default safety posture by environment:

- Internal design work: normal mode
- Customer build work in non-production: `/freeze`
- Customer production work: `/guard`

Use `/careful` when any step can delete, overwrite, rebind, rescope, or deploy something the customer already depends on.

## Phase Gates

### 1. Discover

Primary skill: `/bootcamp`

Required output:

- `BOOTCAMP-SCOPE.md`

Exit criteria:

- headline use case selected
- quick win selected or explicitly deferred
- operational decision is named, not implied
- success metric has a number
- source systems and owners are named
- stakeholder map includes sponsor, operator, and technical gatekeeper

Failure modes:

- customer wants "visibility" instead of a decision workflow
- no named metric
- no viable data path
- too many use cases for the time box

Decision owner:

- DS

If gate fails:

- `retry` if the customer context is real but underspecified
- `split` if multiple use cases are competing
- `stop` if no decision-centered use case with usable data exists

### 2. Vision

Primary skill: `/ontology-vision`

Required output:

- `ONTOLOGY-VISION.md`

Exit criteria:

- core entities are explicit
- links and actions reflect the real operating model
- phased rollout is clear
- out-of-scope entities are explicitly deferred

Failure modes:

- ontology mirrors UI screens instead of real-world entities
- links are omitted because of time pressure
- action types are vague or delegated to "later"

Decision owner:

- DS

If gate fails:

- `retry` with tighter use-case constraints
- `split` if one engagement is hiding multiple ontologies

### 3. Architecture

Primary skills:

- `/ontology-architect`
- `/pipeline-plan`

Required outputs:

- `ONTOLOGY-ARCHITECTURE.md`
- `PIPELINE-ARCHITECTURE.md`

Exit criteria:

- ontology backing datasets are identified or intentionally pending
- transform stages are defined from source to output
- action/writeback paths are explicit
- test plan exists for object types, links, actions, and functions
- batch vs incremental strategy is explicit

Failure modes:

- ontology and pipeline disagree on keys or joins
- architecture assumes data access that the customer has not approved
- build choice depends on unresolved app or agent behavior

Decision owner:

- DS for architecture lock

If gate fails:

- `retry` if the design is salvageable
- `split` into architecture and data-readiness tracks if access is the bottleneck

### 4. Build

Primary skills:

- `/data-connector`
- `/pipeline-builder`
- `/workshop-builder`
- `/aip-architect`
- `/osdk-developer`
- `/slate-builder`

Required outputs:

- `DATA-CONNECTION-STATUS.md`
- `PIPELINE-BUILD-STATUS.md`
- `WORKSHOP-BUILD-STATUS.md`
- `AIP-AGENT-STATUS.md`
- `OSDK-BUILD-STATUS.md`
- `SLATE-BUILD-STATUS.md`

Concurrency rules:

- `/data-connector` must start before `/pipeline-builder`
- `/ontology-architect` should be locked before any app or agent build starts
- `/workshop-builder` can run in parallel with `/pipeline-builder` once ontology is stable
- `/aip-architect` starts after the app surface and ontology are both credible
- `/osdk-developer` and `/slate-builder` are exceptions, not defaults

Exit criteria:

- data sync path is real
- pipeline outputs exist and match the ontology
- at least one operator-facing app path is functional
- agent scope is bounded and evaluated
- every build artifact names blockers and next steps

Failure modes:

- builds compensate for missing architecture by inventing structure
- apps encode business logic that belongs in ontology or pipeline layers
- agents are given broad context because the ontology is weak
- production-like resources are changed without safety modes

Decision owner:

- DS for scope changes
- DS plus technical gatekeeper for risky environment changes

If gate fails:

- `retry` on the failing specialist
- `split` if data onboarding and UX work need separate timelines

### 5. Review

Primary skills:

- `/foundry-reviewer`
- `/foundry-security`

Required outputs:

- `REVIEW-REPORT.md`
- `SECURITY-AUDIT.md`

Exit criteria:

- structural flaws are named and, where obvious, already fixed
- every nontrivial security issue includes exploitation path and remediation
- DS understands residual risks in plain language

Failure modes:

- review becomes passive commentary with no fix loop
- security review lacks severity or exploit framing
- scope changes are proposed under the label of “cleanup”

Decision owner:

- DS for accepting residual risk

If gate fails:

- `retry` on the offending build artifact
- `stop` if the customer environment is not governable enough for safe continuation

### 6. Test

Primary skill:

- `/foundry-qa`

Required output:

- `QA-REPORT.md`

Exit criteria:

- critical user flows are tested
- health score is explicit
- known failures and gaps are named
- deployment recommendation is justified from evidence

Failure modes:

- QA only restates intended behavior
- no negative or edge-path evidence
- a weak artifact chain forces QA to guess expected outcomes

Decision owner:

- DS for accepting borderline readiness

If gate fails:

- `retry` with targeted fixes
- `stop` if the deployment window is gone or evidence is too weak

### 7. Ship

Primary skills:

- `/apollo-deployer`
- `/training-writer`

Required outputs:

- `DEPLOYMENT-PLAN.md`
- `TRAINING-MATERIALS.md`

Exit criteria:

- deployment strategy is explicit
- rollback plan exists
- security verdict is acceptable
- customer enablement material matches the actual delivered system

Failure modes:

- training describes features that are not deployed
- deploy strategy assumes healthy telemetry that does not exist
- rollout happens without named rollback owner

Decision owner:

- DS for release approval
- technical gatekeeper for environment access and controls

If gate fails:

- `retry` if the issue is operationally fixable
- `stop` if the release risk is not acceptable

### 8. Reflect

Primary skill:

- `/deployment-retro`

Required output:

- `RETRO-REPORT.md`

Exit criteria:

- lessons are specific
- metrics are tied back to the original bootcamp scope
- next-phase recommendations are concrete

Failure modes:

- retrospective is sanitized
- no distinction between avoidable mistakes and unavoidable constraints

## Artifact Acceptance Standard

Every artifact must answer four questions before it can be treated as upstream truth:

1. What decision does this artifact enable?
2. What evidence supports it?
3. What remains uncertain?
4. What should the next skill do with it?

Minimum quality bar:

- headings are complete
- assumptions are explicit
- blockers are named
- owner and date are present
- next step is unambiguous

If any of those are missing, the artifact is not ready.

Detailed per-artifact rubric coverage lives in `evals/ARTIFACT-RUBRICS.md`.

## Concurrency Rules

Allowed in parallel:

- `/ontology-vision` + `/pipeline-plan` after `BOOTCAMP-SCOPE.md`
- `/pipeline-builder` + `/workshop-builder` after architecture lock
- `/foundry-reviewer` + `/foundry-security` after build outputs exist

Never in parallel without an explicit reason:

- architecture lock and destructive environment changes
- app build and unresolved ontology redesign
- production deployment and unresolved security remediation

Preferred rhythm:

1. lock artifact
2. fan out bounded specialists
3. converge in review
4. test from evidence
5. deploy only with rollback

## Escalation Format

When a skill needs a real decision, the message should fit this pattern:

```text
CONTEXT: what changed or what was discovered
QUESTION: the exact decision required
RECOMMENDATION: choose X because Y

A) option with trade-off
B) option with trade-off
C) option with trade-off
```

If the agent cannot produce that cleanly, it probably has not thought the issue through enough yet.

## Retry, Split, Stop

Use `retry` when:

- the problem is local
- upstream intent is still valid
- one specialist can repair the artifact without changing scope

Use `split` when:

- the engagement hides multiple use cases or ontologies
- data readiness and product design need separate tracks
- one path can continue while another blocks

Use `stop` when:

- the customer cannot name a real decision workflow
- no viable data path exists
- permissions or governance make safe delivery impossible
- the artifact chain is being propped up by invention instead of evidence

## Governance Contract

Detailed per-skill governance lives in generated form in `docs/skills.md`, sourced from `conductor.json`.

The contract is:

- every skill has an explicit writes scope
- every skill has an approval threshold
- destructive boundaries are named, not implied
- safety modes are part of normal operations, not emergency theater

## First-Week Cadence

### Day 1

- run `/bootcamp`
- leave with one headline use case and one metric that matters

### Day 2

- run `/ontology-vision`
- run `/pipeline-plan`
- lock architecture choices that will unblock builders

### Day 3

- stand up data access
- start transforms
- build the first operator-facing app path

### Day 4

- run review and security
- patch obvious issues
- run QA on actual flows

### Day 5

- finalize deployment plan
- finalize training material
- document what comes next

## Stop Doing These

- using app screens as the ontology source
- calling “visibility” a use case
- treating missing data access as a minor implementation detail
- widening scope midweek because a stakeholder got excited
- letting QA or security be the first time a design is read critically
- deploying because the demo looked good

## Source Of Truth

`conductor.json` is the canonical registry for:

- phases
- skills
- artifacts
- governance metadata
- examples
- eval case inventory

Generated docs:

- `README.md`
- `docs/skills.md`

Operator docs that should be reviewed whenever the conductor changes:

- `PROGRAM.md`
- `PROJECT_TECHNICAL_OVERVIEW.md`
- `CHANGELOG.md`
