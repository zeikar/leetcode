from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        n = len(nums)
        target = sum(nums) // 2

        dp = set([0])

        for i in range(n):
            newSum = []
            for s in dp:
                if s + nums[i] > target:
                    continue

                newSum.append(s + nums[i])

            for s in newSum:
                dp.add(s)

        return target in dp
