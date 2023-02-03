import sys

input = sys.stdin.readline


def QuardTrie(row, col, n, arr):
    first = arr[row][col]
    for nj in range(n):
        for ni in range(n):
            if arr[row + nj][col + ni] != first:
                print('(', end='')
                for y, x in [[row, col], [row, col + n // 2], [row + n // 2, col], [row + n // 2, col + n // 2]]:
                    QuardTrie(y, x, n // 2, arr)
                print(')', end='')
                return
    print(first, end='')


N = int(input())
boards = [list(map(int, list(input().rstrip()))) for _ in range(N)]
QuardTrie(0, 0, N, boards)