# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calculate_divisor(nums, mid, threshold):
            divisor = 0
            for i in range(len(nums)):
                divisor += math.ceil(nums[i] / mid)
            return divisor

        low = 1
        high = max(nums)
        ans = 0 

        while low <= high:
            mid = low + (high - low) // 2
            if calculate_divisor(nums, mid, threshold) <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans