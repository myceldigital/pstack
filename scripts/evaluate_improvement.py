#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONDUCTOR_PATH = ROOT / 'conductor.json'
REQUIRED_PROPOSAL_SECTIONS = [
    '## Problem',
    '## Target Files',
    '## Proposed Change',
    '## Expected Benefit',
    '## Required Evals',
    '## Promotion Gate',
]


def load_conductor() -> dict:
    return json.loads(CONDUCTOR_PATH.read_text())


def resolve_repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else ROOT / candidate


def parse_target_bullets(section_text: str) -> list[str]:
    return [match.strip('` ') for match in re.findall(r'^-\s+`?([^`\n]+)`?$', section_text, flags=re.MULTILINE)]


def split_sections(markdown: str) -> dict[str, str]:
    parts = re.split(r'(^## .+$)', markdown, flags=re.MULTILINE)
    sections: dict[str, str] = {}
    current = None
    for part in parts:
        if part.startswith('## '):
            current = part.strip()
            sections[current] = ''
        elif current:
            sections[current] += part
    return sections


def load_proposal_sections(path: Path) -> dict[str, str]:
    return split_sections(path.read_text())


def canonical_targets(conductor: dict) -> set[str]:
    targets = {
        'PROGRAM.md',
        'README.md',
        'conductor.json',
        'docs/skills.md',
        'evals/ARTIFACT-RUBRICS.md',
        'evals/SKILL-SCORECARD.md',
    }
    targets.update(skill['path'] for skill in conductor['skills'])
    targets.update(artifact['template_path'] for artifact in conductor['artifacts'])
    return targets


def eval_case_ids(conductor: dict) -> set[str]:
    return {case['id'] for case in conductor['eval_cases']}


def recommend_evals(target_files: list[str], conductor: dict) -> list[str]:
    related = set()
    all_cases = {case['id'] for case in conductor['eval_cases']}
    all_targets = set(target_files)
    if {'PROGRAM.md', 'README.md', 'conductor.json', 'docs/skills.md'} & all_targets:
        related.update(all_cases)
    for case in conductor['eval_cases']:
        for skill_id in case['target_skills']:
            skill = next((item for item in conductor['skills'] if item['id'] == skill_id), None)
            if not skill:
                continue
            if skill['path'] in all_targets:
                related.add(case['id'])
                continue
            for artifact_id in skill['produces_artifacts']:
                artifact = next((item for item in conductor['artifacts'] if item['id'] == artifact_id), None)
                if artifact and artifact['template_path'] in all_targets:
                    related.add(case['id'])
    return sorted(related)


def validate_episode(path: Path) -> list[str]:
    errors = []
    try:
        payload = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        return [f'{path}: invalid json ({exc})']
    for key in ['engagement_id', 'industry', 'headliner_use_case', 'artifacts_reviewed', 'worked', 'failed', 'reusable_lessons']:
        if key not in payload:
            errors.append(f'{path}: missing key `{key}`')
    for idx, lesson in enumerate(payload.get('reusable_lessons', []), start=1):
        for key in ['type', 'target', 'change', 'evidence']:
            if key not in lesson:
                errors.append(f'{path}: lesson {idx} missing `{key}`')
    return errors


def evaluate_proposal(path: Path, conductor: dict) -> tuple[int, list[str], list[str]]:
    sections = load_proposal_sections(path)
    issues: list[str] = []
    score = 0
    for section in REQUIRED_PROPOSAL_SECTIONS:
        if section in sections and sections[section].strip():
            score += 1
        else:
            issues.append(f'missing or empty section: {section}')

    targets = parse_target_bullets(sections.get('## Target Files', ''))
    valid_targets = canonical_targets(conductor)
    for target in targets:
        if target not in valid_targets:
            issues.append(f'unknown target file: {target}')

    required_evals = parse_target_bullets(sections.get('## Required Evals', ''))
    known_eval_ids = eval_case_ids(conductor)
    for eval_id in required_evals:
        if eval_id not in known_eval_ids:
            issues.append(f'unknown eval case: {eval_id}')

    recommended = recommend_evals(targets, conductor)
    return score, issues, recommended


def proposal_target_files(path: Path) -> list[str]:
    return parse_target_bullets(load_proposal_sections(path).get('## Target Files', ''))


def proposal_required_evals(path: Path) -> list[str]:
    return parse_target_bullets(load_proposal_sections(path).get('## Required Evals', ''))


def summary(conductor: dict) -> int:
    episode_dir = ROOT / conductor['memory']['episode_dir']
    proposal_dir = ROOT / conductor['memory']['proposal_dir']
    episode_files = sorted(episode_dir.glob('*.json'))
    proposal_files = sorted(path for path in proposal_dir.glob('*.md') if path.name != 'README.md')

    episode_errors: list[str] = []
    for episode in episode_files:
        episode_errors.extend(validate_episode(episode))

    print(f'memory episodes: {len(episode_files)}')
    print(f'improvement proposals: {len(proposal_files)}')
    if episode_errors:
        print('episode validation errors:')
        for error in episode_errors:
            print(f'- {error}')
    else:
        print('episode validation: ok')

    for proposal in proposal_files:
        score, issues, recommended = evaluate_proposal(proposal, conductor)
        print(f'proposal: {proposal.relative_to(ROOT)}')
        print(f'  readiness score: {score}/{len(REQUIRED_PROPOSAL_SECTIONS)}')
        print(f'  recommended evals: {", ".join(recommended) if recommended else "none"}')
        if issues:
            for issue in issues:
                print(f'  issue: {issue}')
    return 1 if episode_errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description='Evaluate pstack improvement-memory readiness.')
    parser.add_argument('--proposal', type=Path, help='Evaluate a single proposal file relative to the repo root or as an absolute path.')
    args = parser.parse_args()

    conductor = load_conductor()
    if args.proposal:
        proposal_path = args.proposal if args.proposal.is_absolute() else ROOT / args.proposal
        score, issues, recommended = evaluate_proposal(proposal_path, conductor)
        print(f'proposal: {proposal_path.relative_to(ROOT)}')
        print(f'readiness score: {score}/{len(REQUIRED_PROPOSAL_SECTIONS)}')
        print(f'recommended evals: {", ".join(recommended) if recommended else "none"}')
        if issues:
            print('issues:')
            for issue in issues:
                print(f'- {issue}')
            return 1
        return 0
    return summary(conductor)


if __name__ == '__main__':
    raise SystemExit(main())
