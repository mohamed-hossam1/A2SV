# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict
n = int(input())
t = int(input())
dic = defaultdict(list)
for _ in range(t):
        arr= list(map(int,input().split()))
        if arr[0]== 1:
                dic[arr[1]].append(arr[2])
                dic[arr[2]].append(arr[1])

        else:
            if dic[arr[1]] != []:
                print(*dic[arr[1]])
                


