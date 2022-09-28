import sys
from collections import defaultdict

input = sys.stdin.readline


def SortingCol(array, w, h):
    max_l = w
    nxt_numbers = []
    for row in range(h):
        nxt = []
        numbers = defaultdict(int)
        for col in range(w):
            if array[row][col]:
                numbers[array[row][col]] += 1
        numbers = sorted(map(list, numbers.items()), key=lambda x: (x[1], x[0]))
        for number in numbers:
            nxt += number
        max_l = max(max_l, len(nxt))
        nxt_numbers.append(nxt)
    else:
        return [nxt_number + [0] * (max_l - len(nxt_number)) for nxt_number in nxt_numbers], max_l


def SortingRow(array, w, h):
    max_l = h
    nxt_numbers = []
    for col in range(w):
        nxt = []
        numbers = defaultdict(int)
        for row in range(h):
            if array[row][col]:
                numbers[array[row][col]] += 1
        numbers = sorted(map(list, numbers.items()), key=lambda x: (x[1], x[0]))
        for number in numbers:
            nxt += number
        max_l = max(max_l, len(nxt))
        nxt_numbers.append(nxt)
    else:
        return list(
            map(list, zip(*[nxt_number + [0] * (max_l - len(nxt_number)) for nxt_number in nxt_numbers]))), max_l


r, c, k = map(int, input().split())
h, w = 3, 3
boards = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

while cnt <= 100:
    if h >= r and w >= c and boards[r - 1][c - 1] == k:
        print(cnt)
        break
    if h >= w:
        boards, w = SortingCol(boards, w, h)
    else:
        boards, h = SortingRow(boards, w, h)
    cnt += 1
else:
    print(-1)
