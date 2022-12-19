import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
_, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in  range(m)]

answer = [[0 for _ in range(k)] for _ in range(n)]

for row in range(n):
    for colm in range(m):
        for colk in range(k):
            answer[row][colk] += A[row][colm] * B[colm][colk]

for ans in answer:
    print(*ans)