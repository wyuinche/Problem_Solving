from collections import deque


def escape(graph, n_, m_):
    move = [(0, 1), (1, 0)]
    queue = deque([(1, 1, 1)])
    while queue:
        x, y, c = queue.popleft()
        for change in move:
            nx, ny = x + change[0], y + change[1]
            if not (nx < 1 or nx > n or ny < 1 or ny > m):
                if graph[nx][ny] > c + 1 or graph[nx][ny] == 1:
                    graph[nx][ny] = c + 1
                    queue.append((nx, ny, c + 1))
    return graph[n_][m_]


n, m = map(int, input().split())
map = [[-1] * (n+1)]
for i in range(n):
    map.append([-1] + list([int(x) for x in list(input())]))


print(escape(map, n, m))