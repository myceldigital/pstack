# Project Technical Overview

## Purpose

`pstack` is an operator-grade repository of AI agent skills for Palantir deployment work. It packages specialist `SKILL.md` files, a canonical conductor registry, generated operator docs, artifact templates, example engagements, and eval rubrics so a single deployment strategist can run a disciplined multi-agent delivery workflow across discovery, ontology design, data onboarding, application building, review, QA, deployment, training, and retrospectives.

## Core Concept

The repository applies a conductor model:

- The human deployment strategist remains the decision-maker.
- Specialized agents each operate in a narrow Palantir domain.
- Agents coordinate through persistent artifacts instead of direct chat-to-chat handoffs.
- The Ontology is treated as both the deployment output and the semantic contract between downstream agents.
- `conductor.json` is the source of truth for phases, skills, artifacts, governance metadata, examples, and generated docs.

## Repository Layout

### Root documents

- `README.md`: generated operator-facing overview, audience fit, first-hour/first-week guidance, and skill/artifact tables.
- `PROGRAM.md`: operator manual and execution contract with phase gates, concurrency rules, retry/split/stop logic, and safety posture.
- `ARCHITECTURE.md`: system architecture, agent pipeline, artifact chain, and security model.
- `ETHOS.md`: deployment principles that shape how the skills reason and recommend.
- `AGENTS.md`: condensed inventory of available skills and repo conventions.
- `CLAUDE.md`: workspace-specific operating rules and routing conventions.
- `workflow_state.md`: bounded planning state for the current task cycle.
- `CHANGELOG.md`: concise change history and rationale.

### Canonical registry and generation

- `conductor.json`: canonical registry of phases, skills, artifacts, governance metadata, examples, and eval cases.
- `scripts/generate_docs.py`: generates `README.md` and `docs/skills.md` from `conductor.json` to reduce drift.

### Skill definitions

- `skills/*/SKILL.md`: one folder per specialist skill.
- Skills cover discovery, planning, build, review, security, QA, deployment, training, retrospectives, and safety guardrails.

### Templates

- `templates/*.md`: artifact templates used by downstream skills.
- Every artifact named in `conductor.json` now has a corresponding template.
- The template set covers discovery, architecture, build status, review, security, QA, deployment, training, and retrospective artifacts.

### Supporting docs

- `docs/`: supporting reference material for usage and domain vocabulary.
- `docs/skills.md` is generated from `conductor.json` and includes the skill registry, artifact registry, and governance matrix.

### Examples and evals

- `examples/engagements/acme-supply-chain/`: full synthetic supply chain / manufacturing engagement with all conductor artifacts.
- `examples/engagements/northstar-healthcare/`: full synthetic healthcare engagement with all conductor artifacts.
- `evals/ARTIFACT-RUBRICS.md`: acceptance rubric for every named artifact.
- `evals/SKILL-SCORECARD.md`: benchmark score targets per skill.
- `evals/cases/*`: benchmark cases with scoped rubric and scorecards.
- `evals/golden/*`: expected-output structure references for benchmark scenarios.

## Skill Model

Each skill is invoked by slash name such as `/bootcamp` or `/pipeline-builder`. The repo is designed so each specialist:

1. Reads upstream project artifacts.
2. Produces a named downstream artifact.
3. Stays inside its domain vocabulary and responsibility boundary.
4. Escalates real strategic decisions to the human strategist.

Representative skills:

- `/bootcamp`: scopes a customer engagement.
- `/ontology-vision`: derives the full target ontology.
- `/ontology-architect`: locks object types, links, actions, and functions.
- `/pipeline-plan` and `/pipeline-builder`: design and build data movement and transforms.
- `/workshop-builder`, `/slate-builder`, `/osdk-developer`: build application surfaces.
- `/aip-architect`: configures agents and evaluations.
- `/foundry-reviewer`, `/foundry-security`, `/foundry-qa`: audit and verify the system.
- `/apollo-deployer`: handles deployment planning and rollout.
- `/training-writer` and `/deployment-retro`: close out operationalization and learning loops.
- `/careful`, `/freeze`, and `/guard`: enforce destructive-operation confirmation and scope restriction.

## Artifact-Chain Architecture

The repository assumes a document-driven workflow:

`BOOTCAMP-SCOPE.md` -> `ONTOLOGY-VISION.md` -> `ONTOLOGY-ARCHITECTURE.md` + `PIPELINE-ARCHITECTURE.md` -> build status artifacts -> review and QA reports -> deployment and training outputs.

This structure allows multiple agent sessions to run in parallel without direct coordination because each skill reads stable upstream documents and writes its own output artifact.

The artifact chain is now formalized in three places:

- `conductor.json`: canonical artifact registry
- `templates/`: concrete artifact skeletons
- `examples/engagements/*/artifacts/`: worked end-to-end examples

Artifact quality is judged against `evals/ARTIFACT-RUBRICS.md`.

## Installation And Use

The current install flow is:

1. Clone the repository.
2. Run `./install.sh`.
3. Regenerate docs with `python3 scripts/generate_docs.py` when `conductor.json` changes.
4. Invoke skills by slash command inside the supported coding environment.

The repository itself is mostly Markdown, JSON, and Python-based generation glue. There is no compiled application runtime in the current version.

## Operating Model

`PROGRAM.md` is the execution layer for the repo. It defines:

- phase gates and exit criteria
- concurrency rules
- retry/split/stop decisions
- safety posture by environment
- artifact acceptance rules
- the boundary between DS decisions and agent execution

`README.md` and `docs/skills.md` are generated reference surfaces. `PROGRAM.md` remains the human operator manual.

## Security And Operating Boundaries

- Safety skills such as `/careful`, `/freeze`, and `/guard` are intended to limit destructive actions in customer environments.
- The deployment strategist retains final authority on strategic decisions.
- The repo emphasizes least privilege, explicit review, and staged trust before autonomous execution.
- Governance metadata for each skill is now recorded in `conductor.json` and surfaced in `docs/skills.md`.

## GitHub Repository Operations

- Canonical repository: `https://github.com/myceldigital/pstack`
- Description: `AI agent skill stack for Palantir deployments, from bootcamp scoping through ontology, pipelines, apps, QA, and Apollo rollout.`
- Homepage: `https://github.com/myceldigital/pstack#readme`
- Topics: `palantir`, `foundry`, `aip`, `ai-agents`, `ontology`, `deployment`, `workshop`, `osdk`, `apollo`
- Default branch: `main`
- Branch protection baseline on `main`: pull requests required, 1 approving review required, stale approvals dismissed on new commits, force-push blocked, branch deletion blocked.

## Publish Notes

This repository was initially bootstrapped locally and then prepared for first publication to GitHub as `myceldigital/pstack`. It has since been upgraded from a skill collection into a more rigorous operator system with a canonical conductor registry, generated docs, a formal program manual, full template coverage, end-to-end examples, and eval rubrics.
