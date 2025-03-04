# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution(object):
    def targetIndices(self, nums, target):
        les,big=0,0
        for i in range(len(nums)):
            if nums[i]>target:
                big+=1
            elif nums[i]<target:
                les+=1
        ans = []
        i = les
        count = len(nums)-(les+big)
        while count:
            ans.append(i)
            i+=1
            count-=1
        return ans