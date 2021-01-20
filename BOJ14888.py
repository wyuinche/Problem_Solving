from itertools import permutations

INF = int(1e9)
n = int(input())
nums = list(map(int, input().split()))
ADD, SUB, MUL, DIV = 0, 1, 2, 3
ADD_n, SUB_n, MUL_n, DIV_n = map(int, input().split())


cals = [ADD] * ADD_n + [SUB] * SUB_n + [MUL] * MUL_n + [DIV] * DIV_n

perms = list(permutations(cals))
perms = list(set(perms))
result = []

for p in perms:
    tmp = nums[0]
    for i in range(1, n):
        if p[i-1] == ADD:
            tmp += nums[i]
        elif p[i-1] == SUB:
            tmp -= nums[i]
        elif p[i-1] == MUL:
            tmp *= nums[i]
        elif p[i-1] == DIV:
            if (tmp > 0 and nums[i] < 0) or (tmp < 0 and nums[i] > 0):
                nums[i] = abs(nums[i])
                tmp = abs(tmp)
                tmp //= nums[i]
                tmp = -tmp
            else:
                tmp //= nums[i]
    result.append(tmp)

print(max(result))
print(min(result))
