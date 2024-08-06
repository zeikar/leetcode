class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s, n = sum(machines), len(machines)
        if s % n != 0:
            return -1

        target = s // n
        ans = max(machines) - target
        needs = 0
        for m in machines:
            needs += m - target
            ans = max(ans, abs(needs))

        return ans
