# leetcode-study — Claude Code plugin

Work through a LeetCode problem with Claude **without being handed the answer.**

```
"I can't get 3414"
   → what did you try?  → what do the constraints allow?
   → the observation it turns on, as a question  → pseudocode
   → your code, your solution
```

Ask any LLM for a LeetCode problem and the default is a finished solution. That
is the fastest way to close the tab having learned nothing. This plugin makes
Claude give **one hint level at a time and then stop and wait** — the user
decides when to go deeper.

## The levels

| | |
| --- | --- |
| **0** | What have you tried? Nothing is given before this is answered. |
| **1** | Does the problem say what you think it says? Restate it, walk one example by hand. |
| **2** | What do the constraints allow? `n ≤ 20` is exponential, `n ≤ 10⁵` is `O(n log n)`. Topic tags belong here, and only here. |
| **3** | The one observation the rest turns on — put as a question first. |
| **4** | Implementation. Pseudocode before code. |

Two rules do most of the work:

**Topic tags are held back.** "Dynamic Programming" collapses most of the search
space on its own, so the lookup omits them unless `--tags` is passed. It is a
level 2 hint, not context to open with — and once seen it cannot be un-seen.

**A wrong answer gets a counterexample, not a rewrite.** Rewriting someone's
code ends the session; finding the smallest input where it breaks does not. For
a wrong submission on 835 that meant:

```
img1 = [[1, 1],     img2 = [[1, 0],       yours = 3
        [0, 1]]             [1, 1]]     correct = 2
```

Two lines of output, and the bug — a flipped sign that Python's negative
indexing had swallowed silently — was theirs to find.

## What's in it

| Component | What it does |
| --- | --- |
| **`study`** (skill) | The escalating-hint session. Answers in whatever language the user writes in. |
| **`scripts/problem.py`** | Resolves a problem from a number, a slug, a URL, or `daily`, in one request. `--content` for the statement, `--tags` to spend the tag hint. |

## Install

```
/plugin marketplace add zeikar/leetcode
/plugin install leetcode-study@leetcode-study
```

Then say you are stuck. "I can't get 3414", "just a hint", "today's daily", a
bare problem number — any of them start a session.

## What it will not do

Fetch an editorial, paste someone else's solution, or show code before level 4.
Ask for the answer outright and it will give it — the point is that it does not
lead with it.
