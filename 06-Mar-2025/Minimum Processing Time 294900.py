# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = 0
        for i in range(len(processorTime)):
            l = max(tasks[i*4:i*4+4])
            ans = max(ans,processorTime[i]+l)
        return ans
        