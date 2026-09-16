from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)[1]

    def solve(self, root: Optional[TreeNode]) -> [int, int]:
        if root is None:
            return 0, 0

        left_sum, left_tilt = self.solve(root.left)
        right_sum, right_tilt = self.solve(root.right)
        return left_sum + right_sum + root.val, abs(left_sum - right_sum) + left_tilt + right_tilt
