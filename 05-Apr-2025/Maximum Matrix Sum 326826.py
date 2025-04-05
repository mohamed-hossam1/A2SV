# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        mini = float('inf')
        cnt = 0
        
        for row in matrix:
            for val in row:
                if val < 0:
                    cnt += 1
                mini = min(abs(val), mini)
                total_sum += abs(val)
        
        if cnt % 2 == 1:
            total_sum -= 2 * mini
        
        return total_sum