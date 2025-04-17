# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

class Solution(object):
    def reverseList(self, head):
        pre = None 
        now = head 
        while now:
            now_node = now.next
            now.next = pre
            pre =now
            now = now_node
        return pre