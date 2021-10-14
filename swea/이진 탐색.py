def f(target, l, r, flag):
    global cnt
    # 중간값 설정
    length = (l + r) // 2

    if l <= r:
        # target 값을 찾았으면 cnt의 값 증가
        if target == A[length]:
            cnt += 1
        # 이전과 다르게 target 값이 더 크면 실행
        elif target > A[length] and flag != 1:
            f(target, length + 1, r, 1)
        # 이전과 다르게 target 값이 더 작으면 실행
        elif target < A[length] and flag != -1:
            f(target, l, length - 1, -1)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for tar in B:
        f(tar, 0, N - 1, 0)
    print(f'#{tc} {cnt}')