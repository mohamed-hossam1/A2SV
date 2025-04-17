# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow, fast = head, head
        ans = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr, prev = slow, None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next   

        while prev:
            ans = max(ans, head.val + prev.val)
            prev = prev.next
            head = head.next

        return ans