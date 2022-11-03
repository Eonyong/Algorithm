import sys
from collections import deque

input = sys.stdin.readline


for _ in range(int(input())):
    n, m = map(int, input().split())
    spend_times = list(map(int, input().split()))
    nodes = [[] for _ in range(n)]
    leaves = [0 for _ in range(n)]
    for _ in range(m):
        s, e = map(int, input().split())
        nodes[s - 1].append(e - 1)
        leaves[e - 1] += 1
    goal = int(input()) - 1
    times = [0 for _ in range(n)]
    soonseo = deque()
    for idx in range(n):
        if leaves[idx] == 0:
            soonseo.append(idx)
            times[idx] = spend_times[idx]
    while soonseo:
        t = soonseo.popleft()
        for value in nodes[t]:
            leaves[value] -= 1
            if leaves[value] == 0:
                soonseo.append(value)
            times[value] = max(times[value], times[t] + spend_times[value])
    print(times[goal])