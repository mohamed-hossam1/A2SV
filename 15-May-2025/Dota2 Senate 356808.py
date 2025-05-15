# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        mp = defaultdict(int)
        for c in senate:
            mp[c]+=1
        r,d=0,0
        i = 0
        while mp['R']>0 and mp['D']>0:
            if senate[i]=='R':
                if d>0:
                    d-=1
                    senate[i]='q'
                    mp['R']-=1
                else:
                    r+=1
            elif senate[i]=='D':
                if r>0:
                    r-=1
                    senate[i]='q'
                    mp['D']-=1
                else:
                    d+=1
            i = (i+1)%len(senate)
        if mp['R']==0:
            return("Dire")
        else:
            return("Radiant")