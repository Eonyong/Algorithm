import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
s, e = 0, 1
answer = float('inf')
for val in ls:
    if val >= m:
        print(1)
        break
else:
    value = ls[s] + ls[e]
    while s < n and e < n:
        if value < m:
            e += 1
            if e == n:
                answer = min(answer, e - s + 1)
                break
            value += ls[e]
        else:
            answer = min(answer, e - s + 1)
            value -= ls[s]
            s += 1
        if s == e:
            break
    if s == 0 and e == n:
        print(0)
    else:
        print(answer)