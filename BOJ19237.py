# from time import sleep

UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
X, Y, D = 0, 1, 2
SHARK_N, SHARK_T, SHARK_E = 0, 1, 2
move = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

def isValidPos(n, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

def targetPos(sea, shark, shark_n, n):
    emptyPos, myPos = [], []
    x, y = shark[X], shark[Y]
    for i in range(1, 5):
        nx, ny = x + move[i][X], y + move[i][Y]
        if not isValidPos(n, nx, ny):
            continue
        if sea[nx][ny][SHARK_N] == 0:
            emptyPos.append((nx, ny, i))
        elif sea[nx][ny][SHARK_N] == shark_n:
            myPos.append((nx, ny, i))
            
    return emptyPos, myPos

def sortInPrior(shark_n, curD, prior, poses):
    if len(poses) == 1:
        return poses
    
    result = [() for _ in range(len(poses))]
    fill = 0
    for p in prior[shark_n][curD]:
        for pos in poses:
            if pos[D] == p:
                result[fill] = pos
                fill += 1
                break
    return result

def cuteShark(sea, sharks, prior, m, k):
    leftShark = m
    
    time_ = 0
    while True:
        if time_ > 1000:
            return -1
        # for s in sea:
        #     for ss in s:
        #         print(ss[:2], end=" ")
        #     print()
        # print()
        # sleep(1)
    
        if leftShark == 1:
            break
        time_ += 1
        for i in range(1, m+1):
            if sharks[i][D] < 0:
                continue
            emptyPos, myPos= targetPos(sea, sharks[i], i, n)
            target = None

            if emptyPos:
                emptyPos = sortInPrior(i, sharks[i][D], prior, emptyPos)
                target = emptyPos[0]
            
            elif myPos:
                myPos = sortInPrior(i, sharks[i][D], prior, myPos)
                target = myPos[0]
        
            if target:
                sharks[i][X], sharks[i][Y], sharks[i][D] = target[X], target[Y], target[D]
        
        for i in range(1, m+1):
            for j in range(1, i):
                if sharks[i][D] < 0:
                    break
                if sharks[j][D] > 0 and sharks[i][X] == sharks[j][X] and sharks[i][Y] == sharks[j][Y]:
                    sharks[i][D] = -1
                    leftShark -= 1
    
        for i in range(n):
            for j in range(n):
                sea[i][j][SHARK_E] = False
                if sea[i][j][SHARK_T] > 0:
                    sea[i][j][SHARK_T] -= 1
                if sea[i][j][SHARK_T] == 0:
                    sea[i][j][SHARK_N] = 0
    
        for i in range(1, m+1):
            if sharks[i][D] < 0:
                continue
            x, y = sharks[i][X], sharks[i][Y]
            sea[x][y][SHARK_E] = True
            sea[x][y][SHARK_N] = i
            sea[x][y][SHARK_T] = k   
    
    return time_
        
    
def parseList(tmp, n, k):
    result = [[0, 0, False] for _ in range(n)]
    for i in range(n):
        if tmp[i] != 0:
            result[i][SHARK_N] = tmp[i]
            result[i][SHARK_T] = k
            result[i][SHARK_E] = True
    return result

n, m, k = map(int, input().split())
prior = [[] for _ in range(m+1)]

sea = []
for _ in range(n):
    sea.append(parseList(list(map(int, input().split())), n, k))
    
sharks = [[-1, -1, -1] for _ in range(m+1)]
for i in range(n):
    for j in range(n):
        if sea[i][j] != 0:
            sharks[sea[i][j][SHARK_N]][X], sharks[sea[i][j][SHARK_N]][Y] = i, j

direction = list(map(int, input().split()))
for i in range(m):
    sharks[i+1][D] = direction[i]

for i in range(1, m+1):
    prior[i].append([])
    for _ in range(4):
        prior[i].append(list(map(int, input().split())))
    
print(cuteShark(sea, sharks, prior, m, k))
