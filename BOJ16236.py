from collections import deque

S_X, S_Y, S_SIZE = 0, 1, 2
DIR_UP, DIR_DOWN, DIR_SAME, DIR_LEFT, DIR_RIGHT = 0, 1, 2, 3, 4
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def isValid(n, a, b):
    if a < 0 or b < 0 or a >= n or b >= n:
        return False
    else:
        return True

def nearPrey(shark, n, sea):
    result = []
    graph = [[False] * n for _ in range(n)]
    que = deque()
    que.append((0, shark[S_X], shark[S_Y]))
    while que:
        cost, sx, sy = que.popleft()
        for m in move:
            nx, ny = sx + m[0], sy + m[1]
            if not isValid(n, nx, ny):
                continue
            if graph[nx][ny]:
                continue
            graph[nx][ny] = True
            if sea[nx][ny] > shark[S_SIZE]:
                continue
            elif sea[nx][ny] < shark[S_SIZE] and sea[nx][ny] != 0:
                result.append((cost + 1, nx, ny))
            que.append((cost + 1, nx, ny))
    if not result:
        return 0, (-1, -1)
    result.sort(key=lambda x: (x[0], x[1], x[2]))
    return result[0][0], (result[0][1], result[0][2])


n = int(input())
sea = []
prey = []
shark = [-1, -1, 2]

exp = 2
time = 0

for _ in range(n):
    sea.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark[S_X] = i
            shark[S_Y] = j
            sea[i][j] = 0
        if sea[i][j] != 0:
            prey.append((i, j))
            
while prey:
    cost, target_prey = nearPrey(shark, n, sea)
    if cost == 0:
        break
    time += cost
    exp -= 1
    shark[S_X], shark[S_Y] = target_prey
    sea[target_prey[0]][target_prey[1]] = 0
    for i in range(len(prey)):
        if prey[i][0] == target_prey[0] and prey[i][1] == target_prey[1]:
            del prey[i]
            break
    if exp == 0:
        shark[S_SIZE] += 1
        exp = shark[S_SIZE]
    
print(time)
