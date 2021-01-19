from itertools import combinations


def copyGraph(src, des, n, m):
    for i in range(n):
        for j in range(m):
            des[i][j] = src[i][j]
    return des

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())

graph = []
space = []
virus = []
orgGraph = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))


orgGraph = copyGraph(graph, orgGraph, n, m)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))


comb = combinations(space, 3)

answer = 0
for c in comb:
    graph = copyGraph(orgGraph, graph, n, m)
    for w in c:
        x, y = w
        graph[x][y] = 1
    stack = [x for x in virus]
    while stack:
        x, y = stack.pop()
        for mo in move:
            nx, ny = x + mo[0], y + mo[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                stack.append((nx, ny))
    result = 0
    for line in graph:
        for l in line:
            if l == 0:
                result += 1
    answer = max(result, answer)

print(answer)