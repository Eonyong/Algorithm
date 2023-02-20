import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ls = [i for i in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    ls[i:j + 1] = ls[j:i - 1:-1]
    
print(*ls[1:])