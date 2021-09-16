def solution(n):
    answer = 0
    # 반복문을 진행하여 n에 나누어떨어지면 약수이므로 그 값을 answer에 더해준다.
    for i in range(1, n + 1):
        if not n % i:
            answer += i
    return answer