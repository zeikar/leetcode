class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @cache
        def pick(x, y1, y2):
            if x == rows:
                return 0

            res = 0
            n = [-1, 0, 1]

            for next1 in n:
                for next2 in n:
                    ny1 = y1 + next1
                    ny2 = y2 + next2
                    if ny1 < 0 or ny1 >= cols or ny2 < 0 or ny2 >= cols:
                        continue

                    if ny1 == ny2:
                        continue

                    res = max(res, pick(x + 1, ny1, ny2) +
                              grid[x][y1] + grid[x][y2])

            return res

        return pick(0, 0, cols - 1)
