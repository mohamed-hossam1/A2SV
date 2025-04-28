# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans=0
        for i in range(len(tickets)):
            if tickets[i]>=tickets[k]:
                ans+=tickets[k]
                if i>k:
                    ans-=1
            else:
                ans+=tickets[i]
        return ans