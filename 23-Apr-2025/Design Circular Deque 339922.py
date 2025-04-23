# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None]*k
        self.size = 0
        self.k = k
        self.i = k//2
        self.j = k//2

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.i]=value
        self.i = (self.i-1) % self.k
        if self.size==0:
            self.j = (self.j+1) % self.k
        self.size+=1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.j]=value
        self.j = (self.j+1) % self.k
        if self.size==0:
            self.i = (self.i-1) % self.k
        self.size+=1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.i = (self.i+1) % self.k
        self.size-=1
        if self.size==0:
            self.i=self.j
        return True

        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.j = (self.j-1) % self.k
        self.size-=1
        if self.size==0:
            self.i=self.j
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.deque[(self.i+1)% self.k]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.deque[(self.j-1)% self.k]

        

    def isEmpty(self) -> bool:
        return (self.size==0)
        

    def isFull(self) -> bool:
        return (self.size==self.k)
        
