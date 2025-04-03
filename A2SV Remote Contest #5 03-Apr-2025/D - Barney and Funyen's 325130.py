# Problem: D - Barney and Funyen's - https://codeforces.com/gym/592318/problem/D

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())
def solve():
    n = int(input().strip())
    poi = list(map(int, input().split()))
    a, b, c, d, e = map(int, input().split())
    val = [(e, 4), (d, 3), (c, 2), (b, 1), (a, 0)]
    count = [0] * 5
    sum = 0
    
    for p in poi:
        sum += p
        
        for cost, idx in val:
            if sum >= cost:
                count[idx] += sum // cost 
                sum %= cost

    print(*count)
    print(sum)
    
    
t = 1
# t = int(input())
for test in range(1, t + 1):
    solve()