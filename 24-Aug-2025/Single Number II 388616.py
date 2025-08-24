# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c= Counter(nums) 
        for i,x in c.items():
            if x == 1:
                return i