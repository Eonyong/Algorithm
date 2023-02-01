import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))
bitonic = [1 for _ in range(n)]
bitonic_reverse = [1 for _ in range(n)]
answer = 0

for start in range(n):
    for end in range(start, n):
        if lis[start] < lis[end]:
            bitonic[end] = max(bitonic[start] + 1, bitonic[end])

lis.reverse()
for start in range(n):
    for end in range(start, n):
        if lis[start] < lis[end]:
            bitonic_reverse[end] = max(bitonic_reverse[end], bitonic_reverse[start] + 1)

bitonic_reverse.reverse()

for idx in range(n):
    answer = max(answer, bitonic[idx] + bitonic_reverse[idx] - 1)
print(answer)