class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def check(x, y):
            # distinct check
            visited = set()
            for i in range(3):
                for j in range(3):
                    if grid[x + i][y + j] <= 0 or grid[x + i][y + j] >= 10:
                        return 0
                    visited.add(grid[x + i][y + j])
            if len(visited) != 9:
                return 0

            # sum check
            sums = set()
            for i in range(3):
                sum = 0
                for j in range(3):
                    sum += grid[x + i][y + j]
                sums.add(sum)

            for j in range(3):
                sum = 0
                for i in range(3):
                    sum += grid[x + i][y + j]
                sums.add(sum)

            sum = 0
            for i in range(3):
                sum += grid[x + i][y + i]
            sums.add(sum)

            sum = 0
            for i in range(3):
                sum += grid[x + 2 - i][y + i]
            sums.add(sum)

            return len(sums) == 1

        r = len(grid)
        c = len(grid[0])
        ans = 0
        for i in range(r - 2):
            for j in range(c - 2):
                ans += check(i, j)
        return ans
