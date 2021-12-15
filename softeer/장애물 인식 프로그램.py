def BFS(r, c, arr, n):
    global answer
    arr[r][c] = 0
    for i, j in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        ni, nj = r + i, c + j
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == '1':
            answer += 1
            BFS(ni, nj, arr, n)


N = int(input())

arr = [list(input()) for _ in range(N)]
box = []

for row in range(N):
    for col in range(N):
        if arr[row][col] == '1':
            answer = 1
            BFS(row, col, arr, N)
            box.append(answer)

box.sort()

print(len(box))
for idx in range(len(box)):
    print(box[idx])