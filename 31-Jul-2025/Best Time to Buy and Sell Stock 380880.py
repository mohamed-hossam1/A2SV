# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        temp = 0
        count = 0
        left = 0
        right = left+1
        while right<len(prices):
            right = left+1
            while right<len(prices) and prices[left]<prices[right]:
                temp = prices[right] - prices[left]
                count = max(count,temp)
                right += 1
            left = right
        return count
                