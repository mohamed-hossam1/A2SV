# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        freq = defaultdict(int)
        for i, char in enumerate(word):
            if char in "aeiou":
                if not i or word[i - 1] not in "aeiou":
                    x = y = i
                    freq.clear()
                freq[char] += 1
                while len(freq) == 5 and all(freq.values()):
                    freq[word[y]] -= 1
                    y += 1
                ans += y - x
        return ans