import sys

input = sys.stdin.readline


def Funny(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return Funny(20, 20, 20)

    if boards[a][b][c]:
        return boards[a][b][c]

    if a < b < c:
        boards[a][b][c] = Funny(a, b, c - 1) + Funny(a, b - 1, c - 1) - Funny(a, b - 1, c)
    else:
        boards[a][b][c] = Funny(a - 1, b, c) + Funny(a - 1, b - 1, c) + Funny(a - 1, b, c - 1) - Funny(a - 1, b - 1, c - 1)

    return boards[a][b][c]

boards = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, Funny(a, b, c)))