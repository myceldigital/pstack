# pstack — Palantir Deployment AI Team

pstack is a collection of SKILL.md files that give AI agents structured roles
for Palantir platform deployment. Each skill is a specialist: ontology architect,
pipeline engineer, Workshop builder, AIP agent designer, security officer,
Apollo deployer, and more.

## Available skills

Skills live in `skills/`. Invoke them by name (e.g., `/bootcamp`).

| Skill | What it does |
|-------|-------------|
| `/bootcamp` | Start here. Structured discovery using AIP Bootcamp methodology. |
| `/ontology-vision` | Strategic ontology design: find the full digital twin in the request. |
| `/ontology-architect` | Lock ontology architecture: object types, links, actions, functions, tests. |
| `/pipeline-plan` | Design data integration and transformation architecture. |
| `/data-connector` | Configure Data Connection sources, sync, auth, health monitoring. |
| `/pipeline-builder` | Build transforms in Pipeline Builder and Code Repositories. |
| `/workshop-builder` | Build Workshop apps: layouts, widgets, events, actions, AIP embedding. |
| `/aip-architect` | Design AIP agents in Agent Studio. Logic, prompts, evals, Automate. |
| `/osdk-developer` | Build custom OSDK applications with TypeScript/Python SDK. |
| `/slate-builder` | Build Slate apps for pixel-perfect or complex integrations. |
| `/foundry-reviewer` | Structural audit: pipelines, ontology, Workshop, AIP prompts. |
| `/foundry-security` | Security audit: permissions, markings, agent scoping, governance. |
| `/foundry-qa` | End-to-end testing: AIP Evals, pipeline validation, health score. |
| `/apollo-deployer` | Apollo deployment: release channels, blue-green, rollback, air-gap. |
| `/training-writer` | Training materials: user guides, runbooks, decks, CoE setup. |
| `/deployment-retro` | Retrospective: metrics, per-use-case analysis, trend tracking. |
| `/careful` | Warn before destructive operations on customer environments. |
| `/freeze` | Lock edits to a specific Foundry project scope. |
| `/guard` | Activate both careful + freeze at once. |

## Key conventions

- SKILL.md files define each agent's role, knowledge, constraints, and output format.
- Artifacts chain between agents — each reads upstream docs and produces its own.
- Every agent knows the Ontology concept and how its work connects to the deployment.
- Safety skills prevent destructive operations on customer Foundry environments.
- All work products follow the templates in `templates/`.
