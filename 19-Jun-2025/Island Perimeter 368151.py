# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += ((i + 1 >= m) or (grid[i + 1][j] == 0))
                    res += ((i - 1 < 0) or (grid[i - 1][j] == 0))
                    res += ((j + 1 >= n) or (grid[i][j + 1] == 0))
                    res += ((j - 1 < 0) or (grid[i][j - 1] == 0))

        return res 