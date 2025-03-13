# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            k = nums[i]
            l,r = i+1,len(nums)-1
            while l<r:
                if k+nums[l]+nums[r]==0:
                    tmp = sorted([nums[i],nums[l],nums[r]])
                    if not tmp in ans:
                        ans.append(tmp)
                    r-=1
                    l+=1
                elif k+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return (ans)