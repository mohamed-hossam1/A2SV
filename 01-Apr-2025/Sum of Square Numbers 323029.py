# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution(object):
    def judgeSquareSum(self, c):
        m = 100000
        for i in range(m):
            d = c-i*i
            if d>=0:
                d = math.sqrt(d)
                if d == int(d):
                    return True
            else:
                return False

        return False

        