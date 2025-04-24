# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.mp = defaultdict(int)
        self.deq = deque()
        

    def consec(self, num: int) -> bool:
        self.mp[num]+=1
        self.deq.append(num)
        if len(self.deq) == self.k+1:
            self.mp[self.deq.popleft()]-=1
        return self.mp[self.value]==self.k
        

