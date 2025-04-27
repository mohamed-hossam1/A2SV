# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        res = {}
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            
            if stack:
                res[nums2[i]] = stack[-1] 
            else: 
                res[nums2[i]] = -1

            stack.append(nums2[i])

        return [res[num] for num in nums1]