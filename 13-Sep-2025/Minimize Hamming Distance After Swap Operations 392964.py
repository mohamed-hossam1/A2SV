# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

class Solution:
    def find(self, i):
        while self.pa[i] != i:
            i = self.pa[i]
        return i

    def uni(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        self.pa[pi] = pj

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        self.pa = [i for i in range(n)]
        for e in allowedSwaps:
            self.uni(e[0], e[1])

        d = defaultdict(dict)
        for i in range(n):
            p = self.find(i)
            if source[i] in d[p]:
                d[p][source[i]] += 1
            else:
                d[p][source[i]] = 1

        ans = 0
        for i in range(n):
            p = self.find(i)
            if target[i] in d[p] and d[p][target[i]] > 0:
                d[p][target[i]] -= 1
            else:
                ans += 1

        return ans
        

        


            
        