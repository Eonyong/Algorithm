def linked(i, links, computers, n, cnt):
    links[i] = cnt
    for idx in range(n):
        if idx != i and computers[i][idx] and not links[idx]:
            links[idx] = cnt
            linked(idx, links, computers, n, cnt)

def solution(n, computers):
    cnt = 0
    links = [0] * n
    for i in range(n):
        if not links[i]:
            cnt += 1
            linked(i, links, computers, n, cnt)
            
    return cnt
