from collections import Counter

def failRatio(eachStage, n):
    if sum(eachStage[n:]) == 0:
        return 0
    return (eachStage[n] * 1.0) / sum(eachStage[n:])
    
def solution(N, stages):
    answer = []
    failRatios = []
    
    stages.sort()
    counter = Counter(stages)
    
    numInEachStage = [0] * (N+2)
    
    for i in range(1, N+2):
        numInEachStage[i] = counter[i]

    for i in range(1, N+1):
        failRatios.append((failRatio(numInEachStage, i), i))
        
    failRatios.sort(key=lambda x: (-x[0], x[1]))
    
    for f in failRatios:
        answer.append(f[1])
    
    return answer