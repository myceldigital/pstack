# pstack Architecture

## System overview

pstack transforms a single Palantir deployment strategist into a conductor
of 16 specialized AI agents, each carrying deep expertise in a different
part of the Palantir technology stack. The architecture follows Garry Tan's
gstack pattern — cognitive gearing through specialized roles, artifact-chain
orchestration, and parallel session management — adapted for the unique
structure of Palantir deployments.

## The Palantir platform stack

pstack agents cover the full Palantir platform:

```
┌──────────────────────────────────────────────────────┐
│                   APPLICATIONS                        │
│  Workshop │ Slate │ OSDK Apps │ Quiver │ Contour      │
├──────────────────────────────────────────────────────┤
│                   AIP LAYER                           │
│  Agent Studio │ AIP Logic │ AIP Assist │ AIP Automate │
├──────────────────────────────────────────────────────┤
│                   ONTOLOGY                            │
│  Object Types │ Link Types │ Actions │ Functions      │
│  Interfaces │ Shared Properties │ Value Types         │
├──────────────────────────────────────────────────────┤
│                   DATA LAYER                          │
│  Pipeline Builder │ Code Repositories │ Code Workspaces│
│  Data Connection │ Data Lineage │ Datasets            │
├──────────────────────────────────────────────────────┤
│                   INFRASTRUCTURE                      │
│  Apollo │ Compute │ Storage │ Networking │ Security    │
└──────────────────────────────────────────────────────┘
```

Each layer has dedicated pstack agents:

- **Data Layer**: `/data-connector`, `/pipeline-builder`
- **Ontology**: `/ontology-vision`, `/ontology-architect`
- **Applications**: `/workshop-builder`, `/slate-builder`, `/osdk-developer`
- **AIP**: `/aip-architect`
- **Infrastructure**: `/apollo-deployer`
- **Cross-cutting**: `/foundry-reviewer`, `/foundry-security`, `/foundry-qa`
- **Meta**: `/bootcamp`, `/pipeline-plan`, `/training-writer`, `/deployment-retro`

## Agent pipeline

```
                    ┌─────────────┐
                    │  /bootcamp  │
                    └──────┬──────┘
                           │ BOOTCAMP-SCOPE.md
                    ┌──────▼──────┐
                    │  /ontology  │
                    │   -vision   │
                    └──────┬──────┘
                           │ ONTOLOGY-VISION.md
              ┌────────────┼────────────┐
              │                         │
       ┌──────▼──────┐          ┌──────▼──────┐
       │  /ontology   │          │  /pipeline  │
       │  -architect  │          │   -plan     │
       └──────┬──────┘          └──────┬──────┘
              │                         │
              │ ONTOLOGY-               │ PIPELINE-
              │ ARCHITECTURE.md         │ ARCHITECTURE.md
              │                         │
              │                  ┌──────▼──────┐
              │                  │   /data     │
              │                  │  -connector │
              │                  └──────┬──────┘
              │                         │
              │                  ┌──────▼──────┐
              │                  │  /pipeline  │
              │                  │  -builder   │
              │                  └──────┬──────┘
              │                         │
              ▼                         ▼
    ┌─────────────────────────────────────────┐
    │         BUILD LAYER (parallel)          │
    │                                         │
    │  /workshop-builder  /aip-architect      │
    │  /osdk-developer    /slate-builder      │
    └─────────────┬───────────────────────────┘
                  │
    ┌─────────────▼───────────────────────────┐
    │        REVIEW LAYER (parallel)          │
    │                                         │
    │  /foundry-reviewer  /foundry-security   │
    └─────────────┬───────────────────────────┘
                  │
           ┌──────▼──────┐
           │ /foundry-qa │
           └──────┬──────┘
                  │
    ┌─────────────▼───────────────────────────┐
    │         SHIP LAYER (sequential)         │
    │                                         │
    │  /apollo-deployer  /training-writer     │
    └─────────────┬───────────────────────────┘
                  │
           ┌──────▼──────┐
           │ /deployment │
           │   -retro    │
           └─────────────┘
```

## Artifact chain

Every agent produces a named artifact. Downstream agents read upstream
artifacts. This is the coordination mechanism — agents never communicate
directly.

