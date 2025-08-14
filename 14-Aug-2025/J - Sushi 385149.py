# Problem: J - Sushi - https://atcoder.jp/contests/dp/tasks/dp_j

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
from queue import PriorityQueue 
import math
from functools import lru_cache

def solve():
    n = int(input())
    o = tw = th = 0
    arr = list(map(int, input().split()))
    for j in arr:
        if j == 1:
            o += 1
        elif j == 2:
            tw += 1
        else:
            th += 1

    @lru_cache(None)
    def fun(x, y, z):
        if x == 0 and y == 0 and z == 0:
            return 0.0
        if x < 0 or y < 0 or z < 0:
            return 0.0
        ans = n
        if x > 0:
            ans += x * fun(x - 1, y, z)
        if y > 0:
            ans += y * fun(x + 1, y - 1, z)
        if z > 0:
            ans += z * fun(x, y + 1, z - 1)
        return ans / (x + y + z)

    print(f"{fun(o, tw, th):.10f}")

t = 1
t = int(input())
for test in range(1, t + 1):
    solve()
