N, M = map(int, input().split())

tetris = {0: [[0, 1], [0, 2], [0, 3]],
          1: [[0, 1], [1, 0], [1, 1]],
          2: [[1, 0], [2, 0], [2, 1]],
          3: [[1, 0], [2, 0], [2, -1]],
          4: [[1, 0], [1, 1], [2, 1]],
          5: [[1, 0], [1, -1], [2, -1]],
          6: [[0, 1], [0, 2], [1, 1]]}

board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for _ in range(4):
    board = list(zip(*board[::-1]))
    N, M = M, N

    for row in range(N):
        for col in range(M):

            for cnt in range(7):
                ans = board[row][col]
                
                for i, j in tetris[cnt]:
                    ni, nj = row + i, col + j
                    if 0 <= ni < N and 0 <= nj < M:
                        ans += board[ni][nj]
                    else:
                        break
                else:
                    if answer < ans:
                        answer = ans
print(answer)
