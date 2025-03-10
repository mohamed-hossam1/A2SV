# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        s = []
        for i in nums:
            if not s or s[-1]!=i:
                s.append(i)
        for i in range(len(s)):
            nums[i] = s[i]
        for i in range(len(s),len(nums)):
            nums[i] = '_'
        return len(s)
        