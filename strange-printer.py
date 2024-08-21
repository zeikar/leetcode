class Solution:
    def strangePrinter(self, s: str) -> int:

        @cache
        def dfs(s):
            if len(s) == 0:
                return 0

            ret = 1 + dfs(s[1:])

            for i in range(1, len(s)):
                if s[i] == s[0]:
                    ret = min(ret, dfs(s[1:i]) + dfs(s[i:]))

            return ret

        return dfs(s)
