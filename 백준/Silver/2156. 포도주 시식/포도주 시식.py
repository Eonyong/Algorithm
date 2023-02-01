import sys

input = sys.stdin.readline

n = int(input())

lis = [0 for _ in range(10000)]
for idx in range(n):
    lis[idx] = int(input())
max_v = [0 for _ in range(10000)]
max_v[0] = lis[0]
max_v[1] = lis[0] + lis[1]
max_v[2] = max(lis[2] + lis[0], lis[2] + lis[1], max_v[1])

for idx in range(3, n):
    max_v[idx] = max(lis[idx] + max_v[idx - 2], lis[idx] + lis[idx - 1] + max_v[idx - 3], max_v[idx - 1])

print(max(max_v))