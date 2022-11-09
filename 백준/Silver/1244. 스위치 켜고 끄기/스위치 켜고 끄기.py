import sys

input = sys.stdin.readline


def ManBulbs(i, n, cnt, bulbs):
    if i >= n:
        return
    else:
        bulbs[i] = 1 if bulbs[i] == 0 else 0
        ManBulbs(i + cnt, n, cnt, bulbs)


def WomanBulbs(i, n, j, bulbs):
    if 0 <= i - j and i + j < n:
        if bulbs[i - j] == bulbs[i + j]:
            if bulbs[i - j] == 0:
                bulbs[i - j] = 1
                bulbs[i + j] = 1
            else:
                bulbs[i - j] = 0
                bulbs[i + j] = 0
            WomanBulbs(i, n, j + 1, bulbs)
    else:
        return


n = int(input())
bulbs = list(map(int, input().split()))

for _ in range(int(input())):
    mf, index = map(int, input().split())
    index -= 1
    if mf == 1:
        ManBulbs(index, n, index + 1, bulbs)
    else:
        bulbs[index] = 1 if bulbs[index] == 0 else 0
        WomanBulbs(index, n, 1, bulbs)
if len(bulbs) > 20:
    for idx in range(0, n, 20):
        print(*bulbs[idx:idx + 20])
else:
    print(*bulbs)
