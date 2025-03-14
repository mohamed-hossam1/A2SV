# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

def compare(a,b):
    if len(a)>len(b):
        return -1
    elif len(a)<len(b):
        return 1
    if a > b:
        return -1  
    elif a < b:
        return 1  
    
    return 0  
class Solution(object):

    def kthLargestNumber(self, nums, k):
        
        nums = sorted(nums, key=cmp_to_key(compare))
        return(nums[k-1])