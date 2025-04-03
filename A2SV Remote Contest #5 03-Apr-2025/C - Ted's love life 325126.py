# Problem: C - Ted's love life - https://codeforces.com/gym/592318/problem/C

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())
def solve():
 
    n=int(input())
 
    l=list(map(int,input().split()))
 
 
    m= int(input())
 
    lstr= list()
    for i in range(m):
        word=input()
        lstr.append(word)
 
    
 
    for i in lstr:
        d= dict()
        if len(i) != n:
            print("NO")
 
 
        else:
            for j in range(n):
                if l[j] not in d.keys():
                    if i[j] not in d.values():
                        d[l[j]]=i[j]
                    else:
                        print("NO")
                        break
                else:
                    if d[l[j]]!=i[j]:
                        print("NO")
                        break
            else:
                print("YES")

t = 1
t = int(input())
for test in range(1, t + 1):
    solve()