# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        
        if Counter(s)==Counter(t):
            return True
        else:
            return False    

        