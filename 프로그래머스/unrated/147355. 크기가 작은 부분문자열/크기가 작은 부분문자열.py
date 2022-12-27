def solution(t, p):
    answer = 0
    n, m = len(t), len(p)
    for idx in range(n - m + 1):
        if int(t[idx:idx + m]) <= int(p):
            answer += 1
    return answer