# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        cur1=l1
        cur2=l2
        while cur1:
            a.append(cur1.val)
            cur1=cur1.next
        while cur2:
            b.append(cur2.val)
            cur2=cur2.next
        a.reverse()
        b.reverse()
        a=int("".join(map(str, a)))
        b=int("".join(map(str, b)))
        c=str(a+b)
        c=[int(i) for i in c ]
        c.reverse()
        dummy=ListNode(0)
        cur=dummy
        for i in c:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next