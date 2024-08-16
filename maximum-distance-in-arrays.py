class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum, maximum = arrays[0][0], arrays[0][-1]
        ans = 0

        for a in arrays[1:]:
            ans = max(ans, abs(maximum - a[0]), abs(a[-1] - minimum))
            maximum = max(maximum, a[-1])
            minimum = min(minimum, a[0])

        return ans
