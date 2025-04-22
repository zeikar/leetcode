class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        c = Counter(nums[0 : k - 1])
        s = sum(nums[0 : k - 1])

        for i in range(k - 1, len(nums)):
            s += nums[i]
            c[nums[i]] += 1

            if len(c) == k:
                result = max(result, s)

            if c[nums[i - k + 1]] == 1:
                del c[nums[i - k + 1]]
            else:
                c[nums[i - k + 1]] -= 1
            s -= nums[i - k + 1]

        return result
