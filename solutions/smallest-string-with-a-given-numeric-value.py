class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ''

        for i in range(n):
            x = k - n + i + 1

            if x >= 26:
                result += 'z'
                k -= 26
            else:
                result += (chr(96 + x))
                k -= x

        return result[::-1]
