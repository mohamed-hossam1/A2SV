# Problem: Detect Cycle In An Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

class Solution:
    def isCycle(self, V, edges):
        from collections import defaultdict

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(u, parent):
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    if dfs(v, u):
                        return True
                elif v != parent:
                    return True
            return False

        for i in range(V):
            if i not in visited:
                if dfs(i, -1):
                    return True

        return False
