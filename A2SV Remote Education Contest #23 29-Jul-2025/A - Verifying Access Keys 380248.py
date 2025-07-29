# Problem: A - Verifying Access Keys - https://codeforces.com/gym/625306/problem/A

a=int(input())
for _ in range(a):
 b=int(input())
 c=input()
 d='0'
 e='a'
 f=0
 g=1
 for h in c:
  if h.isdigit():
   if f:g=0;break
   if h<d:g=0;break
   d=h
  else:
   if h<e:g=0;break
   e=h
   f=1
 print("YES"if g else"NO")