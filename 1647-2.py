import sys

n, m = map(int, input().split())
graph = []
parent = [x for x in range(n+1)]
edges = []

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph.append((c, a, b))


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x, y = find(parent, x), find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


graph.sort()

for edge in graph:
    cost, x, y = edge
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        edges.append(cost)


print(sum(edges[:-1]))
