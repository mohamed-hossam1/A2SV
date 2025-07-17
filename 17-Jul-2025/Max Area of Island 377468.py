# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_length=0
        def dfs(i,j):
            nonlocal length
            if i<0 or j<0 or i==len(grid) or j==len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            length+=1
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    length=0
                    dfs(i,j)
                    max_length=max(max_length,length)
        
        return max_length
        