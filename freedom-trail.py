class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        k = len(key)

        @cache
        def rotate(keyIndex, ringIndex):
            if keyIndex == k:
                return 0

            ans = 987654321
            # left
            for i in range(n):
                ri = (ringIndex + n - i) % n
                if ring[ri] == key[keyIndex]:
                    ans = min(ans, rotate(keyIndex + 1, ri) + i + 1)
                    break

            # right
            for i in range(n):
                ri = (ringIndex + i) % n
                if ring[ri] == key[keyIndex]:
                    ans = min(ans, rotate(keyIndex + 1, ri) + i + 1)
                    break

            return ans

        return rotate(0, 0)
