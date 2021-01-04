n, k = map(int, input().split())
answer = 0

while True:
    if n == 1:
        break
    elif n < k:
        answer += n - 1
        break
    elif n % k == 0:
        n //= k
        answer += 1
    else:
        tmp = n % k
        answer += tmp
        n -= n % k

print(answer)
