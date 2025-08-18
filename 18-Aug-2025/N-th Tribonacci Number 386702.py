# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        prev1=0
        prev2=1
        cur=1
        for i in range(3,n+1):
            prev1,prev2,cur=prev2,cur,prev1+prev2+cur
        return cur