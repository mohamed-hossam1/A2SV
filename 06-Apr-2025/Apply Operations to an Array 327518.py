# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] ==nums[i-1]:
                nums[i] =0
                nums[i-1] *=2
        res=[]
        for j in range(len(nums)):
            if nums[j] >0:
                res.append(nums[j])
        res.extend([0] * (len(nums) - len(res)))

        return res


        