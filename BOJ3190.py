from collections import deque

LEFT, RIGHT = 'L', 'D'
EAST, DOWN, WEST, UP = 0, 1, 2, 3
# 우하좌상
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())
k = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]


for _ in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1

l = int(input())
go = deque([])
for _ in range(l):
    x, c = input().split()
    go.append((int(x), c))

snake = deque([])
snake.append((1, 1))

curTime = 0
curD = EAST
cx, cy = 1, 1

fin = False
while True:
    while go:
        t, d = go.popleft()
        for i in range(t-curTime):
            curTime += 1
            nx, ny = cx + move[curD][0], cy + move[curD][1]
            if nx < 1 or ny < 1 or nx > n or ny > n or graph[nx][ny] == 2:
                print(curTime)
                fin = True
                break
            cx, cy = nx, ny
            snake.append((nx, ny))
            if graph[nx][ny] != 1:
                bx, by = snake.popleft()
                graph[bx][by] = 0
            graph[nx][ny] = 2
        if d == LEFT:
            curD = (curD + 3) % 4
        elif d == RIGHT:
            curD = (curD + 1) % 4
        if fin:
            break
    if fin:
        break
    curTime += 1
    nx, ny = cx + move[curD][0], cy + move[curD][1]
    if nx < 1 or ny < 1 or nx > n or ny > n or graph[nx][ny] == 2:
        print(curTime)
        break
    cx, cy = nx, ny
    snake.append((nx, ny))
    if graph[nx][ny] != 1:
        bx, by = snake.popleft()
        graph[bx][by] = 0
    graph[nx][ny] = 2
