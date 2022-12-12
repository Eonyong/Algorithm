import sys

input = sys.stdin.readline

n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]

a = 0
for idx in range(n):
    a += pos[idx][0] * pos[(idx + 1) % n][1] - pos[idx][1] * pos[(idx + 1) % n][0]
print(round(abs(a) / 2, 1))