import heapq
from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] > rank[py]:
                    parent[py] = px
                else:
                    parent[px] = py
                    if rank[px] == rank[py]:
                        rank[py] += 1

        parent = [i for i in range(len(s))]
        rank = [1] * len(s)
        for x, y in pairs:
            union(x, y)

        m = defaultdict(list)
        for i in range(len(s)):
            m[find(i)].append(s[i])

        for i in m:
            heapq.heapify(m[i])

        res = ""
        for i in range(len(s)):
            res += heapq.heappop(m[find(i)])
        return res
