# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/description/

class Solution(object):
    def hasCycle(self, head):
        """
        """

        current = head

        while current:
            if current.val == None:
                return True
            
            current.val = None
            current = current.next

        return False