move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())


graph = []

for _ in range(n):
    graph.append([int(x) for x in list(input())])
    

def howManyIce(graph):
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                answer += 1
                marking(i, j)
    return answer


def marking(x, y):
    for i in range(4):
        nx, ny = x + move[i][0], y + move[i][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            marking(nx, ny)


print(howManyIce(graph))
