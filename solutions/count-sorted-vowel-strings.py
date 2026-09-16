class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for i in range(1, n):
            dp[0] += dp[1] + dp[2] + dp[3] + dp[4]
            dp[1] += dp[2] + dp[3] + dp[4]
            dp[2] += dp[3] + dp[4]
            dp[3] += dp[4]

        return sum(dp)
