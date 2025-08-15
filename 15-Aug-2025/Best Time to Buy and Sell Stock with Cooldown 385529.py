# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
    
        @lru_cache(None)
        def dp(target: int, res = 0)->int:
       
            for n in nums:
            
                if n == target: res+= 1
                if n <  target: res+= dp(target-n)

            return res    

        return  dp(target)