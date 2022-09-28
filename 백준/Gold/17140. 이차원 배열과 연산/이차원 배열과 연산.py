import sys
from collections import defaultdict

input = sys.stdin.readline


def SortingArray(array, l, flag):
    max_l = l
    nxt_numbers = []
    for arr in array:
        nxt = []
        numbers = defaultdict(int)
        for number in arr:
            if number:
                numbers[number] += 1
        numbers = sorted(map(list, numbers.items()), key=lambda x: (x[1], x[0]))
        for number in numbers:
            nxt += number
        max_l = max(max_l, len(nxt))
        nxt_numbers.append(nxt)
    if flag:
        return list(map(list, zip(*[nxt_number + [0] * (max_l - len(nxt_number)) for nxt_number in nxt_numbers]))), max_l
    else:
        return [nxt_number + [0] * (max_l - len(nxt_number)) for nxt_number in nxt_numbers], max_l


r, c, k = map(int, input().split())
h, w = 3, 3
boards = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

while cnt <= 100:
    if h >= r and w >= c and boards[r - 1][c - 1] == k:
        print(cnt)
        break
    if h >= w:
        boards, w = SortingArray(boards, w, 0)
    else:
        boards, h = SortingArray(list(map(list, zip(*boards))), h, 1)
    cnt += 1
else:
    print(-1)