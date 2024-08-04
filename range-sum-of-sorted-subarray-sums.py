class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        sums = []
        for i in range(n):
            for j in range(i, n):
                sums.append(prefixSum[j + 1] - prefixSum[i])

        sums.sort()

        ans = 0
        for i in range(left - 1, right):
            ans += sums[i]
            ans %= 1000000007
        return ans
