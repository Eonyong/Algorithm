def solution(w, h):
    answer = 0
    # 테스트 12 번의 경우, 아래의 조건문을 안해주니 시간초과가 발생
    # 아마 엄청나게 큰 정사각형을 케이스로 넣은 듯 함
    if w == h:
        return w * h - w
    
    else:

        m = min(w, h)   # 조건문을 돌기 전에 가로와 세로 중 작은 부분을 선택한다.
        # 꼭지점을 기준으로 직선을 그어 각 값의 절대값을 answer에 추가
        # P.S.)변수를 나중에 곱하는 경우 소수정 때문에 6번 케이스에서 에러가 발생할 수 있음

        # 가로가 작은 경우
        if m == w:
            for n in range(w):
                answer += int(h * n / w)    

        # 세로가 작은 경우
        else:
            for n in range(h):
                answer += int(w * n / h)

        return answer * 2