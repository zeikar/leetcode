class Solution:
    def numberToWords(self, num: int) -> str:

        def toWordBelow10(num):
            return [
                "",
                "One",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
            ][num]

        def toWordBelow20(num):
            if num < 10:
                return toWordBelow10(num)
            return [
                "Ten",
                "Eleven",
                "Twelve",
                "Thirteen",
                "Fourteen",
                "Fifteen",
                "Sixteen",
                "Seventeen",
                "Eighteen",
                "Nineteen",
            ][num - 10]

        def toWordBelow100(num):
            if num < 20:
                return toWordBelow20(num)

            ret = []
            if num // 10 > 0:
                ret.append(
                    [
                        "",
                        "",
                        "Twenty",
                        "Thirty",
                        "Forty",
                        "Fifty",
                        "Sixty",
                        "Seventy",
                        "Eighty",
                        "Ninety",
                    ][num // 10]
                )
                num %= 10

            ret.append(toWordBelow10(num % 10))
            return " ".join(ret).strip()

        def toWordBelow1000(num):
            ret = []
            if num // 100 > 0:
                ret.append(toWordBelow10(num // 100))
                ret.append("Hundred")
                num %= 100

            ret.append(toWordBelow100(num))
            return " ".join(ret).strip()

        ret = []
        if num // 10**9 > 0:
            ret.append(toWordBelow1000(num // 10**9))
            ret.append("Billion")
            num %= 10**9

        if num // 10**6 > 0:
            ret.append(toWordBelow1000(num // 10**6))
            ret.append("Million")
            num %= 10**6

        if num // 10**3 > 0:
            ret.append(toWordBelow1000(num // 10**3))
            ret.append("Thousand")
            num %= 10**3

        ret.append(toWordBelow1000(num))
        ans = " ".join(ret).strip()
        if ans == "":
            ans = "Zero"
        return ans
