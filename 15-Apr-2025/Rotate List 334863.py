# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateOne(self, head):
        cur = head 
        while cur.next.next:
            cur = cur.next
        cur.next.next = head
        head = cur.next
        cur.next = None
        return head

    def rotateRight(self, head, k):
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size+=1
        if size ==1 or size ==0:
            return head
        
        k = k%size

        while k:
            head = self.rotateOne(head)
            k-=1
        return head


        