# Problem: B. Petr and a Combination Lock - https://codeforces.com/contest/1097/problem/B

n = int(input())
rotation = []
flag = False
for _ in range(n):
    deg = int(input())
    rotation.append(deg)


def backtrack(degree, cur):
    
    global flag, rotation
    if cur == n:
        if degree == 0:
            flag = True
        return 
    
    
    backtrack(degree + rotation[cur], cur + 1)
    backtrack((degree - rotation[cur] + 360)%360, cur + 1)
    

backtrack(0, 0)

if flag:
    print("YES")
else:
    print("NO")
