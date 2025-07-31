# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution(object):
    def dividePlayers(self, skill):
        total = sum(skill)
        mp = Counter(skill)
        if (2*total)%len(skill)!=0:
            return -1
        res = 0
        target = (2*total)//len(skill)
        for i in skill:
            if not mp[i]:
                continue
            mp[i]-=1
            d = target-i
            if not mp[d]:
                return -1
            res+=i*d
            mp[d]-=1
        return res
            
        