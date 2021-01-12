import heapq
from sys import stdin

INF = int(1e9)
n, m, c = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y, z = map(int, stdin.readline().rstrip().split())
    graph[x].append((y, z))

queue = []
heapq.heappush(queue, (0, c))

while queue:
    cost, src = heapq.heappop(queue)
    for dst in graph[src]:
        ndst, ncost = dst
        if distance[ndst] > cost + ncost:
            distance[ndst] = cost + ncost
            heapq.heappush(queue, (distance[ndst], ndst))

resultList = [x for x in distance if x != INF]
print(len(resultList), max(resultList))
