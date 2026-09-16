class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        dp = [[[ -1 for _ in range(2) ] for _ in range(k+1) ] for _ in range(n)]

        def solve(i, j, c):
            if j == k and c == 0:
                return 1
            if j > k:
                return 0
            if i == n:
                return 0

            if dp[i][j][c] != -1:
                return dp[i][j][c]
            
            if c == 1:
                dp[i][j][c] = (solve(i+1, j, 1) + solve(i+1, j+1, 1) + solve(i+1, j, 0)) % (10**9+7)
                return dp[i][j][c]
            else:
                dp[i][j][c] = (solve(i+1, j, 0) + solve(i+1, j+1, 1)) % (10**9+7)
                return dp[i][j][c]
        
        return solve(0, 0, 0)
