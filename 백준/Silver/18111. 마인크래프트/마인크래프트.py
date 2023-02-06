import sys
from collections import defaultdict
input = sys.stdin.readline

answer = [float('inf'), 0]
n, m, b = map(int, input().split())
heights = defaultdict(int)
boards = [list(map(int, input().split())) for _ in range(n)]

minval, maxval = float('inf'), 0

for row in range(n):
    for col in range(m):
        h = boards[row][col]
        minval, maxval = min(minval, h), max(maxval, h)
        heights[h] += 1

for height in range(minval, maxval + 1):
    tmp, inven = 0, b
    for k, v in heights.items():
        val = abs(k - height)
        if k > height:
            tmp += 2 * v * val
            inven += v * val
        else:
            inven -= v * val
            tmp += v * val

    if inven >= 0:
        if answer[0] > tmp:
            answer = [tmp, height]
        elif answer[0] == tmp:
            answer[1] = max(answer[1], height)
print(*answer)