# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        while b!=0:
            a,b=b,a%b
        return a 
        