# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution(object):
    def nextGreaterElements(self, nums):
        nums = nums+nums
        stack = []
        ans = [-1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()

            if stack:
                ans[i]=stack[-1]

            stack.append(nums[i])

        return(ans[:len(nums)//2])
        

