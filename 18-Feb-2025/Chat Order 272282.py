# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
 
 
def solve():
    x = int(input())
    ls = [input() for _ in range(x)]
    mp = defaultdict(int)
    for i in range(x-1,-1,-1):
        if mp[ls[i]]==0:
            print(ls[i])
        mp[ls[i]] = 1
    
    
        
                
        
        
 
 
        
    
      
    
 
t = 1
# t = int(input())
for test in range(1, t + 1):
    solve()
