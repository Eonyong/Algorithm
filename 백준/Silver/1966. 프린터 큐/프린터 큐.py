import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    boards = list(map(int, input().split()))
    boards_tf = [False for _ in range(n)]   # 해당 인덱스에 대해 프린트 유무 판단
    maxval = sorted(boards) # 출력해야 되는 가장 큰 수를 확인하기 위한 리스트
    idx, cnt = 0, 0
    # 우리가 타겟팅하는 인덱스가 출력되기 전까지 해당 작업을 수행
    while not boards_tf[m]:
        if not boards_tf[idx] and maxval[-1] == boards[idx]:    # 우리가 프린트 해야하는 최댓값이랑 같고 해당 인덱스가 출력 되지 않은 경우
            boards_tf[idx] = True
            maxval.pop()
            cnt += 1
        idx = (idx + 1) % n
    print(cnt)