# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

n= int(input())

sources=[n for n in range(1,n+1)]
sinks=[]
for i in range(1,n+1):
    row=list(map(int,input().split()))
    if max(row)==0: sinks.append(i) ; continue
    for j in range(n):
        if row[j]==1 and j+1 in sources: sources.remove(j+1)
print(len(sources)," ".join(map(str,sources)))
print(len(sinks)," ".join(map(str,sinks)))