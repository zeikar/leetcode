from functools import lru_cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.solve(root, False)

    @lru_cache(None)
    def solve(self, root: Optional[TreeNode], stole_before: bool) -> int:
        if not root:
            return 0
        if stole_before:
            return self.solve(root.left, False) + self.solve(root.right, False)
        else:
            return max(self.solve(root.left, True) + self.solve(root.right, True) + root.val,
                       self.solve(root.left, False) + self.solve(root.right, False))
