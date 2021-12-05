from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        maxim = nums[0]
        minim = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxim, minim = minim, maxim
            maxim = max(maxim * nums[i], nums[i])
            minim = min(minim * nums[i], nums[i])
            ans = max(ans, maxim)

        return ans
