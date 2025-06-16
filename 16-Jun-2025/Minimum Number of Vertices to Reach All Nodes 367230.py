# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        indegree = [0] * n
        for edge in edges:
            indegree[edge[1]] += 1

        ans = []
        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)

        return ans