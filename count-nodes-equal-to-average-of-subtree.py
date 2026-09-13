# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def search(node: TreeNode):
            if node == None:
                return (0, 0, 0)

            left = search(node.left)
            right = search(node.right)

            weights = left[0] + right[0] + node.val
            cnt = left[1] + right[1] + 1
            res = left[2] + right[2]

            if weights // cnt == node.val:
                res += 1

            return (weights, cnt, res)

        return search(root)[2]
