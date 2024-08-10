class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = n * 2
        grid2 = [[0] * m for _ in range(m)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    grid2[2*i][2*j+1] = 1
                    grid2[2*i+1][2*j] = 1
                elif grid[i][j] == "\\":
                    grid2[2*i][2*j] = 1
                    grid2[2*i+1][2*j+1] = 1

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= m or grid2[x][y] == 1:
                return
            grid2[x][y] = 1

            dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
            if grid[x//2][y//2] == "/":
                dir += [[1, -1], [-1, 1]]
            elif grid[x//2][y//2] == "\\":
                dir += [[1, 1], [-1, -1]]

            for d in dir:
                dfs(x+d[0], y+d[1])

        ans = 0
        for i in range(m):
            for j in range(m):
                if grid2[i][j] == 0:
                    ans += 1
                    dfs(i, j)
        return ans
