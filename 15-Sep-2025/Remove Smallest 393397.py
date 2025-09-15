# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

def can_reduce_to_one(n, a):
    a.sort()
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) > 1:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if can_reduce_to_one(n, a):
        print("YES")
    else:
        print("NO")