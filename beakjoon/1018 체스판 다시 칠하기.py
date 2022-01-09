rows, cols = map(int, input().split())
arr = [list(input()) for _ in range(rows)]
answer = 64

for row in range(rows - 7):
    for col in range(cols - 7):
        w_cnt, b_cnt = 0, 0
        for i in range(row, row + 8):
            for j in range(col, col + 8):
                if not (i + j) % 2:
                    if arr[i][j] == 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else:
                    if arr[i][j] == 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
        answer = min(w_cnt, b_cnt, answer)

print(answer)