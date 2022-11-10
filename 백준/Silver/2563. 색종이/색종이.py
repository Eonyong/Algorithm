import sys
input = sys.stdin.readline

boards = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
    r, c = map(int, input().split())
    for row in range(r, r + 10):
        for col in range(c, c + 10):
            boards[row][col] = 1

print(sum(map(sum, boards)))