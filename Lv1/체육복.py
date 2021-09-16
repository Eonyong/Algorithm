def solution(n, lost, reserve):
    student = [1] * n
    answer = 0
    
    for i in lost:
        student[i - 1] -= 1
    for i in reserve:
        student[i - 1] += 1
    
    for who in range(len(student) - 1):
        if (student[who] == 0) &( student[who + 1] > 1):
            student[who] = 1
            student[who + 1] = 1
        elif (student[who] > 1) & ( student[who + 1] == 0):
            student[who] = 1
            student[who + 1] = 1
        
    for val in student:
        if val > 0:
            answer += 1
    
    return answer