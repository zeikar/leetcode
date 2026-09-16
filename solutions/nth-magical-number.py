class Solution:
    def lcm(self, a, b):
        return a // self.gcd(a, b) * b

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = self.lcm(a, b)
        cnt = lcm // a + lcm // b - 1

        skip = n // cnt
        remain = n % cnt
        ans = lcm * skip

        a_cnt = 1
        b_cnt = 1
        for _ in range(remain):
            if a * a_cnt < b * b_cnt:
                ans = lcm * skip + a * a_cnt
                a_cnt += 1
            else:
                ans = lcm * skip + b * b_cnt
                b_cnt += 1

        return ans % int(1e9 + 7)
