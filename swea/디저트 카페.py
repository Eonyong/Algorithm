for tc in range(1, int(input()) + 1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    # 대각선 사각형의 범위를 구해서 미리 사각형을 만드는 작업
    for r in range(N - 2):
        for c in range(1, N - 1):
            # 시작 방향에서 오른쪽 아래로 이동하는 중에 오른쪽 벽에 먼저 닿는지, N - 2층에 먼저 닿는지 결정한다.
            # 이를 통해 오른쪽 대각선이 갈 수 있는 최대 길이가 결정된다.
            R = min(N - 2 - r, N - 1 - c)   
            for j in range(1, R + 1):
                # 이제 시작 방향에서 왼쪽 아래 방향으로 이동하여 왼쪽 벽에 먼저 닿는 것과 j만큼 내려간 지점에서 가장 아래 단면과
                # 닿는 부분이 먼저 도착하는 지 비교하여 최솟값을 결정한다.
                # 이를 통해 왼쪽 대각선의 길이를 결정할 수 있다.
                L = min(N - (r + j + 1), c)
                # 이제 각 방향의 대각선이 갈 수 있는 최대 길이를 정했으니 그 범위 안에 존재하는 대각선 사각형의 모양을 다 그린다.
                for i in range(1, L + 1):
                    # 하나씩 늘려가며 모양을 그리고 이를 stack이라는 리스트에 저장하는데
                    # [row, col, 사각형 둘레의 길이(지나가는 카페의 지점의 수), 왼 대각선의 길이, 오른 대각선의 길이]순으로 저장
                    stack.append([r, c, (i + j) * 2, i, j])
    # 전부 저장한 다음, 거치는 카페의 수가 최대가 되는 것을 구하는 것이므로 지나는 카페 지점의 수를 기준으로 정렬
    # pop을 이용할 예정이므로 오름차순으로 정렬
    stack.sort(key=lambda x: x[2])
 
    # 모든 stack을 확인
    while stack:
        # 거쳐간 카페의 번호를 저장
        answer = []
        # 각 값을 알기 쉬운 변수에 저장
        row, col, ans, left, right = stack.pop()
        # 가장 먼저 처음 출발하는 지접의 카페 번호를 저장
        answer.append(cafes[row][col])
        # 한 번에 계산하기 위해 하나 더 만들어 준다
        rrow, ccol = row, col
         
        # 일단, 왼쪽으로 가면서 값을 저장
        for _ in range(left):
            rrow, ccol = rrow + 1, ccol - 1
            answer.append(cafes[rrow][ccol])
 
        # 이번에 오른쪽 아래로 내려가며 저장하는데 두 변을 한번에 하기 위해
        # row, col 과 rrow, ccol을 동시에 진행
        for _ in range(right):
            row, col = row + 1, col + 1
            rrow, ccol = rrow + 1, ccol + 1
            answer.append(cafes[row][col])
            answer.append(cafes[rrow][ccol])
 
        # 마지막으로 남아있는 나머지 변에 있는 카페의 번호를 저장
        for _ in range(left - 1):
            row, col = row + 1, col - 1
            answer.append(cafes[row][col])
 
        # 저장한 카페 중에 중복된 것이 없으면 test case와 둘레의 길이를 출력
        if len(set(answer)) == ans:
            print(f'#{tc} {ans}')
            break
    # 다 돌았는데도 답이 안나온다면 test case와 -1을 출력
    else:
        print(f'#{tc} -1')