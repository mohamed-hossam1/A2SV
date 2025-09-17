# Problem: Check If It Is a Good Array - https://leetcode.com/problems/check-if-it-is-a-good-array/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = nums[0]
        for i in range(1, len(nums)):
            g = math.gcd(g, nums[i])
        return g == 1


