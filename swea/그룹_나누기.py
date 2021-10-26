def find_set(x, rep):
  
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y, rep):
    rep[find_set(y, rep)] = find_set(x, rep)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    friends = list(map(int, input().split()))
    teams = list(range(N + 1))
    cnt = 0
    for i in range(0, len(friends), 2):
        union(friends[i], friends[i + 1], teams)
    for k in range(1, N + 1):
        if teams[k] == k:
            cnt += 1

    print(f'#{tc} {cnt}')