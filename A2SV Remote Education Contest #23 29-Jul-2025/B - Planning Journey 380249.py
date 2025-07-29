# Problem: B - Planning Journey - https://codeforces.com/gym/625306/problem/B

t=int(input())
for _ in range(t):
 n,m=map(int,input().split())
 x=list(map(int,input().split()))
 y=0;z=0
 for i in x:
  if i==0:z+=1
  else:y+=(z+1)//(m+1);z=0
 y+=(z+1)//(m+1)
 print(y)