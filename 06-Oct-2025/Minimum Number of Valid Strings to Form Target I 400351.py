# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

class Trie:
    def __init__(self, words):
        self._d = {}
        for word in words:
            self._add_word(word)
    
    def _add_word(self, word):
        d = self._d
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
    
    def get_max_length(self, target, i):
        d = self._d
        result = 0
        for j in range(i, len(target)):
            next_d = d.get(target[j])
            if next_d is None:
                break
            d = next_d
            result += 1
        return result

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        trie = Trie(words)

        @cache
        def dp(i):
            if i == n:
                return 0
            
            max_length = trie.get_max_length(target, i)
            if i + max_length == n:  
                return 1
            
            result = float('inf')
            for length in range(max_length, 0, -1):
                current = 1 + dp(i + length)
                if current == 2: 
                    return 2
                result = min(result, current)
            return result

        result = dp(0)
        return -1 if result == float('inf') else result