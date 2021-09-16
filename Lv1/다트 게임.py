def solution(dartResult):
    answer = 'pow('
    darts = []
    for di in dartResult:
        if di.isdigit() and ('D' in answer or 'S' in answer or 'T' in answer):
            darts.append(answer)
            answer = 'pow('
            answer += di
        else:
            answer += di
    else:
        darts.append(answer)
    
    for idx in range(len(darts)):
        
        if 'S' in darts[idx]:
            darts[idx] = darts[idx].replace('S', ', 1)')
        
        elif 'D' in darts[idx]:
            darts[idx] = darts[idx].replace('D', ', 2)')
        
        else:
            darts[idx] = darts[idx].replace('T', ', 3)')
        
        if '*' in darts[idx]:
            if idx:
                darts[idx] += '2'
                darts[idx - 1] += '*2'
            else:
                darts[idx] = darts[idx].replace('*', '*2', 1)
        
        if '#' in darts[idx]:
            darts[idx] = darts[idx].replace('#', '*(-1)')
    
    answer = eval('+'.join(darts))
            
    return answer