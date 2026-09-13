# leetcode-study

### Study LeetCode with Claude Code — instead of having it solved for you.

[![Claude Code plugin](https://img.shields.io/badge/Claude_Code-plugin-d97757)](https://docs.claude.com/en/docs/claude-code/plugins)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](../LICENSE)

Every AI coding tool is built to finish the problem for you. That is the one
thing you do not want when the problem *is* the point.

This plugin makes Claude **give one hint level at a time, then stop and wait.**
You decide when to go deeper. The solution stays yours.

## A real session

LeetCode 835, after a brute force timed out:

```
you      I need to reduce the reallocation.

claude   Right instinct — but a step further: the board is not needed at all.
         Per shift you zero 7921 cells; the overlap you actually compare
         averages ~100. 98% of the run writes zeroes you never read.

you      [rewrites it — still wrong]

claude   img1 = [[1, 1],   img2 = [[1, 0],     yours = 3
                 [0, 1]]           [1, 1]]   correct = 2

         Your answer came out larger than possible.

you      ...the sign on the lower bound. Python read img1[-1] and said nothing.
```

Where another tool pastes a corrected function, this one prints a 2×2 grid —
brute-forced against your own submission, so it is the real minimal case. The
bug stays yours to find.

## The levels

| | |
| --- | --- |
| **0** | What have you tried? Nothing is given before this is answered. |
| **1** | Does the problem say what you think it says? |
| **2** | What do the constraints allow? `n ≤ 20` is exponential, `n ≤ 10⁵` is `O(n log n)`. |
| **3** | The one observation the rest turns on — put as a question first. |
| **4** | Implementation. Pseudocode before code. |

**Topic tags live at level 2 and are held back until then.** "Dynamic
Programming" collapses most of the search space on its own, so the lookup omits
them unless `--tags` is passed — once seen, they cannot be un-seen.

## Install

```
/plugin marketplace add zeikar/leetcode
/plugin install leetcode-study@leetcode-study
```

Working inside a clone of this repo needs neither command — `.claude/settings.json`
registers the plugin from source, so a new session picks it up on its own.

Then say you are stuck: "I can't get 3414", "just a hint", "today's daily", or a
bare problem number — `scripts/problem.py` resolves any of those in one request.
Claude answers in whatever language you write in.

It will not fetch an editorial, paste someone else's solution, or show code
before level 4. Ask for the answer outright and it will give it; the point is
that it does not lead with it.
