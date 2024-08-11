class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y, visited):
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or grid[x][y] == 0:
                return
            visited[x][y] = True
            dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
            for d in dir:
                dfs(x + d[0], y + d[1], visited)

        def countIslands():
            cnt = 0
            visited = [[False] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if visited[i][j] == False and grid[i][j] == 1:
                        cnt += 1
                        dfs(i, j, visited)
            print(cnt)
            return cnt

        if countIslands() != 1:  # already disconnected
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    cnt = countIslands()
                    if cnt != 1:
                        return 1
                    grid[i][j] = 1

        return 2
