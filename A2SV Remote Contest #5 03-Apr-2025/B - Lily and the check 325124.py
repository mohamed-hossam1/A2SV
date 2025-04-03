# Problem: B - Lily and the check - https://codeforces.com/gym/592318/problem/B

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())


def solve():
    x, y = map(int, input().split())
    ans = y % x
    temp = y // x

    while temp > 0:
        ans += temp % 10
        temp //= 10
    print(ans)


t = 1
t = int(input())
for test in range(1, t + 1):
    solve()