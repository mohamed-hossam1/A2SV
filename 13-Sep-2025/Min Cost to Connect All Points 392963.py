# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)
        def getdist(i,j):
            x1,y1 = points[i]
            x2,y2 = points[j]
            return abs(x1-x2)+abs(y1-y2)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    adj[i].append((j,getdist(i,j)))
        nodes = set()
        minheap = []
        heapq.heapify(minheap)
        ans = 0
        for dst,distance in adj[0]:
            heapq.heappush(minheap,(distance,0,dst))
        nodes.add(0)

        while minheap:
            distance, src,dst = heapq.heappop(minheap)
            if dst in nodes:
                continue
            nodes.add(dst)
            ans+=distance
            for nei,dist in adj[dst]:
                if nei not in nodes:
                    heapq.heappush(minheap,(dist,dst,nei))
        return ans