import sys

input = sys.stdin.readline

n = int(input())
ladders = [list(map(int, input().split())) for _ in range(n)]
ladders.sort()
dp = [1 for _ in range(n)]
l = 0
for i in range(n):
    for j in range(i):
        if ladders[i][1] > ladders[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            l = max(l, dp[i])

print(n - l)