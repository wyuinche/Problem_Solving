import sys
from collections import deque

n, L, R = map(int, sys.stdin.readline().rstrip().split())
graph = []
world = [[0] * n for _ in range(n)]
move = [(-1, 0), (1, 0), (0, 1), (0, -1)]


for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


def clearWorld():
    for i in range(n):
        for j in range(n):
            world[i][j] = 0


def isShare(pop1, pop2):
    if abs(pop1 - pop2) >= L and abs(pop1 - pop2) <= R:
        return True
    else:
        return False


def isPosAvailable(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


def bfs(i, j, k):
    q = deque()
    q.append((i, j))
    world[i][j] = k
    pop = graph[i][j]
    count = 1
    while q:
        x, y = q.popleft()
        for m in move:
            nx, ny = x+m[0], y+m[1]
            if isPosAvailable(nx, ny) and isShare(graph[x][y], graph[nx][ny]) and world[nx][ny] == 0:
                q.append((nx, ny))
                world[nx][ny] = k
                pop += graph[nx][ny]
                count += 1
    return pop // count


def changeGraph(count, pops):
    if count == 0:
        return True
    isChanged = False
    for i in range(n):
        for j in range(n):
            if pops[world[i][j]] != graph[i][j]:
                graph[i][j] = pops[world[i][j]]
                isChanged = True
    return isChanged


count = 0
pops = [0]
count_num = 0
while changeGraph(count_num, pops):
    clearWorld()
    count += 1
    count_num = 0
    pops = [0]
    for i in range(n):
        for j in range(n):
            if world[i][j] == 0:
                count_num += 1
                pp = bfs(i, j, count_num)
                pops.append(pp)


print(count-1)
