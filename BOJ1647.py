from sys import stdin
from collections import Counter


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


N, M = map(int, stdin.readline().rstrip().split())


path = []
minPaths = []
parent = [i for i in range(N+1)]
cost = 0

for i in range(M):
    Ha, Hb, c = map(int, stdin.readline().rstrip().split())
    path.append((c, Ha, Hb))

path.sort()

for p in path:
    c, a, b, = p
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa != pb:
        if pa > pb:
            parent[pb] = pa
        else:
            parent[pa] = pb
        minPaths.append((c, a, b))
        cost += c


minPaths.reverse()

print(cost- minPaths[0][0])
