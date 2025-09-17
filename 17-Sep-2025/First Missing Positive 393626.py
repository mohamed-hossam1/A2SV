# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0<nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]:
                q = nums[nums[i]-1]
                w = nums[i]
                nums[nums[i]-1] = w
                nums[i] = q

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return(i+1)
        return(len(nums)+1)