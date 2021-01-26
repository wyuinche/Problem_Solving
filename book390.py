from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
que = deque()
que.append((1, 0))
visited = [False] * (n + 1)
visited[1] = True
dist = [INF] * (n + 1)
dist[1] = 0

while que:
    x, c = que.popleft()
    
    for node in graph[x]:
        if not visited[node] and dist[node] > c + 1:
            dist[node] = c + 1
            visited[node] = True
            que.append((node, c + 1))
for i in range(len(dist)):
    if dist[i] == INF:
        dist[i] = 0
answerDist = max(dist)

print(dist.index(answerDist), end=" ")
print(answerDist, end=" ")
print(dist.count(answerDist))
