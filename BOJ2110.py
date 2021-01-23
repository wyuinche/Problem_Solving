from sys import stdin
    
n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(stdin.readline().rstrip()))
house.sort()

answer = 0
gap = [house[1] - house[0], house[-1] - house[0]]
while gap[0] <= gap[1]:
    count = 1
    midGap = (gap[1] + gap[0]) // 2
    before = house[0]
    for i in range(1, n-1):
        if house[i] >= before + midGap:
            before = house[i]
            count += 1
    if count >= c:
        gap[0] = midGap + 1
        answer = midGap
    else:
        gap[1] = midGap - 1
    
print(answer)