# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):

        count = [0]*26
        cur = [0]*26

        for c in s1:
            count[ord(c)-ord('a')]+=1

        l=0
        for r in range(len(s2)):

            cur[ord(s2[r])-ord('a')]+=1

            if r-l+1>len(s1):
                cur[ord(s2[l])-ord('a')]-=1
                l+=1
            
            if r-l+1==len(s1):
                if count==cur:
                    return True
                
        return False
            
        
        