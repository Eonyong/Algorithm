import sys

input = sys.stdin.readline

n = int(input())
maskings = [0 for _ in range(21)]

for _ in range(n):
    direct, number = list(map(str, input().split())), '0'

    if len(direct) == 2:
        direct, number = direct
    else:
        direct = direct[0]

    if direct == 'add':
        maskings[int(number)] = 1
    elif direct == 'remove':
        maskings[int(number)] = 0
    elif direct == 'check':
        print(maskings[int(number)] | 0)
    elif direct == 'toggle':
        maskings[int(number)] ^= 1
    elif direct == 'all':
        maskings = [1 for _ in range(21)]
    elif direct == 'empty':
        maskings = [0 for _ in range(21)]