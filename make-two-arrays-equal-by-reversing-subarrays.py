class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        n = len(target)
        tcnt = [0] * 1001
        acnt = [0] * 1001

        for i in range(n):
            tcnt[target[i]] += 1
            acnt[arr[i]] += 1

        for i in range(1, 1001):
            if tcnt[i] != acnt[i]:
                return False
        return True
