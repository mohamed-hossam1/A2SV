# Problem: Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = n-1
        k = m+n-1
        while True:
            if i>-1 and j>-1:
                if nums1[i]>nums2[j]:
                    nums1[k]=nums1[i]
                    i-=1
                else:
                    nums1[k]=nums2[j]
                    j-=1
            elif i>-1:
                nums1[k]=nums1[i]
                i-=1
            elif j>-1:
                nums1[k]=nums2[j]
                j-=1
            else:
                break
            k-=1



        