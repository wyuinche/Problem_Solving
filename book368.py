def find_pos(arr, s, e):
    m = (s + e) // 2
    if arr[m] == m:
        return m
    elif arr[m] < m:
        return find_pos(arr, m+1, e)
    else:
        return max(find_pos(arr, s, m-1), find_pos(arr, m+1, e))


n = int(input())
pos = list(map(int, input().split()))

print(find_pos(pos, 0, n - 1))