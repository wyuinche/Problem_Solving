n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

numbers.sort(reverse=True)

tar1, tar2 = numbers[0], numbers[1]

for i in range(1, m+1):
    if i % k == 0:
        answer += tar2
    else:
        answer += tar1

print(answer)
