import heapq


n, m = map(int, input().split())
graph = []
parent = [x for x in range(n)]
total = 0
answer = 0
count = 0

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(graph, (z, x, y))
    total += z
    
while graph:
    if count == n-1:
        break
    cost, a, b = heapq.heappop(graph)
    pa, pb = find(parent, a), find(parent, b)
    if pa != pb:
        union(parent, pa, pb)
        answer += cost
        count += 1
            
print(total - answer)