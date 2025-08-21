# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
            i = 0
            j = 0
            if s=="":
                return True
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i+= 1
                j+= 1
            return i == (len(s))