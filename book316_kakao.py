from collections import Counter


def solution(food_times, k):
    answer = 0

    counter = Counter(food_times)
    counter_time = sorted(counter.keys())

    if sum(food_times) <= k:
        return -1

    before = 0
    left = len(food_times)
    turn = 0
    for t in counter_time:
        if left <= 0:
            return -1
        before = k
        k -= (t - turn) * left
        if k < 0:
            k = before
            while True:
                if k - left <= 0:
                    for i in range(len(food_times)):
                        if food_times[i] > turn:
                            if k <= 0:
                                return i+1
                            k -= 1
                    turn += 1
                else:
                    k -= left
                    turn += 1
                    if turn in counter_time:
                        left -= counter[turn]

        turn = t
        left -= counter[t]
    return answer

print(solution([1, 2, 3], 5))


