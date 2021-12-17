class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1

        return max(ans, cnt)
