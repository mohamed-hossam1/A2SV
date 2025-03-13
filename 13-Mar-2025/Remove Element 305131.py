# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def moveZeroes(self, nums):
        p = 0  
        for s in range(len(nums)):
            if nums[s] != 0:
                nums[p], nums[s] = nums[s], nums[p]  
                p += 1
        return nums