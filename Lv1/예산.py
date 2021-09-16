def solution(d, budget):
    answer = 0
    execution = 0
    
    d = sorted(d, reverse=True)
    
    while True:
        if d:
            execution += d.pop()
        
            if execution <= budget:
                answer += 1
            else:
                return answer
            
        else:
            return answer