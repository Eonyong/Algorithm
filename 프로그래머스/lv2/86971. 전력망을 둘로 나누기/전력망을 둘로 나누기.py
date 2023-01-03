from collections import deque, defaultdict

def Fuck(n, arr, visited):
    global answer
    q, m = deque(), defaultdict(int)
    for idx in range(1, n + 1):
        if visited[idx] == -1:
            m[idx] += 1
            q.append(idx)
            visited[idx] = idx
            while q:
                val = q.popleft()
                for j in arr[val]:
                    if visited[j] == -1:
                        m[idx] += 1
                        visited[j] = visited[val]
                        q.append(j)
    m = m.values()
    answer = min(answer, max(m) - min(m))
    

def solution(n, wires):
    global answer
    answer = float('inf')
    
    for i in range(n - 1):
        nodes = [[] for _ in range(n + 1)]
        visited = [-1 for _ in range(n + 1)]
        for j in range(n - 1):
            if i != j:
                s, e = wires[j]
                nodes[s].append(e)
                nodes[e].append(s)
        Fuck(n, nodes, visited)
    
    return answer