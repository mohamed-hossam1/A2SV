# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True

    def find_root(self, word: str) -> str:
        cur = self.root
        prefix = []
        for ch in word:
            if ch not in cur.children:
                return word  
            cur = cur.children[ch]
            prefix.append(ch)
            if cur.is_end:
                return "".join(prefix) 
        return word   

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)

        return " ".join(self.find_root(word) for word in sentence.split())
