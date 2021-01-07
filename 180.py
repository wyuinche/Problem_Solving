n = int(input())
students = []

for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

students.sort(key=lambda x: x[1])

for i in range(n):
    print(students[i][0], end=' ')
print()