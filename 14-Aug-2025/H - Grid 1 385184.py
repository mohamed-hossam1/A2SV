# Problem: H - Grid 1 - https://atcoder.jp/contests/dp/tasks/dp_h

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
from queue import PriorityQueue 
import math

def solve():
    ro, co = map(int, input().split())
    mod = 10**9 + 7

    dp = [[0] * (co) for _ in range(ro)]
    dp[0][0] = 1

    for i in range(ro):
        s = input().strip()
        for j in range(co):
            if s[j] == '.':
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                    dp[i][j] %= mod
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                    dp[i][j] %= mod
            else:
                dp[i][j] = 0

    print(dp[ro-1][co-1] % mod)

t = 1
t = int(input())
for test in range(1, t + 1):
    solve()
