from itertools import combinations

N, M = map(int, input().split())
# 배달 받을 장소와 치킨집을 정장할 리스트
house, chickens = [], []
answer = 100000000
# 값을 읽으면ㅅ 치킨집과 배당 장소를 저장합니다
for row in range(N):
    arr = list(map(int, input().split()))
    for col in range(N):
        if arr[col] == 1:
            house.append([row, col])
        if arr[col] == 2:
            chickens.append([row, col])

# 많은 치킨집 중 M개의 치킨집으 선택해야 하므로 combination을 이용하여 경우의 수를 만듭니다.
for chicken in combinations(chickens, M):
#     선택된 경우으 수으 경로 합을 저장하기 위하 변수
    total = 0
    for r, c in house:
#       각 배달장소에서 치킨지 거리 주 가자 가까운 점포와의 거리 저장할 원소
        distance = N ** 2
        for s, e in chicken:
            distance = abs(s - r) + abs(e - c) if distance >= abs(s - r) + abs(e - c) else distance
        total += distance
#         전체 경로의 합이 answer보다 작을 경우 answer에 저장
    if answer > total:
        answer = total
#       출력
print(answer)
