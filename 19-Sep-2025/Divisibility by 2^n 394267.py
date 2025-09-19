# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D


def l(x):
    return 0 if x & 1 else l(x // 2) + 1
t = int(input())
for _ in range(t):
    n = int(input())
    p2 = sum(l(x) for x in map(int, input().split()))
    op = 0
    for j in sorted(map(l, range(1, n + 1)))[::-1]:
        if p2 >= n:
            break
        p2 += j
        op += 1
    if p2 >= n:
        print(op)
    else:
        print(-1)
