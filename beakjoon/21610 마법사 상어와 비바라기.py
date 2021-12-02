# d, s가 정해졌을 때 범위 안에서 움직이도록 만드는 함수
def moves(val, direction, sep, n):
    val = val + direction * sep
    if val < 0:
        return -1 * abs(val) % n
    else:
        return val % n

# 대각선의 값을 보고 true이면 1을 증가 시키는 함수
def crossVal(ls, n, arr):
    for row, col in ls:
        for j, i in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
            x, y = col + i, row + j
            if 0 <= x < n and 0 <= y < n and arr[y][x] > 0:
                arr[row][col] += 1
    else:
        return arr

# 구름이 다 돌고 난 후 해당 구름을 제외하고 값이 2이상인 구름을
# 2 감소시키고 리스트에 저장하는 함수
def extraClouds(arr, container, n):
    visit = [[False] * n for _ in range(n)]
    boxes = []
    for row in range(n):
        for col in range(n):
            if arr[row][col] >= 2 and not container[row][col]:
                arr[row][col] -= 2
                visited[row][col] = True
                boxes.append([row, col])
    return arr, visit, boxes

# 입력을 받음
N, M = map(int, input().split())
clouds = [list(map(int, input().split())) for _ in range(N)]
directions = [list(map(int, input().split())) for _ in range(M)]
# 최초 시작이 문제에 주어져 있으므로 아래와 같이 지정
rain = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
# d의 값에 따라 index 1부터 9시방향에서 시계방향으로 이동 방향 설정
x_dir, y_dir = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, -1, -1, -1, 0, 1, 1, 1]
# 방문한 곳인지 표시하는 2차원 리스트
visited = [[False] * N for _ in range(N)]

# 각 이동 명령에따라 구름을 움직임
for d, s in directions:
    # 구름의 수만큼 구름을 이동시켜 준다.
    for rain_idx in range(len(rain)):
        y, x = rain[rain_idx][0], rain[rain_idx][1]
        y, x = moves(y, y_dir[d], s, N), moves(x, x_dir[d], s, N)
        # 이동한 구름의 위치를 update하고 1증가, 방문 표시
        rain[rain_idx] = [y, x]
        clouds[y][x] += 1
        visited[y][x] = True
    # 해당 위치에서 대각선 방향의 물을 보고 0이상이면 1 추가하는 함수 실행후
    # clouds 업데이트
    clouds = crossVal(rain, N, clouds)
    # 또다른 구름들을 업데이트
    clouds, visited, rain = extraClouds(clouds, visited, N)

# 전체 값의 합을 구하는 부분
answer = 0
for row in range(N):
    for col in range(N):
        answer += clouds[row][col]

print(answer)
