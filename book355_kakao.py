from collections import deque

all_move = [(-1, 0, -1, 0), (0, -1, 0, -1), (1, 0, 1, 0), (0, 1, 0, 1)]
circle_move = [(-1, 1, 0, 0), (1, 1, 0, 0), (0, 0, -1, -1), (0, 0, 1, -1), (1, -1, 0, 0), (0, 0, -1, 1), (-1, -1, 0, 0), (0, 0, 1, 1)]
    
def available(robot):
    a, b = robot
    if abs(a[0] - b[0]) + abs(a[1] - b[1]) > 1:
        return False
    return True

def isInMap(robot, n):
    a, b = robot
    if a[0] < 0 or a[1] < 0 or b[0] < 0 or b[1] < 0 or a[0] >= n or a[1] >= n or b[0] >= n or b[1] >= n:
        return False
    return True

def isInRoad(road, a, b):
    for r in road[a[0]][a[1]]:
        if r[0] == b[0] and r[1] == b[1]:
            return True
    return False
    
def isCirculable(board, a, b, na, nb):
    startX = min(a[0], b[0], na[0], nb[0])
    startY = min(a[1], b[1], na[1], nb[1])
    FinX = max(a[0], b[0], na[0], nb[0])
    FinY = max(a[1], b[1], na[1], nb[1])
    for i in range(startX, FinX+1):
        for j in range(startY, FinY+1):
            if board[i][j] == 1:
                return False
    return True
    
def solution(board):
    answer = 0
    n = len(board)
    
    road = [[[] for _ in range(n)] for __ in range(n)]
    road[0][0].append((0, 1))
    road[0][1].append((0, 0))
    
    q = deque([])
    q.append(((0, 0), (0, 1), 0))
    
    countMap = [[int(1e9)] * n for _ in range(n)]
    
    while q:
        a, b, cost = q.popleft()
        cost += 1
        for m in all_move:
            na, nb = (a[0] + m[0], a[1] + m[1]), (b[0] + m[2], b[1] + m[3])
            if not available((na, nb)):
                continue
            if not isInMap((na, nb), n) or board[na[0]][na[1]] == 1 or board[nb[0]][nb[1]] == 1:
                continue
            countMap[na[0]][na[1]] = min(countMap[na[0]][na[1]], cost)
            countMap[nb[0]][nb[1]] = min(countMap[nb[0]][nb[1]], cost)
            if not isInRoad(road, na, nb):
                road[na[0]][na[1]].append(nb)
                road[nb[0]][nb[1]].append(na)
                q.append((na, nb, cost))
            if countMap[n-1][n-1] != int(1e9):
                return countMap[n-1][n-1]

        for m in circle_move:
            na, nb = (a[0] + m[0], a[1] + m[1]), (b[0] + m[2], b[1] + m[3])
            if not available((na, nb)):
                continue
            if not isInMap((na, nb), n) or board[na[0]][na[1]] == 1 or board[nb[0]][nb[1]] == 1:
                continue
            if isCirculable(board, a, b, na, nb):
                countMap[na[0]][na[1]] = min(countMap[na[0]][na[1]], cost)
                countMap[nb[0]][nb[1]] = min(countMap[nb[0]][nb[1]], cost)
                if not isInRoad(road, na, nb):
                    road[na[0]][na[1]].append(nb)
                    road[nb[0]][nb[1]].append(na)
                    q.append((na, nb, cost))
            if countMap[n-1][n-1] != int(1e9):
                return countMap[n-1][n-1]
    answer = countMap[n-1][n-1]
    return answer

print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
