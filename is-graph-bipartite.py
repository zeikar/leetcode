from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        queue = deque()
        visited = [-1] * len(graph)

        for i in range(len(graph)):
            if not graph[i] or visited[i] != -1:
                continue

            queue.append((i, 0))
            visited[i] = 0

            while queue:
                node, flag = queue.popleft()

                for neighbor in graph[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1 - flag
                        queue.append((neighbor, 1 - flag))
                    elif visited[neighbor] == flag:
                        return False

        return True
