# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

def lastStoneWeightII(self, stones: List[int]) -> int:
    def f(stonesSorted):
        if not stonesSorted:
            return 0
        if len(stonesSorted) == 1:
            return stonesSorted[0]
        res = float("inf")
        for i in range(len(stonesSorted) - 1):
            for j in range(i + 1, len(stonesSorted)):
                stonesList = list(stonesSorted)
                si = stonesList.pop(i)
                sj = stonesList.pop(j - 1) 
                stonesList.append(sj - si)
                stonesList.sort()
                res = min(res, f(tuple(stonesList)))
        return res
    return f(tuple(sorted(stones)))