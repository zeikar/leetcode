from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        target = s // 2
        dp = [False] * (target + 1)
        cached = [False] * (s + 1)

        def solve(idx, current_sum):
            if current_sum == target:
                return True
            if current_sum > target:
                return False
            if idx == len(nums):
                return False
            if cached[current_sum]:
                return dp[current_sum]

            dp[current_sum] = solve(idx + 1, current_sum + nums[idx]) or solve(idx + 1, current_sum)
            cached[current_sum] = True
            return dp[current_sum]

        return solve(0, 0)
