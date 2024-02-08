from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1, n + 1):
            dp.append(i)

        for i in range(1, int(sqrt(n))+1):
            for j in range(2, n + 1):
                if j - i * i >= 0:
                    dp[j] = min(dp[j], dp[j - i * i] + 1)

        return dp[n]