| Agent | Reads | Produces |
|-------|-------|----------|
| `/bootcamp` | Customer brief | `BOOTCAMP-SCOPE.md` |
| `/ontology-vision` | `BOOTCAMP-SCOPE.md` | `ONTOLOGY-VISION.md` |
| `/ontology-architect` | `ONTOLOGY-VISION.md` | `ONTOLOGY-ARCHITECTURE.md` |
| `/pipeline-plan` | `BOOTCAMP-SCOPE.md`, `ONTOLOGY-VISION.md` | `PIPELINE-ARCHITECTURE.md` |
| `/data-connector` | `PIPELINE-ARCHITECTURE.md` | `DATA-CONNECTION-STATUS.md` |
| `/pipeline-builder` | `PIPELINE-ARCHITECTURE.md`, `DATA-CONNECTION-STATUS.md` | `PIPELINE-BUILD-STATUS.md` |
| `/workshop-builder` | `ONTOLOGY-ARCHITECTURE.md` | `WORKSHOP-BUILD-STATUS.md` |
| `/aip-architect` | `ONTOLOGY-ARCHITECTURE.md`, `WORKSHOP-BUILD-STATUS.md` | `AIP-AGENT-STATUS.md` |
| `/osdk-developer` | `ONTOLOGY-ARCHITECTURE.md` | `OSDK-BUILD-STATUS.md` |
| `/slate-builder` | `ONTOLOGY-ARCHITECTURE.md` | `SLATE-BUILD-STATUS.md` |
| `/foundry-reviewer` | All build artifacts | `REVIEW-REPORT.md` |
| `/foundry-security` | All build artifacts | `SECURITY-AUDIT.md` |
| `/foundry-qa` | All build artifacts | `QA-REPORT.md` |
| `/apollo-deployer` | `QA-REPORT.md` | `DEPLOYMENT-PLAN.md` |
| `/training-writer` | All architecture + build artifacts | `TRAINING-MATERIALS.md` |
| `/deployment-retro` | All artifacts | `RETRO-REPORT.md` |

## Conductor workflow

The deployment strategist manages parallel sessions:

```
Session 1: /bootcamp ──────────────── scoping with customer SME
Session 2: /pipeline-builder ──────── building transforms for use case 1
Session 3: /ontology-architect ────── refining object types from pipeline output
Session 4: /workshop-builder ──────── building operational dashboard
Session 5: /aip-architect ─────────── configuring agents for NL queries
Session 6: /foundry-reviewer ──────── auditing pipeline code from Session 2
```

Each session runs independently. The conductor checks in when agents surface
decisions via AskUserQuestion. Everything else runs autonomously.

## Status tracking

pstack tracks deployment phase completion:

```
PSTACK DEPLOYMENT STATUS
========================

Engagement: [Customer Name]
Date: [YYYY-MM-DD]
Phase: Build

| Phase              | Status        | Blocking?                    |
|--------------------|---------------|------------------------------|
| Bootcamp scope     | ✅ COMPLETE    | —                            |
| Ontology vision    | ✅ COMPLETE    | —                            |
| Ontology arch      | 🔄 IN PROGRESS | Yes — blocks app build      |
| Pipeline arch      | ✅ COMPLETE    | —                            |
| Data connections   | ✅ COMPLETE    | —                            |
| Pipeline build     | 🔄 IN PROGRESS | Yes — blocks ontology backing|
| Workshop app       | ⏳ WAITING     | Blocked by ontology          |
| AIP agents         | ⏳ WAITING     | Blocked by ontology + app    |
| Security review    | ⏳ WAITING     | Blocked by build             |
| QA / Evals         | ⏳ WAITING     | Blocked by agents            |
| Deploy             | ⏳ WAITING     | Blocked by QA                |
| Training           | ⏳ WAITING     | Blocked by deploy            |
```

## Palantir Ontology as coordination layer

The key architectural insight: in gstack, agents coordinate through Markdown
files on the filesystem. In pstack, agents additionally coordinate through
the Ontology itself.

The Ontology is both:
1. **The product being built** — the customer's digital twin
2. **The coordination mechanism** — the shared semantic layer all agents reference

When `/pipeline-builder` creates an output dataset, `/ontology-architect`
uses it as a backing dataset. When `/ontology-architect` defines an action
type, `/workshop-builder` wires it to a button. When `/workshop-builder`
embeds an AIP widget, `/aip-architect` configures the agent behind it.

The Ontology is the API contract between every agent.

## Security model

pstack operates under the principle of least privilege:

- Agents never modify permissions without DS approval
- `/foundry-security` audits all permission configurations
- Safety skills (`/careful`, `/freeze`, `/guard`) prevent destructive operations
- All customer data access follows Palantir's marking-based security model
- Agent recommendations are staged, never auto-applied to production
