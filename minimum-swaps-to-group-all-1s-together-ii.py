class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        zeros = nums[:ones].count(0)

        nums = nums + nums

        ans = 987654321
        for i in range(ones, 2*n):
            ans = min(ans, zeros)

            if nums[i] == 0:
                zeros += 1
            if nums[i - ones] == 0:
                zeros -= 1

        return ans
