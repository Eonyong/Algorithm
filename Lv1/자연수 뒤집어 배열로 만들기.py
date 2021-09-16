def solution(n):
    answer = []
    for num in str(n):
        answer.insert(0, int(num))
    return answer