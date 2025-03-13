# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def removeElement(self, nums, val):
        l = 0
        for i in nums:
            if  i!=val:
                nums[l] = i
                l+=1
        return l
