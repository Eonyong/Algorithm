import sys
from collections import deque
input = sys.stdin.readline


def DFS(start, nodes, visited):
    global routes
    for node in nodes[start]:
        if not visited[node]:
            visited[node] = True
            routes.append(node)
            DFS(node, nodes, visited)


def BFS(start, nodes):
    tracks = deque([start])
    answer = [start]
    visit = [False for _ in range(n + 1)]
    visit[start] = True
    while tracks:
        s = tracks.popleft()
        for end in nodes[s]:
            if not visit[end]:
                visit[end] = True
                answer.append(end)
                tracks.append(end)
    return answer


n, m, v = map(int, input().split())
nodes = {i: set() for i in range(n + 1)}

for _ in range(m):
    s, e = map(int, input().split())
    nodes[s].add(e)
    nodes[e].add(s)

nodes = {key: sorted(val) for key, val in nodes.items()}

routes = [v]
visited = [False for _ in range(n + 1)]
visited[v] = True
DFS(v, nodes, visited)
print(*routes)
print(*BFS(v, nodes))
