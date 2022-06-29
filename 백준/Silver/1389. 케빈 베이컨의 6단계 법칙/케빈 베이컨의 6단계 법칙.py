n, m = map(int, input().split())
users = [[] for _ in range(n + 1)]
distance, member = float('inf'), 0

for _ in range(m):
    s, e = map(int, input().split())
    users[s].append(e)
    users[e].append(s)

for s in range(1, n + 1):
    visited = [0 for _ in range(n + 1)]
    visited[s] = 1
    user = users[s][:]
    cnt = 1
    while user:
        next_visit = []
        for u in user:
            if not visited[u]:
                visited[u] = cnt
                if users:
                    for end in users[u]:
                        if not visited[end] and s != end:
                            next_visit.append(end)
        user = next_visit[:]
        cnt += 1
    if distance > sum(visited) - visited[s]:
        distance = sum(visited) - visited[s]
        member = s
    elif distance == sum(visited) - visited[s] and member > s:
        member = s
print(member)
