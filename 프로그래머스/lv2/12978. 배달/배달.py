from collections import deque

def BFS(n, arr, visited):
    q = deque()
    q.append(1)
    while q:
        start = q.popleft()
        for end, w in arr[start]:
            if visited[start] + w < visited[end]:
                visited[end] = visited[start] + w
                q.append(end)
    return visited

def solution(N, road, K):
    answer = 0
    nodes = [[] for _ in range(N + 1)]
    visited = [float('inf') for _ in range(N + 1)]
    visited[1] = 0
    for s, e, w in road:
        nodes[s].append((e, w))
        nodes[e].append((s, w))
    visited = BFS(N, nodes, visited)
    
    for k in visited:
        if k <= K:
            answer += 1
    

    return answer