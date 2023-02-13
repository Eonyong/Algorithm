import sys
import heapq

input = sys.stdin.readline


def Dijkstra(middle, nodes, distances):
    queue = []
    heapq.heappush(queue, (0, middle))

    while queue:
        cost, node = heapq.heappop(queue)

        if cost > distances[node]:
            continue

        for end, weight in nodes[node]:
            if distances[end] > distances[node] + weight:
                distances[end] = distances[node] + weight
                heapq.heappush(queue, (distances[end], end))

    return distances[1:n + 1]


n, m = map(int, input().split())
start = int(input())
nodes = [[] for _ in range(n + 1)]
distances = [float('inf') for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    nodes[s].append([e, w])

distances[start] = 0
visited[start] = True

for distance in Dijkstra(start, nodes, distances):
    if distance == float('inf'):
        print("INF")
    else:
        print(distance)
