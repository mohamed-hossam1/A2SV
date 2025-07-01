# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

from collections import defaultdict
t = int(input())
dic = defaultdict(list)
col = 1
for _ in range(t):
        arr= list(map(int,input().split()))
        for i in range(1, t+1):
                if arr[i-1] == 1:
                    dic[min(col,i)].append(max(col,i))
        col += 1
ans= 0
for i,value in dic.items():
       ans += (len(set(value)))
print(ans)
       