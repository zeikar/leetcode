class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglynums = [1]
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            c = min(uglynums[p2] * 2, uglynums[p3] * 3, uglynums[p5] * 5)
            uglynums.append(c)

            if c == uglynums[p2] * 2:
                p2 += 1
            if c == uglynums[p3] * 3:
                p3 += 1
            if c == uglynums[p5] * 5:
                p5 += 1

        return uglynums[n - 1]
