from collections import deque


def boundary(val, N):
    if val < 0:
        return N - abs(val) % N if abs(val) % N else 0
    else:
        return val % N


def rainyday(clouds, baskets, d_s, N):
    directions = {1: [0, -1], 2: [-1, -1], 3: [-1, 0], 4: [-1, 1], 5: [0, 1], 6: [1, 1], 7: [1, 0], 8: [1, -1]}
    d, s = d_s.popleft()
    yy, xx = directions[d] # y, x
    for idx in range(len(clouds)):
        y, x = clouds[idx]
        y, x = boundary(y + yy * s, N),boundary(x + xx * s, N)
        baskets[y][x] += 1
        for j, i in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
            x1, y1 = x + i, y + j
            if 0 <= y1 < N and 0 <= x1 < N and baskets[y1][x1] > 0:
                baskets[y][x] += 1
        clouds[idx] = [y, x]
    return baskets, d_s, clouds


N, M = map(int, input().split())
baskets = [list(map(int, input().split())) for _ in range(N)]
rains = deque(list(map(int, input().split())) for _ in range(M))
baskets, rains, cloud = rainyday([[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]], baskets, rains, N)
print(baskets)
while rains:
    clouds = []
    for row in range(N):
        for col in range(N):
            if baskets[row][col] > 1 and [row, col] not in cloud:
                clouds.append([row, col])
                baskets[row][col] -= 2
    print(baskets)
    baskets, rains, cloud = rainyday(clouds, baskets, rains, N)

answer = 0
for row in range(N):
    for col in range(N):
        answer += baskets[row][col]
print(answer)