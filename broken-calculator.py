class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        def solve(startValue, target):
            if startValue == target:
                return 0
            if startValue > target:
                return startValue - target

            if startValue < target:
                if target % 2 == 0:
                    return 1 + solve(startValue, target // 2)
                else:
                    return 1 + solve(startValue, target + 1)

        return solve(startValue, target)
