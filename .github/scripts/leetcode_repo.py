"""Shared helpers: load the study issues and pair them with solution files."""

import glob
import json
import os
import re
import urllib.error
import urllib.request

GRAPHQL = "https://api.github.com/graphql"
REPO = os.environ.get("GITHUB_REPOSITORY", "zeikar/leetcode")

CODE_BLOCK = re.compile(r"```[Pp]ython\s*\n(.*?)```", re.S)

# The REST list and search endpoints both silently omit at least one issue of
# this repo (#20), so pagination goes through GraphQL, which is cursor-based.
ISSUES_QUERY = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    issues(first: 100, states: OPEN, after: $cursor,
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


def _graphql(variables):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required (GitHub's GraphQL API rejects anonymous calls)")
    payload = json.dumps({"query": ISSUES_QUERY, "variables": variables}).encode()
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
    return body["data"]["repository"]["issues"]


def load_issues():
    """Every open issue in the repo, oldest first."""
    owner, name = REPO.split("/")
    issues, cursor = [], None
    while True:
        page = _graphql({"owner": owner, "name": name, "cursor": cursor})
        issues += [
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
            return issues
        cursor = page["pageInfo"]["endCursor"]


def problem_number(issue_title):
    match = re.match(r"\s*(\d+)\.", issue_title)
    return int(match.group(1)) if match else None


def problem_title(issue_title):
    return re.sub(r"^\s*\d+\.\s*", "", issue_title).strip()


def match_key(text):
    """Key used to pair an issue title with its solution filename.

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
    repo can be linted; the issues keep the pristine editor paste, where those
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


def pair_with_files(issues, root="."):
    """Return (pairs, issues_missing_a_file, files_missing_an_issue)."""
    files = solution_files(root)
    paired, orphan_issues = [], []
    for issue in issues:
        path = files.get(match_key(problem_title(issue["title"])))
        if path is None:
            orphan_issues.append(issue)
        else:
            paired.append((issue, path))
    claimed = {path for _, path in paired}
    orphan_files = [path for path in files.values() if path not in claimed]
    return paired, orphan_issues, orphan_files
