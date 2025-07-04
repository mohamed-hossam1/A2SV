# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        countFresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    countFresh += 1
        
        if countFresh == 0:
            return 0
        if not q:
            return -1

        minutes = -1
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        countFresh -= 1
                        q.append((i, j))
            minutes += 1

        return minutes if countFresh == 0 else -1