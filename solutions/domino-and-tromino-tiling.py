class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = 1
        dp[1][0] = 1

        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 2][0] + dp[i - 1][0] + dp[i - 1][1]) % int(1e9 + 7)
            dp[i][1] = (dp[i - 2][0] * 2 + dp[i - 1][1]) % int(1e9 + 7)

        return dp[n][0]
