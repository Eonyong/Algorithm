import sys
from collections import deque

input = sys.stdin.readline


def GoTo(s, e, ls):
    global answer
    tmp = deque()
    tmp.append(s)
    while tmp:
        t = tmp.popleft()
        for m in [2 * t, t + 1, t - 1]:
            if 0 <= m < 100001:
                if m == t * 2:
                    if ls[m] > ls[t]:
                        ls[m] = ls[t]
                        tmp.append(m)
                else:
                    if ls[m] > ls[t] + 1:
                        tmp.append(m)
                        ls[m] = ls[t] + 1


answer = float('inf')
ls = [sys.maxsize for _ in range(100001)]
s, e = map(int, input().split())
ls[s] = 0
GoTo(s, e, ls)
print(ls[e])
