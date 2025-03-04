# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        mp = {}
        mp[0]=mp[1]=mp[2]=0
        ans = []
        for i in nums:
            mp[i]+=1
        g = 0
        for i in range(3):
            for l in range(mp[i]):
                nums[g]=i
                g+=1
