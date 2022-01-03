N = int(input())
players = [list(map(int, input().split())) for _ in range(N)]
arr = []

for a in range(N):
    cnt = 1
    for b in range(N):
        if players[a][0] < players[b][0] and players[a][1] < players[b][1]:
            cnt += 1
    arr.append(cnt)

print(*arr)