# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals):
        rs = 0
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        for interval in intervals:
            if interval[0] < end:
                rs += 1
            else:
                end = interval[1]
        return rs