from itertools import combinations

n = int(input())
graph = [[0] * (n+1)]
space = []
teacher = []


def isStudent(graph, t):
    tx, ty = t
    for i in range(tx, 0, -1):
        if graph[i][ty] == 'O':
            break
        elif graph[i][ty] == 'S':
            return True
    if tx < n:
        for i in range(tx+1, n+1):
            if graph[i][ty] == 'O':
                break
            elif graph[i][ty] == 'S':
                return True
    for j in range(ty, 0, -1):
        if graph[tx][j] == 'O':
            break
        elif graph[tx][j] == 'S':
            return True
    if ty < n:
        for j in range(ty+1, n+1):
            if graph[tx][j] == 'O':
                break
            elif graph[tx][j] == 'S':
                return True
    return False


for _ in range(n):
    graph.append([0] + list(input().split()))

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 'T':
            teacher.append((i, j))
        elif graph[i][j] == 'X':
            space.append((i, j))

comb = combinations(space, 3)

result = 'NO'
isCont = False
for c in comb:
    isCont = False
    for o in c:
        i, j = o
        graph[i][j] = 'O'
    for t in teacher:
        if isStudent(graph, t):
            result = 'NO'
            isCont = True
            break
    if isCont:
        for o in c:
            i, j = o
            graph[i][j] = 'X'
        continue
    else:
        result = 'YES'
        break


print(result)
