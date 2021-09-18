def solution(progresses, speeds):
    answer = []
    count = 0
    while progresses:
        
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count:
                answer.append(count)
                count = 0
            progresses = [a + b for a, b in zip(progresses, speeds)]
            
    answer.append(count)
    
    return answer