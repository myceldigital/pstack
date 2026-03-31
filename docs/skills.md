# pstack Skills Reference

_This document is generated from `conductor.json`._

## Skill Index by Phase

### Discover

#### `/bootcamp` — AIP Bootcamp Partner
**Purpose:** Structured discovery for new engagements; produces the bootcamp scope and use-case priority.
**Reads:** Customer brief / engagement context
**Produces:** `BOOTCAMP-SCOPE.md`
**Hard gate:** Do not build, configure Foundry resources, or design the full ontology. Output only the bootcamp scope.
**Writes scope:** BOOTCAMP-SCOPE.md only
**Approval threshold:** Choosing the headline and quick-win use cases; Committing to customer-facing success metrics
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

### Vision

#### `/ontology-vision` — Ontology Strategist
**Purpose:** Expands the bootcamp scope into the full target digital twin and phased ontology vision.
**Reads:** `BOOTCAMP-SCOPE.md`
**Produces:** `ONTOLOGY-VISION.md`
**Hard gate:** Do not lock technical backing datasets or build apps. Output only the ontology vision.
**Writes scope:** ONTOLOGY-VISION.md only
**Approval threshold:** Selecting the ontology expansion mode; Deferring out-of-scope entities or interfaces
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

### Architecture

#### `/ontology-architect` — Ontology Engineer
**Purpose:** Locks object types, links, actions, functions, interfaces, and ontology test plans.
**Reads:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-VISION.md`, `PIPELINE-ARCHITECTURE.md`
**Produces:** `ONTOLOGY-ARCHITECTURE.md`
**Hard gate:** Do not configure data connections or build application surfaces. Output only the ontology architecture.
**Writes scope:** ONTOLOGY-ARCHITECTURE.md only
**Approval threshold:** Locking object boundaries, action scope, and writeback patterns
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

#### `/pipeline-plan` — Data Pipeline Architect
**Purpose:** Designs source-to-ontology flow, connection strategy, transform DAGs, and scheduling.
**Reads:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-VISION.md`
**Produces:** `PIPELINE-ARCHITECTURE.md`
**Hard gate:** Do not configure connections or write transforms. Output only the pipeline architecture.
**Writes scope:** PIPELINE-ARCHITECTURE.md only
**Approval threshold:** Choosing batch vs incremental vs CDC; Picking Pipeline Builder vs Code Repositories
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

### Build

#### `/data-connector` — Data Integration Engineer
**Purpose:** Configures data connections, raw datasets, first-stage cleaning, and health monitoring.
**Reads:** `BOOTCAMP-SCOPE.md`, `PIPELINE-ARCHITECTURE.md`
**Produces:** `DATA-CONNECTION-STATUS.md`
**Hard gate:** Do not design ontology or build applications. Stay in data onboarding and raw-to-clean staging.
**Writes scope:** Connection config, raw datasets, and DATA-CONNECTION-STATUS.md
**Approval threshold:** Using production credentials; Agent deployment into customer networks; Accepting degraded data-readiness workarounds
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

#### `/pipeline-builder` — Pipeline Engineer
**Purpose:** Builds transforms, quality checks, and output datasets that back the ontology.
**Reads:** `DATA-CONNECTION-STATUS.md`, `PIPELINE-ARCHITECTURE.md`, `ONTOLOGY-ARCHITECTURE.md`
**Produces:** `PIPELINE-BUILD-STATUS.md`
**Hard gate:** Do not redesign architecture mid-build without surfacing the issue. Output only pipeline build status and associated transforms.
**Writes scope:** Transforms, output datasets, and PIPELINE-BUILD-STATUS.md
**Approval threshold:** Changing incremental strategy after initial lock; Accepting manual refresh as a production workaround
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

