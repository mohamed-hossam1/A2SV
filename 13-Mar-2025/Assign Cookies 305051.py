# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0
        j=0
        for i in g:
            while j<len(s) and s[j]<i:
                j+=1
            if j<len(s) and i<=s[j]:
                count+=1
                j+=1
        return count
        