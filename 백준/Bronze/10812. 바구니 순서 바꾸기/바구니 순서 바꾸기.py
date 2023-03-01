import sys
input = sys.stdin.readline


n, m = map(int, input().split())
ls = [num for num in range(n + 1)]

for _ in range(m):
    start, end, mid = map(int, input().split())
    ls[start: end + 1] = ls[mid:end + 1] + ls[start:mid]
print(*ls[1:])