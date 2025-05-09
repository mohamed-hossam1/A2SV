# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)*len(matrix[0])-1
        size = len(matrix[0])
        while l<=r:
            mid = (l+r)//2
            x,y = int(mid//len(matrix[0])),int(mid%len(matrix[0]))
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                r = mid-1
            else:
                l = mid+1
        return False