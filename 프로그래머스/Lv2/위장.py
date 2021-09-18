def solution(clothes):
    answer = 1
    fashion = {}
    for val, key in clothes:
        if key not in fashion.keys():
            fashion[key] = 1
        else:
            fashion[key] += 1
            
    for value in fashion.values():
        answer *= (value + 1)
    
    return answer - 1