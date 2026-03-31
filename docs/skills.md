# pstack Skills Reference

## Skill Index by Phase

### Phase 1: Discover

#### `/bootcamp` — AIP Bootcamp Partner
**Purpose:** Structured discovery for new customer engagements.
**Trigger:** New engagement, "where do we start?", scoping a bootcamp.
**Reads:** Customer briefs, engagement context.
**Produces:** `BOOTCAMP-SCOPE.md`
**Key workflow:** Five Forcing Questions (Morning Question, Data Reality, Workflow
Gap, Stakeholder Map, Success Metric) → Use Case Prioritization (2x2 matrix) →
Ontology Sketch → Scope Document.

### Phase 2: Vision

#### `/ontology-vision` — Ontology Strategist
**Purpose:** Strategic ontology design that sees the full digital twin.
**Trigger:** After `/bootcamp`, "think about the ontology", "what should we model?"
**Reads:** `BOOTCAMP-SCOPE.md`
**Produces:** `ONTOLOGY-VISION.md`
**Key workflow:** Four Modes (EXPAND/SELECTIVE/HOLD/REDUCE) → Entity Identification →
Relationship Mapping → Action Design → Interface Design → Function Design → Phased
Rollout Plan.

### Phase 3: Architecture

#### `/ontology-architect` — Ontology Engineer
**Purpose:** Lock ontology with precise technical specifications.
**Trigger:** After `/ontology-vision`, "lock the architecture."
**Reads:** `ONTOLOGY-VISION.md`, `BOOTCAMP-SCOPE.md`, `PIPELINE-ARCHITECTURE.md`
**Produces:** `ONTOLOGY-ARCHITECTURE.md`
**Key workflow:** Object Type Spec (properties, types, backing columns) → Link Spec
(cardinality, foreign keys) → Action Spec (parameters, validation, writeback) →
Function Spec (signatures, performance) → Edge Cases → Test Plan.

#### `/pipeline-plan` — Data Pipeline Architect
**Purpose:** Design data integration and transformation architecture.
**Trigger:** After `/bootcamp`, "design the data flow."
**Reads:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-VISION.md`
**Produces:** `PIPELINE-ARCHITECTURE.md`
**Key workflow:** Source-to-Ontology Mapping → Connection Type Selection → Transform
DAG (RAW→CLEAN→TRANSFORM→OUTPUT) → PB vs. CR Decision → Incremental Strategy →
Quality Checks → Scheduling.

### Phase 4: Build

#### `/data-connector` — Data Integration Engineer
**Purpose:** Configure all data connections into Foundry.
**Trigger:** After `/pipeline-plan`, "connect the data."
**Reads:** `PIPELINE-ARCHITECTURE.md`, `BOOTCAMP-SCOPE.md`
**Produces:** `DATA-CONNECTION-STATUS.md`

#### `/pipeline-builder` — Pipeline Engineer
**Purpose:** Build data transformation pipelines.
**Trigger:** After `/data-connector`, "build the transforms."
**Reads:** `PIPELINE-ARCHITECTURE.md`, `DATA-CONNECTION-STATUS.md`, `ONTOLOGY-ARCHITECTURE.md`
**Produces:** `PIPELINE-BUILD-STATUS.md`

#### `/workshop-builder` — Workshop Application Developer
**Purpose:** Build operational applications in Workshop.
**Trigger:** After `/ontology-architect`, "build the app."
**Reads:** `ONTOLOGY-ARCHITECTURE.md`, `BOOTCAMP-SCOPE.md`
**Produces:** `WORKSHOP-BUILD-STATUS.md`

#### `/aip-architect` — AIP Agent Designer
**Purpose:** Design and configure AIP agents.
**Trigger:** After `/ontology-architect` and `/workshop-builder`, "configure the agent."
**Reads:** `ONTOLOGY-ARCHITECTURE.md`, `WORKSHOP-BUILD-STATUS.md`
**Produces:** `AIP-AGENT-STATUS.md`

#### `/osdk-developer` — OSDK Application Developer
**Purpose:** Build custom applications using the Ontology SDK.
**Trigger:** When Workshop can't meet UX requirements.
**Reads:** `ONTOLOGY-ARCHITECTURE.md`
**Produces:** `OSDK-BUILD-STATUS.md`

#### `/slate-builder` — Slate Application Developer
**Purpose:** Build Slate apps for pixel-perfect or complex integrations.
**Trigger:** When Workshop and OSDK don't fit.
**Reads:** `ONTOLOGY-ARCHITECTURE.md`
**Produces:** `SLATE-BUILD-STATUS.md`

### Phase 5: Review

#### `/foundry-reviewer` — Foundry Code Reviewer
**Purpose:** Structural audit of all deployment artifacts.
**Trigger:** After build phase, "review the work."
**Reads:** All build artifacts.
**Produces:** `REVIEW-REPORT.md`

#### `/foundry-security` — Foundry Security Officer
**Purpose:** Security audit with exploitation scenarios.
**Trigger:** After build phase, "audit security."
**Reads:** All build artifacts.
**Produces:** `SECURITY-AUDIT.md`

### Phase 6: Test

#### `/foundry-qa` — AIP Evaluation Engineer
**Purpose:** End-to-end testing with health score.
**Trigger:** After review, "run QA."
**Reads:** All build artifacts, `REVIEW-REPORT.md`
**Produces:** `QA-REPORT.md`

### Phase 7: Ship

#### `/apollo-deployer` — Apollo Deployment Engineer
**Purpose:** Manage deployment lifecycle through Apollo.
**Trigger:** After QA passes, "deploy."
**Reads:** `QA-REPORT.md`, `SECURITY-AUDIT.md`
**Produces:** `DEPLOYMENT-PLAN.md`

#### `/training-writer` — Customer Training Engineer
**Purpose:** Produce all customer-facing documentation and training.
**Trigger:** After deployment, "write the docs."
**Reads:** All artifacts.
**Produces:** `TRAINING-MATERIALS.md`

### Phase 8: Reflect

#### `/deployment-retro` — Deployment Retrospective
**Purpose:** Structured retrospective with metrics and lessons.
**Trigger:** After engagement completes, "run the retro."
**Reads:** All artifacts.
**Produces:** `RETRO-REPORT.md`

### Safety Skills

#### `/careful` — Destructive Operation Warning
**Purpose:** Require confirmation before destructive Foundry operations.

#### `/freeze` — Scope Restriction
**Purpose:** Lock edits to specific Foundry project scope.

#### `/guard` — Maximum Safety
**Purpose:** Activate both careful + freeze simultaneously.

---

## Artifact Chain Summary

```
BOOTCAMP-SCOPE.md
├── ONTOLOGY-VISION.md
│   └── ONTOLOGY-ARCHITECTURE.md
│       ├── WORKSHOP-BUILD-STATUS.md
│       │   └── AIP-AGENT-STATUS.md
│       ├── OSDK-BUILD-STATUS.md
│       └── SLATE-BUILD-STATUS.md
├── PIPELINE-ARCHITECTURE.md
│   ├── DATA-CONNECTION-STATUS.md
│   └── PIPELINE-BUILD-STATUS.md
├── REVIEW-REPORT.md
├── SECURITY-AUDIT.md
├── QA-REPORT.md
├── DEPLOYMENT-PLAN.md
├── TRAINING-MATERIALS.md
└── RETRO-REPORT.md
```
