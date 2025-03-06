# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self, piles):
        i = 1
        l = len(piles)-1
        ans = 0
        piles.sort(reverse=True)
        while i<l:
            ans+=piles[i]
            l-=1
            i+=2
        return ans

        