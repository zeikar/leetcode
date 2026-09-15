class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        paldp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                paldp[l][r] = True
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                paldp[l][r] = True
                l -= 1
                r += 1

        dp = [0 for _ in range(n+1)]
        for i in range(n):
            dp[i+1] = dp[i]
            for j in range(0, i+1):
                if i - j + 1 >= k and paldp[j][i]:
                    dp[i+1] = max(dp[i+1], dp[j] + 1)
                else:
                    dp[i+1] = max(dp[i+1], dp[j])

        return dp[n]
