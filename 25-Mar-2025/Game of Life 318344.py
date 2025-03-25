# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def countAlive(self, i, j, board, m, n, delRow, delCol):
        count = 0
        for k in range(8):
            newRow = i + delRow[k]
            newCol = j + delCol[k]

            if 0 <= newRow < m and 0 <= newCol < n and board[newRow][newCol] == 1:
                count += 1
        return count

    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])
        temp = [[0] * n for _ in range(m)]
        delRow = [-1, 0, 1, 0, -1, 1, 1, -1]
        delCol = [0, 1, 0, -1, 1, 1, -1, -1]

        for i in range(m):
            for j in range(n):
                aliveCount = self.countAlive(i, j, board, m, n, delRow, delCol)
                if board[i][j] == 0:
                    if aliveCount == 3:
                        temp[i][j] = 1
                else:
                    if aliveCount < 2 or aliveCount > 3:
                        temp[i][j] = 0
                    else:
                        temp[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] = temp[i][j]