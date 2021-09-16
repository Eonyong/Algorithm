def solution(n):
    answer = 0
    triple = []
    while n>=3:
        n, tri= divmod(n, 3)
        triple.append(tri)
    else:
        triple.append(n)
        
    triple.reverse()
    for idx in range(len(triple)):
        answer += triple[idx] * 3 ** idx
    return answer