# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        def help(i):
            if i==len(nums):
                ans.append(arr[:])
                return 
            
            arr.append(nums[i])
            help(i+1)

            arr.pop()
            help(i+1)

        help(0)
        return(ans)