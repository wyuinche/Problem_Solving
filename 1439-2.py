import sys

s = list(sys.stdin.readline().rstrip())
s = list(map(int, s))
num = [0, 0]
start = 0

num[s[0]] = 1
start = s[0]

for ss in s[1:]:
    if ss != start:
        num[ss] += 1
        start = (start + 1) % 2
        
print(min(num))