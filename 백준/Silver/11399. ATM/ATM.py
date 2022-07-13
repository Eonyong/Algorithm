import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
for idx in range(1, n):
    arr[idx] += arr[idx - 1]
print(sum(arr))
