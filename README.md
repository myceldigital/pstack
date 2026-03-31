# pstack — Palantir Deployment Strategist AI Team

**Turn one deployment strategist into a disciplined multi-agent Palantir delivery team.**

`pstack` is an operator-grade repository of AI skills for Palantir deployments. It is built for deployment strategists who need an execution contract, not a loose collection of prompts: phase gates, artifact handoffs, governance boundaries, examples, and evals all live in one repo.

## What This Is

`pstack` turns one deployment strategist into a conductor for discovery, ontology, data, application, QA, security, deployment, and retrospective work. The repo is organized around a strict artifact chain so downstream skills consume stable documents rather than improvising off chat history.

## Who This Is For

- Deployment strategists running AIP bootcamps or compressed phase-zero engagements
- Foundry builders who need a disciplined artifact chain across ontology, pipeline, app, and QA work
- Operators managing multiple parallel AI sessions and wanting explicit phase gates

## Who This Is Not For

- Teams looking for a generic prompt pack without phase discipline
- Pure software projects with no Foundry, ontology, or Apollo deployment surface
- Production changes without a human deployment strategist owning approvals

## First Hour

1. Clone the repo and run `./install.sh`.
2. Start with `/bootcamp` and produce `BOOTCAMP-SCOPE.md`.
3. Run `/ontology-vision` and `/pipeline-plan` in parallel once the use case is locked.
4. Promote only the headliner use case into `/ontology-architect`.
5. Do not start build skills until the architecture artifacts are reviewed.

## First Week

1. Day 1: Lock the customer problem, use-case ranking, stakeholder map, and data inventory.
2. Day 2: Finalize ontology and pipeline architecture with explicit gating assumptions.
3. Day 3-4: Run build skills in parallel behind the artifact chain.
4. Day 4-5: Run review, security, and QA before any Apollo cutover discussion.
5. End of week: Produce deployment plan, training materials, and retrospective so the next phase starts from evidence instead of memory.

## Quick Start

```bash
git clone https://github.com/myceldigital/pstack.git
cd pstack
./install.sh

# Start with structured discovery
/bootcamp
/ontology-vision
/pipeline-plan
/ontology-architect
```

## Skills

The skill inventory below is generated from `conductor.json`.

### Discover

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/bootcamp` | Structured discovery for new engagements; produces the bootcamp scope and use-case priority. | Customer brief / engagement context | `BOOTCAMP-SCOPE.md` |

### Vision

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/ontology-vision` | Expands the bootcamp scope into the full target digital twin and phased ontology vision. | `BOOTCAMP-SCOPE.md` | `ONTOLOGY-VISION.md` |

### Architecture

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/ontology-architect` | Locks object types, links, actions, functions, interfaces, and ontology test plans. | `BOOTCAMP-SCOPE.md`, `ONTOLOGY-VISION.md`, `PIPELINE-ARCHITECTURE.md` | `ONTOLOGY-ARCHITECTURE.md` |
| `/pipeline-plan` | Designs source-to-ontology flow, connection strategy, transform DAGs, and scheduling. | `BOOTCAMP-SCOPE.md`, `ONTOLOGY-VISION.md` | `PIPELINE-ARCHITECTURE.md` |

### Build

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/data-connector` | Configures data connections, raw datasets, first-stage cleaning, and health monitoring. | `BOOTCAMP-SCOPE.md`, `PIPELINE-ARCHITECTURE.md` | `DATA-CONNECTION-STATUS.md` |
| `/pipeline-builder` | Builds transforms, quality checks, and output datasets that back the ontology. | `DATA-CONNECTION-STATUS.md`, `PIPELINE-ARCHITECTURE.md`, `ONTOLOGY-ARCHITECTURE.md` | `PIPELINE-BUILD-STATUS.md` |
| `/workshop-builder` | Builds operational Workshop apps, wiring actions, variables, widgets, and flows. | `BOOTCAMP-SCOPE.md`, `ONTOLOGY-ARCHITECTURE.md` | `WORKSHOP-BUILD-STATUS.md` |
| `/aip-architect` | Designs agent prompts, context scope, tools, evals, and Automate workflows. | `ONTOLOGY-ARCHITECTURE.md`, `WORKSHOP-BUILD-STATUS.md` | `AIP-AGENT-STATUS.md` |
| `/osdk-developer` | Builds custom applications against the Ontology SDK when Workshop is insufficient. | `ONTOLOGY-ARCHITECTURE.md` | `OSDK-BUILD-STATUS.md` |
| `/slate-builder` | Builds Slate apps for complex, pixel-precise, or deeply integrated user experiences. | `ONTOLOGY-ARCHITECTURE.md` | `SLATE-BUILD-STATUS.md` |

