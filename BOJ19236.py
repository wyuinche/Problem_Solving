D_UP, D_LEFTUP, D_LEFT, D_LEFTDOWN, D_DOWN, D_RIGHTDOWN, D_RIGHT, D_RIGHTUP = 1, 2, 3, 4, 5, 6, 7, 8
move = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
X, Y, SHARK_D = 0, 1, 2
FISH_N, FISH_D = 0, 1

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False
    return True

def parseInput(tmp):
    result = [[] for _ in range(4)]
    for i in range(8):
        result[i // 2].append(tmp[i])
    return result

def moveFish(sea_, shark, fishPos_):
    sea = [[[y for y in x] for x in s] for s in sea_]
    fishPos = [[x for x in f] for f in fishPos_]
    
    for i in range(1, 17):
        x, y = fishPos[i][X], fishPos[i][Y]
        if x < 0 or y < 0:
            continue
        curD = sea[x][y][FISH_D]
        
        for j in range(8):
            nx, ny = x + move[curD][X], y + move[curD][Y]
            if curD == 8:
                curD = 1
            else:
                curD += 1
            if not isValidPos(nx, ny):
                continue
            if nx == shark[X] and ny == shark[Y]:
                continue
            if sea[nx][ny][FISH_N] == 0:
                if curD == 1:
                    curD = 8
                else:
                    curD -= 1
                fishPos[i][X], fishPos[i][Y] = nx, ny
                sea[nx][ny][FISH_N], sea[nx][ny][FISH_D] = i, curD
                sea[x][y][FISH_N], sea[x][y][FISH_D] = 0, 0
                break
            else:
                if curD == 1:
                    curD = 8
                else:
                    curD -= 1
                tarX, tarY, tarN, tarD = nx, ny, sea[nx][ny][FISH_N], sea[nx][ny][FISH_D]
                sea[nx][ny][FISH_N], sea[nx][ny][FISH_D] = i, curD
                fishPos[tarN][X], fishPos[tarN][Y] = x, y
                sea[x][y][FISH_N], sea[x][y][FISH_D] = tarN, tarD
                fishPos[i][X], fishPos[i][Y] = nx, ny
                break
    return sea, fishPos
    
def eatableFish(sea, shark):
    x, y, d = shark[X], shark[Y], shark[SHARK_D]
    fish = []
    nx, ny = x, y
    while True:
        nx, ny = nx + move[d][X], ny + move[d][Y]
        if not isValidPos(nx, ny):
            break
        if sea[nx][ny][FISH_N] != 0:
            fish.append((nx, ny, sea[nx][ny][FISH_N], sea[nx][ny][FISH_D]))
    return fish
    
def leftFish(fishPos):
    count = 0
    for f in fishPos[1:]:
        if f[X] != -1 and f[Y] != -1:
            count += 1
    return count
    
def run(sea, shark, fishPos, total):
    if leftFish(fishPos) == 0:
        return total
    sea, fishPos = moveFish(sea, shark, fishPos)
    targetFish = eatableFish(sea, shark)
    
    if not targetFish:
        return total
    
    maxVal = total
    for f in targetFish:
        fx, fy, fn, fd = f
        sx, sy, sd = shark[X], shark[Y], shark[SHARK_D]
        sea[fx][fy][FISH_N], sea[fx][fy][FISH_D] = 0, 0
        fishPos[fn][X], fishPos[fn][Y] = -1, -1
        shark[X], shark[Y], shark[SHARK_D] = fx, fy, fd
        val = run(sea, shark, fishPos, total + fn)
        if maxVal < val:
            maxVal = val
        sea[fx][fy][FISH_N], sea[fx][fy][FISH_D] = fn, fd
        fishPos[fn][X], fishPos[fn][Y] = fx, fy
        shark[X], shark[Y], shark[SHARK_D] = sx, sy, sd
    return maxVal
    
    
    
sea = []
for i in range(4):
    sea.append(parseInput(list(map(int, input().split()))))

answer = sea[0][0][FISH_N]
shark = [0, 0, sea[0][0][FISH_D]]
sea[0][0][FISH_N] = 0
sea[0][0][FISH_D] = 0

fishPos = [[-1, -1] for _ in range(17)]
for i in range(4):
    for j in range(4):
        if sea[i][j][FISH_N] != 0:
            fishPos[sea[i][j][FISH_N]][X] = i
            fishPos[sea[i][j][FISH_N]][Y] = j

print(run(sea, shark, fishPos, answer))
