"""Shared helpers: load the study notes and pair them with solution files."""

import glob
import json
import os
import re
import urllib.error
import urllib.request

GRAPHQL = "https://api.github.com/graphql"
REPO = os.environ.get("GITHUB_REPOSITORY", "zeikar/leetcode")
# The discussion category the notes live in, the same one the site publishes.
CATEGORY = "posts"

CODE_BLOCK = re.compile(r"```[Pp]ython\s*\n(.*?)```", re.S)

# Discussions are only in the GraphQL API, which filters them by category id
# rather than slug, so the id is looked up first. It comes from the category
# list: with a workflow's GITHUB_TOKEN, discussionCategory(slug:) answers
# NOT_FOUND even for a category that exists.
CATEGORIES_QUERY = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    discussionCategories(first: 100) { nodes { id slug } }
  }
}
"""

NOTES_QUERY = """
query($owner: String!, $name: String!, $category: ID!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, categoryId: $category, states: [OPEN], after: $cursor,
                orderBy: {field: CREATED_AT, direction: ASC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number
        title
        body
        url
        labels(first: 10) { nodes { name } }
      }
    }
  }
}
"""


def _graphql(query, variables):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required (GitHub's GraphQL API rejects anonymous calls)")
    payload = json.dumps({"query": query, "variables": variables}).encode()
    request = urllib.request.Request(
        GRAPHQL,
        data=payload,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.load(response)
    except urllib.error.HTTPError as error:
        raise SystemExit(f"GitHub GraphQL API refused the request ({error.code})") from error
    if "errors" in body:
        raise SystemExit(f"GitHub GraphQL API returned errors: {body['errors']}")
    return body["data"]["repository"]


def load_notes():
    """Every open discussion in the notes category, oldest first."""
    owner, name = REPO.split("/")
    categories = _graphql(CATEGORIES_QUERY, {"owner": owner, "name": name})["discussionCategories"]["nodes"]
    ids = {category["slug"]: category["id"] for category in categories}
    if CATEGORY not in ids:
        raise SystemExit(f"{REPO} has no discussion category '{CATEGORY}' (found: {', '.join(ids) or 'none'})")
    variables = {"owner": owner, "name": name, "category": ids[CATEGORY]}
    notes, cursor = [], None
    while True:
        page = _graphql(NOTES_QUERY, {**variables, "cursor": cursor})["discussions"]
        notes += [
            {
                "number": node["number"],
                "title": node["title"],
                "body": node["body"],
                "html_url": node["url"],
                "labels": node["labels"]["nodes"],
            }
            for node in page["nodes"]
        ]
        if not page["pageInfo"]["hasNextPage"]:
            return notes
        cursor = page["pageInfo"]["endCursor"]


def problem_number(note_title):
    match = re.match(r"\s*(\d+)\.", note_title)
    return int(match.group(1)) if match else None


def problem_title(note_title):
    return re.sub(r"^\s*\d+\.\s*", "", note_title).strip()


def match_key(text):
    """Key used to pair a note title with its solution filename.

    Hyphenation differs between the two ("Find K-th Smallest Pair Distance" vs
    find-k-th-smallest-pair-distance.py), so only letters and digits survive.
    """
    return re.sub(r"[^a-z0-9]", "", text.lower())


def solution_files(root="."):
    """{match_key: path} for every solution file in the repo root."""
    return {
        match_key(os.path.basename(path)[:-3]): path
        for path in sorted(glob.glob(os.path.join(root, "*.py")))
    }


def code_blocks(body):
    return [match.group(1) for match in CODE_BLOCK.finditer(body or "")]


STUB_CLASS = re.compile(r"^class (?:ListNode|TreeNode|Node|Iterator)\b")
SCAFFOLDING = re.compile(r"^\s*(?:import|from)\s|^\s*#")


def solution_code(code):
    """The solution itself, with the scaffolding around it dropped.

    Solution files carry imports and an uncommented LeetCode class stub so the
    repo can be linted; the notes keep the pristine editor paste, where those
    are absent or commented out. Neither is a difference worth reporting, so
    both sides are stripped down to the solution before they are compared.
    """
    kept, in_stub = [], False
    for line in code.strip().splitlines():
        if STUB_CLASS.match(line):
            in_stub = True
            continue
        if in_stub:
            if not line.strip() or line.startswith((" ", "\t")):
                continue
            in_stub = False
        if line.strip() and not SCAFFOLDING.match(line):
            kept.append(line.rstrip())
    return "\n".join(kept)


def pair_with_files(notes, root="."):
    """Return (pairs, notes_missing_a_file, files_missing_a_note)."""
    files = solution_files(root)
    paired, orphan_notes = [], []
    for note in notes:
        path = files.get(match_key(problem_title(note["title"])))
        if path is None:
            orphan_notes.append(note)
        else:
            paired.append((note, path))
    claimed = {path for _, path in paired}
    orphan_files = [path for path in files.values() if path not in claimed]
    return paired, orphan_notes, orphan_files
