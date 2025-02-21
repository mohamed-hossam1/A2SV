# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        mp = {}
        for i in range(len(s)):
            mp[indices[i]] = s[i]
        
        ans = ""

        for i in range(len(s)):
            ans = ans + mp[i]
            
        return ans
            
        