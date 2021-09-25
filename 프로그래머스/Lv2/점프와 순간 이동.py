def solution(n):
    ans = 1 # 최소 출발 지점에서 시작이므로 1을 더해줌

    # n의 값이 1보다 클 때까지 값을 처리
    while n > 1:
        # n이 홀수일 경우, 1만큼 이동 한 뒤 2로 나누어 줌
        # 1만큼 이동 했기 때문에 ans에 1을 추가
        if n % 2:
            n = (n - 1) // 2
            ans += 1
        # n이 짝수일 경우, 그냥 값을 나눠줌
        else:
            n //= 2
    return ans