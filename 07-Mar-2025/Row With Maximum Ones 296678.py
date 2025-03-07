# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m,c = 0,0
        l = 0
        for lis in mat:
            count = 0
            for i in lis:
                if i==1:
                    count+=1
            if count>m:
                m = count
                c = l

            l+=1
        return [c,m]