class Solution:
    def minSteps(self, n: int) -> int:

        @cache
        def getMinSteps(l, copy):
            if l > n:
                return 987654321
            if l == n:
                return 0

            if copy == 0:
                copy = l
                return getMinSteps(l + copy, copy) + 2

            return min(getMinSteps(l * 2, l) + 2, getMinSteps(l + copy, copy) + 1)

        return getMinSteps(1, 0)
