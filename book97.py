n, m = map(int, input().split())
numbers = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp.sort()
    numbers.append(tmp[0])

numbers.sort()

print(numbers[-1])
