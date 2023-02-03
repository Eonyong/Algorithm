import sys

input = sys.stdin.readline


n, k = map(int, input().split())
lines = [int(input()) for _ in range(n)]

start, end = 1, max(lines)

while start <= end:
    middle = (start + end) // 2
    cnt = 0
    for line in lines:
        cnt += line // middle

    if cnt >= k:
        start = middle + 1
    else:
        end = middle - 1

print(end)