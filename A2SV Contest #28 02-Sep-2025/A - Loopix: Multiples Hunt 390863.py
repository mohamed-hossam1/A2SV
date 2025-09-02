# Problem: A - Loopix: Multiples Hunt - https://codeforces.com/gym/632067/problem/A

for _ in range(int(input())):
    l, r, k = map(int ,input().split())
    x = (r//k)
    if(x < l):
        print(0)
    else:
        print(x-l+1)