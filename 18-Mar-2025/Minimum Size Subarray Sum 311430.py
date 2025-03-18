# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, target, nums):
        cur = 0
        ans = len(nums)+1
        l = 0
        for r in range(len(nums)):
            cur+=nums[r]
            while cur-nums[l]>=target:
                cur-=nums[l]
                l+=1
            if cur>=target:
                ans = min(ans,r-l+1)
        if ans == len(nums)+1:
            return 0
        return ans