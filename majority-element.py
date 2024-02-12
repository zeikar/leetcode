class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ans = 0
        for n in nums:
            if cnt == 0:
                ans = n

            if ans == n:
                cnt += 1
            else:
                cnt -= 1

        return ans
