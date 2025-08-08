# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @cache
        def dp(x):
            if x == 0:
                return 0
            if x < 0:
                return float('inf') 
            return min(dp(x - coin) + 1 for coin in coins)

        res = dp(amount)
        return res if res != float('inf') else -1

        
        

        