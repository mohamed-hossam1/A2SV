# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/


def find(s,val,v):
    l,r,ans = 0,len(v)-1,"-1"
    while l<=r:
        mid = (l+r)//2
        if v[mid]>=val:
            r=mid-1
            ans = v[mid]
        else:
            l=mid+1
    return ans

class Solution(object):
    def findRightInterval(self, intervals):
        v = []
        mp = {"-1": -1}
        i = 0 
        ans = []
        for s,e in intervals:
            v.append(s)
            mp[s]=i
            i+=1
        v.sort()
        for s,e in intervals:
            val = find(s,e,v)
            ans.append(mp[val])
        return ans
        

        