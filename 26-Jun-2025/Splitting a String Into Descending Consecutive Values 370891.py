# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(i, acc):
            if i == len(s):
                return len(acc) >= 2

            for j in range(i, len(s)):
                val = int(s[i:j+1])
                if not acc or acc[-1] - val == 1:
                    acc.append(val)
                    if dfs(j+1, acc):
                        return True
                    acc.pop()
            return False
        
        return dfs(0, [])