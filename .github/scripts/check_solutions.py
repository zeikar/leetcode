#!/usr/bin/env python3
"""Check that each solution file still matches the code block in its study issue.

Usage: check_solutions.py [--all | FILE ...]

Given no arguments it checks nothing, so a workflow can pass it the files a push
touched without special-casing an empty list.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leetcode_repo as repo

def annotate(path, message, line=None):
    where = f"file={path}" + (f",line={line}" if line else "")
    print(f"::error {where}::{message}")


def check_matches_issue(path, issue):
    with open(path, encoding="utf-8") as handle:
        code = repo.solution_code(handle.read())
    blocks = repo.code_blocks(issue["body"])
    if not blocks:
        annotate(path, f"issue #{issue['number']} has no ```Python block")
        return False
    if code not in [repo.solution_code(block) for block in blocks]:
        annotate(
            path,
            f"does not match any code block in issue #{issue['number']} "
            f"({issue['html_url']}) - update whichever side is stale",
        )
        return False
    return True


def main():
    args = sys.argv[1:]
    check_all = "--all" in args
    requested = {os.path.basename(arg) for arg in args if arg.endswith(".py")}
    if not check_all and not requested:
        print("no solution files to check")
        return 0

    paired, _, orphan_files = repo.pair_with_files(repo.load_issues())
    selected = [
        (issue, path)
        for issue, path in paired
        if check_all or os.path.basename(path) in requested
    ]

    ok = True
    for issue, path in selected:
        ok &= check_matches_issue(path, issue)

    for path in orphan_files:
        if check_all or os.path.basename(path) in requested:
            annotate(path, "no study issue found for this solution")
            ok = False

    print(f"checked {len(selected)} solution(s): {'OK' if ok else 'FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
