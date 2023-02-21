import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = input().rstrip()
    print(f'{m[0]}{m[-1]}')