# Problem: A - Marshall's Game - https://codeforces.com/gym/592318/problem/A

import heapq
import bisect
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
import math
# v = list(map(int, input().split()))
# n,k = map(int, input().split())
 
 
def solve():

    t = int(input())
    lst = list(map(int, input().split()))
    p = False
    for i in lst:
        if i == 1:
            print ("HARD")
            p = True
            return
    print ("EASY")


t = 1
# t = int(input())
for test in range(1, t + 1):
    solve()