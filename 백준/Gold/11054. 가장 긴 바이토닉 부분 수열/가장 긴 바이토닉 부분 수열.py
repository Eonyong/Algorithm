import sys

input = sys.stdin.readline


def Lis(n, array):
    bitonic = [1 for _ in range(n)]
    for start in range(n):
        for end in range(start, n):
            if array[start] < array[end]:
                bitonic[end] = max(bitonic[start] + 1, bitonic[end])

    return bitonic


n = int(input())
lis = list(map(int, input().split()))
answer = 0

arr = Lis(n, lis)
revese_arr = Lis(n, lis[::-1])[::-1]

for idx in range(n):
    answer = max(answer, arr[idx] + revese_arr[idx] - 1)
print(answer)
