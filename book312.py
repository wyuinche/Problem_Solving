nums = list(input())
lens = len(nums)
nums = list(map(int, nums))

result = nums[0]
for i in range(1, lens):
    if result != 0 and nums[i] != 0:
        result *= nums[i]
    else:
        result += nums[i]

print(result)