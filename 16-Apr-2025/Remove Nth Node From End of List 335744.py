# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	ptr, length = head, 0
	while ptr:
		ptr, length = ptr.next, length + 1
	if length == n : return head.next
	ptr = head
	for i in range(1, length - n):
		ptr = ptr.next
	ptr.next = ptr.next.next
	return head