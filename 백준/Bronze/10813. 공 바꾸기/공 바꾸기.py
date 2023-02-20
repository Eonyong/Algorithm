import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ls = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    ls[i - 1], ls[j - 1] = ls[j - 1], ls[i - 1]
print(*ls)