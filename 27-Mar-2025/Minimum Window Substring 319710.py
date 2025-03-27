# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

def map_in_map(mapt,maps):
    for i in range(ord('A'),ord('z')+1):
        if mapt[chr(i)]>maps[chr(i)]:
            return False
    return True

class Solution(object):
    def minWindow(self, s, t):
        l,r=0,0
        mapt = defaultdict(int)
        maps = defaultdict(int)
        
        for c in t:
            mapt[c]+=1
        
        ans = [len(s)+1,0]


        while l!=len(s):
            maps[s[l]]+=1
            if map_in_map(mapt,maps):
                while mapt[s[r]]<maps[s[r]]:
                    maps[s[r]]-=1
                    r+=1
                if ans[0]-ans[1]>l-r:
                    ans = [l,r]
            l+=1
            
        if ans!=[len(s)+1,0]:
            return(s[ans[1]:ans[0]+1])
        else:
            return ""

        
