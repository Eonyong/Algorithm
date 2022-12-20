import sys
from collections import deque

input = sys.stdin.readline


def GoTo(s, e, ls):
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


s, e = map(int, input().split())
ls = [100001 for _ in range(100001)]
ls[s] = 0
GoTo(s, e, ls)
print(ls[e])
