def dijkstra(s, V):
    u = [0] * (V + 1)  # 비용이 결정된 정점을 표시
    u[s] = 1  # 출발점 비용 결정
    for i in range(V + 1):
        D[i] = adj[s][i]

    # 남은 정점의 비용 결정
    for _ in range(V):  # 남은 정점 개수만큼 반복
        # D[w]가 최소인 w 결정. 비용이 결정되지 않은 정점 w 중에서
        minV = inf
        w = 0
        for i in range(V + 1):
            if not u[i] and minV > D[i]:
                minV = D[i]
                w = i
        u[w] = 1  # 비용 결정
        for v in range(V + 1):
            if 0 < adj[w][v] < inf:
                D[v] = min(D[v], D[w] + adj[w][v])


for tc in range(1, int(input()) + 1):
    inf = 1000
    V, E = map(int, input().split())
    adj = [[inf] * i + [0] + [inf] * (V - i) for i in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    D = [0] * (V+1)
    dijkstra(0, V)
    print(f'#{tc} {D[-1]}')