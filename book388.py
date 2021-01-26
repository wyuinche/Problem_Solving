from collections import deque

t = int(input())
INF = int(1e9)
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def cost(graph, dist, n):
    que = deque()
    que.append((0, 0, graph[0][0]))
    dist[0][0] = graph[0][0]
    
    while que:
        x, y, c = que.popleft()
        for m in move:
            nx, ny = x + m[0], y + m[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if dist[nx][ny] > c + graph[nx][ny]:
                dist[nx][ny] = c + graph[nx][ny]
                que.append((nx, ny, dist[nx][ny]))
    return dist[n-1][n-1]

result = []
for _ in range(t):
    n = int(input())
    graph = []
    dist = [[INF] * (n) for _ in range(n)]
    for __ in range(n):
        graph.append(list(map(int, input().split())))
        
    result.append(cost(graph, dist, n))
    
for r in result:
    print(r)