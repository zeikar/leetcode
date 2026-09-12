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

Given only a number, look the slug up first - this listing carries every
problem, so it maps a number to its slug:

```bash
curl -s https://leetcode.com/api/problems/all/ -H 'User-Agent: Mozilla/5.0' \
  | python3 -c "import sys,json; print(next(p['stat']['question__title_slug'] for p in json.load(sys.stdin)['stat_status_pairs'] if str(p['stat']['frontend_question_id'])=='NUMBER'))"
```

Take only the slug from it and confirm the rest below - that listing reports
difficulty as a number and its titles can differ slightly from the canonical
ones.

Everything mechanical is derived from the slug:

```bash
curl -s https://leetcode.com/graphql -H 'Content-Type: application/json' \
  -d '{"query":"query q($titleSlug: String!){question(titleSlug:$titleSlug){questionFrontendId title titleSlug difficulty}}","variables":{"titleSlug":"SLUG"}}'
```

| field | used as |
| --- | --- |
| `titleSlug` | the filename, `<titleSlug>.py` |
| `questionFrontendId` | the number in the issue title |
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

It must print `checked 1 solution(s): OK` before committing. Then follow the
repo's convention for solution commits - `Create <file>.py` as the subject, and
the issue number alone in the body:

```bash
git add <file>.py
git commit -m "Create <file>.py" -m "#<issue number>"
git push origin master
```

The body is what gives a solution file a way back to its note. GitHub links the
`#number` and records the commit in that issue's timeline, so the file and the
note reach each other from both sides. Nothing else in the repo does this - the
README index only points issue to file.

## 5. What happens next on its own

- `check-solutions.yml` re-runs the same check on the pushed file
- `update-index.yml` regenerates the README table from the issues

Nothing else needs doing. If the README table does not pick the problem up,
the issue title is the first thing to check.
