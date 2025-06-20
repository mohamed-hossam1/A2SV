# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    arr = [0]
    for j in range(n):
        if a[j]==1:
            arr[0]+=1
            arr.append(j+1)
    print(*arr)