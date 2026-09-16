import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        queue = [(0, 0, 0)]
        distances = [[9999999] * 100 for i in range(100)]

        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            e, x, y = heapq.heappop(queue)

            if x == rows - 1 and y == cols - 1:
                return e

            for d in direction:
                nx, ny = x + d[0], y + d[1]

                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue

                diff = max(e, abs(heights[x][y] - heights[nx][ny]))

                if distances[nx][ny] > diff:
                    distances[nx][ny] = diff
                    heapq.heappush(queue, (diff, nx, ny))

        return -1
