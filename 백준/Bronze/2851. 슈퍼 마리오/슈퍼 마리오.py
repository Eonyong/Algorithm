import sys

input = sys.stdin.readline

boards = [int(input()) for _ in range(10)]
prefix_sum = [0 for _ in range(10)]
prefix_sum[0] = boards[0]
answer = boards[0]
for idx in range(1, 10):
    prefix_sum[idx] += prefix_sum[idx - 1] + boards[idx]
for s in range(10):
    if abs(answer - 100) >= abs(prefix_sum[s] - 100):
        answer = max(answer, prefix_sum[s])
print(answer)