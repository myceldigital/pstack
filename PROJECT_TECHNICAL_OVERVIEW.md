# Project Technical Overview

## Purpose

`pstack` is a repository of AI agent skills for Palantir deployment work. It packages a set of role-specific `SKILL.md` files, supporting templates, and reference documentation so a single deployment strategist can orchestrate a multi-agent delivery workflow across discovery, ontology design, pipeline work, application building, review, QA, deployment, and retrospective analysis.

## Core Concept

The repository applies a conductor model:

- The human deployment strategist remains the decision-maker.
- Specialized agents each operate in a narrow Palantir domain.
- Agents coordinate through persistent artifacts instead of direct chat-to-chat handoffs.
- The Ontology is treated as both the deployment output and the semantic contract between downstream agents.

## Repository Layout

### Root documents

- `README.md`: project overview, quick start, skill catalog, and deployment sequence.
- `ARCHITECTURE.md`: system architecture, agent pipeline, artifact chain, and security model.
- `ETHOS.md`: deployment principles that shape how the skills reason and recommend.
- `AGENTS.md`: condensed inventory of available skills and repo conventions.
- `CLAUDE.md`: workspace-specific operating rules and routing conventions.
- `workflow_state.md`: bounded planning state for the current task cycle.
- `CHANGELOG.md`: concise change history and rationale.

### Skill definitions

- `skills/*/SKILL.md`: one folder per specialist skill.
- Skills cover discovery, planning, build, review, security, QA, deployment, training, retrospectives, and safety guardrails.

### Templates

- `templates/*.md`: artifact templates used by downstream skills.
- These provide standard outputs for bootcamp scoping, ontology and pipeline architecture, QA, security audit, deployment planning, and retrospectives.

### Supporting docs

- `docs/`: supporting reference material for usage and domain vocabulary.

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

## Artifact-Chain Architecture

The repository assumes a document-driven workflow:

`BOOTCAMP-SCOPE.md` -> `ONTOLOGY-VISION.md` -> `ONTOLOGY-ARCHITECTURE.md` + `PIPELINE-ARCHITECTURE.md` -> build status artifacts -> review and QA reports -> deployment and training outputs.

This structure allows multiple agent sessions to run in parallel without direct coordination because each skill reads stable upstream documents and writes its own output artifact.

## Installation And Use

The current install flow is:

1. Clone the repository.
2. Run `./install.sh`.
3. Invoke skills by slash command inside the supported coding environment.

The repository itself is mostly Markdown and shell glue. There is no application runtime, package manifest, or compiled code in the current version.

## Security And Operating Boundaries

- Safety skills such as `/careful`, `/freeze`, and `/guard` are intended to limit destructive actions in customer environments.
- The deployment strategist retains final authority on strategic decisions.
- The repo emphasizes least privilege, explicit review, and staged trust before autonomous execution.

## Publish Notes

This repository was initially bootstrapped locally and then prepared for first publication to GitHub as `myceldigital/pstack`. The first publish includes repository hygiene files and documentation required to make the project understandable from the root without external context.
