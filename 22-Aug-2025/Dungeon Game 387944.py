# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])

       
        def extraHealth(r,c):
            if (r==m and c==n-1) or (r==m-1 and c==n): return 0
            if r==m or c==n: return float("inf")

            right =  extraHealth(r,c+1)
            down = extraHealth(r+1,c)

            return max(0,min(right,down)-dungeon[r][c])

        return 1 + extraHealth(0,0)