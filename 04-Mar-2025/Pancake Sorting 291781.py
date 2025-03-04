# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

def flip(arr,k):
    for i in range(k//2):
        arr[i],arr[k-i-1] = arr[k-i-1],arr[i]
    return arr
class Solution(object):
    def pancakeSort(self,arr):
        ans = []
        for i in range(len(arr)):
            maxi = 0
            for j in range(len(arr)-i):
                if arr[j]>arr[maxi]:
                    maxi = j
            flip(arr,maxi+1)
            flip(arr,len(arr)-i)
            ans.append(maxi+1)
            ans.append(len(arr)-i)
        return ans
        