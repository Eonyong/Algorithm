import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
boards = [list(map(int, list(input().rstrip()))) for _ in range(n)]
routes = [[0 for _ in range(m)] for _ in range(n)]
position = deque([[0, 0]])
while position:
    r, c = position.popleft()
    for j, i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nj, ni = r + j, c + i
        if 0 <= nj < n and 0 <= ni < m and boards[nj][ni] and not routes[nj][ni]:
            routes[nj][ni] = routes[r][c] + 1
            position.append([nj, ni])
print(routes[-1][-1] + 1)