# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        ls = list(range(1,n+1))

        c = 0
        while n>1:
            c = (c+k-1)%n
            ls.pop(c)
            n-=1

        return ls[0]
        