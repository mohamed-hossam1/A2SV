# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

import sys
input = lambda:sys.stdin.readline().rstrip()
RII = lambda: map(int, input().split())

s,n = RII()
drag = []
for _ in range(n):
  a,b = RII()
  drag.append((a,b))

drag.sort()
res = True
for a,b in drag:
  if s > a:
    s+=b
  else:
    res=False
    break
print('YES' if res else 'NO')
  