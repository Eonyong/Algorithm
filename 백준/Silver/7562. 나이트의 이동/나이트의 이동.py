import sys
from collections import deque

input = sys.stdin.readline


def Chess(s_row, s_col, e_row, e_col, l, boards):
    queue = deque([[s_row, s_col]])
    while queue:
        r, c = queue.popleft()
        if r == e_row and c == e_col:
            return boards[r][c]
        for j, i in [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]:
            nj, ni = r + j, c + i
            if 0 <= nj < l and 0 <= ni < l and not boards[nj][ni]:
                boards[nj][ni] = boards[r][c] + 1

                queue.append([nj, ni])
    return boards[e_row][e_col]


for _ in range(int(input())):
    l = int(input())
    boards = [[0 for _ in range(l)] for _ in range(l)]
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    print(Chess(start_r, start_c, end_r, end_c, l, boards))
