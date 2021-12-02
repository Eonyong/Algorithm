def bfs(row, col, array, cases):
    for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ni, nj = row + i, col + j
        if 0 <= ni < N and 0 <= nj < N and L <= abs(array[row][col] - array[ni][nj]) <= R and not cases[ni][nj]:
            cases[ni][nj] = cases[row][col]
            bfs(ni, nj, array, cases)
    return array, cases


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
case = [[0] * N for _ in range(N)]
cnt = 1

for row in range(N):
    for col in range(N):
        if not case[row][col]:
            case[row][col] = cnt
            cnt += 1
            arr, case = bfs(row, col, arr, case)

if cnt - 1 == N**2:
    print(0)