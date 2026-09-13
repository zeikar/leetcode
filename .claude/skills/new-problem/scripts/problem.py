#!/usr/bin/env python3
"""Look up a LeetCode problem, however the user named it.

    problem.py 2265                 number
    problem.py two-sum              slug
    problem.py https://leetcode.com/problems/two-sum/
    problem.py daily                today's daily challenge

Prints JSON: number, title, slug, difficulty. The issue title, the filename and
the difficulty label all come from here, so a typo cannot creep in by hand.
"""
import json
import re
import sys
import urllib.error
import urllib.request

GRAPHQL = "https://leetcode.com/graphql"

BY_SLUG = """
query($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId title titleSlug difficulty %s
  }
}
"""

# The number is not a queryable field, so this searches and the caller picks the
# exact id out of the results - a short number such as "1" also matches 191,
# 1139 and so on.
BY_NUMBER = """
query($filters: QuestionListFilterInput) {
  questionList(categorySlug: "", limit: 20, filters: $filters) {
    data { questionFrontendId title titleSlug difficulty }
  }
}
"""

DAILY = """
query {
  activeDailyCodingChallengeQuestion {
    question { questionFrontendId title titleSlug difficulty }
  }
}
"""


def graphql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        GRAPHQL,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            payload = json.load(resp)
    except urllib.error.URLError as exc:
        sys.exit(f"leetcode.com unreachable: {exc}")
    if payload.get("errors"):
        sys.exit("leetcode graphql error: " + payload["errors"][0].get("message", "?"))
    return payload["data"]


def by_slug(slug, extra):
    q = graphql(BY_SLUG % extra, {"titleSlug": slug})["question"]
    if q is None:
        sys.exit(f"no problem with slug {slug!r}")
    return q


def by_number(number, extra):
    found = graphql(BY_NUMBER, {"filters": {"searchKeywords": number}})["questionList"]["data"]
    exact = [q for q in found if q["questionFrontendId"] == number]
    if not exact:
        sys.exit(f"no problem numbered {number}")
    # Re-fetch by slug so that --content and --tags go through one code path.
    return by_slug(exact[0]["titleSlug"], extra)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if len(args) != 1 or flags - {"--content", "--tags"}:
        sys.exit(__doc__)

    extra = ("content " if "--content" in flags else "") + (
        "topicTags { name } " if "--tags" in flags else ""
    )
    target = args[0]

    if target == "daily":
        slug = graphql(DAILY)["activeDailyCodingChallengeQuestion"]["question"]["titleSlug"]
        q = by_slug(slug, extra)
    elif target.isdigit():
        q = by_number(target, extra)
    else:
        m = re.search(r"/problems/([^/?#]+)", target)
        q = by_slug(m.group(1) if m else target, extra)

    out = {
        "number": q["questionFrontendId"],
        "title": q["title"],
        "slug": q["titleSlug"],
        "difficulty": q["difficulty"],
    }
    if "--content" in flags:
        out["content"] = q["content"]
    if "--tags" in flags:
        out["tags"] = [t["name"] for t in q["topicTags"]]
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
