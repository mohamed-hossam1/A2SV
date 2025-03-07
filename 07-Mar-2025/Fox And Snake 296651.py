# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())

def p3(n):
    s = '.'*(n-1)
    print("#"+s)

def p1(n):
    s = '#'*(n)
    print(s)

def p2(n):
    s = '.'*(n-1)
    print(s+'#')

def solve():
    x,y = map(int, input().split())
    t = 0
    for i in range(x):
        if t==0: p1(y)
        if t==1: p2(y)
        if t==2: p1(y)
        if t==3: p3(y)
        
        t = (t+1)%4
        
    
    
    

    
    
t = 1
# t = int(input())
for test in range(1, t + 1):
    solve()