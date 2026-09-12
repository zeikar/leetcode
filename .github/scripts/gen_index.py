#!/usr/bin/env python3
"""Regenerate the problem table in README.md from the study issues."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import leetcode_repo as repo

README = "README.md"
# Must match the article route of the deployed issueage build.
SITE_ARTICLE = "https://zeikar.dev/leetcode/#/articles"
START = "<!-- PROBLEMS:START -->"
END = "<!-- PROBLEMS:END -->"
DIFFICULTIES = ("easy", "medium", "hard")


def difficulty(issue):
    names = {label["name"] for label in issue["labels"]}
    for name in DIFFICULTIES:
        if name in names:
            return name
    return ""


def render(paired):
    rows = []
    counts = dict.fromkeys(DIFFICULTIES, 0)
    for issue, path in paired:
        level = difficulty(issue)
        if level:
            counts[level] += 1
        name = os.path.basename(path)
        rows.append(
            (
                repo.problem_number(issue["title"]),
                "| {} | [{}]({}) | {} | [{}]({}) |".format(
                    repo.problem_number(issue["title"]),
                    repo.problem_title(issue["title"]),
                    f"{SITE_ARTICLE}/{issue['number']}",
                    level.capitalize() or "-",
                    name,
                    name,
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
    paired, orphan_issues, orphan_files = repo.pair_with_files(repo.load_issues())
    for issue in orphan_issues:
        print(f"::warning::issue #{issue['number']} '{issue['title']}' has no solution file")
    for path in orphan_files:
        print(f"::warning file={path}::no study issue found for this solution")
    for issue, _ in paired:
        if not difficulty(issue):
            print(f"::warning::issue #{issue['number']} '{issue['title']}' has no difficulty label")

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
