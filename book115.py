position = list(input())
answer = 0
move = [(2, 1), (1, 2), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1)]

position[0] = ord(position[0]) - ord('a') + 1
position[1] = int(position[1])

for i in range(8):
    c, r = position[0] - move[i][0], position[1] - move[i][1]
    if c < 1 or r < 1 or c > 8 or r > 8:
        continue
    answer += 1

print(answer)
