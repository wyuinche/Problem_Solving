import sys

n = int(input())
house = list(map(int, sys.stdin.readline().rstrip().split()))

house.sort()

print(house[n//2 - 1  + n%2])
