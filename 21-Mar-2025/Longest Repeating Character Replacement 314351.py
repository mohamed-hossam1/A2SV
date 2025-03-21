# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        fre = [0] * 26 
        l = 0
        mfre = 0 
        ans = 0

        for r in range(len(s)):
            fre[ord(s[r]) - ord('A')] += 1
            mfre = max(mfre, fre[ord(s[r]) - ord('A')])
            while (r - l + 1) - mfre > k:
                fre[ord(s[l]) - ord('A')] -= 1
                l += 1

            ans = max(ans, r  - l + 1)

        return ans

        
