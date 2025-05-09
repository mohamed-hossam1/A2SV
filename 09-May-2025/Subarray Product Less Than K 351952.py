# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0 or k==1:
            return 0
        l,r=0,0
        sum = 1
        ans = 0
        for r in range(len(nums)):
            sum*=nums[r]
            while sum>=k:
                sum/=nums[l]
                l+=1
            ans+= r-l+1
        return ans
