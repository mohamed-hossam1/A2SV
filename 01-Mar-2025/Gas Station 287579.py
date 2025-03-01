# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start = 0 
        have = 0
        must = 0 
        for i in range(len(gas)):
            have += gas[i]-cost[i]
            if have < 0:
                start = i+1
                must+=have
                have = 0
        if have+must>=0:
            return start
        else:
            return -1