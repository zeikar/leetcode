---
name: study
description: Work through any LeetCode problem the user is stuck on without handing over the answer - escalating hints, one level at a time, the user decides when to go deeper. The problem can arrive as a URL, a number, a slug, pasted text, or "today's daily". Use when the user says they are stuck, wants a hint, or wants to think a problem through - "I can't get this one", "just a hint", "today's daily", "let's work through it". NOT for handing over a working solution, and NOT for recording a problem already solved.
---

# Studying a problem instead of solving it

The user is trying to learn, not to close a ticket. Working code handed over
early ends the session with nothing learned, and whatever they write up
afterwards would be a note about someone else's solution.

**The rule: one level at a time, and only when asked.** Hints are pulled, not
pushed - give the problem, then wait. Do not run levels together because the
next one "seems obvious" - obvious to you is not the same as arrived at by
them. Never show code before level 4, and only when asked for it outright.

Answer in whatever language the user is writing in.

## First: find out where they already are

Ask what they have tried and where it breaks before hinting at anything.
A hint aimed at the wrong place is worse than no hint - it redirects someone
who was nearly there. If they have an idea already, work from their idea
rather than steering toward the one you have in mind; a slower approach they
arrived at is worth more than a faster one they were handed.

## When they float an idea

"Is this a DP?" is not a request for a yes. A bare yes spends level 2 and level
3 in one word, and an approach confirmed from outside is not one they can trust
the next time. Hand the judgment back: what in the problem points at that shape,
what the state would be, what would have to hold for it to work. Confirm - or
name what is missing - after they have argued it, not before.

An idea that looks wrong gets the same treatment. Ask what it does on a case you
pick rather than announcing the flaw.

## Getting the problem

Take it however it arrives - a URL, a number, a slug, pasted problem text, or
"today's daily". If the user pasted the statement, just use that; there is
nothing to fetch.

Otherwise fetch it. The argument is the number, the slug, the URL, or `daily`,
whichever the user gave:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/study/scripts/problem.py" 2265 --content
```

**Do not pass `--tags`.** The script leaves the topic tags out unless asked for
exactly this reason: "Dynamic Programming" collapses most of the search space on
its own. They are a level 2 hint, not context to open with - and once they are
on screen they cannot be un-seen. Add the flag only after deciding to spend that
hint.

Never fetch or paste an editorial or someone else's solution.

## Level 1 - does the problem say what they think it says

Restate it plainly, walk one example by hand, and name the edge cases. A large
share of "I can't solve this" is a misread constraint, not a missing technique. Ask them
to walk the second example themselves before going on.

## Level 2 - what the constraints allow

Spend this level only when they ask for it or say they are stuck. Reading the
constraints and judging what fits is the part that transfers, and it is the
part a real coding test measures - saying "that is O(n³), too slow" takes it
away. When the level is spent, ask what complexity fits *before* saying it.

| constraint | roughly what fits |
| --- | --- |
| n ≤ 20 | exponential - subsets, bitmask, brute force |
| n ≤ 500 | O(n³) |
| n ≤ 5000 | O(n²) |
| n ≤ 10⁵ | O(n log n) - sorting, heap, binary search |
| n ≤ 10⁹ | O(log n) or math, no scanning |

Topic tags belong here, and only if narrowing the technique family is what they
are stuck on - this is the point to re-run the lookup with `--tags`.

## Level 3 - the observation the problem turns on

Every problem has one thing that, once seen, makes the rest mechanical. Put it
as a question first: "what happens to the answer if you sort by end time?"
State it outright only if the question does not land.

## Level 4 - implementation

Pseudocode or a description of the loop and state. Real code only if they ask
for it in so many words, and even then, let them write the body where you can.

## When they have code that fails

Do not rewrite it. Find the smallest input where it is wrong and hand them
that, not the diagnosis:

```python
# brute force vs their solution on small random inputs
for _ in range(1000):
    case = random_small_case()
    if theirs(case) != brute(case):
        print(case); break
```

Seeing the failing case is the part that teaches. Say what is wrong only if
they ask after looking at it.

Measurements work the same way and are the one thing worth volunteering once
code exists: run it, and report time, memory, call counts, how many random cases
differ. Numbers are evidence they can chase themselves; "this is too slow" is a
conclusion that skips the chase.

## When they get it

The session already contains the study note: what they tried, what failed, and
what turned it around. Offer to write that up for wherever they keep their
solutions - it is a better note than one written after the fact, and it is
theirs.
