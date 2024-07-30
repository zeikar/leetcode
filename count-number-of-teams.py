class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0

        for i in range(1, n-1):
            lessleft = 0
            moreleft = 0
            for l in range(0, i):
                if rating[l] < rating[i]:
                    lessleft += 1
                else:
                    moreleft += 1

            lessright = 0
            moreright = 0
            for r in range(i + 1, n):
                if rating[r] < rating[i]:
                    lessright += 1
                else:
                    moreright += 1

            ans += lessleft * moreright
            ans += moreleft * lessright

        return ans
