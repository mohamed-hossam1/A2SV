# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        l = 0
        mp = defaultdict(int)
        for r in range(len(s)):
            while mp[s[r]]>0:
                mp[s[l]]-=1
                l+=1
            mp[s[r]]+=1
            ans = max(ans,r-l+1)
        return ans

        