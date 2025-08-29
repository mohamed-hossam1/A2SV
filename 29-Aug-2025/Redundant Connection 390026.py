# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1)) 

    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u 
            return True
        return False  

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = DisjointSet(n)
        for u, v in edges:
            if not ds.union(u, v):
                return [u, v] 
        return []        