# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        ans = [intervals[0]]
        for l,r in intervals[1:]:
            tmp = ans[-1][1]
            if l<=tmp:
                ans[-1][-1] = max(tmp,r)
            else:
                ans.append([l,r])
        
        return(ans)

            
