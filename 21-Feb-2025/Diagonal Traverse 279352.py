# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution(object):
    def findDiagonalOrder(self, mat):

        ans = []
        t = 0
        pi,pj=0,0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans.append(mat[pi][pj])

                if t % 2==0:
                    if pj + 1 < len(mat[0]) and pi - 1 > -1:
                        pj+=1
                        pi-=1
                    else:
                        if pj + 1 < len(mat[0]):
                            pj+=1
                        else:
                            pi+=1
                        t+=1
                else:
                    if pj - 1 > -1 and pi + 1 < len(mat):
                        pj-=1
                        pi+=1
                    else:
                        if pi + 1 < len(mat):
                            pi+=1
                        else:
                            pj+=1
                        t+=1
        return ans

