def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + 2 * heapq.heappop(scoville))
        answer += 1
        
    return answer