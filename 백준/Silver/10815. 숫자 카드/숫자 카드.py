def binary(n, i, arr):
    s, e = 0, n - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] == i:
            return 1
        elif arr[m] < i:
            s = m + 1
        else:
            e = m - 1
    return 0


N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
havings = list(map(int, input().split()))
answer = []
for idx in range(M):
    answer.append(binary(N, havings[idx], cards))
print(*answer)