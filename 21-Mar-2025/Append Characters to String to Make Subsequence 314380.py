# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution(object):
    def appendCharacters(self, s, t):
        count = 0
        j = 0
        for i in range(len(s)):
            if s[i]==t[j]:
                j+=1
                count+=1
            if j==len(t):
                break
        return len(t) - count
        