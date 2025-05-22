# Problem: Remove Nodes From Linked List - https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=problem-list-v2&envId=recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            
            stack.append(curr.val)
            curr = curr.next
        dummy = ListNode(0)
        curr = dummy
        for num in stack:
            temp = ListNode(num)
            curr.next = temp
            curr = curr.next
        return dummy.next
        