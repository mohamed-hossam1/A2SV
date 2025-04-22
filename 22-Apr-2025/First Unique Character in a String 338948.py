# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution(object):
    def firstUniqChar(self, s):
        mp = defaultdict(int)
        for c in s: mp[c]+=1
        for i in range(len(s)):
            if mp[s[i]]==1:
                return i
        return -1
        