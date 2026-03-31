#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import subprocess
from pathlib import Path

from evaluate_improvement import (
    ROOT,
    evaluate_proposal,
    load_conductor,
    proposal_target_files,
)
from replay_improvement_case import replay_proposal


def read_head_version(path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def read_worktree_version(path: str) -> str:
    file_path = ROOT / path
    return file_path.read_text() if file_path.exists() else ""


def diff_summary(path: str, baseline_text: str, candidate_text: str) -> dict:
    baseline_lines = baseline_text.splitlines()
    candidate_lines = candidate_text.splitlines()
    added = max(0, len(candidate_lines) - len(baseline_lines))
    diff_lines = list(
        difflib.unified_diff(
            baseline_lines,
            candidate_lines,
            fromfile=f"HEAD:{path}",
            tofile=path,
            lineterm="",
        )
    )
    additions = sum(1 for line in diff_lines if line.startswith("+") and not line.startswith("+++"))
    deletions = sum(1 for line in diff_lines if line.startswith("-") and not line.startswith("---"))
    return {
        "path": path,
        "changed": baseline_text != candidate_text,
        "additions": additions if diff_lines else added,
        "deletions": deletions if diff_lines else 0,
    }


def promotable(results: list[dict], changed_files: list[dict]) -> tuple[bool, list[str]]:
    issues = []
    if not any(file_result["changed"] for file_result in changed_files):
        issues.append("no proposal target files differ from HEAD")
    improved = False
    for result in results:
        if result["covered_targets"] == 0:
            issues.append(
                f"eval `{result['case_id']}` has no fixture targets overlapping the proposal target files"
            )
            continue
        if result["delta"] < 0:
            issues.append(f"regression against eval `{result['case_id']}`")
        if result["delta"] > 0:
            improved = True
    if not improved:
        issues.append("no eval case improved relative to HEAD")
    return (len(issues) == 0, issues)


def print_report(proposal_path: Path, eval_results: list[dict], changed_files: list[dict], issues: list[str]) -> None:
    print(f"proposal: {proposal_path.relative_to(ROOT)}")
    print("target file diff summary:")
    for file_result in changed_files:
        status = "changed" if file_result["changed"] else "unchanged"
        print(
            f"  - {file_result['path']}: {status}, +{file_result['additions']} / -{file_result['deletions']}"
        )
    print("benchmark comparison:")
    for result in eval_results:
        print(
            f"  - {result['case_id']}: baseline={result['baseline']['score']:.2f}, "
            f"candidate={result['candidate']['score']:.2f}, delta={result['delta']:+.2f}"
        )
        if result["covered_targets"] == 0:
            print(
                f"      * no fixture targets overlapped proposal scope "
                f"({result['available_targets']} available targets in case fixture)"
            )
            continue
        for baseline_target, candidate_target in zip(result["baseline"]["targets"], result["candidate"]["targets"]):
            for base_assertion, cand_assertion in zip(baseline_target["assertions"], candidate_target["assertions"]):
                if base_assertion["passed"] != cand_assertion["passed"]:
                    print(
                        f"      * {baseline_target['path']} :: {cand_assertion['id']} "
                        f"(HEAD={'pass' if base_assertion['passed'] else 'fail'}, "
                        f"candidate={'pass' if cand_assertion['passed'] else 'fail'})"
                    )
    if issues:
        print("promotion issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("promotion issues: none")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare HEAD vs working-tree proposal target files against required benchmark rubrics."
    )
    parser.add_argument("--proposal", type=Path, required=True, help="Proposal markdown file to evaluate")
    args = parser.parse_args()

    proposal_path = args.proposal if args.proposal.is_absolute() else ROOT / args.proposal
    _, proposal_issues, _ = evaluate_proposal(proposal_path, load_conductor())
    if proposal_issues:
        print(f"proposal: {proposal_path.relative_to(ROOT)}")
        print("proposal readiness issues:")
        for issue in proposal_issues:
            print(f"  - {issue}")
        return 1

    targets = proposal_target_files(proposal_path)
    changed_files = [
        diff_summary(path, read_head_version(path), read_worktree_version(path))
        for path in targets
    ]
    eval_results = replay_proposal(proposal_path)
    ok, issues = promotable(eval_results, changed_files)
    print_report(proposal_path, eval_results, changed_files, issues)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
