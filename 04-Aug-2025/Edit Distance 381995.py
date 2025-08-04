# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1); m=len(word2)
        @cache
        def dp(i, j):
            if i<0 and j<0:
                return 0
            if i<0:
                return j+1
            if j<0:
                return i+1
            cost=1
            if word1[i]==word2[j]:
                cost=0
            
            return min(dp(i, j-1)+1, dp(i-1, j)+1, dp(i-1, j-1)+cost)
        return dp(n-1, m-1)