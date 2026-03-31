#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONDUCTOR_PATH = ROOT / "conductor.json"
README_PATH = ROOT / "README.md"
SKILLS_DOC_PATH = ROOT / "docs" / "skills.md"


def load_conductor() -> dict:
    return json.loads(CONDUCTOR_PATH.read_text())


def artifact_lookup(conductor: dict) -> dict[str, dict]:
    return {artifact["id"]: artifact for artifact in conductor["artifacts"]}


def skill_lookup(conductor: dict) -> dict[str, dict]:
    return {skill["id"]: skill for skill in conductor["skills"]}


def phase_lookup(conductor: dict) -> dict[str, dict]:
    return {phase["id"]: phase for phase in conductor["phases"]}


def artifacts_to_files(artifact_ids: list[str], artifacts: dict[str, dict]) -> str:
    if not artifact_ids:
        return "Customer brief / engagement context"
    return ", ".join(f"`{artifacts[artifact_id]['filename']}`" for artifact_id in artifact_ids)


def render_skill_tables(conductor: dict) -> str:
    phases = phase_lookup(conductor)
    artifacts = artifact_lookup(conductor)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in conductor["skills"]:
        grouped[skill["phase"]].append(skill)

    ordered_phases = [phase["id"] for phase in conductor["phases"]]
    lines: list[str] = []
    for phase_id in ordered_phases:
        skills = grouped.get(phase_id)
        if not skills:
            continue
        lines.append(f"### {phases[phase_id]['label']}")
        lines.append("")
        lines.append("| Skill | Purpose | Reads | Produces |")
        lines.append("|-------|---------|-------|----------|")
        for skill in skills:
            produces = (
                ", ".join(f"`{artifacts[artifact_id]['filename']}`" for artifact_id in skill["produces_artifacts"])
                if skill["produces_artifacts"]
                else "Policy mode"
            )
            lines.append(
                f"| `{skill['invoke']}` | {skill['summary']} | "
                f"{artifacts_to_files(skill['reads_artifacts'], artifacts)} | {produces} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip()


def render_sprint_sequence(conductor: dict) -> str:
    phases = phase_lookup(conductor)
    artifacts = artifact_lookup(conductor)
    rows: list[str] = [
        "| Phase | Goal | Primary skills | Primary artifacts |",
        "|-------|------|----------------|-------------------|",
    ]
    for phase in conductor["phases"]:
        phase_skills = [skill for skill in conductor["skills"] if skill["phase"] == phase["id"] and skill["type"] != "safety"]
        if not phase_skills:
            continue
        primary_skills = ", ".join(f"`{skill['invoke']}`" for skill in phase_skills)
        artifact_ids = []
        for skill in phase_skills:
            artifact_ids.extend(skill["produces_artifacts"])
        artifact_list = ", ".join(f"`{artifacts[artifact_id]['filename']}`" for artifact_id in artifact_ids) or "None"
        rows.append(f"| {phases[phase['id']]['label']} | {phase['goal']} | {primary_skills} | {artifact_list} |")
    return "\n".join(rows)


def render_artifact_chain(conductor: dict) -> str:
    artifacts = artifact_lookup(conductor)
    lines = ["```text"]
    for artifact in conductor["artifacts"]:
        consumer_names = [f"/{consumer}" if not consumer.startswith("/") else consumer for consumer in artifact["consumers"]]
        consumer_text = ", ".join(consumer_names) if consumer_names else "end of chain"
        lines.append(f"{artifact['filename']} -> {consumer_text}")
    lines.append("```")
    return "\n".join(lines)


def render_governance_summary(conductor: dict) -> str:
    rows = [
        "| Skill | Governance tier | Approval threshold | Destructive boundary |",
        "|-------|-----------------|--------------------|----------------------|",
    ]
    for skill in conductor["skills"]:
        approvals = "; ".join(skill["approval_required_for"]) if skill["approval_required_for"] else "None"
        boundaries = "; ".join(skill["destructive_boundaries"]) if skill["destructive_boundaries"] else "None"
        rows.append(
            f"| `{skill['invoke']}` | `{skill['governance_tier']}` | {approvals} | {boundaries} |"
        )
    return "\n".join(rows)


def render_readme(conductor: dict) -> str:
    quick_start = "\n".join(conductor["install"]["quick_start"])
    operator_skills = render_skill_tables(conductor)
    sprint_sequence = render_sprint_sequence(conductor)
    return f"""# {conductor['display_name']} — Palantir Deployment Strategist AI Team

**{conductor['tagline']}**

`pstack` is an operator-grade repository of AI skills for Palantir deployments. It is built for deployment strategists who need an execution contract, not a loose collection of prompts: phase gates, artifact handoffs, governance boundaries, examples, and evals all live in one repo.

## What This Is

`pstack` turns one deployment strategist into a conductor for discovery, ontology, data, application, QA, security, deployment, and retrospective work. The repo is organized around a strict artifact chain so downstream skills consume stable documents rather than improvising off chat history.

## Who This Is For

{chr(10).join(f"- {item}" for item in conductor['audience']['for'])}

## Who This Is Not For

{chr(10).join(f"- {item}" for item in conductor['audience']['not_for'])}

## First Hour

1. Clone the repo and run `{conductor['install']['script']}`.
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
git clone {conductor['repo_url']}.git
cd {conductor['name']}
./install.sh

# Start with structured discovery
{quick_start}
```

## Skills

The skill inventory below is generated from `conductor.json`.

{operator_skills}

## Sprint Sequence

{sprint_sequence}

## Artifact Chain

Every named artifact below has a template in `templates/`, rubric coverage in `evals/ARTIFACT-RUBRICS.md`, and live examples under `examples/engagements/`.

{render_artifact_chain(conductor)}

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
"""


def render_skills_doc(conductor: dict) -> str:
    artifacts = artifact_lookup(conductor)
    skills_by_phase: dict[str, list[dict]] = defaultdict(list)
    for skill in conductor["skills"]:
        skills_by_phase[skill["phase"]].append(skill)

    sections: list[str] = [
        "# pstack Skills Reference",
        "",
        "_This document is generated from `conductor.json`._",
        "",
        "## Skill Index by Phase",
        "",
    ]
    for phase in conductor["phases"]:
        skills = skills_by_phase.get(phase["id"])
        if not skills:
            continue
        sections.append(f"### {phase['label']}")
        sections.append("")
        for skill in skills:
            sections.append(f"#### `{skill['invoke']}` — {skill['title']}")
            sections.append(f"**Purpose:** {skill['summary']}")
            sections.append(f"**Reads:** {artifacts_to_files(skill['reads_artifacts'], artifacts)}")
            produces = ", ".join(f"`{artifacts[artifact_id]['filename']}`" for artifact_id in skill["produces_artifacts"]) or "Policy mode only"
            sections.append(f"**Produces:** {produces}")
            sections.append(f"**Hard gate:** {skill['hard_gate']}")
            sections.append(f"**Writes scope:** {skill['writes_scope']}")
            sections.append(f"**Approval threshold:** {'; '.join(skill['approval_required_for']) if skill['approval_required_for'] else 'None'}")
            sections.append(f"**Allowed tools:** {', '.join(f'`{tool}`' for tool in skill['allowed_tools'])}")
            sections.append("")

    sections.extend(
        [
            "## Artifact Registry",
            "",
            "| Artifact | Phase | Owner | Template | Consumers |",
            "|----------|-------|-------|----------|-----------|",
        ]
    )
    skills = skill_lookup(conductor)
    for artifact in conductor["artifacts"]:
        owner = skills[artifact["owner_skill"]]["invoke"]
        consumers = ", ".join(f"`/{consumer}`" if not consumer.startswith("/") else f"`{consumer}`" for consumer in artifact["consumers"]) or "End of chain"
        sections.append(
            f"| `{artifact['filename']}` | {artifact['phase']} | `{owner}` | `{artifact['template_path']}` | {consumers} |"
        )

    sections.extend(
        [
            "",
            "## Governance Matrix",
            "",
            render_governance_summary(conductor),
            "",
            "## Artifact Chain Summary",
            "",
            render_artifact_chain(conductor),
            "",
        ]
    )
    return "\n".join(sections)


def main() -> None:
    conductor = load_conductor()
    README_PATH.write_text(render_readme(conductor))
    SKILLS_DOC_PATH.write_text(render_skills_doc(conductor))


if __name__ == "__main__":
    main()
