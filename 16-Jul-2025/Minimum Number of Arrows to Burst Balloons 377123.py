# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        stack = [  ]
        for sp, ep in points:
            if len(stack)>0 and stack[-1][1] >= sp:
                last_sp, last_ep = stack.pop()
                stack.append( [max(sp, last_sp), min(ep, last_ep)] )
            else:
                stack.append([sp, ep])
        return len(stack)
        