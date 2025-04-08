# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        mp = {'a':0,'b':0,'c':0}
        i=0
        for c in s:
            mp[c]+=1
            while mp['a']>=1 and mp['b']>=1 and mp['c']>=1:
                mp[s[i]]-=1
                i+=1
            ans+=i
        cccccccab

        
            

