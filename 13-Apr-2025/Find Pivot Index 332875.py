# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        if nums[0] == nums[-1]:
            return 0
        for i in range(1, len(nums)):
            if nums[-1] - nums[i] == nums[i-1]:
                return i
        return -1

