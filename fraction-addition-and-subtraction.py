class Solution:
    def fractionAddition(self, expression: str) -> str:
        sign = 1
        n = 0
        numerators, denominators = [], []
        if expression[0] == "-":
            sign = -1
            expression = expression[1:]

        for e in expression:
            if e == "-" or e == "+":
                denominators.append(n)
                n = 0

                if e == "-":
                    sign = -1
                else:
                    sign = 1
            elif e == "/":
                numerators.append(sign * n)
                n = 0
            else:
                n *= 10
                n += int(e)
        denominators.append(n)

        denominator = 1
        g = 1
        for d in denominators:
            g = gcd(g, d)
            denominator *= d
        denominator //= g

        numerator = 0
        for i in range(len(numerators)):
            numerator += numerators[i] * (denominator // denominators[i])
        g = gcd(numerator, denominator)
        return f"{numerator//g}/{denominator//g}"
