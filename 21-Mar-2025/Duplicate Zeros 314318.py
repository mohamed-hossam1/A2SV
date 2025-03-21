# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zero = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zero < n:
                arr[i + zero] = arr[i]
            if arr[i] == 0: 
                zero -= 1
                if i + zero < n:
                    arr[i + zero] = 0