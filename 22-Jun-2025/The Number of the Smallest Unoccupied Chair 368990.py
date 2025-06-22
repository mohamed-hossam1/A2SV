# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n=len(times)
        heap=[]
        for i in range(n):
            times[i]=times[i]+[i]
        times.sort()
        temp=defaultdict(list)
        start=defaultdict(list)
        j=float('inf')
        k=0
        for i in range(n):
            heapq.heappush(heap,i)
            j=min(times[i][0],j)
            k=max(times[i][1],k)
            start[times[i][0]].append((times[i][1],times[i][2]))
    
        for i in range(j,k+1):
            if len(temp[i])>0:
                for val in temp[i]:
                    heapq.heappush(heap,val)
            if len(start[i])>0:
                a=start[i]
                hold=heapq.heappop(heap)
                if a[0][1]==targetFriend:
                     return hold
                temp[a[0][0]].append(hold)
          
        return n