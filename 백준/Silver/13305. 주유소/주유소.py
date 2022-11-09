import sys
input = sys.stdin.readline

cnt = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

min_val = cities[0]
index = 0
answer = 0
tot = roads[0]

for idx in range(1, cnt - 1):
    tot += roads[idx]
    if cities[idx] < min_val:
        answer += min_val * (tot - roads[idx])
        min_val = cities[idx]
        index = idx
        tot = roads[idx]
print(answer + tot * cities[index])