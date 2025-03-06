# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution(object):
    def thirdMax(self, nums):
        nums.sort(reverse=True)
        count = 1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                count+=1
            if count == 3:
                return nums[i]
        return nums[0]

        