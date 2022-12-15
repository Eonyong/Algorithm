import sys

input = sys.stdin.readline


n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = sum(arr[:k])
answer = tmp

for s in range(k, n):
    tmp += arr[s] - arr[s - k]
    answer = max(answer, tmp)
print(answer)