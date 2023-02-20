import sys

input = sys.stdin.readline

n,m = map(int, input().split())
ls = [0 for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    for idx in range(s - 1, e):
        ls[idx] = w
print(*ls)