# Problem: Largest Rectangle in Histogram (Optional) - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution(object):
    def largestRectangleArea(self, arr):
        left = [0]*len(arr)
        right = [len(arr)]*len(arr)
        stack = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]+1
            stack.append(i)
        res = [0]*len(arr)
        for i in range(len(arr)):
            res[i] = ((right[i]-i)+(i-left[i]))*arr[i]
        return (max(res))
            