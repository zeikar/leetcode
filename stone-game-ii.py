class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        prefixSum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + piles[i - 1]

        @cache
        def stone(idx, m):
            if idx == n:
                return 0

            ret = 0
            for x in range(0, 2 * m):
                i = idx + x
                if i < n:
                    ret = max(
                        ret,
                        prefixSum[n] - prefixSum[idx] -
                        stone(i + 1, max(x + 1, m)),
                    )
            return ret

        return stone(0, 1)