#### `/workshop-builder` — Workshop Application Developer
**Purpose:** Builds operational Workshop apps, wiring actions, variables, widgets, and flows.
**Reads:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-ARCHITECTURE.md`
**Produces:** `WORKSHOP-BUILD-STATUS.md`
**Hard gate:** Do not redesign the ontology. Build application surfaces against the locked architecture.
**Writes scope:** Workshop app configuration and WORKSHOP-BUILD-STATUS.md
**Approval threshold:** Publishing customer-facing app flows; Changing operational action bindings
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

#### `/aip-architect` — AIP Agent Designer
**Purpose:** Designs agent prompts, context scope, tools, evals, and Automate workflows.
**Reads:** `ONTOLOGY-ARCHITECTURE.md`, `WORKSHOP-BUILD-STATUS.md`
**Produces:** `AIP-AGENT-STATUS.md`
**Hard gate:** Do not expand the agent beyond the approved ontology and app scope.
**Writes scope:** Agent design, eval definitions, and AIP-AGENT-STATUS.md
**Approval threshold:** Adding write-capable tools; Expanding context scope across sensitive objects
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

#### `/osdk-developer` — OSDK Application Developer
**Purpose:** Builds custom applications against the Ontology SDK when Workshop is insufficient.
**Reads:** `ONTOLOGY-ARCHITECTURE.md`
**Produces:** `OSDK-BUILD-STATUS.md`
**Hard gate:** Do not widen the scope beyond the locked ontology and approved app need.
**Writes scope:** OSDK app assets and OSDK-BUILD-STATUS.md
**Approval threshold:** Adding new OAuth scopes; Choosing OSDK over Workshop for a primary use case
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

#### `/slate-builder` — Slate Application Developer
**Purpose:** Builds Slate apps for complex, pixel-precise, or deeply integrated user experiences.
**Reads:** `ONTOLOGY-ARCHITECTURE.md`
**Produces:** `SLATE-BUILD-STATUS.md`
**Hard gate:** Use Slate only when simpler app surfaces are not sufficient.
**Writes scope:** Slate app assets and SLATE-BUILD-STATUS.md
**Approval threshold:** Choosing Slate as the primary UX path; Introducing external integrations
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

### Review

#### `/foundry-reviewer` — Foundry Code Reviewer
**Purpose:** Performs structural audit of pipeline, ontology, app, and agent deliverables.
**Reads:** `PIPELINE-BUILD-STATUS.md`, `WORKSHOP-BUILD-STATUS.md`, `AIP-AGENT-STATUS.md`, `OSDK-BUILD-STATUS.md`, `SLATE-BUILD-STATUS.md`, `ONTOLOGY-ARCHITECTURE.md`
**Produces:** `REVIEW-REPORT.md`
**Hard gate:** Fix obvious issues first; escalate only genuinely ambiguous trade-offs.
**Writes scope:** REVIEW-REPORT.md and tightly scoped remediations
**Approval threshold:** Any fix that changes product scope or customer-facing behavior
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

#### `/foundry-security` — Foundry Security Officer
**Purpose:** Audits permissions, markings, agent scoping, OAuth scopes, data governance, and deployment security.
**Reads:** `ONTOLOGY-ARCHITECTURE.md`, `AIP-AGENT-STATUS.md`, `OSDK-BUILD-STATUS.md`, `PIPELINE-BUILD-STATUS.md`, `WORKSHOP-BUILD-STATUS.md`
**Produces:** `SECURITY-AUDIT.md`
**Hard gate:** Do not silently accept risky permission patterns. Capture exploit path and remediation for every real issue.
**Writes scope:** SECURITY-AUDIT.md only
**Approval threshold:** Risk acceptance on unresolved high or critical findings
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

### Test

#### `/foundry-qa` — AIP Evaluation Engineer
**Purpose:** Runs end-to-end QA, evals, and readiness scoring before deployment.
**Reads:** `REVIEW-REPORT.md`, `PIPELINE-BUILD-STATUS.md`, `WORKSHOP-BUILD-STATUS.md`, `AIP-AGENT-STATUS.md`, `SECURITY-AUDIT.md`
**Produces:** `QA-REPORT.md`
**Hard gate:** Do not greenlight deployment with a failing health score or missing critical test evidence.
**Writes scope:** QA-REPORT.md only
**Approval threshold:** Accepting a borderline health score or test gap
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

### Ship

#### `/apollo-deployer` — Apollo Deployment Engineer
**Purpose:** Manages release channels, deployment strategy, rollback, and post-deploy verification.
**Reads:** `QA-REPORT.md`, `SECURITY-AUDIT.md`
**Produces:** `DEPLOYMENT-PLAN.md`
**Hard gate:** Block deployment when health score is below threshold or critical security issues remain unresolved.
**Writes scope:** DEPLOYMENT-PLAN.md and deployment execution plan only
**Approval threshold:** Production deployment; Rollback execution; Release-channel policy changes
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

#### `/training-writer` — Customer Training Engineer
**Purpose:** Produces customer guides, runbooks, decks, and enablement materials from the built system.
**Reads:** `DEPLOYMENT-PLAN.md`, `QA-REPORT.md`, `SECURITY-AUDIT.md`, `ONTOLOGY-ARCHITECTURE.md`, `WORKSHOP-BUILD-STATUS.md`, `AIP-AGENT-STATUS.md`
**Produces:** `TRAINING-MATERIALS.md`
**Hard gate:** Do not invent unsupported workflows; training materials must match the actual delivered system.
**Writes scope:** TRAINING-MATERIALS.md only
**Approval threshold:** Any change to customer operating model or support promises
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

### Reflect

#### `/deployment-retro` — Deployment Retrospective
**Purpose:** Captures engagement metrics, friction points, lessons learned, and next-wave opportunities.
**Reads:** `BOOTCAMP-SCOPE.md`, `ONTOLOGY-ARCHITECTURE.md`, `REVIEW-REPORT.md`, `QA-REPORT.md`, `DEPLOYMENT-PLAN.md`, `TRAINING-MATERIALS.md`
**Produces:** `RETRO-REPORT.md`
**Hard gate:** Do not rewrite history; call out what actually happened and what would change next time.
**Writes scope:** RETRO-REPORT.md only
**Approval threshold:** Sharing sensitive customer lessons beyond the project team
**Allowed tools:** `Bash`, `Read`, `Write`, `Edit`, `AskUserQuestion`, `WebSearch`

### Safety

#### `/careful` — Careful Mode
**Purpose:** Requires explicit DS confirmation before destructive Foundry operations.
**Reads:** Customer brief / engagement context
**Produces:** Policy mode only
**Hard gate:** Never proceed with destructive operations without explicit confirmation.
**Writes scope:** No file artifact; policy mode only
**Approval threshold:** All destructive operations
**Allowed tools:** `Bash`, `Read`, `AskUserQuestion`

#### `/freeze` — Freeze Mode
**Purpose:** Restricts all modifications to an explicit project, use-case, or environment scope.
**Reads:** Customer brief / engagement context
**Produces:** Policy mode only
**Hard gate:** No out-of-scope modifications while freeze mode is active.
**Writes scope:** No file artifact; policy mode only
**Approval threshold:** Changing the frozen scope; Disabling freeze when work remains in customer environments
**Allowed tools:** `Bash`, `Read`, `AskUserQuestion`

#### `/guard` — Guard Mode
**Purpose:** Combines careful and freeze for maximum safety in production customer work.
**Reads:** Customer brief / engagement context
**Produces:** Policy mode only
**Hard gate:** Combine confirmation requirements with frozen-scope enforcement for all customer mutations.
**Writes scope:** No file artifact; policy mode only
**Approval threshold:** Changing or disabling safety posture in production environments
**Allowed tools:** `Bash`, `Read`, `AskUserQuestion`

## Artifact Registry

| Artifact | Phase | Owner | Template | Consumers |
|----------|-------|-------|----------|-----------|
| `BOOTCAMP-SCOPE.md` | discover | `/bootcamp` | `templates/BOOTCAMP-SCOPE.md` | `/ontology-vision`, `/pipeline-plan`, `/ontology-architect`, `/data-connector`, `/workshop-builder` |
| `ONTOLOGY-VISION.md` | vision | `/ontology-vision` | `templates/ONTOLOGY-VISION.md` | `/ontology-architect`, `/pipeline-plan` |
| `ONTOLOGY-ARCHITECTURE.md` | architecture | `/ontology-architect` | `templates/ONTOLOGY-ARCHITECTURE.md` | `/pipeline-builder`, `/workshop-builder`, `/aip-architect`, `/osdk-developer`, `/slate-builder`, `/foundry-security`, `/foundry-qa` |
| `PIPELINE-ARCHITECTURE.md` | architecture | `/pipeline-plan` | `templates/PIPELINE-ARCHITECTURE.md` | `/data-connector`, `/ontology-architect`, `/pipeline-builder` |
| `DATA-CONNECTION-STATUS.md` | build | `/data-connector` | `templates/DATA-CONNECTION-STATUS.md` | `/pipeline-builder` |
| `PIPELINE-BUILD-STATUS.md` | build | `/pipeline-builder` | `templates/PIPELINE-BUILD-STATUS.md` | `/foundry-reviewer`, `/foundry-qa` |
| `WORKSHOP-BUILD-STATUS.md` | build | `/workshop-builder` | `templates/WORKSHOP-BUILD-STATUS.md` | `/aip-architect`, `/foundry-reviewer`, `/foundry-qa` |
| `AIP-AGENT-STATUS.md` | build | `/aip-architect` | `templates/AIP-AGENT-STATUS.md` | `/foundry-reviewer`, `/foundry-security`, `/foundry-qa` |
| `OSDK-BUILD-STATUS.md` | build | `/osdk-developer` | `templates/OSDK-BUILD-STATUS.md` | `/foundry-reviewer`, `/foundry-security`, `/foundry-qa` |
| `SLATE-BUILD-STATUS.md` | build | `/slate-builder` | `templates/SLATE-BUILD-STATUS.md` | `/foundry-reviewer`, `/foundry-qa` |
| `REVIEW-REPORT.md` | review | `/foundry-reviewer` | `templates/REVIEW-REPORT.md` | `/foundry-qa`, `/deployment-retro` |
| `SECURITY-AUDIT.md` | review | `/foundry-security` | `templates/SECURITY-AUDIT.md` | `/apollo-deployer`, `/deployment-retro` |
| `QA-REPORT.md` | test | `/foundry-qa` | `templates/QA-REPORT.md` | `/apollo-deployer`, `/deployment-retro` |
| `DEPLOYMENT-PLAN.md` | ship | `/apollo-deployer` | `templates/DEPLOYMENT-PLAN.md` | `/training-writer`, `/deployment-retro` |
| `TRAINING-MATERIALS.md` | ship | `/training-writer` | `templates/TRAINING-MATERIALS.md` | `/deployment-retro` |
| `RETRO-REPORT.md` | reflect | `/deployment-retro` | `templates/RETRO-REPORT.md` | End of chain |

## Governance Matrix

| Skill | Governance tier | Approval threshold | Destructive boundary |
|-------|-----------------|--------------------|----------------------|
| `/bootcamp` | `human_decision_required` | Choosing the headline and quick-win use cases; Committing to customer-facing success metrics | None |
| `/ontology-vision` | `human_decision_required` | Selecting the ontology expansion mode; Deferring out-of-scope entities or interfaces | None |
| `/ontology-architect` | `human_decision_required` | Locking object boundaries, action scope, and writeback patterns | No production ontology mutation without /careful or explicit DS approval |
| `/pipeline-plan` | `human_decision_required` | Choosing batch vs incremental vs CDC; Picking Pipeline Builder vs Code Repositories | None |
| `/data-connector` | `guard_recommended` | Using production credentials; Agent deployment into customer networks; Accepting degraded data-readiness workarounds | Never store secrets in artifacts; Do not overwrite raw data with transformed output |
| `/pipeline-builder` | `guard_recommended` | Changing incremental strategy after initial lock; Accepting manual refresh as a production workaround | No deletion of production datasets without /careful |
| `/workshop-builder` | `guard_recommended` | Publishing customer-facing app flows; Changing operational action bindings | No deletion of published app pages without /careful |
| `/aip-architect` | `guard_recommended` | Adding write-capable tools; Expanding context scope across sensitive objects | No prompt or tool mutation on production agents without /careful |
| `/osdk-developer` | `guard_recommended` | Adding new OAuth scopes; Choosing OSDK over Workshop for a primary use case | No scope expansion without DS approval |
| `/slate-builder` | `guard_recommended` | Choosing Slate as the primary UX path; Introducing external integrations | No production app replacement without DS approval |
| `/foundry-reviewer` | `review_gate` | Any fix that changes product scope or customer-facing behavior | No broad refactors outside reviewed scope |
| `/foundry-security` | `security_gate` | Risk acceptance on unresolved high or critical findings | No permission changes without explicit DS approval |
| `/foundry-qa` | `quality_gate` | Accepting a borderline health score or test gap | None |
| `/apollo-deployer` | `deployment_gate` | Production deployment; Rollback execution; Release-channel policy changes | No production cutover without /careful or explicit DS approval |
| `/training-writer` | `customer_facing` | Any change to customer operating model or support promises | None |
| `/deployment-retro` | `internal_review` | Sharing sensitive customer lessons beyond the project team | None |
| `/careful` | `safety_mode` | All destructive operations | Ontology deletion; Pipeline deletion; Published app changes; Production agent mutation; Permission changes; Production deploy or rollback |
| `/freeze` | `safety_mode` | Changing the frozen scope; Disabling freeze when work remains in customer environments | Block edits outside the specified scope |
| `/guard` | `safety_mode` | Changing or disabling safety posture in production environments | All boundaries from careful plus all scope boundaries from freeze |

## Artifact Chain Summary

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
