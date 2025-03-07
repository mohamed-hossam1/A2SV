# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)==len(goal):
            goal+=goal
            if goal.find(s)!=-1:
                return True
        return False

            
        