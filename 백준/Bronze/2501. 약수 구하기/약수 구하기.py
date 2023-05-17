import sys

input = sys.stdin.readline

n, m = map(int, input().split())

for div in range(1, n + 1):
    if not (n % div):
        m -= 1
    if not m:
        print(div)
        break
else:
    print(0)