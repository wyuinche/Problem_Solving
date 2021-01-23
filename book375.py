def gold(graph, n, m, i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return -1
    else:
        return graph[m * i + j]

def goldTotal(graph, n, m):
    result = []
    for j in range(1, m):
        for i in range(n):
            y = j - 1
            x1, x2, x3 = i - 1, i, i + 1
            graph[m * i + j] += max(gold(graph, n, m, x1, y), gold(graph, n, m, x2, y), gold(graph, n, m, x3, y))
    for i in range(n):
        result.append(graph[i * m + m - 1])
    return max(result)


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = list(map(int, input().split()))
    print(goldTotal(graph, n, m))
