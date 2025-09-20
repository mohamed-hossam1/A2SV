# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            l = 1
            for j in range(i, n):
                l = lcm(l, nums[j])
                if l == k:
                    count += 1
                elif l > k:   
                    break
        return count