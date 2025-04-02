# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        pre = [1]*(n+1)
        suf = [1]*(n+1)
        for i in range(0,n):
            pre[i]=pre[i-1]*nums[i]
        for i in range(n-1,-1,-1):
            suf[i]=suf[i+1]*nums[i]
        
        ans = []
        for i in range(n):
            ans.append(pre[i-1]*suf[i+1])
        return(ans)

        