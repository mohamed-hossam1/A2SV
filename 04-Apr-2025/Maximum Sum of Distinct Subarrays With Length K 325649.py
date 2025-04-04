# Problem: Maximum Sum of Distinct Subarrays With Length K - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

def maximumSubarraySum(nums, k):
    l = 0
    sum_, maxi = 0, 0
    freq = {}

    for r in range(len(nums)):
        sum_ += nums[r]
        freq[nums[r]] = freq.get(nums[r], 0) + 1

        if r - l + 1 == k:
            if len(freq) == k:
                maxi = max(maxi, sum_)
            sum_ -= nums[l]
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                del freq[nums[l]]
            l += 1

    return maxi