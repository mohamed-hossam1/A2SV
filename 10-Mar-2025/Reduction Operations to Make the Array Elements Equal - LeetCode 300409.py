# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        sum = 0
        count = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                count+=1
            sum+=count
        return sum
