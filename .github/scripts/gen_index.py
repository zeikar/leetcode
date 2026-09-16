#!/usr/bin/env python3
"""Regenerate the problem table in README.md from the study notes."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leetcode_repo as repo

README = "README.md"
# Must match the post route of the deployed Repozine build.
SITE_ARTICLE = "https://zeikar.dev/leetcode/posts"
START = "<!-- PROBLEMS:START -->"
END = "<!-- PROBLEMS:END -->"
DIFFICULTIES = ("easy", "medium", "hard")


def difficulty(note):
    names = {label["name"] for label in note["labels"]}
    for name in DIFFICULTIES:
        if name in names:
            return name
    return ""


def render(paired):
    rows = []
    counts = dict.fromkeys(DIFFICULTIES, 0)
    for note, path in paired:
        level = difficulty(note)
        if level:
            counts[level] += 1
        name = os.path.basename(path)
        rows.append(
            (
                repo.problem_number(note["title"]),
                "| {} | [{}]({}) | {} | [{}]({}) |".format(
                    repo.problem_number(note["title"]),
                    repo.problem_title(note["title"]),
                    f"{SITE_ARTICLE}/{note['number']}/",
                    level.capitalize() or "-",
                    name,
                    os.path.relpath(path),
                ),
            )
        )
    rows.sort(key=lambda row: row[0])
    summary = "**{} solved** — Easy {} · Medium {} · Hard {}".format(
        len(rows), counts["easy"], counts["medium"], counts["hard"]
    )
    return "\n".join(
        [summary, "", "| # | Problem | Difficulty | Solution |", "| ---: | --- | --- | --- |"]
        + [row for _, row in rows]
    )


def main():
    paired, orphan_notes, orphan_files = repo.pair_with_files(repo.load_notes())
    for note in orphan_notes:
        print(f"::warning::discussion #{note['number']} '{note['title']}' has no solution file")
    for path in orphan_files:
        print(f"::warning file={path}::no study note found for this solution")
    for note, _ in paired:
        if not difficulty(note):
            print(f"::warning::discussion #{note['number']} '{note['title']}' has no difficulty label")

    with open(README, encoding="utf-8") as handle:
        readme = handle.read()
    if START not in readme or END not in readme:
        raise SystemExit(f"{README} is missing the {START} / {END} markers")

    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    updated = f"{head}{START}\n\n{render(paired)}\n\n{END}{tail}"

    if updated == readme:
        print("index unchanged")
        return
    with open(README, "w", encoding="utf-8") as handle:
        handle.write(updated)
    print(f"index updated: {len(paired)} problems")


if __name__ == "__main__":
    main()
