#!/usr/bin/env python3
"""Check that each solution file still matches the code block in its study note.

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


def check_matches_note(path, note):
    with open(path, encoding="utf-8") as handle:
        code = repo.solution_code(handle.read())
    blocks = repo.code_blocks(note["body"])
    if not blocks:
        annotate(path, f"discussion #{note['number']} has no ```Python block")
        return False
    if code not in [repo.solution_code(block) for block in blocks]:
        annotate(
            path,
            f"does not match any code block in discussion #{note['number']} "
            f"({note['html_url']}) - update whichever side is stale",
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

    paired, _, orphan_files = repo.pair_with_files(repo.load_notes())
    selected = [
        (note, path)
        for note, path in paired
        if check_all or os.path.basename(path) in requested
    ]

    ok = True
    for note, path in selected:
        ok &= check_matches_note(path, note)

    for path in orphan_files:
        if check_all or os.path.basename(path) in requested:
            annotate(path, "no study note found for this solution")
            ok = False

    print(f"checked {len(selected)} solution(s): {'OK' if ok else 'FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
