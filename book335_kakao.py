from itertools import permutations

def makePoint(n, weak_point, p):
    removed = []
    result = weak_point[0]
    maxLen = 0
    
    for w in weak_point:
        for i in range(p+1):
            if (w+i)%n in weak_point:
                removed.append((w+i)%n)
        if len(removed) > maxLen:
            result = w
            maxLen = len(removed)
        removed = []
    return result
            
def isFixed(n, weak, weak_list, friend):
    weak_point = [x for x in weak]
    
    for f in friend:
        setPoint = makePoint(n, weak_point, f)
        for i in range(f+1):
            if (setPoint + i) % n in weak_point:
                weak_point.remove((setPoint+i)%n)
        if not weak_point:
            return True
    return False
    
def solution(n, weak, dist):
    answer = 0
    friendNum = len(dist)
    weak_list = [0] * n
    
    if len(weak) == 1:
        return 1
    
    for x in weak:
        weak_list[x] = 1
    
    for i in range(1, friendNum + 1):
        combi = permutations(dist, i)
        for comb in combi:
            if isFixed(n, weak, weak_list, comb):
                return i
            
    return -1