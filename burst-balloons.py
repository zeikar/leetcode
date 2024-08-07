class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def solve(s, e):
            ret = 0
            for i in range(s + 1, e):
                score = nums[s] * nums[i] * nums[e]
                ret = max(ret, score + solve(s, i) + solve(i, e))

            return ret

        return solve(0, len(nums) - 1)
