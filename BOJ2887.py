from sys import stdin
import heapq

n = int(input())
x = []
y = []
z = []

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
    
x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
    heapq.heappush(edges, (x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    heapq.heappush(edges, (y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    heapq.heappush(edges, (z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))
    

parent = [x for x in range(n)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
        
answer = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    pa, pb = find(parent, a), find(parent, b)
    if pa != pb:
        answer += cost
        union(parent, pa, pb)
            
print(answer)