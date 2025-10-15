# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        ans = []
        f = lambda x: x.start()
        idxA, idxB  = map(f, re.finditer(a, s)), list(map(f, re.finditer(b, s)))

        for i in idxA:
            if bisect_left(idxB, i - k) == bisect_right(idxB, i + k): continue
            ans.append(i)
            
        return ans