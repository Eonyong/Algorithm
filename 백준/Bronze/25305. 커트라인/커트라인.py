import sys

n, a = map(int, sys.stdin.readline().split())
print(sorted(map(int, sys.stdin.readline().split()), reverse=True)[a - 1])

