from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while True:
                idx = nums[i] - 1

                if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[idx]:
                    break

                nums[idx], nums[i] = nums[i], nums[idx]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
