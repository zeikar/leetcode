class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        div = 1000
        while n >= div:
            res += n - div + 1
            div *= 1000

        return res
