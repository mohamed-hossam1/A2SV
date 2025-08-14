# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
from queue import PriorityQueue 
import math

def solve():
    n, w = map(int, input().split())
    weight = []
    value = []
    for _ in range(n):
        wi, vi = map(int, input().split())
        weight.append(wi)
        value.append(vi)

    max_val = sum(value)
    INF = 10**18
    dp = [INF] * (max_val + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(max_val - value[i], -1, -1):
            dp[j + value[i]] = min(dp[j + value[i]], dp[j] + weight[i])

    ans = -10**18
    for i in range(max_val + 1):
        if dp[i] <= w:
            ans = max(ans, i)

    print(ans)

t = 1
t = int(input())
for test in range(1, t + 1):
    solve()
