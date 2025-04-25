# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.s = []
        self.m = None

    def push(self, a):
        s = self.s

        if not s:
            self.m = a
            s.append(a)
        elif a >= self.m:
            s.append(a)
        else:
            s.append(2*a - self.m)
            self.m = a

    def pop(self):
        s = self.s

        if s[-1] < self.m:
            self.m = 2*self.m - s[-1]
        
        s.pop()
        

    def top(self):
        if not self.s:
            return -1
        elif self.s[-1] >= self.m:
            return self.s[-1]
        
        return self.m

    def getMin(self):
        return self.m

