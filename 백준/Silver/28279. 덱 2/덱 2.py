import sys
from collections import deque

input = sys.stdin.readline


deq = deque()
for _ in range(int(input())):
    ls = list(map(int, input().split()))
    if len(ls) == 2:
        if ls[0] == 1:
            deq.appendleft(ls[1])
        else:
            deq.append(ls[1])
    else:
        if ls[0] == 3:
            try:
                print(deq.popleft())
            except:
                print(-1)
        elif ls[0] == 4:
            try:
                print(deq.pop())
            except:
                print(-1)
        elif ls[0] == 5:
            print(len(deq))
        elif ls[0] == 6:
            if deq:
                print(0)
            else:
                print(1)
        elif ls[0] == 7:
            try:
                print(deq[0])
            except:
                print(-1)
        elif ls[0] == 8:
            try:
                print(deq[-1])
            except:
                print(-1)