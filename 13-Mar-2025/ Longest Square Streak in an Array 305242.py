# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution(object):
    def longestSquareStreak(self, nums):
        mp = defaultdict(int)
        for i in nums:
            mp[i]+=1
        count = 0
        for i in nums:
            tmp = i
            c = 1
            # if tmp != int(tmp) or mp[tmp]==0:
            while mp[tmp*tmp]!=0:
                tmp*=tmp
                c+=1
            count = max(c,count)
        if count==1:
            return -1
        else:
            return count
        