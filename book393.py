n, m = map(int, input().split())
road = [[0] * (n+1)]

for i in range(1, n+1):
    road.append([0] + list(map(int, input().split())))
    
plan = list(map(int, input().split()))
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if road[i][j] == 1:
                continue
            if road[i][k] == 1 and road[k][j] == 1:
                road[i][j] = 1

for i in range(m - 1):
    if road[plan[i]][plan[i+1]] == 0:
        print("NO")
        break
    elif i == m - 2:
        print("YES")