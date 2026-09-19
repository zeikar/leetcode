from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first, last = {}, {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for c in first:
            start, end = first[c], last[c]
            ok = True
            i = start
            while i <= end:
                cc = s[i]
                if first[cc] < start:
                    ok = False
                    break
                end = max(end, last[cc])
                i += 1
            if ok:
                intervals.append((end, start))

        intervals.sort()

        ans = []
        prev = -1
        for end, start in intervals:
            if start > prev:
                ans.append(s[start:end + 1])
                prev = end
        return ans
