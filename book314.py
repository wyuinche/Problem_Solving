
def check(coinList, targetNum):
    if targetNum in coinList:
        return True
    elif targetNum < min(coinList):
        return False
    else:
        for c in coinList:
            if targetNum - c <= 0:
                continue
            tmpList = [x for x in coinList]
            tmpList.remove(c)
            if check(tmpList, targetNum - c):
                return True
        return False


n = int(input())
coins = list(map(int, input().split()))

coins.sort()

if min(coins) > 1:
    print(1)
else:
    i = 0
    while True:
        i += 1
        if check(coins, i) is False:
            print(i)
            break
