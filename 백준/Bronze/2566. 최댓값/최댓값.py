import sys
input = sys.stdin.readline

row, col, max_val = 0, 0, -1
for r in range(9):
    ls = list(map(int, input().split()))
    tmp = ls.index(max(ls))
    if ls[tmp] > max_val:
        max_val = max(max_val, ls[tmp])
        row, col = r + 1, tmp + 1
print(max_val)
print(row, col)

