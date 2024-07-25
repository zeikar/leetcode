class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[987654321] * n for i in range(n)]
        dp[0] = grid[0]
        print(dp)

        for i in range(1, n):
            min1, min2 = 0, 0
            min1v, min2v = 987654321, 987654321
            for j in range(n):
                if dp[i - 1][j] <= min1v:
                    min2 = min1
                    min2v = min1v
                    min1 = j
                    min1v = dp[i - 1][j]
                elif dp[i - 1][j] <= min2v:
                    min2 = j
                    min2v = dp[i - 1][j]

            print(min1, min2)
            for j in range(n):
                if j != min1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][min1] + grid[i][j])
                if j != min2:
                    dp[i][j] = min(dp[i][j], dp[i - 1][min2] + grid[i][j])

        print(dp)
        return min(dp[-1])
