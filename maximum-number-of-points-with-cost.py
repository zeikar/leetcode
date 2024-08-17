class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = points[0][i]

        for i in range(1, m):
            leftMax = [0] * n
            leftMax[0] = dp[i - 1][0]
            for j in range(1, n):
                leftMax[j] = max(leftMax[j - 1] - 1, dp[i - 1][j])

            rightMax = [0] * n
            rightMax[-1] = dp[i - 1][-1]
            for j in range(n - 2, -1, -1):
                rightMax[j] = max(rightMax[j + 1] - 1, dp[i - 1][j])

            for j in range(n):
                dp[i][j] = points[i][j] + max(leftMax[j], rightMax[j])

        return max(dp[-1])
