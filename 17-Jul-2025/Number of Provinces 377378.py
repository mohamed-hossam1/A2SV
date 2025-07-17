# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        for i in range(n):
            if not visited[i]:
                queue = [i]
                visited[i] = True
                self.bfs1(isConnected, queue, visited)
                province_count += 1

        return province_count


    def bfs1(self, isConnected: List[List[int]], queue: List[int], visited: List[bool]):
        if not queue:
            return

        city = queue.pop(0)
        next_queue = []

        for neighbor in range(len(isConnected)):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                next_queue.append(neighbor)

        self.bfs2(isConnected, queue, next_queue, visited)


    def bfs2(self, isConnected: List[List[int]], queue: List[int], next_queue: List[int], visited: List[bool]):
        if next_queue:
            queue.extend(next_queue)
        self.bfs1(isConnected, queue, visited)