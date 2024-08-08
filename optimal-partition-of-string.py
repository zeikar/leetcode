class Solution:
    def partitionString(self, s: str) -> int:
        found = defaultdict(bool)
        ans = 1
        for l in s:
            if found[l]:
                found = defaultdict(bool)
                ans += 1
            found[l] = True

        return ans
