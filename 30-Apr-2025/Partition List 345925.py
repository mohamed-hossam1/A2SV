# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1,head2 = ListNode(0) ,ListNode(0) 
        cur1,cur2 = head1,head2
        while head:
            if head.val<x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
        cur2.next = None
        cur1.next = head2.next



        cur = head1.next
        while cur:
            print(cur.val,end=" ")
            cur = cur.next

        
        return head1.next
        