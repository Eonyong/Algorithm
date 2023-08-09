import sys
from collections import deque

input = sys.stdin.readline


def Apartments(row, col, n, visited, boards):
    queue = deque([[row, col]])
    cnt = 1
    visited[row][col] = True
    while queue:
        r, c = queue.popleft()
        for j, i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nj, ni = r + j, c + i
            if 0 <= nj < n and 0 <= ni < n and not visited[nj][ni] and boards[nj][ni]:
                visited[nj][ni] = True
                queue.append([nj, ni])
                cnt += 1
    return cnt


n = int(input())
visited = [[False for _ in range(n)] for _ in range(n)]
boards = [list(map(int, list(input().rstrip()))) for _ in range(n)]
counts = []
for y in range(n):
    for x in range(n):
        if not visited[y][x] and boards[y][x]:
            counts.append(Apartments(y, x, n, visited, boards))
counts.sort()
print(len(counts))
for count in counts:
    print(count)