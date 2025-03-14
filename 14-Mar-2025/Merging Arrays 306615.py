# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
from queue import PriorityQueue 
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())



def solve():
    n,k = map(int, input().split())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    i,j = 0,0
    ans = []
    while i<n and j<k:
        if v1[i]<v2[j]:
            ans.append(v1[i])
            i+=1
        else:
            ans.append(v2[j])
            j+=1
    ans.extend(v1[i:])
    ans.extend(v2[j:])
    print(*ans)
    
    
    
    
    
    

    


    
    
t = 1
# t = int(input())
for test in range(1, t + 1):
    solve()