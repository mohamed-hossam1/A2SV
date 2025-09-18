# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory


def prime(n):
    k = int(math.sqrt(n))
    for i in range(2,k+1):
        if n%i==0:
            return False
    return True

class Solution:
    def isThree(self, n: int) -> bool:
        if n==1:
            return False
        d = math.sqrt(n)
        if d==int(d) and prime(d):
            return True
        else:
            return False
        