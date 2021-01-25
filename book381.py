N_UGLY, N_BEUTY = 0, 1

n = int(input())
dp = [N_BEUTY, N_UGLY]

i = 1
count = 1

while True:
    if count == n:
        print(i)
        break
    i += 1
    if i % 2 == 0:
        if dp[i // 2] == N_UGLY:
            dp.append(N_UGLY)
        else:
            dp.append(N_BEUTY)
    elif i % 3 == 0:
        if dp[i // 3] == N_UGLY:
            dp.append(N_UGLY)
        else:
            dp.append(N_BEUTY)
    elif i % 5 == 0:
        if dp[i // 5] == N_UGLY:
            dp.append(N_UGLY)
        else:
            dp.append(N_BEUTY)
    else:
        dp.append(N_BEUTY)
    if dp[i] == N_UGLY:
        count += 1
    