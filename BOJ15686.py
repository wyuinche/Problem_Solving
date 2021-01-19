from itertools import combinations


n, m = map(int, input().split())
graph = []
chicken = []
house = []
INF = int(1e9)


def length(h, chicken):
    hx, hy = h
    res = INF
    for c in chicken:
        cx, cy = c
        leng = abs(hx - cx) + abs(hy - cy)
        res = min(leng, res)
    return res


def combRes(house, chicken):
    answer = 0
    for h in house:
        answer += length(h, chicken)
    return answer


for _ in range(n):
    graph.append(list(map(int, input().split())))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))


answer = INF
combs = combinations(chicken, m)
for com in combs:
    answer = min(answer, combRes(house, com))


print(answer)
