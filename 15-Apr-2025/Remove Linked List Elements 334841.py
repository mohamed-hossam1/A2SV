# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        previous = None
        
        while head and head.val == val:
            head = head.next
        current = head
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return head
        
