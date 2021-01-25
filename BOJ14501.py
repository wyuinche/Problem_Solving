T, P = 0, 1
AVA_YES, AVA_FIN, AVA_NO = 0, 1, 2

def isAvailable(plan, n, i):
    fin = plan[i][T] + i - 1
    if fin < n:
        return AVA_YES, fin
    elif fin == n:
        return AVA_FIN, fin
    else:
        return AVA_NO, fin
    
def findMax(plan, n):
    dp = [0] * (n + 1)
    val = 0
    for i in range(n, 0, -1):
        available, fin = isAvailable(plan, n, i)
        if available == AVA_FIN:
            dp[i] = max(plan[i][P], val)
        elif available == AVA_YES:
            dp[i] = max(plan[i][P] + dp[fin+1], val)
        else:
            dp[i] = val
        if dp[i] > val:
            val = dp[i]
    return val

n = int(input())
plan = [(-1, -1)]
for _ in range(n):
    plan.append(tuple(map(int, input().split())))
    
print(findMax(plan, n))