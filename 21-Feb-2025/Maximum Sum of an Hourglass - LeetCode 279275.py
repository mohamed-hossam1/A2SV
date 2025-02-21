# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution(object):
    def maxSum(self, grid):
        m = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                m = max(m,sum(grid[i-1][j-1:j+2])+grid[i][j]+sum(grid[i+1][j-1:j+2]))

        return m
        