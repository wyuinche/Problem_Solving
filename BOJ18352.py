from collections import deque
from sys import stdin


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
move = deque([(x, 0)])
result = []
visited = [False] * (n+1)


for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)


while move:
    p, c = move.popleft()
    if visited[p]:
        continue
    visited[p] = True
    if c == k:
        result.append(p)
    if c >= k:
        continue
    for x in graph[p]:
        if not visited[x]:
            move.append((x, c+1))

if not result:
    print(-1)
else:
    result.sort()
    for r in result:
        print(r)