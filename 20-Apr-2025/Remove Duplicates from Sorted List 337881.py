# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        val = head.val
        cur = head
        while cur.next:
            if cur.next.val==val:
                cur.next = cur.next.next
            else:
                val=cur.next.val
                cur = cur.next
        return head
            
        