# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, des, c in times:
            graph[src-1].append((c, des-1))
        dist = [float("inf")] * n
        dist[k-1] = 0
        q = [(0,k-1)]
        while q:
            cost, node = heapq.heappop(q)
            if cost > dist[node]:
                continue


            for newc, nei in graph[node]:
                if newc + cost < dist[nei]:
                    dist[nei] = newc + cost
                    heapq.heappush(q, (newc+cost, nei))

        return max(dist) if max(dist) != float("inf") else -1
        # Time O(E + VlogV)
        # Space O(E + v)