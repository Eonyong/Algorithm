def solution(citations):
    answer = 0
    N = max(citations)
    for i in range(N):
        cite = 0
        for c in citations:
            if c >= i:
                cite += 1
        if cite >= i and len(citations) - cite <= i and i > answer:
            answer = i
    return answer