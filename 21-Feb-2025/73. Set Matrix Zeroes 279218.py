# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution(object):
    def setZeroes(self, matrix):
        pi ,pj = False,False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if i==0:
                        pi=True
                    if j==0:
                        pj = True
        
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][0]==0:
                    if i != 0 or pi:
                        matrix[i][j]=0

                if matrix[0][j]==0:
                    if j != 0 or pj:
                        matrix[i][j]=0
        