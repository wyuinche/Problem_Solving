g = int(input())
p = int(input())
planes = [0]

for _ in range(p):
    planes.append(int(input()))
    
parent = [x for x in range(g+1)]
    
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for i in range(1, p + 1):
    par = find(parent, planes[i])
    if par == 0:
        break
    else:
        union(parent, par, par - 1)
        answer += 1
print(answer)
    
        