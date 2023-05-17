import sys

input = sys.stdin.readline

for _ in range(int(input())):
    answer = []
    money = int(input())
    for m in [25, 10, 5, 1]:
        div, mod = divmod(money, m)
        answer.append(div)
        money = mod
    print(*answer)