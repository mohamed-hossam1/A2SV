# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):

        
        ans, tmp = head, head
        while tmp and tmp.next:
            tmp = tmp.next.next
            ans = ans.next
            
        return ans