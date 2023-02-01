from collections import defaultdict

def solution(weights):
    answer = 0
    
    w_list = []
    w_dict = defaultdict(int)
    
    for weight in weights:
        if not w_dict[weight]:
            w_dict[weight] = 1
            w_list.append(weight)
        else:
            answer += w_dict[weight]
            w_dict[weight] += 1
    
    w_list.sort()
    n = len(w_list)
    
    for l_idx in range(n - 1):
        for r_idx in range(l_idx + 1, n):
            right, left = w_list[r_idx], w_list[l_idx]
            if right / left in [4 / 3, 4 / 2, 3 / 2, 1]:
                answer += w_dict[right] * w_dict[left]
            
    return answer