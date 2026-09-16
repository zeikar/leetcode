class Solution:
    def minimumDeletions(self, s: str) -> int:
        deleteA = [0] * len(s)
        deleteAcnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'a':
                deleteAcnt += 1
            deleteA[i] = deleteAcnt

        deleteB = [0] * len(s)
        deleteBcnt = 0
        for i in range(len(s)):
            if s[i] == 'b':
                deleteBcnt += 1
            deleteB[i] = deleteBcnt

        ans = float('inf')
        for i in range(len(s)):
            ans = min(ans, deleteA[i] + deleteB[i] - 1)
        return ans
