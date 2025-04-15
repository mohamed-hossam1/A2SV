# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if self.size<= index:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

        

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size < index:
            return 
        
        cur = self.head
        node = Node(val)

        if index == 0:
            node.next = self.head
            self.head = node
        else:
            for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

        self.size+=1

        

    def deleteAtIndex(self, index: int) -> None:
        if self.size<= index:
            return 

        cur = self.head
        if index==0:
            self.head = self.head.next
        else:
            for i in range(index-1):
                cur = cur.next
            cur.next = cur.next.next

        self.size-=1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)