import sys
from collections import deque

R_POSSIBLE, R_UNKNOWN, R_IMPOSSIBLE = 0, 1, 2

def init(n, rank):
    graph = [[False] * (n+1) for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            graph[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1
    return graph, indegree

def result(n, graph, indegree):
    que = deque()
    answer = [R_POSSIBLE, []]
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)

    for k in range(n):
        if not que:
            answer[0] = R_IMPOSSIBLE
            return answer
        
        if len(que) > 1:
            answer[0] = R_UNKNOWN
            return answer
        
        x = que.popleft()
        answer[1].append(x)
        
        for i in range(1, n+1):
            if graph[x][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    que.append(i)
        
    return answer

def ranking():
    n = int(input())
    rank = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    graph, indegree = init(n, rank)
    
    m = int(input()) 
    if m == 0:
        for r in rank[1:]:
            print(r, end=" ")
        print()
        return
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if graph[a][b]:
            graph[b][a] = True
            graph[a][b] = False
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    answer = result(n, graph, indegree)
    if answer[0] == R_IMPOSSIBLE:
        print("IMPOSSIBLE")
    elif answer[0] == R_UNKNOWN:
        print("?")
    else:
        for r in answer[1]:
            print(r, end=" ")
        print()

t = int(input())

for _ in range(t):
    ranking()
