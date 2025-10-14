# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

from math import gcd
from functools import reduce
import sys
def input(): return sys.stdin.readline().rstrip()
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rstr(): return input()
def rstrs(): return input().split()
def solve():
    n, m = rints()
    a = rints()
    b = rints()
    D = reduce(gcd, (abs(num - a[0]) for num in a))
    print(*[gcd(D, a[0] + bi) for bi in b])

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
