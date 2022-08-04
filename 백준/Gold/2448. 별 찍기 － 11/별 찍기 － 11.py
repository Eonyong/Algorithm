# def stars(i, n, boards):
#     if i == n:
#         return
#     else:
#         for k in range(n - i - 3, n + i + 1, 6):
#             for kk in range(k, k + 5):
#                 if kk - k == 2:
#                     boards[i][kk] = '*'
#                 if (kk - k) % 2:
#                     boards[i + 1][kk] = '*'
#                 boards[i + 2][kk] = '*'
#         stars(i + 3, n, boards)

# def stars(srow, erow, scol, ecol, boards):
#     if boards[srow][(scol + ecol) // 2] == ' ':
#         boards[srow][(scol + ecol) // 2] = '*'
#
#         stars(srow, (srow + erow) // 2, scol, (scol + ecol) // 2, boards)
#         stars(srow, (srow + erow) // 2, (scol + ecol) // 2, ecol, boards)
#
#         stars((srow + erow) // 2, erow, (scol + ecol) // 2, ecol, boards)
#         stars((srow + erow) // 2, erow, scol, (scol + ecol) // 2, boards)
#
# def stars(srow, erow, scol, ecol, boards):
#     if boards[srow][(scol + ecol) // 2] == ' ':
#         boards[srow][(scol + ecol) // 2] = '*'
#         stars((srow + erow) // 2, erow, scol, (scol + ecol) // 2, boards)
#         stars((srow + erow) // 2, erow, (scol + ecol) // 2, ecol, boards)

# def stars(n, scol, ecol, boards):
#     if n < 0:
#         return
#     else:
#         if boards[n][(scol + ecol) // 2] == ' ':
#             boards[n][(scol + ecol) // 2] = '*'
#             stars(n, scol, (scol + ecol) // 2, boards)
#             stars(n, (scol + ecol) // 2, ecol, boards)
#             stars(n - 1, (scol + ecol) // 4, (ecol + (scol + ecol) // 2) // 2, boards)

# def stars(srow, erow, scol, ecol, boards):
#     if boards[(srow + erow) // 2][(scol + ecol) // 2] == ' ':
#         boards[(srow + erow) // 2][(scol + ecol) // 2] = '*'
#
#         stars((srow + erow) // 2, erow, (scol + ecol) // 2, ecol, boards)
#         stars((srow + erow) // 2, erow, scol, (scol + ecol) // 2, boards)


def stars(row, col, n, boards):
    if not n:
        return
    else:
        if boards[row][col] == ' ' and not row % 3:
            boards[row][col] = '*'
            boards[row + 1][col - 1: col + 2] = '* *'
            boards[row + 2][col - 2: col + 3] = '*' * 5

            while n:
                stars(row + (n >> 1), col + (n >> 1), (n >> 1), boards)
                stars(row + (n >> 1), col - (n >> 1), (n >> 1), boards)
                n >>= 1


n = int(input())
boards = [[' '] * (2 * n - 1) for _ in range(n)]
# stars(0, n, 0, 2 * n - 1, boards)
# stars(0, 0, n, 2 * n - 1, boards)
stars(0, n - 1, n, boards)
for board in boards:
    print(''.join(board))
