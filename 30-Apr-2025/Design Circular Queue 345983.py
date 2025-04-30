# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q=deque()
        self.k=k

    def enQueue(self, value: int) -> bool:
        if self.k>0:
            self.q.append(value)
            self.k-=1
            return True
        return False

    def deQueue(self) -> bool:
        if self.q:
            self.q.popleft()
            self.k+=1
            return True
        return False

    def Front(self) -> int:
        if self.q:
            return self.q[0]
        return -1

    def Rear(self) -> int:
        if self.q:
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        if not self.q:
            return True
        return False

    def isFull(self) -> bool:
        if self.k==0:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()