# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

# example below, replace it with your solution
n = int(input())
ans = []
for x in range(n):
    l = list(map(int, input().split()))
    p = [0]*n
    for i in range(1,len(l)):
        p[l[i]-1] = 1
    ans.append(p)

for l in ans:
    for x in l:
        print(x,end=" ")
    print()
    
