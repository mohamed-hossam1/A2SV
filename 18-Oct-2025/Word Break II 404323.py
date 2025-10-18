# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        
        @lru_cache(None)
        def dfs(start: int) -> List[str]:
            if start == len(s):
                return [""]  
            
            res = []
            for end in range(start + 1, len(s) + 1):
                w = s[start:end]
                if w in word_set:
                    rest = dfs(end)
                    for sent in rest:
                        if sent: 
                            res.append(w + " " + sent)
                        else:
                            res.append(w)
            return res
        
        return dfs(0)