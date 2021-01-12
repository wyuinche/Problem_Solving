INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[1][k] == INF or graph[k][x] == INF or graph[1][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])