class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        board = [[0] * 202 for _ in range(202)]
        x = 101
        y = 101
        minX = x - rStart
        maxX = x + rows - rStart - 1
        minY = y - cStart
        maxY = y + cols - cStart - 1

        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 3
        cnt = 1
        ans = []

        while len(ans) < rows * cols:
            board[x][y] = cnt
            if x >= minX and x <= maxX and y >= minY and y <= maxY:
                ans.append([x - 101 + rStart, y - 101 + cStart])
                cnt += 1

            nx = x + dir[(d+1) % 4][0]
            ny = y + dir[(d+1) % 4][1]
            if board[nx][ny] == 0:  # ok
                x = nx
                y = ny
                d = (d+1) % 4
            else:
                x = x + dir[d][0]
                y = y + dir[d][1]

        return ans
