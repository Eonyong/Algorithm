def clean(row, col, d, arr):
    if 0 < col < N and d == 0:
        if arr[row][col - 1]:
            col -= 1
            arr[row][col - 1] = 0
            return row, col - 1, d, arr
        elif not arr[row][col - 1]:
            return row, col, (d - 1) % 4, arr
        elif row < N - 1 and (not col or (not arr[row - 1][col] and not arr[row + 1][col] and not arr[row][col - 1] and not arr[row][col + 1])):
            return row + 1, col, d, arr

    elif 0 < row < N and d == 1:
        if arr[row - 1][col]:
            row -= 1
            arr[row - 1][col] = 0
            return row - 1, col, d, arr
        elif not arr[row - 1][col]:
            return row, col, (d - 1) % 4, arr
        elif col > 0 and (not row or (not arr[row - 1][col] and not arr[row + 1][col] and not arr[row][col - 1] and not arr[row][col + 1])):
            return row + 1, col, d, arr

N, M = map(int, input().split())
row, col, d = map(int, input().split())
floors = [list(map(int, input().split())) for _ in range(N)]

while True:
    d = (d - 1) % 4