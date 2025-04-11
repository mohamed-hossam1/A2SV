# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution(object):
    def findAnagrams(self, s, p):
        mp_s = defaultdict(int)
        mp_p = defaultdict(int)
        for i in p:
            mp_p[i] += 1

        l=0
        r=0
        ans = []
        
        while r<len(s):
        
            mp_s[s[r]]+=1
            if r-l+1>len(p):
                mp_s[s[l]]-=1
                if mp_s[s[l]] == 0:
                    del mp_s[s[l]]
                l+=1
        
            if r-l+1==len(p):
                if mp_s==mp_p:
                    ans.append(l)
            r+=1
            
        return ans