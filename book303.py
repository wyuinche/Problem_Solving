from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
times = [0 for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
result_time = [0 for _ in range(n+1)]

for i in range(1, n+1):
    course = list(map(int, input().split()))
    times[i] = course[0]
    for c in course[1:]:
        if c == -1:
            break
        else:
            graph[c].append(i)
            indegree[i] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append((i, 0))

while queue:
    node, time = queue.popleft()
    result_time[node] = max(times[node] + time, result_time[node])
    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append((i, result_time[node]))

for t in result_time[1:]:
    print(t)
