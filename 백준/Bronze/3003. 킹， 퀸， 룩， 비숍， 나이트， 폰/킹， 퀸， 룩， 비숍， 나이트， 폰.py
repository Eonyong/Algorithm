import sys

chess = [1, 1, 2, 2, 2, 8]
lst = list(map(int, sys.stdin.readline().split()))
print(*[chess[idx] - lst[idx] for idx in range(6)])