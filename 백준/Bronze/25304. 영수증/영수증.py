import sys

budget = int(sys.stdin.readline())
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    budget -= a * b
print('Yes') if not budget else print('No')