# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        idx = 0
        #up
        while idx + 1 < n and arr[idx] < arr[idx + 1]:
            idx += 1
        #peak
        if idx == 0 or idx == n - 1:
            return False
        #down
        while idx + 1 < n and arr[idx] > arr[idx + 1]:
            idx += 1
        return idx == n - 1