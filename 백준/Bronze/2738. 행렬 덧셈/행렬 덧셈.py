import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
C = [[A[row][col] + B[row][col] for col in range(m)] for row in range(n)]
for c in C:
    print(*c)