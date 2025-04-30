# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def helper(self, a, b, mod=1337):
        if b == 0:
            return 1
        half = self.helper(a, b // 2, mod)
        half = (half * half) % mod
        if b % 2 == 1:
            half = (half * (a % mod)) % mod
        return half % mod

    def superPow(self, a: int, b: List[int]) -> int:
        b=int("".join(map(str,b)))
        return self.helper(a,b)