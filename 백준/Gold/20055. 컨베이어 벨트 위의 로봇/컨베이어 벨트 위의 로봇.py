import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
belts = deque(list(map(int, input().split())))
robots = deque([False for _ in range(n * 2)])
cnt = 0
while True:
    cnt += 1
    belts.rotate(1)
    robots.rotate(1)
    robots[n] = False
    for idx in range(n - 1, -1, -1):
        if idx == n - 1:
            robots[idx] = False
        if belts[idx + 1] > 0 and not robots[idx + 1] and robots[idx]:
            robots[idx + 1], robots[idx] = robots[idx], robots[idx + 1]
            belts[idx + 1] -= 1
    if belts[0] > 0:
        robots[0] = True
        belts[0] -= 1
    if belts.count(0) >= k:
        print(cnt)
        break
