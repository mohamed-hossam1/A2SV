# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LTS=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i, len(nums)):
                if nums[i]<nums[j]:
                    LTS[i]=max(LTS[i], LTS[j]+1)

        return max(LTS)