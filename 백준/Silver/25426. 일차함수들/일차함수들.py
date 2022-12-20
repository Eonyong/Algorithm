import sys

input = sys.stdin.readline

answer = 0
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
ls.sort(key=lambda x: x[0])
for idx in range(n):
    answer += ls[idx][0] * (idx + 1) + ls[idx][1]
print(answer)