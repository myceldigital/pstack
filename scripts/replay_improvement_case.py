#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from evaluate_improvement import (
    ROOT,
    evaluate_proposal,
    load_conductor,
    proposal_required_evals,
    proposal_target_files,
)

SUPPORTED_ASSERTIONS = {'contains', 'not_contains', 'regex'}


def resolve_case_dir(case_id: str) -> Path:
    return ROOT / 'evals' / 'cases' / case_id


def fixture_path(case_id: str) -> Path:
    return resolve_case_dir(case_id) / 'fixture.json'


def load_fixture(case_id: str) -> dict:
    path = fixture_path(case_id)
    if not path.exists():
        raise FileNotFoundError(f'missing fixture: {path}')
    return json.loads(path.read_text())


def scoped_fixture(fixture: dict, allowed_paths: set[str] | None) -> tuple[dict, int]:
    if not allowed_paths:
        return fixture, len(fixture['targets'])
    filtered_targets = [target for target in fixture['targets'] if target['path'] in allowed_paths]
    return ({**fixture, 'targets': filtered_targets}, len(filtered_targets))


def read_head_text(path: str) -> str:
    result = subprocess.run(
        ['git', 'show', f'HEAD:{path}'],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout if result.returncode == 0 else ''


def read_worktree_text(path: str) -> str:
    file_path = ROOT / path
    return file_path.read_text() if file_path.exists() else ''


def assertion_passes(text: str, assertion: dict) -> bool:
    kind = assertion['type']
    value = assertion['value']
    if kind == 'contains':
        return value in text
    if kind == 'not_contains':
        return value not in text
    if kind == 'regex':
        import re
        return re.search(value, text, flags=re.MULTILINE) is not None
    raise ValueError(f'unsupported assertion type: {kind}')


def evaluate_fixture_text(text: str, fixture: dict) -> dict:
    total_weight = 0.0
    passed_weight = 0.0
    target_results = []
    for target in fixture['targets']:
        target_path = target['path']
        target_text = text[target_path]
        assertions = []
        for assertion in target['assertions']:
            if assertion['type'] not in SUPPORTED_ASSERTIONS:
                raise ValueError(f"unsupported assertion type: {assertion['type']}")
            weight = float(assertion.get('weight', 1))
            passed = assertion_passes(target_text, assertion)
            total_weight += weight
            passed_weight += weight if passed else 0.0
            assertions.append({
                'id': assertion['id'],
                'type': assertion['type'],
                'value': assertion['value'],
                'weight': weight,
                'passed': passed,
            })
        target_results.append({'path': target_path, 'assertions': assertions})
    score = (passed_weight / total_weight) if total_weight else 0.0
    return {'score': score, 'targets': target_results}


def replay_case(case_id: str, allowed_paths: set[str] | None = None) -> dict:
    fixture, covered_targets = scoped_fixture(load_fixture(case_id), allowed_paths)
    baseline_text = {target['path']: read_head_text(target['path']) for target in fixture['targets']}
    candidate_text = {target['path']: read_worktree_text(target['path']) for target in fixture['targets']}
    baseline = evaluate_fixture_text(baseline_text, fixture)
    candidate = evaluate_fixture_text(candidate_text, fixture)
    return {
        'case_id': case_id,
        'covered_targets': covered_targets,
        'available_targets': len(load_fixture(case_id)['targets']),
        'baseline': baseline,
        'candidate': candidate,
        'delta': candidate['score'] - baseline['score'],
    }


def replay_proposal(proposal_path: Path) -> list[dict]:
    conductor = load_conductor()
    proposal = proposal_path if proposal_path.is_absolute() else ROOT / proposal_path
    _, issues, _ = evaluate_proposal(proposal, conductor)
    if issues:
        raise ValueError('; '.join(issues))
    allowed_paths = set(proposal_target_files(proposal))
    return [replay_case(case_id, allowed_paths=allowed_paths) for case_id in proposal_required_evals(proposal)]


def print_result(result: dict) -> None:
    print(f"case: {result['case_id']}")
    print(
        f"  baseline={result['baseline']['score']:.2f}, "
        f"candidate={result['candidate']['score']:.2f}, delta={result['delta']:+.2f}"
    )
    if result['covered_targets'] == 0:
        print(
            f"  no fixture targets overlapped the proposal scope "
            f"({result['available_targets']} available targets in case fixture)"
        )
        return
    for baseline_target, candidate_target in zip(result['baseline']['targets'], result['candidate']['targets']):
        print(f"  target: {baseline_target['path']}")
        for base_assertion, cand_assertion in zip(baseline_target['assertions'], candidate_target['assertions']):
            if base_assertion['passed'] != cand_assertion['passed']:
                print(
                    f"    - {cand_assertion['id']}: "
                    f"HEAD={'pass' if base_assertion['passed'] else 'fail'} -> "
                    f"candidate={'pass' if cand_assertion['passed'] else 'fail'}"
                )


def main() -> int:
    parser = argparse.ArgumentParser(description='Replay structured improvement fixtures against HEAD and working tree.')
    parser.add_argument('--case', help='Replay a single eval case by id.')
    parser.add_argument('--proposal', type=Path, help='Replay all required eval cases for a proposal.')
    args = parser.parse_args()

    if bool(args.case) == bool(args.proposal):
        parser.error('provide exactly one of --case or --proposal')

    results = [replay_case(args.case)] if args.case else replay_proposal(args.proposal)
    for result in results:
        print_result(result)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
