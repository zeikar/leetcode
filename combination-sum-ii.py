class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []

        def solve(idx, num, l):
            if num < 0:
                return
            if num == 0:
                ans.append(l)
            if idx == n:
                return

            ret = []
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                solve(i + 1, num - candidates[i], l + [candidates[i]])

        solve(0, target, [])
        return ans
