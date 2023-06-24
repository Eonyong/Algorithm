from collections import defaultdict

def solution(topping):
    answer = 0
    n = len(topping)
    left, right = defaultdict(int), defaultdict(int)
    
    left[topping[0]] = 1
    l_cnt, r_cnt = 1, 0
    
    for idx in range(1, n):
        right[topping[idx]] += 1
    r_cnt = len(right.keys())
    
    if l_cnt == r_cnt:
        answer += 1
        
    for idx in range(1, n - 1):
        top = topping[idx]
        if not left[top]:
            l_cnt += 1
        left[top] += 1
        right[top] -= 1
        if not right[top]:
            r_cnt -= 1
        if l_cnt == r_cnt:
            answer += 1
        
    return answer