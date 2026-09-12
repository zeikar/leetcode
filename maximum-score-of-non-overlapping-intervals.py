from bisect import bisect_left
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        new_intervals = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))

        prev = []
        for i in range(n):
            prev.append(bisect_left(new_intervals, new_intervals[i][1], key=lambda x: x[0]))

        dp = [[(0, [])] * (n + 1) for _ in range(5)]

        for i in range(n):
            for c in range(1, 5):
                a = dp[c][i]
                b = dp[c-1][prev[i]]
                score = b[0]+new_intervals[i][2]
                itv = sorted(b[1] + [new_intervals[i][3]])

                if a[0] > score or (a[0] == score and a[1] < itv):
                    dp[c][i+1] = a
                else:
                    dp[c][i+1] = (b[0]+new_intervals[i][2], itv)

        return dp[4][n][1]
