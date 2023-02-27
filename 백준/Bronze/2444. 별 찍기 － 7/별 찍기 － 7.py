import sys
input = sys.stdin.readline

n = int(input())

for idx in range(n):
    print(' ' * (n - idx - 1) + '*' * (2 * idx + 1))
for idx in range(n - 1):
    print(' ' * (idx + 1) + '*' * (2 * (n - 1) - 1 - 2 * idx))
