import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cnt = 0
visited = [False for _ in range(n + 1)]
q = deque()
q.append((n, [n], 0))
while q:
    number, routes, cnt = q.popleft()
    if number == 1:
        print(cnt)
        print(*routes)
        break
    for j in [3, 2]:
        if not visited[number // j] and not number % j:
            num = number // j
            q.append((num, routes + [num], cnt + 1))
            visited[num] = True
    num = number - 1
    if not visited[num]:
        visited[num] = True
        q.append((num, routes + [num], cnt + 1))
