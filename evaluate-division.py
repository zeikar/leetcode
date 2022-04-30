import math
from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)

        for i in range(len(equations)):
            (a, b) = equations[i]
            edges[a].append((b, values[i]))
            edges[b].append((a, 1.0 / values[i]))

        def bfs(node, target):
            if len(edges[node]) == 0:
                return math.inf

            visited = defaultdict(bool)
            queue = deque([(node, 1.0)])
            visited[node] = True

            while queue:
                (current, value) = queue.popleft()

                if current == target:
                    return value

                for (next, mul) in edges[current]:
                    if visited[next]:
                        continue

                    queue.append((next, value * mul))
                    visited[next] = True

            return math.inf

        res = []
        for query in queries:
            result = bfs(query[0], query[1])
            res.append(result if result != math.inf else -1.0)

        return res
