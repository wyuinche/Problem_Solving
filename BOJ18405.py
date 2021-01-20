from collections import deque

N, K = map(int, input().split())

graph = []
for i in range(N):
    graph.append([0] + list(map(int, input().split())))

S, X, Y = map(int, input().split())
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
graph = [[0] * (N+1)] + graph
queue = [deque() for _ in range(K+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 0:
            continue
        queue[graph[i][j]].append((0, i, j))

for t in range(S):
    for v in range(1, K+1):
        while queue[v]:
            time, x, y = queue[v].popleft()
            if t == time:
                for m in move:
                    nx, ny = x+m[0], y + m[1]
                    if nx < 1 or ny < 1 or nx > N or ny > N:
                        continue
                    else:
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = v
                            queue[v].append((t+1, nx, ny))
            else:
                queue[v].appendleft((time, x, y))
                break
                
print(graph[X][Y])