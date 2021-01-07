def cutTeok(cut, manyTeok):
    result = 0
    for teok in manyTeok:
        if teok > cut:
            result += teok - cut
    return result


n, m = map(int, input().split())
teoks = list(map(int, input().split()))

s = 0
e = max(teoks)
before = (s + e) // 2

while s <= e:
    mid = (s + e) // 2
    availableTeok = cutTeok(mid, teoks)
    if availableTeok >= m:
        before = mid
        s = mid + 1
    elif availableTeok < m:
        e = mid - 1


print(before)