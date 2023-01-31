import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    methods = input().rstrip()

    n = int(input())
    boards = input().rstrip()[1:-1]
    boards = deque(map(int, boards.split(','))) if n else deque([])
    cnt_d = methods.count('D')
    cnt = 0
    if cnt_d > n:
        print('error')
    else:

        for method in methods:
            if method == 'R':
                cnt += 1
            elif method == 'D':
                if cnt % 2:
                    boards.pop()
                else:
                    boards.popleft()

        if cnt % 2:
            boards.reverse()
        print("[" + ','.join(map(str, boards)) + "]")
