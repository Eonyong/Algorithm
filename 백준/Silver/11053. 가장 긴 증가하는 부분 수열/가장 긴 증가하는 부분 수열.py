import sys

input = sys.stdin.readline

n = int(input())
answer = 0
ls = list(map(int, input().split()))
tmp = [1 for _ in range(n)]
for s in range(1, n):
    for e in range(s):
        if ls[s] > ls[e]:
            tmp[s] = max(tmp[e] + 1, tmp[s])
print(max(tmp))