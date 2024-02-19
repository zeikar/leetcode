class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(nums)
        res = [s - nums[0] * n]
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            res.append(res[-1] - diff * (n - i) + diff * i)
        return res
