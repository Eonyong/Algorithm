import sys
input = sys.stdin.readline

e = int(input()) - 1
items = sorted(map(int, input().split()))
ls = []
s = 0
answer = float('inf')
while s < e:
    tmp = items[e] + items[s]
    if answer > abs(tmp):
        answer = abs(tmp)
        ls = [items[s], items[e]]

    if tmp < 0:
        s += 1
    else:
        e -= 1

print(*ls)
