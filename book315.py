from itertools import combinations
from collections import Counter

n, m = map(int, input().split())
balls = list(map(int, input().split()))
counter = Counter(balls)

combination = list(combinations(counter.keys(), 2))
answer = 0

for comb in combination:
    answer += counter[comb[0]] * counter[comb[1]]

print(answer)