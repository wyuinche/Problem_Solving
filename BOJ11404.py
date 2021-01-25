from sys import stdin

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, stdin.readline().rstrip().split())
    graph[a][b] = min(graph[a][b], c)
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

if n == 1:
    print(0)
else:
    for g in graph[1:]:
        for j in g[1:]:
            if j == INF:
                print(0, end=" ")
            else: print(j, end=" ")
        print()
    
