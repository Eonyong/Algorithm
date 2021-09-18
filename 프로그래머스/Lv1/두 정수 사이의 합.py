def solution(a, b):
    answer = 0
    if b > a:
        answer = sum(list(range(a, b+ 1)))
    else:
        answer = sum(list(range(b, a + 1)))
    return answer