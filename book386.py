from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
for i in range(1, n+1):
    indegree[i] = len(graph[i])
    
inNode = [[] for _ in range(n+1)]
outNode = [[] for _ in range(n+1)]
for i in range(1, n+1):
    for node in graph[i]:
        inNode[node].append(i)
        outNode[i].append(node)
        
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    cur = q.popleft()
    
    for i in range(1, n+1):
        if cur in inNode[i]:
            for node in outNode[i]:
                if cur not in inNode[node]:
                    inNode[node].append(cur)
                    
    for i in range(1, n+1):
        if cur in outNode[i]:
            for node in inNode[i]:
                if cur not in inNode[node]:
                    outNode[node].append(cur)
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

count = 0
for i in range(1, n+1):
    if len(inNode[i]) + len(outNode[i]) == n - 1:
        count += 1

print(count)
            