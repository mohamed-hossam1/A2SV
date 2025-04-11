# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0: return -1
        if target == 0: return len(nums)

        ans = -1
        l = 0
        s = 0

        for r in range(len(nums)):
            s += nums[r]
            while s > target:
                s -= nums[l]
                l += 1
            if s == target:
                ans = max(ans, r - l + 1)

        return len(nums) - ans if ans != -1 else -1