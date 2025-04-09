# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_len=0
        s=s.split()
        max_len=max(len(word) for word in s)
        l1=["" for i in range(max_len) ]
        c=0
        for i in range(len(s)):
                for j in range(len(s[i])):
                        l1[j]+=s[i][j]
                        c+=1
                for k in range(c,len(l1)):
                        l1[k]+=" "
                c=0
        for i in range(len(l1)):
                l1[i]=l1[i].rstrip()
        return(l1)
                