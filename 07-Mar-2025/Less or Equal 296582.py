# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())



def solve():
    n,k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = -1
    v.sort()
    if k==0:
        if v[0]==1:
            print(-1)
        else:
            print(1)
        return

    if k!=len(v) and v[k-1]==v[k]:
        print(-1)
    else:
        print(v[k-1])
    
    
    

    
    
t = 1
# t = int(input())
for test in range(1, t + 1):
    solve()