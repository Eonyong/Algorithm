import sys
from itertools import product


def TenBagger(n) -> int:
    for idx in range(len(n)):
        if n[idx] != '0':
            return len(n) - idx
    return 1


n = list(sys.stdin.readline().strip())
m = int(sys.stdin.readline())
buttons = list(set(map(str, range(10))) - set(map(str, sys.stdin.readline().split()))) if m else list(map(str, range(10)))
goal = int(''.join(n))
answer = abs(goal - 100) if goal != 100 else 0

for i in [-1, 0, 1]:
    if len(n) + i:
        for cwr in product(buttons, repeat=len(n) + i):
            channel = int(''.join(cwr))
            answer = min(abs(channel - goal) + TenBagger(cwr), answer)
print(answer)
