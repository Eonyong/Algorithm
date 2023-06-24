def solution(n, m, section):
    answer = 0
    walls = [True for _ in range(n + 1)]
    for sec in section:
        walls[sec] = False
    
    idx = 1
    while idx < n + 1:
        if not walls[idx]:
            idx += m
            answer += 1
        else:
            idx += 1
    
    return answer