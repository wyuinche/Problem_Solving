n = int(input())
students = []

for _ in range(n):
    name, a, b, c = input().split()
    students.append((int(a), int(b), int(c), name))

students.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for s in students:
    print(s[3])