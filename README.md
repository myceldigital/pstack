# pstack — Palantir Deployment Strategist AI Team

**Turn Claude Code into a virtual Palantir deployment team.**

pstack is a collection of SKILL.md files that give AI agents structured roles
for Palantir platform deployment. Each skill is a specialist: ontology architect,
pipeline engineer, Workshop builder, AIP agent designer, security officer,
Apollo deployer, and more.

One deployment strategist. 16 agents. Bootcamp in days, not weeks.

## The problem

A Palantir deployment strategist must simultaneously hold deep expertise in:
data connection, pipeline development, ontology design, Workshop configuration,
AIP agent engineering, OSDK application development, security posture, Apollo
deployment, and customer training. During a 5-day AIP Bootcamp, cognitive
bandwidth — not platform capability — is the bottleneck.

## The solution

pstack distributes expertise across 16 specialized agents while keeping the
DS in the conductor's seat. Each agent carries deep, system-level knowledge
of its Palantir domain and produces persistent artifacts that chain together
through a disciplined sprint pipeline.

```
Discover → Vision → Architecture → Build → Review → Test → Deploy → Reflect
```

Run 5-10 parallel agent sessions. Check in only on decisions that matter.
Let the agents handle the domain expertise. You handle the customer relationship
and strategic judgment.

## Quick start

```bash
# Install pstack skills into Claude Code
git clone https://github.com/your-org/pstack.git
cd pstack && ./install.sh

# Start a new engagement
/bootcamp

# After scoping, run the planning pipeline
/ontology-vision
/ontology-architect
/pipeline-plan

# Build in parallel sessions
/data-connector    # Session 1: onboard data
/pipeline-builder  # Session 2: build transforms
/workshop-builder  # Session 3: build apps
/aip-architect     # Session 4: configure agents

# Review and ship
/foundry-reviewer
/foundry-security
/foundry-qa
/apollo-deployer
/training-writer

# Reflect
/deployment-retro
```

## Available skills

Skills live in `skills/`. Invoke them by name (e.g., `/bootcamp`).

### Think layer — discovery and scoping

| Skill | What it does |
|-------|-------------|
| `/bootcamp` | Start here. Structured discovery using AIP Bootcamp methodology. Produces `BOOTCAMP-SCOPE.md`. |
| `/ontology-vision` | Strategic ontology design. Finds the full digital twin hiding in the customer's request. |

### Plan layer — architecture and design

| Skill | What it does |
|-------|-------------|
| `/ontology-architect` | Lock ontology architecture: object types, links, actions, functions, interfaces, test plan. |
| `/pipeline-plan` | Design data integration and transformation architecture. Source-to-ontology data flow. |

### Build layer — implementation

| Skill | What it does |
|-------|-------------|
| `/data-connector` | Configure Data Connection sources, sync schedules, authentication, health monitoring. |
| `/pipeline-builder` | Build transforms in Pipeline Builder and Code Repositories. Joins, filters, aggregations. |
| `/workshop-builder` | Build Workshop apps. Layouts, widgets, events, actions, AIP agent embedding. |
| `/aip-architect` | Design AIP agents in Agent Studio. Logic functions, prompts, evals, Automate workflows. |
| `/osdk-developer` | Build custom OSDK applications. TypeScript/Python SDK, React integration, Developer Console. |
| `/slate-builder` | Build Slate apps for pixel-perfect or complex external integrations. |

### Review and test layer

| Skill | What it does |
|-------|-------------|
| `/foundry-reviewer` | Structural audit: pipeline performance, ontology modeling, Workshop UX, AIP prompts. |
| `/foundry-security` | Security audit: permissions, markings, agent scoping, OSDK scopes, data governance. |
| `/foundry-qa` | End-to-end testing: AIP Evals, pipeline validation, Workshop flow testing, health score. |

### Ship layer — deployment and production

| Skill | What it does |
|-------|-------------|
| `/apollo-deployer` | Apollo deployment lifecycle: release channels, blue-green, rollback, air-gapped. |
| `/training-writer` | Customer training materials: user guides, runbooks, training decks, CoE setup. |

### Reflect layer

| Skill | What it does |
|-------|-------------|
| `/deployment-retro` | Structured retrospective: metrics, per-use-case analysis, trend tracking. |

### Safety skills

| Skill | What it does |
|-------|-------------|
| `/careful` | Warn before destructive operations (ontology deletions, pipeline overwrites). |
| `/freeze` | Lock edits to specific Foundry project scope. |
| `/guard` | Activate both careful + freeze at once. |

## Sprint sequence

| Phase | Agent(s) | Artifact | Consumed by |
|-------|----------|----------|-------------|
| Discover | `/bootcamp` | `BOOTCAMP-SCOPE.md` | `/ontology-vision`, `/pipeline-plan` |
| Vision | `/ontology-vision` | `ONTOLOGY-VISION.md` | `/ontology-architect` |
| Architecture | `/ontology-architect` + `/pipeline-plan` | `ONTOLOGY-ARCHITECTURE.md` + `PIPELINE-ARCHITECTURE.md` | All build agents |
| Data onboarding | `/data-connector` | Working connections + raw datasets | `/pipeline-builder` |
| Pipeline build | `/pipeline-builder` | Clean output datasets | `/ontology-architect` (backing) |
| App build | `/workshop-builder` + `/aip-architect` + `/osdk-developer` | Working apps + agents | Review agents |
| Review | `/foundry-reviewer` + `/foundry-security` | Review reports + auto-fixes | Build agents (fix loop) |
| Test | `/foundry-qa` | Eval suites + health score | `/apollo-deployer` |
| Deploy | `/apollo-deployer` + `/training-writer` | Deployed system + docs | End users |
| Reflect | `/deployment-retro` | Retro report | Next phase |

## The conductor model

You are the conductor. You manage 5-10 parallel agent sessions, each working on
a different part of the deployment. Agents surface decisions in a consistent format:

```
CONTEXT: [what I found]
QUESTION: [what needs deciding]
RECOMMENDATION: Choose [X] because [reason]

A) [option with trade-off]
B) [option with trade-off]
C) [option with trade-off]
```

You make the call. They execute.

## Key conventions

- SKILL.md files define each agent's role, knowledge, constraints, and output format.
- Artifacts (design docs) chain between agents — each agent reads upstream docs and produces its own.
- Every agent knows the Ontology concept and how its work connects to the overall deployment.
- Safety skills (careful, freeze, guard) prevent destructive operations on customer environments.
- All work products follow the templates in `templates/`.

## Design principles

See [ETHOS.md](ETHOS.md) for the seven principles that govern pstack:

1. **Boil the Ontology** — model the complete entity, not the minimum.
2. **Cognitive gearing** — each agent thinks in its domain's vocabulary.
3. **Artifact chains** — agents coordinate through documents, not direct communication.
4. **DS decides, agents advise** — consistent decision format, human always decides.
5. **Fix-first** — auto-fix obvious issues, surface only ambiguous decisions.
6. **Search before building** — check Palantir templates and patterns first.
7. **Progressive trust** — start human-in-the-loop, graduate to autonomous.

## Requirements

- Claude Code (Claude Max or Claude Team)
- Familiarity with Palantir Foundry, AIP, and deployment workflows
- Access to customer Foundry environment (for build/deploy phases)

## License

MIT