### Review

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/foundry-reviewer` | Performs structural audit of pipeline, ontology, app, and agent deliverables. | `PIPELINE-BUILD-STATUS.md`, `WORKSHOP-BUILD-STATUS.md`, `AIP-AGENT-STATUS.md`, `OSDK-BUILD-STATUS.md`, `SLATE-BUILD-STATUS.md`, `ONTOLOGY-ARCHITECTURE.md` | `REVIEW-REPORT.md` |
| `/foundry-security` | Audits permissions, markings, agent scoping, OAuth scopes, data governance, and deployment security. | `ONTOLOGY-ARCHITECTURE.md`, `AIP-AGENT-STATUS.md`, `OSDK-BUILD-STATUS.md`, `PIPELINE-BUILD-STATUS.md`, `WORKSHOP-BUILD-STATUS.md` | `SECURITY-AUDIT.md` |

### Test

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/foundry-qa` | Runs end-to-end QA, evals, and readiness scoring before deployment. | `REVIEW-REPORT.md`, `PIPELINE-BUILD-STATUS.md`, `WORKSHOP-BUILD-STATUS.md`, `AIP-AGENT-STATUS.md`, `SECURITY-AUDIT.md` | `QA-REPORT.md` |

### Ship

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/apollo-deployer` | Manages release channels, deployment strategy, rollback, and post-deploy verification. | `QA-REPORT.md`, `SECURITY-AUDIT.md` | `DEPLOYMENT-PLAN.md` |
| `/training-writer` | Produces customer guides, runbooks, decks, and enablement materials from the built system. | `DEPLOYMENT-PLAN.md`, `QA-REPORT.md`, `SECURITY-AUDIT.md`, `ONTOLOGY-ARCHITECTURE.md`, `WORKSHOP-BUILD-STATUS.md`, `AIP-AGENT-STATUS.md` | `TRAINING-MATERIALS.md` |

### Reflect

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/deployment-retro` | Captures engagement metrics, friction points, lessons learned, and next-wave opportunities. | `BOOTCAMP-SCOPE.md`, `ONTOLOGY-ARCHITECTURE.md`, `REVIEW-REPORT.md`, `QA-REPORT.md`, `DEPLOYMENT-PLAN.md`, `TRAINING-MATERIALS.md` | `RETRO-REPORT.md` |

### Safety

| Skill | Purpose | Reads | Produces |
|-------|---------|-------|----------|
| `/careful` | Requires explicit DS confirmation before destructive Foundry operations. | Customer brief / engagement context | Policy mode |
| `/freeze` | Restricts all modifications to an explicit project, use-case, or environment scope. | Customer brief / engagement context | Policy mode |
| `/guard` | Combines careful and freeze for maximum safety in production customer work. | Customer brief / engagement context | Policy mode |

## Sprint Sequence

