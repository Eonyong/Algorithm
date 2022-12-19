import sys
from collections import defaultdict

input = sys.stdin.readline


def SquareNum(i, answer, a, b, c):
    if i == b:
        print(answer)
    elif i * 2 <= b:
        tmp[i * 2] = (answer * answer) % c
        SquareNum(i * 2, tmp[i * 2], a, b, c)
    else:
        for k, v in tmp.items():
            if i + k <= b:
                tmp[i + k] = (answer * v) % c
                SquareNum(i + k, tmp[i + k], a, b, c)

                return


a, b, c = map(int, input().split())

tmp = []
i = 1
tmp.append([i, a % c])
answer = tmp[0][1]

while i < b:
    if i * 2 <= b:
        i *= 2
        answer = (answer * answer) % c
        tmp.append([i, answer])
    else:
        for k, v in tmp:
            if i + k <= b:
                answer = (answer * v) % c
                i += k
                tmp.append([i, answer])
                break
        tmp.sort(reverse=True)
print(answer)
