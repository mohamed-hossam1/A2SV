# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution(object):
    def removeStars(self, s):
        l = []
        for c in s:
            if c=='*':
                l.pop()
            else:
                l.append(c)
        return "".join(l)