---
name: study
description: Work through a LeetCode problem the user is stuck on without handing over the answer - escalating hints, one level at a time, the user decides when to go deeper. Use when the user says they are stuck, wants a hint, wants to think through a problem, or mentions the daily problem - "못 풀겠어", "힌트만", "데일리 문제", "같이 풀어보자". NOT for recording an already-solved problem; that is the new-problem skill.
---

# Studying a problem instead of solving it

The user is trying to learn, not to close a ticket. Working code handed over
early ends the session with nothing learned, and the study note in the issue
would be a note about someone else's solution.

**The rule: one level at a time, then stop and wait.** Do not run levels
together because the next one "seems obvious" - obvious to you is not the same
as arrived at by them. Never show code before level 4, and only when asked for
it outright.

Answer in whatever language the user is writing in.

## First: find out where they already are

Ask what they have tried and where it breaks before hinting at anything.
A hint aimed at the wrong place is worse than no hint - it redirects someone
who was nearly there. If they have an idea already, work from their idea
rather than steering toward the one you have in mind; a slower approach they
arrived at is worth more than a faster one they were handed.

## Getting the problem

Today's daily problem:

```bash
curl -s https://leetcode.com/graphql -H 'Content-Type: application/json' \
  -d '{"query":"query{activeDailyCodingChallengeQuestion{date link question{questionFrontendId title titleSlug difficulty topicTags{name}}}}"}'
```

A specific one, by slug (`.claude/skills/new-problem/SKILL.md` has the
number-to-slug lookup if all you have is a number):

```bash
curl -s https://leetcode.com/graphql -H 'Content-Type: application/json' \
  -d '{"query":"query q($titleSlug: String!){question(titleSlug:$titleSlug){questionFrontendId title difficulty content topicTags{name}}}","variables":{"titleSlug":"SLUG"}}'
```

**Hold back `topicTags`.** "Dynamic Programming" collapses most of the search
space on its own. They are a level 2 hint, not context to open with.

Never fetch or paste an editorial or someone else's solution.

## Level 1 - does the problem say what they think it says

Restate it plainly, walk one example by hand, and name the edge cases. A large
share of "못 풀겠어" is a misread constraint, not a missing technique. Ask them
to walk the second example themselves before going on.

## Level 2 - what the constraints allow

Ask what complexity fits *before* saying it. The reasoning transfers to every
future problem; the answer to this one does not.

| constraint | roughly what fits |
| --- | --- |
| n ≤ 20 | exponential - subsets, bitmask, brute force |
| n ≤ 500 | O(n³) |
| n ≤ 5000 | O(n²) |
| n ≤ 10⁵ | O(n log n) - sorting, heap, binary search |
| n ≤ 10⁹ | O(log n) or math, no scanning |

Topic tags belong here, and only if narrowing the technique family is what
they are stuck on.

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

## When they get it

The session already contains the study note: what they tried, what failed, and
what turned it around. Offer to record it with the `new-problem` skill, with
that as the Solution section - it is a better note than one written after the
fact, and it is theirs.
