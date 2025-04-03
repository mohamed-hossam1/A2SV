# Problem: E - Robin and Ice hockey - https://codeforces.com/gym/592318/problem/E

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())
def solve():
    s = [input(), input()]
    n = int(input())
    ans = [[0] * 101 for i in range(2)]
    
    for i in range(n):
        a = input().split()
        q = 0
        p = 0
        
        if a[3] == 'y': q = 1
        else: q = 2
    
        if a[1] == 'h': p = 0
        else: p = 1
    
        if ans[p][int(a[2])] >= 2: continue
    
        ans[p][int(a[2])] += q
    
        if ans[p][int(a[2])] >= 2:
            print(s[p] + ' ' + a[2] + ' ' + a[0])

t = 1
# t = int(input())
for test in range(1, t + 1):
    solve()