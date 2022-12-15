import sys

input = sys.stdin.readline

n = int(input())
boards = [int(input()) for _ in range(n)]
if n == 1:
    print(boards.pop())
elif n == 2:
    print(max(boards[0], boards[0] + boards[1]))
else:
    dp = [boards[0], max(boards[0] + boards[1], boards[1]), max(boards[0], boards[1]) + boards[2]]
    for idx in range(3, n):
        dp.append(max(dp[idx - 2] + boards[idx], dp[idx - 3] + boards[idx - 1] + boards[idx]))
    print(dp.pop())