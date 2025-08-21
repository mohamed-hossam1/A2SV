# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i,curr_total):
            # Base cases
            if curr_total == 0:
                return 1  
            if i == len(coins) or curr_total < 0:
                return 0  

            res = dp(i + 1, curr_total)

            if curr_total >= coins[i]:
                res += dp(i, curr_total - coins[i])

            return res

        return dp(0, amount)
