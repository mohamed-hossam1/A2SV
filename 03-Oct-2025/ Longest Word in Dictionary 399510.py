# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()                 
        visited = {""}               
        res = ''
        
        for word in words:
            if word[:-1] in visited:   
                visited.add(word)  
                if len(word) > len(res): 
                    res = word         
        
        return res