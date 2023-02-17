import sys
from collections import deque

input = sys.stdin.readline


def GoToFloor(f, s, g, u, d, visited):
    queue = deque()
    queue.append(s)
    visited[s] = 0
    while queue:
        start = queue.popleft()
        if start == g:
            return visited[g]
        for val in [u, -d]:
            if 0 < start + val <= f and visited[start + val] == float('inf'):
                visited[start + val] = visited[start] + 1
                queue.append(start + val)
    return visited[g]


f, s, g, u, d = map(int, input().split())
answer = GoToFloor(f, s, g, u, d, [float('inf') for _ in range(f + 1)])
if answer == float('inf'):
    print('use the stairs')
else:
    print(answer)
