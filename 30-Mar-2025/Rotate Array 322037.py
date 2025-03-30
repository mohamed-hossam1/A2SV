# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        k%=len(nums)
        for i in range(0,len(nums)-k):
            nums.append(nums.pop(0))
        