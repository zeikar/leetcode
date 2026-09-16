from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [height[0]] * n
        right_max = [height[n - 1]] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0
        for i in range(n):
            res += max(0, min(left_max[i], right_max[i]) - height[i])

        return res
