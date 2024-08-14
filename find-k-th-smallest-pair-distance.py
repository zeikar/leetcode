class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def countSmallerPair(n):
            ret = 0
            left = 0
            for right in range(len(nums)):
                while left <= right and nums[right] - nums[left] > n:
                    left += 1

                ret += right - left
            return ret

        s, e = 0, nums[-1] - nums[0]
        while s < e:
            mid = s + (e - s) // 2

            cnt = countSmallerPair(mid)
            if cnt < k:
                s = mid + 1
            else:
                e = mid
        return s