| Phase | Goal | Primary skills | Primary artifacts |
|-------|------|----------------|-------------------|
| Discover | Lock the operational problem, customer context, and use-case priority. | `/bootcamp` | `BOOTCAMP-SCOPE.md` |
| Vision | Model the full digital twin and target ontology direction. | `/ontology-vision` | `ONTOLOGY-VISION.md` |
| Architecture | Turn the chosen use case into precise ontology and pipeline designs. | `/ontology-architect`, `/pipeline-plan` | `ONTOLOGY-ARCHITECTURE.md`, `PIPELINE-ARCHITECTURE.md` |
| Build | Stand up data connections, transforms, apps, and agents in parallel. | `/data-connector`, `/pipeline-builder`, `/workshop-builder`, `/aip-architect`, `/osdk-developer`, `/slate-builder` | `DATA-CONNECTION-STATUS.md`, `PIPELINE-BUILD-STATUS.md`, `WORKSHOP-BUILD-STATUS.md`, `AIP-AGENT-STATUS.md`, `OSDK-BUILD-STATUS.md`, `SLATE-BUILD-STATUS.md` |
| Review | Audit quality, security, and operability before testing. | `/foundry-reviewer`, `/foundry-security` | `REVIEW-REPORT.md`, `SECURITY-AUDIT.md` |
| Test | Run end-to-end validation and produce a deployment verdict. | `/foundry-qa` | `QA-REPORT.md` |
| Ship | Deploy safely and enable adoption. | `/apollo-deployer`, `/training-writer` | `DEPLOYMENT-PLAN.md`, `TRAINING-MATERIALS.md` |
| Reflect | Capture lessons, metrics, and next-phase opportunities. | `/deployment-retro` | `RETRO-REPORT.md` |

## Artifact Chain

Every named artifact below has a template in `templates/`, rubric coverage in `evals/ARTIFACT-RUBRICS.md`, and live examples under `examples/engagements/`.

```text
BOOTCAMP-SCOPE.md -> /ontology-vision, /pipeline-plan, /ontology-architect, /data-connector, /workshop-builder
ONTOLOGY-VISION.md -> /ontology-architect, /pipeline-plan
ONTOLOGY-ARCHITECTURE.md -> /pipeline-builder, /workshop-builder, /aip-architect, /osdk-developer, /slate-builder, /foundry-security, /foundry-qa
PIPELINE-ARCHITECTURE.md -> /data-connector, /ontology-architect, /pipeline-builder
DATA-CONNECTION-STATUS.md -> /pipeline-builder
PIPELINE-BUILD-STATUS.md -> /foundry-reviewer, /foundry-qa
WORKSHOP-BUILD-STATUS.md -> /aip-architect, /foundry-reviewer, /foundry-qa
AIP-AGENT-STATUS.md -> /foundry-reviewer, /foundry-security, /foundry-qa
OSDK-BUILD-STATUS.md -> /foundry-reviewer, /foundry-security, /foundry-qa
SLATE-BUILD-STATUS.md -> /foundry-reviewer, /foundry-qa
REVIEW-REPORT.md -> /foundry-qa, /deployment-retro
SECURITY-AUDIT.md -> /apollo-deployer, /deployment-retro
QA-REPORT.md -> /apollo-deployer, /deployment-retro
DEPLOYMENT-PLAN.md -> /training-writer, /deployment-retro
TRAINING-MATERIALS.md -> /deployment-retro
RETRO-REPORT.md -> end of chain
```

## Operator Governance

Use `PROGRAM.md` as the field manual. It defines:

- when an artifact is good enough to advance
- what can run in parallel and what must block
- when to activate `/careful`, `/freeze`, or `/guard`
- what requires explicit DS approval
- how to stop, retry, or split an engagement when the artifact chain breaks

## Examples And Evals

- `examples/engagements/acme-supply-chain/` — control-tower style supply chain engagement
- `examples/engagements/northstar-healthcare/` — patient-flow style healthcare engagement
- `evals/` — benchmark cases, artifact rubrics, and reference scorecards

## Repo Structure

- `PROGRAM.md`: operator manual and execution contract
- `conductor.json`: source of truth for phases, skills, artifacts, governance, and examples
- `docs/skills.md`: generated detailed skill and artifact registry
- `templates/`: artifact templates for every conductor artifact
- `examples/`: end-to-end synthetic engagements
- `evals/`: benchmark cases, rubrics, and reference scorecards

## Design Principles

See `ETHOS.md` for the operating philosophy. `PROGRAM.md` is the execution layer that turns those principles into actual gating, concurrency, and approval rules.

## Requirements

- Claude Code (or equivalent environment that can consume the installed skills)
- Familiarity with Palantir Foundry, AIP, and deployment workflows
- A deployment strategist willing to own customer-facing decisions and approval gates

## License

MIT
