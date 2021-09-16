def solution(x, n):
    answer = []
    for multiple in range(1, n+1):
        answer.append(x * multiple)
    return answer