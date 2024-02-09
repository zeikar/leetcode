class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums = [1] + nums

        @cache
        def countMultiples(i):
            res = []
            for j in range(i + 1, len(nums)):
                c = countMultiples(j)
                if nums[j] % nums[i] == 0 and len(res) <= len(c):
                    res = c

            return [nums[i]] + res

        return countMultiples(0)[1:]
