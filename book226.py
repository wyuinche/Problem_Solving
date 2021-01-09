n, m = map(int, input().split())
coins = []
INF = 1e9

for _ in range(n):
    coins.append(int(input()))

coins.sort()
dp = [INF] * (m+1)
dp[0] = 0

for c in coins:
    for i in range(c, m+1):
        if dp[i - c] != INF:
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[m] != INF:
    print(dp[m])
else:
    print(-1)