class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, c in enumerate(s):
            ans += (i+1) * (26 - (ord(c)-ord('a')))
        
        return ans
