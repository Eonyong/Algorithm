import sys
from collections import deque
input = sys.stdin.readline


n, m, t = map(int, input().split())
boards = deque(deque(list(map(int, input().split()))) for _ in range(n))
for _ in range(t):
    x, d, k = map(int, input().split())
    # d가 1이면 시계, 0이면 반시계
    direction = -1 if d else 1
    idx = x - 1
    while idx < n:
        for _ in range(k):
            boards[idx].rotate(direction)
        idx += x

    flag = False
    avg_val, cnt_val = 0, 0
    for row in range(n):
        for col in range(m):
            value = boards[row][col]
            if value:
                ls = deque()
                ls.append((row, col))
                avg_val += boards[row][col]
                cnt_val += 1
                while ls:
                    y, x = ls.popleft()
                    for j, i in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                        nj, ni = y + j, (x + i) % m
                        if 0 <= nj < n and value == boards[nj][ni]:
                            flag = True
                            ls.append((nj, ni))
                            boards[nj][ni] = 0
    if not flag:
        for row in range(n):
            for col in range(m):
                if boards[row][col]:
                    if (avg_val / cnt_val) < boards[row][col]:
                        boards[row][col] -= 1
                    elif (avg_val / cnt_val) > boards[row][col]:
                        boards[row][col] += 1

print(sum(sum(board) for board in boards))
