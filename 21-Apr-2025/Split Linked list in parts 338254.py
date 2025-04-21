# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self,head, k):
        n = 0
        cur = head
        while cur:
            n+=1
            cur = cur.next
        mod = n%k
        count = n//k
        count+= 1 if mod else 0
        l = [head]
        tmp = 0
        cur = head
        pre = head
        while cur:
            tmp+=1
            if tmp == count+1:
                mod-=1
                if mod == 0:
                    count-=1
                tmp = 1
                pre.next = None
                l.append(cur)
            pre = cur
            cur = cur.next
        while len(l)<k:
            l.append(None)
        return l


            