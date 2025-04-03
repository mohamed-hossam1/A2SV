# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        left = ans = tally = 0
        n, d = len(nums), defaultdict(int)

        for right,num in enumerate(nums):   
            tally += d[num]
            d[num] += 1
            
            while tally >= k:           
                ans+= n - right
                d[nums[left]] -= 1       
                tally -= d[nums[left]]
                left += 1
            
        return ans               