from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] %= k

        ans = [0 for _ in range(k)]
        cnt = [[0 for _ in range(k)] for _ in range(n+1)]
        
        for i in range(n):
            for j in range(k):
                cnt[i+1][j*nums[i]%k] += cnt[i][j]
            cnt[i+1][nums[i]] += 1

            for j in range(k):
                ans[j] += cnt[i+1][j]

        return ans
