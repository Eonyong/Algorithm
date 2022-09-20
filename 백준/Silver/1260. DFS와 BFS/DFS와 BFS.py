import sys
from collections import deque
input = sys.stdin.readline


# DFS
def DFS(start, nodes, visited):
    global routes
    # 현재 노드에서 탐색할 경로 중에서 방문 하지 않는 노드를 추가하고 이동
    for node in nodes[start]:
        if not visited[node]:
            visited[node] = True
            routes.append(node)
            DFS(node, nodes, visited)


# BFS, 사전준비
def BFS(start, nodes):
    # deque을 이용해 탐색한 노드의 값을 저장
    tracks = deque([start])
    answer = [start]
    # 방문 하지 않는 노드를 answer에 추가하고 이동
    visit = [False for _ in range(n + 1)]
    visit[start] = True
    # tracks에 노드가 존재하지 않을때까지 loop
    while tracks:
        s = tracks.popleft()
        # DFS와 마찬가지로 현재 노드에서 갈 수 있는 경로 중 방문하지 않는 node를 answer에 추가
        for end in nodes[s]:
            if not visit[end]:
                visit[end] = True
                answer.append(end)
                tracks.append(end)
    return answer   # 전부 다 돌았으면 answer를 반환


n, m, v = map(int, input().split())
nodes = {i: set() for i in range(n + 1)}

for _ in range(m):
    s, e = map(int, input().split())
    nodes[s].add(e)
    nodes[e].add(s)

# 해당 문제는 node가 방문할 장소를 오름차순으로 해야 엣지케이스에 걸리지 않음
nodes = {key: sorted(val) for key, val in nodes.items()}

# DFS 사전 준비, 경로에 시작하는 node를 넣어주고 여기에 쌓아나간다.
routes = [v]
visited = [False for _ in range(n + 1)]  # 방문 확인 노드
visited[v] = True
DFS(v, nodes, visited)
print(*routes)

# BFS 시작
print(*BFS(v, nodes))
