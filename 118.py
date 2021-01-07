n, m = map(int, input().split())
a, b, d = map(int, input().split())
# NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
dir_move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# GROUND, SEA = 0, 1
answer = 1

uMap = []

for i in range(n):
    uMap.append(list(map(int, input().split())))

ca, cb = a, b
check = False
while True:
    if check == True:
        break
    left = d
    for _ in range(4):
        left = (left + 3) % 4
        na, nb = a + dir_move[left][0], b + dir_move[left][1]
        if na < 1 or nb < 1 or na > n or nb > m or uMap[na][nb] != 0:
            if _ >= 3:
                if uMap[na][nb] == 1:
                    check = True
                    break
                else:
                    a, b = ca, cb
                    break
            else:
                continue
        else:
            ca, cb = a, b
            a, b = na, nb
            d = left
            uMap[na][nb] = 2
            answer += 1
            break
            
print(answer)