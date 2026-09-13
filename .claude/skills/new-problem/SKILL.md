---
name: new-problem
description: Record a newly solved LeetCode problem in this repo - create the study issue, add the solution file, commit and push. Use when the user says they solved a problem and gives a LeetCode link and their code, or asks to "add a problem" / "문제 추가" / "새 문제 풀었어".
---

# Recording a solved problem

Every problem lives in two places: a solution file at the repo root and a study
issue. CI checks that they agree, and the README index is regenerated from the
issues. This skill walks the routine that keeps all of it consistent.

**Order matters: create the issue first, then the file.** `check_solutions.py`
treats a solution file with no matching issue as an error, so pushing the file
first makes CI fail.

## Input needed from the user

- the problem, as a LeetCode URL or just its number
- their solution code
- their notes: what the problem asks, and how they solved it

The notes are the point of this repo - they are the user's study record, so ask
for them rather than inventing them. Offer to draft from the code if the user
wants, but let the user own the final wording.

## The voice of a note

All 154 existing notes share a voice. A drafted note that does not match it
reads as written by someone else, which defeats the point of a study record.

- Plain declarative Korean - `~된다`, `~하면 된다`, `~한다`. Counted across the
  existing notes: 된다 142, 있다 61, 한다 31. Not polite form, not casual speech.
- One bolded sentence carrying the key idea, rarely more.
- State definitions go in a fenced block of their own: `dp[i][j] = ...`
- Short paragraphs, frequent line breaks. Most notes run 250-400 characters;
  a hard problem with several moving parts earns more, but not by much.

## What is worth recording, and what is not

About one note in six records a mistake, and every one of them is at the level
of **approach**, not of typing:

- "처음엔 투포인터로 하다가 2, 2, 1, 1 같은 케이스를 보고 dp로 풀었다" (#23)
- "처음엔 dfs로 구현해서 제출했는데 엣지 케이스 처리가 까다롭다. 결국 위상 정렬로 다시 제출" (#31)

Not one of them records a misnamed variable or an off-by-one. The test: will
this mistake happen again on a different problem? An approach abandoned for a
reason will. A typo will not - it is noise in a note meant to be reread.

## 1. Get the problem metadata

The lookup ships with the `study` skill in this repo's plugin. It takes the
problem however the user named it - a number, a slug, a URL, or `daily` - and
prints the four fields below as JSON:

```bash
python3 plugin/skills/study/scripts/problem.py 2265
```

| field | used as |
| --- | --- |
| `slug` | the filename, `<slug>.py` |
| `number` | the number in the issue title |
| `title` | the rest of the issue title |
| `difficulty` | the issue label, lowercased (`easy` / `medium` / `hard`) |

The issue title must be exactly `<number>. <title>` - `gen_index.py` parses the
leading number, and issues are paired to files by title, so a typo here drops
the problem out of the README.

## 2. Write the solution file

Take the user's code as-is and add only the import lines it needs. **Do not
reformat.** The issue holds the same code, and the sync check compares it line
by line - imports and comments are stripped from both sides, but a reflowed
line is a mismatch. Reformatting is what caused most of the drift this repo
had to clean up.

Common names and where they come from:

| name | import |
| --- | --- |
| `List`, `Optional` | `from typing import ...` |
| `Counter`, `defaultdict`, `deque` | `from collections import ...` |
| `cache`, `lru_cache` | `from functools import ...` |
| `heappush`, `heappop`, `heapify` | `from heapq import ...` |
| `heapq.*`, `random.*` | `import heapq` / `import random` |
| `inf`, `gcd`, `sqrt`, `comb` | `from math import ...` |
| `TreeNode`, `ListNode` | uncomment the stub LeetCode ships in the preamble |

Style: plain `import x` lines first, then `from x import y`, each group
alphabetical, two blank lines before the class.

Verify nothing is missing. pyflakes is not installed globally, so install it
into a throwaway directory (the session scratchpad is a good place):

```bash
python3 -m pip install --quiet --target "$DIR" pyflakes
PYTHONPATH="$DIR" python3 -m pyflakes <file>.py   # expect: no output
```

## 3. Create the issue

Use the template sections in `.github/ISSUE_TEMPLATE/problem.md`: Problem Link,
Problem Summary, Solution, Source Code. The Problem Link is the LeetCode URL.
The Source Code block is the same code, in a ```Python fence.

```bash
gh issue create --title "<number>. <title>" --label <difficulty> --body-file <draft>
```

When the user recorded several approaches, the repo's convention is a
`## Name (runtime)` heading per approach, each with its own code block - see
issues 86 and 138. The check passes if the file matches any one of the blocks.

## 4. Verify, then commit

```bash
GITHUB_TOKEN=$(gh auth token) python3 .github/scripts/check_solutions.py <file>.py
```

It must print `checked 1 solution(s): OK` before committing. Solution commits
here carry `Create <file>.py` as the subject and the issue number alone in the
body - 151 of the 155 existing ones do:

```bash
git add <file>.py
git commit -m "Create <file>.py" -m "#<issue number>"
git push origin master
```

The body is not decoration. GitHub links the `#number` and logs the commit in
that issue's timeline, and that is the only path from a solution file back to
the note explaining it - the README index only points the other way.

Two of the four commits missing it were written from this skill back when it
described the convention as the subject line only. Read `git log` with the body
before assuming a commit convention is just its subject.

## 5. What happens next on its own

- `check-solutions.yml` re-runs the same check on the pushed file
- `update-index.yml` regenerates the README table from the issues

Nothing else needs doing. If the README table does not pick the problem up,
the issue title is the first thing to check.
