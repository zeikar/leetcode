class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            d = divisor
            cnt = 1
            while dividend >= (d << 1):
                d <<= 1
                cnt <<= 1

            dividend -= d
            quotient += cnt

        return min(sign * quotient, (1 << 31) - 1)
