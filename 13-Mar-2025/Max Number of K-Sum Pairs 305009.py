# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        l,r=0,len(nums)-1
        count = 0 
        while l<r:
            if nums[l]+nums[r]==k:
                count+=1
                r-=1
                l+=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                l+=1
        return (count)
        