# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        rowCount = [0] * m
        colCount = [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
       
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rowCount[i] > 1 or colCount[j] > 1):
                    result += 1
        
        return result