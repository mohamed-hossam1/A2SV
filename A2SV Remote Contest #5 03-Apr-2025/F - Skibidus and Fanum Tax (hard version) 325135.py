# Problem: F - Skibidus and Fanum Tax (hard version) - https://codeforces.com/gym/592318/problem/F

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())
d=1000000000000000000
def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b.sort()
    c=-d
    f=1
    for i in range(n):
        v=d
        if a[i]>=c:v=a[i]
        x=c+a[i]
        l,r=0,m-1
        while l<=r:
            mid=(l+r)//2
            if b[mid]>=x:
                r=mid-1
            else:
                l=mid+1
        
        if l<m:
            v=min(v,b[l]-a[i])
        if v==d:
            f=0
            break
        c=v
        
    print("YES"if f else"No")
t = 1
t = int(input())
for test in range(1, t + 1):
    solve()