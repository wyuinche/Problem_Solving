n = int(input())
scary = list(map(int, input().split()))
result = 0

scary.sort(reverse=True)

i = 0
while i < n:
    i += scary[i]
    result += 1

print(result)