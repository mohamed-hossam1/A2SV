# Problem: C - Sort - https://codeforces.com/gym/625306/problem/C

t=int(input())
for _ in range(t):
 a,b=map(int,input().split())
 c=list(map(int,input().split()))
 d=[i+c[i-1]for i in range(1,a+1)]
 d.sort()
 e=0
 for f in d:
  if f<=b:b-=f;e+=1
  else:break
 print(e)