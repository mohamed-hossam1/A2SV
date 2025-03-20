# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution(object):
    def totalFruit(self, fruits):
        ans = 0
        count = 0
        l = 0
        mp = defaultdict(int)
        for r in range(len(fruits)):
            if mp[fruits[r]]==0:
                count+=1
            if count==3:
                while True:
                    mp[fruits[l]]-=1
                    if mp[fruits[l]]==0:
                        count-=1
                        l+=1
                        break
                    l+=1
            mp[fruits[r]]+=1
            ans = max(ans,r-l+1)
        return ans