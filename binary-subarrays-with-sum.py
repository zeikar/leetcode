class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ans = 0
        sum = 0
        cnt = defaultdict(int)
        cnt[0] = 1

        for num in nums:
            sum += num
            ans += cnt[sum - goal]
            cnt[sum] += 1

        return ans
