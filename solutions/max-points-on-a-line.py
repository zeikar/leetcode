from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1

        for i in range(len(points)):
            x1, y1 = points[i]

            gradients = dict({0: 0})
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                g = (y2 - y1) / (x2 - x1) if x2 != x1 else 1e9
                gradients[g] = gradients.get(g, 0) + 1

            ans = max(ans, max(gradients.values()) + 1)

        return ans
    