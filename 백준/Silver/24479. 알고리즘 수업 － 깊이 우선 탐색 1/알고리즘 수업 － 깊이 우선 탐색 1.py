import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def DFS(start, nodes, visited):
    global count
    for middle in nodes[start]:
        if visited[middle] == 0:
            count += 1
            visited[middle] = count
            DFS(middle, nodes, visited)


n, m, r = map(int, input().split())
nodes = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
count = 1

for _ in range(m):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)

for idx in range(1, n + 1):
    nodes[idx].sort()

visited[r] = count
DFS(r, nodes, visited)
for visit in visited[1:]:
    print(visit)
