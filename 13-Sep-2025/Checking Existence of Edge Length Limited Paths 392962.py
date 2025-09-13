# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        par = [i for i in range(n)]
        rank = [1]*(n)
        def find(node):
            res= node
            while res != par[res]:
                par[res] = par[par[res]]
                res =  par[res]
            return res
        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 ==p2:
                return 0
            elif rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1

        for i, q in enumerate(queries):
            queries[i].append(i)
        def sorter(val):
            return val[2]
        queries.sort(key=sorter)
        edgeList.sort(key=sorter)

        i = 0
        res = [False] * len(queries)
        for q in queries:
            while i < len(edgeList) and edgeList[i][2] < q[2]:
                union(edgeList[i][0], edgeList[i][1])
                i += 1

            if find(q[0]) == find(q[1]):
                res[q[3]] = True

        return res        
        