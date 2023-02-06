import sys
from collections import deque

input = sys.stdin.readline

boards = [list(input().rstrip()) for _ in range(12)]
answer = 0


def BFS(row, col, boards):
    queue = deque()
    queue.append((row, col))
    visited = [[False for _ in range(6)] for _ in range(12)]
    visited[row][col] = True
    tmp = [(row, col)]
    while queue:
        r, c = queue.popleft()
        for j, i in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nj, ni = r + j, c + i
            if 0 <= nj < 12 and 0 <= ni < 6 and not visited[nj][ni] and boards[row][col] == boards[nj][ni]:
                tmp.append((nj, ni))
                visited[nj][ni] = True
                queue.append((nj, ni))

    if len(tmp) >= 4:
        for y, x in tmp:
            boards[y][x] = '.'
        return True
    return False


while True:
    flag = False
    for row in range(11, -1, -1):
        for col in range(6):
            if boards[row][col] != '.':
                if BFS(row, col, boards):
                    flag = True

    if flag:
        answer += 1
        for col in range(6):
            cnt, row = 0, 11
            while row >= 0:
                if boards[row][col] == '.':
                    cnt += 1
                else:
                    boards[row + cnt][col], boards[row][col] = boards[row][col], boards[row + cnt][col]
                    row += cnt
                    cnt = 0
                row -= 1
    else:
        break

print(answer)
