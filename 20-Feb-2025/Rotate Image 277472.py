# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] =matrix[j][i],matrix[i][j]
        

        return matrix




         
        