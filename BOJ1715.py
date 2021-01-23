import heapq
import sys


n = int(sys.stdin.readline().rstrip())
cards =[]
for _ in range(n):
    cards.append(int(sys.stdin.readline().rstrip()))

if n == 1:
    print(0)
else:
    cards.sort()
    que = []
    for c in cards:
        heapq.heappush(que, c)
    result = 0
    while que:
        cardA = heapq.heappop(que)
        if not que:
            break
        cardB = heapq.heappop(que)
        heapq.heappush(que, cardA + cardB)
        result += cardA + cardB

    print(result)