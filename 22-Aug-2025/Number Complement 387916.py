# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        new = 0
        i = 0
        while num > 0:
            new += (num + 1) % 2 * 2**i
            num //= 2
            i += 1
        return new