from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}

        for i in range(len(s)):
            pos[s[i]] = i

        ans = []
        chunk = []

        for i in range(len(s)):
            chunk.append(s[i])

            split = True

            for j in range(len(chunk)):
                if pos[chunk[j]] > i:
                    split = False
                    break

            if split:
                ans.append(len(chunk))
                chunk = []

        return ans
