def solution(sizes):
    answer = 0
    x, y = 0, 0 # 각 값을 초기화

    # for문을 돌면서 x, y의 최댓값을 저장합니다.
    for i, j in sizes:
        if i > x:
            x = i
        if j > y:
            y = j
    
    # 만약 x의 최댓값이 더 크면 가로, 세로 중 큰 값을 전부 x에 옮긴 후
    if x > y:
        y = 0
        for idx in range(len(sizes)):
            if sizes[idx][0] < sizes[idx][1]:
                sizes[idx] = [sizes[idx][1], sizes[idx][0]]
            # 작은 값들 중 가장 큰 값을 y에 대입
            if sizes[idx][1] > y:
                y = sizes[idx][1]
    # 만약 ㅛ의 최댓값이 더 크면 가로, 세로 중 큰 값을 전부 ㅛ에 옮긴 후
    else:
        x = 0
        for idx in range(len(sizes)):
            if sizes[idx][1] < sizes[idx][0]:
                sizes[idx] = [sizes[idx][1], sizes[idx][0]]
            # 작은 값들 중 가장 큰 값을 x에 대입
            if sizes[idx][0] > x:
                x = sizes[idx][0]
    # 해당 곱을 반환
    return x * y